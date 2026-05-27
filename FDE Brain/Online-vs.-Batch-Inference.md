---
type: pattern
status: evergreen
aliases:
  - Online vs. Batch Inference
  - Real-time vs. Asynchronous Inference
  - Latency vs. Throughput Optimization
tags:
  - ai-engineering
  - mlops
  - deployment
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/158-inference-overview.md
    locator: pages 430-435
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Online APIs optimize for latency. Requests are processed as soon as they arrive.
      - Batch APIs optimize for cost. If your application doesn’t have strict latency requirements, you can send them to batch APIs for more efficient processing.
created: 2026-05-26T21:55:46.442041+00:00
updated: 2026-05-26T21:55:46.442041+00:00
ingestion_run: 8d527d59
---

# Online vs. Batch Inference

## Summary

Two deployment patterns for running model inference, optimized for different operational goals: Online for low latency, and Batch for high throughput/low cost.

## Core Idea

The choice between online and batch processing is a cost/performance trade-off. Online APIs prioritize immediate response time (latency), while Batch APIs prioritize efficient resource utilization and cost reduction (throughput), making them suitable for non-time-critical workloads.

## Practical Use

If an application requires immediate user feedback (e.g., chat completion), use an Online API. If the task is bulk processing (e.g., nightly data labeling, large dataset summarization), use a Batch API to maximize hardware utilization and minimize cost.

## Related

- [[Inference-Service-Architecture|Inference Service Architecture]]
