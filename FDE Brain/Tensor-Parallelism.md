---
type: pattern
status: evergreen
aliases:
  - Tensor Parallelism
  - Model sharding
  - Weight splitting
tags:
  - ai-engineering
  - parallelism
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/164-summary.md
    locator: pages 471-472
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - tensor parallelism (which both reduces latency and enables serving larger models)
created: 2026-05-26T21:55:46.499355+00:00
updated: 2026-05-26T21:55:46.499355+00:00
ingestion_run: 8d527d59
---

# Tensor Parallelism

## Summary

A pattern that splits the computation (e.g., matrix multiplications) of a single model layer across multiple devices, allowing the serving of models that are too large to fit on a single accelerator.

## Core Idea

It is crucial for enabling the serving of extremely large models (e.g., trillion-parameter models) and significantly reduces latency by distributing the computational load.

## Practical Use

Use tensor parallelism when deploying state-of-the-art, massive models that exceed the memory capacity of a single GPU. It is a key technique for reducing latency and enabling scale.

## Related

- [[Inference-Optimization-Techniques|Inference Optimization Techniques]]
