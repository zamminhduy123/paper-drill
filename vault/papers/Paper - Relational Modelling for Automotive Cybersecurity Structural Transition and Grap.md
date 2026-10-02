---
title: "Relational Modelling for Automotive Cybersecurity: Structural Transition and Graph-Topology-Based CAN Intrusion Detection"
year: 2026
doi: "https://doi.org/10.3390/s26102964"
relevance_score: 95.0
type: paper
---
# Relational Modelling for Automotive Cybersecurity: Structural Transition and Graph-Topology-Based CAN Intrusion Detection

## Novelty
- Systematic stress-testing of relational CAN traffic representations for intrusion detection.
- Identifies a four-level transfer hierarchy: statistical, structural transition, graph topology, and hybrid features.
- Provides boundary conditions for when relational CAN representations transfer across attacks and vehicle platforms.
- Shows that structural identifier transition features are the most robust cross-attack representation within a platform.
- Demonstrates that cross-dataset transfer depends on whether an attack perturbs identifier transition regularity.

## Methodology
- Lightweight intrusion-detection framework built from sliding windows of CAN frames.
- Features include statistical traffic descriptors, structural identifier transition features, and graph topology representations.
- CAN is treated as a broadcast-only bus, so features capture temporal scheduling regularity of identifier broadcasts rather than directed inter-ECU dependencies.
- Framework is evaluated under cross-attack and cross-dataset transfer stress tests.
- Four classifiers are used to assess feature robustness.
- Cross-dataset evaluation includes the ROAD dataset.
- Vehicle-specific calibration uses 10% of target-vehicle normal traffic to close the correlated-attack generalization gap.

## Explicit Limitations
- Statistical features collapse under cross-attack transfer, with ROC-AUC as low as 0.009.
- Graph topology features are scenario-dependent and produce sub-random results in Fuzzy-trained scenarios.
- Structural transition features do not detect attacks that affect only payload semantics, such as speedometer attacks.
- Structural transition features do not detect attacks that exploit identifier-space novelty, such as fuzzing.
- Cross-platform transfer is limited to attacks that perturb identifier transition regularity.

## Future Work
not stated

## Concept Hubs
[[Concept - CAN Intrusion Detection]]
[[Concept - In-Vehicle Network Security]]
[[Concept - Cross-Dataset Evaluation]]
[[Concept - Lightweight Detection]]
[[Concept - Cross-Vehicle Transfer Learning]]

## Relevance Score
95

## Monitoring Transfer
doi: not stated
source_link: not stated
text_kind: abstract
monitoring_problem: Detect CAN intrusion across attacks and vehicle platforms using relational traffic structure
signal: statistical descriptors, structural identifier transition features, and graph topology from sliding windows
uncertainty_method: not stated
action: raise intrusion detection alert
eval_setting: cross-attack and cross-dataset transfer stress testing with four classifiers and ROAD dataset
limitation_author: statistical features fail cross-attack transfer, graph topology is sub-random in fuzzy-trained scenarios, and structural features miss payload-only speedometer and identifier-space fuzzing attacks
limitation_inference: features depend on identifier transition regularity, so attacks preserving broadcast timing or changing only payload semantics can evade detection
limitation_unknown: not stated
support_passage: structural representations transfer only when an attack perturbs identifier transition regularity
transfer_ivn: structural identifier transition features transfer to IVN CAN intrusion detection when attacks alter broadcast scheduling regularity, with 10 percent target-vehicle normal traffic calibration
transfer_risk: transfer may fail for payload-semantics-only attacks or identifier-space novelty fuzzing that do not perturb identifier transition regularity

#needs-review

## Record Fields
doi: https://doi.org/10.3390/s26102964
source_link: not stated
text_kind: abstract
monitoring_problem: Detect CAN intrusion across attacks and vehicle platforms using relational traffic structure
signal: statistical descriptors, structural identifier transition features, and graph topology from sliding windows
uncertainty_method: not stated
action: raise intrusion detection alert
eval_setting: cross-attack and cross-dataset transfer stress testing with four classifiers and ROAD dataset
limitation_author: statistical features fail cross-attack transfer, graph topology is sub-random in fuzzy-trained scenarios, and structural features miss payload-only speedometer and identifier-space fuzzing attacks
limitation_inference: features depend on identifier transition regularity, so attacks preserving broadcast timing or changing only payload semantics can evade detection
limitation_unknown: not stated
support_passage: structural representations transfer only when an attack perturbs identifier transition regularity
transfer_ivn: structural identifier transition features transfer to IVN CAN intrusion detection when attacks alter broadcast scheduling regularity, with 10 percent target-vehicle normal traffic calibration
transfer_risk: transfer may fail for payload-semantics-only attacks or identifier-space novelty fuzzing that do not perturb identifier transition regularity
