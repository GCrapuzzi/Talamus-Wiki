---
type: pattern
status: evergreen
aliases:
  - AI Judge Prompting Framework
  - LLM Evaluation Prompting
  - AI Judge Prompt Structure
tags:
  - ai-engineering
  - prompt-engineering
  - evaluation
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/069-how-to-use-ai-as-a-judge.md
    locator: pages 162-164
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - A judge’s prompt should clearly explain the task the model is to perform.
      - The criteria the model should follow to evaluate.
      - The scoring system.
created: 2026-05-26T21:55:45.714649+00:00
updated: 2026-05-26T21:55:45.714649+00:00
ingestion_run: 8d527d59
---

# AI Judge Prompting Framework

## Summary

A structured approach for designing prompts that guide an LLM to evaluate content based on specific criteria, ensuring the prompt clearly defines the task, the evaluation criteria, and the required scoring format.

## Core Idea

Effective AI judging requires explicit instruction. The prompt must not only ask for a score but must also define the scope (criteria) and the format (scoring system) to minimize ambiguity and maximize reliability.

## Practical Use

When building an evaluation pipeline (e.g., for RAG or code generation), use this framework to construct the system prompt. For instance, if evaluating relevance, the prompt must specify: 1) The goal (relevance check), 2) The criteria (sufficient information based on ground truth), and 3) The output format (e.g., 1-5 score + justification).

## Related

- [[Comparative-Evaluation-Prompting|Comparative Evaluation Prompting]]
- [[Self-Evaluation-Prompting|Self-Evaluation Prompting]]
