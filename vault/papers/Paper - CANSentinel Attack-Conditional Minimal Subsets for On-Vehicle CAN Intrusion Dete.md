---
title: "CANSentinel: Attack-Conditional Minimal Subsets for On-Vehicle CAN Intrusion Detection -- research artifact"
year: 2026
doi: "https://doi.org/10.5281/zenodo.23114549"
relevance_score: 0.95
type: paper
---
# CANSentinel: Attack-Conditional Minimal Subsets for On-Vehicle CAN Intrusion Detection -- research artifact

## Novelty
Attack-conditional minimal feature subsets for on-vehicle CAN intrusion detection, packaged as a frozen, provenance-rich research artifact with embedded STM32 firmware latency measurements.

## Methodology
Reproduces frozen results on HCRL Car-Hacking and ROAD using 18 analysis scripts, 31 provenance-pinned JSONs, figure-generation scripts, and subset-gated STM32F407/STM32G474RE firmware; captures are capped at 120,000 frames with seed 42, with 60k/120k/full frame-budget sensitivity and bit-exact robustness checks.

## Explicit Limitations
Datasets are not included except a 500-frame demonstration excerpt; the frozen protocol uses a 120,000-frame cap and seed 42; evaluation is limited to two public CAN intrusion-detection benchmarks.

## Future Work
not stated

## Concept Hubs
[[Concept - CAN Intrusion Detection]]
[[Concept - Coreset Selection]]
[[Concept - Lightweight Detection]]
[[Concept - Embedded Systems]]
[[Concept - In-Vehicle Network Security]]

## Relevance Score
0.95

## Monitoring Transfer
doi: not stated
source_link: not stated
text_kind: research artifact
monitoring_problem: on-vehicle CAN intrusion detection under a bounded feature-vector and frame budget
signal: CAN frame features from HCRL and ROAD captures
uncertainty_method: not stated
action: subset-gated intrusion detection with board-level latency measurement
eval_setting: HCRL Car-Hacking and ROAD public benchmarks; frozen 120,000-frame captures, seed 42, 60k/120k/full sensitivity
limitation_author: datasets are not included apart from a 500-frame demonstration excerpt; frozen protocol caps each capture at 120,000 frames with seed 42
limitation_inference: results may not generalize beyond the two public benchmarks, fixed seed, and capped frame budget
limitation_unknown: not stated
support_passage: The artifact reproduces the paper's frozen results on two public CAN intrusion-detection benchmarks (HCRL Car-Hacking and ROAD); the frozen protocol caps each capture at 120,000 frames with seed 42; datasets are public benchmarks and are not included apart from a 500-frame demonstration excerpt.
transfer_ivn: Use attack-conditional minimal feature subsets to reduce feature-vector cost and enable subset-gated CAN intrusion detection on embedded ECU gateways.
transfer_risk: Minimal subsets trained on public benchmarks and fixed frame budgets may miss rare, evolving, or vehicle-specific attacks in live IVN traffic.

#needs-review

## Record Fields
doi: https://doi.org/10.5281/zenodo.23114549
source_link: not stated
text_kind: abstract
monitoring_problem: on-vehicle CAN intrusion detection under a bounded feature-vector and frame budget
signal: CAN frame features from HCRL and ROAD captures
uncertainty_method: not stated
action: subset-gated intrusion detection with board-level latency measurement
eval_setting: HCRL Car-Hacking and ROAD public benchmarks; frozen 120,000-frame captures, seed 42, 60k/120k/full sensitivity
limitation_author: datasets are not included apart from a 500-frame demonstration excerpt; frozen protocol caps each capture at 120,000 frames with seed 42
limitation_inference: results may not generalize beyond the two public benchmarks, fixed seed, and capped frame budget
limitation_unknown: not stated
support_passage: The artifact reproduces the paper's frozen results on two public CAN intrusion-detection benchmarks (HCRL Car-Hacking and ROAD); the frozen protocol caps each capture at 120,000 frames with seed 42; datasets are public benchmarks and are not included apart from a 500-frame demonstration excerpt.
transfer_ivn: Use attack-conditional minimal feature subsets to reduce feature-vector cost and enable subset-gated CAN intrusion detection on embedded ECU gateways.
transfer_risk: Minimal subsets trained on public benchmarks and fixed frame budgets may miss rare, evolving, or vehicle-specific attacks in live IVN traffic.
