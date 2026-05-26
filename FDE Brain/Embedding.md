---
type: concept
tags: [embeddings, representation-learning, CLIP, multimodal, vector-search]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#introduction-to-embedding
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Embedding

A numerical vector representation that captures the meaning of input data. Computers process numbers, so any input (text, image, audio) must be converted to embeddings before model processing.

**Properties:**
- Typical dimensionality: 100–10,000 elements (lower-dimensional than raw data).
- Quality criterion: more-similar inputs should have closer embeddings (measured by cosine similarity).

**Common embedding models and sizes:**
| Model | Size |
|---|---|
| BERT base / large | 768 / 1024 |
| CLIP (image & text) | 512 |
| OpenAI text-embedding-3-small / large | 1536 / 3072 |
| Cohere Embed v3 | 1024 (full) / 384 (light) |

**Multimodal embeddings**: CLIP maps text and images into a joint space. ImageBind extends this to six modalities. A **multimodal embedding space** enables cross-modal operations like text-based image search.

**Applications**: [[Semantic Similarity]], classification, topic modeling, recommender systems, [[Retrieval-Augmented Generation]], vector search, data deduplication.

**Evaluation**: MTEB (Massive Text Embedding Benchmark) measures embedding quality across multiple tasks.

General-purpose LLMs (GPT, Llama) produce intermediate embeddings, but specialized embedding models typically produce higher-quality representations.
