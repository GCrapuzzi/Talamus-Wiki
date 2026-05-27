---
type: decision_framework
status: evergreen
aliases:
  - Latency vs Throughput Trade-off
  - Cost vs Speed trade-off
tags:
  - ai-engineering
  - architecture
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/164-summary.md
    locator: pages 471-472
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - There’s a trade-off between latency and throughput.
      - if low latency is a higher priority than cost, you might want to scale up replica parallelism.
created: 2026-05-26T21:55:46.505284+00:00
updated: 2026-05-26T21:55:46.505284+00:00
ingestion_run: 8d527d59
---

# Latency vs Throughput Trade-off

## Summary

A fundamental trade-off in AI deployment where reducing inference latency (faster response time) typically requires increasing computational cost (more resources/machines), and vice versa.

## Core Idea

The choice of optimization technique must be guided by the business requirement: if low latency is critical (e.g., real-time chat), cost must be secondary. If cost is critical (e.g., batch processing), latency can be tolerated.

## Practical Use

Before deploying, define the acceptable SLA for both latency (e.g., < 500ms) and cost (e.g., < $0.01/1000 tokens). This framework dictates whether to prioritize replica parallelism (low latency, high cost) or batching/quantization (low cost, potentially higher latency).

## Related

- [[Inference-Optimization-Techniques|Inference Optimization Techniques]]
