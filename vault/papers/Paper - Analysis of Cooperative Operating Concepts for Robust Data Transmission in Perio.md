---
title: "Analysis of Cooperative Operating Concepts for Robust Data Transmission in Periodically Disturbed CAN FD Networks"
year: 2024
doi: "https://doi.org/10.1109/temc.2024.3365218"
relevance_score: 7.952
type: paper
---
# Analysis of Cooperative Operating Concepts for Robust Data Transmission in Periodically Disturbed CAN FD Networks

Novelty

* Introduces a cooperative operating concept that treats the electromagnetic interference (EMI) source (e.g., motor inverter) and the CAN FD communication system jointly, rather than mitigating interference on the receiver side alone.
* Proposes synchronizing CAN FD data transmission to a known periodic disturbance source, exploiting the periodicity of PWM-driven power electronics instead of merely enduring it.
* Demonstrates that this source-sink co-design enables faster, more reliable data transmission with low latency in periodically disturbed channels.

Methodology

* Analysis of periodically disturbed CAN FD transmission channels caused by fast-switching power electronics in electric drivetrains (common-mode and differential-mode disturbances).
* Introduction and analysis of a modified CAN FD communication system whose transmission schedule is aligned with a dominant, known disturbance source.
* Evaluation of effective data rate and latency improvements when communication is synchronized to the periodic EMI pattern of, e.g., the motor inverter.

Explicit Limitations

* Periodic disturbances in the transmission channel can significantly reduce effective data rate and increase latency (motivating problem, not solution limitation).
* The concept presupposes a known, dominant, periodic disturbance source; interference that is aperiodic or unknown is not addressed in the abstract.
* Approach requires cooperation/coordination between EMI-generating power electronics and the communication system, implying added system-level coupling.
* (Implied) No deep learning or learning-based component is involved; the contribution is at the communication/signal level.

Future Work

* (Implied) Extension to additional or multiple disturbance sources beyond the motor inverter.
* (Implied) Integration into future vehicles with highly automated driving functions and extended wire harnesses.
* (Implied) Practical validation in realistic vehicular electromagnetic environments, including cable coupling effects.

Concept Hubs

* [[Concept - EMI Robust Communication]]
* [[Concept - CAN FD Scheduling]]
* [[Concept - Cooperative Operating Concept]]
* [[Concept - Functional Safety Verification]]

Relevance Score

* 2/10 — The paper addresses physical-layer robustness of CAN FD against EMI, which is background-relevant to in-vehicle network reliability, but contains no deep learning methods, matching only marginally with the thesis on deep learning in In-Vehicle Networks. (Functional Safety Verification reused; other hubs created as no existing hub covers EMI-driven communication robustness.)