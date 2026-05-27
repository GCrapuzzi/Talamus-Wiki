---
type: concept
status: evergreen
aliases:
  - Reward Model (RM)
  - RLHF Scorer
  - Scoring Model
tags:
  - ai-engineering
  - rlhf
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/071-what-models-can-act-as-judges.md
    locator: pages 169-171
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - A reward model takes in a (prompt, response) pair and scores how good the response is given the prompt.
      - Reward models have been successfully used in RLHF for many years.
created: 2026-05-26T21:55:45.744767+00:00
updated: 2026-05-26T21:55:45.744767+00:00
ingestion_run: 8d527d59
---

# Reward Model (RM)

## Summary

A specialized judge that takes a (prompt, response) pair and outputs a single scalar score indicating the quality or correctness of the response.

## Core Idea

RMs are foundational to Reinforcement Learning from Human Feedback (RLHF). They distill complex human preference into a quantifiable, lightweight score, making evaluation scalable.

## Practical Use

Use an RM to score thousands of generated responses efficiently, allowing for automated ranking and filtering based on a continuous quality metric (e.g., a score between 0 and 1).

## Related

- [[Preference-Model|Preference Model]]
- [[Reference-based-Judge|Reference-based Judge]]
