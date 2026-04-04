#!/usr/bin/env python3
"""Update the Awesome MICCAI 2026 README from arXiv data.

Pipeline stages:
1) Discover: fetch candidate MICCAI 2026 papers from arXiv
2) Normalize: clean and canonicalize repository links
3) Validate: reject malformed/unsupported records
4) Categorize: assign one-or-more categories via weighted rules
5) Render: deterministically regenerate README category blocks
"""

from __future__ import annotations

import re
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Sequence, Tuple
from urllib.parse import urlparse

import arxiv


CATEGORY_ORDER = [
    "Segmentation",
    "Reconstruction",
    "Classification",
    "Image Registration",
    "Domain Adaptation",
    "Generative Models",
    "General",
]

CATEGORY_MARKERS = {
    "Segmentation": "SEGMENTATION",
    "Reconstruction": "RECONSTRUCTION",
    "Classification": "CLASSIFICATION",
    "Image Registration": "IMAGE_REGISTRATION",
    "Domain Adaptation": "DOMAIN_ADAPTATION",
    "Generative Models": "GENERATIVE_MODELS",
    "General": "GENERAL",
}

ALLOWED_CODE_HOSTS = {"github.com", "gitlab.com", "huggingface.co"}

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
}

CATEGORY_THRESHOLDS = {
    "Segmentation": 2,
    "Reconstruction": 2,
    "Classification": 2,
    "Image Registration": 2,
    "Domain Adaptation": 2,
    "Generative Models": 2,
}

REPO_URL_PATTERN = re.compile(
    r"https?://(?:www\.)?(?:github\.com|gitlab\.com|huggingface\.co)/[^\s\]\[<>\"')]+",
    flags=re.IGNORECASE,
)

ARXIV_ABS_PATTERN = re.compile(r"^https?://arxiv\.org/abs/\d{4}\.\d{4,5}(?:v\d+)?$")


def _normalize_host(host: str) -> str:
    host = host.lower().strip()
    return host[4:] if host.startswith("www.") else host


def _clean_url_candidate(url: str) -> str:
    url = url.strip()
    # Handle malformed concatenations like ...repo}{https://...
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

    # Normalize trailing .git in repository segment.
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


def categorize_paper(title: str, abstract: str) -> List[str]:
    title_l = title.lower()
    abstract_l = abstract.lower()

    categories: List[str] = []
    for category, rules in CATEGORY_RULES.items():
        score = 0
        for pattern, weight in rules:
            title_hit = re.search(pattern, title_l)
            abstract_hit = re.search(pattern, abstract_l)
            if title_hit:
                score += weight * 2
            elif abstract_hit:
                score += weight

        if score >= CATEGORY_THRESHOLDS.get(category, 2):
            categories.append(category)

    if not categories:
        categories = ["General"]

    # Stable ordering keeps output deterministic across runs.
    categories.sort(key=lambda c: CATEGORY_ORDER.index(c))
    return categories


def discover_papers() -> Tuple[List[Dict[str, Any]], Dict[str, int], List[str]]:
    """Discover MICCAI 2026 papers from arXiv that contain public code links."""
    print("[discover] Searching arXiv for MICCAI 2026 papers")

    queries = [
        'ti:"MICCAI 2026"',
        'abs:"MICCAI 2026"',
        'co:"MICCAI 2026"',
    ]

    client = arxiv.Client(page_size=50, delay_seconds=3, num_retries=3)
    seen_arxiv = set()
    papers: List[Dict[str, Any]] = []
    failed_queries: List[str] = []
    stats = {
        "fetched_records": 0,
        "unique_arxiv_records": 0,
        "without_code_links": 0,
        "accepted_records": 0,
    }

    for query in queries:
        print(f"[discover] Query: {query}")
        try:
            search = arxiv.Search(
                query=query,
                max_results=100,
                sort_by=arxiv.SortCriterion.SubmittedDate,
                sort_order=arxiv.SortOrder.Descending,
            )
            results = list(client.results(search))
            print(f"[discover] Results: {len(results)}")
        except Exception as exc:
            failed_queries.append(f"{query}: {exc}")
            print(f"[discover] ERROR: {query} failed -> {exc}")
            continue

        for result in results:
            stats["fetched_records"] += 1
            if result.entry_id in seen_arxiv:
                continue
            seen_arxiv.add(result.entry_id)
            stats["unique_arxiv_records"] += 1

            text_for_links = f"{result.summary}\n{getattr(result, 'comment', '') or ''}"
            links = get_repository_links(text_for_links)

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
                }
            )
            stats["accepted_records"] += 1

    return papers, stats, failed_queries


