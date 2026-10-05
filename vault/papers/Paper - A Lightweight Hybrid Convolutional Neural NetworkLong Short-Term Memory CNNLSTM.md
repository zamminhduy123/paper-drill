---
title: "A Lightweight Hybrid Convolutional Neural Network–Long Short-Term Memory (CNN–LSTM) and AdaBoost Framework for Edge-Based Internet of Things (IoT) Intrusion Detection"
year: 2026
doi: "https://doi.org/10.7759/s44389-026-00170-3"
relevance_score: 0.92
type: paper
---
# A Lightweight Hybrid Convolutional Neural Network–Long Short-Term Memory (CNN–LSTM) and AdaBoost Framework for Edge-Based Internet of Things (IoT) Intrusion Detection

## Novelty
TinyML-optimized CNN-LSTM with AdaBoost, focal loss, feature reduction, sigmoid calibration, and TensorFlow Lite quantization for resource-constrained edge IoT intrusion detection.

## Methodology
Merged UNSW-NB15 and RT-IoT2022 with a 70/30 normal-to-attack split; Correlation-Based Elimination and Mutual Information selected the top 30 features; CNN-LSTM extracted spatiotemporal features; AdaBoost ensembled the outputs; focal loss addressed imbalance; sigmoid calibration controlled false positives; TensorFlow Lite dynamic range quantization compressed the model; deployment used a simulated Docker edge gateway with three CCTV streams.

## Explicit Limitations
Author-stated: not stated  
Inferred: evaluation relies on a simulated Docker-based edge gateway and merged public datasets, so real edge hardware behavior and live deployment effects are not fully validated.  
Unknown: not stated

## Future Work
not stated

## Concept Hubs
[[Concept - Edge AI Inference]] [[Concept - IoT Intrusion Detection]] [[Concept - Lightweight Detection]] [[Concept - Feature Selection]] [[Concept - Class Imbalance]]

## Relevance Score
0.92

## Monitoring Transfer
doi: not stated
source_link: not stated
text_kind: abstract
monitoring_problem: detect IoT network intrusions on a resource-constrained edge gateway
signal: 30 selected network traffic features processed by a CNN-LSTM detector
uncertainty_method: sigmoid calibration of classifier outputs to restrict false positive rate
action: flag intrusion when calibrated probability exceeds threshold
eval_setting: simulated Docker-based edge gateway processing three continuous CCTV video streams with 24 KB memory, 23.8% CPU, and ~60.16 ms latency
limitation_author: not stated
limitation_inference: simulated Docker-based edge gateway and merged public datasets may not capture real edge hardware constraints, live traffic dynamics, or IVN domain shift
limitation_unknown: not stated
support_passage: Deployed inside a simulated Docker-based edge gateway processing three continuous CCTV video streams
transfer_ivn: adapt the quantized CNN-LSTM-AdaBoost detector to in-vehicle network intrusion detection by replacing IoT features with selected CAN or IVN message features and deploying it on a vehicle edge node
transfer_risk: IVN traffic has stricter real-time, safety-critical, and protocol-specific constraints than the IoT datasets used, so calibrated false positive behavior and latency may not transfer reliably

#needs-review

## Record Fields
doi: https://doi.org/10.7759/s44389-026-00170-3
source_link: not stated
text_kind: abstract
monitoring_problem: detect IoT network intrusions on a resource-constrained edge gateway
signal: 30 selected network traffic features processed by a CNN-LSTM detector
uncertainty_method: sigmoid calibration of classifier outputs to restrict false positive rate
action: flag intrusion when calibrated probability exceeds threshold
eval_setting: simulated Docker-based edge gateway processing three continuous CCTV video streams with 24 KB memory, 23.8% CPU, and ~60.16 ms latency
limitation_author: not stated
limitation_inference: simulated Docker-based edge gateway and merged public datasets may not capture real edge hardware constraints, live traffic dynamics, or IVN domain shift
limitation_unknown: not stated
support_passage: Deployed inside a simulated Docker-based edge gateway processing three continuous CCTV video streams
transfer_ivn: adapt the quantized CNN-LSTM-AdaBoost detector to in-vehicle network intrusion detection by replacing IoT features with selected CAN or IVN message features and deploying it on a vehicle edge node
transfer_risk: IVN traffic has stricter real-time, safety-critical, and protocol-specific constraints than the IoT datasets used, so calibrated false positive behavior and latency may not transfer reliably
