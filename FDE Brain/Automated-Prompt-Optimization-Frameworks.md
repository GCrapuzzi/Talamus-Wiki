---
type: method
status: evergreen
aliases:
  - Automated Prompt Optimization Frameworks
  - Prompt Optimization Tools
  - Auto-Prompting
tags:
  - ai-engineering
  - optimization
  - llm-ops
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/102-evaluate-prompt-engineering-tools.md
    locator: pages 254-256
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Tools that aim to automate the whole prompt engineering workflow include Open-Prompt... and DSPy.
      - At a high level, you specify the input and output formats, evaluation metrics, and evaluation data for your task.
      - Functionally, these tools are similar to autoML (automated ML) tools that automatically find the optimal hyperparameters for classical ML models.
created: 2026-05-26T21:55:45.968518+00:00
updated: 2026-05-26T21:55:45.968518+00:00
ingestion_run: 8d527d59
---

# Automated Prompt Optimization Frameworks

## Summary

Tools (e.g., DSPy, Open-Prompt) that treat prompt engineering like hyperparameter tuning in classical ML. The user specifies the input/output formats, metrics, and data, and the tool automatically searches for the optimal prompt or prompt chain.

## Core Idea

These frameworks abstract away the manual, time-consuming process of prompt iteration by using optimization algorithms (similar to AutoML) to maximize performance metrics on a given evaluation dataset.

## Practical Use

When manual prompt tuning is infeasible due to the infinite search space, utilize these frameworks. Define the task constraints (input/output schema) and let the tool iteratively refine the prompt structure and content.

## Related

- AutoML
- Prompt Engineering Lifecycle
