---
type: framework
status: evergreen
aliases:
  - Goodput Metric
  - SLO-constrained throughput
tags:
  - ai-engineering
  - performance-metrics
  - reliability
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/159-inference-performance-metrics.md
    locator: pages 436-442
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Goodput measures the number of requests per second that satisfies the SLO, software-level objective.
created: 2026-05-26T21:55:46.453838+00:00
updated: 2026-05-26T21:55:46.453838+00:00
ingestion_run: 8d527d59
---

# Goodput Metric

## Summary

An adapted metric that measures the number of requests per second that successfully meet a predefined Service Level Objective (SLO) for latency (e.g., TTFT < 200ms, TPOT < 100ms).

## Core Idea

Goodput is superior to raw throughput because it accounts for the quality of service. A high throughput that fails to meet SLOs is misleading; goodput focuses on reliable, high-quality performance.

## Practical Use

When an application has strict user experience requirements (SLOs), use goodput to evaluate the true capacity of the inference service, rather than just the maximum theoretical throughput.

## Related

- [[Inference-Latency-Metrics|Inference Latency Metrics]]
- Service Level Objectives (SLOs)
