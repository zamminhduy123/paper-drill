---
title: "MicroCAN: Ultra-Fast Windowed Statistical Learning for Real-Time CAN Intrusion Detection"
year: 2026
doi: "10.1109/ISBDAS69350.2026.11484978"
relevance_score: 7.0
type: paper
---
# MicroCAN: Ultra-Fast Windowed Statistical Learning for Real-Time CAN Intrusion Detection

## Novelty
MicroCAN is a lightweight, leakage-free sliding-window statistical CAN intrusion detection framework that uses robust CAN-ID parsing, per-trace windowing, and compact ID/timing/payload features for microsecond-level inference on constrained in-vehicle gateways.

## Methodology
The pipeline parses CAN IDs with automatic base detection, assigns frames to per-trace time or count windows, labels windows by ANY or MAJ rules, extracts top-N ID histogram counts/proportions, periodicity/jitter, payload Hamming change rates and byte entropy, then trains lightweight LR or RF classifiers with top-N IDs computed only from training data.

## Explicit Limitations
not stated

## Future Work
not stated

## Concept Hubs
[[Concept - CAN Intrusion Detection]]
[[Concept - Lightweight Detection]]
[[Concept - Data Leakage Prevention]]
[[Concept - Edge AI Inference]]

## Relevance Score
7

## Monitoring Transfer
doi: 10.1109/ISBDAS69350.2026.11484978
source_link: https://doi.org/10.1109/ISBDAS69350.2026.11484978
text_kind: conference paper
monitoring_problem: real-time CAN intrusion detection on in-vehicle gateways and ECUs
signal: per-window CAN ID distribution, timing periodicity/jitter, and payload dynamics
uncertainty_method: not stated
action: classify each CAN window as normal or attack and flag anomalous windows
eval_setting: mixed CAN datasets with per-source windowing, time-based and holdout splits, three seeds, accuracy and microsecond inference latency
limitation_author: not stated
limitation_inference: may miss attacks that preserve normal ID and timing distributions while changing only subtle payload semantics
limitation_unknown: not stated
support_passage: MicroCAN aggregates complementary signals from (i) CAN identifier (ID) distribution structure, (ii) per-ID timing periodicity and jitter, and (iii) payload dynamics
transfer_ivn: deploy MicroCAN on an in-vehicle gateway to monitor CAN bus windows in real time and alert on anomalous ID, timing, and payload statistics
transfer_risk: attacks that maintain normal ID and timing patterns while altering only payload semantics may evade the statistical features

#needs-review

## Record Fields
doi: 10.1109/ISBDAS69350.2026.11484978
source_link: https://doi.org/10.1109/ISBDAS69350.2026.11484978
text_kind: fulltext
monitoring_problem: real-time CAN intrusion detection on in-vehicle gateways and ECUs
signal: per-window CAN ID distribution, timing periodicity/jitter, and payload dynamics
uncertainty_method: not stated
action: classify each CAN window as normal or attack and flag anomalous windows
eval_setting: mixed CAN datasets with per-source windowing, time-based and holdout splits, three seeds, accuracy and microsecond inference latency
limitation_author: not stated
limitation_inference: may miss attacks that preserve normal ID and timing distributions while changing only subtle payload semantics
limitation_unknown: not stated
support_passage: MicroCAN aggregates complementary signals from (i) CAN identifier (ID) distribution structure, (ii) per-ID timing periodicity and jitter, and (iii) payload dynamics
transfer_ivn: deploy MicroCAN on an in-vehicle gateway to monitor CAN bus windows in real time and alert on anomalous ID, timing, and payload statistics
transfer_risk: attacks that maintain normal ID and timing patterns while altering only payload semantics may evade the statistical features
