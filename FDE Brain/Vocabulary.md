---
type: concept
status: evergreen
aliases:
  - Vocabulary
  - Model Vocabulary
tags:
  - ai-engineering
  - llm
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/016-from-language-models-to-large-language-models.md
    locator: pages 26-31
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - The set of all tokens a model can work with is the model’s vocabulary.
created: 2026-05-26T21:55:45.332687+00:00
updated: 2026-05-26T21:55:45.332687+00:00
ingestion_run: 8d527d59
---

# Vocabulary

## Summary

The finite set of all unique tokens that a specific language model is trained to recognize and work with.

## Core Idea

The vocabulary size dictates the model's capacity to represent language. By using a vocabulary, the model can construct a large number of distinct words using a limited set of tokens, improving efficiency.

## Practical Use

When designing or fine-tuning a model, understanding the vocabulary size and the tokenization method is crucial for managing memory and ensuring that domain-specific terminology is handled efficiently.

## Related

- [[Tokenization|Tokenization]]
- [[Language-Model-LM|Language Model (LM)]]
