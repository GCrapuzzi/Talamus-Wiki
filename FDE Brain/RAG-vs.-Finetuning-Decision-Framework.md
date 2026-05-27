---
type: framework
status: evergreen
aliases:
  - RAG vs. Finetuning Decision Framework
  - AI Model Failure Diagnosis
  - RAG vs Finetuning Guide
tags:
  - ai-engineering
  - llm-deployment
  - architecture
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/128-finetuning-and-rag.md
    locator: pages 340-342
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - The answer depends on whether your model’s failures are information-based or behavior-based.
      - If the model fails because it lacks information, a RAG system... can help.
      - If the model has behavioral issues, finetuning might help.
created: 2026-05-26T21:55:46.198750+00:00
updated: 2026-05-26T21:55:46.198750+00:00
ingestion_run: 8d527d59
---

# RAG vs. Finetuning Decision Framework

## Summary

A decision framework to determine whether a model's performance gap is due to lack of information (use RAG) or poor adherence to format/style (use Finetuning).

## Core Idea

The failure mode dictates the solution. If the model is factually wrong or outdated (information-based failure), RAG is needed. If the model is factually correct but irrelevant, or fails to follow a specific format (behavior-based failure), Finetuning is needed.

## Practical Use

When a model fails, first diagnose the failure type. If the failure is 'I don't know that' or 'That information is old,' implement RAG. If the failure is 'I know it, but I formatted it wrong' or 'I missed the specific technical style,' implement Finetuning.

## Related

- [[Retrieval-Augmented-Generation-RAG|Retrieval-Augmented Generation (RAG)]]
- Model Behavior Correction
- [[Evaluation-Pipeline-Design|Evaluation Pipeline Design]]
