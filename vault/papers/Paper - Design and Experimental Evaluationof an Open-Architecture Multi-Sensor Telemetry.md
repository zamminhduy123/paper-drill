---
title: "Design and Experimental Evaluationof an Open-Architecture Multi-Sensor Telemetry System for Real-Time Motorcycle Dynamics Acquisition"
year: 2026
doi: "https://doi.org/10.3390/electronics15122604"
relevance_score: 5.0
type: paper
---
# Design and Experimental Evaluationof an Open-Architecture Multi-Sensor Telemetry System for Real-Time Motorcycle Dynamics Acquisition

Novelty

An open-architecture, dual-core (STM32H745) motorcycle telemetry unit integrating RTK-GNSS, a 9-DoF IMU with on-chip fusion, CAN-FD powertrain acquisition, and 4G/LTE streaming in a single extensible platform at ~EUR 265 BOM. The work is explicit about the epistemic status of each claim: CAN-FD acquisition and end-to-end reliability are empirically validated, while positioning accuracy, fusion latency, uplink reliability, and thermal margins rest on specifications, Monte Carlo simulation, and analytical models.

Methodology

Deterministic dual-core task partitioning: Cortex-M7 handles high-frequency sensor fusion and CAN-FD; Cortex-M4 manages 4G communication and microSD logging. Hardware combines a u-blox ZED-F9P RTK-GNSS receiver, Bosch BNO085 9-DoF IMU with on-chip fusion, CAN-FD interface, and SIM7600E-H 4G/LTE module in a 3D-printed vibration-resistant enclosure. Effective 50 Hz positioning rate from 25 Hz GNSS plus IMU interpolation. Validation on real circuit data: four campaigns, over 100 laps, 5.8 h of logging, 13 powertrain channels at speeds up to 185 km/h. Non-validated quantities characterized via manufacturer specifications, Monte Carlo simulation, and analytical models.

Explicit Limitations

CAN-FD powertrain acquisition and end-to-end operational reliability are the only experimentally validated claims on real circuit data. RTK positioning accuracy (2.5 cm CEP), sensor-fusion latency (sub-2 ms at 99th percentile), 4G-uplink reliability, and thermal margins are characterized through manufacturer specifications, Monte Carlo simulation, and analytical models, not through a fully instrumented end-to-end measurement campaign. Zero system resets or data-integrity errors reported, but only within the stated 5.8 h / four-campaign envelope.

Future Work

A fully instrumented end-to-end measurement campaign to empirically validate RTK positioning accuracy, sensor-fusion latency, 4G-uplink reliability, and thermal margins, identified as the immediate next step. Full openness and extensibility are positioned as enablers for distributed intelligence applications.

Concept Hubs

[[Concept - Real-Time Telemetry]]
[[Concept - Multi-Sensor Fusion]]
[[Concept - Embedded Systems]]
[[Concept - Open Architecture]]
[[Concept - Edge Security]]

Relevance Score

5

Monitoring Transfer

Monitoring problem, signal, uncertainty method, resulting action, evaluation setting.
Monitoring problem: acquisition and transport integrity of high-rate in-vehicle sensor and powertrain data during real operation.
Signal: CAN-FD powertrain channels (13 channels), RTK-GNSS position fixes at 25 Hz interpolated to 50 Hz, 9-DoF IMU with on-chip fusion, 4G uplink status, system reset and data-integrity counters.
Uncertainty method: manufacturer specifications, Monte Carlo simulation, and analytical models for non-validated quantities; direct measurement (zero resets, zero data-integrity errors) for CAN-FD and operational reliability.
Action: deterministic dual-core task partitioning with the Cortex-M7 reserved for high-frequency fusion and CAN-FD and the Cortex-M4 for 4G and microSD logging; real-time remote streaming.
Evaluation setting: real motorcycle circuit data, four campaigns, over 100 laps, 5.8 h of logging, speeds up to 185 km/h.
Limitation author: the paper itself delimits scope, stating that positioning accuracy, fusion latency, uplink reliability, and thermal margins are characterized only via specifications, simulation, and analytical models, with a fully instrumented end-to-end campaign identified as the immediate next step.
Limitation inference: the validated envelope (5.8 h, four campaigns, one motorcycle, one enclosure) is too narrow to establish reliability under the longer horizons, thermal extremes, and adversarial or degraded conditions typical of in-vehicle network security evaluation; the open architecture and 4G uplink also widen the attack surface without any security validation.
Limitation unknown: whether the 50 Hz interpolated positioning and sub-2 ms fusion latency hold under GNSS degradation, vibration, and thermal extremes; whether the 4G uplink is robust to loss, jamming, or spoofing; whether any security or intrusion-detection capability exists at all.

