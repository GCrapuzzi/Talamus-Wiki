---
type: glossary
status: evergreen
aliases:
  - Cross Entropy
  - LLM Loss Function
  - Negative Log-Likelihood (NLL)
tags:
  - ai-engineering
  - llm-evaluation
  - loss-function
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/059-cross-entropy.md
    locator: pages 144-144
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - A language model’s cross entropy on a dataset measures how difficult it is for the language model to predict what comes next in this dataset.
      - Cross entropy depends on the training data’s predictability (Entropy) and how the model's distribution diverges from the true distribution (KL Divergence).
created: 2026-05-26T21:55:45.654715+00:00
updated: 2026-05-26T21:55:45.654715+00:00
ingestion_run: 8d527d59
---

# Cross Entropy

## Summary

A metric used to evaluate how well a language model's predicted probability distribution (Q) matches the true probability distribution (P) of the training data. It measures the average number of bits needed to encode the true data using the model's predicted distribution.

## Core Idea

Cross Entropy quantifies the difficulty of predicting the next token in a sequence. Minimizing this value during training forces the language model to adjust its learned distribution (Q) to closely approximate the true underlying data distribution (P).

## Practical Use

1. **Training Objective:** Used as the primary loss function during LLM training (optimization objective). 2. **Evaluation:** Provides a quantitative measure of model performance; a lower cross entropy indicates better alignment with the true data distribution. 3. **Diagnosis:** Helps diagnose if the model is failing to capture the true statistical properties of the data.

## Related

- Entropy
- Kullback–Leibler (KL) Divergence
- Negative Log-Likelihood
