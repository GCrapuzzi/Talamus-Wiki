---
type: method
tags: [gradient-checkpointing, memory-optimization, training, activations]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#memory-math
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Gradient Checkpointing

Also called **activation recomputation**. A memory-saving technique that avoids storing all activation values during the forward pass by recomputing them on-the-fly during the backward pass.

Activation memory can dwarf model weight memory (especially for large sequence lengths and batch sizes). By not storing activations, training memory drops significantly at the cost of increased training time due to recomputation.

Trade-off: **memory ↓, compute time ↑**. Useful when GPU memory is the binding constraint.
