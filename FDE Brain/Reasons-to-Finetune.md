---
type: concept
tags: [finetuning, distillation, bias-mitigation, model-compression]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#reasons-to-finetune
  - AI Space/normalized/pdf/ai-engineering.md#when-to-finetune
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Reasons to Finetune

Primary motivations for finetuning:

1. **Quality improvement**: domain-specific capabilities (coding, medical QA) and task-specific output formats (JSON, YAML, domain-specific SQL dialects)
2. **Bias mitigation**: exposing model to curated data to counteract training biases (e.g., finetuning on text by women reduces gender bias in BERT-like models)
3. **Model compression via distillation**: finetune a small model to imitate a larger model. Grammarly's finetuned Flan-T5 outperformed a GPT-3 variant on writing tasks while being 60× smaller, using only 82K examples
4. **Token optimization**: finetuning encodes few-shot examples into weights, enabling shorter prompts (less relevant with [[Prompt Caching]], but finetuning has no context-length limit on example count)

Smaller models are more commonly finetuned—cheaper to train and serve. The open-source ecosystem has made finetuning increasingly viable with high-quality base models of all sizes.
