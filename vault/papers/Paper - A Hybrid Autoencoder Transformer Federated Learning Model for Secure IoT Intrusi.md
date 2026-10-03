---
title: "A Hybrid Autoencoder Transformer Federated Learning Model for Secure IoT Intrusion Detection"
year: 2026
doi: "https://doi.org/10.70917/ijcisim-2026-4096"
relevance_score: 0.93
type: paper
---
# A Hybrid Autoencoder Transformer Federated Learning Model for Secure IoT Intrusion Detection

## Novelty
Proposes a hybrid Autoencoder–Transformer federated learning intrusion detection system for IoT networks, combining latent feature extraction, spatio-temporal traffic modeling, FedProx optimization, and differential privacy.

## Methodology
An Autoencoder extracts latent traffic features, a Transformer captures spatio-temporal traffic patterns, and the hybrid model is trained jointly in a privacy-preserving federated learning framework using FedProx and differential privacy. Evaluation is performed on the ToN-IoT-IDS dataset for the CECIC task.

## Explicit Limitations
not stated

## Future Work
not stated

## Concept Hubs
[[Concept - IoT Intrusion Detection]]
[[Concept - Privacy-Preserving Learning]]
[[Concept - Deep Learning Intrusion Detection]]
[[Concept - Network Traffic Analysis]]

## Relevance Score
0.93

## Monitoring Transfer
doi:
not stated
source_link:
not stated
text_kind:
abstract
monitoring_problem:
secure IoT intrusion detection under distributed heterogeneous devices with privacy constraints
signal:
latent Autoencoder features and spatio-temporal network traffic patterns
uncertainty_method:
not stated
action:
classify network traffic as normal or malicious and update federated local models
eval_setting:
ToN-IoT-IDS CECIC task with accuracy, macro-F1, and ROC-AUC
limitation_author:
not stated
limitation_inference:
No explicit model limitations are stated; inferred gaps include communication overhead, differential privacy utility tradeoff, and real-time edge feasibility.
limitation_unknown:
not stated
support_passage:
The Autoencoder is responsible for latent features extraction, meanwhile the Transformer captures spatio-temporal traffic patterns and trained jointly in a privacy-preserving federated learning framework with FedProx optimization and differential privacy.
transfer_ivn:
Use local Autoencoder–Transformer models on vehicle ECUs with federated aggregation to detect in-vehicle network intrusions.
transfer_risk:
IVN traffic has automotive protocol semantics, strict real-time constraints, and vehicle-specific distributions that may not match IoT traffic.

#needs-review

## Record Fields
doi: https://doi.org/10.70917/ijcisim-2026-4096
source_link: not stated
text_kind: abstract
monitoring_problem: secure IoT intrusion detection under distributed heterogeneous devices with privacy constraints
signal: latent Autoencoder features and spatio-temporal network traffic patterns
uncertainty_method: not stated
action: classify network traffic as normal or malicious and update federated local models
eval_setting: ToN-IoT-IDS CECIC task with accuracy, macro-F1, and ROC-AUC
limitation_author: not stated
limitation_inference: No explicit model limitations are stated; inferred gaps include communication overhead, differential privacy utility tradeoff, and real-time edge feasibility.
limitation_unknown: not stated
support_passage: The Autoencoder is responsible for latent features extraction, meanwhile the Transformer captures spatio-temporal traffic patterns and trained jointly in a privacy-preserving federated learning framework with FedProx optimization and differential privacy.
transfer_ivn: Use local Autoencoder–Transformer models on vehicle ECUs with federated aggregation to detect in-vehicle network intrusions.
transfer_risk: IVN traffic has automotive protocol semantics, strict real-time constraints, and vehicle-specific distributions that may not match IoT traffic.
