---
type: operation
status: evergreen
aliases:
  - AI Model Evaluation Playbook (4-Step)
  - LLM Validation Workflow
  - Model Selection Pipeline
tags:
  - ai-engineering
  - llm-ops
  - playbook
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/083-model-selection-workflow.md
    locator: pages 203-204
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - 1. Filter out models whose hard attributes don’t work for you.
      - 2. Use publicly available information, e.g., benchmark performance and leaderboard ranking, to narrow down the most promising models to experiment with.
      - 3. Run experiments with your own evaluation pipeline to find the best model.
      - 4. Continually monitor your model in production to detect failure and collect feedback to improve your application.
created: 2026-05-26T21:55:45.834113+00:00
updated: 2026-05-26T21:55:45.834113+00:00
ingestion_run: 8d527d59
---

# AI Model Evaluation Playbook (4-Step)

## Summary

A structured, four-stage operational playbook for systematically evaluating an LLM candidate, moving from broad filtering to continuous production monitoring.

## Core Idea

Evaluation is a continuous, multi-stage process. Skipping any stage (especially monitoring) risks deploying a model that fails in real-world conditions.

## Practical Use

1. **Filter:** Eliminate models based on hard constraints (e.g., licensing). 2. **Benchmark:** Use public leaderboards to narrow the field, balancing quality, latency, and cost. 3. **Experiment:** Run internal, custom evaluation pipelines to find the optimal balance. 4. **Monitor:** Continuously track performance in production to detect drift and collect feedback for iteration.

## Related

- Model Monitoring
- Benchmarking
- [[Model-Selection-Workflow|Model Selection Workflow]]
