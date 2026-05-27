---
type: data-format
status: evergreen
aliases:
  - Comparison Data (Pairwise Ranking)
  - A/B Preference Data
  - Winning/Losing Pairs
tags:
  - ai-engineering
  - data-curation
  - llm-alignment
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/047-preference-finetuning.md
    locator: pages 107-111
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - An easier task is to ask labelers to compare two responses and decide which one is better.
      - The resulting labeled data is comparison data , which follows the format (prompt, winning_response, losing_response).
created: 2026-05-26T21:55:45.563884+00:00
updated: 2026-05-26T21:55:45.563884+00:00
ingestion_run: 8d527d59
---

# Comparison Data (Pairwise Ranking)

## Summary

A dataset format where human labelers are presented with a single prompt and multiple generated responses, and are asked only to rank or compare which response is superior, rather than assigning an absolute score.

## Core Idea

Pairwise comparison is significantly more reliable and efficient than pointwise evaluation because it leverages human judgment by focusing on relative preference (A > B) rather than absolute scoring (A=7, B=5).

## Practical Use

When curating data for an RM, an engineer collects data in the format (prompt, winning_response, losing_response). This data is then used to train the RM to predict the relative preference, which is mathematically modeled to maximize the score difference.

## Related

- Reward Model Training
- [[Preference-Finetuning|Preference Finetuning]]
