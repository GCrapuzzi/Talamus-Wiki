---
type: framework
tags: [ai-stack, architecture, evaluation, prompt-engineering, inference-optimization]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#three-layers-of-the-ai-stack
  - AI Space/normalized/pdf/ai-engineering.md#ai-engineering-versus-ml-engineering
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# AI Engineering Stack

Three-layer architecture for building AI applications, worked top-down:

### 1. Application Development
The layer with the most post-2023 innovation. Responsibilities:
- **Evaluation** — harder with open-ended outputs; no exhaustive ground truths. Different prompting techniques cause large performance swings (e.g. Gemini MMLU: 83.7% with 5-shot vs 90.04% with CoT@32).
- **Prompt Engineering & context construction** — adapting model behavior from input alone: instructions, examples, retrieved context, memory management.
- **AI interface** — standalone apps, browser extensions, chat integrations, voice, embodied. New interfaces → new feedback collection patterns.

### 2. Model Development
- **Modeling & training** — ML knowledge now nice-to-have, not required. Encompasses [[Pre-Training vs Finetuning vs Post-Training]].
- **Dataset engineering** — shifts from feature engineering on tabular data to deduplication, tokenization, context retrieval, quality control, and toxic/sensitive data removal.
- **Inference optimization** — even more critical as autoregressive generation is sequential (10 ms/token × 100 tokens = 1s). Techniques: quantization, distillation, parallelism.

### 3. Infrastructure
Core needs (serving, compute management, monitoring) remain largely unchanged from traditional ML. Saw the least growth post-ChatGPT.

Post-2023 GitHub data (920 repos, 500+ stars): application layer and applications saw the biggest jump; infrastructure grew modestly.
