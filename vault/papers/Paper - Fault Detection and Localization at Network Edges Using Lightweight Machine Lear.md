---
title: "Fault Detection and Localization at Network Edges Using Lightweight Machine Learning Models"
year: 2026
doi: "https://doi.org/10.1201/9781003771654-9"
relevance_score: 4.955
type: paper
---
# Fault Detection and Localization at Network Edges Using Lightweight Machine Learning Models

Novelty

* Compressed latent space representation optimized specifically for low-resource inference in optical network fault detection.

* Adaptive quantization mechanism that dynamically reduces processing overhead without compromising accuracy.

* Integration of variational autoencoders with TinyML for real-time fault management under strict computational and energy constraints.

Methodology

* Variational autoencoder (VAE) based framework deployed for fault detection and localization.

* TinyML paradigm applied to embed models on ultra-constrained edge devices.

* Compressed latent space designed for efficient low-resource inference.

* Adaptive quantization mechanism for dynamic processing overhead reduction.

* Experimental evaluation comparing detection speed, localization precision, and energy efficiency against conventional centralized architectures.

Explicit Limitations

Not stated.

Future Work

* Broader adoption of intelligent, edge-native solutions across diverse industrial and communication domains.

* Moving toward decentralized and scalable optical network management.

Concept Hubs

[[Concept - Edge AI Inference]]
[[Concept - TinyML Systems]]
[[Concept - Resource-Constrained Edge]]
[[Concept - Lightweight Detection]]

Relevance Score

Not stated.

Monitoring Transfer

Monitoring problem: Real-time fault detection and localization in optical networks under strict computational and energy constraints at the edge.
Signal: Optical network telemetry data compressed into a VAE latent space representation.
Uncertainty method: Variational autoencoder latent space encoding (probabilistic latent representation).
Resulting action: Immediate fault detection and localization at network edges.
Evaluation setting: Experimental evaluation comparing detection speed, localization precision, and energy efficiency against conventional centralized architectures.

Transfer to IVN: Lightweight VAE + TinyML fault detection could be embedded in in-vehicle edge devices (e.g., zonal controllers, gateways) for real-time fault detection and localization on CAN/CAN FD/Ethernet backbones under tight compute and energy budgets.
Transfer risk: Optical network fault signatures (e.g., signal power degradation, BER) differ fundamentally from in-vehicle network fault modes (e.g., bus-off, frame loss, EMI-induced bit errors), so the learned latent space may not capture IVN-specific fault dynamics without retraining or domain adaptation.

doi: not stated
source_link: not stated
text_kind: abstract
monitoring_problem: real-time fault detection and localization in optical networks under strict computational and energy constraints
signal: optical network telemetry encoded via variational autoencoder latent space
uncertainty_method: variational autoencoder latent space representation
action: immediate fault detection and localization at network edges
eval_setting: experimental comparison against conventional centralized architectures on detection speed, localization precision, and energy efficiency
limitation_author: not stated
limitation_inference: evaluation limited to optical network domain; generalizability to other network types (e.g., in-vehicle, industrial IoT) not demonstrated; no discussion of fault type coverage or dataset diversity
limitation_unknown: whether evaluation used real-world deployments or simulations; specific hardware platforms used; dataset characteristics; latency and energy figures
support_passage: This study introduces a novel, resource-efficient framework for immediate fault detection and localization in optical networks, leveraging lightweight machine learning models tailored for edge computing environments.
transfer_ivn: Lightweight VAE + TinyML models can be embedded in in-vehicle edge devices for real-time fault detection and localization on CAN/CAN FD/Ethernet backbones under tight compute and energy budgets.
transfer_risk: Optical network fault signatures differ fundamentally from in-vehicle network fault modes, so the learned latent space may not capture IVN-specific fault dynamics without retraining or domain adaptation.

Compressed latent space representation optimized specifically for low-resource inference in optical network fault detection.

Adaptive quantization mechanism that dynamically reduces processing overhead without compromising accuracy.

Integration of variational autoencoders with TinyML for real-time fault management under strict computational and energy constraints.

Variational autoencoder (VAE) based framework deployed for fault detection and localization.

TinyML paradigm applied to embed models on ultra-constrained edge devices.

Compressed latent space designed for efficient low-resource inference.

