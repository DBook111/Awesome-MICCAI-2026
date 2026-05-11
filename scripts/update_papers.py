#!/usr/bin/env python3
"""Update the Awesome MICCAI README from arXiv data.

Pipeline stages:
1) Discover: fetch candidate MICCAI papers from arXiv
2) Normalize: clean and canonicalize repository links
3) Validate: reject malformed/unsupported records
4) Categorize: multi-label category + confidence assignment
5) Render: deterministically regenerate README category blocks and coverage report
"""

from __future__ import annotations

import argparse
import re
import time
from datetime import datetime, timedelta, timezone
from typing import Any, Dict, List, Optional, Pattern, Sequence, Tuple
from urllib.parse import urlparse

import arxiv


CATEGORY_ORDER = [
    "Segmentation",
    "Reconstruction",
    "Classification",
    "Image Registration",
    "Domain Adaptation",
    "Generative Models",
    "Fundus Imaging",
    "OCT",
    "OCTA",
    "Ophthalmic Foundation Models",
    "General",
]

CATEGORY_MARKERS = {
    "Segmentation": "SEGMENTATION",
    "Reconstruction": "RECONSTRUCTION",
    "Classification": "CLASSIFICATION",
    "Image Registration": "IMAGE_REGISTRATION",
    "Domain Adaptation": "DOMAIN_ADAPTATION",
    "Generative Models": "GENERATIVE_MODELS",
    "Fundus Imaging": "FUNDUS_IMAGING",
    "OCT": "OCT",
    "OCTA": "OCTA",
    "Ophthalmic Foundation Models": "OPHTHALMIC_FOUNDATION_MODELS",
    "General": "GENERAL",
}

ALLOWED_CODE_HOSTS = {"github.com", "gitlab.com", "huggingface.co"}
TRACK_OPTIONS = {"main", "workshops", "challenges", "all"}
CONFERENCE_SCOPE_OPTIONS = {"miccai-all-years"}

# (regex pattern, weight)
CATEGORY_RULES = {
    "Segmentation": [
        (r"\bsegmentation\b", 3),
        (r"\bsegment\b", 2),
        (r"\bdelineation\b", 2),
        (r"\bcontour\b", 2),
        (r"\bmask\b", 1),
        (r"\bmasking\b", 1),
    ],
    "Reconstruction": [
        (r"\breconstruction\b", 3),
        (r"\breconstruct\b", 2),
        (r"\brestoration\b", 2),
        (r"\brestore\b", 1),
        (r"\bsuper[- ]resolution\b", 2),
        (r"\bdenoising\b", 2),
    ],
    "Classification": [
        (r"\bclassification\b", 3),
        (r"\bclassify\b", 2),
        (r"\bclassifier\b", 2),
        (r"\brecognition\b", 2),
        (r"\bdetection\b", 2),
        (r"\bdiagnosis\b", 1),
    ],
    "Image Registration": [
        (r"\bregistration\b", 3),
        (r"\balignment\b", 2),
        (r"\bdeformable\b", 2),
        (r"\bdeformation\b", 2),
    ],
    "Domain Adaptation": [
        (r"\bdomain adaptation\b", 3),
        (r"\btransfer learning\b", 2),
        (r"\bcross[- ]domain\b", 2),
        (r"\bdomain shift\b", 2),
        (r"\bdomain generalization\b", 3),
        (r"\bgeneralization\b", 1),
    ],
    "Generative Models": [
        (r"\bgenerative\b", 3),
        (r"\bgeneration\b", 2),
        (r"\bsynthesis\b", 2),
        (r"\bgan\b", 2),
        (r"\bdiffusion\b", 2),
        (r"\bvae\b", 2),
        (r"\bautoencoder\b", 2),
        (r"\bflow matching\b", 2),
    ],
    "Fundus Imaging": [
        (r"\bfundus\b", 3),
        (r"\bretina(?:l)?\b", 2),
        (r"\bophthalm(?:ic|ology)\b", 2),
        (r"\boptic disc\b", 2),
        (r"\boptic cup\b", 2),
        (r"\bmacula(?:r)?\b", 2),
    ],
    "OCT": [
        (r"\boptical coherence tomography\b", 3),
        (r"\boct\b", 2),
        (r"\boct b[- ]?scan\b", 2),
        (r"\boct volume\b", 2),
        (r"\bretina(?:l)?\b", 1),
    ],
    "OCTA": [
        (r"\boptical coherence tomography angiography\b", 3),
        (r"\bocta\b", 3),
        (r"\bretinal angiography\b", 2),
        (r"\bvessel density\b", 1),
    ],
    "Ophthalmic Foundation Models": [
        (r"\bfoundation model(?:s)?\b", 2),
        (r"\bvision foundation model(?:s)?\b", 2),
        (r"\bpre[- ]?trained\b", 1),
        (r"\bfundus\b", 2),
        (r"\bretina(?:l)?\b", 2),
        (r"\bophthalm(?:ic|ology)\b", 2),
        (r"\bocta?\b", 2),
    ],
}
CATEGORY_COMPILED_RULES: Dict[str, List[Tuple[Pattern[str], int]]] = {
    category: [(re.compile(pattern), weight) for pattern, weight in rules]
    for category, rules in CATEGORY_RULES.items()
}

