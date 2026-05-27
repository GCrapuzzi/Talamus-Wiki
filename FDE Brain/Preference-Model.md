---
type: concept
status: evergreen
aliases:
  - Preference Model
  - Pairwise Judge
  - Human Preference Predictor
tags:
  - ai-engineering
  - alignment
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/071-what-models-can-act-as-judges.md
    locator: pages 169-171
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - A preference model takes in (prompt, response 1, response 2) as input and outputs which of the two responses is better (preferred by users) for the given prompt.
created: 2026-05-26T21:55:45.749658+00:00
updated: 2026-05-26T21:55:45.749658+00:00
ingestion_run: 8d527d59
---

# Preference Model

## Summary

A specialized judge that takes a prompt and two candidate responses (Response 1, Response 2) and outputs a prediction of which response is preferred by a human user.

## Core Idea

Preference models are highly valuable because they directly predict human judgment, which is the ultimate goal of AI alignment. They are essential for building safer and more user-aligned models.

## Practical Use

Use a preference model to rank multiple generated responses in a pairwise manner (A vs B, B vs C, etc.), simulating human user choice without requiring actual human labeling for every comparison.

## Related

- Reward Model
- Human Preference Data
