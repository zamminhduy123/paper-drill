---
title: "Stacked Deep Learning Ensemble Framework for IoT Network Intrusion Detection"
year: 2026
doi: "https://doi.org/10.11648/j.net.20261302.11"
relevance_score: 8.0
type: paper
---
# Stacked Deep Learning Ensemble Framework for IoT Network Intrusion Detection

## Novelty
Stacked deep learning ensemble for binary IoT/IIoT network intrusion detection using RNN, GRU, and autoencoder base learners with an LSTM meta-learner, combined with a systematic preprocessing pipeline including SMOTE and feature selection.

## Methodology
The framework is trained and evaluated on the ToN_IoT dataset with 461,043 records and nine attack categories. Preprocessing includes label encoding, one-hot encoding, feature selection, SMOTE-based class balancing, and standard scaling. Base learners are RNN, GRU, and autoencoders, and an LSTM network acts as the meta-learner for binary intrusion detection.

## Explicit Limitations
not stated

## Future Work
not stated

## Concept Hubs
[[Concept - Deep Learning Intrusion Detection]]
[[Concept - IoT Intrusion Detection]]
[[Concept - Stacking Ensemble]]
[[Concept - Heterogeneous Base Learners]]
[[Concept - Class Imbalance]]

## Relevance Score
8.0

## Monitoring Transfer
doi: not stated
source_link: not stated
text_kind: abstract
monitoring_problem: binary network intrusion detection in IoT/IIoT traffic
signal: preprocessed ToN_IoT network traffic features
uncertainty_method: not stated
action: classify traffic as intrusion or normal
eval_setting: ToN_IoT dataset with 461,043 records and nine attack categories
limitation_author: not stated
limitation_inference: single-dataset evaluation and binary task may limit generalization
limitation_unknown: not stated
support_passage: The framework is trained and evaluated on the ToN_IoT dataset
transfer_ivn: apply the stacked RNN/GRU/autoencoder LSTM meta-learner to in-vehicle network traffic
transfer_risk: IoT/IIoT traffic features and attacks differ from IVN protocol behavior

#needs-review

## Record Fields
doi: https://doi.org/10.11648/j.net.20261302.11
source_link: not stated
text_kind: abstract
monitoring_problem: binary network intrusion detection in IoT/IIoT traffic
signal: preprocessed ToN_IoT network traffic features
uncertainty_method: not stated
action: classify traffic as intrusion or normal
eval_setting: ToN_IoT dataset with 461,043 records and nine attack categories
limitation_author: not stated
limitation_inference: single-dataset evaluation and binary task may limit generalization
limitation_unknown: not stated
support_passage: The framework is trained and evaluated on the ToN_IoT dataset
transfer_ivn: apply the stacked RNN/GRU/autoencoder LSTM meta-learner to in-vehicle network traffic
transfer_risk: IoT/IIoT traffic features and attacks differ from IVN protocol behavior
