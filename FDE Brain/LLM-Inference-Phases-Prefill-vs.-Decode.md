---
type: method
status: evergreen
aliases:
  - LLM Inference Phases (Prefill vs. Decode)
  - Transformer Inference Stages
  - Autoregressive Decoding Stages
tags:
  - ai-engineering
  - llm
  - inference
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/158-inference-overview.md
    locator: pages 430-435
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Prefilling... is limited by the number of operations your hardware can execute in a given time. Therefore, prefilling is compute-bound.
      - Decode... is limited by how quickly your hardware can load data into memory. Decoding is, therefore, memory bandwidth-bound.
created: 2026-05-26T21:55:46.439982+00:00
updated: 2026-05-26T21:55:46.439982+00:00
ingestion_run: 8d527d59
---

# LLM Inference Phases (Prefill vs. Decode)

## Summary

The two distinct computational phases of running a transformer-based language model: Prefill (parallel processing of input tokens) and Decode (sequential generation of output tokens).

## Core Idea

These two phases have fundamentally different computational profiles, leading to different bottlenecks. Prefilling is typically compute-bound, while Decoding is typically memory bandwidth-bound. Recognizing this difference allows for specialized optimization and decoupling of the stages.

## Practical Use

When optimizing an LLM, treat the prefill and decode stages separately. For long context inputs, the memory bandwidth bottleneck of the prefill stage must be addressed, often requiring techniques like KV cache optimization or specialized hardware.

## Related

- [[Computational-Bottlenecks|Computational Bottlenecks]]
- Context Length Optimization
