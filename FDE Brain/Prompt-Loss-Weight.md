---
type: glossary
status: evergreen
aliases:
  - Prompt Loss Weight
  - Loss Weighting for Prompts
tags:
  - ai-engineering
  - finetuning
  - hyperparameter
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/138-summary.md
    locator: pages 385-386
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - The prompt model weight determines how much prompts should contribute to this loss compared to responses.
      - If this weight is 0%, the model learns only from responses.
      - Typically, this weight is set to 10% by default.
created: 2026-05-26T21:55:46.281445+00:00
updated: 2026-05-26T21:55:46.281445+00:00
ingestion_run: 8d527d59
---

# Prompt Loss Weight

## Summary

A hyperparameter in instruction finetuning that determines the relative contribution of prompt tokens versus response tokens to the model's total loss during training.

## Core Idea

It allows engineers to explicitly control the learning signal, enabling the model to prioritize learning from the generated response (the desired output) over simply matching the provided prompt context.

## Practical Use

When finetuning, set the weight to 0% if the model should only learn from the response, or a low value (e.g., 10%) if some prompt context learning is desired, preventing the model from over-optimizing for prompt matching.

## Related

- Instruction Finetuning
- Loss Function
