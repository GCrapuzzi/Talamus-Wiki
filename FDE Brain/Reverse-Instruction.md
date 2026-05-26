---
type: method
tags: [instruction-tuning, synthetic-data, data-synthesis]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#ai-powered-data-synthesis
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Reverse Instruction

Instead of generating responses from instructions, take existing high-quality long-form content (books, Wikipedia articles, stories) and use AI to generate instructions that would elicit that content.

**Advantage:** The response quality is guaranteed (it's real, human-written content), avoiding AI hallucinations in the most consequential part of training data.

**Iterative bootstrapping** (Li et al., 2023):
1. Train a weak model on small seed examples
2. Use the weak model to generate instructions for existing high-quality content
3. Finetune on the resulting high-quality instruction data
4. Repeat until target performance is reached

This enables developing increasingly powerful models without adding manually annotated data—the student can theoretically surpass the teacher through access to better response data.
