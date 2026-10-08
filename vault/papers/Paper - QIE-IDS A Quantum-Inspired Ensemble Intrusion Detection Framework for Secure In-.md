---
title: "QIE-IDS: A Quantum-Inspired Ensemble Intrusion Detection Framework for Secure In-Vehicle CAN Networks"
year: 2026
doi: "10.1109/ICAUC68182.2026.11441047"
relevance_score: 0.95
type: paper
---
# QIE-IDS: A Quantum-Inspired Ensemble Intrusion Detection Framework for Secure In-Vehicle CAN Networks

## Novelty
Proposes QIE-IDS, a quantum-inspired ensemble intrusion detection framework for in-vehicle CAN networks that combines a self-learning Enhanced Cuckoo Filter pre-filter, simulated quantum-inspired feature enhancement, and an ensemble of deep learning models for real-time CAN intrusion detection.

## Methodology
CAN traffic is first pre-filtered by a self-learning Enhanced Cuckoo Filter to separate known normal and malicious patterns. Remaining traffic is enhanced using simulated quantum rotation and superposition concepts, then classified by an ensemble containing a Temporal Attention Transformer, CNN-LSTM, Quantum-Inspired Neural Network, and hybrid deep model. Model outputs are combined using weighted voting, and the system is evaluated on the Car Hacking Dataset and a CAN train-and-test dataset under DoS, fuzzy, gear, and RPM attacks.

## Explicit Limitations
- Does not focus on cryptographic authentication.
- Does not focus on blockchain-based security.
- Does not focus on non-CAN vehicular communication protocols.

## Future Work
Not stated in the provided excerpt; only general future improvements and extensions are mentioned.

## Concept Hubs
[[Concept - CAN Intrusion Detection]]
[[Concept - Deep Learning Intrusion Detection]]
[[Concept - Quantum-Classical Detection]]
[[Concept - Lightweight Detection]]
[[Concept - Heterogeneous Base Learners]]

## Relevance Score
0.95

## Monitoring Transfer
doi: 10.1109/ICAUC68182.2026.11441047
source_link: https://doi.org/10.1109/ICAUC68182.2026.11441047
text_kind: conference paper
monitoring_problem: real-time intrusion detection in in-vehicle CAN networks
signal: CAN message traffic features after ECF pre-filtering and quantum-inspired feature enhancement
uncertainty_method: not stated
action: classify CAN messages as normal or malicious
eval_setting: Car Hacking Dataset and CAN train-and-test dataset under DoS, fuzzy, gear, and RPM attacks
limitation_author: does not focus on cryptographic authentication, blockchain-based security, or non-CAN vehicular communication protocols
limitation_inference: simulated quantum-inspired features and ensemble deep learning may not retain claimed latency and CPU efficiency on constrained ECUs
limitation_unknown: not stated
support_passage: The proposed system is evaluated using the Car Hacking Dataset (CHD) and the CAN train-and-test dataset under multiple attack scenarios such as DoS, fuzzy, gear, and RPM attacks.
transfer_ivn: apply ECF pre-filtering, quantum-inspired feature enhancement, and ensemble deep learning to CAN bus intrusion detection
transfer_risk: the multi-model ensemble and simulated quantum-inspired module may exceed real-time CPU and latency budgets on constrained automotive ECUs

#needs-review

## Record Fields
doi: 10.1109/ICAUC68182.2026.11441047
source_link: https://doi.org/10.1109/ICAUC68182.2026.11441047
text_kind: fulltext
monitoring_problem: real-time intrusion detection in in-vehicle CAN networks
signal: CAN message traffic features after ECF pre-filtering and quantum-inspired feature enhancement
uncertainty_method: not stated
action: classify CAN messages as normal or malicious
eval_setting: Car Hacking Dataset and CAN train-and-test dataset under DoS, fuzzy, gear, and RPM attacks
limitation_author: does not focus on cryptographic authentication, blockchain-based security, or non-CAN vehicular communication protocols
limitation_inference: simulated quantum-inspired features and ensemble deep learning may not retain claimed latency and CPU efficiency on constrained ECUs
limitation_unknown: not stated
support_passage: The proposed system is evaluated using the Car Hacking Dataset (CHD) and the CAN train-and-test dataset under multiple attack scenarios such as DoS, fuzzy, gear, and RPM attacks.
transfer_ivn: apply ECF pre-filtering, quantum-inspired feature enhancement, and ensemble deep learning to CAN bus intrusion detection
transfer_risk: the multi-model ensemble and simulated quantum-inspired module may exceed real-time CPU and latency budgets on constrained automotive ECUs
