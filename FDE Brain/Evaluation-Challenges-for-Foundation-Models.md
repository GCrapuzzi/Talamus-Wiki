---
type: concept
tags: [evaluation, foundation-models, benchmarks, ai-engineering]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#chapter-3-evaluation-methodology
  - AI Space/normalized/pdf/ai-engineering.md#challenges-of-evaluating-foundation-models
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Evaluation Challenges for Foundation Models

Foundation models are harder to evaluate than traditional ML models for several compounding reasons:

1. **Intelligence–evaluation gap**: The smarter the model, the harder it is to verify correctness. Validating a PhD-level math proof requires domain expertise that most evaluators lack.
2. **Open-ended outputs undermine ground truths**: Traditional ML has close-ended outputs (e.g., classification labels) that can be checked against expected values. Open-ended generation has many valid responses per input—exhaustive reference sets are impossible.
3. **Black-box opacity**: Model providers rarely expose architecture, training data, or training process. Evaluation is limited to observing outputs.
4. **Benchmark saturation**: Benchmarks become useless once models achieve perfect scores. GLUE (2018) saturated in one year → SuperGLUE (2019). MMLU (2020) → MMLU-Pro (2024).
5. **Expanded scope**: General-purpose models must be evaluated not just on known tasks but on *discovering* new capabilities and limitations.

Despite exponential growth in evaluation research and tooling, investment in evaluation still lags behind investment in model development and AI orchestration.
