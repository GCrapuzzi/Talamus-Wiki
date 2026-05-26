---
type: glossary
tags: [pre-training, finetuning, post-training, training, glossary]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#ai-engineering-versus-ml-engineering
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Pre-Training vs Finetuning vs Post-Training

Three phases of model training that form a spectrum:

- **Pre-training**: training from scratch (randomly initialized weights). For LLMs, typically text completion. Consumes up to 98% of total compute and data resources (per InstructGPT). Extremely expensive; mistakes are costly. A specialized art practiced by few.

- **Finetuning**: continuing to train a previously trained model. Weights come from pre-training. Requires fewer resources since the model already has foundational knowledge. Done by **application developers** to adapt a model to their needs.

- **Post-training**: conceptually identical to finetuning, but done by **model developers** (e.g. OpenAI training a model to follow instructions before release).

All three involve updating model weights. **Prompt engineering is not training** — it adapts behavior via context input without weight changes.

Note: **quantization** changes weight values (reduces precision) but is not considered training.