One transfer to IVN and one reason the transfer may fail.
Transfer to IVN: the deterministic dual-core partitioning and CAN-FD acquisition path can serve as a low-cost, open telemetry and ground-truth capture substrate for in-vehicle network intrusion-detection research, providing synchronized physical (IMU/GNSS) and bus-level signals for physical-semantics detection and anomaly labeling.
Transfer risk: the platform was validated on a motorcycle with a single CAN-FD bus and no adversarial traffic, so its timing determinism, message authentication, and reset-free guarantees may not survive the higher bus loads, multi-ECU topologies, and active attacks of a production in-vehicle network.

doi: not stated
source_link: not stated
text_kind: research paper
monitoring_problem: acquisition and transport integrity of high-rate in-vehicle sensor and powertrain data during real operation
signal: CAN-FD powertrain channels, RTK-GNSS position fixes, 9-DoF IMU fusion output, 4G uplink status, reset and data-integrity counters
uncertainty_method: manufacturer specifications, Monte Carlo simulation, and analytical models for non-validated quantities; direct measurement for CAN-FD and operational reliability
action: deterministic dual-core task partitioning with real-time remote streaming and microSD logging
eval_setting: real motorcycle circuit data, four campaigns, over 100 laps, 5.8 h of logging, speeds up to 185 km/h
limitation_author: positioning accuracy, fusion latency, 4G-uplink reliability, and thermal margins are characterized only by specifications, simulation, and analytical models, pending a fully instrumented end-to-end campaign
limitation_inference: validated envelope is too narrow for long-horizon, multi-node, adversarial in-vehicle network conditions, and the open architecture plus 4G uplink expands attack surface without security validation
limitation_unknown: behavior under GNSS degradation, vibration, thermal extremes, uplink loss or jamming, and whether any security or intrusion-detection capability exists
support_passage: We explicitly delimit the scope of the evidence presented: CAN-FD powertrain acquisition and end-to-end operational reliability are experimentally validated on real circuit data spanning four campaigns, over 100 laps, and 5.8 h of logging—with sustained acquisition of 13 powertrain channels at speeds up to 185 km/h and zero system resets or data-integrity errors. In contrast, RTK positioning accuracy (2.5 cm CEP), sensor-fusion latency (sub-2 ms at the 99th percentile), 4G-uplink reliability, and thermal margins are characterized through manufacturer specifications, Monte Carlo simulation, and analytical models, with a fully instrumented end-to-end measurement campaign identified as the immediate next step.
transfer_ivn: deterministic dual-core partitioning and CAN-FD acquisition path as a low-cost open telemetry and ground-truth capture substrate for in-vehicle network intrusion-detection research
transfer_risk: single-bus motorcycle validation with no adversarial traffic may not preserve timing determinism, reset-free operation, or authentication under production multi-ECU loads and active attacks

An open-architecture, dual-core (STM32H745) motorcycle telemetry unit integrating RTK-GNSS, a 9-DoF IMU with on-chip fusion, CAN-FD powertrain acquisition, and 4G/LTE streaming in a single extensible platform at ~EUR 265 BOM. The work is explicit about the epistemic status of each claim: CAN-FD acquisition and end-to-end reliability are empirically validated, while positioning accuracy, fusion latency, uplink reliability, and thermal margins rest on specifications, Monte Carlo simulation, and analytical models.

Deterministic dual-core task partitioning: Cortex-M7 handles high-frequency sensor fusion and CAN-FD; Cortex-M4 manages 4G communication and microSD logging. Hardware combines a u-blox ZED-F9P RTK-GNSS receiver, Bosch BNO085 9-DoF IMU with on-chip fusion, CAN-FD interface, and SIM7600E-H 4G/LTE module in a 3D-printed vibration-resistant enclosure. Effective 50 Hz positioning rate from 25 Hz GNSS plus IMU interpolation. Validation on real circuit data: four campaigns, over 100 laps, 5.8 h of logging, 13 powertrain channels at speeds up to 185 km/h. Non-validated quantities characterized via manufacturer specifications, Monte Carlo simulation, and analytical models.

