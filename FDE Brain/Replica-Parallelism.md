---
type: pattern
status: evergreen
aliases:
  - Replica Parallelism
  - Horizontal scaling
  - Service replication
tags:
  - ai-engineering
  - parallelism
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/164-summary.md
    locator: pages 471-472
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - for applications with strict latency requirements, pipeline parallelism is typically avoided in favor of replica parallelism.
      - replica parallelism (which is relatively straightforward to implement)
created: 2026-05-26T21:55:46.497873+00:00
updated: 2026-05-26T21:55:46.497873+00:00
ingestion_run: 8d527d59
---

# Replica Parallelism

## Summary

A service-level pattern where multiple independent copies (replicas) of the entire model are run simultaneously, distributing incoming requests across these replicas.

## Core Idea

This pattern is relatively straightforward to implement and is highly effective for improving overall throughput and handling high request volumes. It is preferred over pipeline parallelism for applications requiring strict, low latency.

## Practical Use

When the primary bottleneck is request volume or when low latency is critical, scale out by adding more replicas. This allows each replica to handle fewer requests, improving response time.

## Related

- [[Inference-Optimization-Techniques|Inference Optimization Techniques]]
- [[Latency-vs-Throughput-Trade-off|Latency vs Throughput Trade-off]]
