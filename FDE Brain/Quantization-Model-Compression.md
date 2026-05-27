---
type: glossary
status: evergreen
aliases:
  - Quantization (Model Compression)
  - Precision Reduction
  - Low-bit representation
tags:
  - ai-engineering
  - model-compression
  - optimization
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/133-quantization.md
    locator: pages 352-355
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - The fewer bits needed to represent a model’s values, the lower the model’s memory footprint will be.
      - Reducing precision, also known as quantization, is a cheap and extremely effective way to reduce a model’s memory footprint.
      - In the context of ML, low precision generally refers to any format with fewer bits than the standard FP32.
created: 2026-05-26T21:55:46.237137+00:00
updated: 2026-05-26T21:55:46.237137+00:00
ingestion_run: 8d527d59
---

# Quantization (Model Compression)

## Summary

The process of reducing the number of bits required to represent a model's weights and activations (e.g., from FP32 to INT8 or FP16). This significantly reduces the model's memory footprint and often improves computation speed.

## Core Idea

By using fewer bits per parameter, the memory required to store the model weights is drastically reduced (e.g., 32-bit to 16-bit halves the size). This enables deployment on resource-constrained devices and allows for larger batch sizes.

## Practical Use

When deploying a large LLM or model to an edge device or a memory-limited environment, quantization is the primary technique used to fit the model into memory and accelerate inference. Engineers must select the appropriate target format (e.g., INT8, FP8, 4-bit) based on the target hardware and required performance.

## Related

- [[Mixed-Precision-Inference|Mixed Precision Inference]]
- [[Quantization-Aware-Training-QAT|Quantization-Aware Training (QAT)]]
- [[Post-Training-Quantization-PTQ|Post-Training Quantization (PTQ)]]
