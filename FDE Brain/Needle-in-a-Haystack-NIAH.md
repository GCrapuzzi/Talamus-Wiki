---
type: method
status: evergreen
aliases:
  - Needle in a Haystack (NIAH)
  - Context Retrieval Test
  - Context Position Evaluation
tags:
  - evaluation
  - llm-testing
  - rag-engineering
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/095-context-length-and-context-efficiency.md
    locator: pages 242-243
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - The idea is to insert a random piece of information (the needle) in different locations in a prompt (the haystack) and ask the model to find it.
      - All the models tested seemed much better at finding the information when it’s closer to the beginning and the end of the prompt than the middle.
created: 2026-05-26T21:55:45.924999+00:00
updated: 2026-05-26T21:55:45.924999+00:00
ingestion_run: 8d527d59
---

# Needle in a Haystack (NIAH)

## Summary

A standardized evaluation methodology used to test the robustness and reliability of an LLM's ability to retrieve specific information (the 'needle') when that information is intentionally placed at varying positions within a large body of text (the 'haystack').

## Core Idea

NIAH moves beyond simple accuracy metrics by testing *where* the model is paying attention. It quantifies the impact of context position, confirming if the model relies on the provided context or if it defaults to internal knowledge.

## Practical Use

When evaluating a RAG pipeline or a long-context model, implement NIAH by: 1) Selecting a private, verifiable piece of information (the needle). 2) Inserting this needle at the start, middle, and end of a large, neutral context (the haystack). 3) Prompting the model to locate and extract the needle. 4) Comparing retrieval success rates across positions.

## Related

- [[Retrieval-Augmented-Generation-RAG|Retrieval-Augmented Generation (RAG)]]
- [[Context-Placement-Pattern-Attention-Decay|Context Placement Pattern (Attention Decay)]]
