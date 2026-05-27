---
type: glossary
status: evergreen
aliases:
  - Logit Vector
  - Unnormalized Logits
tags:
  - llm-architecture
  - tokenization
  - math-concepts
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/049-sampling-fundamentals.md
    locator: pages 112-113
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Given an input, a neural network outputs a logit vector. Each logit corresponds to one possible value.
      - In the case of a language model, each logit corresponds to one token in the model’s vocabulary.
created: 2026-05-26T21:55:45.576358+00:00
updated: 2026-05-26T21:55:45.576358+00:00
ingestion_run: 8d527d59
---

# Logit Vector

## Summary

The raw output vector from a neural network (specifically, the final layer) that represents the model's unnormalized scores for every possible token in its vocabulary.

## Core Idea

The logit vector is the foundational step in LLM output generation. These raw scores must be passed through a softmax function to convert them into a usable probability distribution (where all values sum to 1).

## Practical Use

When debugging or fine-tuning models, understanding the logit vector helps diagnose why the model might be biased toward certain tokens, even if the final probabilities seem balanced.

## Related

- Probability Distribution
- [[Softmax-Function|Softmax Function]]
