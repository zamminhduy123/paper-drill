---
title: "CarDS - Controller Area Network and Automotive Ethernet Realistic Data Set"
year: 2026
doi: "https://doi.org/10.48328/tudatalib-2179"
relevance_score: 0.95
type: paper
---
# CarDS - Controller Area Network and Automotive Ethernet Realistic Data Set

## Novelty
A large multi-protocol in-vehicle network dataset from a 2020 commercial electric vehicle, combining CAN CC, CAN FD, and Automotive Ethernet traffic with benign and advanced attack scenarios.

## Methodology
Real in-vehicle network data were recorded from a modern commercial electric vehicle with 10 internal CAN buses and 6 Automotive Ethernet buses. The dataset contains 258 traces, 9h07m09s of traffic, 397,383,125 CAN messages, and 180,604,377 Automotive Ethernet messages. A pseudonymization pipeline was applied to MAC/IP headers, ICMP metadata, VIN, OEM references, and attack payloads, while raw payloads were released without DBC files or reverse-engineered signal definitions.

## Explicit Limitations
Not stated as formal limitations; explicit constraints include pseudonymization, removal of OEM references, no published DBC files or reverse-engineered signal definitions, and modified attack payloads.

## Future Work
Not stated.

## Concept Hubs
[[Concept - In-Vehicle Network Security]] [[Concept - Intrusion Detection]] [[Concept - Deep Learning Intrusion Detection]] [[Concept - Network Traffic Analysis]]

## Relevance Score
0.95

## Monitoring Transfer
doi:
not stated
source_link:
not stated
text_kind:
dataset paper
monitoring_problem:
detect malicious CAN and Automotive Ethernet traffic in in-vehicle networks
signal:
raw CAN CC, CAN FD, and Automotive Ethernet message payloads and traces
uncertainty_method:
not stated
action:
train and evaluate intrusion detection models
eval_setting:
258 traces covering 9h07m09s with 397,383,125 CAN and 180,604,377 Automotive Ethernet messages across 10 CAN domains and 6 Ethernet buses
limitation_author:
not stated
limitation_inference:
pseudonymization and modified attack payloads may reduce replay fidelity and payload-specific detection
limitation_unknown:
not stated
support_passage:
It presents both benign traffic as well as advanced attacks launched against the in-vehicle network of a modern commercial electric vehicle from 2020 consisting of 10 internal CAN buses and 6 Automotive Ethernet buses.
transfer_ivn:
Use CarDS to benchmark deep learning intrusion detection for CAN and Automotive Ethernet in IVN
transfer_risk:
Lack of DBC files and modified payloads may limit signal-level interpretation and real-world transfer

#needs-review

## Record Fields
doi: https://doi.org/10.48328/tudatalib-2179
source_link: not stated
text_kind: abstract
monitoring_problem: detect malicious CAN and Automotive Ethernet traffic in in-vehicle networks
signal: raw CAN CC, CAN FD, and Automotive Ethernet message payloads and traces
uncertainty_method: not stated
action: train and evaluate intrusion detection models
eval_setting: 258 traces covering 9h07m09s with 397,383,125 CAN and 180,604,377 Automotive Ethernet messages across 10 CAN domains and 6 Ethernet buses
limitation_author: not stated
limitation_inference: pseudonymization and modified attack payloads may reduce replay fidelity and payload-specific detection
limitation_unknown: not stated
support_passage: It presents both benign traffic as well as advanced attacks launched against the in-vehicle network of a modern commercial electric vehicle from 2020 consisting of 10 internal CAN buses and 6 Automotive Ethernet buses.
transfer_ivn: Use CarDS to benchmark deep learning intrusion detection for CAN and Automotive Ethernet in IVN
transfer_risk: Lack of DBC files and modified payloads may limit signal-level interpretation and real-world transfer
