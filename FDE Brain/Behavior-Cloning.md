---
type: pattern
status: evergreen
aliases:
  - Behavior Cloning
  - Imitation Learning
tags:
  - ai-engineering
  - ml-patterns
  - data-labeling
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/046-supervised-finetuning.md
    locator: pages 104-106
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - "Some people refer to this process as behavior cloning: you demonstrate how the model should behave, and the model clones this behavior."
created: 2026-05-26T21:55:45.556619+00:00
updated: 2026-05-26T21:55:45.556619+00:00
ingestion_run: 8d527d59
---

# Behavior Cloning

## Summary

A machine learning pattern where an AI model is trained to replicate expert behavior by learning from a dataset of successful demonstrations, rather than being trained purely on statistical prediction.

## Core Idea

The model is taught 'how' to behave by observing 'what' the expert does. This is crucial for tasks requiring complex judgment, critical thinking, or adherence to specific protocols.

## Practical Use

When designing the data pipeline, frame the data collection process as 'behavior cloning' to emphasize that the goal is not just pattern matching, but replicating expert judgment (e.g., complex summarization or legal analysis).

## Related

- [[Demonstration-Data|Demonstration Data]]
- [[Supervised-Finetuning-SFT|Supervised Finetuning (SFT)]]