CATEGORY_THRESHOLDS = {
    "Segmentation": 2,
    "Reconstruction": 2,
    "Classification": 2,
    "Image Registration": 2,
    "Domain Adaptation": 2,
    "Generative Models": 2,
    "Fundus Imaging": 2,
    "OCT": 2,
    "OCTA": 2,
    "Ophthalmic Foundation Models": 3,
}

REPO_URL_PATTERN = re.compile(
    r"https?://(?:www\.)?(?:github\.com|gitlab\.com|huggingface\.co)/[^\s\]\[<>\"')]+",
    flags=re.IGNORECASE,
)

ARXIV_ABS_PATTERN = re.compile(r"^https?://arxiv\.org/abs/\d{4}\.\d{4,5}(?:v\d+)?$")
MICCAI_PATTERN = re.compile(r"\bmiccai\b", re.IGNORECASE)
MICCAI_YEAR_SCOPE_PATTERN = re.compile(r"^miccai-(20\d{2})$")
MICCAI_EXPLICIT_YEAR_PATTERN = re.compile(
    r"\bmiccai\s*[-_ ]?(?P<year>20\d{2}|'?\d{2})\b", re.IGNORECASE
)
MICCAI_SUBMISSION_PATTERN = re.compile(
    r"\b(submitted|under review|accepted|camera[- ]ready)\b.{0,32}\bmiccai\b",
    re.IGNORECASE,
)

TRACK_PATTERNS = {
    "workshops": re.compile(r"\bworkshop\b", re.IGNORECASE),
    "challenges": re.compile(r"\bchallenge\b", re.IGNORECASE),
}

SCOPE_LINE_PATTERN = re.compile(r"\*\*Conference Scope\*\*: [^\n]*")
MODE_LINE_PATTERN = re.compile(r"\*\*Discovery Mode\*\*: [^\n]*")
COVERAGE_BLOCK_PATTERN = re.compile(
    r"<!-- BEGIN COVERAGE_REPORT -->(?P<body>.*?)<!-- END COVERAGE_REPORT -->", re.S
)


def resolve_output_path(conference_scope: str, output_path: Optional[str]) -> str:
    if output_path:
        return output_path
    target_year = get_target_miccai_year(conference_scope)
    if target_year is not None:
        return f"MICCAI{target_year}.md"
    return "README.md"


def get_target_miccai_year(conference_scope: str) -> Optional[int]:
    match = MICCAI_YEAR_SCOPE_PATTERN.match(conference_scope)
    if not match:
        return None
    return int(match.group(1))


def _normalize_host(host: str) -> str:
    host = host.lower().strip()
    return host[4:] if host.startswith("www.") else host


