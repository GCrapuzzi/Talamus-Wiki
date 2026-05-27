---
type: concept
status: evergreen
aliases:
  - Cross Entropy (H(P, Q))
  - Cross-Entropy Loss
tags:
  - llm-metrics
  - training-loss
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/061-perplexity.md
    locator: pages 145-145
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - A language model is trained to minimize its cross entropy with respect to the training data.
      - Cross entropy tells us how efficient a language model will be at compressing text.
created: 2026-05-26T21:55:45.664158+00:00
updated: 2026-05-26T21:55:45.664158+00:00
ingestion_run: 8d527d59
---

# Cross Entropy (H(P, Q))

## Summary

A metric quantifying the difference between a true probability distribution (P) and a predicted distribution (Q). Language models are trained to minimize this value.

## Core Idea

Cross entropy measures the average number of bits required to encode data from the true distribution P using the code optimized for the predicted distribution Q. Minimizing H(P, Q) means the model's predictions (Q) are closely approximating the true data distribution (P).

## Practical Use

Used as the primary loss function during language model training. Engineers use it to evaluate model performance on held-out validation sets, aiming for the lowest possible value.

## Related

- Perplexity
- Entropy
