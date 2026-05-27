---
type: pattern
status: evergreen
aliases:
  - Parameter-Efficient Finetuning (PEFT)
  - Parameter-Efficient Fine-Tuning
tags:
  - ai-engineering
  - finetuning
  - llm-optimization
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/135-parameter-efficient-finetuning.md
    locator: pages 356-370
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - A technique is considered parameter-efficient if it can achieve performance close to that of full finetuning while using several orders of magnitude fewer trainable parameters.
      - PEFT was introduced by Houlsby et al. (2019) by inserting additional parameters (adapters) into the model.
      - PEFT enables finetuning on more affordable hardware, making it accessible to many more developers.
created: 2026-05-26T21:55:46.252480+00:00
updated: 2026-05-26T21:55:46.252480+00:00
ingestion_run: 8d527d59
---

# Parameter-Efficient Finetuning (PEFT)

## Summary

A set of techniques designed to adapt large pre-trained models to specific tasks by updating only a small subset of parameters, significantly reducing computational and memory requirements compared to full finetuning.

## Core Idea

PEFT addresses the prohibitive memory and data costs of full finetuning. By freezing the majority of the original model weights and introducing or updating only small, specialized modules (like adapters), it achieves performance comparable to full finetuning while drastically reducing the number of trainable parameters (often by orders of magnitude).

## Practical Use

When adapting a large foundation model (e.g., LLama, GPT) to a niche domain or task, use PEFT (e.g., LoRA, adapters) to minimize GPU memory usage, allowing deployment on consumer-grade or less powerful hardware. This is crucial for democratizing model customization.

## Related

- [[Full-Finetuning|Full Finetuning]]
- [[Quantization|Quantization]]
- [[Mixed-Precision-Training|Mixed Precision Training]]
