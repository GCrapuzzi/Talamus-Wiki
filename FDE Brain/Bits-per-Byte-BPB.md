---
type: metric
status: evergreen
aliases:
  - Bits-per-Byte (BPB)
  - Byte Efficiency Metric
tags:
  - llm-metrics
  - compression
  - data-efficiency
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/060-bits-per-character-and-bits-per-byte.md
    locator: pages 145-145
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - A more standardized metric would be bits-per-byte (BPB), the number of bits a language model needs to represent one byte of the original training data.
created: 2026-05-26T21:55:45.658114+00:00
updated: 2026-05-26T21:55:45.658114+00:00
ingestion_run: 8d527d59
---

# Bits-per-Byte (BPB)

## Summary

A standardized metric representing the number of bits a language model requires to encode one byte of the original training data. It normalizes model efficiency against the fundamental unit of data storage (8 bits).

## Core Idea

BPB provides a robust, comparable measure of compression efficiency. By normalizing against the byte, it mitigates the variability introduced by different tokenization methods and character encoding schemes (like UTF-8).

## Practical Use

Used to compare the theoretical compression capability of different LLMs. If a model has a BPB of 3.43, it means it can represent 8 bits of original data using only 3.43 bits, indicating significant compression potential.

## Related

- [[Bits-per-Character-BPC|Bits-per-Character (BPC)]]
- Entropy
