---
type: concept
status: evergreen
aliases:
  - Entropy (Information Theory)
  - Shannon Entropy
  - Information Content
tags:
  - ai-engineering
  - information-theory
  - llm-evaluation
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/058-entropy.md
    locator: pages 143-143
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Entropy measures how much information, on average, a token carries.
      - The higher the entropy, the more information each token carries, and the more bits are needed to represent a token.
created: 2026-05-26T21:55:45.650633+00:00
updated: 2026-05-26T21:55:45.650633+00:00
ingestion_run: 8d527d59
---

# Entropy (Information Theory)

## Summary

A statistical parameter that measures the average amount of information, or uncertainty, carried by a token or symbol in a given source. Higher entropy indicates that each token carries more information and requires more bits for efficient representation.

## Core Idea

Entropy quantifies the minimum average number of bits required to encode information from a source. In language modeling, it measures the inherent unpredictability or information density of the language distribution. A lower entropy suggests a highly predictable, constrained language (e.g., binary code), while higher entropy suggests greater randomness or complexity.

## Practical Use

1. **Model Evaluation:** Used to understand the theoretical minimum loss achievable by a language model. A model's cross-entropy loss should ideally approach the true entropy of the data distribution. 2. **Data Compression/Efficiency:** Helps determine the theoretical limits of data compression for a given token set. 3. **Model Selection:** When comparing models, understanding the entropy helps determine if the model is capturing the true information density of the target domain, rather than just memorizing training patterns.

## Related

- Cross-Entropy
- Perplexity
- [[Language-Modeling-Metrics|Language Modeling Metrics]]
- Information Theory
