---
title: "A Low-Power Pipelined IEEE 754 Floating-Point Datapath for Energy-Efficient Neural Network Acceleration"
year: 2026
doi: "10.1109/ICCMC69250.2026.11624775"
relevance_score: 8.0
type: paper
---
# A Low-Power Pipelined IEEE 754 Floating-Point Datapath for Energy-Efficient Neural Network Acceleration

## Novelty
A low-power, pipelined IEEE 754 single-precision floating-point datapath for neural network accelerators that jointly targets latency, energy, throughput, and numerical accuracy for resource-constrained edge AI inference.

## Methodology
The paper designs a 32-bit IEEE 754 floating-point datapath with multi-stage pipelined addition, multiplication, and accumulation units. It applies operand isolation and clock-aware pipeline staging to reduce critical-path delay and switching activity, then evaluates the design using post-synthesis simulations against non-pipelined floating-point implementations.

## Explicit Limitations
No explicit limitations section is provided. Inferred limitations include reliance on post-synthesis simulation only, limited reported end-to-end neural network accuracy validation, and no physical hardware or automotive safety validation.

## Future Work
Adapt the scalable and modular datapath to other neural network designs and resource-constrained edge AI systems requiring high-performance, low-energy inference.

## Concept Hubs
[[Concept - Edge AI Inference]]
[[Concept - Energy-Aware Inference]]
[[Concept - Resource-Constrained Edge]]
[[Concept - Embedded Systems]]

## Relevance Score
8

## Monitoring Transfer
doi:
10.1109/ICCMC69250.2026.11624775
source_link:
not stated
text_kind:
conference paper
monitoring_problem:
energy, latency, and throughput of edge AI neural network inference
signal:
propagation delay, dynamic power, throughput, numerical accuracy
uncertainty_method:
not stated
action:
use a pipelined IEEE 754 floating-point datapath for real-time low-power inference
eval_setting:
post-synthesis simulation on resource-constrained edge and embedded AI platforms
limitation_author:
not stated
limitation_inference:
no physical hardware validation and no end-to-end neural network accuracy benchmark are reported
limitation_unknown:
not stated
support_passage:
Simulations after synthesis show that the proposed data path has significant propagation delay and dynamic power improvements over the state-of-the-art non-pipelined floating-point implementations.
transfer_ivn:
Deploy the pipelined low-power IEEE 754 datapath in in-vehicle network edge AI nodes for real-time inference under power and latency constraints.
transfer_risk:
In-vehicle network safety and deterministic timing requirements may reject floating-point datapaths due to power, area, voltage-scaling timing errors, and lack of fault tolerance.

#needs-review

## Record Fields
doi: 10.1109/ICCMC69250.2026.11624775
source_link: not stated
text_kind: fulltext
monitoring_problem: energy, latency, and throughput of edge AI neural network inference
signal: propagation delay, dynamic power, throughput, numerical accuracy
uncertainty_method: not stated
action: use a pipelined IEEE 754 floating-point datapath for real-time low-power inference
eval_setting: post-synthesis simulation on resource-constrained edge and embedded AI platforms
limitation_author: not stated
limitation_inference: no physical hardware validation and no end-to-end neural network accuracy benchmark are reported
limitation_unknown: not stated
support_passage: Simulations after synthesis show that the proposed data path has significant propagation delay and dynamic power improvements over the state-of-the-art non-pipelined floating-point implementations.
transfer_ivn: Deploy the pipelined low-power IEEE 754 datapath in in-vehicle network edge AI nodes for real-time inference under power and latency constraints.
transfer_risk: In-vehicle network safety and deterministic timing requirements may reject floating-point datapaths due to power, area, voltage-scaling timing errors, and lack of fault tolerance.
