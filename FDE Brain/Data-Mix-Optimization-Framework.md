---
type: framework
status: evergreen
aliases:
  - Data Mix Optimization Framework
  - Data Balancing
  - Dataset Composition Strategy
tags:
  - data-engineering
  - llm-training
  - experimental-design
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/142-data-coverage.md
    locator: pages 393-395
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - A simple approach is to choose a data mix that accurately reflects the real-world application usage.
      - For each candidate data mix, they trained several small models on a data mix and used that to predict the performance of a large model on that mix.
created: 2026-05-26T21:55:46.332304+00:00
updated: 2026-05-26T21:55:46.332304+00:00
ingestion_run: 8d527d59
---

# Data Mix Optimization Framework

## Summary

A systematic approach to determining the optimal ratio and mix of different data types (e.g., domain, topic, length, code, math) to maximize model performance while reflecting real-world usage.

## Core Idea

The performance of a large model is not solely determined by the total volume of data, but by the strategic balance and quality of its constituent parts. The mix must be empirically validated against the target application's usage profile.

## Practical Use

1. **Profile:** Analyze real-world usage to determine the ideal mix (e.g., 50% general knowledge, 20% coding, 30% math). 2. **Experiment:** Use scaling law experiments or train small proxy models on candidate mixes to predict the performance of the final large model. 3. **Iterate:** Adjust the mix based on empirical results and domain expertise.

## Related

- [[Data-Coverage-and-Diversity|Data Coverage and Diversity]]