def validate_papers_data(papers: List[Dict[str, Any]]) -> Tuple[int, int]:
    """Validate normalized papers and deduplicate by (arxiv, repo)."""
    print("[validate] Validating normalized paper records")

    deduped_papers: List[Dict[str, Any]] = []
    seen_pairs = set()
    removed_duplicates = 0
    rejected_records = 0

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

        pair_key = (arxiv_url.lower(), tuple(cleaned_links))
        if pair_key in seen_pairs:
            removed_duplicates += 1
            continue

        seen_pairs.add(pair_key)
        normalized_paper = dict(paper)
        normalized_paper["repo_links"] = cleaned_links
        normalized_paper["categories"] = categorize_paper(title, paper.get("summary", ""))
        deduped_papers.append(normalized_paper)

    papers[:] = deduped_papers
    print(
        "[validate] Completed: "
        f"kept={len(deduped_papers)} removed_duplicates={removed_duplicates} rejected={rejected_records}"
    )
    return removed_duplicates, rejected_records


def generate_category_markdown(papers: Sequence[Dict[str, Any]], category: str) -> str:
    category_papers = [paper for paper in papers if category in paper["categories"]]
    category_papers.sort(key=lambda p: (-p["published"].timestamp(), p["title"].lower()))

    lines = []
    for paper in category_papers:
        title = paper["title"]
        arxiv_url = paper["arxiv_url"]
        links = paper["repo_links"]

        line = f"* **[{title}]({arxiv_url})** - [Code]({links[0]})"
        if len(links) > 1:
            extras = [f"[Code{i + 2}]({url})" for i, url in enumerate(links[1:])]
            line += " | " + " | ".join(extras)

        lines.append(line)

    return "\n".join(lines)


def replace_category_block(content: str, marker: str, body: str) -> str:
    pattern = rf"(<!-- BEGIN {marker}_PAPERS -->).*?(<!-- END {marker}_PAPERS -->)"
    replacement = f"\\1\n{body}\n\\2" if body else f"\\1\n\\2"

    if not re.search(pattern, content, flags=re.DOTALL):
        raise ValueError(f"Missing marker block for {marker}")

    return re.sub(pattern, replacement, content, flags=re.DOTALL)


def update_readme(papers: Sequence[Dict[str, Any]], readme_path: str = "README.md") -> Dict[str, int]:
    with open(readme_path, "r", encoding="utf-8") as file:
        content = file.read()

    category_counts: Dict[str, int] = {}
    for category in CATEGORY_ORDER:
        marker = CATEGORY_MARKERS[category]
        body = generate_category_markdown(papers, category)
        content = replace_category_block(content, marker, body)
        category_counts[category] = len([p for p in papers if category in p["categories"]])

    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    content = re.sub(
        r"\*\*Last Updated\*\*: [^\n]*",
        f"**Last Updated**: {timestamp} by GitHub Actions",
        content,
    )

    with open(readme_path, "w", encoding="utf-8") as file:
        file.write(content)

    return category_counts


def main() -> int:
    print("Starting Awesome MICCAI 2026 update")

    papers, stats, failed_queries = discover_papers()

    if failed_queries:
        print("[discover] Failing update because one or more discovery queries failed:")
        for failure in failed_queries:
            print(f"  - {failure}")
        return 1

    removed_duplicates, rejected_records = validate_papers_data(papers)
    category_counts = update_readme(papers)

    print("[summary] Pipeline completed")
    print(f"[summary] fetched_records={stats['fetched_records']}")
    print(f"[summary] unique_arxiv_records={stats['unique_arxiv_records']}")
    print(f"[summary] without_code_links={stats['without_code_links']}")
    print(f"[summary] accepted_records={stats['accepted_records']}")
    print(f"[summary] deduplicated_records={removed_duplicates}")
    print(f"[summary] rejected_records={rejected_records}")
    print("[summary] category_counts=" + ", ".join(f"{k}:{v}" for k, v in category_counts.items()))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
