---
type: method
status: evergreen
aliases:
  - Scoring Rubric Design
  - Evaluation Scoring System
  - AI Grading Schema
tags:
  - ai-engineering
  - evaluation
  - data-annotation
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/088-step-2.-create-an-evaluation-guideline.md
    locator: pages 226-227
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - "For each criterion, choose a scoring system: would it be binary (0 and 1), from 1 to 5, between 0 and 1, or something else?"
      - On this scoring system, create a rubric with examples. What does a response with a score of 1 look like and why does it deserve a 1?
created: 2026-05-26T21:55:45.869893+00:00
updated: 2026-05-26T21:55:45.869893+00:00
ingestion_run: 8d527d59
---

# Scoring Rubric Design

## Summary

The process of selecting and formalizing a scoring system (e.g., binary, ordinal scale, continuous) for each defined evaluation criterion, and documenting what specific scores represent.

## Core Idea

The scoring system must be unambiguous. The rubric must explicitly define what a score of '1' looks like and why it deserves that score, minimizing subjective human interpretation.

## Practical Use

For a criterion like 'Factual Consistency,' choose a system (e.g., binary: 1 for entailment, 0 for inconsistency). Then, create a rubric: 'A score of 1 means the response cites the source document and the claim is directly supported by the text.' Validate this rubric with multiple human reviewers to ensure consistency.

## Related

- [[AI-Evaluation-Guideline-Playbook|AI Evaluation Guideline Playbook]]
- [[Defining-Evaluation-Criteria|Defining Evaluation Criteria]]
