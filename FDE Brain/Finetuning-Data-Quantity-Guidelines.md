---
type: framework
tags: [finetuning, data-quantity, scaling, peft]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#data-quantity
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Finetuning Data Quantity Guidelines

How much finetuning data you need depends on three factors beyond quality and diversity:

1. **Finetuning technique** — full finetuning needs 10K–millions of examples; [[LoRA]] and other PEFT methods work with hundreds to low thousands
2. **Task complexity** — simple classification needs far less data than complex QA
3. **Base model performance** — stronger base models need fewer examples to reach target performance (opposite of pre-training)

**Practical protocol:**
- Start with ~50 well-crafted examples to validate that finetuning helps at all
- If improvement is seen, plot a **performance gain curve** by training on 25%, 50%, 100% subsets
- Steep slope → more data will help significantly; plateau → diminishing returns
- If no improvement with 50–100 examples, a bigger dataset rarely fixes it—check hyperparameters, data quality, and prompt design first

**Key finding:** With few examples (100), more advanced base models win. With many examples (550K), all models converge to similar performance.

**Rule of thumb:** Small data → PEFT on advanced models. Large data → full finetuning on smaller models.
