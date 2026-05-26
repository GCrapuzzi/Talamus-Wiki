---
type: concept
tags: [attention, transformer, KV-cache, multi-head-attention]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#model-architecture
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Attention Mechanism

The core mechanism of the [[Transformer Architecture]]. Allows the model to weigh the importance of different input tokens when generating each output token.

Uses three learned vector types:
- **Query (Q)**: represents the current decoder state — "the person looking for information"
- **Key (K)**: represents each previous token — "the page number"
- **Value (V)**: represents the actual content of each previous token — "the page content"

Computed via learned weight matrices applied to input: `K = xW_K`, `V = xW_V`, `Q = xW_Q`.

Attention score = dot product of Q and K. High score → more of that token's value is used.

$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d}}\right)V$$

**Multi-headed attention** splits Q, K, V into smaller vectors per head, allowing simultaneous attention to different token groups. E.g., Llama 2-7B: hidden dim 4096, 32 heads → each head operates on 128-dim vectors.

Key implication: longer sequences require more KV vectors to be stored, making context length extension difficult. This drives optimization techniques in inference (see Chapters 7 and 9).

Note: attention predates transformers by 3 years (Bahdanau et al., 2014) and was first used with RNNs.
