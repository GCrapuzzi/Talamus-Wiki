---
type: method
status: evergreen
aliases:
  - Partial Finetuning
  - Layer Freezing
tags:
  - ai-engineering
  - finetuning
  - memory-optimization
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/135-parameter-efficient-finetuning.md
    locator: pages 356-370
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - In partial finetuning, only some of the model's parameters are updated.
      - While partial finetuning can reduce the memory footprint, it’s parameter-inefficient.
      - A study by Houlsby et al. (2019) shows that with BERT large, you’d need to update approximately 25% of the parameters.
created: 2026-05-26T21:55:46.255332+00:00
updated: 2026-05-26T21:55:46.255332+00:00
ingestion_run: 8d527d59
---

# Partial Finetuning

## Summary

A technique where only a specific subset of layers or parameters (e.g., the output layers) are updated, while the remaining layers are frozen and kept constant.

## Core Idea

Partial finetuning reduces the memory footprint by limiting the number of trainable parameters. However, it is parameter-inefficient; achieving performance comparable to full finetuning often requires updating a significantly larger percentage of parameters than initially anticipated.

## Practical Use

Use partial finetuning as an intermediate step when full finetuning is too costly, but PEFT methods are not yet feasible or appropriate. Be aware that performance gains may plateau unless a sufficient number of parameters are updated.

## Related

- [[Parameter-Efficient-Finetuning-PEFT|Parameter-Efficient Finetuning (PEFT)]]
- [[Full-Finetuning|Full Finetuning]]
