---
type: pattern
status: evergreen
aliases:
  - Foundational AI Architecture Pattern
  - RAG Pattern
  - Augmented Generation
tags:
  - ai-engineering
  - architecture
  - llm-design
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/004-preface.md
    locator: pages 13-13
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Retrieval-augmented generation (RAG) applications are built upon retrieval technology that has powered search and recommender systems since long before the term RAG was coined.
created: 2026-05-26T21:55:45.248473+00:00
updated: 2026-05-26T21:55:45.248473+00:00
ingestion_run: 8d527d59
---

# Foundational AI Architecture Pattern

## Summary

Modern AI applications, even those using advanced LLMs, are built upon established computing techniques (e.g., search, recommendation systems, retrieval). The LLM acts as the reasoning layer over existing, proven data retrieval mechanisms.

## Core Idea

AI innovation is often an integration pattern, not a pure invention. Understanding the underlying, stable components (like retrieval technology) allows engineers to build reliable, grounded systems.

## Practical Use

When designing an LLM application, first identify the core knowledge retrieval need. Implement a robust, traditional retrieval system (e.g., vector search) *before* integrating the LLM. This ensures the application is grounded in verifiable data.

## Related

- [[Retrieval-Augmented-Generation-RAG|Retrieval-Augmented Generation (RAG)]]
- Information Retrieval
