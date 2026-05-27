---
type: method
status: evergreen
aliases:
  - Speculative Decoding
  - Speculative Sampling
  - Parallel Decoding
tags:
  - ai-engineering
  - inference
  - optimization
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/162-model-optimization.md
    locator: pages 450-463
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Speculative decoding (also called speculative sampling) uses a faster but less powerful model to generate a sequence of tokens, which are then verified by the target model.
      - The target model verifies these K generated tokens in parallel.
      - Speculative decoding effectively turns the computation profile of decoding into that of prefilling.
created: 2026-05-26T21:55:46.478471+00:00
updated: 2026-05-26T21:55:46.478471+00:00
ingestion_run: 8d527d59
---

# Speculative Decoding

## Summary

An inference technique that uses a faster, less powerful 'draft model' to predict a sequence of tokens (K tokens). The main, target model then verifies this sequence in parallel, accepting the longest valid subsequence (j tokens).

## Core Idea

It transforms the computation profile of sequential, autoregressive decoding (which is slow and bandwidth-heavy) into a profile closer to parallel prefilling. This dramatically reduces latency by leveraging the fact that verification is parallelizable while generation is sequential.

## Practical Use

Implement speculative decoding when latency is the primary constraint for text generation. The process involves: 1) Draft model generates K tokens. 2) Target model verifies K tokens in parallel. 3) Target model accepts j tokens and generates the next token. This is most effective when the acceptance rate is high (e.g., code generation).

## Related

- Autoregressive Decoding
- [[Inference-Optimization-Hierarchy|Inference Optimization Hierarchy]]
