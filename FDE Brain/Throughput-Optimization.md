---
type: method
status: evergreen
aliases:
  - Throughput Optimization
  - Tokens/second (TPS)
  - System capacity
tags:
  - ai-engineering
  - cost-optimization
  - throughput
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/159-inference-performance-metrics.md
    locator: pages 436-442
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Throughput measures the number of output tokens per second an inference service can generate across all users and requests.
      - Input and output throughput should be counted separately.
created: 2026-05-26T21:55:46.451872+00:00
updated: 2026-05-26T21:55:46.451872+00:00
ingestion_run: 8d527d59
---

# Throughput Optimization

## Summary

A measure of the total number of tokens (input and/or output) an inference service can process per second across all users. It is directly linked to compute cost.

## Core Idea

High throughput generally means lower cost per token. Engineers must distinguish between input throughput (prefilling) and output throughput (decoding) as they have different computational bottlenecks.

## Practical Use

Use throughput metrics to calculate the cost per request or cost per million tokens. When comparing services, prioritize 'cost per request' over raw TPS to account for variable workload sizes.

## Related

- Goodput
- Utilization Metrics
