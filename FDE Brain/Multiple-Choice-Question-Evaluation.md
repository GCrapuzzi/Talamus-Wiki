---
type: method
tags: [evaluation, benchmarks, methodology]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#domain-specific-capability
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Multiple-Choice Question Evaluation

MCQs are the dominant format for evaluating domain-specific capabilities. As of April 2024, 75% of tasks in Eleuther's lm-evaluation-harness are multiple-choice (MMLU, AGIEval, ARC-C).

**Advantages:** easy to create, verify, and compare against random baselines (4 options → 25% random baseline).

**Limitations:**
- MCQs test ability to **differentiate** good from bad (classification), not ability to **generate** good responses
- Model performance is sensitive to minor prompt variations — an extra space or an added instructional phrase like "Choices:" can flip answers (Alzahrani et al. 2024)
- Best suited for evaluating **knowledge** and **reasoning**, not generation tasks like summarisation or translation

Metrics: accuracy, F1/precision/recall (for classification), point systems for harder questions or multi-correct answers.
