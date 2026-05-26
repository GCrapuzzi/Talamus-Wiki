---
type: concept
tags: [distillation, knowledge-distillation, model-compression]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#model-distillation
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Model Distillation

Training a smaller **student** model to mimic a larger **teacher** model (Hinton et al., 2015). The teacher's knowledge is compressed into the student.

**Goal:** Produce smaller, faster models retaining comparable performance. DistilBERT achieved 97% of BERT's comprehension at 60% of the size and 60% faster.

**Approaches:**
- Train student from scratch (DistilBERT)
- Finetune a pre-trained student on teacher outputs (Alpaca: Llama-7B finetuned on text-davinci-003 outputs → 4% teacher size, similar behavior)
- Combine with [[LoRA]] for cost efficiency (e.g., BuzzFeed: 80% inference cost reduction)

**Not all synthetic training is distillation.** Distillation implies the teacher is the gold standard. Counterexamples:
- NVIDIA's Nemotron-4 340B student outperformed its 56B Mixtral teacher
- [[Reverse Instruction]] bootstrapping can iteratively improve beyond the original model

**Legal constraint:** Many model licenses prohibit using outputs to train competing models.

**Key finding (Llama 3):** Training on data from a more competent model helps, but indiscriminate self-generated data doesn't—quality verification is required for self-improvement.
