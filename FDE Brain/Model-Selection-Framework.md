---
type: framework
status: evergreen
aliases:
  - Model Selection Framework
  - LLM Selection Workflow
  - Model Evaluation Strategy
tags:
  - ai-engineering
  - llm-ops
  - model-selection
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/082-model-selection.md
    locator: pages 203-203
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Model selection is about finding the best model for your application, not the best model overall.
      - "The selection process involves two steps: figuring out the best achievable performance and mapping models along the cost–performance axes."
      - Hard attributes (licenses, model size) are unchangeable constraints that reduce the model pool.
      - Soft attributes (accuracy, toxicity) are attributes that can be improved upon.
created: 2026-05-26T21:55:45.828299+00:00
updated: 2026-05-26T21:55:45.828299+00:00
ingestion_run: 8d527d59
---

# Model Selection Framework

## Summary

A structured, iterative process for selecting the optimal LLM by prioritizing application-specific criteria, differentiating between hard and soft constraints, and mapping performance against cost.

## Core Idea

The goal of model selection is not to find the 'best' model overall, but the model that provides the best performance-to-cost ratio for a specific, defined application. This requires systematically identifying unchangeable constraints (hard attributes) before optimizing mutable ones (soft attributes).

## Practical Use

1. **Define Criteria:** Establish measurable metrics (e.g., pass@1, factual consistency). 2. **Identify Hard Attributes:** Determine non-negotiable constraints (e.g., license type, maximum model size, privacy requirements). These reduce the initial model pool. 3. **Iterative Testing:** Select a starting model (e.g., strongest model for feasibility, or smallest for initial testing) and iterate through adaptation techniques (prompting, finetuning). 4. **Optimize:** Estimate achievable performance improvements on soft attributes (e.g., accuracy) and map the resulting models along the cost-performance axes to select the best value.

## Related

- Cost-Performance Optimization
- Prompt Engineering Strategy
- Finetuning Strategy
