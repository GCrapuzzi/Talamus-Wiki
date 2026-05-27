---
type: method
status: evergreen
aliases:
  - Training Memory Calculation
  - LLM Training Memory Budgeting
  - Backward Pass Memory Estimate
tags:
  - ai-engineering
  - training
  - optimization
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/131-memory-math.md
    locator: pages 346-348
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Training memory = model weights + activations + gradients + optimizer states
      - A vanilla SGD optimizer has no state.
      - An Adam optimizer stores two values per trainable parameter.
created: 2026-05-26T21:55:46.225106+00:00
updated: 2026-05-26T21:55:46.225106+00:00
ingestion_run: 8d527d59
---

# Training Memory Calculation

## Summary

Calculates the total memory required during the training phase, which includes weights, activations, gradients, and optimizer states.

## Core Idea

Training memory is additive: Weights + Activations + Gradients + Optimizer States. The memory for gradients and optimizer states scales linearly with the number of trainable parameters (N). Activations often represent the largest, most variable component.

## Practical Use

When scaling up training, calculate the memory for the optimizer states first, as this often dictates the minimum required memory. For example, using Adam requires 2 states per parameter, significantly increasing the memory overhead compared to SGD.

## Related

- Gradient Checkpointing
- [[Model-Memory-Footprint-Analysis|Model Memory Footprint Analysis]]