def _clean_url_candidate(url: str) -> str:
    url = url.strip()
    url = url.split("}{", 1)[0]
    url = re.sub(r"[.,;:!?\]\}>\"'\s]+$", "", url)
    return url


def _canonical_repo_key(parsed_path: str, host: str) -> Optional[Tuple[str, str, str]]:
    segments = [segment for segment in parsed_path.split("/") if segment]
    if len(segments) < 2:
        return None

    owner = segments[0].lower()
    repo = segments[1].lower()

    blocked_owner_paths = {"orgs", "topics", "collections", "about", "search", "settings"}
    if owner in blocked_owner_paths:
        return None

    repo = repo[:-4] if repo.endswith(".git") else repo
    if not owner or not repo:
        return None

    return host, owner, repo


def normalize_repository_url(url: str) -> Optional[Tuple[str, Tuple[str, str, str]]]:
    cleaned = _clean_url_candidate(url)
    try:
        parsed = urlparse(cleaned)
    except ValueError:
        return None

    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        return None

    host = _normalize_host(parsed.netloc)
    if host not in ALLOWED_CODE_HOSTS:
        return None

    repo_key = _canonical_repo_key(parsed.path, host)
    if repo_key is None:
        return None

    canonical_url = f"https://{repo_key[0]}/{repo_key[1]}/{repo_key[2]}"
    return canonical_url, repo_key


def get_repository_links(text: str) -> List[str]:
    candidates = REPO_URL_PATTERN.findall(text or "")
    deduped: List[str] = []
    seen_keys = set()

    for candidate in candidates:
        normalized = normalize_repository_url(candidate)
        if normalized is None:
            continue
        canonical_url, repo_key = normalized
        if repo_key in seen_keys:
            continue
        seen_keys.add(repo_key)
        deduped.append(canonical_url)

    return deduped


def score_categories(title: str, abstract: str) -> Dict[str, int]:
    title_l = title.lower()
    abstract_l = abstract.lower()

    scores: Dict[str, int] = {}
    for category, rules in CATEGORY_COMPILED_RULES.items():
        score = 0
        for pattern, weight in rules:
            title_hit = pattern.search(title_l)
            abstract_hit = pattern.search(abstract_l)
            if title_hit:
                score += weight * 2
            elif abstract_hit:
                score += weight
        scores[category] = score
    return scores


def categorize_paper(title: str, abstract: str, scores: Optional[Dict[str, int]] = None) -> List[str]:
    if scores is None:
        scores = score_categories(title, abstract)
    categories = [
        category
        for category in CATEGORY_ORDER
        if category in scores and scores[category] >= CATEGORY_THRESHOLDS.get(category, 2)
    ]
    if not categories:
        categories = ["General"]
    return categories


def get_category_confidence(category_scores: Dict[str, int], categories: Sequence[str]) -> Dict[str, str]:
    confidence: Dict[str, str] = {}
    for category in categories:
        if category == "General":
            confidence[category] = "medium"
            continue
        score = category_scores.get(category, 0)
        confidence[category] = "high" if score >= 4 else "medium"
    return confidence


def _extract_arxiv_year(arxiv_url: str) -> Optional[int]:
    match = re.search(r"/abs/(\d{2})\d{2}\.\d{4,5}", arxiv_url)
    if match:
        return int(match.group(1))
    # Legacy arXiv IDs such as /abs/cs/0601001
    legacy_match = re.search(r"/abs/[a-z\-]+/(\d{2})\d{4}", arxiv_url, re.IGNORECASE)
    if legacy_match:
        return int(legacy_match.group(1))
    return None


def _extract_explicit_miccai_years(text: str) -> List[int]:
    years: List[int] = []
    for match in MICCAI_EXPLICIT_YEAR_PATTERN.finditer(text):
        value = match.group("year").replace("'", "")
        year = int(value)
        if year < 100:
            year += 2000
        years.append(year)
    return years


