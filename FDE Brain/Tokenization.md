---
type: method
status: evergreen
aliases:
  - Tokenization
  - Text Preprocessing
  - N-gram Generation
tags:
  - ai-engineering
  - nlp
  - preprocessing
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/113-retrieval-algorithms.md
    locator: pages 281-290
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - One process I glossed over is tokenization, the process of breaking a query into individual terms.
      - One way to mitigate this issue is to treat the most common n-grams as terms.
created: 2026-05-26T21:55:46.057461+00:00
updated: 2026-05-26T21:55:46.057461+00:00
ingestion_run: 8d527d59
---

# Tokenization

## Summary

The process of breaking down raw text (queries or documents) into smaller, manageable units called tokens (words, subwords, or character sequences) for processing by NLP models.

## Core Idea

Proper tokenization is crucial for maintaining meaning. Simple word splitting can lose context (e.g., splitting 'hot dog' into 'hot' and 'dog'). Advanced methods, like treating common n-grams, mitigate this loss.

## Practical Use

Must be applied to both the query and the document chunks before indexing or scoring. Common steps include converting to lowercase, removing punctuation, and eliminating stop words.

## Related

- [[Term-based-Retrieval|Term-based Retrieval]]
- Chunking Strategies
