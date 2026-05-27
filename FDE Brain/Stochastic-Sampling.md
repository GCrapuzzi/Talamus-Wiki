---
type: method
status: evergreen
aliases:
  - Stochastic Sampling
  - Temperature Sampling
  - Top-K/Top-P Sampling
tags:
  - llm-deployment
  - sampling
  - generation
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/049-sampling-fundamentals.md
    locator: pages 112-113
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Instead of always picking the next most likely token, the model can sample the next token according to the probability distribution over all possible values.
created: 2026-05-26T21:55:45.572556+00:00
updated: 2026-05-26T21:55:45.572556+00:00
ingestion_run: 8d527d59
---

# Stochastic Sampling

## Summary

Generating model outputs by sampling the next token according to the full probability distribution, rather than always selecting the most likely token.

## Core Idea

Unlike deterministic methods, stochastic sampling introduces controlled randomness, preventing the model from generating repetitive or 'boring' outputs while still maintaining coherence based on probability weights.

## Practical Use

When deploying an LLM for creative tasks (e.g., content generation, brainstorming, code completion), use stochastic sampling to increase diversity and robustness. Adjusting parameters (like temperature) controls the level of randomness vs. adherence to the mean.

## Related

- [[Greedy-Sampling|Greedy Sampling]]
- [[Logit-Vector|Logit Vector]]
