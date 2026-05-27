---
type: concept
status: evergreen
aliases:
  - Cross-Entropy Loss
  - Cross-Entropy
  - Negative Log-Likelihood
tags:
  - ai-engineering
  - llm-training
  - metrics
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/057-understanding-language-modeling-metrics.md
    locator: pages 142-142
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Most autoregressive language models are trained using cross entropy or its relative, perplexity.
created: 2026-05-26T21:55:45.647028+00:00
updated: 2026-05-26T21:55:45.647028+00:00
ingestion_run: 8d527d59
---

# Cross-Entropy Loss

## Summary

A loss function used in training autoregressive language models. It measures the difference between the predicted probability distribution and the true probability distribution (the ground truth).

## Core Idea

Minimizing cross-entropy loss is the primary objective function for training LMs, as it forces the model to assign high probability to the correct next token in a sequence.

## Practical Use

When reviewing model training reports, understanding that the goal is to minimize cross-entropy loss helps interpret the model's optimization objective. It is the fundamental metric guiding LM development.

## Related

- [[Perplexity-PPL|Perplexity (PPL)]]
- [[Language-Modeling-Metrics|Language Modeling Metrics]]
