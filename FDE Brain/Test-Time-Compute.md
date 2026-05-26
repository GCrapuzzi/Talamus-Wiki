---
type: method
tags: [test-time-compute, best-of-n, beam-search, verifier, inference-optimization]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#test-time-compute
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Test Time Compute

Allocating additional compute at inference to improve response quality by generating multiple outputs and selecting the best one.

**Selection methods:**
- **Highest average logprob**: probability of sequence = product of token probabilities. Use average to avoid bias toward shorter sequences
- **Reward model / verifier**: score outputs and pick the highest. Nextdoor found this was the key factor in performance improvement
- **Majority voting (self-consistency)**: pick the most common answer among outputs — effective for exact-answer tasks (math, multiple choice). Google used 32 samples per question for Gemini MMLU evaluation
- **Application-specific heuristics**: shortest response, first valid output, etc.

**Key findings:**
- A verifier can provide performance equivalent to a **30x model size increase** (OpenAI, Cobbe et al. 2021)
- DeepMind (Snell et al., 2024): scaling test time compute can be more efficient than scaling model parameters
- Diminishing returns: OpenAI saw performance peak at ~400 samples then decline (verifier fooling). Stanford (Brown et al., 2024) found log-linear improvement up to 10K samples

**Practical tip**: vary sampling variables across outputs to increase diversity. For latency-sensitive apps, generate in parallel and serve the first valid response.

See also: [[Sampling Strategies]], [[Post-Training Pipeline]].
