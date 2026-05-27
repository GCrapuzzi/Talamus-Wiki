---
type: concept
status: evergreen
aliases:
  - Autoregressive Decoding Bottleneck
  - Sequential Token Generation
  - Autoregressive Latency
tags:
  - ai-engineering
  - llm-architecture
  - latency
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/162-model-optimization.md
    locator: pages 450-463
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Each token generation step necessitates the transfer of the entire model’s parameters from the accelerator’s high-bandwidth memory to its compute units.
      - Because the model can produce only one token at a time, the process consumes only a small number of FLOP/s, resulting in computational inefficiency.
created: 2026-05-26T21:55:46.480715+00:00
updated: 2026-05-26T21:55:46.480715+00:00
ingestion_run: 8d527d59
---

# Autoregressive Decoding Bottleneck

## Summary

The inherent limitation in language models where each output token must be generated sequentially, requiring the entire model's parameters to be transferred for every single step. This process is computationally inefficient and bandwidth-heavy.

## Core Idea

Because generation is sequential (one token at a time), the process is slow and expensive. This bottleneck is the primary target for advanced inference optimization techniques like Speculative Decoding.

## Practical Use

When benchmarking model performance, identify the 'time per token' metric. If this metric is high, the bottleneck is likely autoregressive decoding. Solutions must focus on parallelizing or predicting multiple tokens simultaneously.

## Related

- [[Speculative-Decoding|Speculative Decoding]]
- [[Inference-Optimization-Hierarchy|Inference Optimization Hierarchy]]
