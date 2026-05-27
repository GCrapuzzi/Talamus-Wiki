---
type: glossary
status: evergreen
aliases:
  - Prompt vs. Context (Terminology)
  - Input vs. Contextual Information
tags:
  - llm-terminology
  - prompt-engineering
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/093-in-context-learning-zero-shot-and-few-shot.md
    locator: pages 237-238
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - I’ll use prompt to refer to the whole input into the model, and context to refer to the information provided to the model so that it can perform a given task.
created: 2026-05-26T21:55:45.909698+00:00
updated: 2026-05-26T21:55:45.909698+00:00
ingestion_run: 8d527d59
---

# Prompt vs. Context (Terminology)

## Summary

Clarifies the distinction between 'Prompt' and 'Context' in LLM engineering. The Prompt is the entire input, while Context is the specific information provided to guide the model's task execution.

## Core Idea

Using 'Prompt' for the entire input and 'Context' for the guiding information prevents ambiguity. Context is the information that shapes *how* the model responds (e.g., required format, restricted vocabulary, specific topic focus).

## Practical Use

When documenting prompt templates, clearly delineate the sections: the main instruction (part of the prompt), the examples (part of the context), and the background information (part of the context). This ensures consistent communication among engineering teams.

## Related

- [[In-Context-Learning-ICL|In-Context Learning (ICL)]]
