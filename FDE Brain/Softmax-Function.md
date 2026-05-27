---
type: method
status: evergreen
aliases:
  - Softmax Function
  - logit to probability conversion
tags:
  - ai-engineering
  - llm-math
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/050-sampling-strategies.md
    locator: pages 114-119
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - To convert logits to probabilities, a softmax layer is often used.
      - "The probability for the $i^{th}$ token, $p_i$, is computed as follows: $p_i = \\text{softmax}(x_i) = \\frac{e^{x_i}}{\\sum_j e^{x_j}}$"
created: 2026-05-26T21:55:45.581663+00:00
updated: 2026-05-26T21:55:45.581663+00:00
ingestion_run: 8d527d59
---

# Softmax Function

## Summary

A mathematical function used to convert a vector of raw model outputs (logits) into a probability distribution where all values are between 0 and 1 and sum to 1.

## Core Idea

Logits are raw, unnormalized scores that can be negative and do not sum to one. Softmax normalizes these logits into a valid probability distribution, $p_i = \frac{e^{x_i}}{\sum_j e^{x_j}}$, making them suitable for sampling.

## Practical Use

When implementing custom sampling or evaluating model outputs, use softmax to normalize raw logits into interpretable probabilities. This is the foundational step before any sampling strategy (like temperature adjustment) is applied.

## Related

- [[Temperature-Sampling|Temperature Sampling]]
- Logprobs
