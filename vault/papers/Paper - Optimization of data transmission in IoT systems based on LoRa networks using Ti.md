---
title: "Optimization of data transmission in IoT systems based on LoRa networks using TinyML"
year: 2026
doi: "not stated"
relevance_score: 8.0
type: paper
---
# Optimization of data transmission in IoT systems based on LoRa networks using TinyML

## Novelty
Local edge transmission decisions using lightweight ML to send only informative measurements, reducing LoRa packets and energy while maintaining monitoring quality; comparative framework including periodic, decision-tree, logistic-regression, MLP, and Autoencoder approaches with LoRa PHY parameters.

## Methodology
Environmental monitoring case study with temperature and humidity sensors on resource-constrained microcontrollers connected to LoRa; compares periodic 1-minute transmission, decision-tree transmission gating, and logistic-regression transmission gating; evaluates transmitted packets, transmission reduction, airtime, estimated energy consumption, and monitoring quality.

## Explicit Limitations
The study is presented as a methodological framework with expected results; quantitative evaluation requires real data and implementation.

## Future Work
Obtain real data and implementation for quantitative evaluation; test additional TinyML approaches such as MLP predictor and Autoencoder; evaluate LoRa PHY parameters PRR, SF, BW, CR, payload size, and airtime.

## Concept Hubs
[[Concept - TinyML Systems]]
[[Concept - Resource-Constrained Edge]]
[[Concept - Energy-Aware Inference]]
[[Concept - Edge AI Inference]]

## Relevance Score
8

## Monitoring Transfer
doi: not stated
source_link: not stated
text_kind: abstract
monitoring_problem: minimize unnecessary LoRa transmissions and sensor energy while preserving acceptable monitoring quality
signal: temperature and humidity sensor measurements
uncertainty_method: not stated
action: transmit only when the model predicts the measurement contains sufficient useful information
eval_setting: comparative LoRa environmental monitoring framework with packet, airtime, energy, and quality metrics
limitation_author: requires real data and implementation for quantitative evaluation
limitation_inference: lightweight models may miss complex patterns or rare informative events
limitation_unknown: not stated
support_passage: Η προτεινόμενη μέθοδος επιτρέπει τη λήψη τοπικών αποφάσεων στον κόμβο άκρου, όπου κάθε κόμβος είναι υπεύθυνος για τον προσδιορισμό του εάν η τελευταία νέα μέτρηση έχει αρκετές χρήσιμες πληροφορίες για να δικαιολογήσει τη μετάδοση. Η εργασία παρουσιάζει ένα πλήρως καθορισμένο μεθοδολογικό πλαίσιο, το οποίο μπορεί να αξιολογηθεί ποσοτικά όταν διατεθούν πραγματικά δεδομένα και υλοποίηση.
transfer_ivn: use lightweight edge models to gate in-vehicle network telemetry transmission, reducing bus traffic while preserving diagnostic monitoring quality
transfer_risk: IVN signals are safety-critical, latency-sensitive, and protocol-constrained, so ML-based gating may miss rare faults or violate real-time reliability

#needs-review

## Record Fields
doi: not stated
source_link: not stated
text_kind: abstract
monitoring_problem: minimize unnecessary LoRa transmissions and sensor energy while preserving acceptable monitoring quality
signal: temperature and humidity sensor measurements
uncertainty_method: not stated
action: transmit only when the model predicts the measurement contains sufficient useful information
eval_setting: comparative LoRa environmental monitoring framework with packet, airtime, energy, and quality metrics
limitation_author: requires real data and implementation for quantitative evaluation
limitation_inference: lightweight models may miss complex patterns or rare informative events
limitation_unknown: not stated
support_passage: Η προτεινόμενη μέθοδος επιτρέπει τη λήψη τοπικών αποφάσεων στον κόμβο άκρου, όπου κάθε κόμβος είναι υπεύθυνος για τον προσδιορισμό του εάν η τελευταία νέα μέτρηση έχει αρκετές χρήσιμες πληροφορίες για να δικαιολογήσει τη μετάδοση. Η εργασία παρουσιάζει ένα πλήρως καθορισμένο μεθοδολογικό πλαίσιο, το οποίο μπορεί να αξιολογηθεί ποσοτικά όταν διατεθούν πραγματικά δεδομένα και υλοποίηση.
transfer_ivn: use lightweight edge models to gate in-vehicle network telemetry transmission, reducing bus traffic while preserving diagnostic monitoring quality
transfer_risk: IVN signals are safety-critical, latency-sensitive, and protocol-constrained, so ML-based gating may miss rare faults or violate real-time reliability
