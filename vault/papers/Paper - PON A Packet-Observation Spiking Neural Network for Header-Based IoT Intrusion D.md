---
title: "PON: A Packet-Observation Spiking Neural Network for Header-Based IoT Intrusion Detection"
year: 2026
doi: "https://doi.org/10.4108/eetinis.133.13277"
relevance_score: 9.0
type: paper
---
# PON: A Packet-Observation Spiking Neural Network for Header-Based IoT Intrusion Detection

## Novelty
Proposes PON, a packet-observation spiking neural network for real-time, lightweight IoT intrusion detection using only packet headers. Introduces a behavior-adaptive redundancy filter, a Sparse Attack Detector for rare attacks, and ternary quantization for edge-friendly storage.

## Methodology
Uses 64-byte normalized packet headers and a sliding-window source IP diversity ratio as features. The model combines 1D convolution with leaky-integrate-and-fire neurons and a Sparse Attack Detector. It performs online packet-level header-only inference and applies trained ternary quantization to reduce model size.

## Explicit Limitations
Not stated in the provided abstract.

## Future Work
Not stated in the provided abstract.

## Concept Hubs
[[Concept - IoT Intrusion Detection]]
[[Concept - Edge AI Inference]]
[[Concept - Lightweight Detection]]
[[Concept - Network Traffic Analysis]]
[[Concept - Deep Learning Intrusion Detection]]

## Relevance Score
9/10

## Monitoring Transfer
- Monitoring problem: Real-time, lightweight intrusion detection in IoT network traffic at the edge.
- Signal: Normalized 64-byte packet headers and sliding-window source IP diversity ratio.
- Uncertainty method: not stated
- Resulting action: Online header-only packet classification and reduced edge processing traffic.
- Evaluation setting: CIC-IoT2023 mixed traffic streams; Macro F1 92.48%, detection rate 90.23%, rare-attack detection improved by up to 21.5 percentage points; ternary model size 13.82 KB versus 30.69 KB float32.
- IVN transfer: Adapt the header-only spiking network and redundancy filter to in-vehicle network intrusion detection on vehicle edge nodes.
- Transfer risk: Vehicle network protocols, timing behavior, and encrypted or payload-dependent attacks may not be captured by IoT header features trained on CIC-IoT2023.

doi: not stated
source_link: not stated
text_kind: abstract
monitoring_problem: Real-time lightweight IoT network intrusion detection at the edge
signal: 64-byte normalized packet headers and sliding-window source IP diversity ratio
uncertainty_method: not stated
action: Header-only online packet classification and redundant edge traffic reduction
eval_setting: CIC-IoT2023 mixed traffic streams with Macro F1, detection rate, rare-attack improvement, and model-size evaluation
limitation_author: not stated
limitation_inference: Header-only inference may miss attacks that require payload inspection
limitation_unknown: not stated
support_passage: PON performs header-only inference using these features, while payload data are not forwarded to the classifier.
transfer_ivn: Apply header-only spiking intrusion detection with redundancy filtering to in-vehicle network edge monitoring
transfer_risk: IoT header features and CIC-IoT2023 training may not generalize to vehicle bus protocols and payload-dependent attacks

#needs-review

## Record Fields
doi: https://doi.org/10.4108/eetinis.133.13277
source_link: not stated
text_kind: abstract
monitoring_problem: Real-time lightweight IoT network intrusion detection at the edge
signal: 64-byte normalized packet headers and sliding-window source IP diversity ratio
uncertainty_method: not stated
action: Header-only online packet classification and redundant edge traffic reduction
eval_setting: CIC-IoT2023 mixed traffic streams with Macro F1, detection rate, rare-attack improvement, and model-size evaluation
limitation_author: not stated
limitation_inference: Header-only inference may miss attacks that require payload inspection
limitation_unknown: not stated
support_passage: PON performs header-only inference using these features, while payload data are not forwarded to the classifier.
transfer_ivn: Apply header-only spiking intrusion detection with redundancy filtering to in-vehicle network edge monitoring
transfer_risk: IoT header features and CIC-IoT2023 training may not generalize to vehicle bus protocols and payload-dependent attacks