def _infer_track(text: str) -> str:
    if TRACK_PATTERNS["challenges"].search(text):
        return "challenges"
    if TRACK_PATTERNS["workshops"].search(text):
        return "workshops"
    return "main"


def track_matches(requested_track: str, inferred_track: str) -> bool:
    if requested_track == "all":
        return True
    return requested_track == inferred_track


def resolve_requested_track(tracks: str, exclude_non_main: bool) -> str:
    if exclude_non_main:
        return "main"
    return tracks


def is_target_miccai_paper(text: str, arxiv_url: str, mode: str, conference_scope: str) -> bool:
    target_year = get_target_miccai_year(conference_scope)
    if target_year is not None:
        explicit_years = _extract_explicit_miccai_years(text)
        if target_year in explicit_years:
            return True
        if explicit_years and target_year not in explicit_years:
            return False

        year_short = target_year % 100
        target_year_pattern = re.compile(
            rf"\bmiccai\s*[-_ ]?\s*{target_year}\b|\bmiccai(?:'{year_short:02d}|{year_short:02d})\b",
            re.IGNORECASE,
        )
        if target_year_pattern.search(text):
            return True
        if mode == "strict":
            return False
        if not MICCAI_PATTERN.search(text):
            return False
        year = _extract_arxiv_year(arxiv_url)
        if year == year_short:
            return True
        return bool(MICCAI_SUBMISSION_PATTERN.search(text))

    # miccai-all-years
    if not MICCAI_PATTERN.search(text):
        return False
    if mode == "strict":
        return bool(re.search(r"\bmiccai\s*[-_ ]?\s*20\d{2}\b", text, re.IGNORECASE))
    return True


def build_queries(mode: str, conference_scope: str) -> List[str]:
    target_year = get_target_miccai_year(conference_scope)
    if target_year is not None:
        queries = [
            f'ti:"MICCAI {target_year}"',
            f'abs:"MICCAI {target_year}"',
            f'co:"MICCAI {target_year}"',
        ]
        if mode == "broad":
            queries.extend(['ti:"MICCAI"', 'abs:"MICCAI"', 'co:"MICCAI"'])
        return queries

    # miccai-all-years
    return ['ti:"MICCAI"', 'abs:"MICCAI"', 'co:"MICCAI"']


def _is_transient_discovery_error(exc: Exception) -> Tuple[bool, str]:
    transient_status_codes = {429, 500, 502, 503, 504}
    status = getattr(exc, "status_code", None)
    if isinstance(status, int) and status in transient_status_codes:
        return True, f"HTTP {status}"

    text = str(exc)
    status_match = re.search(r"HTTP (\d{3})", text)
    if status_match:
        parsed_status = int(status_match.group(1))
        if parsed_status in transient_status_codes:
            return True, f"HTTP {parsed_status}"

    timeout_indicators = (
        "timed out",
        "timeout",
        "ReadTimeout",
        "ConnectTimeout",
        "Connection aborted",
        "Temporary failure in name resolution",
    )
    lowered = text.lower()
    if isinstance(exc, TimeoutError) or any(token.lower() in lowered for token in timeout_indicators):
        return True, "network timeout"

    return False, "non-transient error"


