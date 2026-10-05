---
title: "Adaptive TinyML with Shift-Aware Routing for Human Activity Recognition Under Distribution Shifts"
year: 2026
doi: "https://doi.org/10.3390/app16199711"
relevance_score: 92.0
type: paper
---
# Adaptive TinyML with Shift-Aware Routing for Human Activity Recognition Under Distribution Shifts

## Novelty
Shift-aware adaptive TinyML framework that combines prediction confidence with a source-derived feature-space shift score to route HAR samples across multi-exit depths, plus guarded label-free test-time adaptation for persistent severe shifts.

## Methodology
Lightweight multi-exit model classifies confident samples early and routes uncertain or shifted samples to deeper exits; a source-derived shift score complements confidence routing; persistent severe shifts trigger guarded label-free test-time adaptation; evaluated on REALDISP, WISDM, and PAMAP2.

## Explicit Limitations
Deeper inference alone may not overcome severe domain mismatch, and performance gains are scenario-dependent, with no significant differences in REALDISP SELF or PAMAP2 ANKLE.

## Future Work
not stated

## Concept Hubs
[[Concept - Edge AI Inference]], [[Concept - TinyML Systems]], [[Concept - Resource-Constrained Edge]], [[Concept - Energy-Aware Inference]], [[Concept - Cross-Dataset Evaluation]]

## Relevance Score
92

## Monitoring Transfer
doi: not stated
source_link: not stated
text_kind: abstract
monitoring_problem: Human activity recognition under distribution shifts on resource-constrained wearable and edge devices
signal: Prediction confidence and source-derived feature-space shift score
uncertainty_method: Confidence-based routing with shift-score routing and guarded label-free test-time adaptation
action: Route confident samples to early exits and uncertain or shifted samples to deeper exits, increasing computation when sensing conditions change
eval_setting: REALDISP, WISDM, and PAMAP2 benchmarks covering sensor-displacement, sensing-domain, unseen-user, and body-location shifts
limitation_author: not stated
limitation_inference: Deeper inference alone may not overcome severe domain mismatch, and benefits depend on the shift scenario
limitation_unknown: not stated
support_passage: deeper inference alone may not overcome severe domain mismatch
transfer_ivn: Use confidence and feature-space shift scores to route in-vehicle network anomaly detection samples to deeper detectors under vehicle, sensor, or traffic domain shifts
transfer_risk: IVN traffic may lack a reliable source-derived shift score, and severe domain mismatch may require labeled adaptation beyond label-free test-time adaptation

#needs-review

## Record Fields
doi: https://doi.org/10.3390/app16199711
source_link: not stated
text_kind: abstract
monitoring_problem: Human activity recognition under distribution shifts on resource-constrained wearable and edge devices
signal: Prediction confidence and source-derived feature-space shift score
uncertainty_method: Confidence-based routing with shift-score routing and guarded label-free test-time adaptation
action: Route confident samples to early exits and uncertain or shifted samples to deeper exits, increasing computation when sensing conditions change
eval_setting: REALDISP, WISDM, and PAMAP2 benchmarks covering sensor-displacement, sensing-domain, unseen-user, and body-location shifts
limitation_author: not stated
limitation_inference: Deeper inference alone may not overcome severe domain mismatch, and benefits depend on the shift scenario
limitation_unknown: not stated
support_passage: deeper inference alone may not overcome severe domain mismatch
transfer_ivn: Use confidence and feature-space shift scores to route in-vehicle network anomaly detection samples to deeper detectors under vehicle, sensor, or traffic domain shifts
transfer_risk: IVN traffic may lack a reliable source-derived shift score, and severe domain mismatch may require labeled adaptation beyond label-free test-time adaptation
