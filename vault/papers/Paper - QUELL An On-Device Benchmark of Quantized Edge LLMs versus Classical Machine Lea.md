---
title: "QUELL: An On-Device Benchmark of Quantized Edge LLMs versus Classical Machine Learning for IoT Intrusion Detection"
year: 2026
doi: "https://doi.org/10.5281/zenodo.21819108"
relevance_score: 9.574
type: paper
---
# QUELL: An On-Device Benchmark of Quantized Edge LLMs versus Classical Machine Learning for IoT Intrusion Detection

Novelty

* First hardware-grounded, multi-axis benchmark comparing quantized edge LLMs (GPT-2-medium, Qwen2.5-0.5B/1.5B at FP16/INT8/4-bit) against classical ML (XGBoost, random forest) for IoT intrusion detection on a shared NVIDIA Jetson Orin Nano.

* Serializes network-flow records as text to fine-tune lightweight decoder-only LLMs, unifying tabular intrusion data with LLM input formats.

* Simultaneously evaluates detection quality, on-device latency/energy/memory, quantization retention, unknown-attack generalization, and adversarial robustness across three heterogeneous IoT datasets (Edge-IIoTset, CICIoT2023, N-BaIoT).

* Provides a leakage-controlled matched protocol and full reproducibility package with committed raw results, split manifest, and table/figure regeneration scripts.

Methodology

* Fine-tune lightweight decoder-only LLMs (GPT-2-medium, Qwen2.5-0.5B/1.5B) by serializing network-flow records as text.

* Quantize models to FP16, INT8, and 4-bit precision.

* Deploy quantized LLMs on an NVIDIA Jetson Orin Nano.

* Compare against well-tuned XGBoost and random-forest baselines.

* Evaluate on three heterogeneous IoT datasets: Edge-IIoTset, CICIoT2023, N-BaIoT.

* Use a matched, leakage-controlled protocol with a leakage-safe split manifest (results/split_report.json).

* Assess across five axes: detection quality, on-device latency/energy/memory, quantization retention, unknown-attack generalization, adversarial robustness.

* Regenerate every table via scripts/reproduce_tables.py and figures via figures/make_fig*.py; verify figure values with figures/verify_figures.py.

Explicit Limitations

* Classical detectors match or exceed quantized LLM accuracy while costing one to three orders of magnitude less on the same device.

* Benchmark datasets are public and not redistributed; no new data collection.

* Datasets are limited to three IoT datasets (Edge-IIoTset, CICIoT2023, N-BaIoT).

* LLM size capped at 1.5B parameters; only decoder-only architectures tested.

* Quantization limited to FP16/INT8/4-bit.

* Single edge device (NVIDIA Jetson Orin Nano) for deployment.

* No stated evaluation on non-IoT network domains.

Future Work

* Not stated.

Concept Hubs

[[Concept - IoT Intrusion Detection]]
[[Concept - Edge Security]]
[[Concept - Lightweight Detection]]
[[Concept - Energy-Aware Inference]]
[[Concept - Data Leakage Prevention]]

Relevance Score

Not stated.

Monitoring Transfer

Monitoring problem, signal, uncertainty method, resulting action, evaluation setting.

* Monitoring problem: IoT network intrusion detection under on-device resource constraints.

* Signal: Serialized network-flow records as text fed to quantized LLMs; classical ML features for XGBoost/random forest.

* Uncertainty method: Not stated.

* Action: Classify network flows as benign or attack; compare detector quality, latency, energy, memory, quantization retention, unknown-attack generalization, and adversarial robustness.

* Evaluation setting: On-device (NVIDIA Jetson Orin Nano) with matched, leakage-controlled protocol across Edge-IIoTset, CICIoT2023, N-BaIoT.

One transfer to IVN and one reason the transfer may fail.

* Transfer to IVN: Serialize CAN/CAN-FD frame or signal records as text and deploy quantized decoder-only LLMs on in-vehicle edge hardware for intrusion detection, benchmarking against classical tree ensembles under matched leakage-controlled splits.

