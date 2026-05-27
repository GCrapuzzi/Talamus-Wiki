---
type: method
status: evergreen
aliases:
  - Sequence Parallelism
  - Operator splitting
tags:
  - ai-engineering
  - parallelism
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/164-summary.md
    locator: pages 471-472
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - In sequence parallelism , operators needed for the entire input are split across machines.
created: 2026-05-26T21:55:46.503413+00:00
updated: 2026-05-26T21:55:46.503413+00:00
ingestion_run: 8d527d59
---

# Sequence Parallelism

## Summary

A technique that splits the operators (computational components) needed for the entire input across multiple devices. Different devices handle different parts of the model's computation.

## Core Idea

It improves efficiency for long input processing by distributing the computational graph, rather than the input data itself.

## Practical Use

Use this when the computational complexity of the model (e.g., needing both attention and feedforward passes) is the bottleneck, allowing different stages of the model to run concurrently on different hardware.

## Related

- [[Context-Parallelism|Context Parallelism]]
