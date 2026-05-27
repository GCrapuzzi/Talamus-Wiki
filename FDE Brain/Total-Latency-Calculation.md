---
type: framework
status: evergreen
aliases:
  - Total Latency Calculation
  - End-to-end latency
tags:
  - ai-engineering
  - optimization-framework
  - latency
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/159-inference-performance-metrics.md
    locator: pages 436-442
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - The total latency will equal TTFT + TPOT × (number of output tokens).
created: 2026-05-26T21:55:46.449840+00:00
updated: 2026-05-26T21:55:46.449840+00:00
ingestion_run: 8d527d59
---

# Total Latency Calculation

## Summary

A formula used to estimate the total time a user waits for a complete LLM response.

## Core Idea

Total Latency = TTFT + (TPOT × Number of Output Tokens). Understanding this decomposition allows engineers to pinpoint whether the bottleneck is the initial prompt processing (TTFT) or the token generation rate (TPOT).

## Practical Use

When optimizing, if the goal is to reduce total latency, the trade-off between improving TTFT (via prefilling) and improving TPOT (via decoding) must be analyzed based on the expected output length.

## Related

- [[Time-to-First-Token-TTFT|Time to First Token (TTFT)]]
- [[Time-Per-Output-Token-TPOT|Time Per Output Token (TPOT)]]
