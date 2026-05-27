---
type: concept
status: evergreen
aliases:
  - Masked Language Model (MLM)
  - Bidirectional Encoder Representations from Transformers (BERT)
tags:
  - ai-engineering
  - llm
  - understanding
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/016-from-language-models-to-large-language-models.md
    locator: pages 26-31
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - A masked language model is trained to predict missing tokens anywhere in a sequence, using the context from both before and after the missing tokens.
created: 2026-05-26T21:55:45.337825+00:00
updated: 2026-05-26T21:55:45.337825+00:00
ingestion_run: 8d527d59
---

# Masked Language Model (MLM)

## Summary

A language model trained to predict missing tokens anywhere in a sequence, utilizing context from both the tokens before and the tokens after the missing point (bidirectional context).

## Core Idea

MLMs excel at understanding the overall context of a sequence because they are trained to 'fill in the blank.' This makes them powerful for understanding, rather than generating, text.

## Practical Use

MLMs are commonly used for non-generative tasks such as sentiment analysis, text classification, and code debugging, where understanding the full context is paramount.

## Related

- [[Language-Model-LM|Language Model (LM)]]
- Text Classification
