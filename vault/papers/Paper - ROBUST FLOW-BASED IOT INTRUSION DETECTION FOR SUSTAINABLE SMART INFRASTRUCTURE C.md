---
title: "ROBUST FLOW-BASED IOT INTRUSION DETECTION FOR SUSTAINABLE SMART INFRASTRUCTURE: CROSS-CAPTURE EVALUATION AND INTERPRETABLE ATTACK FINGERPRINTS"
year: 2026
doi: "https://doi.org/10.24874/pes08.02a.015"
relevance_score: 0.72
type: paper
---
# ROBUST FLOW-BASED IOT INTRUSION DETECTION FOR SUSTAINABLE SMART INFRASTRUCTURE: CROSS-CAPTURE EVALUATION AND INTERPRETABLE ATTACK FINGERPRINTS

## Novelty
Cross-capture evaluation of flow-based IoT intrusion detection, showing a large generalization gap between random-split and capture-group evaluation, with interpretable attack fingerprints based on timing patterns and packet/flow sizes.

## Methodology
Flow-based tabular data from the CIC IoT-IDAD dataset is classified into normal, DoS-UDP, DDoS-ICMP, and Mirai using Logistic Regression and Random Forest. Performance is evaluated under standard random splitting and cross-capture train/test settings using Macro-F1, with feature importance used to identify stable indicators.

## Explicit Limitations
Performance drops sharply when trained on one capture group and tested on another, with average Macro-F1 of 0.34-0.39, indicating a significant generalization gap in real deployment scenarios.

## Future Work
not stated

## Concept Hubs
[[Concept - IoT Intrusion Detection]]
[[Concept - Cross-Dataset Evaluation]]
[[Concept - Explainable Intrusion Detection]]
[[Concept - Network Traffic Analysis]]

## Relevance Score
0.72

## Monitoring Transfer
monitoring_problem: detect IoT network intrusions under changing network conditions
signal: flow-based tabular features, especially timing patterns and packet/flow sizes
uncertainty_method: not stated
action: classify traffic as normal, DoS-UDP, DDoS-ICMP, or Mirai
eval_setting: standard random split and cross-capture train/test on CIC IoT-IDAD
limitation_author: performance drops sharply when trained on one capture group and tested on another, with average Macro-F1 of 0.34-0.39
limitation_inference: the models may depend on capture-specific flow patterns and lack robustness to network-condition shifts
limitation_unknown: not stated
support_passage: its performance drops sharply when trained on one capture group and tested on another (average Macro-F1: 0.34-0.39).This study highlights a significant generalization gap in real deployment scenarios.
transfer_ivn: apply flow-based timing and packet-size fingerprints plus cross-capture evaluation to monitor in-vehicle network traffic for intrusion
transfer_risk: IVN traffic is protocol-specific, real-time, and vehicle-state dependent, so IoT flow features may not generalize

#needs-review

## Record Fields
doi: https://doi.org/10.24874/pes08.02a.015
source_link: not stated
text_kind: abstract
monitoring_problem: detect IoT network intrusions under changing network conditions
signal: flow-based tabular features, especially timing patterns and packet/flow sizes
uncertainty_method: not stated
action: classify traffic as normal, DoS-UDP, DDoS-ICMP, or Mirai
eval_setting: standard random split and cross-capture train/test on CIC IoT-IDAD
limitation_author: performance drops sharply when trained on one capture group and tested on another, with average Macro-F1 of 0.34-0.39
limitation_inference: the models may depend on capture-specific flow patterns and lack robustness to network-condition shifts
limitation_unknown: not stated
support_passage: its performance drops sharply when trained on one capture group and tested on another (average Macro-F1: 0.34-0.39).This study highlights a significant generalization gap in real deployment scenarios.
transfer_ivn: apply flow-based timing and packet-size fingerprints plus cross-capture evaluation to monitor in-vehicle network traffic for intrusion
transfer_risk: IVN traffic is protocol-specific, real-time, and vehicle-state dependent, so IoT flow features may not generalize
