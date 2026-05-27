---
type: concept
status: evergreen
aliases:
  - Bits-per-Character (BPC) / Bits-per-Byte (BPB)
  - BPC
  - BPB
tags:
  - ai-engineering
  - llm-efficiency
  - metrics
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/057-understanding-language-modeling-metrics.md
    locator: pages 142-142
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - When reading papers and model reports, you might also come across bits-per-character (BPC) and bits-per-byte (BPB); both are variations of cross entropy.
created: 2026-05-26T21:55:45.649260+00:00
updated: 2026-05-26T21:55:45.649260+00:00
ingestion_run: 8d527d59
---

# Bits-per-Character (BPC) / Bits-per-Byte (BPB)

## Summary

Variations of cross-entropy used to quantify the average number of bits required to encode the model's output. They provide a measure of information density and model efficiency.

## Core Idea

These metrics offer a standardized, quantifiable way to measure the information content of the model's predictions, often used in model compression or efficiency benchmarking.

## Practical Use

When comparing models or evaluating model compression techniques, BPC/BPB provides a concrete metric for efficiency that goes beyond simple token counts.

## Related

- [[Cross-Entropy-Loss|Cross-Entropy Loss]]
- [[Language-Modeling-Metrics|Language Modeling Metrics]]
