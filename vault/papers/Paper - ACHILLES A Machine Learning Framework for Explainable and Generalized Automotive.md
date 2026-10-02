---
title: "ACHILLES: A Machine Learning Framework for Explainable and Generalized Automotive Intrusion Detection System"
year: 2026
doi: "10.1109/TITS.2026.3688299"
relevance_score: 9.0
type: paper
---
# ACHILLES: A Machine Learning Framework for Explainable and Generalized Automotive Intrusion Detection System

## Novelty
ACHILLES proposes a centralized-training, decentralized-execution automotive intrusion detection framework that combines standardized vendor-agnostic CAN telemetry features, meta-learning-based model selection, and SHAP-based explainability to improve cross-dataset generalization and trustworthiness.

## Methodology
The framework uses CAN message timing and frequency statistics instead of raw payload content to build standardized feature formats. Multiple ML models, including DNN and Random Forest, are trained centrally, with a meta-learning process selecting effective model configurations and hyperparameters. SHAP is used to evaluate feature importance and explainability. Performance is evaluated on four CAN-bus datasets containing real and advanced attacks, especially under cross train-test settings.

## Explicit Limitations
not stated

## Future Work
not stated

## Concept Hubs
[[Concept - CAN Intrusion Detection]] [[Concept - In-Vehicle Network Security]] [[Concept - Deep Learning Intrusion Detection]] [[Concept - Cross-Dataset Evaluation]] [[Concept - Explainable Intrusion Detection]]

## Relevance Score
9/10

## Monitoring Transfer
doi: 10.1109/TITS.2026.3688299
source_link: not stated
text_kind: journal article
monitoring_problem: detecting cyberattacks in in-vehicle CAN networks
signal: CAN message timing and frequency statistics
uncertainty_method: not stated
action: deploy centrally trained explainable IDS models to onboard ECUs for intrusion detection
eval_setting: four CAN-bus datasets with real and advanced attacks under cross train-test settings
limitation_author: not stated
limitation_inference: reliance on timing and frequency features may miss payload-dependent attacks
limitation_unknown: not stated
support_passage: we use CAN telemetry statistics (timing, frequency) instead of raw frames, reducing dependence on OEM-specific content
transfer_ivn: monitor IVN gateway traffic using standardized CAN timing and frequency features with centralized meta-learning and SHAP-based explanation
transfer_risk: payload-based or encrypted attacks may evade detection if only timing and frequency features are used

#needs-review

## Record Fields
doi: 10.1109/TITS.2026.3688299
source_link: not stated
text_kind: fulltext
monitoring_problem: detecting cyberattacks in in-vehicle CAN networks
signal: CAN message timing and frequency statistics
uncertainty_method: not stated
action: deploy centrally trained explainable IDS models to onboard ECUs for intrusion detection
eval_setting: four CAN-bus datasets with real and advanced attacks under cross train-test settings
limitation_author: not stated
limitation_inference: reliance on timing and frequency features may miss payload-dependent attacks
limitation_unknown: not stated
support_passage: we use CAN telemetry statistics (timing, frequency) instead of raw frames, reducing dependence on OEM-specific content
transfer_ivn: monitor IVN gateway traffic using standardized CAN timing and frequency features with centralized meta-learning and SHAP-based explanation
transfer_risk: payload-based or encrypted attacks may evade detection if only timing and frequency features are used
