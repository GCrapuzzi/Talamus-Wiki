---
type: metric
status: evergreen
aliases:
  - Perplexity (PPL)
  - PPL
tags:
  - llm-metrics
  - evaluation
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/061-perplexity.md
    locator: pages 145-145
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Perplexity is the exponential of entropy and cross entropy.
      - "Given a dataset with the true distribution P, its perplexity is defined as: PPL (P) = 2H (P )"
created: 2026-05-26T21:55:45.666123+00:00
updated: 2026-05-26T21:55:45.666123+00:00
ingestion_run: 8d527d59
---

# Perplexity (PPL)

## Summary

The exponential of the model's entropy or cross entropy. It serves as a measure of how well a language model predicts a given sample; lower values indicate better performance.

## Core Idea

Perplexity can be interpreted as the weighted average number of choices the model has for the next token. A PPL of 100 means the model is, on average, as confused as if it were choosing uniformly among 100 options.

## Practical Use

Used for benchmarking and comparing different LLMs or model versions on standardized datasets. A decrease in PPL generally indicates an improvement in the model's ability to capture the underlying data distribution.

## Related

- [[Cross-Entropy-H-P-Q|Cross Entropy (H(P, Q))]]
- Entropy
