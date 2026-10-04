---
title: "Acquisition and processing of vehicle dynamics data for predictive modeling"
year: 2026
doi: "https://doi.org/10.1080/21642583.2026.2634457"
relevance_score: 5.0
type: paper
---
# Acquisition and processing of vehicle dynamics data for predictive modeling

## Novelty
Modular low-latency vehicle dynamics data acquisition and analytics platform integrating a front-right suspension prototype, STM32 CAN-FD microcontrollers, custom analog front-end circuits, Raspberry Pi telemetry dashboard, and AI-driven analytics.

## Methodology
Sensors for displacement, steering angle, damper velocity, and temperature stream via CAN-FD to STM32 microcontrollers and a Raspberry Pi. Data are visualized with Plotly-Dash and logged in InfluxDB. Rule-based methods and Gaussian mixture models analyze damper behavior, classify damping regimes, and estimate tire thermal state from wheel speed, accelerometer, and temperature data. Validation is performed on a custom mechanical test rig.

## Explicit Limitations
not stated

## Future Work
not stated

## Concept Hubs
[[Concept - Embedded Systems]]
[[Concept - Multi-Sensor Fusion]]
[[Concept - Real-Time Telemetry]]
[[Concept - Edge AI Inference]]

## Relevance Score
5/10

## Monitoring Transfer
doi: not stated
source_link: not stated
text_kind: abstract
monitoring_problem: damper behavior and tire thermal state monitoring
signal: displacement, steering angle, damper velocity, temperature, wheel speed, accelerometer
uncertainty_method: Gaussian mixture model
action: classify damping regimes and estimate tire thermal state
eval_setting: custom mechanical test rig
limitation_author: not stated
limitation_inference: front-right suspension prototype and test rig only
limitation_unknown: not stated
support_passage: Rule based and gaussian mixture models analyze damper behavior, classify damping regimes, and estimate tire thermal state using wheel speed, accelerometer, and temperature data
transfer_ivn: Monitor damper and tire thermal anomalies from CAN-FD vehicle dynamics signals in an in-vehicle network
transfer_risk: Test-rig suspension data may not generalize to full-vehicle network conditions and network faults

#needs-review

## Record Fields
doi: https://doi.org/10.1080/21642583.2026.2634457
source_link: not stated
text_kind: abstract
monitoring_problem: damper behavior and tire thermal state monitoring
signal: displacement, steering angle, damper velocity, temperature, wheel speed, accelerometer
uncertainty_method: Gaussian mixture model
action: classify damping regimes and estimate tire thermal state
eval_setting: custom mechanical test rig
limitation_author: not stated
limitation_inference: front-right suspension prototype and test rig only
limitation_unknown: not stated
support_passage: Rule based and gaussian mixture models analyze damper behavior, classify damping regimes, and estimate tire thermal state using wheel speed, accelerometer, and temperature data
transfer_ivn: Monitor damper and tire thermal anomalies from CAN-FD vehicle dynamics signals in an in-vehicle network
transfer_risk: Test-rig suspension data may not generalize to full-vehicle network conditions and network faults
