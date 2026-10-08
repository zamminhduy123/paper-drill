---
title: "TS-FL: A Two-Stage Federated Learning Framework for Zero-Day Attack Detection in Autonomous Vehicle CAN-FD Networks"
year: 2026
doi: "10.1109/TITS.2026.3715632"
relevance_score: 0.65
type: paper
---
# TS-FL: A Two-Stage Federated Learning Framework for Zero-Day Attack Detection in Autonomous Vehicle CAN-FD Networks

## Novelty
- Proposes TS-FL, a two-stage federated learning framework for zero-day attack detection in autonomous vehicle CAN-FD networks.
- Uses progressive filtering: fast XGBoost binary anomaly detection with dynamic thresholding, then ensemble Isolation Forest plus multi-class XGBoost for unknown/known attack separation.
- Claims privacy-preserving collaborative learning, lower latency than CNN-based FL, and zero frame drops under 1 kHz CAN-FD batch processing.

## Methodology
- Federated learning trains local models on vehicle CAN-FD data and aggregates parameters to preserve privacy.
- Stage 1 applies personalized feature engineering, XGBoost binary classification, and dynamic thresholding to flag suspicious frames with low latency.
- Stage 2 uses an ensemble Isolation Forest to screen unknown zero-day attacks and multi-class XGBoost to classify known attack types.
- Evaluation uses sustained 1 kHz CAN-FD traffic, batch size 100 frames, frame-drop rate, per-frame inference latency, and zero-day detection metrics.

## Explicit Limitations
not stated

## Future Work
not stated

## Concept Hubs
[[Concept - Federated Learning]]
[[Concept - Anomaly Detection]]
[[Concept - CAN Intrusion Detection]]
[[Concept - Zero-Day Attack Detection]]
[[Concept - Privacy-Preserving Learning]]

## Relevance Score
0.65

## Monitoring Transfer
Monitoring problem: detect zero-day attacks in CAN-FD traffic while preserving privacy and avoiding frame drops.
Signal: CAN-FD frame features processed in windowed batches.
Uncertainty method: ensemble Isolation Forest anomaly screening and dynamic thresholding.
Resulting action: alarm on suspicious traffic, then separate unknown zero-day attacks from known attack classes.
Evaluation setting: 1 kHz CAN-FD traffic with batch size 100 frames, measuring frame drops, latency, and detection accuracy.
Transfer to IVN: deploy TS-FL on in-vehicle edge nodes for privacy-preserving CAN-FD zero-day monitoring.
Transfer risk: vehicle-specific CAN-FD feature drift can degrade federated XGBoost/Isolation Forest thresholds and increase false alarms.

doi: 10.1109/TITS.2026.3715632
source_link: https://doi.org/10.1109/TITS.2026.3715632
text_kind: journal article
monitoring_problem: zero-day attack detection in autonomous vehicle CAN-FD networks under privacy and latency constraints
signal: CAN-FD frame features in windowed batches
uncertainty_method: ensemble Isolation Forest screening with dynamic thresholding
action: trigger alarms and classify suspicious traffic into unknown zero-day attacks or known attack types
eval_setting: sustained 1 kHz CAN-FD traffic with batch size 100 frames, measuring frame drops, latency, and detection metrics
limitation_author: not stated
limitation_inference: may underperform on strongly temporal or adversarially crafted CAN-FD sequences because it relies on XGBoost and Isolation Forest rather than sequence models
limitation_unknown: not stated
support_passage: Under sustained 1 kHz CAN-FD traffic with a batch size of 100 frames, TS-FL achieves zero frame drops while other methods lose 0.5-12%.
transfer_ivn: deploy TS-FL on in-vehicle edge nodes for privacy-preserving CAN-FD zero-day monitoring
transfer_risk: vehicle-specific CAN-FD feature drift can degrade federated XGBoost and Isolation Forest thresholds, increasing false alarms

#needs-review

## Record Fields
doi: 10.1109/TITS.2026.3715632
source_link: https://doi.org/10.1109/TITS.2026.3715632
text_kind: fulltext
monitoring_problem: detect zero-day attacks in CAN-FD traffic while preserving privacy and avoiding frame drops.
signal: CAN-FD frame features processed in windowed batches.
uncertainty_method: ensemble Isolation Forest anomaly screening and dynamic thresholding.
action: trigger alarms and classify suspicious traffic into unknown zero-day attacks or known attack types
eval_setting: sustained 1 kHz CAN-FD traffic with batch size 100 frames, measuring frame drops, latency, and detection metrics
limitation_author: not stated
limitation_inference: may underperform on strongly temporal or adversarially crafted CAN-FD sequences because it relies on XGBoost and Isolation Forest rather than sequence models
limitation_unknown: not stated
support_passage: Under sustained 1 kHz CAN-FD traffic with a batch size of 100 frames, TS-FL achieves zero frame drops while other methods lose 0.5-12%.
transfer_ivn: deploy TS-FL on in-vehicle edge nodes for privacy-preserving CAN-FD zero-day monitoring
transfer_risk: vehicle-specific CAN-FD feature drift can degrade federated XGBoost/Isolation Forest thresholds and increase false alarms.
