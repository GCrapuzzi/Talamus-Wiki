---
type: framework
status: evergreen
aliases:
  - "AI Evaluation Methodology: Functional vs. Reference-Based"
  - AI output evaluation framework
  - functional correctness vs reference data
tags:
  - ai-engineering
  - evaluation
  - testing
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/065-similarity-measurements-against-reference-data.md
    locator: pages 151-157
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - If the task you care about can’t be automatically evaluated using functional correctness, one common approach is to evaluate AI’s outputs against reference data.
created: 2026-05-26T21:55:45.688930+00:00
updated: 2026-05-26T21:55:45.688930+00:00
ingestion_run: 8d527d59
---

# AI Evaluation Methodology: Functional vs. Reference-Based

## Summary

A decision framework for evaluating AI model performance: Functional correctness measures performance based on measurable objectives (e.g., energy saved, game score), while reference-based metrics compare AI output against predefined ground truth data.

## Core Idea

The choice of evaluation method depends on whether the task has a measurable, objective outcome (functional) or requires comparison to a canonical set of answers (reference-based). Functional evaluation is preferred when possible as it avoids the bottleneck and potential biases of reference data generation.

## Practical Use

When designing an evaluation pipeline, first determine if the task can be quantified by an objective metric (e.g., calculating energy savings). If not, proceed to reference-based metrics, understanding the limitations imposed by the quality and completeness of the reference data.

## Related

- Similarity Measurements Against Reference Data
- [[Pass-k-Metric|Pass@k Metric]]