* Transfer risk: IVN traffic has tight real-time determinism and safety certification constraints; the one-to-three-orders-of-magnitude latency/energy penalty of quantized LLMs on embedded hardware may violate hard deadlines and functional-safety requirements that IoT intrusion detection does not enforce.

doi: not stated
source_link: not stated
text_kind: reproducibility package / repository abstract
monitoring_problem: IoT network intrusion detection on resource-constrained edge devices
signal: serialized network-flow records as text; classical ML flow features
uncertainty_method: not stated
action: compare quantized LLMs vs classical ML across detection quality, on-device latency/energy/memory, quantization retention, unknown-attack generalization, adversarial robustness
eval_setting: on-device NVIDIA Jetson Orin Nano; Edge-IIoTset, CICIoT2023, N-BaIoT; matched leakage-controlled protocol
limitation_author: classical detectors match or exceed quantized LLM accuracy at one to three orders of magnitude lower cost on the same device
limitation_inference: findings may not generalize beyond the three tested IoT datasets, decoder-only LLMs up to 1.5B, and the single Jetson Orin Nano platform
limitation_unknown: no reported uncertainty quantification method; no evaluation on non-IoT network domains or larger LLMs
support_passage: Under a matched, leakage-controlled protocol the classical detectors match or exceed the quantized LLM on accuracy while costing one to three orders of magnitude less on the same device.
transfer_ivn: serialize CAN/CAN-FD frame or signal records as text, fine-tune and quantize decoder-only LLMs, deploy on in-vehicle edge hardware, and benchmark against classical tree ensembles under leakage-controlled splits
transfer_risk: IVN hard real-time deadlines and functional-safety certification may be violated by the one-to-three-orders-of-magnitude latency/energy penalty of quantized LLMs on embedded hardware

First hardware-grounded, multi-axis benchmark comparing quantized edge LLMs (GPT-2-medium, Qwen2.5-0.5B/1.5B at FP16/INT8/4-bit) against classical ML (XGBoost, random forest) for IoT intrusion detection on a shared NVIDIA Jetson Orin Nano.

Serializes network-flow records as text to fine-tune lightweight decoder-only LLMs, unifying tabular intrusion data with LLM input formats.

Simultaneously evaluates detection quality, on-device latency/energy/memory, quantization retention, unknown-attack generalization, and adversarial robustness across three heterogeneous IoT datasets (Edge-IIoTset, CICIoT2023, N-BaIoT).

Provides a leakage-controlled matched protocol and full reproducibility package with committed raw results, split manifest, and table/figure regeneration scripts.

Fine-tune lightweight decoder-only LLMs (GPT-2-medium, Qwen2.5-0.5B/1.5B) by serializing network-flow records as text.

Quantize models to FP16, INT8, and 4-bit precision.

Deploy quantized LLMs on an NVIDIA Jetson Orin Nano.

Compare against well-tuned XGBoost and random-forest baselines.

Evaluate on three heterogeneous IoT datasets: Edge-IIoTset, CICIoT2023, N-BaIoT.

Use a matched, leakage-controlled protocol with a leakage-safe split manifest (results/split_report.json).

Assess across five axes: detection quality, on-device latency/energy/memory, quantization retention, unknown-attack generalization, adversarial robustness.

Regenerate every table via scripts/reproduce_tables.py and figures via figures/make_fig*.py; verify figure values with figures/verify_figures.py.

Classical detectors match or exceed quantized LLM accuracy while costing one to three orders of magnitude less on the same device.

Benchmark datasets are public and not redistributed; no new data collection.

Datasets are limited to three IoT datasets (Edge-IIoTset, CICIoT2023, N-BaIoT).

LLM size capped at 1.5B parameters; only decoder-only architectures tested.

Quantization limited to FP16/INT8/4-bit.

Single edge device (NVIDIA Jetson Orin Nano) for deployment.

No stated evaluation on non-IoT network domains.

Not stated.

[[Concept - IoT Intrusion Detection]]
[[Concept - Edge Security]]
[[Concept - Lightweight Detection]]
[[Concept - Energy-Aware Inference]]
[[Concept - Data Leakage Prevention]]

Not stated.

Monitoring problem, signal, uncertainty method, resulting action, evaluation setting.

