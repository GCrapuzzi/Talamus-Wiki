---
type: pattern
status: evergreen
aliases:
  - Pass@k Metric
  - Pass at k
  - Code sample success rate
tags:
  - ai-engineering
  - evaluation
  - code-generation
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/065-similarity-measurements-against-reference-data.md
    locator: pages 151-157
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - When evaluating a model, for each problem a number of code samples, denoted as k, are generated. A model solves a problem if any of the k code samples it generated pass all of that problem’s test cases. The final score, called pass@k, is the fraction of the solved problems out of all problems.
created: 2026-05-26T21:55:45.691485+00:00
updated: 2026-05-26T21:55:45.691485+00:00
ingestion_run: 8d527d59
---

# Pass@k Metric

## Summary

A metric used to evaluate code generation models. It calculates the fraction of problems solved out of all problems, where a problem is considered solved if at least one of the k generated code samples passes all associated test cases.

## Core Idea

It accounts for the probabilistic nature of model output by testing multiple samples (k). The score increases as k increases, reflecting the higher chance of success with more attempts.

## Practical Use

When benchmarking code generation models, use Pass@k to provide a robust measure of reliability. Understanding that Pass@k is monotonically increasing with k helps set realistic performance expectations.

## Related

- Functional Correctness