def discover_papers(mode: str, conference_scope: str, tracks: str) -> Tuple[List[Dict[str, Any]], Dict[str, int], List[str]]:
    print(
        "[discover] Searching arXiv "
        f"(mode={mode}, conference_scope={conference_scope}, tracks={tracks})"
    )

    queries = build_queries(mode, conference_scope)

    client = arxiv.Client(page_size=100, delay_seconds=3, num_retries=3)
    seen_arxiv = set()
    papers: List[Dict[str, Any]] = []
    failed_queries: List[str] = []
    stats = {
        "fetched_records": 0,
        "unique_arxiv_records": 0,
        "without_code_links": 0,
        "filtered_non_target": 0,
        "filtered_track": 0,
        "accepted_records": 0,
    }

    backoff_seconds = [20, 40, 80]

    for query in queries:
        print(f"[discover] Query: {query}")
        search = arxiv.Search(
            query=query,
            max_results=5000 if conference_scope == "miccai-all-years" else 300,
            sort_by=arxiv.SortCriterion.SubmittedDate,
            sort_order=arxiv.SortOrder.Descending,
        )

        results: List[Any] = []
        last_exc: Optional[Exception] = None
        for attempt in range(len(backoff_seconds) + 1):
            try:
                results = list(client.results(search))
                print(f"[discover] Results: {len(results)}")
                last_exc = None
                break
            except Exception as exc:
                last_exc = exc
                should_retry, retry_reason = _is_transient_discovery_error(exc)
                has_retry = attempt < len(backoff_seconds)
                if should_retry and has_retry:
                    wait_seconds = backoff_seconds[attempt]
                    print(
                        f"[discover] WARN: {query} hit {retry_reason}; "
                        f"retrying in {wait_seconds}s "
                        f"(attempt {attempt + 1}/{len(backoff_seconds) + 1})"
                    )
                    time.sleep(wait_seconds)
                    continue
                break

        if last_exc is not None:
            failed_queries.append(f"{query}: {last_exc}")
            print(f"[discover] ERROR: {query} failed -> {last_exc}")
            continue

        for result in results:
            stats["fetched_records"] += 1
            if result.entry_id in seen_arxiv:
                continue
            seen_arxiv.add(result.entry_id)
            stats["unique_arxiv_records"] += 1

            text = f"{result.title}\n{result.summary}\n{getattr(result, 'comment', '') or ''}"
            if not is_target_miccai_paper(text, result.entry_id, mode, conference_scope):
                stats["filtered_non_target"] += 1
                continue

            inferred_track = _infer_track(text)
            if not track_matches(tracks, inferred_track):
                stats["filtered_track"] += 1
                continue

            links = get_repository_links(text)
            if not links:
                stats["without_code_links"] += 1
                continue

            papers.append(
                {
                    "title": result.title.strip(),
                    "arxiv_url": result.entry_id.replace("http://", "https://"),
                    "repo_links": links,
                    "published": result.published,
                    "summary": result.summary,
                    "track": inferred_track,
                }
            )
            stats["accepted_records"] += 1

    return papers, stats, failed_queries


def validate_papers_data(papers: List[Dict[str, Any]]) -> Tuple[int, int, int]:
    print("[validate] Validating normalized paper records")

    deduped_papers: List[Dict[str, Any]] = []
    seen_pairs = set()
    removed_duplicates = 0
    rejected_records = 0
    uncertain_records = 0

    for paper in papers:
        arxiv_url = paper.get("arxiv_url", "")
        title = paper.get("title", "").strip()
        links = paper.get("repo_links", [])

        if not title or not ARXIV_ABS_PATTERN.match(arxiv_url):
            rejected_records += 1
            continue

        cleaned_links = []
        seen_repo_keys = set()
        for link in links:
            normalized = normalize_repository_url(link)
            if normalized is None:
                continue
            canonical_url, repo_key = normalized
            if repo_key in seen_repo_keys:
                continue
            seen_repo_keys.add(repo_key)
            cleaned_links.append(canonical_url)

        if not cleaned_links:
            rejected_records += 1
            continue

        pair_key = arxiv_url.lower()
        if pair_key in seen_pairs:
            removed_duplicates += 1
            continue

        seen_pairs.add(pair_key)
        normalized_paper = dict(paper)
        normalized_paper["repo_links"] = cleaned_links

        scores = score_categories(title, paper.get("summary", ""))
        categories = categorize_paper(title, paper.get("summary", ""), scores=scores)
        normalized_paper["category_scores"] = scores
        normalized_paper["categories"] = categories
        normalized_paper["confidence"] = get_category_confidence(scores, categories)
        normalized_paper["is_uncertain"] = (
            categories == ["General"] and max(scores.values()) < 2 if scores else True
        )
        if normalized_paper["is_uncertain"]:
            uncertain_records += 1

        deduped_papers.append(normalized_paper)

    papers[:] = deduped_papers
    print(
        "[validate] Completed: "
        f"kept={len(deduped_papers)} removed_duplicates={removed_duplicates} "
        f"rejected={rejected_records} uncertain={uncertain_records}"
    )
    return removed_duplicates, rejected_records, uncertain_records