Monitoring problem: IoT network intrusion detection under on-device resource constraints.

Signal: Serialized network-flow records as text fed to quantized LLMs; classical ML features for XGBoost/random forest.

Uncertainty method: Not stated.

Action: Classify network flows as benign or attack; compare detector quality, latency, energy, memory, quantization retention, unknown-attack generalization, and adversarial robustness.

Evaluation setting: On-device (NVIDIA Jetson Orin Nano) with matched, leakage-controlled protocol across Edge-IIoTset, CICIoT2023, N-BaIoT.

One transfer to IVN and one reason the transfer may fail.

Transfer to IVN: Serialize CAN/CAN-FD frame or signal records as text and deploy quantized decoder-only LLMs on in-vehicle edge hardware for intrusion detection, benchmarking against classical tree ensembles under matched leakage-controlled splits.

Transfer risk: IVN traffic has tight real-time determinism and safety certification constraints; the one-to-three-orders-of-magnitude latency/energy penalty of quantized LLMs on embedded hardware may violate hard deadlines and functional-safety requirements that IoT intrusion detection does not enforce.

doi: not stated
source_link: not stated
text_kind: reproducibility package / repository abstract
monitoring_problem: IoT network intrusion detection on resource-constrained edge devices
signal: serialized network-flow records as text; classical ML flow features
uncertainty_method: not stated
action: compare quantized LLMs vs classical ML across detection quality, on-device latency/energy/memory, quantization retention, unknown-attack generalization, adversarial robustness
eval_setting: on-device NVIDIA Jetson Orin Nano; Edge-IIoTset, CICIoT2023, N-BaIoT; matched leakage-controlled protocol
limitation_author: classical detectors match or exceed quantized LLM accuracy at one to three orders of magnitude lower cost on the same device
limitation_inference: findings may not generalize beyond the three tested IoT datasets, decoder-only LLMs up to 1.5B, and the single Jetson Orin Nano platform
limitation_unknown: no reported uncertainty quantification method; no evaluation on non-IoT network domains or larger LLMs
support_passage: Under a matched, leakage-controlled protocol the classical detectors match or exceed the quantized LLM on accuracy while costing one to three orders of magnitude less on the same device.
transfer_ivn: serialize CAN/CAN-FD frame or signal records as text, fine-tune and quantize decoder-only LLMs, deploy on in-vehicle edge hardware, and benchmark against classical tree ensembles under leakage-controlled splits
transfer_risk: IVN hard real-time deadlines and functional-safety certification may be violated by the one-to-three-orders-of-magnitude latency/energy penalty of quantized LLMs on embedded hardware

#needs-review

## Record Fields
doi: https://doi.org/10.5281/zenodo.21819108
source_link: not stated
text_kind: abstract
monitoring_problem: IoT network intrusion detection on resource-constrained edge devices
signal: serialized network-flow records as text; classical ML flow features
uncertainty_method: not stated
action: compare quantized LLMs vs classical ML across detection quality, on-device latency/energy/memory, quantization retention, unknown-attack generalization, adversarial robustness
eval_setting: on-device NVIDIA Jetson Orin Nano; Edge-IIoTset, CICIoT2023, N-BaIoT; matched leakage-controlled protocol
limitation_author: classical detectors match or exceed quantized LLM accuracy at one to three orders of magnitude lower cost on the same device
limitation_inference: findings may not generalize beyond the three tested IoT datasets, decoder-only LLMs up to 1.5B, and the single Jetson Orin Nano platform
limitation_unknown: no reported uncertainty quantification method; no evaluation on non-IoT network domains or larger LLMs
support_passage: Under a matched, leakage-controlled protocol the classical detectors match or exceed the quantized LLM on accuracy while costing one to three orders of magnitude less on the same device.
transfer_ivn: serialize CAN/CAN-FD frame or signal records as text, fine-tune and quantize decoder-only LLMs, deploy on in-vehicle edge hardware, and benchmark against classical tree ensembles under leakage-controlled splits
transfer_risk: IVN hard real-time deadlines and functional-safety certification may be violated by the one-to-three-orders-of-magnitude latency/energy penalty of quantized LLMs on embedded hardware
