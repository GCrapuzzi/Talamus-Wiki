---
type: concept
status: evergreen
aliases:
  - Memory System (LLM)
  - Context Management
tags:
  - ai-engineering
  - llm-architecture
  - state-management
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/122-summary.md
    locator: pages 329-330
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Both RAG and agents work with a lot of information, which often exceeds the maximum context length of the underlying model. This necessitates the introduction of a memory system for managing and using all the information a model has.
created: 2026-05-26T21:55:46.148563+00:00
updated: 2026-05-26T21:55:46.148563+00:00
ingestion_run: 8d527d59
---

# Memory System (LLM)

## Summary

A dedicated component designed to manage, store, and retrieve information that exceeds the maximum context length of the underlying LLM, allowing the model to maintain state and progress over long interactions.

## Core Idea

As both RAG and Agents deal with vast amounts of information, a memory system is necessary to prevent information loss and maintain coherence, enabling the model to 'remember' past steps and context.

## Practical Use

Implement a memory system when building multi-turn conversational agents or complex, multi-step workflows. This system must manage the history and relevant context to feed back into the prompt, augmenting the model's effective context window.

## Related

- [[AI-Agent-Framework|AI Agent Framework]]
- RAG
