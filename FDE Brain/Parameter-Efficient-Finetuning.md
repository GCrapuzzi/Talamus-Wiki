---
type: concept
tags: [PEFT, finetuning, LoRA, adapters, soft-prompts, memory-efficiency]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#parameter-efficient-finetuning
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Parameter-Efficient Finetuning

PEFT achieves performance close to full finetuning using several orders of magnitude fewer trainable parameters, dramatically reducing memory requirements.

**Motivation**: Full finetuning a 7B model in FP16 with Adam needs ~56 GB (14 GB weights + 42 GB gradients/optimizer)—exceeding most consumer GPUs (12–48 GB), before even counting activations.

**Two main families**:

1. **Adapter-based (additive) methods**: insert small trainable modules into the model
   - Original adapters (Houlsby et al., 2019): 0.4% of full finetuning performance gap with 3% of parameters on GLUE, but adds inference latency
   - [[LoRA]]: dominant technique, no inference latency overhead
   - IA3, LongLoRA, BitFit

2. **Soft prompt-based methods**: prepend trainable continuous vectors (not human-readable) to inputs
   - Prefix-tuning: soft prompts at every transformer layer
   - Prompt tuning: soft prompts only at the embedded input
   - P-Tuning: similar family
   - Crossover between prompt engineering and finetuning

PEFT methods are generally also **sample-efficient**—strong performance with just a few thousand examples vs. tens of thousands for full finetuning.

Analysis of 1,000+ GitHub issues on huggingface/peft (Oct 2024) shows LoRA dominates overwhelmingly.
