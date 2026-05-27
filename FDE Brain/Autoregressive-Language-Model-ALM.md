---
type: concept
status: evergreen
aliases:
  - Autoregressive Language Model (ALM)
  - Causal Language Model
tags:
  - ai-engineering
  - llm
  - generation
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/016-from-language-models-to-large-language-models.md
    locator: pages 26-31
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - An autoregressive language model is trained to predict the next token in a sequence, using only the preceding tokens.
      - An autoregressive model can continually generate one token after another.
created: 2026-05-26T21:55:45.334845+00:00
updated: 2026-05-26T21:55:45.334845+00:00
ingestion_run: 8d527d59
---

# Autoregressive Language Model (ALM)

## Summary

A language model trained to predict the next token in a sequence using only the tokens that preceded it (unidirectional context).

## Core Idea

ALMs are inherently generative, making them ideal for open-ended text completion and generation because they can continually predict one token after another based on the established context.

## Practical Use

This is the standard architecture for modern generative AI (e.g., ChatGPT). Engineers use ALMs for chatbots, content generation, and sequential data prediction.

## Related

- [[Generative-AI|Generative AI]]
- [[Language-Model-LM|Language Model (LM)]]
