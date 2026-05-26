---
type: pattern
tags: [model-as-a-service, API, deployment-pattern, defensibility]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#chapter-1-introduction-to-building-ai-applications-with-foundation-models
  - AI Space/normalized/pdf/ai-engineering.md#from-foundation-models-to-ai-engineering
  - AI Space/normalized/pdf/ai-engineering.md#maintenance
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Model as a Service

The deployment pattern where foundation models are exposed via APIs, enabling application developers to use powerful models without hosting infrastructure.

Popularized by OpenAI and adopted broadly. Key implications:

- **Democratizes access**: anyone can build AI applications via single API calls, without upfront model development investment.
- **Shifts the bottleneck**: from model training (requires specialized ML talent, massive compute) to model adaptation (prompt engineering, RAG, finetuning).
- **Creates dependency risk**: provider pricing changes, capability expansions, or business failures can disrupt your product. A provider dropping prices 50% can make your in-house model the expensive option overnight.
- **Defensibility concern**: if your product is a thin layer over a model API, the model provider (or a larger company) can subsume your functionality. Three moats: technology (converging), data (via usage flywheel), distribution.

Convergence toward common APIs makes model swapping easier, but each model's quirks require workflow/prompt adjustments. Proper versioning and evaluation infrastructure is essential for smooth transitions.
