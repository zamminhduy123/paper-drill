---
title: "A Blockchain-Integrated Federated Learning Model and Autoencoder-Based Feature Reduction for Improving IoT Intrusion Detection"
year: 2026
doi: "https://doi.org/10.65445/3106-1192.1013"
relevance_score: 9.0
type: paper
---
# A Blockchain-Integrated Federated Learning Model and Autoencoder-Based Feature Reduction for Improving IoT Intrusion Detection

## Novelty
Proposes a blockchain-verified federated learning intrusion detection framework for IoT that combines autoencoder feature reduction with local LSTM training to improve privacy, scalability, and model integrity.

## Methodology
Preprocesses ToN-IoT, applies an unsupervised autoencoder for low-dimensional feature extraction, trains local LSTM models on client data, records SHA-256 hashed local model weights on a blockchain, and updates the global model using federated averaging with blockchain-based verification.

## Explicit Limitations
not stated

## Future Work
not stated

## Concept Hubs
[[Concept - IoT Intrusion Detection]] [[Concept - Deep Learning Intrusion Detection]] [[Concept - Privacy-Preserving Learning]] [[Concept - Feature Selection]]

## Relevance Score
9/10

## Monitoring Transfer
doi: not stated
source_link: not stated
text_kind: abstract
monitoring_problem: detect network intrusions in IoT environments while preserving privacy and avoiding centralized failure
signal: autoencoder-reduced network traffic features processed by local LSTM models
uncertainty_method: not stated
action: update the global intrusion detection model through federated averaging after blockchain verification
eval_setting: ToN-IoT dataset evaluated with accuracy, precision, recall, and F1-score
limitation_author: not stated
limitation_inference: reported metrics rely on a single dataset and do not establish real-time, cross-domain, or resource-constrained robustness
limitation_unknown: not stated
support_passage: Our findings show the performance of the proposed framework leading to an accuracy of 99.96% precision of 99.99% recall of 99.95% and F1-score of 99.97%
transfer_ivn: apply the federated autoencoder-LSTM model to in-vehicle networks by training local ECU clients and aggregating a global intrusion detection model with blockchain verification
transfer_risk: blockchain aggregation latency and autoencoder feature assumptions may violate real-time in-vehicle network constraints

#needs-review

## Record Fields
doi: https://doi.org/10.65445/3106-1192.1013
source_link: not stated
text_kind: abstract
monitoring_problem: detect network intrusions in IoT environments while preserving privacy and avoiding centralized failure
signal: autoencoder-reduced network traffic features processed by local LSTM models
uncertainty_method: not stated
action: update the global intrusion detection model through federated averaging after blockchain verification
eval_setting: ToN-IoT dataset evaluated with accuracy, precision, recall, and F1-score
limitation_author: not stated
limitation_inference: reported metrics rely on a single dataset and do not establish real-time, cross-domain, or resource-constrained robustness
limitation_unknown: not stated
support_passage: Our findings show the performance of the proposed framework leading to an accuracy of 99.96% precision of 99.99% recall of 99.95% and F1-score of 99.97%
transfer_ivn: apply the federated autoencoder-LSTM model to in-vehicle networks by training local ECU clients and aggregating a global intrusion detection model with blockchain verification
transfer_risk: blockchain aggregation latency and autoencoder feature assumptions may violate real-time in-vehicle network constraints
