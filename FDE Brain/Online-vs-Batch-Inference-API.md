---
type: pattern
tags: [inference, API-design, latency, throughput, cost-optimization]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#inference-overview
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Online vs Batch Inference API

Two API tiers offered by model providers, optimizing for different objectives.

| | Online API | Batch API |
|---|---|---|
| Optimizes for | Latency | Cost |
| Processing | Immediate on arrival | Queued, hours turnaround |
| Typical discount | Baseline | ~50% (Gemini, OpenAI as of writing) |

**Batch API use cases**: synthetic data generation, periodic reporting (Slack summaries, sentiment analysis), document onboarding, model migration reprocessing, personalized recommendations, knowledge base reindexing.

This differs from traditional ML batch inference where predictions are *precomputed* for finite inputs (e.g., recommendation systems). Foundation model inputs are open-ended, so precomputation is impractical.

**Streaming mode**: online APIs can return tokens as generated, reducing perceived TTFT. Trade-off: you can't score/filter a response before the user sees it, but you can retrospectively update or remove it.