def generate_category_markdown(papers: Sequence[Dict[str, Any]], category: str) -> str:
    category_papers = [paper for paper in papers if category in paper["categories"]]
    category_papers.sort(key=_published_sort_key)

    lines = []
    for paper in category_papers:
        title = paper["title"]
        arxiv_url = paper["arxiv_url"]
        links = paper["repo_links"]

        confidence = paper.get("confidence", {}).get(category, "medium")
        confidence_badge = f"(confidence: {confidence})"

        line = f"* **[{title}]({arxiv_url})** - [Code]({links[0]}) {confidence_badge}"
        if len(links) > 1:
            extras = [f"[Code{i + 2}]({url})" for i, url in enumerate(links[1:])]
            line += " | " + " | ".join(extras)

        lines.append(line)

    return "\n".join(lines)


def _published_sort_key(paper: Dict[str, Any]) -> Tuple[float, str]:
    published = paper["published"]
    if published.tzinfo is None:
        published = published.replace(tzinfo=timezone.utc)
    else:
        published = published.astimezone(timezone.utc)
    return (-published.timestamp(), paper["title"].lower())


def replace_category_block(content: str, marker: str, body: str) -> str:
    pattern = rf"(<!-- BEGIN {marker}_PAPERS -->).*?(<!-- END {marker}_PAPERS -->)"
    replacement = f"\\1\n{body}\n\\2" if body else f"\\1\n\\2"

    if not re.search(pattern, content, flags=re.DOTALL):
        raise ValueError(f"Missing marker block for {marker}")

    return re.sub(pattern, replacement, content, flags=re.DOTALL)


def build_coverage_report(
    papers: Sequence[Dict[str, Any]],
    stats: Dict[str, int],
    conference_scope: str,
    mode: str,
    tracks: str,
) -> str:
    category_counts = {category: len([p for p in papers if category in p["categories"]]) for category in CATEGORY_ORDER}
    total = len(papers)

    lines = [
        f"- Conference scope: `{conference_scope}`",
        f"- Discovery mode: `{mode}`",
        f"- Tracks: `{tracks}`",
        f"- Total code-backed papers: `{total}`",
        f"- Fetched arXiv records: `{stats['fetched_records']}`",
        f"- Unique arXiv records: `{stats['unique_arxiv_records']}`",
        f"- Filtered (non-target): `{stats['filtered_non_target']}`",
        f"- Filtered (track): `{stats['filtered_track']}`",
        f"- Filtered (no code links): `{stats['without_code_links']}`",
        "",
        "| Category | Count | Gap to 1000 |",
        "|---|---:|---:|",
    ]

    for category in CATEGORY_ORDER:
        count = category_counts[category]
        gap = max(0, 1000 - count)
        lines.append(f"| {category} | {count} | {gap} |")

    return "\n".join(lines)


