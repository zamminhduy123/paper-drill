---
title: "Lightweight Physical-based Intrusion Detection Systems for In-Vehicle Communication Networks"
year: 2026
doi: "https://doi.org/10.17169/refubium-51285"
relevance_score: 0.95
type: paper
---
# Lightweight Physical-based Intrusion Detection Systems for In-Vehicle Communication Networks

## Novelty
Development and evaluation of three lightweight physical-based IDS/IDPS approaches for CAN/CAN-FD: VALID using voltage levels, ASSASSIN using temporal features, and SPARTA using signal arrival differences, with automotive design criteria and embedded/real-vehicle evaluation.

## Methodology
Literature review and component data-sheet analysis of analog signal variation origins; derivation of automotive constraints and design criteria; development of three physical-feature-based detection/prevention approaches; evaluation on embedded platforms using prototype CAN-FD traffic and real vehicles.

## Explicit Limitations
not stated

## Future Work
not stated

## Concept Hubs
[[Concept - CAN Intrusion Detection]]
[[Concept - Lightweight Detection]]
[[Concept - Physical Semantics Detection]]
[[Concept - In-Vehicle Network Security]]
[[Concept - Real-Time Attack Defense]]

## Relevance Score
0.95

## Monitoring Transfer
doi: not stated
source_link: not stated
text_kind: abstract
monitoring_problem: detect unauthorized ECU transmissions and assess message authenticity on CAN/CAN-FD
signal: CAN bus voltage levels, clock skew, signal rise/fall times, and signal arrival differences
uncertainty_method: not stated
action: detect unauthorized transmissions, classify transmitting ECUs, and actively prevent unauthorized messages
eval_setting: embedded platforms using prototype CAN-FD bus traffic and real vehicles
limitation_author: not stated
limitation_inference: physical signal features may vary with ECU hardware, cable topology, temperature, aging, and bus load, reducing cross-vehicle reliability
limitation_unknown: not stated
support_passage: SPARTA measures signal arrival differences to identify ECUs and implements active prevention, achieving a 100% detection rate while meeting real-time and resource constraints
transfer_ivn: monitor IVN ECU authenticity using CAN/CAN-FD analog voltage, timing, and arrival-time features to detect spoofed or unauthorized messages
transfer_risk: vehicle-specific wiring, ECU hardware, temperature, aging, and bus load can change physical features, causing detection failure across vehicles or after component replacement

#needs-review

## Record Fields
doi: https://doi.org/10.17169/refubium-51285
source_link: not stated
text_kind: abstract
monitoring_problem: detect unauthorized ECU transmissions and assess message authenticity on CAN/CAN-FD
signal: CAN bus voltage levels, clock skew, signal rise/fall times, and signal arrival differences
uncertainty_method: not stated
action: detect unauthorized transmissions, classify transmitting ECUs, and actively prevent unauthorized messages
eval_setting: embedded platforms using prototype CAN-FD bus traffic and real vehicles
limitation_author: not stated
limitation_inference: physical signal features may vary with ECU hardware, cable topology, temperature, aging, and bus load, reducing cross-vehicle reliability
limitation_unknown: not stated
support_passage: SPARTA measures signal arrival differences to identify ECUs and implements active prevention, achieving a 100% detection rate while meeting real-time and resource constraints
transfer_ivn: monitor IVN ECU authenticity using CAN/CAN-FD analog voltage, timing, and arrival-time features to detect spoofed or unauthorized messages
transfer_risk: vehicle-specific wiring, ECU hardware, temperature, aging, and bus load can change physical features, causing detection failure across vehicles or after component replacement
