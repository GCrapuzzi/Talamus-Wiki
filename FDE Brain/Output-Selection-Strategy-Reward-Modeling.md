---
type: method
status: evergreen
aliases:
  - "Output Selection Strategy: Reward Modeling"
  - Verifier scoring
  - Discriminative scoring
tags:
  - ai-engineering
  - llm-evaluation
  - rlhf
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/051-test-time-compute.md
    locator: pages 120-122
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Another selection method is to use a reward model to score each output...
      - OpenAI also trained verifiers to help their models pick the best solutions to math problems...
created: 2026-05-26T21:55:45.593199+00:00
updated: 2026-05-26T21:55:45.593199+00:00
ingestion_run: 8d527d59
---

# Output Selection Strategy: Reward Modeling

## Summary

Using a separate, specialized model (a Reward Model or Verifier) to score or evaluate the quality, adherence, or correctness of each generated output, rather than relying solely on intrinsic language model probabilities.

## Core Idea

Reward models can capture complex, task-specific criteria (e.g., factual accuracy, adherence to schema, tone) that are difficult to encode purely through token probability, significantly boosting performance.

## Practical Use

For critical applications (e.g., code generation, medical summarization), pipeline the LLM output through a fine-tuned Reward Model. The output with the highest score from the verifier is selected as the final answer.

## Related

- [[Test-Time-Compute-TTC|Test Time Compute (TTC)]]
- Fine-tuning
