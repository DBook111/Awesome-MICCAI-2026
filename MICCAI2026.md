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
- Total code-backed papers: `79`
- Fetched arXiv records: `811`
- Unique arXiv records: `613`
- Filtered (non-target): `407`
- Filtered (track): `30`
- Filtered (no code links): `97`

| Category | Count | Gap to 1000 |
|---|---:|---:|
| Segmentation | 25 | 975 |
| Reconstruction | 14 | 986 |
| Classification | 33 | 967 |
| Image Registration | 17 | 983 |
| Domain Adaptation | 4 | 996 |
| Generative Models | 19 | 981 |
| Fundus Imaging | 6 | 994 |
| OCT | 3 | 997 |
| OCTA | 0 | 1000 |
| Ophthalmic Foundation Models | 13 | 987 |
| General | 9 | 991 |
<!-- END COVERAGE_REPORT -->

## 📊 Segmentation

*This list is automatically generated. See any issues? Please open a pull request!*

<!-- BEGIN SEGMENTATION_PAPERS -->
* **[Controllable Generation of Diverse Dermatological Imagery for Fair and Efficient Malignancy Classification](https://arxiv.org/abs/2607.12987v2)** - [Code](https://github.com/hectorcarrion/controllablegenddi) (confidence: high)
* **[Decouple and Reason: Anatomically Guided Two-Stage Voxel-Level Grounding of Free-Text Findings in 3D Chest CT](https://arxiv.org/abs/2607.12602v1)** - [Code](https://github.com/khuhm/dagg) (confidence: medium)
* **[Probe-EM: Targeted Neuron Tracing via Training-Free Semantic Verification](https://arxiv.org/abs/2607.04696v1)** - [Code](https://github.com/headliuyun/probe-em) (confidence: medium)
* **[Self-Supervised Temporal Regularization for Landmark-Based Cardiac Segmentation with Automatic AHA Regional Mapping](https://arxiv.org/abs/2606.31785v1)** - [Code](https://github.com/david-montalvoo/maskhybridgnet-tempreg) (confidence: high)
* **[Distilling Temporal Coherence into 2D Networks for Transrectal Ultrasound Prostate Video Segmentation](https://arxiv.org/abs/2606.31198v1)** - [Code](https://github.com/dydevelop/dtc-trus) (confidence: high)
* **[Set-Inclusive Uncertainty Modeling for Robust Brain Tumor Segmentation](https://arxiv.org/abs/2606.30374v1)** - [Code](https://github.com/atlas-sky/sium) (confidence: high)
* **[Controllable Histopathology Image Synthesis with Training-free Structural Initialization and Textural Modulation](https://arxiv.org/abs/2606.27935v2)** - [Code](https://github.com/ibil-code/chis) (confidence: high)
* **[Mask to Concept: Auto-Promptable SAM3 via Efficient Test-Time Concept Embedding Search for Few-Shot Annotation](https://arxiv.org/abs/2606.26711v2)** - [Code](https://github.com/huster-hq/m2c) (confidence: high)
* **[Interpretable Probabilistic Medical Image Segmentation via Gaussian Process with Explicit Modelling of Annotation Bias and Variability](https://arxiv.org/abs/2606.23177v1)** - [Code](https://github.com/qili111/gps-var) (confidence: high)
* **[Surgical Anatomy Recognition with Context Learning using Foundation Representations](https://arxiv.org/abs/2606.22124v1)** - [Code](https://github.com/timjaspers0801/atlas) (confidence: medium)
* **[Rethinking the Adaptation of Vision Foundation Models for Efficient Cell Segmentation](https://arxiv.org/abs/2606.21913v1)** - [Code](https://github.com/xq141839/efficell-seg) (confidence: high)
* **[Single-Stage Hierarchical Rectification for Weakly Supervised Histopathology Segmentation](https://arxiv.org/abs/2606.20250v1)** - [Code](https://github.com/trongduc-nguyen/sshr) (confidence: high)
* **[CSWinUNETR: Segmentation of Thin Anatomical Structures in Medical Images](https://arxiv.org/abs/2606.19824v1)** - [Code](https://github.com/labhai/cswinunetr) (confidence: high)
* **[Quantification of Uncertainty with Adversarial Models in Medical Image Segmentation](https://arxiv.org/abs/2606.18860v1)** - [Code](https://github.com/hanajebril/quam_sm) (confidence: high)
* **[Beyond Visual Cues: CoT-Enhanced Reasoning for Semi-supervised Medical Image Segmentation](https://arxiv.org/abs/2606.17958v1)** - [Code](https://github.com/cymasuna/cers) (confidence: high)
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
* **[DermDepth: Toward Monocular Metric Scale 3D Reconstruction Models for Dermatology](https://arxiv.org/abs/2607.13010v2)** - [Code](https://github.com/hectorcarrion/dermdepth) (confidence: high)
* **[Probe-EM: Targeted Neuron Tracing via Training-Free Semantic Verification](https://arxiv.org/abs/2607.04696v1)** - [Code](https://github.com/headliuyun/probe-em) (confidence: high)
* **[Anatomy-Grounded Synthetic Coronary Angiography for Geometry-Informed Multi-View Matching](https://arxiv.org/abs/2606.28474v1)** - [Code](https://github.com/medipixel/gimm) (confidence: medium)
* **[NeuroSonic: Conditional Flow Matching for EEG-to-Speech Reconstruction](https://arxiv.org/abs/2606.24087v1)** - [Code](https://github.com/y-research-sbu/neurosonic) (confidence: high)
* **[MaRS: Robust Out-of-Distribution Detection via Mahalanobis Residual Scoring](https://arxiv.org/abs/2606.22649v2)** - [Code](https://github.com/francescodisalvo05/mars) (confidence: medium)
* **[When, Where, and How: Adaptive Binning for Tabular Self-Supervised Learning](https://arxiv.org/abs/2606.19827v1)** - [Code](https://github.com/labhai/adaptive-binning) (confidence: medium)
* **[Test-Time Adaptation in Optical Coherence Tomography Using Trajectory-Aligned Time-Independent Flow](https://arxiv.org/abs/2606.18876v2)** - [Code](https://github.com/veit21/tta-flow) (confidence: medium)
* **[Propagating Structural Guidance: Synthesizing Fluorescein Angiography from Fundus Images and Sparse OCT Scans](https://arxiv.org/abs/2606.16234v1)** - [Code](https://github.com/while-plus/oct-guide-ffa-syn) (confidence: medium)
* **[Learning Directional Semantic Transitions for Longitudinal Chest X-ray Analysis](https://arxiv.org/abs/2606.15938v1)** - [Code](https://github.com/rpidial/protrans) (confidence: medium)
* **[Anatomy-Anchored Self-Supervision: Distilling Vision Foundation Models for Invariant Ultrasound Representation](https://arxiv.org/abs/2605.25402v3)** - [Code](https://github.com/zhcz328/anaus) (confidence: medium)
* **[Defining Robust Ultrasound Quality Metrics via an Ultrasound Foundation Model](https://arxiv.org/abs/2604.19512v2)** - [Code](https://github.com/sextant-fable/us-metrics) (confidence: medium)
* **[VecHeart: Holistic Four-Chamber Cardiac Anatomy Modeling via Hybrid VecSets](https://arxiv.org/abs/2604.19403v2)** - [Code](https://github.com/scalsol/vecheart) (confidence: medium)
* **[EchoLVFM: One-Step Video Generation via Latent Flow Matching for Echocardiogram Synthesis](https://arxiv.org/abs/2603.13967v1)** - [Code](https://github.com/engemmanuel/echolvfm) (confidence: medium)
* **[Diverse Normal Prototypes-Guided Contrastive Reconstruction for Medical Anomaly Detection](https://arxiv.org/abs/2508.19573v2)** - [Code](https://github.com/liluhu0/dnp-conformer) (confidence: high)
<!-- END RECONSTRUCTION_PAPERS -->

## 🏷️ Classification

*This list is automatically generated. See any issues? Please open a pull request!*

<!-- BEGIN CLASSIFICATION_PAPERS -->
* **[Controllable Generation of Diverse Dermatological Imagery for Fair and Efficient Malignancy Classification](https://arxiv.org/abs/2607.12987v2)** - [Code](https://github.com/hectorcarrion/controllablegenddi) (confidence: high)
* **[Decouple and Reason: Anatomically Guided Two-Stage Voxel-Level Grounding of Free-Text Findings in 3D Chest CT](https://arxiv.org/abs/2607.12602v1)** - [Code](https://github.com/khuhm/dagg) (confidence: medium)
* **[Longitudinal Multi-View Breast Cancer Risk Prediction](https://arxiv.org/abs/2607.11343v1)** - [Code](https://github.com/sot176/lmv-net) (confidence: medium)
* **[Compass: Prostate Cancer Detection Needs Multi-View Context](https://arxiv.org/abs/2607.06919v1)** - [Code](https://github.com/mharmanani/compass) (confidence: high)
* **[Boosting Ultrasound Image Classification via Attribute-Guided Dual-Branch Framework](https://arxiv.org/abs/2607.01648v1)** - [Code](https://github.com/zhaobo253-crypto/attrguide) (confidence: high)
* **[FrameONE: Hierarchical Motion Modeling for Universal Multi-View Echocardiographic Keyframe Detection](https://arxiv.org/abs/2607.00748v1)** - [Code](https://github.com/szuboy/frameone) (confidence: high)
* **[Self-Supervised Temporal Regularization for Landmark-Based Cardiac Segmentation with Automatic AHA Regional Mapping](https://arxiv.org/abs/2606.31785v1)** - [Code](https://github.com/david-montalvoo/maskhybridgnet-tempreg) (confidence: medium)
* **[Learning Where to Look: A Reinforcement Learning Framework for Robust Micro-Ultrasound Prostate Cancer Detection](https://arxiv.org/abs/2606.30951v1)** - [Code](https://github.com/deeprcl/prost-rl) (confidence: high)
* **[MammoFlow: Multiview Mammogram Synthesis with Anatomically Consistent Flow Matching](https://arxiv.org/abs/2606.28537v1)** - [Code](https://github.com/xypb/mammoflow) (confidence: medium)
* **[Pulmonary Embolism Risk Stratification from CTPA and Medical Records: Vascular Graphs Are Not All You Need](https://arxiv.org/abs/2606.25956v2)** - [Code](https://github.com/creatis-myriad/genesis) (confidence: medium)
* **[FunPiQ: A New Benchmark for Pixel-Level Quality Assessment in Fundus Images](https://arxiv.org/abs/2606.25915v1)** - [Code](https://github.com/penway/funpiq) (confidence: high)
* **[From Point Estimates to Distributions: GMM Pooling for MIL in Preterm Birth Prediction](https://arxiv.org/abs/2606.23005v1)** - [Code](https://github.com/hussainalasmawi/gmm_pooling) (confidence: medium)
* **[Evo-RAD: Navigating Rare Retinal Disease Diagnosis via Self-Evolving Agentic Retrieval](https://arxiv.org/abs/2606.22955v1)** - [Code](https://github.com/sdh-lab/evo-rad) (confidence: medium)
* **[MaRS: Robust Out-of-Distribution Detection via Mahalanobis Residual Scoring](https://arxiv.org/abs/2606.22649v2)** - [Code](https://github.com/francescodisalvo05/mars) (confidence: high)
* **[Surgical Anatomy Recognition with Context Learning using Foundation Representations](https://arxiv.org/abs/2606.22124v1)** - [Code](https://github.com/timjaspers0801/atlas) (confidence: high)
* **[One-Shot Data Selection for Medical Image Classification via Graph Coverage](https://arxiv.org/abs/2606.22002v1)** - [Code](https://github.com/zahiriddin-rustamov/graph-coverage-selection) (confidence: high)
* **[MedTS-TTT: Test-Time Training for Medical Time Series Classification](https://arxiv.org/abs/2606.21329v1)** - [Code](https://github.com/mingzhi-c/medts-ttt) (confidence: high)
* **[A Neurosymbolic Framework for Interpretable Skeleton-Based Seizure Detection via Concept-Driven Logical Reasoning](https://arxiv.org/abs/2606.21252v2)** - [Code](https://github.com/mr-talhailyas/cdsd) (confidence: high)
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
* **[Wasserstein-Aligned Localisation for VLM-Based Distributional OOD Detection in Medical Imaging](https://arxiv.org/abs/2605.05161v2)** - [Code](https://github.com/bkainz/waldo_miccai26_demo) (confidence: high)
* **[Exemplar Diffusion: Improving Medical Object Detection with Opportunistic Labels](https://arxiv.org/abs/2603.15267v1)** - [Code](https://github.com/waahlstrand/exemplardiffusion) (confidence: high)
* **[Evidential Perfusion Physics-Informed Neural Networks with Residual Uncertainty Quantification](https://arxiv.org/abs/2603.09359v2)** - [Code](https://github.com/jhlee0619/eppinn) (confidence: medium)
* **[Echo2ECG: Enhancing ECG Representations with Cardiac Morphology from Multi-View Echos](https://arxiv.org/abs/2603.08505v2)** - [Code](https://github.com/michelleespranita/echo2ecg) (confidence: medium)
* **[Diverse Normal Prototypes-Guided Contrastive Reconstruction for Medical Anomaly Detection](https://arxiv.org/abs/2508.19573v2)** - [Code](https://github.com/liluhu0/dnp-conformer) (confidence: high)
<!-- END CLASSIFICATION_PAPERS -->

## 🔄 Image Registration

*This list is automatically generated. See any issues? Please open a pull request!*

<!-- BEGIN IMAGE_REGISTRATION_PAPERS -->
* **[Decouple and Reason: Anatomically Guided Two-Stage Voxel-Level Grounding of Free-Text Findings in 3D Chest CT](https://arxiv.org/abs/2607.12602v1)** - [Code](https://github.com/khuhm/dagg) (confidence: medium)
* **[Longitudinal Multi-View Breast Cancer Risk Prediction](https://arxiv.org/abs/2607.11343v1)** - [Code](https://github.com/sot176/lmv-net) (confidence: medium)
* **[KOAL: Knowledge-Driven Prostate Cancer Grading with Ordinal-Aware Learning](https://arxiv.org/abs/2607.06019v1)** - [Code](https://github.com/gother-gz/koal) (confidence: medium)
* **[Distilling Temporal Coherence into 2D Networks for Transrectal Ultrasound Prostate Video Segmentation](https://arxiv.org/abs/2606.31198v1)** - [Code](https://github.com/dydevelop/dtc-trus) (confidence: medium)
* **[MammoFlow: Multiview Mammogram Synthesis with Anatomically Consistent Flow Matching](https://arxiv.org/abs/2606.28537v1)** - [Code](https://github.com/xypb/mammoflow) (confidence: medium)
* **[MedTS-TTT: Test-Time Training for Medical Time Series Classification](https://arxiv.org/abs/2606.21329v1)** - [Code](https://github.com/mingzhi-c/medts-ttt) (confidence: medium)
* **[OTCHA: Optimal Transport-driven Confidence-aware Latent Hub Alignment for Multi-View Medical Image Classification](https://arxiv.org/abs/2606.19838v1)** - [Code](https://github.com/labhai/otcha) (confidence: high)
* **[Propagating Structural Guidance: Synthesizing Fluorescein Angiography from Fundus Images and Sparse OCT Scans](https://arxiv.org/abs/2606.16234v1)** - [Code](https://github.com/while-plus/oct-guide-ffa-syn) (confidence: medium)
* **[WaveDiT: Distribution-Aware Wavelet Flow Matching for Efficient 3D Brain MRI Synthesis](https://arxiv.org/abs/2606.08670v1)** - [Code](https://github.com/sisinflab/wavedit) (confidence: medium)
* **[Genetically Aligned Patient Representations Improve Hematological Diagnosis](https://arxiv.org/abs/2605.29980v1)** - [Code](https://github.com/marrlab/genbloom) (confidence: medium)
* **[Evi-Steer: Learning to Steer Biomedical Vision-Language Models through Efficient and Generalizable Evidential Tuning](https://arxiv.org/abs/2605.26292v2)** - [Code](https://github.com/healthx-lab/evi-steer) (confidence: medium)
* **[Anatomy-Anchored Self-Supervision: Distilling Vision Foundation Models for Invariant Ultrasound Representation](https://arxiv.org/abs/2605.25402v3)** - [Code](https://github.com/zhcz328/anaus) (confidence: medium)
* **[Subspace-Guided Semantic and Topological Invariant Registration for Annotation-Free Ultrasound Plane Quality Control](https://arxiv.org/abs/2605.25396v1)** - [Code](https://github.com/zhcz328/striq) (confidence: high)
* **[EchoTracker2: Enhancing Myocardial Point Tracking by Modeling Local Motion](https://arxiv.org/abs/2605.12140v1)** - [Code](https://github.com/riponazad/ptecho) (confidence: medium)
* **[VecHeart: Holistic Four-Chamber Cardiac Anatomy Modeling via Hybrid VecSets](https://arxiv.org/abs/2604.19403v2)** - [Code](https://github.com/scalsol/vecheart) (confidence: medium)
* **[Diverse Normal Prototypes-Guided Contrastive Reconstruction for Medical Anomaly Detection](https://arxiv.org/abs/2508.19573v2)** - [Code](https://github.com/liluhu0/dnp-conformer) (confidence: medium)
* **[Improving Factuality of 3D Brain MRI Report Generation with Paired Image-domain Retrieval and Text-domain Augmentation](https://arxiv.org/abs/2411.15490v3)** - [Code](https://github.com/jhlee0619/pirta) (confidence: medium)
<!-- END IMAGE_REGISTRATION_PAPERS -->

## 🔀 Domain Adaptation

*This list is automatically generated. See any issues? Please open a pull request!*

<!-- BEGIN DOMAIN_ADAPTATION_PAPERS -->
* **[ContiStain: Cross-Domain Relation-Preserving Distillation for Continual Multi-Domain Virtual IHC Staining](https://arxiv.org/abs/2607.03851v1)** - [Code](https://github.com/ccitachi/contistain) (confidence: high)
* **[MedTS-TTT: Test-Time Training for Medical Time Series Classification](https://arxiv.org/abs/2606.21329v1)** - [Code](https://github.com/mingzhi-c/medts-ttt) (confidence: medium)
* **[Evi-Steer: Learning to Steer Biomedical Vision-Language Models through Efficient and Generalizable Evidential Tuning](https://arxiv.org/abs/2605.26292v2)** - [Code](https://github.com/healthx-lab/evi-steer) (confidence: high)
* **[Anatomy-Anchored Self-Supervision: Distilling Vision Foundation Models for Invariant Ultrasound Representation](https://arxiv.org/abs/2605.25402v3)** - [Code](https://github.com/zhcz328/anaus) (confidence: medium)
<!-- END DOMAIN_ADAPTATION_PAPERS -->

## 🎨 Generative Models

*This list is automatically generated. See any issues? Please open a pull request!*

<!-- BEGIN GENERATIVE_MODELS_PAPERS -->
* **[Controllable Generation of Diverse Dermatological Imagery for Fair and Efficient Malignancy Classification](https://arxiv.org/abs/2607.12987v2)** - [Code](https://github.com/hectorcarrion/controllablegenddi) (confidence: high)
* **[Synergistic Perception-Reasoning Governance: Grounding Medical MLLMs with Verifiable Anatomical Evidence](https://arxiv.org/abs/2607.00060v1)** - [Code](https://github.com/henry991115/sprg) (confidence: medium)
* **[MammoFlow: Multiview Mammogram Synthesis with Anatomically Consistent Flow Matching](https://arxiv.org/abs/2606.28537v1)** - [Code](https://github.com/xypb/mammoflow) (confidence: high)
* **[Anatomy-Grounded Synthetic Coronary Angiography for Geometry-Informed Multi-View Matching](https://arxiv.org/abs/2606.28474v1)** - [Code](https://github.com/medipixel/gimm) (confidence: medium)
* **[Controllable Histopathology Image Synthesis with Training-free Structural Initialization and Textural Modulation](https://arxiv.org/abs/2606.27935v2)** - [Code](https://github.com/ibil-code/chis) (confidence: high)
* **[NeuroSonic: Conditional Flow Matching for EEG-to-Speech Reconstruction](https://arxiv.org/abs/2606.24087v1)** - [Code](https://github.com/y-research-sbu/neurosonic) (confidence: high)
* **[MaRS: Robust Out-of-Distribution Detection via Mahalanobis Residual Scoring](https://arxiv.org/abs/2606.22649v2)** - [Code](https://github.com/francescodisalvo05/mars) (confidence: medium)
* **[One-Shot Data Selection for Medical Image Classification via Graph Coverage](https://arxiv.org/abs/2606.22002v1)** - [Code](https://github.com/zahiriddin-rustamov/graph-coverage-selection) (confidence: medium)
* **[Single-Stage Hierarchical Rectification for Weakly Supervised Histopathology Segmentation](https://arxiv.org/abs/2606.20250v1)** - [Code](https://github.com/trongduc-nguyen/sshr) (confidence: medium)
* **[A Multi-Center Benchmark for Abdominal Disease Diagnosis and Report Generation from Non-Contrast CT](https://arxiv.org/abs/2606.16991v1)** - [Code](https://github.com/xmed-lab/trials-report) (confidence: high)
* **[Propagating Structural Guidance: Synthesizing Fluorescein Angiography from Fundus Images and Sparse OCT Scans](https://arxiv.org/abs/2606.16234v1)** - [Code](https://github.com/while-plus/oct-guide-ffa-syn) (confidence: medium)
* **[WaveDiT: Distribution-Aware Wavelet Flow Matching for Efficient 3D Brain MRI Synthesis](https://arxiv.org/abs/2606.08670v1)** - [Code](https://github.com/sisinflab/wavedit) (confidence: high)
* **[BrainAnytime: Anatomy-Aware Cross-Modal Pretraining for Brain Image Analysis with Arbitrary Modality Availability](https://arxiv.org/abs/2605.13059v1)** - [Code](https://github.com/sdh-lab/brainanytime) (confidence: medium)
* **[ScribbleDose: Scribble-Guided Dose Prediction in Radiotherapy](https://arxiv.org/abs/2605.11555v2)** - [Code](https://github.com/icherishxixixi/scribbledose) (confidence: medium)
* **[VecHeart: Holistic Four-Chamber Cardiac Anatomy Modeling via Hybrid VecSets](https://arxiv.org/abs/2604.19403v2)** - [Code](https://github.com/scalsol/vecheart) (confidence: medium)
* **[Exemplar Diffusion: Improving Medical Object Detection with Opportunistic Labels](https://arxiv.org/abs/2603.15267v1)** - [Code](https://github.com/waahlstrand/exemplardiffusion) (confidence: high)
* **[EchoLVFM: One-Step Video Generation via Latent Flow Matching for Echocardiogram Synthesis](https://arxiv.org/abs/2603.13967v1)** - [Code](https://github.com/engemmanuel/echolvfm) (confidence: high)
* **[DUCX: Decomposing Unfairness in Tool-Using Chest X-ray Agents](https://arxiv.org/abs/2603.00777v2)** - [Code](https://github.com/nanboy-ronan/duck) (confidence: medium)
* **[Improving Factuality of 3D Brain MRI Report Generation with Paired Image-domain Retrieval and Text-domain Augmentation](https://arxiv.org/abs/2411.15490v3)** - [Code](https://github.com/jhlee0619/pirta) (confidence: high)
<!-- END GENERATIVE_MODELS_PAPERS -->

## 👁️ Fundus Imaging

*This list is automatically generated. See any issues? Please open a pull request!*

<!-- BEGIN FUNDUS_IMAGING_PAPERS -->
* **[FunPiQ: A New Benchmark for Pixel-Level Quality Assessment in Fundus Images](https://arxiv.org/abs/2606.25915v1)** - [Code](https://github.com/penway/funpiq) (confidence: high)
* **[Evo-RAD: Navigating Rare Retinal Disease Diagnosis via Self-Evolving Agentic Retrieval](https://arxiv.org/abs/2606.22955v1)** - [Code](https://github.com/sdh-lab/evo-rad) (confidence: high)
* **[CSWinUNETR: Segmentation of Thin Anatomical Structures in Medical Images](https://arxiv.org/abs/2606.19824v1)** - [Code](https://github.com/labhai/cswinunetr) (confidence: high)
* **[Test-Time Adaptation in Optical Coherence Tomography Using Trajectory-Aligned Time-Independent Flow](https://arxiv.org/abs/2606.18876v2)** - [Code](https://github.com/veit21/tta-flow) (confidence: high)
* **[Propagating Structural Guidance: Synthesizing Fluorescein Angiography from Fundus Images and Sparse OCT Scans](https://arxiv.org/abs/2606.16234v1)** - [Code](https://github.com/while-plus/oct-guide-ffa-syn) (confidence: high)
* **[Clinical Graph-Mediated Distillation for Unpaired MRI-to-CFI Hypertension Prediction](https://arxiv.org/abs/2603.21809v1)** - [Code](https://github.com/dillanimans/cgmd-unpaired-distillation) (confidence: high)
<!-- END FUNDUS_IMAGING_PAPERS -->

## 🧿 OCT

*This list is automatically generated. See any issues? Please open a pull request!*

<!-- BEGIN OCT_PAPERS -->
* **[Evo-RAD: Navigating Rare Retinal Disease Diagnosis via Self-Evolving Agentic Retrieval](https://arxiv.org/abs/2606.22955v1)** - [Code](https://github.com/sdh-lab/evo-rad) (confidence: medium)
* **[Test-Time Adaptation in Optical Coherence Tomography Using Trajectory-Aligned Time-Independent Flow](https://arxiv.org/abs/2606.18876v2)** - [Code](https://github.com/veit21/tta-flow) (confidence: high)
* **[Propagating Structural Guidance: Synthesizing Fluorescein Angiography from Fundus Images and Sparse OCT Scans](https://arxiv.org/abs/2606.16234v1)** - [Code](https://github.com/while-plus/oct-guide-ffa-syn) (confidence: high)
<!-- END OCT_PAPERS -->

## 🩸 OCTA

*This list is automatically generated. See any issues? Please open a pull request!*

<!-- BEGIN OCTA_PAPERS -->
<!-- END OCTA_PAPERS -->

## 🧠👁️ Ophthalmic Foundation Models

*This list is automatically generated. See any issues? Please open a pull request!*

<!-- BEGIN OPHTHALMIC_FOUNDATION_MODELS_PAPERS -->
* **[Foundation Model-driven Key Anatomy Frame Selection for Blind-sweep Ultrasound Fetal Birth Weight Estimation](https://arxiv.org/abs/2607.00745v1)** - [Code](https://github.com/ouleoule/blindsweep-ebw) (confidence: high)
* **[FunPiQ: A New Benchmark for Pixel-Level Quality Assessment in Fundus Images](https://arxiv.org/abs/2606.25915v1)** - [Code](https://github.com/penway/funpiq) (confidence: high)
* **[Evo-RAD: Navigating Rare Retinal Disease Diagnosis via Self-Evolving Agentic Retrieval](https://arxiv.org/abs/2606.22955v1)** - [Code](https://github.com/sdh-lab/evo-rad) (confidence: high)
* **[One-Shot Data Selection for Medical Image Classification via Graph Coverage](https://arxiv.org/abs/2606.22002v1)** - [Code](https://github.com/zahiriddin-rustamov/graph-coverage-selection) (confidence: medium)
* **[Rethinking the Adaptation of Vision Foundation Models for Efficient Cell Segmentation](https://arxiv.org/abs/2606.21913v1)** - [Code](https://github.com/xq141839/efficell-seg) (confidence: high)
* **[CSWinUNETR: Segmentation of Thin Anatomical Structures in Medical Images](https://arxiv.org/abs/2606.19824v1)** - [Code](https://github.com/labhai/cswinunetr) (confidence: high)
* **[Test-Time Adaptation in Optical Coherence Tomography Using Trajectory-Aligned Time-Independent Flow](https://arxiv.org/abs/2606.18876v2)** - [Code](https://github.com/veit21/tta-flow) (confidence: high)
* **[Propagating Structural Guidance: Synthesizing Fluorescein Angiography from Fundus Images and Sparse OCT Scans](https://arxiv.org/abs/2606.16234v1)** - [Code](https://github.com/while-plus/oct-guide-ffa-syn) (confidence: high)
* **[Mutual Distillation of Dual-Foundation Models for Semi-Supervised PET/CT Segmentation](https://arxiv.org/abs/2606.15611v1)** - [Code](https://github.com/wu-beining/muduo) (confidence: high)
* **[Anatomy-Anchored Self-Supervision: Distilling Vision Foundation Models for Invariant Ultrasound Representation](https://arxiv.org/abs/2605.25402v3)** - [Code](https://github.com/zhcz328/anaus) (confidence: high)
* **[BrainAnytime: Anatomy-Aware Cross-Modal Pretraining for Brain Image Analysis with Arbitrary Modality Availability](https://arxiv.org/abs/2605.13059v1)** - [Code](https://github.com/sdh-lab/brainanytime) (confidence: medium)
* **[Defining Robust Ultrasound Quality Metrics via an Ultrasound Foundation Model](https://arxiv.org/abs/2604.19512v2)** - [Code](https://github.com/sextant-fable/us-metrics) (confidence: high)
* **[Clinical Graph-Mediated Distillation for Unpaired MRI-to-CFI Hypertension Prediction](https://arxiv.org/abs/2603.21809v1)** - [Code](https://github.com/dillanimans/cgmd-unpaired-distillation) (confidence: high)
<!-- END OPHTHALMIC_FOUNDATION_MODELS_PAPERS -->

## 📚 General

*This list is automatically generated. See any issues? Please open a pull request!*

<!-- BEGIN GENERAL_PAPERS -->
* **[ENC-ODE: Event-level Neurodegenerative Modeling in Continuous Time with Neural ODEs](https://arxiv.org/abs/2606.30398v1)** - [Code](https://github.com/jardindelsol/enc-ode) (confidence: medium)
* **[Re-mixing Embeddings for Patient Augmentation in Data Scarce Multiple Instance Learning](https://arxiv.org/abs/2606.25770v1)** - [Code](https://github.com/marrlab/recipe) (confidence: medium)
* **[AGE-MIL: Anchor-Guided Evidence Learning for Patient-Level Prediction](https://arxiv.org/abs/2606.12126v1)** - [Code](https://github.com/wodeniua/age-mil) (confidence: medium)
* **[StrokeTimer: Robust Representation Learning for Ischemic Stroke Onset-Time Estimation from Non-contrast CT](https://arxiv.org/abs/2606.04722v1)** - [Code](https://github.com/brainvas/stroketimer) (confidence: medium)
* **[BCER Agent: Reliable Long-Horizon MRI Workflow Execution via Compilation, Artifact Binding, and Bounded Local Recovery](https://arxiv.org/abs/2605.29163v1)** - [Code](https://github.com/albertlongzi/bcer) (confidence: medium)
* **[BioFact-MoE: Biologically Factorized Mixture of Experts for Vision-Language Prognostic Modeling in Hepatocellular Carcinoma](https://arxiv.org/abs/2605.26376v1)** - [Code](https://github.com/jy-639/biofact-moe) (confidence: medium)
* **[Network-Aware Bilinear Tokenization for Brain Functional Connectivity Representation Learning](https://arxiv.org/abs/2605.14048v3)** - [Code](https://github.com/leomlck/nerve) (confidence: medium)
* **[UltraStar: Semantic-Aware Star Graph Modeling for Echocardiography Navigation](https://arxiv.org/abs/2603.01461v2)** - [Code](https://github.com/leaplabthu/ultrastar) (confidence: medium)
* **[Can Agents Distinguish Visually Hard-to-Separate Diseases in a Zero-Shot Setting? A Pilot Study](https://arxiv.org/abs/2602.22959v2)** - [Code](https://github.com/truhnlab/contrastive-agent-reasoning) (confidence: medium)
<!-- END GENERAL_PAPERS -->

---

**Repository Topics**: awesome, awesome-list, miccai, miccai2026, medical-imaging, deep-learning, computer-vision, segmentation, reconstruction, classification, medical-image-analysis, artificial-intelligence

**Conference Scope**: miccai-2026
**Discovery Mode**: broad

**Last Updated**: 2026-07-20 11:08 北京时间 by GitHub Actions

**License**: Apache License 2.0
