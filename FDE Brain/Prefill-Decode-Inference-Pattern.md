---
type: pattern
status: evergreen
aliases:
  - Prefill/Decode Inference Pattern
  - Parallel/Sequential Inference
  - LLM generation stages
tags:
  - ai-engineering
  - deployment
  - optimization
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/043-model-architecture.md
    locator: pages 82-90
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - "Inference for transformer-based language models, therefore, consists of two steps: Prefill... Decode..."
      - The model processes the input tokens in parallel. This step creates the intermediate state necessary to generate the first output token.
      - The model generates one output token at a time.
created: 2026-05-26T21:55:45.531802+00:00
updated: 2026-05-26T21:55:45.531802+00:00
ingestion_run: 8d527d59
---

# Prefill/Decode Inference Pattern

## Summary

The two-stage process for generating text using transformer-based autoregressive language models: Prefill (parallel input processing) followed by Decode (sequential token generation).

## Core Idea

The Transformer's ability to process input tokens in parallel (Prefill) is combined with the inherent sequential nature of generating one token at a time (Decode). Optimizing both stages is key to efficient LLM deployment.

## Practical Use

When optimizing LLM serving infrastructure, engineers must implement KV caching during the Decode phase and ensure the Prefill phase maximizes GPU utilization by processing the entire prompt context in parallel.

## Related

- [[Transformer-Architecture|Transformer Architecture]]
- KV Caching
