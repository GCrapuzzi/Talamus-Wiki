---
type: concept
tags: [quantization, inference-optimization, memory, numerical-precision, PTQ, QAT]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#numerical-representations
  - AI Space/normalized/pdf/ai-engineering.md#quantization
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Quantization

Converting model values from a higher-precision format to a lower-precision format to reduce memory footprint. A 10B-param model in FP32 = 40 GB; in FP16 = 20 GB.

**Common numerical formats (bits / type)**:
- FP32 (32-bit, single precision) — training default historically
- FP16 (16-bit, half precision) — limited range
- BF16 (16-bit, wider range, less precision than FP16) — designed by Google for TPUs
- TF32 (19-bit, NVIDIA) — GPU-optimized
- INT8, INT4 — increasingly popular for inference

**What to quantize**: weights (most common, stable impact) or activations (less common, riskier).

**When to quantize**:
- **Post-training quantization (PTQ)**: most common, quantize after training. Supported by PyTorch, TensorFlow, HuggingFace
- **Quantization-aware training (QAT)**: simulate low-precision during training so model learns to perform well at low precision. Doesn't reduce training cost
- **Low-precision training**: train directly in reduced precision (e.g., INT8). Harder but reduces training cost

**Mixed precision**: keep sensitive operations (loss, certain weights) in higher precision, rest in lower. Automatic mixed precision (AMP) available in major frameworks.

**Caution**: load models in their intended format. Llama 2 (BF16) loaded in FP16 showed significantly degraded quality.
