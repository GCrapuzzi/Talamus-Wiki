---
type: pattern
tags: [inference, batching, serving, latency, throughput]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#inference-service-optimization
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Inference Batching Strategies

Three batching strategies for inference services, progressively more sophisticated.

### Static batching
Wait until batch is full, then process. Simple but unbounded latency — first request waits for the last.

### Dynamic batching
Process when batch is full **or** a time window expires (e.g., 100 ms), whichever first. Bounds latency but may waste compute on partial batches.

### Continuous batching (in-flight batching)
Introduced in Orca (Yu et al., 2022). Responses are returned as they complete; freed slots are immediately filled by new requests. Eliminates the problem where a 10-token response waits for a 1,000-token response in the same batch.

Analogy: static = bus waits until full; dynamic = bus leaves on schedule or when full; continuous = bus drops/picks up passengers at every stop.
