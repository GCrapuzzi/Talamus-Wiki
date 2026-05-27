---
type: pattern
status: evergreen
aliases:
  - Gradient Checkpointing (Activation Recomputation)
  - Activation Recomputation
  - Memory-Time Tradeoff
tags:
  - ai-engineering
  - optimization
  - memory-management
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/131-memory-math.md
    locator: pages 346-348
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - One way to reduce the memory needed for activations is not to store them. Instead of storing activations for reuse, you recompute activations when necessary. This technique is called gradient checkpointing or activation recomputation.
      - While this reduces the memory requirements, it increases the time needed for training due to the recomputation.
created: 2026-05-26T21:55:46.226593+00:00
updated: 2026-05-26T21:55:46.226593+00:00
ingestion_run: 8d527d59
---

# Gradient Checkpointing (Activation Recomputation)

## Summary

A memory optimization technique that avoids storing all intermediate activation values during the forward pass. Instead, these values are recomputed only when needed during the backward pass.

## Core Idea

By sacrificing computational time (re-running parts of the forward pass) to save memory, this technique drastically reduces the memory bottleneck caused by storing large activation tensors, especially in deep transformer models.

## Practical Use

When training models with extremely large batch sizes or deep architectures where activation memory is the primary bottleneck, implement gradient checkpointing to reduce VRAM usage, accepting a corresponding increase in training time.

## Related

- [[Training-Memory-Calculation|Training Memory Calculation]]
- [[Model-Memory-Footprint-Analysis|Model Memory Footprint Analysis]]
