---
type: method
status: evergreen
aliases:
  - AI Evaluation Experiment Tracking
  - LLM Reproducibility Logging
  - Evaluation Variable Logging
tags:
  - ai-engineering
  - mlops
  - reproducibility
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/090-summary.md
    locator: pages 232-234
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - "As you iterate on your evaluation pipeline, make sure to do proper experiment tracking: log all variables that could change in an evaluation process, including but not limited to the evaluation data, the rubric, and the prompt and sampling configurations used for the AI judges."
created: 2026-05-26T21:55:45.887691+00:00
updated: 2026-05-26T21:55:45.887691+00:00
ingestion_run: 8d527d59
---

# AI Evaluation Experiment Tracking

## Summary

A mandatory operational playbook requiring the logging of all variables that influence the evaluation outcome to ensure reproducibility and guide iterative improvements.

## Core Idea

To maintain consistency during iteration, every variable that can change—including data, scoring rules, and model parameters—must be logged. Failure to track variables invalidates the ability to use results for development guidance.

## Practical Use

Implement a logging system (e.g., MLflow, dedicated database) to track versions of: 1) Evaluation Data, 2) Scoring Rubrics, 3) Prompt Templates, and 4) Sampling/Decoding Configurations (e.g., temperature, top_p).

## Related

- [[AI-Evaluation-Pipeline-Design|AI Evaluation Pipeline Design]]
