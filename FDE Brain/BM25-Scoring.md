---
type: method
status: evergreen
aliases:
  - BM25 Scoring
  - Best Matching Algorithm
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
      - Compared to naive TF-IDF, BM25 normalizes term frequency scores by document length.
created: 2026-05-26T21:55:46.052916+00:00
updated: 2026-05-26T21:55:46.052916+00:00
ingestion_run: 8d527d59
---

# BM25 Scoring

## Summary

An advanced scoring algorithm, an evolution of TF-IDF, that normalizes term frequency scores by document length to provide a more accurate measure of relevance.

## Core Idea

BM25 improves upon naive TF-IDF by accounting for document length, ensuring that longer documents do not artificially inflate the relevance score of a term simply because they have more words.

## Practical Use

BM25 and its variants (BM25+, BM25F) are standard, high-performing baselines for lexical retrieval systems and are often used to benchmark modern embedding-based models.

## Related

- [[TF-IDF-Scoring|TF-IDF Scoring]]
- [[Term-based-Retrieval|Term-based Retrieval]]
