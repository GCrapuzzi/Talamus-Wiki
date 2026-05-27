---
type: method
status: evergreen
aliases:
  - Pruning (Neural Networks)
  - Sparsity Induction
  - Weight Elimination
tags:
  - ai-engineering
  - optimization
  - sparsity
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/162-model-optimization.md
    locator: pages 450-463
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Another is to find parameters least useful to predictions and set them to zero.
      - This makes the model more sparse, which both reduces the model’s storage space and speeds up computation.
created: 2026-05-26T21:55:46.477280+00:00
updated: 2026-05-26T21:55:46.477280+00:00
ingestion_run: 8d527d59
---

# Pruning (Neural Networks)

## Summary

A technique that reduces model size and computation by identifying and removing (or setting to zero) the least useful parameters (weights) in a neural network. This results in a sparse model.

## Core Idea

By making the model sparse, computation can be optimized, reducing memory footprint and speeding up inference. Unlike quantization, pruning does not change the total number of parameters, only the number of non-zero ones.

## Practical Use

Use pruning when memory bandwidth is a major bottleneck and the model architecture is well understood. Note that pruning requires specialized hardware or frameworks designed to efficiently handle sparse matrix operations to realize performance gains.

## Related

- [[Model-Compression-Techniques|Model Compression Techniques]]
