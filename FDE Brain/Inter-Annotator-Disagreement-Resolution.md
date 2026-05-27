---
type: operation
status: evergreen
aliases:
  - Inter-Annotator Disagreement Resolution
  - Annotation Conflict Resolution
  - Inter-Annotator Agreement (IAA)
tags:
  - annotation
  - data-quality
  - evaluation
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/151-inspect-data.md
    locator: pages 421-422
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - If each example has more than one annotation, compute the inter-annotator disagreement. Check the examples with conflicting annotations and resolve the conflicts.
created: 2026-05-26T21:55:46.401381+00:00
updated: 2026-05-26T21:55:46.401381+00:00
ingestion_run: 8d527d59
---

# Inter-Annotator Disagreement Resolution

## Summary

A mandatory step in dataset engineering when multiple annotators provide labels or scores for the same example. It involves quantifying disagreement and resolving conflicts.

## Core Idea

Disagreement indicates potential ambiguity in the task definition, the data itself, or the annotators' understanding. Identifying and resolving these conflicts is crucial for creating a high-quality, consensus-driven training dataset.

## Practical Use

1. Calculate the disagreement metric (e.g., Cohen's Kappa, simple conflict count). 2. Isolate all examples with conflicting annotations. 3. Review these examples manually (or via consensus guidelines) to determine the correct label or score, and update the dataset accordingly.

## Related

- [[Data-Inspection-Protocol|Data Inspection Protocol]]
