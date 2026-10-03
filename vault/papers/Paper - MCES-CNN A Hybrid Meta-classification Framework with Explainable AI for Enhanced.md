---
title: "MCES-CNN: A Hybrid Meta-classification Framework with Explainable AI for Enhanced IoT Intrusion Detection"
year: 2026
doi: "https://doi.org/10.1007/s44196-026-01426-5"
relevance_score: 0.95
type: paper
---
# MCES-CNN: A Hybrid Meta-classification Framework with Explainable AI for Enhanced IoT Intrusion Detection

## Novelty
MCES-CNN combines meta-classification ensemble stacking, CNN-based classification, LIME-based explainability, and compression-aware pruning/quantization for IoT intrusion detection.

## Methodology
Traditional classifiers are stacked to generate high-level predictive features, which are processed by an optimized CNN. LIME provides quantitative feature attribution to support interpretability and false-positive reduction. Structured pruning and quantization are evaluated for memory footprint and inference latency on representative IoT hardware. Experiments use CIC-IDS2017, EIIoT, and RT-IoT2022.

## Explicit Limitations
not stated

## Future Work
not stated

## Concept Hubs
[[Concept - IoT Intrusion Detection]]
[[Concept - Deep Learning Intrusion Detection]]
[[Concept - Explainable Intrusion Detection]]
[[Concept - Stacking Ensemble]]
[[Concept - Resource-Constrained Edge]]

## Relevance Score
0.95

## Monitoring Transfer
Monitoring problem: detect malicious traffic in IoT networks.
Signal: stacked classifier predictive features derived from network traffic.
Uncertainty method: not stated.
Resulting action: classify traffic and suppress false positives using LIME feature attribution.
Evaluation setting: CIC-IDS2017, EIIoT, RT-IoT2022, and representative IoT hardware.
Transfer to IVN: apply MCES-CNN to in-vehicle network intrusion detection on edge ECUs.
Transfer risk: IoT traffic features and attack distributions may not match in-vehicle network protocols.

doi: not stated
source_link: not stated
text_kind: abstract
monitoring_problem: IoT network intrusion detection
signal: stacked classifier predictive features from network traffic
uncertainty_method: not stated
action: classify traffic and reduce false positives using LIME feature attribution
eval_setting: CIC-IDS2017, EIIoT, RT-IoT2022, representative IoT hardware
limitation_author: not stated
limitation_inference: benchmark results may not capture live heterogeneous IoT deployment variability
limitation_unknown: not stated
support_passage: Experimental validation on benchmark datasets CIC-IDS2017, EIIoT, and RT-IoT2022- demonstrated the effectiveness of MCES-CNN, achieving 99.95% binary and 98.29% multiclass accuracy
transfer_ivn: apply MCES-CNN to in-vehicle network intrusion detection on edge ECUs
transfer_risk: IoT traffic and attack patterns may not transfer to in-vehicle network protocols

#needs-review

## Record Fields
doi: https://doi.org/10.1007/s44196-026-01426-5
source_link: not stated
text_kind: abstract
monitoring_problem: detect malicious traffic in IoT networks.
signal: stacked classifier predictive features derived from network traffic.
uncertainty_method: not stated.
action: classify traffic and reduce false positives using LIME feature attribution
eval_setting: CIC-IDS2017, EIIoT, RT-IoT2022, representative IoT hardware
limitation_author: not stated
limitation_inference: benchmark results may not capture live heterogeneous IoT deployment variability
limitation_unknown: not stated
support_passage: Experimental validation on benchmark datasets CIC-IDS2017, EIIoT, and RT-IoT2022- demonstrated the effectiveness of MCES-CNN, achieving 99.95% binary and 98.29% multiclass accuracy
transfer_ivn: apply MCES-CNN to in-vehicle network intrusion detection on edge ECUs
transfer_risk: IoT traffic features and attack distributions may not match in-vehicle network protocols.
