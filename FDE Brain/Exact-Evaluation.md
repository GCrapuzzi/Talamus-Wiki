---
type: framework
status: evergreen
aliases:
  - Exact Evaluation
  - Objective Evaluation
tags:
  - ai-engineering
  - evaluation-metrics
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/063-exact-evaluation.md
    locator: pages 149-149
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Exact evaluation produces judgment without ambiguity.
      - It is used for evaluating open-ended responses (arbitrary text generation) via functional correctness and similarity measurements.
created: 2026-05-26T21:55:45.680542+00:00
updated: 2026-05-26T21:55:45.680542+00:00
ingestion_run: 8d527d59
---

# Exact Evaluation

## Summary

An evaluation approach that produces unambiguous, objective scores, contrasting with subjective methods like human grading.

## Core Idea

Exact evaluation is necessary when the correctness of the output can be definitively determined (e.g., multiple-choice answers), eliminating ambiguity inherent in subjective scoring.

## Practical Use

When designing an LLM test suite, use exact evaluation for tasks requiring deterministic output, such as checking for functional correctness or measuring similarity against specific reference data.

## Related

- Functional Correctness
- Similarity Measurement
