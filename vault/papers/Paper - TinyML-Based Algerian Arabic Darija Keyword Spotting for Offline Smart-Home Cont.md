---
title: "TinyML-Based Algerian Arabic Darija Keyword Spotting for Offline Smart-Home Control: Dataset, Model, and Hardware Deployment"
year: 2026
doi: "https://doi.org/10.5281/zenodo.21810130"
relevance_score: 5.916
type: paper
---
# TinyML-Based Algerian Arabic Darija Keyword Spotting for Offline Smart-Home Control: Dataset, Model, and Hardware Deployment

Novelty

Introduces a new dialectal (Algerian Arabic Darija) keyword-spotting dataset of 5,100 recordings from 100 native speakers for offline smart-home control, using 16 compound action–object commands across five home domains plus a noise rejection class. Combines a low-resource dialect corpus with TinyML deployment for resource-constrained edge inference.

Methodology

* Data: 5,100 WAV recordings (16 kHz, 16-bit, mono, 2.0 s), 100 native Darija speakers, four indoor environments; 170 min total (160 min commands + 10 min noise).

* Classes: 16 compound commands (four shared verb prefixes chaal-, tafi-, eftah-, eghlak-; eight shared object suffixes) + background noise class.

* Balance: 300 samples per class (3 repetitions × 100 speakers); 300 noise files.

* Split: 4,416 train / 384 test (≈92%/8%), speaker-disjoint for commands.

* Model/deployment: TinyML-based KWS model with hardware deployment for offline smart-home control (specific architecture and hardware not stated).

Explicit Limitations

* No model architecture, accuracy, latency, or memory footprint results are reported in the provided text.

* Dataset scope limited to 100 speakers and four indoor environments; generalization to other dialects, accents, or noisy conditions is untested here.

* Compound two-word commands introduce deliberate acoustic overlap, which may complicate discrimination.

* Noise class limited to 300 files / 10 minutes, potentially underrepresenting real-world background variability.

* Hardware deployment details (target MCU, quantization, power) are not stated.

Future Work

Not stated.

Concept Hubs

[[Concept - TinyML Systems]]
[[Concept - Edge Security]]
[[Concept - Energy-Aware Inference]]
[[Concept - Lightweight Detection]]
[[Concept - Privacy-Preserving Learning]]

Relevance Score

Not stated.

Monitoring Transfer

Monitoring problem, signal, uncertainty method, resulting action, evaluation setting. One transfer to IVN and one reason the transfer may fail.

doi: not stated
source_link: not stated
text_kind: dataset and model paper (abstract)
monitoring_problem: offline keyword spotting for smart-home voice command recognition under resource-constrained edge conditions
signal: 16 kHz 16-bit mono WAV audio recordings of Algerian Arabic Darija compound commands and background noise
uncertainty_method: not stated
action: classify spoken utterance into one of 16 smart-home commands or the background noise rejection class
eval_setting: 4,416 training / 384 test files (≈92%/8%), speaker-disjoint for commands; 300 samples per class; four indoor environments; 100 native speakers
limitation_author: not stated
limitation_inference: no reported accuracy, latency, memory, or hardware specifics; small speaker pool and limited noise diversity constrain generalization claims
limitation_unknown: model architecture, quantization scheme, target microcontroller, power budget, on-device performance metrics
support_passage: This dataset comprises 5,100 audio recordings (16 kHz, 16-bit, mono, WAV, 2.0 s duration) collected from 100 native Algerian Arabic Darija speakers across four indoor environments ... It supports keyword spotting (KWS) for 16 compound smart-home voice commands ... plus a background noise class for rejection training.
transfer_ivn: Treat spoken Darija command tokens as in-vehicle voice-control utterances and use the KWS pipeline for hands-free IVN actuation (e.g., climate, lighting, door lock), with noise class mapped to road/cabin noise rejection.
transfer_risk: Dialectal Darija phonetics, vocabulary, and compound morphology differ from in-vehicle command grammars and languages, so the trained model may not transfer without new in-cabin recordings and domain adaptation.

Introduces a new dialectal (Algerian Arabic Darija) keyword-spotting dataset of 5,100 recordings from 100 native speakers for offline smart-home control, using 16 compound action–object commands across five home domains plus a noise rejection class. Combines a low-resource dialect corpus with TinyML deployment for resource-constrained edge inference.

Data: 5,100 WAV recordings (16 kHz, 16-bit, mono, 2.0 s), 100 native Darija speakers, four indoor environments; 170 min total (160 min commands + 10 min noise).

