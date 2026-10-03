---
title: "A Multiplication-Free Feature Extractor for Signal Classification: Keyword Spotting Case Study"
year: 2026
doi: "https://doi.org/10.48550/arxiv.2608.17108"
relevance_score: 9.0
type: paper
---
# A Multiplication-Free Feature Extractor for Signal Classification: Keyword Spotting Case Study

## Novelty
The paper proposes next iRDT, a multiplication-free feature extractor for keyword spotting that uses only simple, energy-efficient arithmetic operators. It targets TinyML and ultra-low-power edge devices, claiming accuracy comparable to MFCC- or CNN-based extractors with suitable classifiers and at least one order of magnitude lower CPU processing time than MFCC.

## Methodology
The authors evaluate next iRDT on the Google KWS 12-class keyword spotting dataset. The method is compared against MFCC and CNN-based feature extractors using baseline classifiers. The system is tuned for KWS, and a different classifier achieves 94.7% validation accuracy. CPU processing time and hardware footprint are used to assess complexity and suitability for edge deployment.

## Explicit Limitations
Not stated in the abstract.

## Future Work
Not stated in the abstract.

## Concept Hubs
[[Concept - Edge AI Inference]]
[[Concept - TinyML Systems]]
[[Concept - Resource-Constrained Edge]]
[[Concept - Energy-Aware Inference]]

## Relevance Score
9/10

## Monitoring Transfer
doi:
not stated
source_link:
not stated
text_kind:
abstract
monitoring_problem:
keyword spotting and speech command classification on resource-constrained edge devices
signal:
audio speech signal processed by the next iRDT feature extractor
uncertainty_method:
not stated
action:
classify detected speech commands or keywords
eval_setting:
Google KWS 12-classes dataset with validation accuracy and CPU processing time comparison
limitation_author:
not stated
limitation_inference:
evaluation is limited to keyword spotting on the Google KWS dataset and CPU processing time, without full edge-device power, latency, or hardware deployment benchmarks
limitation_unknown:
not stated
support_passage:
our algorithm is multiplier-free and it employs only simple, energy-efficient arithmetic operators
transfer_ivn:
apply next iRDT as a low-complexity feature extractor for in-vehicle network event classification or lightweight anomaly detection
transfer_risk:
audio keyword features may not capture in-vehicle network protocol dynamics, and performance may degrade without IVN-specific tuning, labels, and uncertainty calibration

#needs-review

## Record Fields
doi: https://doi.org/10.48550/arxiv.2608.17108
source_link: not stated
text_kind: abstract
monitoring_problem: keyword spotting and speech command classification on resource-constrained edge devices
signal: audio speech signal processed by the next iRDT feature extractor
uncertainty_method: not stated
action: classify detected speech commands or keywords
eval_setting: Google KWS 12-classes dataset with validation accuracy and CPU processing time comparison
limitation_author: not stated
limitation_inference: evaluation is limited to keyword spotting on the Google KWS dataset and CPU processing time, without full edge-device power, latency, or hardware deployment benchmarks
limitation_unknown: not stated
support_passage: our algorithm is multiplier-free and it employs only simple, energy-efficient arithmetic operators
transfer_ivn: apply next iRDT as a low-complexity feature extractor for in-vehicle network event classification or lightweight anomaly detection
transfer_risk: audio keyword features may not capture in-vehicle network protocol dynamics, and performance may degrade without IVN-specific tuning, labels, and uncertainty calibration
