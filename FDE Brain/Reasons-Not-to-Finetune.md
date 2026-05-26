---
type: concept
tags: [finetuning, decision-making, prompt-engineering, trade-offs]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#reasons-not-to-finetune
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Reasons Not to Finetune

Key counterarguments to finetuning:

1. **Task degradation**: finetuning on task A can hurt performance on tasks B and C (alignment tax). Mitigation: finetune on all tasks you care about, or use separate models and merge them
2. **High up-front investment**: requires annotated data, ML expertise (optimizers, learning rates, overfitting), model hosting/serving infrastructure, and ongoing maintenance budget
3. **Rapidly improving base models**: a new base model may outperform your finetuned model before you finish iterating
4. **Prompting often suffices**: many practitioners insist on finetuning prematurely—upon investigation, prompt experiments were minimal and unsystematic. Refining prompts with best practices often closes the gap
5. **General models beating specialized ones**: BloombergGPT (50B params, $1.3–2.6M compute) was significantly outperformed by GPT-4 zero-shot on financial benchmarks (FiQA F1: 87.15 vs 75.07)

**Rule of thumb**: exhaust prompt engineering before attempting finetuning. Prompt experiments also build the evaluation pipeline, annotation guidelines, and experiment tracking needed for finetuning.
