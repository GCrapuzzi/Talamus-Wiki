---
type: pattern
status: evergreen
aliases:
  - Context Grounding
  - Context Restriction
  - Source-Grounded Generation
tags:
  - ai-engineering
  - prompt-engineering
  - hallucination-mitigation
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/099-break-complex-tasks-into-simpler-subtasks.md
    locator: pages 248-250
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - In many scenarios, it’s desirable for the model to use only information provided in the context to respond.
      - Clear instructions, such as 'answer using only the provided context', along with examples of questions it shouldn’t be able to answer, can help.
created: 2026-05-26T21:55:45.951057+00:00
updated: 2026-05-26T21:55:45.951057+00:00
ingestion_run: 8d527d59
---

# Context Grounding

## Summary

A technique used to constrain a Large Language Model's response to use only information provided within the immediate context window, preventing reliance on pre-trained knowledge or hallucination.

## Core Idea

By explicitly instructing the model to 'answer using only the provided context' and requiring it to quote its sources, the output is tethered to the provided corpus, making the model suitable for simulations or internal knowledge bases.

## Practical Use

Implementing roleplaying scenarios (e.g., a character only knowing about a specific fictional universe) or building internal knowledge chatbots where factual accuracy based on a limited, verified corpus is paramount.

## Related

- RAG Pipeline
- System Prompting
