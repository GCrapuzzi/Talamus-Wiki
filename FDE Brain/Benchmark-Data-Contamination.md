---
type: concept
tags: [evaluation, benchmarks, data-contamination, ai-engineering]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#navigate-public-benchmarks
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Benchmark Data Contamination

Data contamination occurs when a model is trained on the same data it's evaluated on, inflating benchmark scores via memorisation.

**How it happens:**
- Unintentional: internet-scraped training data accidentally includes public benchmark data
- Indirect: training and benchmark data drawn from the same source (e.g., math textbooks)
- Intentional (legitimate): continuing training on benchmark data after model selection to improve the released model's performance

**Detection methods:**
- **N-gram overlapping** — if a 13-token sequence from an eval sample appears in training data, it's contaminated. Accurate but expensive; requires training data access.
- **Perplexity** — unusually low perplexity on eval data suggests prior exposure. Less accurate but resource-efficient.

**Mitigation:**
- Remove benchmarks you care about from training data before training
- Report contamination rates alongside benchmark scores
- Keep part of benchmark data private with automated evaluation tools
- Leaderboard hosts plot standard deviations to spot outliers

GPT-3 analysis found 13 benchmarks with ≥40% data in training set (Brown et al. 2020). Schaeffer (2023) demonstrated a 1M-parameter model achieving near-perfect scores by training exclusively on benchmark data.
