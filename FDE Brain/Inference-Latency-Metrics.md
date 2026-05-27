---
type: glossary
status: evergreen
aliases:
  - Inference Latency Metrics
  - LLM latency metrics
  - streaming latency
tags:
  - ai-engineering
  - llm-optimization
  - performance-metrics
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/159-inference-performance-metrics.md
    locator: pages 436-442
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Latency measures the time from when users send a query until they receive the complete response.
      - For autoregressive generation, especially in the streaming mode, the overall latency can be broken into several metrics.
created: 2026-05-26T21:55:46.443908+00:00
updated: 2026-05-26T21:55:46.443908+00:00
ingestion_run: 8d527d59
---

# Inference Latency Metrics

## Summary

A set of metrics used to quantify the time taken for an LLM to generate a response, crucial for optimizing user experience.

## Core Idea

Latency is the primary user-facing metric. For autoregressive generation, total latency is broken down into components (TTFT, TPOT) to diagnose bottlenecks and optimize the user experience.

## Practical Use

When diagnosing slow LLM performance, break down the total latency into TTFT and TPOT. If TTFT is high, focus on prefill optimization; if TPOT is high, focus on decoding/generation optimization.

## Related

- [[Time-to-First-Token-TTFT|Time to First Token (TTFT)]]
- [[Time-Per-Output-Token-TPOT|Time Per Output Token (TPOT)]]
- [[Total-Latency-Calculation|Total Latency Calculation]]
