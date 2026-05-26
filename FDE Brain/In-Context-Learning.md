---
type: concept
tags: [prompt-engineering, few-shot, zero-shot, in-context-learning, foundation-models]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#in-context-learning-zero-shot-and-few-shot
  - AI Space/normalized/pdf/ai-engineering.md#system-prompt-and-user-prompt
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# In-Context Learning

Teaching models desired behavior via examples and instructions placed directly in the prompt, without updating model weights. Introduced by Brown et al. (2020) in the GPT-3 paper.

A foundation model encodes many latent "programs" from pre-training. A prompt activates the relevant program (François Chollet's analogy: the model is a library of programs, and prompting selects which one runs).

In-context learning enables **continual learning** — new information (e.g., updated API docs) can be injected at inference time, keeping the model current beyond its training cutoff.

### Shot terminology
- **Zero-shot** — no examples provided; relies entirely on instruction-following.
- **Few-shot (k-shot)** — k examples included in the prompt.

As models grow stronger, the marginal gain from few-shot over zero-shot shrinks for common tasks (Microsoft 2023 analysis on GPT-4). Few-shot remains high-value for **domain-specific tasks** where the model saw little training data (e.g., niche dataframe APIs).

Trade-off: more examples → better learning but longer prompt → higher cost and latency, bounded by Context Length.
