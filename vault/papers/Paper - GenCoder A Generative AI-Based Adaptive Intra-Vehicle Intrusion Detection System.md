---
title: "GenCoder: A Generative AI-Based Adaptive Intra-Vehicle Intrusion Detection System"
year: 2024
doi: "https://doi.org/10.1109/access.2024.3476177"
relevance_score: 10.0
type: paper
---
# GenCoder: A Generative AI-Based Adaptive Intra-Vehicle Intrusion Detection System

Novelty

          * Introduces GenCoder, a generative AI-based adaptive intra-vehicular IDS: a variational autoencoder (VAE) generates new training data when traffic deviates from known patterns, letting the detector evolve with emerging threats instead of remaining static.
          * Proposes the novel "GenCoder layer," a dedicated communication layer coordinating the DNN, the VAE, and the dataset.
          * Introduces adaptability-focused evaluation strategies, including feature-deformation robustness testing and Shannon entropy analysis of synthetic samples (1.65 bits across four classes).

        Methodology

          * Architecture: a five-layer deep neural network (DNN) combined with a VAE, orchestrated by the GenCoder communication layer.
          * Adaptation loop: detection of deviations from known intrusion patterns triggers synthetic data generation, which is fed back for retraining to capture new threat variants.
          * Evaluation: accuracy, precision, recall, and F1-score improve from 84.79%/83.58%/83.70%/83.64% to 92.19%/90.12%/90.44%/90.28% after 50% feature deformation of testing data; Shannon entropy quantifies diversity of generated samples.

        Explicit Limitations

          * None explicitly stated in the abstract; no constraints on datasets, computation cost, or real-world deployment are reported there.

        Future Work

          * Not explicitly stated in the abstract; the authors position the work as opening "a new dimension in automotive IDS research," implying continued development of adaptive, generative-AI-driven vehicular intrusion detection.

        Concept Hubs

          * [[Concept - Deep Learning Intrusion Detection]]
          * [[Concept - In-Vehicle Network Security]]
          * [[Concept - CAN Network Anomaly Detection]]
          * [[Concept - Generative Adaptive Detection]]

        Relevance Score

        10/10 — Directly applies deep learning (DNN + VAE) to intra-vehicular network intrusion detection, matching the thesis focus on deep learning for in-vehicle networks.
