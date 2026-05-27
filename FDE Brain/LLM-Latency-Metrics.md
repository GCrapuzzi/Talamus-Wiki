---
type: glossary
status: evergreen
aliases:
  - LLM Latency Metrics
  - Time to First Token (TTFT)
  - Time Per Token (TPT)
tags:
  - ai-engineering
  - performance
  - latency
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/081-cost-and-latency.md
    locator: pages 201-202
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - There are multiple metrics for latency for foundation models, including but not limited to time to first token, time per token, time between tokens, time per query, etc.
      - The more tokens it has to generate, the higher the total latency.
created: 2026-05-26T21:55:45.826707+00:00
updated: 2026-05-26T21:55:45.826707+00:00
ingestion_run: 8d527d59
---

# LLM Latency Metrics

## Summary

A set of metrics used to quantify the speed of an autoregressive language model's output. Understanding the difference between these metrics is crucial for optimizing user experience.

## Core Idea

Latency is not a single number. TTFT measures perceived speed (how fast the first word appears), while Time per total query measures the overall throughput. Optimizing for conciseness or setting stopping conditions are primary methods to control total latency.

## Practical Use

If the user experience is critical, focus on minimizing TTFT (P90). If the application processes large documents, focus on minimizing Time per total query. Always differentiate between 'must-have' and 'nice-to-have' latency targets.

## Related

- [[LLM-Evaluation-Trilemma|LLM Evaluation Trilemma]]
- [[Comprehensive-LLM-Evaluation-Checklist|Comprehensive LLM Evaluation Checklist]]
