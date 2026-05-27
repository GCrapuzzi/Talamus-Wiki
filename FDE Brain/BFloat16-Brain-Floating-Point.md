---
type: glossary
status: evergreen
aliases:
  - BFloat16 (Brain Floating Point)
  - BF16
tags:
  - ai-engineering
  - data-types
  - hardware-optimization
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/132-numerical-representations.md
    locator: pages 349-351
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - BF16 was designed by Google to optimize AI performance on TPUs.
      - BF16 has more bits for range and fewer bits for precision. This allows BF16 to represent large values that are out-of-bound for FP16.
created: 2026-05-26T21:55:46.232138+00:00
updated: 2026-05-26T21:55:46.232138+00:00
ingestion_run: 8d527d59
---

# BFloat16 (Brain Floating Point)

## Summary

A 16-bit floating-point format designed by Google, characterized by having more bits dedicated to the exponent (range) and fewer bits dedicated to the significand (precision) compared to FP16.

## Core Idea

BF16 excels at representing a wider dynamic range of values, making it robust for training large models where activations can span a wide magnitude, even if it sacrifices some absolute precision compared to FP16.

## Practical Use

Use BF16 when training models that involve large dynamic ranges (e.g., deep transformers) and where maintaining numerical stability across different magnitudes is critical, even if the absolute precision is slightly lower than FP16.

## Related

- [[Floating-Point-Precision-Trade-offs|Floating Point Precision Trade-offs]]
- FP16
