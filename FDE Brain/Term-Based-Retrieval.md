---
type: method
tags: [retrieval, tf-idf, bm25, elasticsearch, information-retrieval]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#retrieval-algorithms
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Term-Based Retrieval

Retrieval based on lexical matching — ranking documents by keyword relevance scores.

### TF-IDF
- **Term Frequency (TF)**: number of times a term appears in a document. More occurrences → higher relevance.
- **Inverse Document Frequency (IDF)**: `log(N / C(t))` where N = total documents, C(t) = documents containing term t. Rarer terms → more informative.
- **Score**: `∑ IDF(tᵢ) × f(tᵢ, D)` for all query terms.

### Key Solutions
- **Elasticsearch** (built on Lucene): uses an **inverted index** — dictionary mapping terms → documents containing them, with term frequency and document counts.
- **BM25** (Okapi Best Matching 25): TF-IDF variant that normalizes term frequency by document length. Still a formidable baseline against modern retrieval algorithms.

### Tokenization considerations
- Simple word splitting can break multi-word terms ("hot dog" → "hot" + "dog")
- Mitigate with common n-gram detection
- Lowercase conversion, punctuation removal, stop word elimination
- Tools: NLTK, spaCy, Stanford CoreNLP

Pros: fast, cheap, strong out-of-box performance. Cons: lexical-only (no semantic understanding), limited tuning levers.
