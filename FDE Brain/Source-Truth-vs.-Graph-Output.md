---
type: pattern
status: evergreen
aliases:
  - Source Truth vs. Graph Output
  - Graph as Router, Markdown as Source
  - Knowledge Graph for Navigation
tags:
  - ai-engineering
  - rag
  - knowledge-graph
sources:
  - raw_path: AI Space/raw/markdown/2026-05-26-controlled-rollout-pattern.md
    normalized_path: AI Space/normalized/markdown/controlled-rollout-pattern/sections/001-controlled-rollout-pattern-for-local-first-llm-wikis.md
    locator: markdown
    source_hash: sha256:edf1e72906a78e3f2f5f27e600c5f6b94abae9606c75c0c9ecf29a645190aca2
    supported_claims:
      - The key decision rule is that graph output is never treated as source truth. Graphify is used for routing... The answering agent then reads the actual Markdown files in the Obsidian vault or normalized source packages before drafting an answer.
created: 2026-05-26T14:20:20.854827+00:00
updated: 2026-05-26T14:20:20.854827+00:00
ingestion_run: c1f8c7e7
---

# Source Truth vs. Graph Output

## Summary

A decision framework stating that the knowledge graph (Graphify output) must only be used for routing, concept labeling, and relation hinting, while the actual Markdown files or normalized source packages must always be treated as the definitive source of truth for answering questions.

## Core Idea

This separation prevents the system from hallucinating facts based on graph connections. The graph provides structure and connectivity (metadata), but the LLM answering agent must read the original, validated text content to generate an answer, ensuring factual grounding.

## Practical Use

When building an RAG system for the wiki, the engineer must configure the retrieval agent to prioritize fetching and citing chunks from the normalized Markdown source packages, even if the graph suggests a connection. The graph output is used only to identify *which* documents to retrieve.

## Related

- [[Controlled-Rollout-Pattern-for-Local-First-LLM-Wikis|Controlled Rollout Pattern for Local-First LLM Wikis]]
