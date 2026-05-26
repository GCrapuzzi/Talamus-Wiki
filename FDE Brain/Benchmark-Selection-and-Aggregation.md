---
type: method
tags: [benchmarks, leaderboards, model-selection, evaluation]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#navigate-public-benchmarks
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Benchmark Selection and Aggregation

Creating a leaderboard requires choosing which benchmarks to include and how to aggregate results.

**Selection principles:**
- Balance coverage (range of capabilities) against compute cost
- Check **benchmark correlation** — strongly correlated benchmarks exaggerate biases (e.g., WinoGrande, MMLU, ARC-C all test reasoning → r > 0.86). If two benchmarks are perfectly correlated, drop one.
- TruthfulQA is only moderately correlated with reasoning benchmarks (r ≈ 0.45–0.55), suggesting truthfulness is a distinct capability axis.
- Benchmarks saturate quickly and need replacement (GSM-8K → MATH lvl 5; MMLU → MMLU-PRO).

**Aggregation methods:**
- **Averaging** (Hugging Face) — simple but treats all benchmarks equally regardless of difficulty
- **Mean win rate** (HELM) — fraction of times a model beats another, averaged across scenarios

**Custom leaderboards:** Map your application's criteria to relevant benchmarks. Weight scores according to importance. Not all scores use the same unit (accuracy vs. F1 vs. BLEU) — normalisation needed.

Evaluation harnesses: EleutherAI's lm-evaluation-harness (400+ benchmarks), OpenAI's evals (~500 benchmarks).
