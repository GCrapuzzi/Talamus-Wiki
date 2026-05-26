---
type: concept
tags: [hallucination, self-delusion, alignment, reliability, factuality]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#the-probabilistic-nature-of-ai
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Hallucination

When a model generates responses not grounded in facts. A consequence of the [[Sampling Strategies|probabilistic nature]] of language models. Predates transformers — mentioned in text generation literature since 2016.

**Two complementary hypotheses for why hallucinations occur:**

1. **Self-delusion** (Ortega et al., DeepMind, 2021): the model can't differentiate between given data and its own generated tokens. Once it generates a slightly wrong statement, it treats that as fact and snowballs — Zhang et al. (2023) call this "snowballing hallucinations." Mitigations: RL to differentiate observations from actions; factual/counterfactual signals in training data.

2. **Knowledge mismatch** (Leo Gao, OpenAI): during SFT, labelers write responses using knowledge the model doesn't have, effectively teaching it to confabulate. Mitigations: verification (ask model to cite sources); better reward functions that penalize fabrication.

**Practical mitigations:**
- Prompt: "Answer as truthfully as possible; if unsure, say 'I don't know'"
- Request concise responses (fewer tokens → less hallucination opportunity)
- Use RAG / context construction (Chapters 5–6)
- Test time compute with verification

**Paradox**: RLHF was shown to *worsen* hallucination in InstructGPT while improving overall preference.

See also: [[Post-Training Pipeline]], [[Test Time Compute]].
