---
type: glossary
status: evergreen
aliases:
  - FP16 (Half Precision)
  - Half Precision
tags:
  - ai-engineering
  - data-types
  - optimization
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/132-numerical-representations.md
    locator: pages 349-351
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - FP16 uses 16 bits (2 bytes) and is called half precision.
      - FP32 and FP16 are more common.
created: 2026-05-26T21:55:46.233377+00:00
updated: 2026-05-26T21:55:46.233377+00:00
ingestion_run: 8d527d59
---

# FP16 (Half Precision)

## Summary

A 16-bit floating-point format adhering to IEEE 754, offering a significant reduction in memory footprint compared to FP32, making it highly popular for inference and certain training stages.

## Core Idea

FP16 provides excellent memory efficiency and computational speedup on specialized hardware. However, its limited range and precision can lead to overflow or underflow errors if not managed correctly.

## Practical Use

Use FP16 for inference or model deployment where memory bandwidth is a primary bottleneck, and the model's weights and activations are known to operate within a manageable dynamic range.

## Related

- [[Floating-Point-Precision-Trade-offs|Floating Point Precision Trade-offs]]
- BF16