CAN-FD powertrain acquisition and end-to-end operational reliability are the only experimentally validated claims on real circuit data. RTK positioning accuracy (2.5 cm CEP), sensor-fusion latency (sub-2 ms at 99th percentile), 4G-uplink reliability, and thermal margins are characterized through manufacturer specifications, Monte Carlo simulation, and analytical models, not through a fully instrumented end-to-end measurement campaign. Zero system resets or data-integrity errors reported, but only within the stated 5.8 h / four-campaign envelope.

A fully instrumented end-to-end measurement campaign to empirically validate RTK positioning accuracy, sensor-fusion latency, 4G-uplink reliability, and thermal margins, identified as the immediate next step. Full openness and extensibility are positioned as enablers for distributed intelligence applications.

[[Concept - Real-Time Telemetry]]
[[Concept - Multi-Sensor Fusion]]
[[Concept - Embedded Systems]]
[[Concept - Open Architecture]]
[[Concept - Edge Security]]

5

Monitoring problem, signal, uncertainty method, resulting action, evaluation setting.
Monitoring problem: acquisition and transport integrity of high-rate in-vehicle sensor and powertrain data during real operation.
Signal: CAN-FD powertrain channels (13 channels), RTK-GNSS position fixes at 25 Hz interpolated to 50 Hz, 9-DoF IMU with on-chip fusion, 4G uplink status, system reset and data-integrity counters.
Uncertainty method: manufacturer specifications, Monte Carlo simulation, and analytical models for non-validated quantities; direct measurement (zero resets, zero data-integrity errors) for CAN-FD and operational reliability.
Action: deterministic dual-core task partitioning with the Cortex-M7 reserved for high-frequency fusion and CAN-FD and the Cortex-M4 for 4G and microSD logging; real-time remote streaming.
Evaluation setting: real motorcycle circuit data, four campaigns, over 100 laps, 5.8 h of logging, speeds up to 185 km/h.
Limitation author: the paper itself delimits scope, stating that positioning accuracy, fusion latency, uplink reliability, and thermal margins are characterized only via specifications, simulation, and analytical models, with a fully instrumented end-to-end campaign identified as the immediate next step.
Limitation inference: the validated envelope (5.8 h, four campaigns, one motorcycle, one enclosure) is too narrow to establish reliability under the longer horizons, thermal extremes, and adversarial or degraded conditions typical of in-vehicle network security evaluation; the open architecture and 4G uplink also widen the attack surface without any security validation.
Limitation unknown: whether the 50 Hz interpolated positioning and sub-2 ms fusion latency hold under GNSS degradation, vibration, and thermal extremes; whether the 4G uplink is robust to loss, jamming, or spoofing; whether any security or intrusion-detection capability exists at all.

One transfer to IVN and one reason the transfer may fail.
Transfer to IVN: the deterministic dual-core partitioning and CAN-FD acquisition path can serve as a low-cost, open telemetry and ground-truth capture substrate for in-vehicle network intrusion-detection research, providing synchronized physical (IMU/GNSS) and bus-level signals for physical-semantics detection and anomaly labeling.
Transfer risk: the platform was validated on a motorcycle with a single CAN-FD bus and no adversarial traffic, so its timing determinism, message authentication, and reset-free guarantees may not survive the higher bus loads, multi-ECU topologies, and active attacks of a production in-vehicle network.

