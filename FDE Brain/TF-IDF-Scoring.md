---
type: method
status: evergreen
aliases:
  - TF-IDF Scoring
  - Term Frequency - Inverse Document Frequency
tags:
  - ai-engineering
  - nlp
  - scoring
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/113-retrieval-algorithms.md
    locator: pages 281-290
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - The number of times a term appears in a document is called term frequency (TF).
      - A term’s importance is inversely proportional to the number of documents it appears in. This metric is called inverse document frequency (IDF).
      - "TF-IDF is an algorithm that combines these two metrics: term frequency (TF) and inverse document frequency (IDF)."
created: 2026-05-26T21:55:46.051111+00:00
updated: 2026-05-26T21:55:46.051111+00:00
ingestion_run: 8d527d59
---

# TF-IDF Scoring

## Summary

A statistical scoring algorithm that weights the importance of a term in a document based on how frequently it appears in that document (Term Frequency, TF) and how rare it is across the entire corpus (Inverse Document Frequency, IDF).

## Core Idea

TF-IDF addresses the limitation of simple keyword matching by penalizing common, uninformative terms (like 'for' or 'at') and boosting the score of rare, highly specific terms. The combined score measures a term's local importance relative to the corpus.

## Practical Use

Used as a foundational baseline for lexical retrieval systems (e.g., in Elasticsearch). The formula Score(D, Q) = ∑i=1 to q IDF(ti) × f(ti, D) is used to rank document relevance.

## Related

- [[BM25-Scoring|BM25 Scoring]]
- [[Term-based-Retrieval|Term-based Retrieval]]
