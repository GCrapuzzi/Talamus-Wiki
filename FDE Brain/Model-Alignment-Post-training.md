---
type: framework
status: evergreen
aliases:
  - Model Alignment (Post-training)
  - Human Preference Alignment
  - Safety Tuning
tags:
  - ai-engineering
  - llm-ops
  - safety
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/039-training-data.md
    locator: pages 74-74
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - The goal of post-training is to align the model with human preferences.
      - The way a model developer aligns their model has a significant impact on the model’s usability.
created: 2026-05-26T21:55:45.505706+00:00
updated: 2026-05-26T21:55:45.505706+00:00
ingestion_run: 8d527d59
---

# Model Alignment (Post-training)

## Summary

The process of refining a pre-trained foundation model to ensure its outputs are safe, usable, and consistent with human preferences and ethical guidelines.

## Core Idea

Pre-training grants capability, but post-training (alignment) grants usability. Alignment is necessary to mitigate raw model risks (e.g., generating harmful or nonsensical content) and guide the model toward desired behavior.

## Practical Use

Implement Reinforcement Learning from Human Feedback (RLHF) or similar preference-based tuning loops. Define clear, measurable preference criteria (e.g., helpfulness, harmlessness, honesty) before starting the alignment phase.

## Related

- Sampling Strategies
- Operational Playbook: Bias Mitigation
