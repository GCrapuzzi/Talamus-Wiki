---
type: framework
tags: [observability, monitoring, metrics, production-systems]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#monitoring-and-observability
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# AI Observability Metrics

Observability for AI applications extends traditional software monitoring with model-specific metrics. Three meta-metrics from DevOps assess observability quality:

- **MTTD** (mean time to detection) — how fast you notice a problem.
- **MTTR** (mean time to response) — how fast you resolve it after detection.
- **CFR** (change failure rate) — percentage of deployments that cause failures/rollbacks.

### What to track

| Category | Metrics |
|---|---|
| Format | Invalid JSON rate, fixability of malformed outputs |
| Quality | Factual consistency, conciseness, creativity (via AI Judge) |
| Safety | Toxicity rate, PII in inputs/outputs, guardrail trigger rate, refusal rate, abnormal query detection |
| Conversational signals | Generation stop rate, turns per conversation, tokens per input/output, output token distribution over time |
| Latency | Time to First Token, Time Per Output Token, total latency — all tracked per user |
| Cost | Tokens per second, requests per second, cache hit rate |
| Retrieval (RAG) | Context relevance, context precision, index storage, query latency |

Correlate all metrics to business north stars (DAU, session duration, subscriptions). Use spot checks (sampled) and exhaustive checks together. Break down by user, release, prompt version, and time.
