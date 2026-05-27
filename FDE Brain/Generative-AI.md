---
type: concept
status: evergreen
aliases:
  - Generative AI
  - Completion Machine
tags:
  - ai-engineering
  - llm
  - generative
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/016-from-language-models-to-large-language-models.md
    locator: pages 26-31
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - A model that can generate open-ended outputs is called generative, hence the term generative AI.
      - "You can think of a language model as a completion machine: given a text (prompt), it tries to complete that text."
created: 2026-05-26T21:55:45.341273+00:00
updated: 2026-05-26T21:55:45.341273+00:00
ingestion_run: 8d527d59
---

# Generative AI

## Summary

AI systems, typically powered by autoregressive language models, that can use a fixed, finite vocabulary to construct infinite possible, open-ended outputs based on a given prompt.

## Core Idea

Generative AI is defined by its ability to create novel content (text, images, code) rather than just classifying or analyzing existing data. Its outputs are probabilistic predictions, not guaranteed facts.

## Practical Use

Used for content creation, drafting code, summarizing documents, and conversational AI. Engineers must treat model outputs as probabilistic suggestions requiring validation.

## Related

- [[Autoregressive-Language-Model-ALM|Autoregressive Language Model (ALM)]]
- [[Language-Model-LM|Language Model (LM)]]
