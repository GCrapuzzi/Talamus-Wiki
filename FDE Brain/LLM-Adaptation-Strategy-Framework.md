---
type: framework
status: evergreen
aliases:
  - LLM Adaptation Strategy Framework
  - Finetuning vs RAG vs Prompting Decision Flow
tags:
  - ai-engineering
  - llm-architecture
  - deployment-strategy
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/123-chapter-7.-finetuning.md
    locator: pages 331-331
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - this chapter will discuss the reasons for finetuning and the reasons for not finetuning, as well as a simple framework for thinking about choosing between finetuning and alternate methods.
created: 2026-05-26T21:55:46.156076+00:00
updated: 2026-05-26T21:55:46.156076+00:00
ingestion_run: 8d527d59
---

# LLM Adaptation Strategy Framework

## Summary

A decision framework for AI engineers to determine the optimal method (Prompting, RAG, or Finetuning) for customizing an LLM's behavior based on the required change type, data source, and complexity.

## Core Idea

The choice of adaptation method dictates the cost, complexity, and permanence of the change. Prompting is for immediate instructions; RAG is for external, up-to-date knowledge; Finetuning is for deep, structural behavioral changes.

## Practical Use

Before committing to finetuning (which is costly), use this framework: 1. If the issue is knowledge retrieval, use RAG. 2. If the issue is format/style adherence, try advanced prompting. 3. Only if the model fundamentally fails to adopt a required behavior or domain style should finetuning be considered.

## Related

- [[Finetuning|Finetuning]]
- [[Retrieval-Augmented-Generation-RAG|Retrieval-Augmented Generation (RAG)]]
- [[Prompt-Engineering|Prompt Engineering]]
