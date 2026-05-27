---
type: method
status: evergreen
aliases:
  - AI Pipeline Chaining (Function Composition)
  - Pipelining
  - Sequential Component Execution
tags:
  - ai-engineering
  - llm
  - design-pattern
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/173-ai-pipeline-orchestration.md
    locator: pages 496-497
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - "Chaining is basically function composition: it combines different functions (components) together."
      - In chaining (pipelining), you tell the orchestrator the steps your system takes from receiving the user query until completing the task.
created: 2026-05-26T21:55:46.554660+00:00
updated: 2026-05-26T21:55:46.554660+00:00
ingestion_run: 8d527d59
---

# AI Pipeline Chaining (Function Composition)

## Summary

The process of defining the ordered steps (functions/components) that an AI system must execute from receiving the initial user query until the final output is generated. The orchestrator manages the data transformation between these steps.

## Core Idea

Chaining treats the entire AI process as a series of dependent functions. The output of step N must be correctly formatted and passed as the input to step N+1. This ensures data integrity and logical flow.

## Practical Use

Define the exact sequence of operations: e.g., (1) Pre-process query -> (2) Retrieve context -> (3) Construct prompt -> (4) Generate response -> (5) Evaluate response. The orchestrator handles the data passing at each boundary.

## Related

- [[AI-Pipeline-Orchestration|AI Pipeline Orchestration]]
- [[Prompt-Engineering|Prompt Engineering]]