doi: not stated
source_link: not stated
text_kind: research paper
monitoring_problem: acquisition and transport integrity of high-rate in-vehicle sensor and powertrain data during real operation
signal: CAN-FD powertrain channels, RTK-GNSS position fixes, 9-DoF IMU fusion output, 4G uplink status, reset and data-integrity counters
uncertainty_method: manufacturer specifications, Monte Carlo simulation, and analytical models for non-validated quantities; direct measurement for CAN-FD and operational reliability
action: deterministic dual-core task partitioning with real-time remote streaming and microSD logging
eval_setting: real motorcycle circuit data, four campaigns, over 100 laps, 5.8 h of logging, speeds up to 185 km/h
limitation_author: positioning accuracy, fusion latency, 4G-uplink reliability, and thermal margins are characterized only by specifications, simulation, and analytical models, pending a fully instrumented end-to-end campaign
limitation_inference: validated envelope is too narrow for long-horizon, multi-node, adversarial in-vehicle network conditions, and the open architecture plus 4G uplink expands attack surface without security validation
limitation_unknown: behavior under GNSS degradation, vibration, thermal extremes, uplink loss or jamming, and whether any security or intrusion-detection capability exists
support_passage: We explicitly delimit the scope of the evidence presented: CAN-FD powertrain acquisition and end-to-end operational reliability are experimentally validated on real circuit data spanning four campaigns, over 100 laps, and 5.8 h of logging—with sustained acquisition of 13 powertrain channels at speeds up to 185 km/h and zero system resets or data-integrity errors. In contrast, RTK positioning accuracy (2.5 cm CEP), sensor-fusion latency (sub-2 ms at the 99th percentile), 4G-uplink reliability, and thermal margins are characterized through manufacturer specifications, Monte Carlo simulation, and analytical models, with a fully instrumented end-to-end measurement campaign identified as the immediate next step.
transfer_ivn: deterministic dual-core partitioning and CAN-FD acquisition path as a low-cost open telemetry and ground-truth capture substrate for in-vehicle network intrusion-detection research
transfer_risk: single-bus motorcycle validation with no adversarial traffic may not preserve timing determinism, reset-free operation, or authentication under production multi-ECU loads and active attacks

#needs-review

## Record Fields
doi: https://doi.org/10.3390/electronics15122604
source_link: not stated
text_kind: abstract
monitoring_problem: acquisition and transport integrity of high-rate in-vehicle sensor and powertrain data during real operation.
signal: CAN-FD powertrain channels (13 channels), RTK-GNSS position fixes at 25 Hz interpolated to 50 Hz, 9-DoF IMU with on-chip fusion, 4G uplink status, system reset and data-integrity counters.
uncertainty_method: manufacturer specifications, Monte Carlo simulation, and analytical models for non-validated quantities; direct measurement (zero resets, zero data-integrity errors) for CAN-FD and operational reliability.
action: deterministic dual-core task partitioning with the Cortex-M7 reserved for high-frequency fusion and CAN-FD and the Cortex-M4 for 4G and microSD logging; real-time remote streaming.
eval_setting: real motorcycle circuit data, four campaigns, over 100 laps, 5.8 h of logging, speeds up to 185 km/h
limitation_author: the paper itself delimits scope, stating that positioning accuracy, fusion latency, uplink reliability, and thermal margins are characterized only via specifications, simulation, and analytical models, with a fully instrumented end-to-end campaign identified as the immediate next step.
limitation_inference: the validated envelope (5.8 h, four campaigns, one motorcycle, one enclosure) is too narrow to establish reliability under the longer horizons, thermal extremes, and adversarial or degraded conditions typical of in-vehicle network security evaluation; the open architecture and 4G uplink also widen the attack surface without any security validation.
limitation_unknown: whether the 50 Hz interpolated positioning and sub-2 ms fusion latency hold under GNSS degradation, vibration, and thermal extremes; whether the 4G uplink is robust to loss, jamming, or spoofing; whether any security or intrusion-detection capability exists at all.
support_passage: We explicitly delimit the scope of the evidence presented: CAN-FD powertrain acquisition and end-to-end operational reliability are experimentally validated on real circuit data spanning four campaigns, over 100 laps, and 5.8 h of logging—with sustained acquisition of 13 powertrain channels at speeds up to 185 km/h and zero system resets or data-integrity errors. In contrast, RTK positioning accuracy (2.5 cm CEP), sensor-fusion latency (sub-2 ms at the 99th percentile), 4G-uplink reliability, and thermal margins are characterized through manufacturer specifications, Monte Carlo simulation, and analytical models, with a fully instrumented end-to-end measurement campaign identified as the immediate next step.
transfer_ivn: deterministic dual-core partitioning and CAN-FD acquisition path as a low-cost open telemetry and ground-truth capture substrate for in-vehicle network intrusion-detection research
transfer_risk: the platform was validated on a motorcycle with a single CAN-FD bus and no adversarial traffic, so its timing determinism, message authentication, and reset-free guarantees may not survive the higher bus loads, multi-ECU topologies, and active attacks of a production in-vehicle network.
