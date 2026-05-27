---
type: framework
status: evergreen
aliases:
  - Hard vs. Soft Model Attributes
  - Model Constraints
  - LLM Attribute Classification
tags:
  - ai-engineering
  - llm-ops
  - architecture
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/083-model-selection-workflow.md
    locator: pages 203-204
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Hard attributes are often the results of decisions made by model providers (licenses, training data, model size) or your own policies (privacy, control).
      - Soft attributes are attributes that can be improved upon, such as accuracy, toxicity, or factual consistency.
      - Latency is a soft attribute if you have access to the model to optimize it to run faster. It’s a hard attribute if you use a model hosted by someone else.
created: 2026-05-26T21:55:45.832561+00:00
updated: 2026-05-26T21:55:45.832561+00:00
ingestion_run: 8d527d59
---

# Hard vs. Soft Model Attributes

## Summary

A decision framework used to categorize model characteristics into non-negotiable constraints (Hard) and optimizable metrics (Soft).

## Core Idea

Hard attributes are fixed by external policies (e.g., licensing, hosting provider, privacy requirements) and must be filtered first. Soft attributes are performance metrics that can be improved through engineering effort (e.g., prompt decomposition, fine-tuning, optimization).

## Practical Use

When evaluating a model candidate, first establish the hard boundaries (e.g., 'Must run on-premise' or 'Cannot use commercial API'). Only models passing these filters are considered for optimization against soft attributes like latency or factual consistency.

## Related

- [[AI-Model-Evaluation-Playbook-4-Step|AI Model Evaluation Playbook (4-Step)]]
- Deployment Strategy
