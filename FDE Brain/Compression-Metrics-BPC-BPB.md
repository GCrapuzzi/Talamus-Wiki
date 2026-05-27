---
type: pattern
status: evergreen
aliases:
  - Compression Metrics (BPC/BPB)
  - Bits-per-Character
  - Bits-per-Byte
tags:
  - data-compression
  - llm-metrics
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/061-perplexity.md
    locator: pages 145-145
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - A more standardized metric would be bits-per-byte (BPB), the number of bits a language model needs to represent one byte of the original training data.
      - If the BPB of a language model is 3.43, meaning it can represent each original byte (8 bits) using 3.43 bits, this language model can compress the original training text to less than half the text’s original size.
created: 2026-05-26T21:55:45.668733+00:00
updated: 2026-05-26T21:55:45.668733+00:00
ingestion_run: 8d527d59
---

# Compression Metrics (BPC/BPB)

## Summary

Metrics used to quantify the compression efficiency of a language model. Bits-per-Byte (BPB) is the preferred standardized metric, representing the average number of bits needed to encode one byte of the original training data.

## Core Idea

These metrics translate the model's cross-entropy performance into a tangible measure of data compression. A lower BPB indicates higher compression efficiency, meaning the model can represent the original data using fewer bits.

## Practical Use

When comparing models trained with different tokenization schemes (e.g., word-based vs. character-based) or different character encodings (e.g., ASCII vs. UTF-8), BPB provides a standardized, comparable measure of efficiency.

## Related

- [[Cross-Entropy-H-P-Q|Cross Entropy (H(P, Q))]]
