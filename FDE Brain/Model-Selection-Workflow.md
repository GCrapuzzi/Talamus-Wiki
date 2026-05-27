---
type: framework
status: evergreen
aliases:
  - Model Selection Workflow
  - LLM Model Selection
  - AI Model Evaluation Strategy
tags:
  - ai-engineering
  - llm-ops
  - model-selection
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/083-model-selection-workflow.md
    locator: pages 203-204
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - You care about which model is the best for your applications.
      - "The selection process typically involves two steps: Figuring out the best achievable performance and Mapping models along the cost–performance axes."
      - The process is iterative, requiring model selection over and over again as adaptation techniques are applied.
created: 2026-05-26T21:55:45.830233+00:00
updated: 2026-05-26T21:55:45.830233+00:00
ingestion_run: 8d527d59
---

# Model Selection Workflow

## Summary

An iterative, application-centric process for selecting the optimal LLM by balancing performance, cost, and technical constraints.

## Core Idea

The goal is not to find the 'best' model overall, but the model that provides the best performance relative to the specific application's constraints and budget (cost-performance axis).

## Practical Use

1. Define hard constraints (e.g., required privacy, hosting environment). 2. Use public benchmarks to narrow the field. 3. Run internal experiments, potentially starting with strong models for feasibility and scaling down for hardware constraints. 4. Implement continuous monitoring post-deployment.

## Related

- [[Hard-vs.-Soft-Model-Attributes|Hard vs. Soft Model Attributes]]
- [[AI-Model-Evaluation-Playbook-4-Step|AI Model Evaluation Playbook (4-Step)]]
- Cost-Performance Optimization
