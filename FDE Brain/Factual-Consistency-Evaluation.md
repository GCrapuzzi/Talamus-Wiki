---
type: framework
status: evergreen
aliases:
  - Factual Consistency Evaluation
  - Hallucination Detection
  - Grounding Check
tags:
  - ai-engineering
  - evaluation
  - hallucination
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/079-generation-capability.md
    locator: pages 187-195
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - The output is evaluated against explicitly provided facts (context) or against open knowledge.
      - Local factual consistency is important for tasks with limited scopes such as summarization...
      - Global factual consistency is important for tasks with broad scopes such as general chatbots, fact-checking, market research, etc.
created: 2026-05-26T21:55:45.802894+00:00
updated: 2026-05-26T21:55:45.802894+00:00
ingestion_run: 8d527d59
---

# Factual Consistency Evaluation

## Summary

A structured approach to verifying if a generated output is supported by explicit context (Local) or general, accepted knowledge (Global).

## Core Idea

Factual consistency is critical because hallucinations can cause catastrophic consequences. Verification must be scoped: Local consistency checks the output against provided context (e.g., a retrieved document), while Global consistency checks against open, accepted knowledge.

## Practical Use

When building RAG systems or chatbots, implement a two-tiered validation layer. For summarization or Q&A, enforce Local consistency by comparing generated claims only against the retrieved context chunks. For general knowledge tasks, use external knowledge bases or established fact-checking APIs to validate Global consistency.

## Related

- [[AI-as-a-Judge|AI as a Judge]]
- [[Contextual-Grounding|Contextual Grounding]]
