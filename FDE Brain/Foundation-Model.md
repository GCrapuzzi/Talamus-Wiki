---
type: glossary
tags: [foundation-model, multimodal, model-as-a-service, definition]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#from-large-language-models-to-foundation-models
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Foundation Model

A large-scale model — language or multimodal — trained on broad data that can be adapted to many downstream tasks. The term signifies both the model's importance as a building block and its capacity to be built upon.

Key properties:

- **Multimodal**: extends beyond text to images, video, audio, 3D assets, protein structures. A multimodal model generates the next token conditioned on tokens from multiple modalities.
- **General-purpose**: capable of a wide range of tasks out of the box (translation, classification, coding, summarization), unlike prior task-specific models. Can be specialized via Prompt Engineering, [[Retrieval-Augmented Generation]], or Finetuning.
- **Model as a service**: training requires data, compute, and talent only a few orgs can afford. The resulting models are exposed via APIs, democratizing access.

Foundation models mark a structural break in AI research: previously siloed fields (NLP, computer vision, speech) converge into unified architectures. They also shift the workflow from task-specific model development to adapting general models — the core of [[AI Engineering]].

Embedding models like CLIP (non-generative) underpin generative multimodal models such as Flamingo, LLaVA, and Gemini.
