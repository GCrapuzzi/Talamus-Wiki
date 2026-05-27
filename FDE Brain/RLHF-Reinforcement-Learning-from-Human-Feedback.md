---
type: technique
status: evergreen
aliases:
  - RLHF (Reinforcement Learning from Human Feedback)
  - Human Feedback Tuning
tags:
  - ai-engineering
  - rl
  - llm-methods
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/045-post-training.md
    locator: pages 102-103
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Techniques for preference finetuning include reinforcement learning from human feedback (RLHF) (used by GPT-3.5 and Llama 2).
created: 2026-05-26T21:55:45.548752+00:00
updated: 2026-05-26T21:55:45.548752+00:00
ingestion_run: 8d527d59
---

# RLHF (Reinforcement Learning from Human Feedback)

## Summary

A preference finetuning technique that uses human rankings of model outputs to train a reward model. This reward model then guides the LLM's generation process via reinforcement learning.

## Core Idea

RLHF allows the model to optimize against difficult, subjective objectives (human preference) by quantifying human judgment into a measurable reward signal, making the model safer and more aligned.

## Practical Use

The industry standard for initial model alignment (e.g., GPT-3.5, Llama 2). Requires a robust pipeline for human data collection, reward model training, and RL integration.

## Related

- [[Preference-Finetuning|Preference Finetuning]]
- Reward Model
