---
title: "CAN-TEMPO: Unsupervised CAN Bus Intrusion Detection via Temporal Multi-Period Oscillation Encoding"
year: 2026
doi: "https://doi.org/10.3390/technologies14060375"
relevance_score: 9.0
type: paper
---
# CAN-TEMPO: Unsupervised CAN Bus Intrusion Detection via Temporal Multi-Period Oscillation Encoding

## Novelty
CAN-TEMPO introduces an unsupervised CAN bus intrusion detection framework that explicitly models multi-periodic CAN traffic structure using a Temporal Multi-Periodic Oscillation block.

## Methodology
The method transforms one-dimensional CAN sequences into multi-scale two-dimensional representations through frequency-domain analysis, enabling capture of intra-period correlations and inter-period temporal variations. It is evaluated on public CAN intrusion detection benchmarks under diverse attack scenarios and generalization settings.

## Explicit Limitations
not stated

## Future Work
not stated

## Concept Hubs
[[Concept - CAN Intrusion Detection]]
[[Concept - Unsupervised Intrusion Detection]]
[[Concept - In-Vehicle Network Security]]
[[Concept - Network Traffic Analysis]]
[[Concept - Cross-Vehicle Transfer Learning]]

## Relevance Score
9

## Monitoring Transfer
doi: not stated
source_link: not stated
text_kind: abstract
monitoring_problem: CAN bus intrusion detection
signal: CAN message sequences with multi-periodic temporal patterns
uncertainty_method: not stated
action: flag anomalous CAN traffic
eval_setting: public CAN intrusion detection benchmarks with diverse attacks and cross-vehicle generalization
limitation_author: not stated
limitation_inference: Abstract does not address real-time computational cost, threshold calibration, or deployment on constrained ECUs
limitation_unknown: not stated
support_passage: We evaluate CAN-TEMPO on multiple public CAN intrusion detection benchmarks under diverse attack scenarios and generalization settings
transfer_ivn: Use TEMPO to monitor periodic CAN traffic for unsupervised intrusion detection in IVNs
transfer_risk: Periodicity assumptions may not hold for adaptive, encrypted, or non-periodic IVN traffic

#needs-review

## Record Fields
doi: https://doi.org/10.3390/technologies14060375
source_link: not stated
text_kind: abstract
monitoring_problem: CAN bus intrusion detection
signal: CAN message sequences with multi-periodic temporal patterns
uncertainty_method: not stated
action: flag anomalous CAN traffic
eval_setting: public CAN intrusion detection benchmarks with diverse attacks and cross-vehicle generalization
limitation_author: not stated
limitation_inference: Abstract does not address real-time computational cost, threshold calibration, or deployment on constrained ECUs
limitation_unknown: not stated
support_passage: We evaluate CAN-TEMPO on multiple public CAN intrusion detection benchmarks under diverse attack scenarios and generalization settings
transfer_ivn: Use TEMPO to monitor periodic CAN traffic for unsupervised intrusion detection in IVNs
transfer_risk: Periodicity assumptions may not hold for adaptive, encrypted, or non-periodic IVN traffic
