---
type: method
status: evergreen
aliases:
  - Dynamic Batching
  - Time-window batching
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
      - Dynamic batching, on the other hand, sets a maximum time window for each batch.
      - The server processes the batch either when it has four requests or when 100 ms has passed, whichever happens first.
created: 2026-05-26T21:55:46.484673+00:00
updated: 2026-05-26T21:55:46.484673+00:00
ingestion_run: 8d527d59
---

# Dynamic Batching

## Summary

A resource allocation technique where a batch is processed either when a fixed number of requests are gathered or when a predefined maximum time window expires, whichever occurs first.

## Core Idea

It balances throughput (by waiting for a full batch) and latency (by enforcing a time limit). Unlike static batching, it prevents early requests from being unnecessarily delayed by late arrivals.

## Practical Use

Use this as a baseline optimization for inference services. It is ideal when maintaining predictable, low latency is critical, even if it results in occasional under-filled batches and slightly lower compute efficiency.

## Related

- Static Batching
- Continuous Batching
