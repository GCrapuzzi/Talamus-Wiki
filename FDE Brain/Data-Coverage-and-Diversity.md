---
type: concept
tags: [data-diversity, data-coverage, finetuning, llama]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#data-coverage
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Data Coverage and Diversity

Training data must cover the range of problems the model will face. Coverage requires diversity across multiple axes:

- **Task types** — summarization, QA, classification, etc.
- **Topics** — domain breadth matching user distribution
- **Input styles** — detailed vs. terse instructions, typos, multiple languages
- **Output formats** — JSON, yes/no, open-ended, varying lengths
- **Turn count** — single-turn and multi-turn interactions

Llama 3's gains were "primarily driven by improvements in data quality and diversity." Their training mix across phases shows different optimal domain ratios (e.g., math+code ≈50% in pre-training/SFT but only ≈13% in preference finetuning).

Scaling instruction-finetuned models showed performance increased significantly from 9→282 finetuning tasks, with diminishing but positive gains up to 1,836 tasks.

**Caution:** Adding heterogeneous data can sometimes hurt performance (Shen et al., 2024). The right mix requires experimentation—Meta used Scaling Laws experiments on small models to predict optimal mixes for large models.
