---
type: glossary
status: evergreen
aliases:
  - Transformer Architecture Bottlenecks
  - LLM Resource Constraints
  - Autoregressive Inference Challenges
tags:
  - ai-engineering
  - llm
  - transformer
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/161-inference-optimization.md
    locator: pages 450-450
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - "Foundation models... have three characteristics that make inference resource-intensive: model size, autoregressive decoding, and the attention mechanism."
created: 2026-05-26T21:55:46.469557+00:00
updated: 2026-05-26T21:55:46.469557+00:00
ingestion_run: 8d527d59
---

# Transformer Architecture Bottlenecks

## Summary

The three primary components of modern foundation models (Transformer-based LLMs) that contribute significantly to high inference resource consumption.

## Core Idea

Understanding these bottlenecks (size, decoding, attention) is necessary for targeted optimization efforts, as they dictate where computational resources are most heavily utilized during inference.

## Practical Use

When profiling an LLM, identify which of these three components is the primary bottleneck. If it's the attention mechanism, focus on sparse attention methods; if it's size, focus on quantization or distillation.

## Related

- [[Model-Optimization|Model Optimization]]
- [[Attention-Mechanism|Attention Mechanism]]
- Autoregressive Decoding
