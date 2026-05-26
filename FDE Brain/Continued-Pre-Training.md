---
type: method
tags: [finetuning, self-supervised-learning, domain-adaptation]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#finetuning-overview
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Continued Pre-Training

Self-supervised finetuning on cheap, task-related but unannotated data before expensive supervised finetuning. Also called **continued pre-training**.

Examples:
- Before finetuning on annotated (question, answer) pairs for legal QA, finetune on raw legal documents
- Before finetuning for Vietnamese book summarization, finetune on a large Vietnamese text corpus

This bridges the domain gap between the general pre-training corpus and the target task without requiring expensive annotations. The model can also be finetuned for **infilling** (fill-in-the-blank) even if originally pre-trained autoregressively—useful for text editing and code debugging.
