---
title: "Thermal-Aware Signal Integrity and Fault-Propagation in Distributed Electrification Architectures for Intelligent Vehicles: A System-Level Safety and Reliability Analysis"
year: 2026
doi: "10.1109/CSNT69054.2026.11502568"
relevance_score: 30.0
type: paper
---
# Thermal-Aware Signal Integrity and Fault-Propagation in Distributed Electrification Architectures for Intelligent Vehicles: A System-Level Safety and Reliability Analysis

## Novelty
The paper studies how temperature-driven impedance changes, EMI drift, and signal-integrity degradation interact in distributed electric-vehicle architectures, especially BMS and inverter networks using CAN FD and daisy-chained SPI. Its main contribution is a system-level safety and reliability analysis that links thermal behavior, communication timing, and functional-safety implications, with a trade-off comparison of centralized, modular, and wireless BMS architectures.

## Methodology
The work uses a secondary technical research approach based on literature review, simulation review, and cross-referencing of published FMEDA and reliability data. It searches IEEE Xplore, SAE Mobilus, and ScienceDirect for 2015–2025 publications on automotive electrification, BMS, EMI, and functional safety. Secondary modeling uses SPICE signal-integrity simulations, COMSOL thermal analysis, and ANSYS EMI field studies. Assumptions include 85 °C ambient temperature, a 4-layer FR-4 PCB with 70 µm copper, CAN FD at 5 Mbps, and SPI at 10 MHz. The analysis focuses on relative trends in propagation delay, clock skew, jitter, impedance drift, and EMI susceptibility rather than certified quantitative safety metrics.

## Explicit Limitations
The authors state that the paper does not claim recalculated quantitative safety metrics. Quantitative bottom-up FMEDA recalculation and hardware fault-injection experiments are outside the scope. The simulation results are interpreted as relative and qualitative trends to support system-level architectural comparison, not as absolute or certified safety metrics.

## Future Work
Not explicitly stated as a formal future-work section. The paper implies future directions such as early architecture selection, interface partitioning, shielding optimization, redundancy-based communication design, predictive thermal management, and deeper integration of thermal, EMI, and signal-interference models into safety-critical EV network design.

## Concept Hubs
[[Concept - EMI Robust Communication]]
[[Concept - Functional Safety Verification]]
[[Concept - Embedded Systems]]
[[Concept - Thermal Signal Integrity]]

## Relevance Score
30

## Monitoring Transfer
doi: 10.1109/CSNT69054.2026.11502568
source_link: not stated
text_kind: IEEE conference paper
monitoring_problem: thermal- and EMI-induced timing degradation and fault propagation in BMS and inverter communication networks
signal: CAN FD and SPI propagation delay, clock skew, jitter, impedance drift, and EMI field drift
uncertainty_method: not stated
action: shielding optimization, redundancy-based communication design, predictive thermal management, and architecture/interface partitioning
eval_setting: secondary SPICE, COMSOL, and ANSYS simulations at 85 °C worst-case ambient, 4-layer PCB, CAN FD 5 Mbps, SPI 10 MHz, evaluated as relative system-level trends
limitation_author: no recalculated quantitative safety metrics, no bottom-up FMEDA recalculation, and no hardware fault-injection experiments
limitation_inference: secondary simulation and published-data cross-referencing may not capture real vehicle variability, dynamic thermal loads, manufacturing tolerances, or certified safety behavior
limitation_unknown: not stated
support_passage: Quantitative bottom-up FMEDA recalculation and hardware fault-injection experiments are outside the scope of this work
transfer_ivn: Use thermal- and EMI-aware timing drift as an in-vehicle network health signal to detect early CAN FD or SPI link degradation and trigger redundancy, rerouting, or thermal management
transfer_risk: The transfer may fail because the study is secondary, relative, and not validated on live IVN telemetry, real vehicle fault data, or deep-learning-based monitoring models

#needs-review

## Record Fields
doi: 10.1109/CSNT69054.2026.11502568
source_link: not stated
text_kind: fulltext
monitoring_problem: thermal- and EMI-induced timing degradation and fault propagation in BMS and inverter communication networks
signal: CAN FD and SPI propagation delay, clock skew, jitter, impedance drift, and EMI field drift
uncertainty_method: not stated
action: shielding optimization, redundancy-based communication design, predictive thermal management, and architecture/interface partitioning
eval_setting: secondary SPICE, COMSOL, and ANSYS simulations at 85 °C worst-case ambient, 4-layer PCB, CAN FD 5 Mbps, SPI 10 MHz, evaluated as relative system-level trends
limitation_author: no recalculated quantitative safety metrics, no bottom-up FMEDA recalculation, and no hardware fault-injection experiments
limitation_inference: secondary simulation and published-data cross-referencing may not capture real vehicle variability, dynamic thermal loads, manufacturing tolerances, or certified safety behavior
limitation_unknown: not stated
support_passage: Quantitative bottom-up FMEDA recalculation and hardware fault-injection experiments are outside the scope of this work
transfer_ivn: Use thermal- and EMI-aware timing drift as an in-vehicle network health signal to detect early CAN FD or SPI link degradation and trigger redundancy, rerouting, or thermal management
transfer_risk: The transfer may fail because the study is secondary, relative, and not validated on live IVN telemetry, real vehicle fault data, or deep-learning-based monitoring models
