---
type: pattern
status: evergreen
aliases:
  - Prefill/Decode Decoupling
  - DistServe
  - Inference Without Interference
tags:
  - ai-engineering
  - llm-serving
  - optimization
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/163-inference-service-optimization.md
    locator: pages 464-470
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Prefill is compute-bound and decode is memory bandwidth-bound, using the same machine to perform both can cause them to inefficiently compete for resources.
      - Assigning prefill and decode operations to different instances... can significantly improve the volume of processed requests while adhering to latency requirements.
created: 2026-05-26T21:55:46.486976+00:00
updated: 2026-05-26T21:55:46.486976+00:00
ingestion_run: 8d527d59
---

# Prefill/Decode Decoupling

## Summary

Separating the LLM inference process into two distinct stages—Prefill (input processing) and Decode (token generation)—and running them on separate hardware instances (e.g., different GPUs).

## Core Idea

Prefill is compute-bound, and Decode is memory bandwidth-bound. Running both on the same device causes resource contention, slowing down both Time-to-First-Token (TTFT) and Time-Per-Output-Token (TPOT). Decoupling allows each stage to operate optimally on hardware suited to its bottleneck.

## Practical Use

Implement this when serving high-volume LLM workloads. The optimal ratio of prefill to decode instances depends on the workload: use a higher prefill ratio (e.g., 2:1 to 4:1) for long input sequences prioritizing TTFT, and a higher decode ratio (e.g., 1:2 to 1:1.25) for short inputs prioritizing TPOT.

## Related

- Prompt Caching
- LLM Inference Lifecycle
