---
type: concept
tags: [model-selection, optimisation, latency, cost]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#cost-and-latency
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Pareto Optimisation for Model Evaluation

Optimising for multiple objectives (quality, latency, cost) simultaneously when selecting models.

Approach: be explicit about **hard requirements** vs. **nice-to-haves**. If latency is non-negotiable, first filter by latency threshold, then optimise remaining candidates for quality and cost.

Key latency metrics for foundation models:
- Time to first token (TTFT)
- Time per token
- Time between tokens
- Time per total query

Latency depends on the model, prompt, and sampling variables. Autoregressive models generate token-by-token — more output tokens = higher latency. Controllable via concise prompting, stop conditions, and inference optimisation.

Cost considerations:
- API: pay per token, cost scales linearly
- Self-hosted: compute is fixed; cost per token decreases with scale. Popular model sizes (7B, 65B params) exist because they max out common GPU memory configs (16/24/48/80 GB)
- At certain scale thresholds, re-evaluate API vs. self-hosting
