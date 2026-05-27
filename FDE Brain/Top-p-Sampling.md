---
type: method
status: evergreen
aliases:
  - Top-p Sampling
  - Nucleus Sampling
tags:
  - ai-engineering
  - llm-sampling
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/050-sampling-strategies.md
    locator: pages 114-119
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - In top-k sampling, the number of values considered is fixed to k. However, this number should change depending on the situation.
created: 2026-05-26T21:55:45.587001+00:00
updated: 2026-05-26T21:55:45.587001+00:00
ingestion_run: 8d527d59
---

# Top-p Sampling

## Summary

A dynamic sampling strategy that restricts the vocabulary to the smallest set of tokens whose cumulative probability exceeds a threshold $p$.

## Core Idea

Unlike Top-k, which uses a fixed number of tokens ($k$), Top-p adapts the size of the candidate set based on the probability distribution itself. This ensures that the model considers a narrow set of tokens when the distribution is sharp (predictable) and a wider set when the distribution is flat (creative).

## Practical Use

Use Top-p for general-purpose generation where the optimal number of candidate tokens changes based on the context. It is often preferred over Top-k because it is adaptive.

## Related

- [[Top-k-Sampling|Top-k Sampling]]
- Sampling Strategies
