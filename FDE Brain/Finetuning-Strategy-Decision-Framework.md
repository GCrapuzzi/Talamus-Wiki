---
type: framework
status: evergreen
aliases:
  - Finetuning Strategy Decision Framework
  - When to Finetune vs RAG
tags:
  - ai-engineering
  - architecture
  - decision-making
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/138-summary.md
    locator: pages 385-386
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - "It also discussed one question that I have been asked many times: when to finetune and when to do RAG."
created: 2026-05-26T21:55:46.288515+00:00
updated: 2026-05-26T21:55:46.288515+00:00
ingestion_run: 8d527d59
---

# Finetuning Strategy Decision Framework

## Summary

A structured decision process for determining the optimal approach (Finetuning, RAG, or Prompt Engineering) based on the nature of the knowledge update, resource constraints, and desired behavioral change.

## Core Idea

Guides engineers to avoid over-engineering by systematically evaluating whether the goal is to update *knowledge* (RAG) or update *behavior/style* (Finetuning).

## Practical Use

Before starting a project, ask: 1) Is the knowledge static and external (Use RAG)? 2) Does the model need to change its underlying style, tone, or format (Use Finetuning)? 3) Are resources sufficient for full finetuning (Use PEFT/LoRA)?

## Related

- [[Retrieval-Augmented-Generation-RAG|Retrieval-Augmented Generation (RAG)]]
- [[Prompt-Engineering|Prompt Engineering]]
- PEFT
