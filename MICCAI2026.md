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
- Total code-backed papers: `43`
- Fetched arXiv records: `743`
- Unique arXiv records: `605`
- Filtered (non-target): `455`
- Filtered (track): `33`
- Filtered (no code links): `74`

| Category | Count | Gap to 1000 |
|---|---:|---:|
| Segmentation | 15 | 985 |
| Reconstruction | 7 | 993 |
| Classification | 13 | 987 |
| Image Registration | 8 | 992 |
| Domain Adaptation | 2 | 998 |
| Generative Models | 10 | 990 |
| Fundus Imaging | 5 | 995 |
| OCT | 3 | 997 |
| OCTA | 0 | 1000 |
| Ophthalmic Foundation Models | 9 | 991 |
| General | 6 | 994 |
<!-- END COVERAGE_REPORT -->

## 📊 Segmentation

*This list is automatically generated. See any issues? Please open a pull request!*

<!-- BEGIN SEGMENTATION_PAPERS -->
* **[Single-Stage Hierarchical Rectification for Weakly Supervised Histopathology Segmentation](https://arxiv.org/abs/2606.20250v1)** - [Code](https://github.com/trongduc-nguyen/sshr) (confidence: high)
* **[CSWinUNETR: Segmentation of Thin Anatomical Structures in Medical Images](https://arxiv.org/abs/2606.19824v1)** - [Code](https://github.com/labhai/cswinunetr) (confidence: high)
* **[Quantification of Uncertainty with Adversarial Models in Medical Image Segmentation](https://arxiv.org/abs/2606.18860v1)** - [Code](https://github.com/hanajebril/quam_sm) (confidence: high)
* **[Beyond Visual Cues: CoT-Enhanced Reasoning for Semi-supervised Medical Image Segmentation](https://arxiv.org/abs/2606.17958v1)** - [Code](https://github.com/cymasuna/cers) (confidence: high)
* **[Attention-Based Prototype Calibration for Multi-Rater Few-Shot Medical Image Segmentation](https://arxiv.org/abs/2606.16325v1)** - [Code](https://github.com/truong2710-cyber/japc) (confidence: high)
* **[Mutual Distillation of Dual-Foundation Models for Semi-Supervised PET/CT Segmentation](https://arxiv.org/abs/2606.15611v1)** - [Code](https://github.com/wu-beining/muduo) (confidence: high)
* **[Attenuation-Resilient Alternating Optimization for Laparoscopic Liver Landmark Detection](https://arxiv.org/abs/2605.26630v1)** - [Code](https://github.com/hyperiondk115/a2onet) (confidence: medium)
* **[Detail Consistent Stage-Wise Distillation for Efficient 3D MRI Segmentation](https://arxiv.org/abs/2605.26382v1)** - [Code](https://github.com/clinicaalpha/dcd-3d-medseg) (confidence: high)
* **[Anatomy-Anchored Self-Supervision: Distilling Vision Foundation Models for Invariant Ultrasound Representation](https://arxiv.org/abs/2605.25402v3)** - [Code](https://github.com/zhcz328/anaus) (confidence: medium)
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
* **[When, Where, and How: Adaptive Binning for Tabular Self-Supervised Learning](https://arxiv.org/abs/2606.19827v1)** - [Code](https://github.com/labhai/adaptive-binning) (confidence: medium)
* **[Test-Time Adaptation in Optical Coherence Tomography Using Trajectory-Aligned Time-Independent Flow](https://arxiv.org/abs/2606.18876v1)** - [Code](https://github.com/veit21/tta-flow) (confidence: medium)
* **[Propagating Structural Guidance: Synthesizing Fluorescein Angiography from Fundus Images and Sparse OCT Scans](https://arxiv.org/abs/2606.16234v1)** - [Code](https://github.com/while-plus/oct-guide-ffa-syn) (confidence: medium)
* **[Learning Directional Semantic Transitions for Longitudinal Chest X-ray Analysis](https://arxiv.org/abs/2606.15938v1)** - [Code](https://github.com/rpidial/protrans) (confidence: medium)
* **[Anatomy-Anchored Self-Supervision: Distilling Vision Foundation Models for Invariant Ultrasound Representation](https://arxiv.org/abs/2605.25402v3)** - [Code](https://github.com/zhcz328/anaus) (confidence: medium)
* **[Defining Robust Ultrasound Quality Metrics via an Ultrasound Foundation Model](https://arxiv.org/abs/2604.19512v2)** - [Code](https://github.com/sextant-fable/us-metrics) (confidence: medium)
* **[EchoLVFM: One-Step Video Generation via Latent Flow Matching for Echocardiogram Synthesis](https://arxiv.org/abs/2603.13967v1)** - [Code](https://github.com/engemmanuel/echolvfm) (confidence: medium)
<!-- END RECONSTRUCTION_PAPERS -->

## 🏷️ Classification

*This list is automatically generated. See any issues? Please open a pull request!*

<!-- BEGIN CLASSIFICATION_PAPERS -->
* **[OTCHA: Optimal Transport-driven Confidence-aware Latent Hub Alignment for Multi-View Medical Image Classification](https://arxiv.org/abs/2606.19838v1)** - [Code](https://github.com/labhai/otcha) (confidence: high)
* **[When, Where, and How: Adaptive Binning for Tabular Self-Supervised Learning](https://arxiv.org/abs/2606.19827v1)** - [Code](https://github.com/labhai/adaptive-binning) (confidence: medium)
* **[A Multi-Center Benchmark for Abdominal Disease Diagnosis and Report Generation from Non-Contrast CT](https://arxiv.org/abs/2606.16991v1)** - [Code](https://github.com/xmed-lab/trials-report) (confidence: medium)
* **[3D Classification of Paramagnetic Rim Lesions in Multiple Sclerosis via Asymmetric QSM-FLAIR Modeling](https://arxiv.org/abs/2606.16756v1)** - [Code](https://github.com/veronicapignedoli/frodo) (confidence: high)
* **[Learning Directional Semantic Transitions for Longitudinal Chest X-ray Analysis](https://arxiv.org/abs/2606.15938v1)** - [Code](https://github.com/rpidial/protrans) (confidence: medium)
* **[Genetically Aligned Patient Representations Improve Hematological Diagnosis](https://arxiv.org/abs/2605.29980v1)** - [Code](https://github.com/marrlab/genbloom) (confidence: medium)
* **[Attenuation-Resilient Alternating Optimization for Laparoscopic Liver Landmark Detection](https://arxiv.org/abs/2605.26630v1)** - [Code](https://github.com/hyperiondk115/a2onet) (confidence: high)
* **[VIHD: Visual Intervention-based Hallucination Detection for Medical Visual Question Answering](https://arxiv.org/abs/2605.20772v2)** - [Code](https://github.com/jiayi-chen-au/vihd) (confidence: high)
* **[BrainAnytime: Anatomy-Aware Cross-Modal Pretraining for Brain Image Analysis with Arbitrary Modality Availability](https://arxiv.org/abs/2605.13059v1)** - [Code](https://github.com/sdh-lab/brainanytime) (confidence: medium)
* **[Contrastive Learning under Noisy Temporal Self-Supervision for Colonoscopy Videos](https://arxiv.org/abs/2605.12320v2)** - [Code](https://github.com/lparolari/ntssl) (confidence: medium)
* **[Wasserstein-Aligned Localisation for VLM-Based Distributional OOD Detection in Medical Imaging](https://arxiv.org/abs/2605.05161v1)** - [Code](https://github.com/bkainz/waldo_miccai26_demo) (confidence: high)
* **[Exemplar Diffusion: Improving Medical Object Detection with Opportunistic Labels](https://arxiv.org/abs/2603.15267v1)** - [Code](https://github.com/waahlstrand/exemplardiffusion) (confidence: high)
* **[Echo2ECG: Enhancing ECG Representations with Cardiac Morphology from Multi-View Echos](https://arxiv.org/abs/2603.08505v2)** - [Code](https://github.com/michelleespranita/echo2ecg) (confidence: medium)
<!-- END CLASSIFICATION_PAPERS -->

## 🔄 Image Registration

*This list is automatically generated. See any issues? Please open a pull request!*

<!-- BEGIN IMAGE_REGISTRATION_PAPERS -->
* **[OTCHA: Optimal Transport-driven Confidence-aware Latent Hub Alignment for Multi-View Medical Image Classification](https://arxiv.org/abs/2606.19838v1)** - [Code](https://github.com/labhai/otcha) (confidence: high)
* **[Propagating Structural Guidance: Synthesizing Fluorescein Angiography from Fundus Images and Sparse OCT Scans](https://arxiv.org/abs/2606.16234v1)** - [Code](https://github.com/while-plus/oct-guide-ffa-syn) (confidence: medium)
* **[WaveDiT: Distribution-Aware Wavelet Flow Matching for Efficient 3D Brain MRI Synthesis](https://arxiv.org/abs/2606.08670v1)** - [Code](https://github.com/sisinflab/wavedit) (confidence: medium)
* **[Genetically Aligned Patient Representations Improve Hematological Diagnosis](https://arxiv.org/abs/2605.29980v1)** - [Code](https://github.com/marrlab/genbloom) (confidence: medium)
* **[Evi-Steer: Learning to Steer Biomedical Vision-Language Models through Efficient and Generalizable Evidential Tuning](https://arxiv.org/abs/2605.26292v2)** - [Code](https://github.com/healthx-lab/evi-steer) (confidence: medium)
* **[Anatomy-Anchored Self-Supervision: Distilling Vision Foundation Models for Invariant Ultrasound Representation](https://arxiv.org/abs/2605.25402v3)** - [Code](https://github.com/zhcz328/anaus) (confidence: medium)
* **[Subspace-Guided Semantic and Topological Invariant Registration for Annotation-Free Ultrasound Plane Quality Control](https://arxiv.org/abs/2605.25396v1)** - [Code](https://github.com/zhcz328/striq) (confidence: high)
* **[EchoTracker2: Enhancing Myocardial Point Tracking by Modeling Local Motion](https://arxiv.org/abs/2605.12140v1)** - [Code](https://github.com/riponazad/ptecho) (confidence: medium)
<!-- END IMAGE_REGISTRATION_PAPERS -->

## 🔀 Domain Adaptation

*This list is automatically generated. See any issues? Please open a pull request!*

<!-- BEGIN DOMAIN_ADAPTATION_PAPERS -->
* **[Evi-Steer: Learning to Steer Biomedical Vision-Language Models through Efficient and Generalizable Evidential Tuning](https://arxiv.org/abs/2605.26292v2)** - [Code](https://github.com/healthx-lab/evi-steer) (confidence: high)
* **[Anatomy-Anchored Self-Supervision: Distilling Vision Foundation Models for Invariant Ultrasound Representation](https://arxiv.org/abs/2605.25402v3)** - [Code](https://github.com/zhcz328/anaus) (confidence: medium)
<!-- END DOMAIN_ADAPTATION_PAPERS -->

## 🎨 Generative Models

*This list is automatically generated. See any issues? Please open a pull request!*

<!-- BEGIN GENERATIVE_MODELS_PAPERS -->
* **[Single-Stage Hierarchical Rectification for Weakly Supervised Histopathology Segmentation](https://arxiv.org/abs/2606.20250v1)** - [Code](https://github.com/trongduc-nguyen/sshr) (confidence: medium)
* **[A Multi-Center Benchmark for Abdominal Disease Diagnosis and Report Generation from Non-Contrast CT](https://arxiv.org/abs/2606.16991v1)** - [Code](https://github.com/xmed-lab/trials-report) (confidence: high)
* **[Propagating Structural Guidance: Synthesizing Fluorescein Angiography from Fundus Images and Sparse OCT Scans](https://arxiv.org/abs/2606.16234v1)** - [Code](https://github.com/while-plus/oct-guide-ffa-syn) (confidence: medium)
* **[WaveDiT: Distribution-Aware Wavelet Flow Matching for Efficient 3D Brain MRI Synthesis](https://arxiv.org/abs/2606.08670v1)** - [Code](https://github.com/sisinflab/wavedit) (confidence: high)
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
* **[CSWinUNETR: Segmentation of Thin Anatomical Structures in Medical Images](https://arxiv.org/abs/2606.19824v1)** - [Code](https://github.com/labhai/cswinunetr) (confidence: high)
* **[Test-Time Adaptation in Optical Coherence Tomography Using Trajectory-Aligned Time-Independent Flow](https://arxiv.org/abs/2606.18876v1)** - [Code](https://github.com/veit21/tta-flow) (confidence: high)
* **[Propagating Structural Guidance: Synthesizing Fluorescein Angiography from Fundus Images and Sparse OCT Scans](https://arxiv.org/abs/2606.16234v1)** - [Code](https://github.com/while-plus/oct-guide-ffa-syn) (confidence: high)
* **[Response-Aware Multimodal Learning for Post-Treatment Visual Acuity Forecasting](https://arxiv.org/abs/2606.00588v2)** - [Code](https://github.com/nguyenpbui/reva) (confidence: medium)
* **[Clinical Graph-Mediated Distillation for Unpaired MRI-to-CFI Hypertension Prediction](https://arxiv.org/abs/2603.21809v1)** - [Code](https://github.com/dillanimans/cgmd-unpaired-distillation) (confidence: high)
<!-- END FUNDUS_IMAGING_PAPERS -->

## 🧿 OCT

*This list is automatically generated. See any issues? Please open a pull request!*

<!-- BEGIN OCT_PAPERS -->
* **[Test-Time Adaptation in Optical Coherence Tomography Using Trajectory-Aligned Time-Independent Flow](https://arxiv.org/abs/2606.18876v1)** - [Code](https://github.com/veit21/tta-flow) (confidence: high)
* **[Propagating Structural Guidance: Synthesizing Fluorescein Angiography from Fundus Images and Sparse OCT Scans](https://arxiv.org/abs/2606.16234v1)** - [Code](https://github.com/while-plus/oct-guide-ffa-syn) (confidence: high)
* **[Response-Aware Multimodal Learning for Post-Treatment Visual Acuity Forecasting](https://arxiv.org/abs/2606.00588v2)** - [Code](https://github.com/nguyenpbui/reva) (confidence: medium)
<!-- END OCT_PAPERS -->

## 🩸 OCTA

*This list is automatically generated. See any issues? Please open a pull request!*

<!-- BEGIN OCTA_PAPERS -->
<!-- END OCTA_PAPERS -->

## 🧠👁️ Ophthalmic Foundation Models

*This list is automatically generated. See any issues? Please open a pull request!*

<!-- BEGIN OPHTHALMIC_FOUNDATION_MODELS_PAPERS -->
* **[CSWinUNETR: Segmentation of Thin Anatomical Structures in Medical Images](https://arxiv.org/abs/2606.19824v1)** - [Code](https://github.com/labhai/cswinunetr) (confidence: high)
* **[Test-Time Adaptation in Optical Coherence Tomography Using Trajectory-Aligned Time-Independent Flow](https://arxiv.org/abs/2606.18876v1)** - [Code](https://github.com/veit21/tta-flow) (confidence: high)
* **[Propagating Structural Guidance: Synthesizing Fluorescein Angiography from Fundus Images and Sparse OCT Scans](https://arxiv.org/abs/2606.16234v1)** - [Code](https://github.com/while-plus/oct-guide-ffa-syn) (confidence: high)
* **[Mutual Distillation of Dual-Foundation Models for Semi-Supervised PET/CT Segmentation](https://arxiv.org/abs/2606.15611v1)** - [Code](https://github.com/wu-beining/muduo) (confidence: high)
* **[Response-Aware Multimodal Learning for Post-Treatment Visual Acuity Forecasting](https://arxiv.org/abs/2606.00588v2)** - [Code](https://github.com/nguyenpbui/reva) (confidence: medium)
* **[Anatomy-Anchored Self-Supervision: Distilling Vision Foundation Models for Invariant Ultrasound Representation](https://arxiv.org/abs/2605.25402v3)** - [Code](https://github.com/zhcz328/anaus) (confidence: high)
* **[BrainAnytime: Anatomy-Aware Cross-Modal Pretraining for Brain Image Analysis with Arbitrary Modality Availability](https://arxiv.org/abs/2605.13059v1)** - [Code](https://github.com/sdh-lab/brainanytime) (confidence: medium)
* **[Defining Robust Ultrasound Quality Metrics via an Ultrasound Foundation Model](https://arxiv.org/abs/2604.19512v2)** - [Code](https://github.com/sextant-fable/us-metrics) (confidence: high)
* **[Clinical Graph-Mediated Distillation for Unpaired MRI-to-CFI Hypertension Prediction](https://arxiv.org/abs/2603.21809v1)** - [Code](https://github.com/dillanimans/cgmd-unpaired-distillation) (confidence: high)
<!-- END OPHTHALMIC_FOUNDATION_MODELS_PAPERS -->

## 📚 General

*This list is automatically generated. See any issues? Please open a pull request!*

<!-- BEGIN GENERAL_PAPERS -->
* **[AGE-MIL: Anchor-Guided Evidence Learning for Patient-Level Prediction](https://arxiv.org/abs/2606.12126v1)** - [Code](https://github.com/wodeniua/age-mil) (confidence: medium)
* **[StrokeTimer: Robust Representation Learning for Ischemic Stroke Onset-Time Estimation from Non-contrast CT](https://arxiv.org/abs/2606.04722v1)** - [Code](https://github.com/brainvas/stroketimer) (confidence: medium)
* **[BCER Agent: Reliable Long-Horizon MRI Workflow Execution via Compilation, Artifact Binding, and Bounded Local Recovery](https://arxiv.org/abs/2605.29163v1)** - [Code](https://github.com/albertlongzi/bcer) (confidence: medium)
* **[BioFact-MoE: Biologically Factorized Mixture of Experts for Vision-Language Prognostic Modeling in Hepatocellular Carcinoma](https://arxiv.org/abs/2605.26376v1)** - [Code](https://github.com/jy-639/biofact-moe) (confidence: medium)
* **[Network-Aware Bilinear Tokenization for Brain Functional Connectivity Representation Learning](https://arxiv.org/abs/2605.14048v3)** - [Code](https://github.com/leomlck/nerve) (confidence: medium)
* **[Can Agents Distinguish Visually Hard-to-Separate Diseases in a Zero-Shot Setting? A Pilot Study](https://arxiv.org/abs/2602.22959v2)** - [Code](https://github.com/truhnlab/contrastive-agent-reasoning) (confidence: medium)
<!-- END GENERAL_PAPERS -->

---

**Repository Topics**: awesome, awesome-list, miccai, miccai2026, medical-imaging, deep-learning, computer-vision, segmentation, reconstruction, classification, medical-image-analysis, artificial-intelligence

**Conference Scope**: miccai-2026
**Discovery Mode**: broad

**Last Updated**: 2026-06-19 12:29 北京时间 by GitHub Actions

**License**: Apache License 2.0
