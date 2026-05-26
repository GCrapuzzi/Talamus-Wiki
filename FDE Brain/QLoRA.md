---
type: method
tags: [QLoRA, quantization, LoRA, PEFT, finetuning, memory-efficiency]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#parameter-efficient-finetuning
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# QLoRA

**Quantized LoRA** (Dettmers et al., 2023) — combines 4-bit quantization of base model weights with LoRA adapters to dramatically reduce finetuning memory.

Key techniques:
- Store model weights in **NF4 (NormalFloat-4)** format, exploiting the normal distribution of pre-trained weights
- Dequantize to BF16 only for forward/backward pass computation
- **Paged optimizers**: automatically offload data between CPU and GPU when GPU memory is exhausted

Enables finetuning a **65B-parameter model on a single 48 GB GPU**.

The resulting Guanaco model family showed competitive performance: Guanaco 65B (41 GB) achieved Elo 1022 vs ChatGPT's 966 (GPT-4 judge, May 2023).

**Limitation**: NF4 quantization/dequantization is expensive—may increase training time despite reducing memory.

Other quantized LoRA variants: QA-LoRA, ModuLoRA, IR-QLoRA.
