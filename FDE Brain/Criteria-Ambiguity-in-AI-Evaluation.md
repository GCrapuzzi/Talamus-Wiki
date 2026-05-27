---
type: glossary
status: evergreen
aliases:
  - Criteria Ambiguity in AI Evaluation
  - Non-Standardized Metrics
  - Evaluation Metric Variability
tags:
  - ai-engineering
  - evaluation-methodology
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/070-limitations-of-ai-as-a-judge.md
    locator: pages 165-168
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - The faithfulness scores outputted by these three tools won’t be comparable. If, given a (context, answer) pair, MLflow gives a faithfulness score of 3, Ragas outputs 1, and LlamaIndex outputs NO, which score would you use?
created: 2026-05-26T21:55:45.734012+00:00
updated: 2026-05-26T21:55:45.734012+00:00
ingestion_run: 8d527d59
---

# Criteria Ambiguity in AI Evaluation

## Summary

AI evaluation metrics (e.g., faithfulness, coherence) lack standardization across different open-source tools (MLflow, Ragas, LlamaIndex). This leads to non-comparable scoring systems (e.g., 1-5 scale vs. 0/1 binary vs. YES/NO).

## Core Idea

The output format and scoring logic of evaluation tools are not universally comparable. Engineers must understand the specific scoring system and constraints of the tool they are using to interpret results correctly.

## Practical Use

When comparing evaluation results across different frameworks, do not assume score comparability. Always document the exact scoring system (e.g., 'Ragas 0/1 scale') used for the metric.

## Related

- Evaluation Reproducibility Protocol
