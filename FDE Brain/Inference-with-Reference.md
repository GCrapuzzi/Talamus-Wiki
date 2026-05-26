---
type: method
tags: [inference, decoding, optimization, RAG]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#model-optimization
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Inference with Reference

Accelerates autoregressive decoding by copying token spans directly from the input context instead of generating them, when the output overlaps significantly with the input.

Similar to [[Speculative Decoding]] but uses input text spans as draft tokens instead of a separate model. At each decode step, an algorithm identifies the most relevant span from context (simplest: match current token prefix). The target model verifies the copied span.

### Properties
- No extra model required.
- ~2× generation speedup in high-overlap scenarios (Yang et al., 2023).
- Most useful for: retrieval-augmented generation, code editing/bug fixing, multi-turn conversations where prior context is repeated.
- Not beneficial when output has low overlap with input.
