---
title: "Real-Time Network Intrusion Detection Dataset: Campus Traffic and Behavioral Features"
year: 2026
doi: "https://doi.org/10.17632/w7ww2czdtb"
relevance_score: 0.93
type: paper
---
# Real-Time Network Intrusion Detection Dataset: Campus Traffic and Behavioral Features

## Novelty
- Real-time NIDS dataset combining synthetic lab traffic, personal browsing traffic, and university campus traffic.
- Provides raw Wireshark CSV captures and a processed 3,270,480-record engineered dataset.
- Uses rolling-window behavioral features instead of static IP/port memorization.
- Replaces IP addresses with sentinel values to encourage behavior-based learning.
- Reports strong baseline performance using Random Forest and Deep Neural Network classifiers.

## Methodology
- Captured five raw Wireshark packet-capture CSV files with a common 10-column schema.
- Generated synthetic benign and attack traffic in a controlled lab environment.
- Captured real human browsing traffic and real institutional campus traffic from COMSIT, University of Ilorin, Nigeria.
- Extracted 12 behavioral features using 50-packet, 100-packet, and 1-second rolling windows.
- Features include flow duration, inter-arrival time, packet-size variance, port diversity, and SYN/ACK ratio.
- Trained baseline Random Forest and Deep Neural Network classifiers.
- Evaluated on a held-out test split and a separate 5.2-million-record real campus attack capture.

## Explicit Limitations
- Not explicitly stated in the abstract.
- Inferred limitations include reliance on engineered behavioral features, sentinel IP replacement, and evaluation on a single campus/lab traffic mix.
- No uncertainty quantification method is described.

## Future Work
- Use the raw files to build and test alternative feature-engineering pipelines.
- Use the processed file for model training and benchmarking.
- Improve generalization beyond static, single-origin benchmark datasets.
- Extend evaluation to additional enterprise, internet, and real-time network environments.

## Concept Hubs
[[Concept - Deep Learning Intrusion Detection]]
[[Concept - Network Traffic Dynamics]]
[[Concept - Real-Time Attack Defense]]
[[Concept - Dataset Bias]]
[[Concept - Cross-Dataset Evaluation]]

## Relevance Score
0.93

## Monitoring Transfer
Monitoring problem: real-time detection of network intrusions in enterprise and campus traffic.
Signal: rolling-window behavioral packet features.
Uncertainty method: not stated.
Resulting action: classify traffic as benign or attack.
Evaluation setting: held-out test split and separate real campus attack capture.
Transfer to IVN: apply rolling-window behavioral features and DNN/RF classifiers to in-vehicle network intrusion detection.
Transfer risk: campus TCP/IP behavioral patterns may not generalize to protocol-specific, low-rate in-vehicle traffic.

doi: not stated
source_link: not stated
text_kind: dataset
monitoring_problem: real-time network intrusion detection in enterprise and campus networks
signal: rolling-window behavioral packet features
uncertainty_method: not stated
action: classify traffic as benign or attack
eval_setting: held-out test split and separate real campus attack capture
limitation_author: not stated
limitation_inference: engineered features and sentinel IPs may reduce endpoint context; baselines lack uncertainty quantification; single campus/lab sources may limit generalization
limitation_unknown: not stated
support_passage: Baseline Random Forest and Deep Neural Network classifiers trained on this data achieved a 1.0000 F1-score and 0.0000 false-positive rate on a held-out test split
transfer_ivn: apply rolling-window behavioral features and DNN/RF classifiers to in-vehicle network intrusion detection
transfer_risk: campus TCP/IP behavioral patterns may not generalize to protocol-specific in-vehicle traffic

#needs-review

## Record Fields
doi: https://doi.org/10.17632/w7ww2czdtb
source_link: not stated
text_kind: abstract
monitoring_problem: real-time detection of network intrusions in enterprise and campus traffic.
signal: rolling-window behavioral packet features.
uncertainty_method: not stated.
action: classify traffic as benign or attack
eval_setting: held-out test split and separate real campus attack capture
limitation_author: not stated
limitation_inference: engineered features and sentinel IPs may reduce endpoint context; baselines lack uncertainty quantification; single campus/lab sources may limit generalization
limitation_unknown: not stated
support_passage: Baseline Random Forest and Deep Neural Network classifiers trained on this data achieved a 1.0000 F1-score and 0.0000 false-positive rate on a held-out test split
transfer_ivn: apply rolling-window behavioral features and DNN/RF classifiers to in-vehicle network intrusion detection
transfer_risk: campus TCP/IP behavioral patterns may not generalize to protocol-specific, low-rate in-vehicle traffic.
