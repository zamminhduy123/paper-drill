---
title: "AEGIS-KD: Reliability-Guided Optimal-Transport Distillation for Lightweight IoT Intrusion Detection"
year: 2026
doi: "https://doi.org/10.5281/zenodo.22005948"
relevance_score: 9.711
type: paper
---
# AEGIS-KD: Reliability-Guided Optimal-Transport Distillation for Lightweight IoT Intrusion Detection

Novelty

The paper proposes AEGIS-KD, a reliability-guided optimal-transport distillation framework for lightweight IoT intrusion detection. Its novelty lies in using optimal transport to transfer knowledge from a teacher to a compact student model while guiding distillation by reliability estimates, improving robustness and efficiency under IoT resource constraints.

Methodology

The method applies knowledge distillation to compress a deep intrusion detection model into a lightweight student suitable for IoT deployment. It employs optimal-transport-based alignment between teacher and student representations, weighted by reliability-guided signals to suppress noisy or uncertain teacher outputs. Evaluation is conducted on IoT network intrusion detection benchmarks.

Explicit Limitations

Not stated.

Future Work

Not stated.

Concept Hubs

[[Concept - Knowledge Distillation]]
[[Concept - Optimal Transport]]
[[Concept - IoT Intrusion Detection]]
[[Concept - Reliability-Guided Learning]]
[[Concept - Lightweight Detection]]

Relevance Score

Medium

Monitoring Transfer

Monitoring problem: detecting network intrusions in resource-constrained IoT environments.
Signal: network traffic features and model representation discrepancies.
Uncertainty method: reliability-guided weighting of teacher outputs during distillation.
Action: deploy a lightweight student intrusion detector.
Evaluation setting: IoT network intrusion detection benchmarks.
Transfer to IVN: reliability-guided optimal-transport distillation could compress in-vehicle network intrusion detectors for resource-limited ECUs.
Transfer risk: IoT traffic statistics and attack distributions differ substantially from CAN/CAN FD in-vehicle traffic, so reliability estimates and optimal-transport alignments may not generalize.

doi: not stated
source_link: not stated
text_kind: abstract
monitoring_problem: network intrusion detection in IoT environments
signal: network traffic data and teacher-student representation alignment
uncertainty_method: reliability-guided optimal-transport distillation
action: lightweight student intrusion detection model deployment
eval_setting: IoT network intrusion detection benchmarks
limitation_author: not stated
limitation_inference: evaluation limited to IoT traffic; no validation on in-vehicle or other domain-specific networks; reliance on teacher reliability may propagate teacher bias
limitation_unknown: dataset specifics, model architectures, attack types, and computational cost are not stated
support_passage: AEGIS-KD: Reliability-Guided Optimal-Transport Distillation for Lightweight IoT Intrusion Detection
transfer_ivn: reliability-guided optimal-transport distillation for compressing in-vehicle network intrusion detectors
transfer_risk: IoT and IVN traffic differ in protocols, timing, and attack semantics, so distillation reliability and transport alignment may not transfer

The paper proposes AEGIS-KD, a reliability-guided optimal-transport distillation framework for lightweight IoT intrusion detection. Its novelty lies in using optimal transport to transfer knowledge from a teacher to a compact student model while guiding distillation by reliability estimates, improving robustness and efficiency under IoT resource constraints.

The method applies knowledge distillation to compress a deep intrusion detection model into a lightweight student suitable for IoT deployment. It employs optimal-transport-based alignment between teacher and student representations, weighted by reliability-guided signals to suppress noisy or uncertain teacher outputs. Evaluation is conducted on IoT network intrusion detection benchmarks.

Not stated.

Not stated.

[[Concept - Knowledge Distillation]]
[[Concept - Optimal Transport]]
[[Concept - IoT Intrusion Detection]]
[[Concept - Reliability-Guided Learning]]
[[Concept - Lightweight Detection]]

Medium

Monitoring problem: detecting network intrusions in resource-constrained IoT environments.
Signal: network traffic features and model representation discrepancies.
Uncertainty method: reliability-guided weighting of teacher outputs during distillation.
Action: deploy a lightweight student intrusion detector.
Evaluation setting: IoT network intrusion detection benchmarks.
Transfer to IVN: reliability-guided optimal-transport distillation could compress in-vehicle network intrusion detectors for resource-limited ECUs.
Transfer risk: IoT traffic statistics and attack distributions differ substantially from CAN/CAN FD in-vehicle traffic, so reliability estimates and optimal-transport alignments may not generalize.

doi: not stated
source_link: not stated
text_kind: abstract
monitoring_problem: network intrusion detection in IoT environments
signal: network traffic data and teacher-student representation alignment
uncertainty_method: reliability-guided optimal-transport distillation
action: lightweight student intrusion detection model deployment
eval_setting: IoT network intrusion detection benchmarks
limitation_author: not stated
limitation_inference: evaluation limited to IoT traffic; no validation on in-vehicle or other domain-specific networks; reliance on teacher reliability may propagate teacher bias
limitation_unknown: dataset specifics, model architectures, attack types, and computational cost are not stated
support_passage: AEGIS-KD: Reliability-Guided Optimal-Transport Distillation for Lightweight IoT Intrusion Detection
transfer_ivn: reliability-guided optimal-transport distillation for compressing in-vehicle network intrusion detectors
transfer_risk: IoT and IVN traffic differ in protocols, timing, and attack semantics, so distillation reliability and transport alignment may not transfer

#needs-review

## Record Fields
doi: https://doi.org/10.5281/zenodo.22005948
source_link: not stated
text_kind: abstract
monitoring_problem: detecting network intrusions in resource-constrained IoT environments.
signal: network traffic features and model representation discrepancies.
uncertainty_method: reliability-guided weighting of teacher outputs during distillation.
action: deploy a lightweight student intrusion detector.
eval_setting: IoT network intrusion detection benchmarks
limitation_author: not stated
limitation_inference: evaluation limited to IoT traffic; no validation on in-vehicle or other domain-specific networks; reliance on teacher reliability may propagate teacher bias
limitation_unknown: dataset specifics, model architectures, attack types, and computational cost are not stated
support_passage: AEGIS-KD: Reliability-Guided Optimal-Transport Distillation for Lightweight IoT Intrusion Detection
transfer_ivn: reliability-guided optimal-transport distillation for compressing in-vehicle network intrusion detectors
transfer_risk: IoT traffic statistics and attack distributions differ substantially from CAN/CAN FD in-vehicle traffic, so reliability estimates and optimal-transport alignments may not generalize.
