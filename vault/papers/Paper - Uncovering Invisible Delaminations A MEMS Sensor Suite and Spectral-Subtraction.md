---
title: "Uncovering Invisible Delaminations: A MEMS Sensor Suite and Spectral-Subtraction Pipeline for Multilayer Diagnostics"
year: 2026
doi: "https://doi.org/10.58286/33921"
relevance_score: 0.75
type: paper
---
# Uncovering Invisible Delaminations: A MEMS Sensor Suite and Spectral-Subtraction Pipeline for Multilayer Diagnostics

## Novelty
Compact battery-operated impact probe combining an ESP32-S3 MCU, PDM MEMS microphone, high-resolution MEMS accelerometer, and solenoid actuator for repeatable impulse scanning. The key novelty is an on-device adaptive spectral-subtraction pipeline that removes the solenoid’s actuator signature from impact transients, enabling low-cost material-dependent feature extraction and potential TinyML-based defect screening.

## Methodology
The system uses a solenoid-driven impact probe with a 4 kHz sampling front-end based on a PDM MEMS microphone and ADXL355 accelerometer. The signal-processing chain performs pre-processing, temporal alignment, automatic impulse detection, and adaptive spectral subtraction using STFT analysis, inverse-STFT reconstruction with normalization, STFT delay correction, and optional fine alignment. From the reconstructed vibration channel, it extracts peak acceleration, RMS acceleration, dominant FFT amplitude, and dominant FFT frequency. These features support on-device thresholding, rule-based screening, or a tiny edge classifier. Laboratory validation was performed on cardboard, plastic, and wood samples.

## Explicit Limitations
The current system is implemented as a USB peripheral for PC operation. Laboratory validation is limited to three reference materials: cardboard, plastic, and wood.

## Future Work
Convert the system into a wireless node for untethered surveys. Expand multilayer test campaigns. Add localization capabilities. Develop on-device TinyML models for noise subtraction, data fusion, automated defect detection, and mapping.

## Concept Hubs
[[Concept - TinyML Systems]] [[Concept - Edge AI Inference]] [[Concept - Multi-Sensor Fusion]] [[Concept - Resource-Constrained Edge]] [[Concept - Anomaly Detection]]

## Relevance Score
0.75

## Monitoring Transfer
doi:
not stated
source_link:
not stated
text_kind:
abstract
monitoring_problem:
Detect hidden delaminations and subsurface discontinuities in multilayer architectural finishes, civil structures, and industrial coverings.
signal:
Impact-induced vibration and acoustic transients from a MEMS accelerometer and PDM MEMS microphone.
uncertainty_method:
not stated
action:
On-device thresholding, rule-based screening, or TinyML-based defect detection and mapping.
eval_setting:
Laboratory validation on three reference materials: cardboard, plastic, and wood.
limitation_author:
USB peripheral for PC operation; laboratory validation on three reference materials.
limitation_inference:
No field validation, no localization, limited material set, no demonstrated wireless node, and no explicit uncertainty quantification.
limitation_unknown:
not stated
support_passage:
The current system is implemented as a USB peripheral for PC operation and can be converted to a wireless node for untethered surveys. Laboratory validation on three reference materials spanning thin/soft to thick/rigid behaviors.
transfer_ivn:
Use an ESP32-class TinyML node with MEMS vibration/acoustic sensing and spectral-subtraction features to detect mechanical loosening, delamination, or structural anomalies in vehicle components and stream alerts over the IVN.
transfer_risk:
Nonstationary engine, road, and acoustic noise in vehicles may overlap defect signatures, causing spectral subtraction and lab-trained thresholds to miss faults or produce false alarms.

#needs-review

## Record Fields
doi: https://doi.org/10.58286/33921
source_link: not stated
text_kind: abstract
monitoring_problem: Detect hidden delaminations and subsurface discontinuities in multilayer architectural finishes, civil structures, and industrial coverings.
signal: Impact-induced vibration and acoustic transients from a MEMS accelerometer and PDM MEMS microphone.
uncertainty_method: not stated
action: On-device thresholding, rule-based screening, or TinyML-based defect detection and mapping.
eval_setting: Laboratory validation on three reference materials: cardboard, plastic, and wood.
limitation_author: USB peripheral for PC operation; laboratory validation on three reference materials.
limitation_inference: No field validation, no localization, limited material set, no demonstrated wireless node, and no explicit uncertainty quantification.
limitation_unknown: not stated
support_passage: The current system is implemented as a USB peripheral for PC operation and can be converted to a wireless node for untethered surveys. Laboratory validation on three reference materials spanning thin/soft to thick/rigid behaviors.
transfer_ivn: Use an ESP32-class TinyML node with MEMS vibration/acoustic sensing and spectral-subtraction features to detect mechanical loosening, delamination, or structural anomalies in vehicle components and stream alerts over the IVN.
transfer_risk: Nonstationary engine, road, and acoustic noise in vehicles may overlap defect signatures, causing spectral subtraction and lab-trained thresholds to miss faults or produce false alarms.
