---
type: framework
tags: [model-selection, framework, ai-engineering]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#model-selection-workflow
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Model Selection Workflow

Four-step iterative workflow for selecting the right model for an application:

1. **Filter by hard attributes** — license, data privacy policy, model size constraints, on-device requirements. Hard attributes are impossible or impractical to change (set by provider or your policies). This step alone can eliminate most candidates.
2. **Narrow via public benchmarks** — use publicly available scores and leaderboard rankings to identify promising candidates, balancing quality, latency, and cost.
3. **Evaluate with your own pipeline** — run experiments using your own evaluation data, criteria, and metrics. Public benchmarks won't find the best model for *your* application.
4. **Monitor in production** — detect failures, collect user feedback, iterate.

Key distinction: **hard attributes** (license, training data, model size, privacy policies) vs. **soft attributes** (accuracy, toxicity, factual consistency — improvable via prompting, finetuning, etc.). Whether an attribute is hard or soft depends on your access level — latency is soft if you can optimise the model, hard if you use someone else's API.

General strategy: start with the strongest model to evaluate feasibility, then work backward to find smaller/cheaper models that still meet requirements.
