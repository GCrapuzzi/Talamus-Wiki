---
type: framework
tags: [finetuning, RAG, decision-framework, model-adaptation]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#finetuning-and-rag
  - AI Space/normalized/pdf/ai-engineering.md#when-to-finetune
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Finetuning vs RAG Decision Framework

**Core heuristic**: finetuning is for *form*, RAG is for *facts*.

Diagnose failure mode first:

| Failure type | Symptom | Remedy |
|---|---|---|
| **Information-based** | Outputs factually wrong or outdated; model lacks private/current knowledge | RAG |
| **Behavior-based** | Outputs correct but irrelevant, wrong format, wrong style, unsafe | Finetuning |
| **Both** | Start with RAG (easier, bigger boost), add finetuning later |

Ovadia et al. (2024) showed RAG outperforms finetuning on current-events QA, and RAG with a base model can outperform RAG with a finetuned model (finetuning may degrade RAG compatibility).

**Recommended progression:**
1. Prompt engineering with best practices
2. Add few-shot examples (1–50)
3. Simple retrieval (BM25 term-based) if information gaps exist
4. Branch: advanced RAG (embedding-based) for information failures OR finetuning for behavioral failures
5. Combine RAG + finetuning for maximum performance

Always establish an Evaluation Pipeline before any adaptation step.
