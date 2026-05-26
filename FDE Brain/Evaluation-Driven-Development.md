---
type: method
tags: [evaluation, methodology, ai-engineering]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#evaluation-criteria
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Evaluation-Driven Development

Define evaluation criteria **before** building the AI application. Inspired by test-driven development in software engineering.

Applications with clear evaluation criteria are the most common in production:
- **Recommender systems** — measurable via engagement / purchase-through rates
- **Fraud detection** — measurable via money saved from prevented fraud
- **Code generation** — measurable via functional correctness
- **Classification tasks** (intent, sentiment, next-action) — easier to evaluate than open-ended generation

The lamppost problem: focusing only on applications whose outcomes can be measured may cause teams to miss game-changing applications that lack obvious metrics. Evaluation is the biggest bottleneck to AI adoption — building reliable evaluation pipelines unlocks new application categories.
