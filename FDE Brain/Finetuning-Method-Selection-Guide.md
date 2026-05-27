---
type: framework
status: evergreen
aliases:
  - Finetuning Method Selection Guide
  - LoRA vs Full Finetuning
  - Data Volume Finetuning Strategy
tags:
  - ai-engineering
  - finetuning
  - optimization
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/137-finetuning-tactics.md
    locator: pages 381-384
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - LoRA is cost-effective but may not match full finetuning performance.
      - Full finetuning requires at least thousands of examples.
      - LoRA allows serving multiple models that share the same base model, requiring only one full model to be served.
created: 2026-05-26T21:55:46.271115+00:00
updated: 2026-05-26T21:55:46.271115+00:00
ingestion_run: 8d527d59
---

# Finetuning Method Selection Guide

## Summary

A decision guide for selecting a finetuning method based on data volume, performance requirements, and deployment constraints.

## Core Idea

The choice between Parameter-Efficient Finetuning (PEFT) methods like LoRA and Full Finetuning is a trade-off between performance ceiling and resource efficiency. LoRA is ideal for small datasets and serving multiple models efficiently.

## Practical Use

If the dataset is small (hundreds of examples), start with LoRA. If maximum performance is required and data volume is high (thousands of examples), consider full finetuning. If multiple specialized models are needed, LoRA is preferred as it allows serving multiple models sharing one base model.

## Related

- LoRA
- Model Serving Optimization
