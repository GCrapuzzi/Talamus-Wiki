---
type: glossary
status: evergreen
aliases:
  - Time Per Output Token (TPOT)
  - Inter-token latency (ITL)
  - Time between tokens (TBT)
tags:
  - ai-engineering
  - llm-optimization
  - latency
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/159-inference-performance-metrics.md
    locator: pages 436-442
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - TPOT measures how quickly each output token is generated after the first token.
      - The total latency will equal TTFT + TPOT × (number of output tokens).
created: 2026-05-26T21:55:46.447551+00:00
updated: 2026-05-26T21:55:46.447551+00:00
ingestion_run: 8d527d59
---

# Time Per Output Token (TPOT)

## Summary

The average time taken to generate each subsequent output token after the first token has been received. This measures the efficiency of the decoding process.

## Core Idea

TPOT is critical for the perceived smoothness of the response. While fast, it does not need to be faster than human reading speed, but consistency is key.

## Practical Use

If TPOT is high, the decoding process is the bottleneck. Optimization efforts should focus on efficient generation algorithms and hardware utilization during decoding.

## Related

- [[Total-Latency-Calculation|Total Latency Calculation]]
- Throughput
