---
type: glossary
status: evergreen
aliases:
  - Time to First Token (TTFT)
  - Time to first token
  - Prefill time
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
      - TTFT measures how quickly the first token is generated after users send a query.
      - It corresponds to the duration of the prefill step and depends on the input’s length.
created: 2026-05-26T21:55:46.445220+00:00
updated: 2026-05-26T21:55:46.445220+00:00
ingestion_run: 8d527d59
---

# Time to First Token (TTFT)

## Summary

The time elapsed between sending a query and receiving the very first generated token. It corresponds to the duration of the prefill step.

## Core Idea

TTFT is highly dependent on the input prompt length. For conversational applications, TTFT should be near-instantaneous, as user expectations are high.

## Practical Use

If TTFT is poor, investigate the prefill stage. Techniques like prompt caching can mitigate this by reusing system prompts.

## Related

- [[Total-Latency-Calculation|Total Latency Calculation]]
- Prompt Caching
