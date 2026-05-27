---
type: framework
status: evergreen
aliases:
  - Finetuning Trade-offs and Risks
  - Catastrophic Forgetting
  - Model Specialization Risk
tags:
  - ai-engineering
  - llm-deployment
  - model-maintenance
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/127-reasons-not-to-finetune.md
    locator: pages 336-339
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - while finetuning a model for a specific task can improve its performance for that task, it can degrade its performance for other tasks.
created: 2026-05-26T21:55:46.189625+00:00
updated: 2026-05-26T21:55:46.189625+00:00
ingestion_run: 8d527d59
---

# Finetuning Trade-offs and Risks

## Summary

Finetuning a model for a specific task (Task A) can improve performance on that task but often degrades performance on other tasks (Task B, Task C), leading to reduced generalizability.

## Core Idea

Specialization comes at the cost of generalization. A model optimized for one domain may perform poorly when exposed to diverse, out-of-scope prompts. This requires careful planning of the target use cases.

## Practical Use

If a model must handle diverse queries (e.g., product recommendations, changing orders, general feedback), do not finetune on only one task. Instead, either finetune on a comprehensive dataset covering all expected tasks or, preferably, use separate, specialized models for distinct functional areas.

## Related

- Model Ensemble
- Task-Specific Model Deployment
