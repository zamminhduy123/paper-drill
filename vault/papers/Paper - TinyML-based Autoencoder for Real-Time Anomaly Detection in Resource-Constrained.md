---
title: "TinyML-based Autoencoder for Real-Time Anomaly Detection in Resource-Constrained IoT Sensor Streams"
year: 2026
doi: "10.1109/ICSCSS69635.2026.11645876"
relevance_score: 9.0
type: paper
---
# TinyML-based Autoencoder for Real-Time Anomaly Detection in Resource-Constrained IoT Sensor Streams

## Novelty
- 530-parameter fully connected autoencoder for TinyML anomaly detection.
- INT8-quantized model fits in 10–20 KB flash and runs in about 34 ms on ESP32.
- Ten-dimensional input adds orientation-invariant motion magnitude and temporal descriptors.
- Uses the 90th percentile of training reconstruction errors as the anomaly threshold.
- Ablation shows threshold calibration drives most of the F1 improvement over baseline.
- Hardware benchmark compares FC-AE against LSTM-AE, Isolation Forest, and CNN-AE on ESP32.

## Methodology
- Train a lightweight fully connected autoencoder only on normal sensor readings.
- Convert and quantize the model with TensorFlow Lite Micro for INT8 deployment.
- Deploy the model on an ESP32-WROOM-32 microcontroller.
- Construct features from raw sensor channels plus motion magnitude and time-of-day descriptors.
- Compute reconstruction error at inference and compare it against the 90th percentile training threshold.
- Evaluate on a subset of a large IoT dataset with more than 50,000 samples.
- Validate on a physical ESP32 prototype using PIR, MQ-2 gas, and DHT22 sensors.

## Explicit Limitations
- Faults are rare, with less than 0.5% of logging instances being anomalous.
- Labeled fault data is scarce before deployment, making supervised learning impractical.
- ESP32 has limited SRAM, flash, and no hardware floating-point support.
- Reported recall, precision, and F1 are low despite high accuracy.
- Threshold choice is critical and may require recalibration as new normal data arrives.

## Future Work
not stated in provided excerpt

## Concept Hubs
[[Concept - Anomaly Detection]] [[Concept - TinyML Systems]] [[Concept - Resource-Constrained Edge]] [[Concept - Threshold Control]] [[Concept - Class Imbalance]]

## Relevance Score
9/10

## Monitoring Transfer
doi: 10.1109/ICSCSS69635.2026.11645876
source_link: https://doi.org/10.1109/ICSCSS69635.2026.11645876
text_kind: conference paper
monitoring_problem: real-time fault and anomaly detection in resource-constrained IoT sensor streams
signal: autoencoder reconstruction error over ten-dimensional sensor features
uncertainty_method: 90th percentile threshold of training reconstruction errors
action: flag anomalous sensor readings or faults on the ESP32 edge device
eval_setting: subset of a large IoT dataset with more than 50,000 samples and physical ESP32 with PIR, MQ-2, and DHT22 sensors
limitation_author: faults make up less than 0.5% of data, labeled faults are scarce, and ESP32 has limited SRAM, flash, and no hardware floating-point support
limitation_inference: low recall and precision suggest rare anomalies may be under-detected, and the single-board 10-minute test limits field generalization
limitation_unknown: not stated
support_passage: Tests on the anomaly detection algorithm using a portion of a big IoT data set having more than 50 thousand samples revealed the accuracy level to be 96.4%, recall rate as 43.29%, precision 31.56%, and the F1-score value of 36.5%.
transfer_ivn: Deploy the same INT8 autoencoder on in-vehicle ECUs to monitor CAN or vehicle sensor streams and raise anomaly alerts using reconstruction-error percentile thresholds.
transfer_risk: Vehicle networks have stricter safety, latency, and driving-condition variability requirements, so a normal-data percentile threshold may miss rare faults or produce false positives.

#needs-review

## Record Fields
doi: 10.1109/ICSCSS69635.2026.11645876
source_link: https://doi.org/10.1109/ICSCSS69635.2026.11645876
text_kind: fulltext
monitoring_problem: real-time fault and anomaly detection in resource-constrained IoT sensor streams
signal: autoencoder reconstruction error over ten-dimensional sensor features
uncertainty_method: 90th percentile threshold of training reconstruction errors
action: flag anomalous sensor readings or faults on the ESP32 edge device
eval_setting: subset of a large IoT dataset with more than 50,000 samples and physical ESP32 with PIR, MQ-2, and DHT22 sensors
limitation_author: faults make up less than 0.5% of data, labeled faults are scarce, and ESP32 has limited SRAM, flash, and no hardware floating-point support
limitation_inference: low recall and precision suggest rare anomalies may be under-detected, and the single-board 10-minute test limits field generalization
limitation_unknown: not stated
support_passage: Tests on the anomaly detection algorithm using a portion of a big IoT data set having more than 50 thousand samples revealed the accuracy level to be 96.4%, recall rate as 43.29%, precision 31.56%, and the F1-score value of 36.5%.
transfer_ivn: Deploy the same INT8 autoencoder on in-vehicle ECUs to monitor CAN or vehicle sensor streams and raise anomaly alerts using reconstruction-error percentile thresholds.
transfer_risk: Vehicle networks have stricter safety, latency, and driving-condition variability requirements, so a normal-data percentile threshold may miss rare faults or produce false positives.
