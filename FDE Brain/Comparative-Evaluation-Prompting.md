---
type: method
status: evergreen
aliases:
  - Comparative Evaluation Prompting
  - Pairwise Comparison
  - A/B Testing with LLMs
tags:
  - ai-engineering
  - evaluation
  - rlhf
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/069-how-to-use-ai-as-a-judge.md
    locator: pages 162-164
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Compare two generated responses and determine which one is better or predict which one users will likely prefer.
      - Output A or B.
created: 2026-05-26T21:55:45.716828+00:00
updated: 2026-05-26T21:55:45.716828+00:00
ingestion_run: 8d527d59
---

# Comparative Evaluation Prompting

## Summary

A method for using an AI judge to compare two generated responses (A and B) against a single question, determining which is superior or predicting user preference.

## Core Idea

This method is crucial for generating preference data for post-training alignment (RLHF) and ranking models, as it forces the LLM to make a relative judgment rather than an absolute one.

## Practical Use

When comparing two model outputs (A and B), the prompt must explicitly ask the model to choose one ('Output A or B') and provide a justification for its choice. This is superior to asking for two separate scores.

## Related

- [[AI-Judge-Prompting-Framework|AI Judge Prompting Framework]]
