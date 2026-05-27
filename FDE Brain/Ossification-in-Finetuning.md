---
type: glossary
status: evergreen
aliases:
  - Ossification in Finetuning
  - Model Weight Freezing
  - Pretraining Overfitting
tags:
  - ai-engineering
  - llm-theory
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/143-data-quantity.md
    locator: pages 396-400
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - This is due to a phenomenon called ossification, where pre-training can ossify (i.e., freeze) the model weights so that they don’t adapt as well to the finetuning data.
created: 2026-05-26T21:55:46.339206+00:00
updated: 2026-05-26T21:55:46.339206+00:00
ingestion_run: 8d527d59
---

# Ossification in Finetuning

## Summary

A phenomenon where extensive pre-training or finetuning can 'freeze' the model weights, making the model less adaptable or resistant to learning new, specific patterns during subsequent finetuning stages.

## Core Idea

While pre-training is necessary, excessive or poorly managed pre-training can limit the model's plasticity. Smaller models are noted to be more susceptible to this effect than larger, more robust models.

## Practical Use

If finetuning fails to improve performance, consider if the base model has been over-trained or if the finetuning process is causing weight ossification. This suggests a need for careful hyperparameter tuning or a different finetuning technique.

## Related

- [[Data-Scaling-and-Finetuning-Strategy|Data Scaling and Finetuning Strategy]]
- Hyperparameter Tuning
