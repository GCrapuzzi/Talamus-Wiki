---
type: glossary
tags: [finetuning, pre-training, model-training]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#data-quantity
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Ossification

A phenomenon where pre-training freezes model weights such that they resist adaptation during finetuning (Hernandez et al., 2021). The model's learned representations become rigid, making it harder for finetuning data to shift behavior.

Smaller models are more susceptible than larger models. When you have enough finetuning data (millions of examples), training from scratch may outperform finetuning a pre-trained model due to ossification.
