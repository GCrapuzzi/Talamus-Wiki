---
type: pattern
status: evergreen
aliases:
  - AI Judge Drift Monitoring
  - Evaluation Metric Drift
  - Judge Consistency Check
tags:
  - ai-engineering
  - mlops
  - evaluation-methodology
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/070-limitations-of-ai-as-a-judge.md
    locator: pages 165-168
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - AI judges are also AI applications, which means that they also can change over time.
      - Do not trust any AI judge if you can’t see the model and the prompt used for the judge.
created: 2026-05-26T21:55:45.727557+00:00
updated: 2026-05-26T21:55:45.727557+00:00
ingestion_run: 8d527d59
---

# AI Judge Drift Monitoring

## Summary

AI judges are themselves AI applications and are susceptible to drift. Changes in the judge's prompt, model, or underlying parameters can cause evaluation scores to change, leading to false attribution of performance changes to the application itself.

## Core Idea

Evaluation metrics must be fixed and versioned alongside the application. If the judge changes, the evaluation results are invalid for comparison, regardless of the observed score change.

## Practical Use

Implement a mandatory versioning system for the judge's prompt and model configuration. Before comparing evaluation results across time periods, verify that the exact judge configuration used in both periods is identical.

## Related

- MLOps Model Monitoring
