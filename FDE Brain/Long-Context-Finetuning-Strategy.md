---
type: method
status: evergreen
aliases:
  - Long-Context Finetuning Strategy
  - Context Extension Training
tags:
  - ai-engineering
  - llm-tuning
  - context-window
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/148-ai-powered-data-synthesis.md
    locator: pages 410-418
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Split long documents into shorter chunks (e.g., under 8K tokens). For each short chunk, generate several (question, answer) pairs. For each (question, answer) pair, use the original long document, which may exceed 8K tokens but be shorter than your target length, as the context.
created: 2026-05-26T21:55:46.384368+00:00
updated: 2026-05-26T21:55:46.384368+00:00
ingestion_run: 8d527d59
---

# Long-Context Finetuning Strategy

## Summary

A specialized data synthesis technique used to train models to handle context lengths far exceeding their current maximum token limit (e.g., training an 8K model to handle 128K tokens).

## Core Idea

Instead of feeding the entire long document, the process involves chunking the long document and generating localized (Question, Answer) pairs, while using the full, extended context as the reference material for the model.

## Practical Use

When a model struggles with long documents, split the document into manageable chunks. For each chunk, generate multiple (Q, A) pairs. Crucially, during training, ensure the model is exposed to the full, original long document (even if it exceeds the chunk size) as the context, forcing it to utilize the extended context for answering the localized questions.

## Related

- AI-Powered Data Synthesis
- Long-Context Modeling
