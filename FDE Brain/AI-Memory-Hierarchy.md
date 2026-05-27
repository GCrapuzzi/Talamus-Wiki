---
type: glossary
status: evergreen
aliases:
  - AI Memory Hierarchy
  - Model Memory Types
  - Information Retention Mechanisms
tags:
  - ai-engineering
  - memory
  - llm-architecture
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/121-memory.md
    locator: pages 324-328
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - "Internal knowledge: Model retains knowledge from training data, does not change unless model is updated."
      - "Short-term memory: Model's context, limited capacity, does not persist across tasks."
      - "Long-term memory: External data sources accessed via retrieval (RAG), persists across tasks, can be deleted without updating the model."
created: 2026-05-26T21:55:46.130007+00:00
updated: 2026-05-26T21:55:46.130007+00:00
ingestion_run: 8d527d59
---

# AI Memory Hierarchy

## Summary

Defines the three primary mechanisms for information retention in AI models: Internal (training knowledge), Short-term (context window), and Long-term (external retrieval).

## Core Idea

AI models require structured memory management to handle information that exceeds context limits and to maintain state across interactions. Understanding the source of knowledge (training vs. external) dictates how it should be managed.

## Practical Use

When designing an agent, classify data based on its permanence and scope. Core domain knowledge goes into fine-tuning (Internal). Immediate task details go into the prompt/context (Short-term). Persistent, large-scale data (e.g., user history, knowledge base) must be stored externally and retrieved (Long-term/RAG).

## Related

- RAG System
- Agentic Workflow
