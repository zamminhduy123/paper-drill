---
title: "CAN-FD ECU Authentication Using Voltage-Characteristic Hardware Fingerprints"
year: 2026
doi: "https://doi.org/10.3390/electronics15051094"
relevance_score: 9.0
type: paper
---
# CAN-FD ECU Authentication Using Voltage-Characteristic Hardware Fingerprints

## Novelty
The paper proposes CAN-FD ECU authentication using voltage hardware fingerprints (VHFs) as identity credentials. A single CAN-FD frame combines control-field voltage characteristics and data-field edges to form stable, distinguishable node fingerprints. It also proposes a lightweight vehicle intrusion detection scheme to identify attack types and locate compromised ECUs in real time.

## Methodology
The method extracts voltage characteristics from the control field and edge features from the data field of a single CAN-FD frame to construct hardware fingerprints. The VHF offset behavior under spoofing and wire-tapping attacks is analyzed. A lightweight VIDS is then used to classify attack scenarios and identify the compromised ECU. Experiments are conducted on a six-node prototype system under substitution, masquerade, injection, and wire-tapping attacks.

## Explicit Limitations
not stated

## Future Work
not stated

## Concept Hubs
[[Concept - In-Vehicle Network Security]]
[[Concept - CAN Intrusion Detection]]
[[Concept - Lightweight Detection]]
[[Concept - Physical Semantics Detection]]
[[Concept - Real-Time Attack Defense]]

## Relevance Score
9

## Monitoring Transfer
doi:
not stated
source_link:
not stated
text_kind:
abstract
monitoring_problem:
identify compromised ECU and attack type in CAN-FD networks
signal:
voltage characteristics in the control field and data-field edges from a single CAN-FD frame
uncertainty_method:
not stated
action:
authenticate ECU identity, identify attack type, and locate compromised ECU
eval_setting:
six-node prototype system with substitution, masquerade, injection, and wire-tapping attacks
limitation_author:
not stated
limitation_inference:
voltage fingerprints may be affected by temperature, supply variation, aging, wiring differences, and manufacturing variability
limitation_unknown:
not stated
support_passage:
a single frame of data is utilized to integrate the control field’s voltage characteristics and data field’s edges, forming stable and distinguishable hardware fingerprints
transfer_ivn:
apply single-frame voltage-fingerprint ECU authentication and lightweight VIDS to CAN-FD nodes in IVNs for real-time identity verification and attack localization
transfer_risk:
production IVN voltage variability and hardware spoofing may reduce fingerprint stability and distinguishability

#needs-review

## Record Fields
doi: https://doi.org/10.3390/electronics15051094
source_link: not stated
text_kind: abstract
monitoring_problem: identify compromised ECU and attack type in CAN-FD networks
signal: voltage characteristics in the control field and data-field edges from a single CAN-FD frame
uncertainty_method: not stated
action: authenticate ECU identity, identify attack type, and locate compromised ECU
eval_setting: six-node prototype system with substitution, masquerade, injection, and wire-tapping attacks
limitation_author: not stated
limitation_inference: voltage fingerprints may be affected by temperature, supply variation, aging, wiring differences, and manufacturing variability
limitation_unknown: not stated
support_passage: a single frame of data is utilized to integrate the control field’s voltage characteristics and data field’s edges, forming stable and distinguishable hardware fingerprints
transfer_ivn: apply single-frame voltage-fingerprint ECU authentication and lightweight VIDS to CAN-FD nodes in IVNs for real-time identity verification and attack localization
transfer_risk: production IVN voltage variability and hardware spoofing may reduce fingerprint stability and distinguishability
