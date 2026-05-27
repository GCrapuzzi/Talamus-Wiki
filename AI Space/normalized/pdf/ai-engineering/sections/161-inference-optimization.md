---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 161
section-title: "Inference Optimization "
source-location: pages 450-450
previous-section: AI Space/normalized/pdf/ai-engineering/sections/160-ai-accelerators.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/162-model-optimization.md
classification: reusable-knowledge-candidate
---
# Inference Optimization 

Inference Optimization
Inference optimization can be done at the model, hardware, or service level. To illus‐
trate their differences, consider archery. Model-level optimization is like crafting bet‐
ter arrows. Hardware-level optimization is like training a stronger and better archer.
Service-level optimization is like refining the entire shooting process, including the
bow and aiming conditions.
Ideally, optimizing a model for speed and cost shouldn’t change the model’s quality.
However, many techniques might cause model degradation. Figure 9-8  shows the
same Llama models’ performance on different benchmarks, served by different infer‐
ence service providers.
Figure 9-8. An inference service provider might use optimization techniques that can
alter a model’s behavior, causing different providers to have slight model quality varia‐
tions. The experiment was conducted by Cerebras (2024).
Since hardware design is outside the scope of this book, I’ll discuss techniques at the
model and service levels. While the techniques are discussed separately, keep in mind
that, in production, optimization typically involves techniques at more than one
level.
Model Optimization
Model-level optimization aims to make the model more efficient, often by modifying
the model itself, which can alter its behavior. As of this writing, many foundation
models follow the transformer architecture and include an autoregressive language
model component. These models have three characteristics that make inference
resource-intensive: model size, autoregressive decoding, and the attention mecha‐
nism. Let’s discuss approaches to address these challenges.
426 | Chapter 9: Inference Optimization

[Visual content extracted via GLM-OCR]

Inference Optimization

Inference optimization can be done at the model, hardware, or service level. To illustrate their differences, consider archery. Model-level optimization is like crafting better arrows. Hardware-level optimization is like training a stronger and better archer. Service-level optimization is like refining the entire shooting process, including the bow and aiming conditions.

Ideally, optimizing a model for speed and cost shouldn’t change the model’s quality. However, many techniques might cause model degradation. Figure 9-8 shows the same Llama models’ performance on different benchmarks, served by different inference service providers.

Figure 9-8. An inference service provider might use optimization techniques that can alter a model’s behavior, causing different providers to have slight model quality variations. The experiment was conducted by Cerebras (2024).

Since hardware design is outside the scope of this book, I’ll discuss techniques at the model and service levels. While the techniques are discussed separately, keep in mind that, in production, optimization typically involves techniques at more than one level.

Model Optimization

Model-level optimization aims to make the model more efficient, often by modifying the model itself, which can alter its behavior. As of this writing, many foundation models follow the transformer architecture and include an autoregressive language model component. These models have three characteristics that make inference resource-intensive: model size, autoregressive decoding, and the attention mechanism. Let’s discuss approaches to address these challenges.
