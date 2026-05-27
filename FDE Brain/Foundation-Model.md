---
type: concept
status: evergreen
aliases:
  - Foundation Model
  - General-purpose model
  - Large Multimodal Model (LMM)
tags:
  - ai-engineering
  - llm
  - ml-architecture
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/017-from-large-language-models-to-foundation-models.md
    locator: pages 32-35
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Foundation models mark a breakthrough from the traditional structure of AI research.
      - Foundation models... are capable of a wide range of tasks.
      - The word foundation signifies both the importance of these models in AI applications and the fact that they can be built upon for different needs.
created: 2026-05-26T21:55:45.342861+00:00
updated: 2026-05-26T21:55:45.342861+00:00
ingestion_run: 8d527d59
---

# Foundation Model

## Summary

A large, general-purpose model trained on vast, diverse datasets (text, image, audio, etc.) that can be adapted and fine-tuned for a wide range of downstream tasks without task-specific retraining.

## Core Idea

Foundation models represent a paradigm shift from traditional, task-specific AI models (e.g., a model only for sentiment analysis). Their scale and general training allow them to perform a wide range of tasks 'out of the box,' making them highly adaptable building blocks for complex applications.

## Practical Use

When designing an AI application, start with a foundation model (e.g., GPT-4V, Gemini) rather than building a model from scratch for a single task. Use prompt engineering or fine-tuning to maximize performance on a specific business need (e.g., capturing a brand's voice in product descriptions).

## Related

- [[Multimodal-Model|Multimodal Model]]
- [[Self-supervised-Learning|Self-supervised Learning]]
