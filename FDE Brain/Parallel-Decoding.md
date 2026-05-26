---
type: method
tags: [inference, decoding, Medusa, Lookahead, parallel-decoding]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#model-optimization
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Parallel Decoding

Breaks the sequential dependency of autoregressive generation by predicting multiple future tokens simultaneously.

### Lookahead Decoding (Fu et al., 2024)
A single decoder generates K future tokens in parallel, verified via the **Jacobi method** — iteratively refine parallel tokens until all pass coherence checks.

### Medusa (Cai et al., 2024)
Extends the original model with multiple small decoding heads, each trained to predict a token at a specific future position (kth head predicts x_{t+k+1}). Original model is frozen during head training. Uses **tree-based attention** for verification: each head proposes several options, organized into a tree structure to select the best combination. NVIDIA reported up to 1.9× speedup on Llama 3.1 with HGX H200.

### Trade-offs
- Parallel tokens require verification, adding complexity.
- Medusa requires training additional heads and is harder to implement.
- Works because existing context often suffices to predict nearby tokens even without knowing immediate predecessors.
