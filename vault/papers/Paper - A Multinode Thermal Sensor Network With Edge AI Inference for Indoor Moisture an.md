---
title: "A Multinode Thermal Sensor Network With Edge AI Inference for Indoor Moisture and Humidity Classification"
year: 2026
doi: "10.1109/JSEN.2026.3719511"
relevance_score: 9.0
type: paper
---
# A Multinode Thermal Sensor Network With Edge AI Inference for Indoor Moisture and Humidity Classification

## Novelty
The paper introduces a distributed indoor thermal sensing system with cloud-edge collaborative training and a lightweight CNN for 22-class moisture/humidity classification, achieving 98.91% test accuracy with a 2.6-MB model, 0.542 GFLOPs, and 273-314 ms edge inference on Raspberry Pi 4B and Rock Pi C+.

## Methodology
Multiple FLIR Lepton 3.5 thermal sensors are connected to Raspberry Pi 4B nodes for data acquisition and wireless upload to a GPU cloud server. The authors curate the THERMID dataset with 22 indoor moisture, cold-spot, condensation, and temperature-state classes, train a lightweight CNN centrally, and deploy the model on Rock Pi C+ edge devices for on-device inference.

## Explicit Limitations
Author-stated limitations are not provided in the excerpt. Inferred limitations include 273-314 ms per-image inference latency, dependence on cloud connectivity for centralized training, lack of uncertainty quantification, and evaluation limited to two edge platforms and indoor thermal classes.

## Future Work
not stated

## Concept Hubs
[[Concept - Edge AI Inference]]
[[Concept - Resource-Constrained Edge]]
[[Concept - Lightweight Detection]]
[[Concept - Multi-Sensor Fusion]]
[[Concept - TinyML Systems]]

## Relevance Score
9/10

## Monitoring Transfer
doi: 10.1109/JSEN.2026.3719511
source_link: not stated
text_kind: journal article
monitoring_problem: indoor moisture and humidity classification for building health monitoring
signal: radiometric thermal images from FLIR Lepton 3.5 sensors
uncertainty_method: not stated
action: deploy a lightweight CNN on edge devices for low-latency on-device inference and smart home control integration
eval_setting: THERMID dataset with 22 classes, evaluated on Raspberry Pi 4B and Rock Pi C+ with 98.91% test accuracy and 273-314 ms inference latency
limitation_author: not stated
limitation_inference: 273-314 ms inference latency may limit high-frequency monitoring, cloud training requires connectivity, and no uncertainty quantification is reported
limitation_unknown: not stated
support_passage: The proposed lightweight DL model outperforms existing state-of-the-art pretrained models, providing 98.91% test accuracy with only a 2.6-MB model size and requiring only 0.542 GFLOPs for inference.
transfer_ivn: transfer lightweight edge CNN inference to in-vehicle network monitoring by deploying compact models on vehicle ECUs or edge gateways to classify network anomalies or component states
transfer_risk: the indoor thermal dataset and edge hardware do not capture vehicle network traffic dynamics, safety-critical latency requirements, or in-vehicle compute constraints, so accuracy and latency may not transfer

#needs-review

## Record Fields
doi: 10.1109/JSEN.2026.3719511
source_link: not stated
text_kind: fulltext
monitoring_problem: indoor moisture and humidity classification for building health monitoring
signal: radiometric thermal images from FLIR Lepton 3.5 sensors
uncertainty_method: not stated
action: deploy a lightweight CNN on edge devices for low-latency on-device inference and smart home control integration
eval_setting: THERMID dataset with 22 classes, evaluated on Raspberry Pi 4B and Rock Pi C+ with 98.91% test accuracy and 273-314 ms inference latency
limitation_author: not stated
limitation_inference: 273-314 ms inference latency may limit high-frequency monitoring, cloud training requires connectivity, and no uncertainty quantification is reported
limitation_unknown: not stated
support_passage: The proposed lightweight DL model outperforms existing state-of-the-art pretrained models, providing 98.91% test accuracy with only a 2.6-MB model size and requiring only 0.542 GFLOPs for inference.
transfer_ivn: transfer lightweight edge CNN inference to in-vehicle network monitoring by deploying compact models on vehicle ECUs or edge gateways to classify network anomalies or component states
transfer_risk: the indoor thermal dataset and edge hardware do not capture vehicle network traffic dynamics, safety-critical latency requirements, or in-vehicle compute constraints, so accuracy and latency may not transfer
