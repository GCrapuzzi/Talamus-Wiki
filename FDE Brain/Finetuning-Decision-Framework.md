---
type: framework
status: evergreen
aliases:
  - Finetuning Decision Framework
  - When to Finetune
  - Finetuning vs Prompting
tags:
  - ai-engineering
  - llm-deployment
  - model-adaptation
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/126-reasons-to-finetune.md
    locator: pages 335-335
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Compared to prompt-based methods, finetuning requires significantly more resources, not just in data and hardware, but also in ML talent.
      - Therefore, finetuning is generally attempted after extensive experiments with prompt-based methods.
      - However, finetuning and prompting aren’t mutually exclusive.
created: 2026-05-26T21:55:46.181448+00:00
updated: 2026-05-26T21:55:46.181448+00:00
ingestion_run: 8d527d59
---

# Finetuning Decision Framework

## Summary

A structured approach for determining if finetuning is necessary, prioritizing less resource-intensive methods first.

## Core Idea

Finetuning is a high-resource intervention (data, hardware, ML talent) and should generally be attempted only after extensive experimentation with prompt-based methods. However, the two approaches are complementary and often required together in real-world applications.

## Practical Use

Before spending resources on finetuning, first attempt to solve the problem using advanced prompting techniques (e.g., few-shot prompting, Chain-of-Thought). If prompting fails to achieve the required performance or structure, then proceed to finetuning.

## Related

- Prompt Engineering Playbook
- [[Structured-Output-Generation|Structured Output Generation]]
