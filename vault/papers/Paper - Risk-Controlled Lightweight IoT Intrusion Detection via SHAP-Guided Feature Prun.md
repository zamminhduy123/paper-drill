---
title: "Risk-Controlled Lightweight IoT Intrusion Detection via SHAP-Guided Feature Pruning and Conformal Prediction"
year: 2026
doi: "10.1109/SmartIoT70864.2026.00014"
relevance_score: 7.0
type: paper
---
# Risk-Controlled Lightweight IoT Intrusion Detection via SHAP-Guided Feature Pruning and Conformal Prediction

## Novelty
Couples SHAP-guided feature pruning with split conformal selective prediction for lightweight IoT intrusion detection, reducing features from 46 to 15 while controlling decision risk.

## Methodology
Benchmarks six classifiers on a grouped 8-class CICIoT2023 setting, selects LightGBM, prunes features using SHAP, and applies split conformal prediction to accept singleton prediction sets while deferring non-singleton or empty sets.

## Explicit Limitations
not stated

## Future Work
not stated

## Concept Hubs
[[Concept - IoT Intrusion Detection]], [[Concept - Lightweight Detection]], [[Concept - Feature Selection]], [[Concept - Explainable Intrusion Detection]], [[Concept - Conformal Prediction]]

## Relevance Score
7

## Monitoring Transfer
The paper monitors IoT network traffic using pruned flow features and conformal uncertainty to accept or defer intrusion decisions.

doi: 10.1109/SmartIoT70864.2026.00014
source_link: not stated
text_kind: conference paper
monitoring_problem: IoT intrusion detection on resource-constrained edge devices with uncertain traffic
signal: network-flow features from CICIoT2023, reduced from 46 to 15 features
uncertainty_method: split conformal prediction on pruned LightGBM
action: accept singleton prediction sets; defer non-singleton or empty sets
eval_setting: grouped 8-class CICIoT2023 at 90% target coverage
limitation_author: not stated
limitation_inference: conformal coverage assumes exchangeability, which may not hold for nonstationary IoT traffic
limitation_unknown: not stated
support_passage: split conformal prediction is added to the pruned backbone to translate predictive uncertainty into a selective decision mechanism
transfer_ivn: use SHAP-pruned LightGBM with split conformal prediction to monitor IVN traffic, accepting singleton prediction sets and deferring non-singleton or empty sets
transfer_risk: IVN traffic may be nonstationary and non-exchangeable across vehicles and attack types, breaking conformal coverage guarantees

#needs-review

## Record Fields
doi: 10.1109/SmartIoT70864.2026.00014
source_link: not stated
text_kind: fulltext
monitoring_problem: IoT intrusion detection on resource-constrained edge devices with uncertain traffic
signal: network-flow features from CICIoT2023, reduced from 46 to 15 features
uncertainty_method: split conformal prediction on pruned LightGBM
action: accept singleton prediction sets; defer non-singleton or empty sets
eval_setting: grouped 8-class CICIoT2023 at 90% target coverage
limitation_author: not stated
limitation_inference: conformal coverage assumes exchangeability, which may not hold for nonstationary IoT traffic
limitation_unknown: not stated
support_passage: split conformal prediction is added to the pruned backbone to translate predictive uncertainty into a selective decision mechanism
transfer_ivn: use SHAP-pruned LightGBM with split conformal prediction to monitor IVN traffic, accepting singleton prediction sets and deferring non-singleton or empty sets
transfer_risk: IVN traffic may be nonstationary and non-exchangeable across vehicles and attack types, breaking conformal coverage guarantees