Classes: 16 compound commands (four shared verb prefixes chaal-, tafi-, eftah-, eghlak-; eight shared object suffixes) + background noise class.

Balance: 300 samples per class (3 repetitions × 100 speakers); 300 noise files.

Split: 4,416 train / 384 test (≈92%/8%), speaker-disjoint for commands.

Model/deployment: TinyML-based KWS model with hardware deployment for offline smart-home control (specific architecture and hardware not stated).

No model architecture, accuracy, latency, or memory footprint results are reported in the provided text.

Dataset scope limited to 100 speakers and four indoor environments; generalization to other dialects, accents, or noisy conditions is untested here.

Compound two-word commands introduce deliberate acoustic overlap, which may complicate discrimination.

Noise class limited to 300 files / 10 minutes, potentially underrepresenting real-world background variability.

Hardware deployment details (target MCU, quantization, power) are not stated.

Not stated.

[[Concept - TinyML Systems]]
[[Concept - Edge Security]]
[[Concept - Energy-Aware Inference]]
[[Concept - Lightweight Detection]]
[[Concept - Privacy-Preserving Learning]]

Not stated.

Monitoring problem, signal, uncertainty method, resulting action, evaluation setting. One transfer to IVN and one reason the transfer may fail.

doi: not stated
source_link: not stated
text_kind: dataset and model paper (abstract)
monitoring_problem: offline keyword spotting for smart-home voice command recognition under resource-constrained edge conditions
signal: 16 kHz 16-bit mono WAV audio recordings of Algerian Arabic Darija compound commands and background noise
uncertainty_method: not stated
action: classify spoken utterance into one of 16 smart-home commands or the background noise rejection class
eval_setting: 4,416 training / 384 test files (≈92%/8%), speaker-disjoint for commands; 300 samples per class; four indoor environments; 100 native speakers
limitation_author: not stated
limitation_inference: no reported accuracy, latency, memory, or hardware specifics; small speaker pool and limited noise diversity constrain generalization claims
limitation_unknown: model architecture, quantization scheme, target microcontroller, power budget, on-device performance metrics
support_passage: This dataset comprises 5,100 audio recordings (16 kHz, 16-bit, mono, WAV, 2.0 s duration) collected from 100 native Algerian Arabic Darija speakers across four indoor environments ... It supports keyword spotting (KWS) for 16 compound smart-home voice commands ... plus a background noise class for rejection training.
transfer_ivn: Treat spoken Darija command tokens as in-vehicle voice-control utterances and use the KWS pipeline for hands-free IVN actuation (e.g., climate, lighting, door lock), with noise class mapped to road/cabin noise rejection.
transfer_risk: Dialectal Darija phonetics, vocabulary, and compound morphology differ from in-vehicle command grammars and languages, so the trained model may not transfer without new in-cabin recordings and domain adaptation.

#needs-review

## Record Fields
doi: https://doi.org/10.5281/zenodo.21810130
source_link: not stated
text_kind: abstract
monitoring_problem: offline keyword spotting for smart-home voice command recognition under resource-constrained edge conditions
signal: 16 kHz 16-bit mono WAV audio recordings of Algerian Arabic Darija compound commands and background noise
uncertainty_method: not stated
action: classify spoken utterance into one of 16 smart-home commands or the background noise rejection class
eval_setting: 4,416 training / 384 test files (≈92%/8%), speaker-disjoint for commands; 300 samples per class; four indoor environments; 100 native speakers
limitation_author: not stated
limitation_inference: no reported accuracy, latency, memory, or hardware specifics; small speaker pool and limited noise diversity constrain generalization claims
limitation_unknown: model architecture, quantization scheme, target microcontroller, power budget, on-device performance metrics
support_passage: This dataset comprises 5,100 audio recordings (16 kHz, 16-bit, mono, WAV, 2.0 s duration) collected from 100 native Algerian Arabic Darija speakers across four indoor environments ... It supports keyword spotting (KWS) for 16 compound smart-home voice commands ... plus a background noise class for rejection training.
transfer_ivn: Treat spoken Darija command tokens as in-vehicle voice-control utterances and use the KWS pipeline for hands-free IVN actuation (e.g., climate, lighting, door lock), with noise class mapped to road/cabin noise rejection.
transfer_risk: Dialectal Darija phonetics, vocabulary, and compound morphology differ from in-vehicle command grammars and languages, so the trained model may not transfer without new in-cabin recordings and domain adaptation.
