---
type: method
status: evergreen
aliases:
  - Latency Percentile Analysis
  - p95 analysis
  - outlier detection
tags:
  - ai-engineering
  - observability
  - performance-metrics
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/159-inference-performance-metrics.md
    locator: pages 436-442
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Because latency is a distribution, the average can be misleading.
      - It’s more helpful to look at latency in percentiles, as they tell you something about a certain percentage of your requests.
created: 2026-05-26T21:55:46.455337+00:00
updated: 2026-05-26T21:55:46.455337+00:00
ingestion_run: 8d527d59
---

# Latency Percentile Analysis

## Summary

Analyzing latency using percentiles (e.g., p50, p90, p95, p99) instead of the average (mean) to provide a more accurate and robust view of service performance.

## Core Idea

The average latency can be heavily skewed by outliers (e.g., network errors or extremely long prompts). Percentiles provide a clearer picture of the typical user experience and help identify systemic issues.

## Practical Use

Always report p95 and p99 latency alongside the median (p50) latency. Plotting TTFT against input length is also recommended to identify scaling issues.

## Related

- [[Inference-Latency-Metrics|Inference Latency Metrics]]
