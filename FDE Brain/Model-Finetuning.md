---
type: method
status: evergreen
aliases:
  - Model Finetuning
  - Model Adaptation
  - Parameter Tuning
tags:
  - ai-engineering
  - llm-deployment
  - finetuning
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/009-conventions-used-in-this-book.md
    locator: pages 19-19
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Chapter 7 is about how to adapt a model to an application by changing the model itself with finetuning.
      - native model finetuning is memory-intensive, and many techniques are developed to allow finetuning better models with less memory.
      - "The chapter covers different finetuning approaches, supplemented by a more experimental approach: model merging."
created: 2026-05-26T21:55:45.297609+00:00
updated: 2026-05-26T21:55:45.297609+00:00
ingestion_run: 8d527d59
---

# Model Finetuning

## Summary

Process of adapting a large foundation model to a specific application domain or task by modifying the model's weights.

## Core Idea

Finetuning is necessary to tailor general-purpose foundation models for specialized tasks. Due to the massive scale of modern models, techniques like parameter-efficient finetuning (PEFT) and model merging are crucial to manage memory and computational costs.

## Practical Use

When a general LLM performs poorly on domain-specific jargon or tasks, finetuning is the primary method to improve its performance. Engineers must select the appropriate finetuning technique (e.g., LoRA, QLoRA) based on available compute resources and desired performance gain.

## Related

- [[Model-Merging|Model Merging]]
- Data Quality Management
