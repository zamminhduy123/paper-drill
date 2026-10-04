---
title: "EWCMD: real-time attack detection using ensemble weighted combination machine learning and deep learning methods"
year: 2026
doi: "https://doi.org/10.1038/s41598-026-73458-y"
relevance_score: 0.85
type: paper
---
# EWCMD: real-time attack detection using ensemble weighted combination machine learning and deep learning methods

## Novelty
Proposes a five-stage ensemble intrusion detection framework that combines seven machine learning classifiers with a CNN, using feature selection and hyperparameter optimization, and introduces two final prediction strategies: a weighted roulette-wheel mechanism for low-latency decisions and a CNN-based meta-classifier for maximum accuracy.

## Methodology
Trains and evaluates seven machine learning classifiers and a convolutional neural network on the NSL-KDD and UNSW-NB15 datasets. Applies feature selection and hyperparameter optimization to improve accuracy and reduce computational cost. Combines the trained models using a weighted roulette-wheel mechanism, ERCMD, for low-latency prediction and a CNN-based meta-classifier, EDCMD, for maximum accuracy.

## Explicit Limitations
not stated

## Future Work
not stated

## Concept Hubs
[[Concept - Deep Learning Intrusion Detection]] [[Concept - Meta-Classifier]] [[Concept - Feature Selection]] [[Concept - Real-Time Attack Defense]] [[Concept - IoT Intrusion Detection]]

## Relevance Score
0.85

## Monitoring Transfer
Monitoring problem: real-time detection of DDoS and network intrusion attacks in IoT environments. Signal: predictions from an ensemble of machine learning classifiers and a CNN. Uncertainty method: weighted roulette-wheel mechanism. Resulting action: issue a low-latency attack decision. Evaluation setting: NSL-KDD and UNSW-NB15 benchmark datasets.

Transfer to IVN: apply the ensemble weighted combination and CNN meta-classifier to in-vehicle network intrusion detection using CAN or IVN traffic features. Transfer risk: IVN traffic is protocol-specific, low-rate, and safety-critical, so DDoS-oriented features and latency-accuracy tradeoffs may not transfer.

doi: not stated
source_link: not stated
text_kind: abstract
monitoring_problem: real-time DDoS and network intrusion detection in IoT environments
signal: predictions from an ensemble of machine learning classifiers and a CNN
uncertainty_method: weighted roulette-wheel mechanism
action: issue a low-latency attack decision
eval_setting: NSL-KDD and UNSW-NB15 benchmark datasets
limitation_author: not stated
limitation_inference: high benchmark accuracy may not generalize to unseen attack types or live network conditions
limitation_unknown: not stated
support_passage: The fifth stage introduces two final prediction strategies: a weighted roulette-wheel mechanism (ERCMD) for low-latency decisions and a CNN-based meta-classifier (EDCMD) for maximum accuracy.
transfer_ivn: apply the ensemble weighted combination and CNN meta-classifier to in-vehicle network intrusion detection using CAN or IVN traffic features
transfer_risk: IVN traffic is protocol-specific, low-rate, and safety-critical, so DDoS-oriented features and latency-accuracy tradeoffs may not transfer

#needs-review

## Record Fields
doi: https://doi.org/10.1038/s41598-026-73458-y
source_link: not stated
text_kind: abstract
monitoring_problem: real-time detection of DDoS and network intrusion attacks in IoT environments. Signal: predictions from an ensemble of machine learning classifiers and a CNN. Uncertainty method: weighted roulette-wheel mechanism. Resulting action: issue a low-latency attack decision. Evaluation setting: NSL-KDD and UNSW-NB15 benchmark datasets.
signal: predictions from an ensemble of machine learning classifiers and a CNN
uncertainty_method: weighted roulette-wheel mechanism
action: issue a low-latency attack decision
eval_setting: NSL-KDD and UNSW-NB15 benchmark datasets
limitation_author: not stated
limitation_inference: high benchmark accuracy may not generalize to unseen attack types or live network conditions
limitation_unknown: not stated
support_passage: The fifth stage introduces two final prediction strategies: a weighted roulette-wheel mechanism (ERCMD) for low-latency decisions and a CNN-based meta-classifier (EDCMD) for maximum accuracy.
transfer_ivn: apply the ensemble weighted combination and CNN meta-classifier to in-vehicle network intrusion detection using CAN or IVN traffic features
transfer_risk: IVN traffic is protocol-specific, low-rate, and safety-critical, so DDoS-oriented features and latency-accuracy tradeoffs may not transfer
