---
title: "Federated Learning-Based Counterfactual Explanations for Resolving the Privacy-Explainability Dilemma in IoT Intrusion Detection"
year: 2026
doi: "https://doi.org/10.1109/siu71813.2026.11636543"
relevance_score: 9.0
type: paper
---
# Federated Learning-Based Counterfactual Explanations for Resolving the Privacy-Explainability Dilemma in IoT Intrusion Detection

## Novelty
- Proposes FedCF-IoT, a federated learning framework that combines differential privacy with counterfactual explanations for IoT intrusion detection.
- Shows that differential privacy noise can improve counterfactual validity from 93.2% to 98.8% rather than degrading it.
- Evaluates privacy-preserving explainable intrusion detection on the 15-class Edge-IIoTset dataset with accuracy, macro F1-score, and counterfactual quality metrics.

## Methodology
- Uses an MLP classifier with 256-128-64 layers, batch normalization, and dropout.
- Trains the model centrally and federatedly using FedAvg, FedProx, and FedNova with K=10 clients, T=30 communication rounds, and E=5 local epochs.
- Generates counterfactual explanations by minimizing a loss combining prediction loss, L1 proximity, diversity, and IoT feasibility constraints.
- Applies Rényi differential privacy via DP-SGD with gradient clipping, δ=10^-5, and ε values of 0.5, 1.0, 2.0, 5.0, and 10.0.
- Evaluates on Edge-IIoTset with 500,000 stratified samples, 56 features, StandardScaler normalization, and an 80/20 train/test split.

## Explicit Limitations
- Federated learning alone is insufficient because gradient and membership inference attacks can leak sensitive information from model updates.
- High class imbalance makes ROC-AUC an optimistic indicator, so macro F1-score is used as the primary evaluation metric.

## Future Work
not stated

## Concept Hubs
[[Concept - IoT Intrusion Detection]]
[[Concept - Explainable Intrusion Detection]]
[[Concept - Privacy-Preserving Learning]]
[[Concept - Class Imbalance]]

## Relevance Score
9/10

## Monitoring Transfer
monitoring_problem: Privacy-preserving and explainable intrusion detection in IoT networks
signal: 56 numerical network traffic features from Edge-IIoTset and model class predictions
uncertainty_method: Rényi differential privacy with DP-SGD gradient noise
action: Federated training of an MLP intrusion detector and generation of feasible counterfactual explanations for attack alerts
eval_setting: Edge-IIoTset 15-class attack classification, 500,000 stratified samples, 80/20 split, centralized and federated settings with K=10, T=30, E=5
limitation_author: Federated learning alone is insufficient because gradient and membership inference attacks can leak sensitive information from model updates; ROC-AUC is optimistic under high class imbalance
limitation_inference: Evaluation is limited to Edge-IIoTset, an MLP classifier, fixed FL/DP hyperparameters, and counterfactual validity based on final class decisions
limitation_unknown: not stated
support_passage: The proposed framework combines counterfactual explanations with differential privacy mechanisms to produce explainable predictions without sharing raw data
transfer_ivn: Apply federated differential-privacy counterfactual intrusion detection to in-vehicle network traffic to detect intrusions while preserving vehicle data privacy and explaining alerts
transfer_risk: IVN traffic is low-dimensional, highly real-time constrained, and has different attack semantics, so DP noise and counterfactual search may be too slow or reduce detection performance

#needs-review

## Record Fields
doi: https://doi.org/10.1109/siu71813.2026.11636543
source_link: not stated
text_kind: fulltext
monitoring_problem: Privacy-preserving and explainable intrusion detection in IoT networks
signal: 56 numerical network traffic features from Edge-IIoTset and model class predictions
uncertainty_method: Rényi differential privacy with DP-SGD gradient noise
action: Federated training of an MLP intrusion detector and generation of feasible counterfactual explanations for attack alerts
eval_setting: Edge-IIoTset 15-class attack classification, 500,000 stratified samples, 80/20 split, centralized and federated settings with K=10, T=30, E=5
limitation_author: Federated learning alone is insufficient because gradient and membership inference attacks can leak sensitive information from model updates; ROC-AUC is optimistic under high class imbalance
limitation_inference: Evaluation is limited to Edge-IIoTset, an MLP classifier, fixed FL/DP hyperparameters, and counterfactual validity based on final class decisions
limitation_unknown: not stated
support_passage: The proposed framework combines counterfactual explanations with differential privacy mechanisms to produce explainable predictions without sharing raw data
transfer_ivn: Apply federated differential-privacy counterfactual intrusion detection to in-vehicle network traffic to detect intrusions while preserving vehicle data privacy and explaining alerts
transfer_risk: IVN traffic is low-dimensional, highly real-time constrained, and has different attack semantics, so DP noise and counterfactual search may be too slow or reduce detection performance
