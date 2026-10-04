---
title: "A Lightweight Hybrid Convolutional Neural Network–Long Short-Term Memory (CNN–LSTM) and AdaBoost Framework for Edge-Based Internet of Things (IoT) Intrusion Detection"
year: 2026
doi: "https://doi.org/10.7759/s44389-026-00170-3"
relevance_score: 0.95
type: paper
---
# A Lightweight Hybrid Convolutional Neural Network–Long Short-Term Memory (CNN–LSTM) and AdaBoost Framework for Edge-Based Internet of Things (IoT) Intrusion Detection

## Novelty
The study proposes a TinyML-optimized 1D CNN-LSTM and AdaBoost intrusion detection framework for resource-constrained IoT edge gateways. Its novelty combines strict feature reduction using Correlation-Based Elimination and Mutual Information, native class-imbalance handling with Focal Loss, sigmoid calibration to control false positives, and TensorFlow Lite dynamic range quantization for lightweight real-time deployment.

## Methodology
The method uses a merged UNSW-NB15 and RT-IoT2022 dataset with a 70/30 normal-to-attack split. Correlation-Based Elimination and Mutual Information select the top 30 network features. A 1D CNN-LSTM extracts spatiotemporal traffic features, which are passed to an AdaBoost ensemble. Focal Loss addresses class imbalance without synthetic data, sigmoid calibration restricts the False Positive Rate, and the pipeline is compressed with TensorFlow Lite dynamic range quantization. Evaluation is performed in a simulated Docker-based edge gateway processing three continuous CCTV video streams.

## Explicit Limitations
No explicit limitations are stated in the abstract.

## Future Work
Future work is not explicitly stated. Plausible extensions include deployment on physical edge hardware, evaluation on additional IoT traffic datasets, adversarial robustness testing, and transfer to other constrained network domains.

## Concept Hubs
[[Concept - IoT Intrusion Detection]]
[[Concept - Lightweight Detection]]
[[Concept - Feature Selection]]
[[Concept - Class Imbalance]]
[[Concept - Edge AI Inference]]

## Relevance Score
0.95

## Monitoring Transfer
doi:
not stated
source_link:
not stated
text_kind:
abstract
monitoring_problem:
detect IoT network intrusions in real time on a resource-constrained edge gateway
signal:
top 30 selected network features from merged UNSW-NB15 and RT-IoT2022 traffic
uncertainty_method:
sigmoid calibration of ensemble probabilities to restrict false positive rate
action:
raise an intrusion alert when the calibrated probability exceeds the calibrated threshold
eval_setting:
simulated Docker-based edge gateway processing three continuous CCTV video streams with a quantized TensorFlow Lite model using 24 KB memory, 23.8% host CPU, and about 60.16 ms inference latency
limitation_author:
not stated
limitation_inference:
simulated edge gateway and public datasets may not fully capture production IoT traffic diversity, adversarial attacks, or real hardware constraints
limitation_unknown:
not stated
support_passage:
Deployed inside a simulated Docker-based edge gateway processing three continuous CCTV video streams, the quantized model occupied just 24 KB of memory.
transfer_ivn:
transfer the quantized CNN-LSTM AdaBoost detector to in-vehicle network intrusion detection by selecting vehicle bus traffic features and deploying the model on an ECU gateway
transfer_risk:
vehicle networks have stricter latency, safety, and protocol-specific temporal constraints, so IoT traffic features and calibrated thresholds may not generalize

#needs-review

## Record Fields
doi: https://doi.org/10.7759/s44389-026-00170-3
source_link: not stated
text_kind: abstract
monitoring_problem: detect IoT network intrusions in real time on a resource-constrained edge gateway
signal: top 30 selected network features from merged UNSW-NB15 and RT-IoT2022 traffic
uncertainty_method: sigmoid calibration of ensemble probabilities to restrict false positive rate
action: raise an intrusion alert when the calibrated probability exceeds the calibrated threshold
eval_setting: simulated Docker-based edge gateway processing three continuous CCTV video streams with a quantized TensorFlow Lite model using 24 KB memory, 23.8% host CPU, and about 60.16 ms inference latency
limitation_author: not stated
limitation_inference: simulated edge gateway and public datasets may not fully capture production IoT traffic diversity, adversarial attacks, or real hardware constraints
limitation_unknown: not stated
support_passage: Deployed inside a simulated Docker-based edge gateway processing three continuous CCTV video streams, the quantized model occupied just 24 KB of memory.
transfer_ivn: transfer the quantized CNN-LSTM AdaBoost detector to in-vehicle network intrusion detection by selecting vehicle bus traffic features and deploying the model on an ECU gateway
transfer_risk: vehicle networks have stricter latency, safety, and protocol-specific temporal constraints, so IoT traffic features and calibrated thresholds may not generalize
