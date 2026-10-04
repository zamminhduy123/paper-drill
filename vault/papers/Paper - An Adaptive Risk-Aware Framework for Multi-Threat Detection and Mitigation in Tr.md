---
title: "An Adaptive Risk-Aware Framework for Multi-Threat Detection and Mitigation in Trustworthy Artificial Intelligence Systems"
year: 2026
doi: "https://doi.org/10.5281/zenodo.23046517"
relevance_score: 3.0
type: paper
---
# An Adaptive Risk-Aware Framework for Multi-Threat Detection and Mitigation in Trustworthy Artificial Intelligence Systems

## Novelty
The work proposes a risk-aware adversarial machine learning prototype, TrustGuard-AI, that combines classification, adversarial perturbation testing, threat detection, composite risk scoring, and selective abstention. It also includes separate experiments for label-flipping, feature-trigger backdoor attacks, and confidence-based membership inference.

## Methodology
The notebook uses an embedded synthetic dataset of 1,600 labeled records with preprocessing for missing values, numerical standardization, and categorical encoding. It trains logistic regression, random forest, and histogram gradient boosting classifiers. Gradient-sign and projected iterative evasion attacks are applied to the logistic regression model. A threat detector and composite risk score are calibrated on validation data, then used for risk-based routing with monitoring, review flags, and abstention. Ablation and sensitivity analyses examine risk routing and uncertainty weighting. Evaluation includes predictive accuracy, macro-F1, ROC-AUC, attack success, detection performance, and prediction coverage.

## Explicit Limitations
The release uses synthetic data only. Loaders are provided for UNSW-NB15 and CICIDS2017, but those official datasets are not included or evaluated. The notebook is a research prototype, not a complete implementation of TrustGuard-AI. Automated mitigation selection, the proposed MLP/ART pipeline, and privacy defenses are outside the implemented scope. Synthetic demonstration results do not substantiate the illustrative performance values in the associated manuscript. Reductions in accepted attack success must be interpreted alongside abstention and prediction coverage.

## Future Work
Future work should evaluate the framework on real enterprise/internet network intrusion datasets such as UNSW-NB15 and CICIDS2017, implement the full TrustGuard-AI architecture, add automated mitigation selection, complete the MLP/ART pipeline, incorporate privacy defenses, and test the approach under realistic network traffic and latency constraints.

## Concept Hubs
[[Concept - AI-Ready Security Framework]]
[[Concept - Adversarial Training]]
[[Concept - Anomaly Detection]]
[[Concept - Intrusion Detection]]
[[Concept - Threshold Control]]

## Relevance Score
3/10

## Monitoring Transfer
doi: not stated
source_link: not stated
text_kind: abstract
monitoring_problem: detecting adversarial threats and unreliable predictions in machine learning classification pipelines
signal: composite risk score, threat detector output, model confidence, and perturbation bounds
uncertainty_method: selective abstention, risk-based routing, validation-calibrated thresholds, and uncertainty weighting
action: route predictions to monitoring, raise review flags, or abstain from final prediction
eval_setting: synthetic embedded dataset with per-seed measurements of accuracy, macro-F1, ROC-AUC, attack success, detection performance, and prediction coverage
limitation_author: synthetic data only; UNSW-NB15 and CICIDS2017 are not included or evaluated; not a complete TrustGuard-AI implementation; automated mitigation, MLP/ART pipeline, and privacy defenses are outside scope; synthetic results do not substantiate manuscript performance values
limitation_inference: not directly evaluated on enterprise/internet network intrusion detection; uses shallow classifiers rather than deep learning; abstention-based routing may reduce prediction coverage; transfer to in-vehicle networks may be constrained by latency and domain shift
limitation_unknown: not stated
support_passage: The embedded data are synthetic and enable execution without downloading a dataset. Loaders and instructions are provided for separately obtained UNSW-NB15 and CICIDS2017 CSV files; these official datasets are not included or evaluated in this release.
transfer_ivn: apply risk-scored threat detection and selective abstention to in-vehicle network traffic monitoring, flagging suspicious messages for review
transfer_risk: may fail because in-vehicle networks require deterministic low-latency response and real traffic lacks the synthetic calibration labels and risk thresholds used in the notebook

#needs-review

## Record Fields
doi: https://doi.org/10.5281/zenodo.23046517
source_link: not stated
text_kind: abstract
monitoring_problem: detecting adversarial threats and unreliable predictions in machine learning classification pipelines
signal: composite risk score, threat detector output, model confidence, and perturbation bounds
uncertainty_method: selective abstention, risk-based routing, validation-calibrated thresholds, and uncertainty weighting
action: route predictions to monitoring, raise review flags, or abstain from final prediction
eval_setting: synthetic embedded dataset with per-seed measurements of accuracy, macro-F1, ROC-AUC, attack success, detection performance, and prediction coverage
limitation_author: synthetic data only; UNSW-NB15 and CICIDS2017 are not included or evaluated; not a complete TrustGuard-AI implementation; automated mitigation, MLP/ART pipeline, and privacy defenses are outside scope; synthetic results do not substantiate manuscript performance values
limitation_inference: not directly evaluated on enterprise/internet network intrusion detection; uses shallow classifiers rather than deep learning; abstention-based routing may reduce prediction coverage; transfer to in-vehicle networks may be constrained by latency and domain shift
limitation_unknown: not stated
support_passage: The embedded data are synthetic and enable execution without downloading a dataset. Loaders and instructions are provided for separately obtained UNSW-NB15 and CICIDS2017 CSV files; these official datasets are not included or evaluated in this release.
transfer_ivn: apply risk-scored threat detection and selective abstention to in-vehicle network traffic monitoring, flagging suspicious messages for review
transfer_risk: may fail because in-vehicle networks require deterministic low-latency response and real traffic lacks the synthetic calibration labels and risk thresholds used in the notebook
