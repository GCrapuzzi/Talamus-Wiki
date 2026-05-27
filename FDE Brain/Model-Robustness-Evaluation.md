---
type: method
status: evergreen
aliases:
  - Model Robustness Evaluation
  - Prompt perturbation testing
  - Instruction-following stability testing
tags:
  - llm-evaluation
  - qa-engineering
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/093-in-context-learning-zero-shot-and-few-shot.md
    locator: pages 237-238
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - If the prompt changes slightly—such as writing “5” instead of “five”, adding a new line, or changing capitalization—would the model’s response be dramatically different?
      - You can measure a model’s robustness by randomly perturbing the prompts to see how the output changes.
created: 2026-05-26T21:55:45.905093+00:00
updated: 2026-05-26T21:55:45.905093+00:00
ingestion_run: 8d527d59
---

# Model Robustness Evaluation

## Summary

A technique to measure how sensitive an LLM's output is to minor, non-semantic changes in the input prompt (e.g., changing capitalization, substituting synonyms, adding whitespace).

## Core Idea

A model's robustness is strongly correlated with its overall capability. Low robustness indicates that the model requires extensive 'fiddling' (detailed prompt engineering) to achieve consistent results, suggesting a need to upgrade to a more capable model.

## Practical Use

Before deploying an LLM, systematically test the prompt by introducing random perturbations (e.g., changing '5' to 'five', adding newlines) to ensure the core task output remains consistent. This helps determine the necessary level of prompt engineering effort.

## Related

- Instruction-Following Capability
