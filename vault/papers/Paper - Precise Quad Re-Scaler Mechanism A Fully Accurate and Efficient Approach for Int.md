---
title: "Precise Quad Re-Scaler Mechanism: A Fully Accurate and Efficient Approach for Integer-Only Quantized TinyML Inference"
year: 2026
doi: "https://doi.org/10.5281/zenodo.21448826"
relevance_score: 95.0
type: paper
---
# Precise Quad Re-Scaler Mechanism: A Fully Accurate and Efficient Approach for Integer-Only Quantized TinyML Inference

## Novelty
PQRM eliminates integer-only quantization rounding errors in TinyML inference by replacing fixed-point multiplications with grouped shift-add operations from power-of-two decomposition and applying lookup-table rounding correction, achieving exact results with lower latency and memory use.

## Methodology
The authors developed the Ingenuity Inference Engine and benchmarked PQRM against Espressif’s esp-tflite-micro using the MLPerf Tiny autoencoder model on an ESP32-S3 microcontroller.

## Explicit Limitations
not stated

## Future Work
not stated

## Concept Hubs
[[Concept - Edge AI Inference]], [[Concept - TinyML Systems]], [[Concept - Resource-Constrained Edge]], [[Concept - Embedded Systems]]

## Relevance Score
95

## Monitoring Transfer
doi: not stated
source_link: not stated
text_kind: abstract
monitoring_problem: monitoring accuracy and latency of quantized TinyML inference on resource-constrained microcontrollers
signal: integer-only quantized model outputs and execution metrics
uncertainty_method: not stated
action: apply PQRM shift-add operations and lookup-table rounding correction
eval_setting: MLPerf Tiny autoencoder on ESP32-S3 benchmarked against esp-tflite-micro
limitation_author: not stated
limitation_inference: evaluation is limited to one autoencoder model and one microcontroller platform
limitation_unknown: not stated
support_passage: The results demonstrate a 1.67× reduction in latency, a 35× smaller memory footprint, and 100% accuracy
transfer_ivn: use PQRM integer-only TinyML inference on in-vehicle microcontrollers for lightweight CAN FD anomaly detection
transfer_risk: IVN detection may need higher precision, larger models, or safety certification beyond integer-only microcontroller inference

#needs-review

## Record Fields
doi: https://doi.org/10.5281/zenodo.21448826
source_link: not stated
text_kind: abstract
monitoring_problem: monitoring accuracy and latency of quantized TinyML inference on resource-constrained microcontrollers
signal: integer-only quantized model outputs and execution metrics
uncertainty_method: not stated
action: apply PQRM shift-add operations and lookup-table rounding correction
eval_setting: MLPerf Tiny autoencoder on ESP32-S3 benchmarked against esp-tflite-micro
limitation_author: not stated
limitation_inference: evaluation is limited to one autoencoder model and one microcontroller platform
limitation_unknown: not stated
support_passage: The results demonstrate a 1.67× reduction in latency, a 35× smaller memory footprint, and 100% accuracy
transfer_ivn: use PQRM integer-only TinyML inference on in-vehicle microcontrollers for lightweight CAN FD anomaly detection
transfer_risk: IVN detection may need higher precision, larger models, or safety certification beyond integer-only microcontroller inference
