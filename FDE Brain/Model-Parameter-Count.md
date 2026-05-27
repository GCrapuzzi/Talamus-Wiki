---
type: glossary
status: evergreen
aliases:
  - Model Parameter Count
  - Model Size
  - Number of Parameters
tags:
  - ai-engineering
  - foundation-models
  - model-architecture
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/044-model-size.md
    locator: pages 91-101
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - The number of parameters is usually appended at the end of a model name.
      - In general, increasing a model’s parameters increases its capacity to learn, resulting in better models.
created: 2026-05-26T21:55:45.534580+00:00
updated: 2026-05-26T21:55:45.534580+00:00
ingestion_run: 8d527d59
---

# Model Parameter Count

## Summary

The total count of trainable weights (parameters) in a neural network model, often used as a primary metric for model capacity and scale.

## Core Idea

Generally, increasing the number of parameters within a model family increases its capacity to learn, leading to better performance. However, parameter count alone is insufficient for performance prediction.

## Practical Use

Use this metric to estimate the baseline memory requirements for inference (e.g., 7B parameters * 2 bytes/parameter = 14 GB). Always cross-reference with data quality and compute requirements.

## Related

- Sparsity
- [[Mixture-of-Experts-MoE|Mixture-of-Experts (MoE)]]
- Training Data Scale
