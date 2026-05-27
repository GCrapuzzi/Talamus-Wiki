---
type: pattern
status: evergreen
aliases:
  - Model Response Optimization Pillars
  - LLM Performance Inputs
  - AI Response Quality Factors
tags:
  - ai-engineering
  - llm-ops
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/008-navigating-this-book.md
    locator: pages 18-18
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - "Given a query, the quality of a model’s response depends on the following aspects (outside of the model’s generation setting): The instructions for how the model should behave; The context the model can use to respond to the query; The model itself."
created: 2026-05-26T21:55:45.289576+00:00
updated: 2026-05-26T21:55:45.289576+00:00
ingestion_run: 8d527d59
---

# Model Response Optimization Pillars

## Summary

The three primary, controllable inputs that determine the quality and reliability of a foundation model's response, independent of the model's base generation settings.

## Core Idea

Model performance is not solely determined by the model itself, but by the quality of the surrounding inputs: the instructions (prompting), the context (retrieval), and the model architecture.

## Practical Use

When performance degrades, systematically check these three pillars (Instructions, Context, Model) to pinpoint the source of the issue rather than simply increasing model size or complexity.

## Related

- [[Prompt-Engineering|Prompt Engineering]]
- [[Retrieval-Augmented-Generation-RAG|Retrieval-Augmented Generation (RAG)]]
- Foundation Model Architecture
