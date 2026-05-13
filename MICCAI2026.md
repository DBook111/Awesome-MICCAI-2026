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
- [Fundus Imaging](#fundus-imaging)
- [OCT](#oct)
- [OCTA](#octa)
- [Ophthalmic Foundation Models](#ophthalmic-foundation-models)
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
- Total code-backed papers: `9`
- Fetched arXiv records: `664`
- Unique arXiv records: `605`
- Filtered (non-target): `526`
- Filtered (track): `34`
- Filtered (no code links): `36`

| Category | Count | Gap to 1000 |
|---|---:|---:|
| Segmentation | 2 | 998 |
| Reconstruction | 1 | 999 |
| Classification | 3 | 997 |
| Image Registration | 1 | 999 |
| Domain Adaptation | 0 | 1000 |
| Generative Models | 4 | 996 |
| Fundus Imaging | 1 | 999 |
| OCT | 0 | 1000 |
| OCTA | 0 | 1000 |
| Ophthalmic Foundation Models | 1 | 999 |
| General | 0 | 1000 |
<!-- END COVERAGE_REPORT -->

## 📊 Segmentation

*This list is automatically generated. See any issues? Please open a pull request!*

<!-- BEGIN SEGMENTATION_PAPERS -->
* **[ScribbleDose: Scribble-Guided Dose Prediction in Radiotherapy](https://arxiv.org/abs/2605.11555v1)** - [Code](https://github.com/icherishxixixi/scribbledose) (confidence: medium)
* **[XTinyU-Net: Training-Free U-Net Scaling via Initialization-Time Sensitivity](https://arxiv.org/abs/2605.09639v1)** - [Code](https://github.com/alvinkimbowa/nntinyunet) (confidence: medium)
<!-- END SEGMENTATION_PAPERS -->

## 🔧 Reconstruction

*This list is automatically generated. See any issues? Please open a pull request!*

<!-- BEGIN RECONSTRUCTION_PAPERS -->
* **[EchoLVFM: One-Step Video Generation via Latent Flow Matching for Echocardiogram Synthesis](https://arxiv.org/abs/2603.13967v1)** - [Code](https://github.com/engemmanuel/echolvfm) (confidence: medium)
<!-- END RECONSTRUCTION_PAPERS -->

## 🏷️ Classification

*This list is automatically generated. See any issues? Please open a pull request!*

<!-- BEGIN CLASSIFICATION_PAPERS -->
* **[Contrastive Learning under Noisy Temporal Self-Supervision for Colonoscopy Videos](https://arxiv.org/abs/2605.12320v1)** - [Code](https://github.com/lparolari/ntssl) (confidence: medium)
* **[Wasserstein-Aligned Localisation for VLM-Based Distributional OOD Detection in Medical Imaging](https://arxiv.org/abs/2605.05161v1)** - [Code](https://github.com/bkainz/waldo_miccai26_demo) (confidence: high)
* **[Exemplar Diffusion: Improving Medical Object Detection with Opportunistic Labels](https://arxiv.org/abs/2603.15267v1)** - [Code](https://github.com/waahlstrand/exemplardiffusion) (confidence: high)
<!-- END CLASSIFICATION_PAPERS -->

## 🔄 Image Registration

*This list is automatically generated. See any issues? Please open a pull request!*

<!-- BEGIN IMAGE_REGISTRATION_PAPERS -->
* **[EchoTracker2: Enhancing Myocardial Point Tracking by Modeling Local Motion](https://arxiv.org/abs/2605.12140v1)** - [Code](https://github.com/riponazad/ptecho) (confidence: medium)
<!-- END IMAGE_REGISTRATION_PAPERS -->

## 🔀 Domain Adaptation

*This list is automatically generated. See any issues? Please open a pull request!*

<!-- BEGIN DOMAIN_ADAPTATION_PAPERS -->
<!-- END DOMAIN_ADAPTATION_PAPERS -->

## 🎨 Generative Models

*This list is automatically generated. See any issues? Please open a pull request!*

<!-- BEGIN GENERATIVE_MODELS_PAPERS -->
* **[ScribbleDose: Scribble-Guided Dose Prediction in Radiotherapy](https://arxiv.org/abs/2605.11555v1)** - [Code](https://github.com/icherishxixixi/scribbledose) (confidence: medium)
* **[Hierarchical Perfusion Graphs for Tumor Heterogeneity Modeling in Glioma Molecular Subtyping](https://arxiv.org/abs/2605.07156v1)** - [Code](https://github.com/janghana/hiperfgnn) (confidence: high)
* **[Exemplar Diffusion: Improving Medical Object Detection with Opportunistic Labels](https://arxiv.org/abs/2603.15267v1)** - [Code](https://github.com/waahlstrand/exemplardiffusion) (confidence: high)
* **[EchoLVFM: One-Step Video Generation via Latent Flow Matching for Echocardiogram Synthesis](https://arxiv.org/abs/2603.13967v1)** - [Code](https://github.com/engemmanuel/echolvfm) (confidence: high)
<!-- END GENERATIVE_MODELS_PAPERS -->

## 👁️ Fundus Imaging

*This list is automatically generated. See any issues? Please open a pull request!*

<!-- BEGIN FUNDUS_IMAGING_PAPERS -->
* **[Clinical Graph-Mediated Distillation for Unpaired MRI-to-CFI Hypertension Prediction](https://arxiv.org/abs/2603.21809v1)** - [Code](https://github.com/dillanimans/cgmd-unpaired-distillation) (confidence: high)
<!-- END FUNDUS_IMAGING_PAPERS -->

## 🧿 OCT

*This list is automatically generated. See any issues? Please open a pull request!*

<!-- BEGIN OCT_PAPERS -->
<!-- END OCT_PAPERS -->

## 🩸 OCTA

*This list is automatically generated. See any issues? Please open a pull request!*

<!-- BEGIN OCTA_PAPERS -->
<!-- END OCTA_PAPERS -->

## 🧠👁️ Ophthalmic Foundation Models

*This list is automatically generated. See any issues? Please open a pull request!*

<!-- BEGIN OPHTHALMIC_FOUNDATION_MODELS_PAPERS -->
* **[Clinical Graph-Mediated Distillation for Unpaired MRI-to-CFI Hypertension Prediction](https://arxiv.org/abs/2603.21809v1)** - [Code](https://github.com/dillanimans/cgmd-unpaired-distillation) (confidence: high)
<!-- END OPHTHALMIC_FOUNDATION_MODELS_PAPERS -->

## 📚 General

*This list is automatically generated. See any issues? Please open a pull request!*

<!-- BEGIN GENERAL_PAPERS -->
<!-- END GENERAL_PAPERS -->

---

**Repository Topics**: awesome, awesome-list, miccai, miccai2026, medical-imaging, deep-learning, computer-vision, segmentation, reconstruction, classification, medical-image-analysis, artificial-intelligence

**Conference Scope**: miccai-2026
**Discovery Mode**: broad

**Last Updated**: 2026-05-13 13:17 北京时间 by GitHub Actions

**License**: Apache License 2.0
