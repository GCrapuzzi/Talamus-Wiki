---
type: method
tags: [evaluation, embeddings, cosine-similarity, semantic-search]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#similarity-measurements-against-reference-data
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Semantic Similarity

Measures whether two texts have the same *meaning*, not just surface overlap. Also called **embedding similarity**.

**Process:**
1. Convert texts to numerical vectors ([[Embedding]]) using a model (BERT, Sentence Transformers, or proprietary APIs).
2. Compute **cosine similarity**: $\frac{A \cdot B}{\|A\| \|B\|}$. Score of 1 = identical, −1 = opposite.

**Metrics**: BERTScore (BERT embeddings), MoverScore (mixed algorithms).

**Advantages over [[Lexical Similarity]]:**
- Doesn't require as comprehensive a reference set—semantically equivalent paraphrases score high even if lexically different.
- "What's up?" and "How are you?" correctly score as similar.

**Drawbacks:**
- Quality depends entirely on the embedding model—bad embeddings yield misleading scores.
- Embedding computation adds non-trivial compute and latency.
- Technically subjective (different embedding algorithms → different scores), though score computation itself is exact.

Works across modalities (text, images, audio) when using multimodal embedding models.
