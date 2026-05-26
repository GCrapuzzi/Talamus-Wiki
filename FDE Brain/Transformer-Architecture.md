---
type: framework
tags: [transformer, architecture, seq2seq, attention, foundation-models]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#model-architecture
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Transformer Architecture

The dominant architecture for language-based foundation models (since Vaswani et al., 2017). Built on the [[Attention Mechanism]], it solved two problems with the prior seq2seq (RNN-based) architecture:

1. **Information bottleneck**: seq2seq decoder used only the final hidden state (like summarizing a book from its summary). Transformers attend to all input tokens directly.
2. **Sequential processing**: RNNs process tokens sequentially. Transformers process input tokens in parallel.

**Inference has two phases:**
- **Prefill**: processes input tokens in parallel, producing KV vectors for all input tokens
- **Decode**: generates output tokens one at a time (still sequential)

**Transformer block** contains:
- **Attention module**: query, key, value, and output projection weight matrices
- **MLP module**: linear (feedforward) layers separated by nonlinear activation functions (ReLU, GELU)

A transformer model also includes:
- **Embedding module** (before blocks): embedding matrix + positional embedding matrix
- **Output layer / unembedding layer** (after blocks): maps output vectors to token probabilities

Model size is determined by: model dimension, number of transformer blocks (layers), feedforward dimension, and vocabulary size.

See also: [[Attention Mechanism]], [[State Space Models]].
