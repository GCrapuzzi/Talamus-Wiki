---
type: concept
status: evergreen
aliases:
  - AI Component Definition
  - System Components
  - Pipeline Modules
tags:
  - ai-engineering
  - architecture
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/173-ai-pipeline-orchestration.md
    locator: pages 496-497
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - You need to tell the orchestrator what components your system uses, including different models, external data sources for retrieval, and tools that your system can use.
created: 2026-05-26T21:55:46.558860+00:00
updated: 2026-05-26T21:55:46.558860+00:00
ingestion_run: 8d527d59
---

# AI Component Definition

## Summary

The explicit identification and definition of all functional units within an AI system, including LLMs, external data sources (databases), and specialized tools.

## Core Idea

Before building the pipeline, all inputs and capabilities must be cataloged. This includes defining the model gateway, the data retrieval mechanism, and any evaluation/monitoring tools that will interact with the core process.

## Practical Use

Create an inventory of all system parts. For example: Component A (LLM API), Component B (Vector DB), Component C (PII Filter Tool). The orchestrator then connects these defined components.

## Related

- [[AI-Pipeline-Orchestration|AI Pipeline Orchestration]]
