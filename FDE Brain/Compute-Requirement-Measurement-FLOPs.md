---
type: glossary
status: evergreen
aliases:
  - Compute Requirement Measurement (FLOPs)
  - Floating Point Operations
  - Computational Cost
tags:
  - ai-engineering
  - compute-optimization
  - hardware-acceleration
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/044-model-size.md
    locator: pages 91-101
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - A more standardized unit for a model’s compute requirement is FLOP, or floating point operation.
      - FLOP measures the number of floating point operations performed for a certain task.
      - FLOPs measure the compute requirement for a task, whereas FLOP/s measures a machine’s peak performance.
created: 2026-05-26T21:55:45.542183+00:00
updated: 2026-05-26T21:55:45.542183+00:00
ingestion_run: 8d527d59
---

# Compute Requirement Measurement (FLOPs)

## Summary

A standardized unit (FLOP) used to measure the total number of floating-point operations required to train or run a model. This is preferred over counting machine hours or specific hardware types.

## Core Idea

FLOP measures the intrinsic computational work required for a task (e.g., training a model). It is distinct from FLOP/s, which measures the peak performance of a specific machine (e.g., H100 GPU).

## Practical Use

To estimate the total compute budget for a project, calculate the required FLOPs. To estimate the time needed, divide the total FLOPs by the combined FLOP/s capacity of the available hardware cluster.

## Related

- FLOP/s vs FLOPs
- Model Training Compute
