---
title: "Lightweight CNN-Based Intrusion Detection for CAN Bus Networks"
year: 2026
doi: "10.1109/ACCESS.2026.3654521"
relevance_score: 0.95
type: paper
---
# Lightweight CNN-Based Intrusion Detection for CAN Bus Networks

## Novelty
Proposes TinyCNNCANNet, an ultra-lightweight CNN with about 13K parameters for CAN bus intrusion detection, plus two efficient baseline CNNs. Introduces SynCAN 2025, a synthetic CAN intrusion dataset for generalization testing, and shows competitive or superior accuracy versus models with 115-300x more parameters, with much lower inference latency and model size.

## Methodology
Designs lightweight CNN architectures tailored to CAN traffic characteristics, including small input sizes and strict resource constraints. Evaluates detection accuracy, inference latency, and model size on four datasets: CANFD 2021, CICIoV 2024, Multi-Fuzzer-CAN 2025, and SynCAN 2025, covering nine attack types. The study is experimental and focuses on feasibility for future real-time capable CAN intrusion detection rather than on-vehicle deployment.

## Explicit Limitations
No explicit limitations section is provided in the supplied text. The authors state that the work does not focus on on-vehicle deployment and evaluates feasibility under experimental settings.

## Future Work
Develop real-time capable CAN intrusion detection and deploy lightweight CNN models on embedded automotive platforms.

## Concept Hubs
[[Concept - CAN Intrusion Detection]]
[[Concept - Lightweight Detection]]
[[Concept - Deep Learning Intrusion Detection]]
[[Concept - Resource-Constrained Edge]]
[[Concept - Cross-Dataset Evaluation]]

## Relevance Score
0.95

## Monitoring Transfer
doi: 10.1109/ACCESS.2026.3654521
source_link: not stated
text_kind: journal article
monitoring_problem: detect intrusions in CAN bus traffic
signal: CAN message sequences/frames
uncertainty_method: not stated
action: classify CAN traffic as normal or attack and identify attack type
eval_setting: four datasets (CANFD 2021, CICIoV 2024, Multi-Fuzzer-CAN 2025, SynCAN 2025) with nine attack types; experimental evaluation, not on-vehicle
limitation_author: not on-vehicle deployment; experimental feasibility only
limitation_inference: no embedded ECU validation; real-time and resource constraints may differ in a vehicle
limitation_unknown: not stated
support_passage: Rather than focusing on on-vehicle deployment, this work evaluates the feasibility of lightweight CNN architectures for future real-time capable CAN intrusion detection.
transfer_ivn: Use TinyCNNCANNet to monitor CAN/CAN FD traffic in an in-vehicle network and classify normal versus attack traffic.
transfer_risk: May fail if ECU hardware, real-time scheduling, or unseen attack distributions exceed the experimental assumptions.

#needs-review

## Record Fields
doi: 10.1109/ACCESS.2026.3654521
source_link: not stated
text_kind: fulltext
monitoring_problem: detect intrusions in CAN bus traffic
signal: CAN message sequences/frames
uncertainty_method: not stated
action: classify CAN traffic as normal or attack and identify attack type
eval_setting: four datasets (CANFD 2021, CICIoV 2024, Multi-Fuzzer-CAN 2025, SynCAN 2025) with nine attack types; experimental evaluation, not on-vehicle
limitation_author: not on-vehicle deployment; experimental feasibility only
limitation_inference: no embedded ECU validation; real-time and resource constraints may differ in a vehicle
limitation_unknown: not stated
support_passage: Rather than focusing on on-vehicle deployment, this work evaluates the feasibility of lightweight CNN architectures for future real-time capable CAN intrusion detection.
transfer_ivn: Use TinyCNNCANNet to monitor CAN/CAN FD traffic in an in-vehicle network and classify normal versus attack traffic.
transfer_risk: May fail if ECU hardware, real-time scheduling, or unseen attack distributions exceed the experimental assumptions.
