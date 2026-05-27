---
type: method
status: evergreen
aliases:
  - Preference Finetuning
  - RLHF Finetuning
  - Reinforcement Learning from Human Feedback
tags:
  - ai-engineering
  - llm-alignment
  - rl-techniques
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/124-finetuning-overview.md
    locator: pages 332-334
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Preference finetuning requires comparative data that typically follows the format (instruction, winning response, losing response).
created: 2026-05-26T21:55:46.168088+00:00
updated: 2026-05-26T21:55:46.168088+00:00
ingestion_run: 8d527d59
---

# Preference Finetuning

## Summary

A finetuning technique that uses comparative data (e.g., a winning response vs. a losing response) to train the model to generate responses that maximize human preference and alignment.

## Core Idea

Unlike SFT, which teaches *what* to say, Preference Finetuning teaches *how* to behave according to human values and preferences. It is critical for making models safe, helpful, and aligned.

## Practical Use

Use this method when the desired output is subjective, ethical, or requires nuanced judgment (e.g., deciding which of two generated summaries is more helpful or less biased). The input data must be comparative.

## Related

- Supervised Finetuning
- RLHF
