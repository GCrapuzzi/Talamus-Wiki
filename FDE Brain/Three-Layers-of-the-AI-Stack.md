---
type: framework
status: evergreen
aliases:
  - Three Layers of the AI Stack
  - AI Application Stack
  - AI Engineering Stack
tags:
  - ai-engineering
  - architecture
  - mlops
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/034-three-layers-of-the-ai-stack.md
    locator: pages 61-62
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - The stack consists of application development, model development, and infrastructure.
      - Application development involves providing a model with good prompts and necessary context.
      - Model development includes frameworks for modeling, training, finetuning, and inference optimization, and dataset engineering.
      - Infrastructure includes tooling for model serving, managing data and compute, and monitoring.
created: 2026-05-26T21:55:45.473179+00:00
updated: 2026-05-26T21:55:45.473179+00:00
ingestion_run: 8d527d59
---

# Three Layers of the AI Stack

## Summary

A foundational architectural model dividing any AI application into three distinct, hierarchical layers: Application Development (the user interface and prompt logic), Model Development (training, finetuning, and dataset engineering), and Infrastructure (serving, compute management, and monitoring).

## Core Idea

AI development requires addressing three separate concerns. By separating the stack, engineers can isolate problems (e.g., poor UX vs. poor model accuracy vs. deployment failure) and apply specialized tooling and expertise to each layer, rather than treating the system as a single monolithic unit.

## Practical Use

When scoping an AI project, use this framework to define responsibilities. 
1. **Application:** Focus on prompt engineering, context management, and UI/UX. (Start here).
2. **Model:** Focus on data quality, training pipelines, and optimization. (If performance is insufficient).
3. **Infrastructure:** Focus on scalability, model serving endpoints, and monitoring pipelines. (For reliable deployment).

## Related

- MLOps
- [[Prompt-Engineering|Prompt Engineering]]
- Data Pipeline Architecture
