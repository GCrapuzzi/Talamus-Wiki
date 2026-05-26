---
type: method
tags: [inference, decoding, speculative-decoding, latency-optimization]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#model-optimization
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Speculative Decoding

Uses a fast, weaker **draft model** to propose K tokens, then the **target model** verifies them in parallel. Accepted tokens are kept; the target model generates one additional token after the last accepted draft token.

### Why it works
1. **Verification is cheaper than generation** — verification is parallelizable (prefill-like), generation is sequential.
2. **Many tokens are predictable** — a weaker model can get "easy" tokens right, yielding high acceptance rates.
3. **Decode has idle FLOPs** — bandwidth-bound decoding leaves spare compute for free verification.

### Key properties
- Worst case (all rejected): produces 1 token (target-generated) + verification overhead.
- Best case (all accepted): produces K + 1 tokens per loop.
- **Does not change model quality** — only the target model's distribution matters.
- Acceptance rates are domain-dependent; structured outputs (code) have higher rates.
- Draft model should share vocabulary/tokenizer with target.

DeepMind: 4B draft model for Chinchilla-70B achieved >2× latency reduction (1.8 ms/token draft vs 14.1 ms/token target). Supported in vLLM, TensorRT-LLM, llama.cpp. Implementable in ~50 lines of PyTorch.
