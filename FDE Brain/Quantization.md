---
type: concept
status: evergreen
aliases:
  - Quantization
  - Low-bit quantization
tags:
  - ai-engineering
  - model-optimization
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/164-summary.md
    locator: pages 471-472
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Model-level techniques include model-agnostic techniques like quantization...
created: 2026-05-26T21:55:46.495345+00:00
updated: 2026-05-26T21:55:46.495345+00:00
ingestion_run: 8d527d59
---

# Quantization

## Summary

A model-level optimization technique that reduces the precision of model weights and activations (e.g., from 32-bit floating point to 8-bit integers), significantly reducing memory footprint and computational requirements.

## Core Idea

Quantization makes models cheaper and faster to run by reducing the data size, making it a generally applicable technique across many model types.

## Practical Use

When deploying a model on resource-constrained edge devices or when cost per inference is a major concern, quantize the model first. Always benchmark the quantized model against the original to check for performance degradation.

## Related

- [[Inference-Optimization-Techniques|Inference Optimization Techniques]]
