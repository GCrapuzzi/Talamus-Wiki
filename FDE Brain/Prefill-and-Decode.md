---
type: glossary
tags: [inference, prefill, decode, transformer, optimization]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#model-architecture
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Prefill and Decode

The two phases of inference in transformer-based autoregressive language models:

- **Prefill**: processes all input tokens in parallel. Creates intermediate state (KV vectors) needed to generate the first output token. Latency depends on input length but benefits from parallelism.
- **Decode**: generates output tokens one at a time, sequentially. Each new token is conditioned on all previous tokens (input + generated). This is the sequential bottleneck.

The distinction between these phases motivates many inference optimization techniques (see Chapter 9). Prefill is compute-bound; decode is memory-bandwidth-bound.
