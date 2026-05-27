---
type: concept
status: evergreen
aliases:
  - AI Judge System Definition
  - AI Evaluator System
tags:
  - ai-engineering
  - evaluation-methodology
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/070-limitations-of-ai-as-a-judge.md
    locator: pages 165-168
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - An AI judge is not just a model—it’s a system that includes both a model and a prompt. Altering the model, the prompt, or the model’s sampling parameters results in a different judge.
created: 2026-05-26T21:55:45.725998+00:00
updated: 2026-05-26T21:55:45.725998+00:00
ingestion_run: 8d527d59
---

# AI Judge System Definition

## Summary

An AI judge is not merely a model, but a complete system comprising a specific language model, a detailed prompt, and defined sampling parameters. Changes to any of these components constitute a different judge.

## Core Idea

The evaluation process is defined by the entire system (Model + Prompt + Parameters), not just the underlying LLM. This emphasizes the need to version control all components for reproducible evaluation.

## Practical Use

When setting up an evaluation pipeline, treat the judge configuration (e.g., GPT-4-turbo, specific system prompt, temperature=0.1) as a versioned artifact. Documenting this triad is critical for reproducibility.

## Related

- Evaluation Reproducibility Protocol
