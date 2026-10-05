---
title: "An Adaptive Feature-Aware Feed-Forward Neural Network for Intelligent Network Intrusion Detection"
year: 2026
doi: "10.1109/IMSA70415.2026.11700298"
relevance_score: 88.0
type: paper
---
# An Adaptive Feature-Aware Feed-Forward Neural Network for Intelligent Network Intrusion Detection

## Novelty
Proposes an Adaptive Feature-Aware Feed-Forward Neural Network (AF-FFNN) for network intrusion detection that adds a learnable input feature-weighting mechanism to a feed-forward architecture, enabling soft feature selection, improved discrimination between benign and malicious traffic, and a lightweight accuracy-efficiency trade-off.

## Methodology
The AF-FFNN applies element-wise learned weights to input network traffic features, then passes the weighted features through fully connected hidden layers and an output classifier. The system is evaluated on CICIDS2017 using data preprocessing, feature selection, and hyperparameter optimization, and is benchmarked against Decision Tree, Random Forest, SVM, KNN, and conventional MLP. Reported metrics include accuracy, precision, recall, F1-score, false positive rate, and inference latency.

## Explicit Limitations
not stated

## Future Work
not stated

## Concept Hubs
[[Concept - Deep Learning Intrusion Detection]]
[[Concept - Feature Selection]]
[[Concept - Lightweight Detection]]
[[Concept - Network Traffic Analysis]]

## Relevance Score
88

## Monitoring Transfer
doi: 10.1109/IMSA70415.2026.11700298
source_link: https://doi.org/10.1109/IMSA70415.2026.11700298
text_kind: conference paper
monitoring_problem: detect intrusions and anomalies in network traffic
signal: weighted network traffic features
uncertainty_method: not stated
action: classify traffic as benign or malicious
eval_setting: CICIDS2017 dataset with five baseline classifiers
limitation_author: not stated
limitation_inference: single-dataset evaluation and no explicit temporal modeling of traffic sequences
limitation_unknown: not stated
support_passage: Evaluated on the CICIDS2017 dataset through a rigorous experimental pipeline encompassing data preprocessing, feature selection, and systematic hyperparameter optimization
transfer_ivn: apply the adaptive feature-weighted FFNN to in-vehicle network traffic features for real-time intrusion detection
transfer_risk: CICIDS2017 enterprise and internet traffic may not capture in-vehicle protocol semantics, attack distributions, and strict latency constraints

#needs-review

## Record Fields
doi: 10.1109/IMSA70415.2026.11700298
source_link: https://doi.org/10.1109/IMSA70415.2026.11700298
text_kind: fulltext
monitoring_problem: detect intrusions and anomalies in network traffic
signal: weighted network traffic features
uncertainty_method: not stated
action: classify traffic as benign or malicious
eval_setting: CICIDS2017 dataset with five baseline classifiers
limitation_author: not stated
limitation_inference: single-dataset evaluation and no explicit temporal modeling of traffic sequences
limitation_unknown: not stated
support_passage: Evaluated on the CICIDS2017 dataset through a rigorous experimental pipeline encompassing data preprocessing, feature selection, and systematic hyperparameter optimization
transfer_ivn: apply the adaptive feature-weighted FFNN to in-vehicle network traffic features for real-time intrusion detection
transfer_risk: CICIDS2017 enterprise and internet traffic may not capture in-vehicle protocol semantics, attack distributions, and strict latency constraints