def update_readme(
    papers: Sequence[Dict[str, Any]],
    stats: Dict[str, int],
    conference_scope: str,
    mode: str,
    tracks: str,
    readme_path: str = "README.md",
) -> Dict[str, int]:
    if readme_path != "README.md":
        try:
            with open(readme_path, "r", encoding="utf-8") as file:
                content = file.read()
        except FileNotFoundError:
            with open("README.md", "r", encoding="utf-8") as template_file:
                content = template_file.read()
    else:
        with open(readme_path, "r", encoding="utf-8") as file:
            content = file.read()

    category_counts: Dict[str, int] = {}
    for category in CATEGORY_ORDER:
        marker = CATEGORY_MARKERS[category]
        body = generate_category_markdown(papers, category)
        content = replace_category_block(content, marker, body)
        category_counts[category] = len([p for p in papers if category in p["categories"]])

    coverage_body = build_coverage_report(papers, stats, conference_scope, mode, tracks)
    coverage_match = COVERAGE_BLOCK_PATTERN.search(content)
    if coverage_match:
        content = COVERAGE_BLOCK_PATTERN.sub(
            f"<!-- BEGIN COVERAGE_REPORT -->\n{coverage_body}\n<!-- END COVERAGE_REPORT -->",
            content,
        )

    content = SCOPE_LINE_PATTERN.sub(f"**Conference Scope**: {conference_scope}", content)
    content = MODE_LINE_PATTERN.sub(f"**Discovery Mode**: {mode}", content)

    beijing_tz = timezone(timedelta(hours=8))
    timestamp = datetime.now(beijing_tz).strftime("%Y-%m-%d %H:%M 北京时间")
    content = re.sub(
        r"\*\*Last Updated\*\*: [^\n]*",
        f"**Last Updated**: {timestamp} by GitHub Actions",
        content,
    )

    with open(readme_path, "w", encoding="utf-8") as file:
        file.write(content)

    return category_counts


def main() -> int:
    parser = argparse.ArgumentParser(description="Update Awesome MICCAI list")
    parser.add_argument(
        "--mode",
        choices=["strict", "broad"],
        default="strict",
        help="Discovery strictness",
    )
    parser.add_argument(
        "--conference-scope",
        default="miccai-2026",
        help="Conference scope: miccai-all-years or miccai-<year> (e.g., miccai-2025)",
    )
    parser.add_argument(
        "--tracks",
        choices=sorted(TRACK_OPTIONS),
        default="all",
        help="Track filter",
    )
    parser.add_argument(
        "--exclude-non-main",
        action="store_true",
        help="Exclude workshop/challenge papers and keep only main-track papers",
    )
    parser.add_argument(
        "--output",
        default=None,
        help=(
            "Output markdown path. If omitted: miccai-<year> -> MICCAI<year>.md, "
            "miccai-all-years -> README.md"
        ),
    )
    args = parser.parse_args()
    if (
        args.conference_scope not in CONFERENCE_SCOPE_OPTIONS
        and get_target_miccai_year(args.conference_scope) is None
    ):
        parser.error(
            "Invalid --conference-scope. Use miccai-all-years or miccai-<year> "
            "(e.g., miccai-2025)."
        )
    requested_track = resolve_requested_track(args.tracks, args.exclude_non_main)
    output_path = resolve_output_path(args.conference_scope, args.output)

    print(
        "Starting Awesome MICCAI update "
        f"(mode={args.mode}, conference_scope={args.conference_scope}, tracks={requested_track})"
    )
    print(f"[output] Writing results to: {output_path}")

    papers, stats, failed_queries = discover_papers(args.mode, args.conference_scope, requested_track)

    if failed_queries:
        print("[discover] Failing update because one or more discovery queries failed:")
        for failure in failed_queries:
            print(f"  - {failure}")
        return 1

    removed_duplicates, rejected_records, uncertain_records = validate_papers_data(papers)
    category_counts = update_readme(
        papers,
        stats,
        args.conference_scope,
        args.mode,
        requested_track,
        readme_path=output_path,
    )

    print("[summary] Pipeline completed")
    print(f"[summary] fetched_records={stats['fetched_records']}")
    print(f"[summary] unique_arxiv_records={stats['unique_arxiv_records']}")
    print(f"[summary] without_code_links={stats['without_code_links']}")
    print(f"[summary] filtered_non_target={stats['filtered_non_target']}")
    print(f"[summary] filtered_track={stats['filtered_track']}")
    print(f"[summary] accepted_records={stats['accepted_records']}")
    print(f"[summary] deduplicated_records={removed_duplicates}")
    print(f"[summary] rejected_records={rejected_records}")
    print(f"[summary] uncertain_records={uncertain_records}")
    print("[summary] category_counts=" + ", ".join(f"{k}:{v}" for k, v in category_counts.items()))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
