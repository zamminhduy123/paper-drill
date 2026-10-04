---
title: "DCANFL: Decentralized Federated Learning for In-Vehicle CAN Intrusion Detection"
year: 2026
doi: "10.1109/TVT.2026.3671351"
relevance_score: 0.95
type: paper
---
# DCANFL: Decentralized Federated Learning for In-Vehicle CAN Intrusion Detection

## Novelty
DCANFL is a decentralized federated learning framework for in-vehicle CAN intrusion detection that removes the central FL server, uses gossip-based dissimilarity-driven node pairing for model exchange, and integrates continual learning to reduce performance degradation in decentralized training.

## Methodology
Each vehicle acts as a local FL client with a private CAN dataset. Raw CAN frames are deserialized using DBC files into semantic signal values, and a local autoencoder is trained unsupervised to reconstruct normal signals. Reconstruction error is used as the anomaly score. Vehicles form dynamic gossip clusters over V2V links, exchange models with dissimilar peers, and use a continual learning training pipeline to stabilize convergence and maintain detection accuracy.

## Explicit Limitations
Not stated for DCANFL in the provided excerpt. The paper notes that centralized FL raises privacy and deployment concerns, while conventional decentralized FL can suffer performance degradation and unstable convergence.

## Future Work
Not stated.

## Concept Hubs
[[Concept - CAN Intrusion Detection]]
[[Concept - Privacy-Preserving Learning]]
[[Concept - Continual Learning]]
[[Concept - Unsupervised Intrusion Detection]]

## Relevance Score
0.95

## Monitoring Transfer
doi: 10.1109/TVT.2026.3671351
source_link: not stated
text_kind: journal article
monitoring_problem: in-vehicle CAN bus intrusion detection
signal: DBC-decoded CAN signal reconstruction error
uncertainty_method: reconstruction error threshold
action: flag anomalous CAN frames
eval_setting: two in-vehicle CAN datasets with FedAvg and decentralized FL baselines
limitation_author: not stated
limitation_inference: depends on V2V gossip connectivity, dynamic clustering, model dissimilarity estimation, and anomaly threshold calibration
limitation_unknown: not stated
support_passage: DCANFL uses gossip-based, dissimilarity-driven pairing for efficient model exchange and a continual learning training pipeline to improve performance and maintain high accuracy across diverse attack types.
transfer_ivn: extend gossip-based decentralized federated learning to other in-vehicle networks such as automotive Ethernet or FlexRay
transfer_risk: CAN-specific signal semantics, DBC decoding, and V2V mobility assumptions may not transfer directly to other IVN protocols.

#needs-review

## Record Fields
doi: 10.1109/TVT.2026.3671351
source_link: not stated
text_kind: fulltext
monitoring_problem: in-vehicle CAN bus intrusion detection
signal: DBC-decoded CAN signal reconstruction error
uncertainty_method: reconstruction error threshold
action: flag anomalous CAN frames
eval_setting: two in-vehicle CAN datasets with FedAvg and decentralized FL baselines
limitation_author: not stated
limitation_inference: depends on V2V gossip connectivity, dynamic clustering, model dissimilarity estimation, and anomaly threshold calibration
limitation_unknown: not stated
support_passage: DCANFL uses gossip-based, dissimilarity-driven pairing for efficient model exchange and a continual learning training pipeline to improve performance and maintain high accuracy across diverse attack types.
transfer_ivn: extend gossip-based decentralized federated learning to other in-vehicle networks such as automotive Ethernet or FlexRay
transfer_risk: CAN-specific signal semantics, DBC decoding, and V2V mobility assumptions may not transfer directly to other IVN protocols.
