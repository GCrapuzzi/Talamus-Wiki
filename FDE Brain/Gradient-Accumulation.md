---
type: concept
status: evergreen
aliases:
  - Gradient Accumulation
  - Gradient Aggregation
tags:
  - ai-engineering
  - optimization
  - training
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/137-finetuning-tactics.md
    locator: pages 381-384
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Gradient accumulation updates the model weights once enough reliable gradients are accumulated, rather than after each batch.
created: 2026-05-26T21:55:46.275439+00:00
updated: 2026-05-26T21:55:46.275439+00:00
ingestion_run: 8d527d59
---

# Gradient Accumulation

## Summary

A technique used in deep learning training where gradients are computed and accumulated across multiple small batches before a single weight update is performed.

## Core Idea

It allows simulating the effect of a large batch size (leading to stable updates) even when hardware constraints (memory) force the use of small physical batch sizes.

## Practical Use

When training large models on limited GPU memory, implement gradient accumulation to maintain stable model weight updates without increasing the physical batch size.

## Related

- Batch Size
- Distributed Training
