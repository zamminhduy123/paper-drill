---
title: "AI-Based Network Intrusion Detection System"
year: 2026
doi: "https://doi.org/10.22214/ijraset.2026.84969"
relevance_score: 0.55
type: paper
---
# AI-Based Network Intrusion Detection System

## Novelty
AI-based network intrusion detection system using a Random Forest classifier on the NSL-KDD dataset, integrated into a Flask web application with secure authentication, dataset upload, prediction, visual analytics, prediction logs, and alert generation.

## Methodology
The system preprocesses structured network traffic data using feature transformation, categorical encoding, normalization, and label conversion. A Random Forest classifier is trained to distinguish normal connections from attack traffic. The model is deployed in a Flask-based web application with SQLite storage for user and prediction data. The application supports authentication, dataset uploading, intrusion prediction, result visualization, logging, alert generation, and logout. Evaluation includes accuracy, precision, recall, F1-score, and functional testing of the web application.

## Explicit Limitations
not stated

## Future Work
not stated

## Concept Hubs
[[Concept - Intrusion Detection]]
[[Concept - Network Traffic Analysis]]
[[Concept - Lightweight Detection]]

## Relevance Score
0.55

## Monitoring Transfer
doi: not stated
source_link: not stated
text_kind: abstract
monitoring_problem: detect malicious network traffic and intrusion attempts
signal: structured network traffic features from the NSL-KDD dataset
uncertainty_method: not stated
action: alert generation, prediction logging, and result visualization
eval_setting: NSL-KDD dataset with accuracy, precision, recall, F1-score, and functional web-application tests
limitation_author: not stated
limitation_inference: The system is evaluated on NSL-KDD with a Random Forest model, so generalization to real-time enterprise traffic, unseen attacks, and deep-learning-based detection is not directly established.
limitation_unknown: not stated
support_passage: The proposed system uses the NSL-KDD dataset and a Random Forest classifier to distinguish normal network connections from attack traffic.
transfer_ivn: Apply a Random Forest-based traffic classifier with alerting to monitor in-vehicle network traffic for anomalous or malicious messages.
transfer_risk: In-vehicle network traffic has different protocols, timing, and real-time constraints than NSL-KDD, so the classifier may miss attacks or produce false alarms.

#needs-review

## Record Fields
doi: https://doi.org/10.22214/ijraset.2026.84969
source_link: not stated
text_kind: abstract
monitoring_problem: detect malicious network traffic and intrusion attempts
signal: structured network traffic features from the NSL-KDD dataset
uncertainty_method: not stated
action: alert generation, prediction logging, and result visualization
eval_setting: NSL-KDD dataset with accuracy, precision, recall, F1-score, and functional web-application tests
limitation_author: not stated
limitation_inference: The system is evaluated on NSL-KDD with a Random Forest model, so generalization to real-time enterprise traffic, unseen attacks, and deep-learning-based detection is not directly established.
limitation_unknown: not stated
support_passage: The proposed system uses the NSL-KDD dataset and a Random Forest classifier to distinguish normal network connections from attack traffic.
transfer_ivn: Apply a Random Forest-based traffic classifier with alerting to monitor in-vehicle network traffic for anomalous or malicious messages.
transfer_risk: In-vehicle network traffic has different protocols, timing, and real-time constraints than NSL-KDD, so the classifier may miss attacks or produce false alarms.
