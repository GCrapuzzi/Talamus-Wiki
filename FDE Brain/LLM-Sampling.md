---
type: method
status: evergreen
aliases:
  - LLM Sampling
  - Output Sampling
  - Decoding Strategy
tags:
  - ai-engineering
  - llm-fundamentals
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/048-sampling.md
    locator: pages 112-112
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - A model constructs its outputs through a process known as sampling.
      - This section discusses different sampling strategies and sampling variables, including temperature, top-k, and top-p.
created: 2026-05-26T21:55:45.568501+00:00
updated: 2026-05-26T21:55:45.568501+00:00
ingestion_run: 8d527d59
---

# LLM Sampling

## Summary

The process by which a neural network constructs an output sequence by selecting tokens probabilistically from the vocabulary, rather than simply choosing the single most likely token (greedy decoding).

## Core Idea

Sampling introduces controlled randomness, allowing the model to explore diverse and creative outputs. Understanding the sampling variables (temperature, top-k, top-p) is crucial for balancing coherence (low randomness) and creativity (high randomness).

## Practical Use

When fine-tuning or deploying a model, adjust the sampling parameters based on the task: use low temperature/top-p for factual extraction or classification, and higher values for creative writing or brainstorming.

## Related

- Temperature Parameter
- Top-K Sampling
- Top-P Sampling
