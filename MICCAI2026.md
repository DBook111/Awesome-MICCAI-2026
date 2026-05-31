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
- Total code-backed papers: `24`
- Fetched arXiv records: `703`
- Unique arXiv records: `605`
- Filtered (non-target): `489`
- Filtered (track): `37`
- Filtered (no code links): `55`

| Category | Count | Gap to 1000 |
|---|---:|---:|
| Segmentation | 9 | 991 |
| Reconstruction | 3 | 997 |
| Classification | 7 | 993 |
| Image Registration | 5 | 995 |
| Domain Adaptation | 2 | 998 |
| Generative Models | 6 | 994 |
| Fundus Imaging | 1 | 999 |
| OCT | 0 | 1000 |
| OCTA | 0 | 1000 |
| Ophthalmic Foundation Models | 4 | 996 |
| General | 3 | 997 |
<!-- END COVERAGE_REPORT -->

## 📊 Segmentation

*This list is automatically generated. See any issues? Please open a pull request!*

<!-- BEGIN SEGMENTATION_PAPERS -->
* **[Attenuation-Resilient Alternating Optimization for Laparoscopic Liver Landmark Detection](https://arxiv.org/abs/2605.26630v1)** - [Code](https://github.com/hyperiondk115/a2onet) (confidence: medium)
* **[Detail Consistent Stage-Wise Distillation for Efficient 3D MRI Segmentation](https://arxiv.org/abs/2605.26382v1)** - [Code](https://github.com/clinicaalpha/dcd-3d-medseg) (confidence: high)
* **[Anatomy-Anchored Self-Supervision: Distilling Vision Foundation Models for Invariant Ultrasound Representation](https://arxiv.org/abs/2605.25402v1)** - [Code](https://github.com/zhcz328/anaus) (confidence: medium)
* **[R2AoP: Reliable and Robust Angle of Progression Estimation from Intrapartum Ultrasound](https://arxiv.org/abs/2605.21099v1)** - [Code](https://github.com/baiyou1234/r2aop) (confidence: high)
* **[VoxShield: Protecting 3D Medical Datasets from Unauthorized Training via Frequency-Aware Inter-Slice Disruption](https://arxiv.org/abs/2605.17345v1)** - [Code](https://github.com/kk266299/voxshield) (confidence: medium)
* **[ScribbleDose: Scribble-Guided Dose Prediction in Radiotherapy](https://arxiv.org/abs/2605.11555v2)** - [Code](https://github.com/icherishxixixi/scribbledose) (confidence: medium)
* **[XTinyU-Net: Training-Free U-Net Scaling via Initialization-Time Sensitivity](https://arxiv.org/abs/2605.09639v2)** - [Code](https://github.com/alvinkimbowa/nntinyunet) (confidence: medium)
* **[Defining Robust Ultrasound Quality Metrics via an Ultrasound Foundation Model](https://arxiv.org/abs/2604.19512v2)** - [Code](https://github.com/sextant-fable/us-metrics) (confidence: medium)
* **[DUCX: Decomposing Unfairness in Tool-Using Chest X-ray Agents](https://arxiv.org/abs/2603.00777v2)** - [Code](https://github.com/nanboy-ronan/duck) (confidence: medium)
<!-- END SEGMENTATION_PAPERS -->

## 🔧 Reconstruction

*This list is automatically generated. See any issues? Please open a pull request!*

<!-- BEGIN RECONSTRUCTION_PAPERS -->
* **[Anatomy-Anchored Self-Supervision: Distilling Vision Foundation Models for Invariant Ultrasound Representation](https://arxiv.org/abs/2605.25402v1)** - [Code](https://github.com/zhcz328/anaus) (confidence: medium)
* **[Defining Robust Ultrasound Quality Metrics via an Ultrasound Foundation Model](https://arxiv.org/abs/2604.19512v2)** - [Code](https://github.com/sextant-fable/us-metrics) (confidence: medium)
* **[EchoLVFM: One-Step Video Generation via Latent Flow Matching for Echocardiogram Synthesis](https://arxiv.org/abs/2603.13967v1)** - [Code](https://github.com/engemmanuel/echolvfm) (confidence: medium)
<!-- END RECONSTRUCTION_PAPERS -->

## 🏷️ Classification

*This list is automatically generated. See any issues? Please open a pull request!*

<!-- BEGIN CLASSIFICATION_PAPERS -->
* **[Genetically Aligned Patient Representations Improve Hematological Diagnosis](https://arxiv.org/abs/2605.29980v1)** - [Code](https://github.com/marrlab/genbloom) (confidence: medium)
* **[Attenuation-Resilient Alternating Optimization for Laparoscopic Liver Landmark Detection](https://arxiv.org/abs/2605.26630v1)** - [Code](https://github.com/hyperiondk115/a2onet) (confidence: high)
* **[VIHD: Visual Intervention-based Hallucination Detection for Medical Visual Question Answering](https://arxiv.org/abs/2605.20772v2)** - [Code](https://github.com/jiayi-chen-au/vihd) (confidence: high)
* **[BrainAnytime: Anatomy-Aware Cross-Modal Pretraining for Brain Image Analysis with Arbitrary Modality Availability](https://arxiv.org/abs/2605.13059v1)** - [Code](https://github.com/sdh-lab/brainanytime) (confidence: medium)
* **[Contrastive Learning under Noisy Temporal Self-Supervision for Colonoscopy Videos](https://arxiv.org/abs/2605.12320v2)** - [Code](https://github.com/lparolari/ntssl) (confidence: medium)
* **[Wasserstein-Aligned Localisation for VLM-Based Distributional OOD Detection in Medical Imaging](https://arxiv.org/abs/2605.05161v1)** - [Code](https://github.com/bkainz/waldo_miccai26_demo) (confidence: high)
* **[Exemplar Diffusion: Improving Medical Object Detection with Opportunistic Labels](https://arxiv.org/abs/2603.15267v1)** - [Code](https://github.com/waahlstrand/exemplardiffusion) (confidence: high)
<!-- END CLASSIFICATION_PAPERS -->

## 🔄 Image Registration

*This list is automatically generated. See any issues? Please open a pull request!*

<!-- BEGIN IMAGE_REGISTRATION_PAPERS -->
* **[Genetically Aligned Patient Representations Improve Hematological Diagnosis](https://arxiv.org/abs/2605.29980v1)** - [Code](https://github.com/marrlab/genbloom) (confidence: medium)
* **[Evi-Steer: Learning to Steer Biomedical Vision-Language Models through Efficient and Generalizable Evidential Tuning](https://arxiv.org/abs/2605.26292v1)** - [Code](https://github.com/healthx-lab/evi-steer) (confidence: medium)
* **[Anatomy-Anchored Self-Supervision: Distilling Vision Foundation Models for Invariant Ultrasound Representation](https://arxiv.org/abs/2605.25402v1)** - [Code](https://github.com/zhcz328/anaus) (confidence: medium)
* **[Subspace-Guided Semantic and Topological Invariant Registration for Annotation-Free Ultrasound Plane Quality Control](https://arxiv.org/abs/2605.25396v1)** - [Code](https://github.com/zhcz328/striq) (confidence: high)
* **[EchoTracker2: Enhancing Myocardial Point Tracking by Modeling Local Motion](https://arxiv.org/abs/2605.12140v1)** - [Code](https://github.com/riponazad/ptecho) (confidence: medium)
<!-- END IMAGE_REGISTRATION_PAPERS -->

## 🔀 Domain Adaptation

*This list is automatically generated. See any issues? Please open a pull request!*

<!-- BEGIN DOMAIN_ADAPTATION_PAPERS -->
* **[Evi-Steer: Learning to Steer Biomedical Vision-Language Models through Efficient and Generalizable Evidential Tuning](https://arxiv.org/abs/2605.26292v1)** - [Code](https://github.com/healthx-lab/evi-steer) (confidence: high)
* **[Anatomy-Anchored Self-Supervision: Distilling Vision Foundation Models for Invariant Ultrasound Representation](https://arxiv.org/abs/2605.25402v1)** - [Code](https://github.com/zhcz328/anaus) (confidence: medium)
<!-- END DOMAIN_ADAPTATION_PAPERS -->

## 🎨 Generative Models

*This list is automatically generated. See any issues? Please open a pull request!*

<!-- BEGIN GENERATIVE_MODELS_PAPERS -->
* **[BrainAnytime: Anatomy-Aware Cross-Modal Pretraining for Brain Image Analysis with Arbitrary Modality Availability](https://arxiv.org/abs/2605.13059v1)** - [Code](https://github.com/sdh-lab/brainanytime) (confidence: medium)
* **[ScribbleDose: Scribble-Guided Dose Prediction in Radiotherapy](https://arxiv.org/abs/2605.11555v2)** - [Code](https://github.com/icherishxixixi/scribbledose) (confidence: medium)
* **[Hierarchical Perfusion Graphs for Tumor Heterogeneity Modeling in Glioma Molecular Subtyping](https://arxiv.org/abs/2605.07156v1)** - [Code](https://github.com/janghana/hiperfgnn) (confidence: high)
* **[Exemplar Diffusion: Improving Medical Object Detection with Opportunistic Labels](https://arxiv.org/abs/2603.15267v1)** - [Code](https://github.com/waahlstrand/exemplardiffusion) (confidence: high)
* **[EchoLVFM: One-Step Video Generation via Latent Flow Matching for Echocardiogram Synthesis](https://arxiv.org/abs/2603.13967v1)** - [Code](https://github.com/engemmanuel/echolvfm) (confidence: high)
* **[DUCX: Decomposing Unfairness in Tool-Using Chest X-ray Agents](https://arxiv.org/abs/2603.00777v2)** - [Code](https://github.com/nanboy-ronan/duck) (confidence: medium)
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
* **[Anatomy-Anchored Self-Supervision: Distilling Vision Foundation Models for Invariant Ultrasound Representation](https://arxiv.org/abs/2605.25402v1)** - [Code](https://github.com/zhcz328/anaus) (confidence: high)
* **[BrainAnytime: Anatomy-Aware Cross-Modal Pretraining for Brain Image Analysis with Arbitrary Modality Availability](https://arxiv.org/abs/2605.13059v1)** - [Code](https://github.com/sdh-lab/brainanytime) (confidence: medium)
* **[Defining Robust Ultrasound Quality Metrics via an Ultrasound Foundation Model](https://arxiv.org/abs/2604.19512v2)** - [Code](https://github.com/sextant-fable/us-metrics) (confidence: high)
* **[Clinical Graph-Mediated Distillation for Unpaired MRI-to-CFI Hypertension Prediction](https://arxiv.org/abs/2603.21809v1)** - [Code](https://github.com/dillanimans/cgmd-unpaired-distillation) (confidence: high)
<!-- END OPHTHALMIC_FOUNDATION_MODELS_PAPERS -->

## 📚 General

*This list is automatically generated. See any issues? Please open a pull request!*

<!-- BEGIN GENERAL_PAPERS -->
* **[BCER Agent: Reliable Long-Horizon MRI Workflow Execution via Compilation, Artifact Binding, and Bounded Local Recovery](https://arxiv.org/abs/2605.29163v1)** - [Code](https://github.com/albertlongzi/bcer) (confidence: medium)
* **[BioFact-MoE: Biologically Factorized Mixture of Experts for Vision-Language Prognostic Modeling in Hepatocellular Carcinoma](https://arxiv.org/abs/2605.26376v1)** - [Code](https://github.com/jy-639/biofact-moe) (confidence: medium)
* **[Network-Aware Bilinear Tokenization for Brain Functional Connectivity Representation Learning](https://arxiv.org/abs/2605.14048v3)** - [Code](https://github.com/leomlck/nerve) (confidence: medium)
<!-- END GENERAL_PAPERS -->

---

**Repository Topics**: awesome, awesome-list, miccai, miccai2026, medical-imaging, deep-learning, computer-vision, segmentation, reconstruction, classification, medical-image-analysis, artificial-intelligence

**Conference Scope**: miccai-2026
**Discovery Mode**: broad

**Last Updated**: 2026-05-31 11:56 北京时间 by GitHub Actions

**License**: Apache License 2.0
