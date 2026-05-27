---
type: pattern
status: evergreen
aliases:
  - Continuous Batching (In-Flight Batching)
  - In-flight batching
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
      - Continuous batching allows responses in a batch to be returned to users as soon as they are completed.
      - After a request in a batch is completed and its response returned, the service can add another request into the batch in its place, making the batching continuous.
created: 2026-05-26T21:55:46.482406+00:00
updated: 2026-05-26T21:55:46.482406+00:00
ingestion_run: 8d527d59
---

# Continuous Batching (In-Flight Batching)

## Summary

A dynamic batching technique that allows responses to be returned immediately upon completion, enabling the service to continuously add new requests into the batch in the vacated slot.

## Core Idea

Traditional batching forces all requests to wait for the longest response to complete. Continuous batching maximizes GPU utilization and minimizes latency for short responses by processing results and immediately filling the vacated slot with a new request.

## Practical Use

Implement this when serving LLMs with highly variable response lengths (e.g., chat applications). It significantly improves throughput and reduces the perceived latency for users with short queries, maximizing the utilization of expensive GPU resources.

## Related

- [[Dynamic-Batching|Dynamic Batching]]
- Inference Service Optimization
