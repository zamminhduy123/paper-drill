---
title: "Аутентификация электронных блоков управления автотранспорта на основе скрытых каналов"
year: 2026
doi: "https://doi.org/10.48612/jisp/rtzv-kfdx-ddfg"
relevance_score: 0.58
type: paper
---
# Аутентификация электронных блоков управления автотранспорта на основе скрытых каналов

## Novelty
Development and modification of a noise-robust hidden channel for ECU authentication in vehicle CAN FD networks, including a counter-synchronization method based on traffic optimization.

## Methodology
Comparative analysis of existing CAN hidden-channel and extended-protocol approaches, design of a CAN FD hidden channel integrated with time synchronization, and stand-based testing under noise-injection attacks.

## Explicit Limitations
None stated.

## Future Work
Deployment and validation of the proposed hidden-channel authentication scheme in real vehicles using CAN FD.

## Concept Hubs
[[Concept - In-Vehicle Network Security]]
[[Concept - CAN FD Scheduling]]
[[Concept - Network Traffic Analysis]]
[[Concept - Real-Time Attack Defense]]

## Relevance Score
0.58

## Monitoring Transfer
doi: not stated
source_link: not stated
text_kind: abstract
monitoring_problem: Authentication of vehicle ECUs in CAN FD networks under noise and injection attacks
signal: Hidden-channel information embedded in CAN FD traffic and counter-synchronization signals
uncertainty_method: not stated
action: Authenticate ECUs using hidden-channel counter synchronization
eval_setting: Laboratory stand simulating CAN FD hidden-channel operation with noise-injection attacks
limitation_author: not stated
limitation_inference: Evaluation is stand-based and not yet validated in real vehicles
limitation_unknown: not stated
support_passage: Разработанный скрытый канал интегрирован в систему синхронизации времени и протестирован на стенде, что позволило верифицировать его работоспособность в условиях воздействия шума.
transfer_ivn: Use CAN FD hidden-channel counter synchronization as an IVN authentication and monitoring signal to detect unauthorized ECUs under noisy bus conditions
transfer_risk: Real-world EMI, bus load variation, timing jitter, or adversarial noise may disrupt the hidden channel and reduce authentication reliability

#needs-review

## Record Fields
doi: https://doi.org/10.48612/jisp/rtzv-kfdx-ddfg
source_link: not stated
text_kind: abstract
monitoring_problem: Authentication of vehicle ECUs in CAN FD networks under noise and injection attacks
signal: Hidden-channel information embedded in CAN FD traffic and counter-synchronization signals
uncertainty_method: not stated
action: Authenticate ECUs using hidden-channel counter synchronization
eval_setting: Laboratory stand simulating CAN FD hidden-channel operation with noise-injection attacks
limitation_author: not stated
limitation_inference: Evaluation is stand-based and not yet validated in real vehicles
limitation_unknown: not stated
support_passage: Разработанный скрытый канал интегрирован в систему синхронизации времени и протестирован на стенде, что позволило верифицировать его работоспособность в условиях воздействия шума.
transfer_ivn: Use CAN FD hidden-channel counter synchronization as an IVN authentication and monitoring signal to detect unauthorized ECUs under noisy bus conditions
transfer_risk: Real-world EMI, bus load variation, timing jitter, or adversarial noise may disrupt the hidden channel and reduce authentication reliability
