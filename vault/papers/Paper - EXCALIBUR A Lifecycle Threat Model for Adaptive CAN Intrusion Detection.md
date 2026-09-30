---
title: "EXCALIBUR: A Lifecycle Threat Model for Adaptive CAN Intrusion Detection"
year: 2026
doi: "https://doi.org/10.13140/rg.2.2.29872.52489"
relevance_score: 11.0
type: paper
---
# EXCALIBUR: A Lifecycle Threat Model for Adaptive CAN Intrusion Detection

Novelty

The paper introduces EXCALIBUR, a lifecycle threat model specifically designed for adaptive CAN intrusion detection systems. Unlike static threat models that assume fixed detection rules, EXCALIBUR addresses how threats and detection requirements evolve across the vehicle lifecycle—from design through production to post-deployment monitoring - 11 . The novelty lies in treating the intrusion detection system itself as a dynamic asset whose threat surface changes as the system learns and adapts, a dimension largely absent from conventional TARA frameworks that focus on static architectures - 5 - 10 .

Methodology

The methodology likely combines formal threat modeling techniques (STRIDE or attack trees) with the specific constraints of adaptive intrusion detection on CAN networks. The approach derives monitoring requirements by fusing threat analysis and risk assessment with attack-tree-based coverage analysis—a strategy recently proposed to guarantee sufficiency of CAN network monitoring - 11 . Lifecycle phases are mapped to detection adaptation triggers, ensuring that threats emerging during operation (e.g., concept drift, adversarial evasion) are accounted for in the detection model updates. The evaluation probably employs a CAN bus testbed with injected attacks across lifecycle stages to validate whether the threat model captures evolving detection gaps.

Explicit Limitations

Not stated in the search results. The abstract text provided in the query does not enumerate limitations, and no search result contains the full paper content. Based on the paper type (lifecycle threat model), likely limitations include: validation restricted to simulated CAN environments rather than production vehicles, and difficulty quantifying threat evolution across real-world firmware update cycles.

Future Work

Not stated in the search results. Inferred avenues based on the topic include: extending the lifecycle threat model to CAN FD and automotive Ethernet, integrating with ISO/SAE 21434 compliance workflows for post-production monitoring - 5 - 10 , and validating the framework against adversarial attacks specifically designed to poison adaptive intrusion detection models over time.

Concept Hubs

[[Concept - In-Vehicle Network Security]]
[[Concept - Deep Learning Intrusion Detection]]
[[Concept - CAN Network Anomaly Detection]]
[[Concept - AI-Ready Security Framework]]
[[Concept - Functional Safety Verification]]

Relevance Score

High for IVN security research focused on detection lifecycle management; moderate for general CAN intrusion detection literature. The paper addresses a gap between static threat models and adaptive detection systems, but without access to the full text (no DOI, source, or passage available in results), its specific technical contributions cannot be verified against existing frameworks like AutoGuardX or the risk-based monitoring framework - 9 - 11 .

Monitoring Transfer

Monitoring problem: Ensuring adaptive CAN intrusion detection systems maintain threat coverage as detection models evolve across the vehicle lifecycle.
Signal: CAN bus message patterns, error frames, and detection model confidence scores.
Uncertainty method: Lifecycle-aware threat modeling that propagates risk across design, production, and operational phases.
Action: Update intrusion detection rules or retrain models when lifecycle threat model indicates coverage degradation.
Evaluation setting: CAN bus testbed with staged attack injections simulating different lifecycle phases (design-time, post-deployment, adversarial adaptation).

Transfer to IVN: Adaptive detection requires knowing when threats change, not just what threats exist—EXCALIBUR provides a temporal mapping that static TARA cannot deliver.

Transfer risk: If the lifecycle stages assumed in the model do not match real OEM update cycles or aftermarket ECU replacements, the detection adaptation triggers may fire at wrong times, causing either false alerts or missed novel attacks.

doi: not stated
source_link: not stated
text_kind: not stated
monitoring_problem: Ensuring adaptive CAN intrusion detection maintains threat coverage as detection models evolve across the vehicle lifecycle
signal: CAN bus message patterns, error frames, and detection model confidence scores
uncertainty_method: Lifecycle-aware threat modeling that propagates risk across design, production, and operational phases
action: Update intrusion detection rules or retrain models when lifecycle threat model indicates coverage degradation
eval_setting: CAN bus testbed with staged attack injections simulating different lifecycle phases
limitation_author: not stated
limitation_inference: Validation restricted to simulated CAN environments rather than production vehicles; difficulty quantifying threat evolution across real-world firmware update cycles
limitation_unknown: Whether the lifecycle threat model has been empirically validated against adversarial adaptation or concept drift attacks
support_passage: not stated
transfer_ivn: Adaptive detection requires knowing when threats change, not just what threats exist; EXCALIBUR provides a temporal mapping that static TARA cannot deliver
transfer_risk: Lifecycle stages assumed in the model may not match real OEM update cycles or aftermarket ECU replacements, causing detection adaptation triggers to fire at wrong times

The paper introduces EXCALIBUR, a lifecycle threat model specifically designed for adaptive CAN intrusion detection systems. Unlike static threat models that assume fixed detection rules, EXCALIBUR addresses how threats and detection requirements evolve across the vehicle lifecycle—from design through production to post-deployment monitoring - 11 . The novelty lies in treating the intrusion detection system itself as a dynamic asset whose threat surface changes as the system learns and adapts, a dimension largely absent from conventional TARA frameworks that focus on static architectures - 5 - 10 .

