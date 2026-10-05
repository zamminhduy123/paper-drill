---
title: "Windows Local Model Accelerator (WLMA): A Strategic Architecture for OS-Level Edge AI Inference Orchestration"
year: 2026
doi: "https://doi.org/10.5281/zenodo.21429041"
relevance_score: 9.0
type: paper
---
# Windows Local Model Accelerator (WLMA): A Strategic Architecture for OS-Level Edge AI Inference Orchestration

## Novelty
Proposes a Windows OS-level local model accelerator for on-device 4–8B LLM inference, combining a 6-layer orchestration architecture with an RL-MOTS Deep Q-Network scheduler that balances token throughput against thermal, battery, and KV-cache memory constraints.

## Methodology
Engineering specification and strategic case study that analyzes Windows ML, DirectML, and ONNX Runtime, then designs an OS-level inference orchestration layer. The core method is a mathematical RL-MOTS scheduling agent that uses live system metrics to distribute multi-application inference workloads across CPU, GPU, and NPU accelerators.

## Explicit Limitations
Hardware driver fragmentation is identified as a major risk. The proposal also notes that Windows currently lacks a kernel-coordinated scheduling engine for dynamic multi-accelerator inference distribution. No empirical validation, benchmark results, or quantitative performance evaluation are provided.

## Future Work
Implement and benchmark a prototype across Qualcomm, Intel, and AMD NPU platforms. Extend evaluation to driver fragmentation, thermal throttling, battery-saver modes, and integration with Microsoft Project Solara and Aion 1.0 models.

## Concept Hubs
[[Concept - Edge AI Inference]]
[[Concept - Resource-Constrained Edge]]
[[Concept - Energy-Aware Inference]]
[[Concept - Thermal Signal Integrity]]
[[Concept - Fine-Grained Power Management]]

## Relevance Score
9

## Monitoring Transfer
doi: not stated
source_link: not stated
text_kind: abstract
monitoring_problem: Dynamic OS-level scheduling of concurrent on-device LLM inference under thermal, power, and memory constraints
signal: Junction temperature, TDP, KV-cache memory pressure, token throughput, and battery-saver state
uncertainty_method: not stated
action: A kernel-coordinated RL-MOTS scheduler allocates inference workloads across CPU, GPU, and NPU accelerators
eval_setting: not stated
limitation_author: hardware driver fragmentation
limitation_inference: no empirical evaluation or benchmark results are provided
limitation_unknown: not stated
support_passage: it replaces standard static scheduling heuristics with an advanced, mathematical RL-MOTS algorithm (a Deep Q-Network reinforcement learning agent) designed to balance token throughput targets against real-time thermal limits and battery-saver constraints
transfer_ivn: Apply the same RL scheduling idea to in-vehicle network security monitoring by allocating intrusion-detection models across vehicle ECUs using CPU load, thermal state, and anomaly-score signals, evaluated on in-vehicle network traces
transfer_risk: Vehicle safety-critical latency and heterogeneous ECU constraints may make learned scheduling unsafe or infeasible

#needs-review

## Record Fields
doi: https://doi.org/10.5281/zenodo.21429041
source_link: not stated
text_kind: abstract
monitoring_problem: Dynamic OS-level scheduling of concurrent on-device LLM inference under thermal, power, and memory constraints
signal: Junction temperature, TDP, KV-cache memory pressure, token throughput, and battery-saver state
uncertainty_method: not stated
action: A kernel-coordinated RL-MOTS scheduler allocates inference workloads across CPU, GPU, and NPU accelerators
eval_setting: not stated
limitation_author: hardware driver fragmentation
limitation_inference: no empirical evaluation or benchmark results are provided
limitation_unknown: not stated
support_passage: it replaces standard static scheduling heuristics with an advanced, mathematical RL-MOTS algorithm (a Deep Q-Network reinforcement learning agent) designed to balance token throughput targets against real-time thermal limits and battery-saver constraints
transfer_ivn: Apply the same RL scheduling idea to in-vehicle network security monitoring by allocating intrusion-detection models across vehicle ECUs using CPU load, thermal state, and anomaly-score signals, evaluated on in-vehicle network traces
transfer_risk: Vehicle safety-critical latency and heterogeneous ECU constraints may make learned scheduling unsafe or infeasible
