---
title: "ICSim++: A CAN/CAN FD simulator for modern vehicle networks with LLM-assisted workflows"
year: 2026
doi: "https://doi.org/10.1016/j.softx.2026.102722"
relevance_score: 0.35
type: paper
---
# ICSim++: A CAN/CAN FD simulator for modern vehicle networks with LLM-assisted workflows

## Novelty
ICSim++ is an open-source CAN/CAN FD simulation platform that extends ICSim with state-driven traffic generation, segmented multi-bus topologies with a virtual gateway, scriptable repeatable experiments, enhanced logging with optional interpretive annotations, and an optional LLM-assisted layer for natural-language command generation and log interpretation.

## Methodology
The work builds a simulation platform compatible with Linux SocketCAN workflows. It supports Classical CAN and CAN FD, generates traffic from internal vehicle variables, connects multiple buses through a virtual gateway, and provides scriptable experiment execution, logging, and optional LLM-assisted interaction for commands and log interpretation.

## Explicit Limitations
The platform does not target full vehicle or hardware-in-the-loop fidelity; it focuses on message-, architectural-, and workflow-level fidelity sufficient for reproducible academic research and teaching.

## Future Work
not stated

## Concept Hubs
[[Concept - In-Vehicle Network Security]], [[Concept - CAN Network Anomaly Detection]], [[Concept - Network Traffic Analysis]]

## Relevance Score
0.35

## Monitoring Transfer
doi: not stated
source_link: not stated
text_kind: abstract
monitoring_problem: reproducible CAN/CAN FD vehicle-network traffic monitoring and IDS evaluation
signal: CAN/CAN FD messages and internal vehicle state variables
uncertainty_method: not stated
action: natural-language command generation and log interpretation
eval_setting: academic research, teaching, automotive security experimentation, and IDS evaluation
limitation_author: not full vehicle or hardware-in-the-loop fidelity
limitation_inference: LLM-assisted log interpretation may introduce annotation bias
limitation_unknown: not stated
support_passage: Rather than targeting full vehicle or hardware-in-the-loop fidelity, ICSim++ focuses on message-, architectural-, and workflow-level fidelity sufficient for reproducible academic research and teaching.
transfer_ivn: Use ICSim++ to generate reproducible CAN/CAN FD traffic and logs for evaluating deep-learning intrusion detection in IVN
transfer_risk: Simulated message and workflow fidelity may not capture real ECU timing, gateway behavior, or attack side effects

#needs-review

## Record Fields
doi: https://doi.org/10.1016/j.softx.2026.102722
source_link: not stated
text_kind: abstract
monitoring_problem: reproducible CAN/CAN FD vehicle-network traffic monitoring and IDS evaluation
signal: CAN/CAN FD messages and internal vehicle state variables
uncertainty_method: not stated
action: natural-language command generation and log interpretation
eval_setting: academic research, teaching, automotive security experimentation, and IDS evaluation
limitation_author: not full vehicle or hardware-in-the-loop fidelity
limitation_inference: LLM-assisted log interpretation may introduce annotation bias
limitation_unknown: not stated
support_passage: Rather than targeting full vehicle or hardware-in-the-loop fidelity, ICSim++ focuses on message-, architectural-, and workflow-level fidelity sufficient for reproducible academic research and teaching.
transfer_ivn: Use ICSim++ to generate reproducible CAN/CAN FD traffic and logs for evaluating deep-learning intrusion detection in IVN
transfer_risk: Simulated message and workflow fidelity may not capture real ECU timing, gateway behavior, or attack side effects