- 11

- 5

- 10

The methodology likely combines formal threat modeling techniques (STRIDE or attack trees) with the specific constraints of adaptive intrusion detection on CAN networks. The approach derives monitoring requirements by fusing threat analysis and risk assessment with attack-tree-based coverage analysis—a strategy recently proposed to guarantee sufficiency of CAN network monitoring - 11 . Lifecycle phases are mapped to detection adaptation triggers, ensuring that threats emerging during operation (e.g., concept drift, adversarial evasion) are accounted for in the detection model updates. The evaluation probably employs a CAN bus testbed with injected attacks across lifecycle stages to validate whether the threat model captures evolving detection gaps.

- 11

Not stated in the search results. The abstract text provided in the query does not enumerate limitations, and no search result contains the full paper content. Based on the paper type (lifecycle threat model), likely limitations include: validation restricted to simulated CAN environments rather than production vehicles, and difficulty quantifying threat evolution across real-world firmware update cycles.

Not stated in the search results. Inferred avenues based on the topic include: extending the lifecycle threat model to CAN FD and automotive Ethernet, integrating with ISO/SAE 21434 compliance workflows for post-production monitoring - 5 - 10 , and validating the framework against adversarial attacks specifically designed to poison adaptive intrusion detection models over time.

- 5

- 10

[[Concept - In-Vehicle Network Security]]
[[Concept - Deep Learning Intrusion Detection]]
[[Concept - CAN Network Anomaly Detection]]
[[Concept - AI-Ready Security Framework]]
[[Concept - Functional Safety Verification]]

High for IVN security research focused on detection lifecycle management; moderate for general CAN intrusion detection literature. The paper addresses a gap between static threat models and adaptive detection systems, but without access to the full text (no DOI, source, or passage available in results), its specific technical contributions cannot be verified against existing frameworks like AutoGuardX or the risk-based monitoring framework - 9 - 11 .

- 9

- 11

Monitoring problem: Ensuring adaptive CAN intrusion detection systems maintain threat coverage as detection models evolve across the vehicle lifecycle.
Signal: CAN bus message patterns, error frames, and detection model confidence scores.
Uncertainty method: Lifecycle-aware threat modeling that propagates risk across design, production, and operational phases.
Action: Update intrusion detection rules or retrain models when lifecycle threat model indicates coverage degradation.
Evaluation setting: CAN bus testbed with staged attack injections simulating different lifecycle phases (design-time, post-deployment, adversarial adaptation).

Transfer to IVN: Adaptive detection requires knowing when threats change, not just what threats exist—EXCALIBUR provides a temporal mapping that static TARA cannot deliver.

Transfer risk: If the lifecycle stages assumed in the model do not match real OEM update cycles or aftermarket ECU replacements, the detection adaptation triggers may fire at wrong times, causing either false alerts or missed novel attacks.

doi: not stated
source_link: not stated
text_kind: not stated
monitoring_problem: Ensuring adaptive CAN intrusion detection maintains threat coverage as detection models evolve across the vehicle lifecycle
signal: CAN bus message patterns, error frames, and detection model confidence scores
uncertainty_method: Lifecycle-aware threat modeling that propagates risk across design, production, and operational phases
action: Update intrusion detection rules or retrain models when lifecycle threat model indicates coverage degradation
eval_setting: CAN bus testbed with staged attack injections simulating different lifecycle phases
limitation_author: not stated
limitation_inference: Validation restricted to simulated CAN environments rather than production vehicles; difficulty quantifying threat evolution across real-world firmware update cycles
limitation_unknown: Whether the lifecycle threat model has been empirically validated against adversarial adaptation or concept drift attacks
support_passage: not stated
transfer_ivn: Adaptive detection requires knowing when threats change, not just what threats exist; EXCALIBUR provides a temporal mapping that static TARA cannot deliver
transfer_risk: Lifecycle stages assumed in the model may not match real OEM update cycles or aftermarket ECU replacements, causing detection adaptation triggers to fire at wrong times

#needs-review

## Record Fields
doi: https://doi.org/10.13140/rg.2.2.29872.52489
source_link: not stated
text_kind: abstract
monitoring_problem: Ensuring adaptive CAN intrusion detection systems maintain threat coverage as detection models evolve across the vehicle lifecycle.
signal: CAN bus message patterns, error frames, and detection model confidence scores.
uncertainty_method: Lifecycle-aware threat modeling that propagates risk across design, production, and operational phases.
action: Update intrusion detection rules or retrain models when lifecycle threat model indicates coverage degradation.
eval_setting: CAN bus testbed with staged attack injections simulating different lifecycle phases
limitation_author: not stated
limitation_inference: Validation restricted to simulated CAN environments rather than production vehicles; difficulty quantifying threat evolution across real-world firmware update cycles
limitation_unknown: Whether the lifecycle threat model has been empirically validated against adversarial adaptation or concept drift attacks
support_passage: not stated
transfer_ivn: Adaptive detection requires knowing when threats change, not just what threats exist; EXCALIBUR provides a temporal mapping that static TARA cannot deliver
transfer_risk: If the lifecycle stages assumed in the model do not match real OEM update cycles or aftermarket ECU replacements, the detection adaptation triggers may fire at wrong times, causing either false alerts or missed novel attacks.
