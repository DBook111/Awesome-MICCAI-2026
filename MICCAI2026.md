# Awesome MICCAI 2026

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of MICCAI papers with public code implementations, updated automatically.

This repository automatically discovers and organizes MICCAI papers from arXiv that include public code links. A daily bot run searches arXiv metadata, validates links and formatting, assigns categories with confidence tiers, and regenerates the list deterministically.

## 📋 Table of Contents

- [How to Contribute](#how-to-contribute)
- [Inclusion Policy](#-inclusion-policy)
- [Trust and Validation](#-trust-and-validation)
- [Coverage Report](#-coverage-report)
- [Segmentation](#segmentation)
- [Reconstruction](#reconstruction)
- [Classification](#classification)
- [Image Registration](#image-registration)
- [Domain Adaptation](#domain-adaptation)
- [Generative Models](#generative-models)
- [General](#general)

## 🤝 How to Contribute

Contributions are welcome! While this list is automatically maintained by a bot that searches arXiv for MICCAI papers (scope configurable), we appreciate human oversight to ensure quality and completeness.

**Ways to contribute:**
- 🐛 **Report errors**: broken links, malformed entries, stale papers, wrong category placement
- 📝 **Add missing papers**: papers that match the active conference scope and provide public code
- 🏷️ **Suggest better categorization**: improve multi-label quality without removing valid overlap
- 💡 **Propose taxonomy improvements**: suggest category changes with examples

**Before contributing:**
1. Provide evidence that the paper is associated with the active conference scope
2. Ensure the code repository is public and reachable
3. Verify links and category suggestions are specific and reproducible

## ✅ Inclusion Policy

- The source of truth is arXiv metadata (`title`, `abstract`, and `comment`) plus public repository links.
- Papers must include MICCAI wording in searchable arXiv metadata; when scope is `miccai-2026`, entries must indicate 2026.
- Code links must resolve to supported public hosts: GitHub, GitLab, or Hugging Face.
- A paper may appear in multiple categories intentionally when it strongly matches multiple tasks.

## 🔍 Trust and Validation

- Content between `<!-- BEGIN ... -->` and `<!-- END ... -->` markers is bot-generated and overwritten on each successful run.
- Daily automation fails fast if discovery is incomplete, generated markdown is malformed, or quality checks fail.
- README validation checks marker integrity, malformed URLs, duplicate entries per category, and unsupported code hosts.
- Default automation runs with `--conference-scope miccai-all-years --mode broad --tracks all`.
- Maintainers can narrow scope with `--conference-scope miccai-2026` and stricter matching via `--mode strict`.

## 📈 Coverage Report

<!-- BEGIN COVERAGE_REPORT -->
- Conference scope: `miccai-2026`
- Discovery mode: `broad`
- Tracks: `main`
- Total code-backed papers: `5`
- Fetched arXiv records: `656`
- Unique arXiv records: `605`
- Filtered (non-target): `533`
- Filtered (track): `33`
- Filtered (no code links): `34`

| Category | Count | Gap to 1000 |
|---|---:|---:|
| Segmentation | 0 | 1000 |
| Reconstruction | 1 | 999 |
| Classification | 2 | 998 |
| Image Registration | 0 | 1000 |
| Domain Adaptation | 0 | 1000 |
| Generative Models | 3 | 997 |
| General | 1 | 999 |
<!-- END COVERAGE_REPORT -->

## 📊 Segmentation

*This list is automatically generated. See any issues? Please open a pull request!*

<!-- BEGIN SEGMENTATION_PAPERS -->
<!-- END SEGMENTATION_PAPERS -->

## 🔧 Reconstruction

*This list is automatically generated. See any issues? Please open a pull request!*

<!-- BEGIN RECONSTRUCTION_PAPERS -->
* **[EchoLVFM: One-Step Video Generation via Latent Flow Matching for Echocardiogram Synthesis](https://arxiv.org/abs/2603.13967v1)** - [Code](https://github.com/engemmanuel/echolvfm) (confidence: medium)
<!-- END RECONSTRUCTION_PAPERS -->

## 🏷️ Classification

*This list is automatically generated. See any issues? Please open a pull request!*

<!-- BEGIN CLASSIFICATION_PAPERS -->
* **[Wasserstein-Aligned Localisation for VLM-Based Distributional OOD Detection in Medical Imaging](https://arxiv.org/abs/2605.05161v1)** - [Code](https://github.com/bkainz/waldo_miccai26_demo) (confidence: high)
* **[Exemplar Diffusion: Improving Medical Object Detection with Opportunistic Labels](https://arxiv.org/abs/2603.15267v1)** - [Code](https://github.com/waahlstrand/exemplardiffusion) (confidence: high)
<!-- END CLASSIFICATION_PAPERS -->

## 🔄 Image Registration

*This list is automatically generated. See any issues? Please open a pull request!*

<!-- BEGIN IMAGE_REGISTRATION_PAPERS -->
<!-- END IMAGE_REGISTRATION_PAPERS -->

## 🔀 Domain Adaptation

*This list is automatically generated. See any issues? Please open a pull request!*

<!-- BEGIN DOMAIN_ADAPTATION_PAPERS -->
<!-- END DOMAIN_ADAPTATION_PAPERS -->

## 🎨 Generative Models

*This list is automatically generated. See any issues? Please open a pull request!*

<!-- BEGIN GENERATIVE_MODELS_PAPERS -->
* **[Hierarchical Perfusion Graphs for Tumor Heterogeneity Modeling in Glioma Molecular Subtyping](https://arxiv.org/abs/2605.07156v1)** - [Code](https://github.com/janghana/hiperfgnn) (confidence: high)
* **[Exemplar Diffusion: Improving Medical Object Detection with Opportunistic Labels](https://arxiv.org/abs/2603.15267v1)** - [Code](https://github.com/waahlstrand/exemplardiffusion) (confidence: high)
* **[EchoLVFM: One-Step Video Generation via Latent Flow Matching for Echocardiogram Synthesis](https://arxiv.org/abs/2603.13967v1)** - [Code](https://github.com/engemmanuel/echolvfm) (confidence: high)
<!-- END GENERATIVE_MODELS_PAPERS -->

## 📚 General

*This list is automatically generated. See any issues? Please open a pull request!*

<!-- BEGIN GENERAL_PAPERS -->
* **[Clinical Graph-Mediated Distillation for Unpaired MRI-to-CFI Hypertension Prediction](https://arxiv.org/abs/2603.21809v1)** - [Code](https://github.com/dillanimans/cgmd-unpaired-distillation) (confidence: medium)
<!-- END GENERAL_PAPERS -->

---

**Repository Topics**: awesome, awesome-list, miccai, miccai2026, medical-imaging, deep-learning, computer-vision, segmentation, reconstruction, classification, medical-image-analysis, artificial-intelligence

**Conference Scope**: miccai-2026
**Discovery Mode**: broad

**Last Updated**: 2026-05-11 21:56 北京时间 by GitHub Actions

**License**: Apache License 2.0
