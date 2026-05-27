---
type: method
status: evergreen
aliases:
  - Greedy Sampling
  - Most Likely Outcome Selection
tags:
  - llm-deployment
  - sampling
  - determinism
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/049-sampling-fundamentals.md
    locator: pages 112-113
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Always picking the most likely outcome = is called greedy sampling.
      - However, for a language model, greedy sampling creates boring outputs.
created: 2026-05-26T21:55:45.574293+00:00
updated: 2026-05-26T21:55:45.574293+00:00
ingestion_run: 8d527d59
---

# Greedy Sampling

## Summary

A deterministic method of token generation where the model always selects the token with the highest calculated probability at each step.

## Core Idea

Greedy sampling is simple and highly predictable, making it suitable for classification tasks where the highest probability outcome is desired (e.g., spam detection). However, for open-ended language generation, it often leads to repetitive or overly common outputs.

## Practical Use

Use greedy sampling when the task requires maximum determinism and minimal variation, such as structured data extraction or binary classification. Avoid it for creative or conversational AI applications.

## Related

- [[Stochastic-Sampling|Stochastic Sampling]]
- Classification Model
