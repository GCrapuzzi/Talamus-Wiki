---
type: concept
status: evergreen
aliases:
  - In-Context Learning (ICL)
  - Prompt-based learning
  - Zero-shot/Few-shot learning mechanism
tags:
  - llm-architecture
  - prompt-engineering
  - knowledge-retrieval
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/093-in-context-learning-zero-shot-and-few-shot.md
    locator: pages 237-238
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - GPT-3 demonstrated that language models can learn the desirable behavior from examples in the prompt, even if this desirable behavior is different from what the model was originally trained to do.
      - In-context learning allows a model to incorporate new information continually to make decisions, preventing it from becoming outdated.
created: 2026-05-26T21:55:45.900768+00:00
updated: 2026-05-26T21:55:45.900768+00:00
ingestion_run: 8d527d59
---

# In-Context Learning (ICL)

## Summary

The ability of a large language model (LLM) to learn a desirable behavior or perform a task solely by being provided examples or instructions within the input prompt, without requiring any weight updates or fine-tuning.

## Core Idea

ICL allows models to adapt to new tasks or incorporate updated information (e.g., new documentation) by simply including the context in the prompt, making it a form of continual learning. This bypasses the need for expensive and time-consuming retraining (finetuning).

## Practical Use

When integrating an LLM for a new domain or updating its knowledge base (e.g., new company policies, updated API documentation), include the relevant examples and information directly in the prompt context rather than attempting a full model retraining cycle.

## Related

- Zero-Shot Learning
- Few-Shot Learning
- Continual Learning
