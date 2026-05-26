---
type: method
tags: [sampling, temperature, top-k, top-p, logprobs, inference]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#sampling-fundamentals
  - AI Space/normalized/pdf/ai-engineering.md#sampling-strategies
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Sampling Strategies

Techniques to control how a language model selects output tokens from its probability distribution.

**Core pipeline**: input → logit vector → (optional adjustment) → softmax → probability distribution → token selection.

**Temperature**: divides logits by T before softmax.
- T < 1: sharpens distribution → more deterministic, less creative
- T > 1: flattens distribution → more random, more creative
- T = 0 (practical): greedy sampling (argmax), picks highest-logit token
- Common creative setting: T = 0.7

**Top-k**: compute softmax over only the k highest logits. Reduces computation; k typically 50–500.

**Top-p (nucleus sampling)**: dynamically select the smallest set of tokens whose cumulative probability exceeds p (typically 0.9–0.95). More context-adaptive than top-k.

**Min-p**: set minimum probability threshold for token consideration.

**Stopping conditions**: max tokens (may truncate mid-sentence), stop tokens/words (e.g., EOS). Premature stopping can break structured output formats.

**Logprobs**: probabilities in log scale to avoid underflow. Useful for classification, evaluation, and debugging. Many providers limit logprob access for security reasons.

See also: [[Test Time Compute]], [[Structured Outputs]].