Adaptive quantization mechanism for dynamic processing overhead reduction.

Experimental evaluation comparing detection speed, localization precision, and energy efficiency against conventional centralized architectures.

Not stated.

Broader adoption of intelligent, edge-native solutions across diverse industrial and communication domains.

Moving toward decentralized and scalable optical network management.

[[Concept - Edge AI Inference]]
[[Concept - TinyML Systems]]
[[Concept - Resource-Constrained Edge]]
[[Concept - Lightweight Detection]]

Not stated.

Monitoring problem: Real-time fault detection and localization in optical networks under strict computational and energy constraints at the edge.
Signal: Optical network telemetry data compressed into a VAE latent space representation.
Uncertainty method: Variational autoencoder latent space encoding (probabilistic latent representation).
Resulting action: Immediate fault detection and localization at network edges.
Evaluation setting: Experimental evaluation comparing detection speed, localization precision, and energy efficiency against conventional centralized architectures.

Transfer to IVN: Lightweight VAE + TinyML fault detection could be embedded in in-vehicle edge devices (e.g., zonal controllers, gateways) for real-time fault detection and localization on CAN/CAN FD/Ethernet backbones under tight compute and energy budgets.
Transfer risk: Optical network fault signatures (e.g., signal power degradation, BER) differ fundamentally from in-vehicle network fault modes (e.g., bus-off, frame loss, EMI-induced bit errors), so the learned latent space may not capture IVN-specific fault dynamics without retraining or domain adaptation.

doi: not stated
source_link: not stated
text_kind: abstract
monitoring_problem: real-time fault detection and localization in optical networks under strict computational and energy constraints
signal: optical network telemetry encoded via variational autoencoder latent space
uncertainty_method: variational autoencoder latent space representation
action: immediate fault detection and localization at network edges
eval_setting: experimental comparison against conventional centralized architectures on detection speed, localization precision, and energy efficiency
limitation_author: not stated
limitation_inference: evaluation limited to optical network domain; generalizability to other network types (e.g., in-vehicle, industrial IoT) not demonstrated; no discussion of fault type coverage or dataset diversity
limitation_unknown: whether evaluation used real-world deployments or simulations; specific hardware platforms used; dataset characteristics; latency and energy figures
support_passage: This study introduces a novel, resource-efficient framework for immediate fault detection and localization in optical networks, leveraging lightweight machine learning models tailored for edge computing environments.
transfer_ivn: Lightweight VAE + TinyML models can be embedded in in-vehicle edge devices for real-time fault detection and localization on CAN/CAN FD/Ethernet backbones under tight compute and energy budgets.
transfer_risk: Optical network fault signatures differ fundamentally from in-vehicle network fault modes, so the learned latent space may not capture IVN-specific fault dynamics without retraining or domain adaptation.

#needs-review

## Record Fields
doi: https://doi.org/10.1201/9781003771654-9
source_link: not stated
text_kind: abstract
monitoring_problem: Real-time fault detection and localization in optical networks under strict computational and energy constraints at the edge.
signal: Optical network telemetry data compressed into a VAE latent space representation.
uncertainty_method: Variational autoencoder latent space encoding (probabilistic latent representation).
action: immediate fault detection and localization at network edges
eval_setting: experimental comparison against conventional centralized architectures on detection speed, localization precision, and energy efficiency
limitation_author: not stated
limitation_inference: evaluation limited to optical network domain; generalizability to other network types (e.g., in-vehicle, industrial IoT) not demonstrated; no discussion of fault type coverage or dataset diversity
limitation_unknown: whether evaluation used real-world deployments or simulations; specific hardware platforms used; dataset characteristics; latency and energy figures
support_passage: This study introduces a novel, resource-efficient framework for immediate fault detection and localization in optical networks, leveraging lightweight machine learning models tailored for edge computing environments.
transfer_ivn: Lightweight VAE + TinyML models can be embedded in in-vehicle edge devices for real-time fault detection and localization on CAN/CAN FD/Ethernet backbones under tight compute and energy budgets.
transfer_risk: Optical network fault signatures (e.g., signal power degradation, BER) differ fundamentally from in-vehicle network fault modes (e.g., bus-off, frame loss, EMI-induced bit errors), so the learned latent space may not capture IVN-specific fault dynamics without retraining or domain adaptation.
