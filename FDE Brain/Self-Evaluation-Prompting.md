---
type: method
status: evergreen
aliases:
  - Self-Evaluation Prompting
  - Intrinsic Quality Scoring
  - Single-Pass Evaluation
tags:
  - ai-engineering
  - evaluation
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/069-how-to-use-ai-as-a-judge.md
    locator: pages 162-164
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Evaluate the quality of a response by itself, given the original question.
created: 2026-05-26T21:55:45.718991+00:00
updated: 2026-05-26T21:55:45.718991+00:00
ingestion_run: 8d527d59
---

# Self-Evaluation Prompting

## Summary

Using an AI judge to evaluate the quality of a single generated response based solely on the original question and the answer itself.

## Core Idea

This approach is useful for initial quality checks or when no external reference answer is available. The prompt must guide the model to assess the answer's completeness and coherence relative to the prompt.

## Practical Use

Use this when assessing a chatbot's general performance or when the goal is to measure the inherent quality of the generated text, independent of a ground truth.

## Related

- [[AI-Judge-Prompting-Framework|AI Judge Prompting Framework]]
