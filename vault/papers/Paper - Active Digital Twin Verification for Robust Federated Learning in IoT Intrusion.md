---
title: "Active Digital Twin Verification for Robust Federated Learning in IoT Intrusion Detection"
year: 2026
doi: "10.1109/ICCE70609.2026.11658485"
relevance_score: 0.95
type: paper
---
# Active Digital Twin Verification for Robust Federated Learning in IoT Intrusion Detection

## Novelty
Introduces DT-Guard, a server-side digital twin that actively verifies federated client updates on synthetic challenge data and uses DT-driven performance weighting to identify free riders.

## Methodology
Clients upload local IoT IDS updates; the server deploys each update in a sandboxed digital twin; a four-layer pipeline scores detection capability, backdoor resistance, parameter deviation, and cross-round stability; DT-PW compares client predictions with the global model and applies an effort gate; accepted updates are aggregated with contribution-based weights.

## Explicit Limitations
not stated

## Future Work
not stated

## Concept Hubs
[[Concept - IoT Intrusion Detection]]
[[Concept - Privacy-Preserving Learning]]
[[Concept - Deep Learning Intrusion Detection]]
[[Concept - Benchmark Stress Testing]]
[[Concept - Edge Security]]

## Relevance Score
0.95

## Monitoring Transfer
doi: 10.1109/ICCE70609.2026.11658485
source_link: not stated
text_kind: conference paper
monitoring_problem: detecting malicious and free-rider client updates in federated IoT intrusion detection
signal: client model predictions on synthetic challenge data, parameter deviation, cross-round stability, and prediction divergence from the global model
uncertainty_method: threshold-based trust score and effort gate from four-layer verification
action: reject failed updates and aggregate accepted updates using DT-driven performance weighting
eval_setting: CIC-IoT-2023 under five poisoning strategies compared with nine baselines
limitation_author: not stated
limitation_inference: reliance on synthetic challenge data and server-side digital twin overhead may limit coverage and scalability
limitation_unknown: not stated
support_passage: We validate DT-Guard on CIC-IoT-2023 under five poisoning strategies. DT-Guard generally outperforms nine existing defenses in accuracy, false positive rate, and contribution fairness.
transfer_ivn: deploy a vehicle digital twin to actively test ECU model updates on synthetic CAN/DoIP challenge traffic before federated aggregation
transfer_risk: vehicle-specific protocol dynamics and real-time constraints may make synthetic challenge data and digital twin testing miss IVN attacks

#needs-review

## Record Fields
doi: 10.1109/ICCE70609.2026.11658485
source_link: not stated
text_kind: fulltext
monitoring_problem: detecting malicious and free-rider client updates in federated IoT intrusion detection
signal: client model predictions on synthetic challenge data, parameter deviation, cross-round stability, and prediction divergence from the global model
uncertainty_method: threshold-based trust score and effort gate from four-layer verification
action: reject failed updates and aggregate accepted updates using DT-driven performance weighting
eval_setting: CIC-IoT-2023 under five poisoning strategies compared with nine baselines
limitation_author: not stated
limitation_inference: reliance on synthetic challenge data and server-side digital twin overhead may limit coverage and scalability
limitation_unknown: not stated
support_passage: We validate DT-Guard on CIC-IoT-2023 under five poisoning strategies. DT-Guard generally outperforms nine existing defenses in accuracy, false positive rate, and contribution fairness.
transfer_ivn: deploy a vehicle digital twin to actively test ECU model updates on synthetic CAN/DoIP challenge traffic before federated aggregation
transfer_risk: vehicle-specific protocol dynamics and real-time constraints may make synthetic challenge data and digital twin testing miss IVN attacks
