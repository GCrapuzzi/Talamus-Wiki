---
type: framework
status: evergreen
aliases:
  - Comparative Evaluation Framework
  - Model Comparison Methodology
  - Pairwise Ranking System
tags:
  - ai-engineering
  - evaluation
  - model-selection
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/073-challenges-of-comparative-evaluation.md
    locator: pages 176-178
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Comparative evaluation is challenging because both signal gathering and model ranking are difficult.
      - It is useful when the goal is to determine which model is better, rather than how good a model is.
created: 2026-05-26T21:55:45.763816+00:00
updated: 2026-05-26T21:55:45.763816+00:00
ingestion_run: 8d527d59
---

# Comparative Evaluation Framework

## Summary

A structured approach to determining model superiority by comparing pairs of models (A vs. B) rather than scoring them against a fixed benchmark (Pointwise Evaluation).

## Core Idea

Comparative evaluation measures relative performance, which is useful when absolute performance metrics are difficult to define or when the goal is simply to select the 'best' model for a specific task. It shifts the focus from 'How good is Model A?' to 'Is Model A better than Model B for this task?'

## Practical Use

When selecting between two foundation models for a specific use case (e.g., code generation, summarization), use comparative evaluation (e.g., A/B testing, Chatbot Arena style voting) to determine the optimal choice, especially if the required performance threshold ('good enough') is known, but the absolute metric is not.

## Related

- Pointwise Evaluation
- Transitivity Assumption
- Efficient Matching Algorithms
