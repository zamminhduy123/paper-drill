---
title: "An Empirical Comparative Review of Classifiers for Real-Time IoT Cyber Attack Detection"
year: 2026
doi: "https://doi.org/10.19139/soic-2310-5070-4092"
relevance_score: 0.88
type: paper
---
# An Empirical Comparative Review of Classifiers for Real-Time IoT Cyber Attack Detection

## Novelty
Empirical comparative evaluation of ten classifiers for real-time IoT intrusion detection on RT-IoT2022, with a compact 15-feature subset selected by consensus LightGBM and CatBoost feature importances, deployment-cost profiling, statistical significance testing, and external validation on NSL-KDD.

## Methodology
Ten classifiers are evaluated on RT-IoT2022 using the full 83-feature space and a reduced 15-feature subset. Experiments use stratified five-fold cross-validation, SMOTE for minority-attack recall, 95% confidence intervals, paired McNemar and Wilcoxon tests with Holm-Bonferroni correction, training and per-flow inference cost measurement, and external validation on NSL-KDD.

## Explicit Limitations
Not stated in the provided abstract.

## Future Work
Not explicitly stated; the abstract implies future development of adaptive, lightweight, and interpretable IoT intrusion detection systems.

## Concept Hubs
[[Concept - IoT Intrusion Detection]]
[[Concept - Feature Selection]]
[[Concept - Class Imbalance]]
[[Concept - Cross-Dataset Evaluation]]
[[Concept - Lightweight Detection]]

## Relevance Score
0.88

## Monitoring Transfer
doi: not stated
source_link: not stated
text_kind: empirical comparative review
monitoring_problem: real-time IoT network intrusion detection
signal: network traffic features, including full 83-feature and compact 15-feature representations
uncertainty_method: 95% confidence intervals and Holm-Bonferroni-corrected paired McNemar and Wilcoxon tests
action: classify traffic as benign or attack and select a lightweight detector
eval_setting: stratified five-fold cross-validation on RT-IoT2022 with external validation on NSL-KDD
limitation_author: not stated
limitation_inference: high reported accuracy may not generalize to unseen attacks, adversarial traffic, or non-IoT domains
limitation_unknown: not stated
support_passage: Experiments indicate that tree-based ensembles, CatBoost, XGBoost, and LightGBM, achieve the best performance, producing accuracy and AUC values above 99.7% and 99.9%, respectively, for both feature configurations.
transfer_ivn: apply compact feature selection and tree-based ensembles to real-time in-vehicle network intrusion detection
transfer_risk: IVN traffic has safety-critical latency constraints and protocol-specific dynamics that IoT traffic features may not capture

#needs-review

## Record Fields
doi: https://doi.org/10.19139/soic-2310-5070-4092
source_link: not stated
text_kind: abstract
monitoring_problem: real-time IoT network intrusion detection
signal: network traffic features, including full 83-feature and compact 15-feature representations
uncertainty_method: 95% confidence intervals and Holm-Bonferroni-corrected paired McNemar and Wilcoxon tests
action: classify traffic as benign or attack and select a lightweight detector
eval_setting: stratified five-fold cross-validation on RT-IoT2022 with external validation on NSL-KDD
limitation_author: not stated
limitation_inference: high reported accuracy may not generalize to unseen attacks, adversarial traffic, or non-IoT domains
limitation_unknown: not stated
support_passage: Experiments indicate that tree-based ensembles, CatBoost, XGBoost, and LightGBM, achieve the best performance, producing accuracy and AUC values above 99.7% and 99.9%, respectively, for both feature configurations.
transfer_ivn: apply compact feature selection and tree-based ensembles to real-time in-vehicle network intrusion detection
transfer_risk: IVN traffic has safety-critical latency constraints and protocol-specific dynamics that IoT traffic features may not capture
