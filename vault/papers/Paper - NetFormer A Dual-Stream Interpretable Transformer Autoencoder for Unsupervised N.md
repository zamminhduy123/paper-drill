---
title: "NetFormer: A Dual-Stream Interpretable Transformer Autoencoder for Unsupervised Network Intrusion Detection"
year: 2026
doi: "https://doi.org/10.12688/f1000research.182153.2"
relevance_score: 95.0
type: paper
---
# NetFormer: A Dual-Stream Interpretable Transformer Autoencoder for Unsupervised Network Intrusion Detection

## Novelty
NetFormer introduces a Transformer-based unsupervised autoencoder for network traffic time-series with dual-stream categorical/numerical embeddings, normal-traffic reconstruction scoring, and attention-map interpretability.

## Methodology
The model embeds categorical and numerical traffic features separately, trains a reconstruction autoencoder on normal traffic, computes anomaly scores from reconstruction error, and uses attention maps to explain detections. It is evaluated on CSE-CIC-IDS2018 and UNSW-NB15.

## Explicit Limitations
Cross-dataset transfer is not seamless, indicating imperfect generalization between network traffic datasets.

## Future Work
not stated

## Concept Hubs
[[Concept - Unsupervised Intrusion Detection]]
[[Concept - Deep Learning Intrusion Detection]]
[[Concept - Explainable Intrusion Detection]]
[[Concept - Network Traffic Analysis]]
[[Concept - Cross-Dataset Evaluation]]

## Relevance Score
95

## Monitoring Transfer
doi: not stated
source_link: not stated
text_kind: abstract
monitoring_problem: detect malicious network traffic anomalies in enterprise/internet networks with low false positives
signal: reconstruction anomaly score from dual-stream Transformer autoencoder and attention-map feature highlights
uncertainty_method: not stated
action: flag anomalous traffic as potential intrusion
eval_setting: CSE-CIC-IDS2018 and UNSW-NB15 benchmarks with F1, precision, recall, and false positive rate
limitation_author: cross-dataset transition is not seamless
limitation_inference: performance may degrade across datasets due to traffic distribution shift
limitation_unknown: not stated
support_passage: the transition from one dataset to another is not seamless
transfer_ivn: apply NetFormer to in-vehicle network traffic by encoding vehicle bus messages as categorical and numerical time-series and alerting on reconstruction anomalies
transfer_risk: vehicle network traffic has strict real-time constraints and protocol-specific distributions that may reduce detection accuracy and increase false positives

#needs-review

## Record Fields
doi: https://doi.org/10.12688/f1000research.182153.2
source_link: not stated
text_kind: abstract
monitoring_problem: detect malicious network traffic anomalies in enterprise/internet networks with low false positives
signal: reconstruction anomaly score from dual-stream Transformer autoencoder and attention-map feature highlights
uncertainty_method: not stated
action: flag anomalous traffic as potential intrusion
eval_setting: CSE-CIC-IDS2018 and UNSW-NB15 benchmarks with F1, precision, recall, and false positive rate
limitation_author: cross-dataset transition is not seamless
limitation_inference: performance may degrade across datasets due to traffic distribution shift
limitation_unknown: not stated
support_passage: the transition from one dataset to another is not seamless
transfer_ivn: apply NetFormer to in-vehicle network traffic by encoding vehicle bus messages as categorical and numerical time-series and alerting on reconstruction anomalies
transfer_risk: vehicle network traffic has strict real-time constraints and protocol-specific distributions that may reduce detection accuracy and increase false positives
