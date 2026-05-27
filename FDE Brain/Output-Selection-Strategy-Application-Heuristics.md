---
type: method
status: evergreen
aliases:
  - "Output Selection Strategy: Application Heuristics"
  - Domain-specific filtering
  - Constraint-based selection
tags:
  - ai-engineering
  - prompt-engineering
  - data-validation
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/051-test-time-compute.md
    locator: pages 120-122
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - You can also use application-specific heuristics to select the best response. For example, if your application benefits from shorter responses, you can pick the shortest candidate.
      - If your application converts natural language to SQL queries, you can get the model to keep on generating outputs until it generates a valid SQL query.
created: 2026-05-26T21:55:45.594443+00:00
updated: 2026-05-26T21:55:45.594443+00:00
ingestion_run: 8d527d59
---

# Output Selection Strategy: Application Heuristics

## Summary

Implementing simple, application-specific rules or constraints to filter or select the best output candidate, based on known requirements of the downstream task.

## Core Idea

When the application has predictable output characteristics (e.g., length, format, syntax), these constraints can be used as a selection mechanism that is more efficient than complex scoring models.

## Practical Use

If the application requires a short summary, select the shortest candidate. If the task is Natural Language to SQL, configure the generation loop to continue until a syntactically valid SQL query is produced, effectively using the syntax as the selection heuristic.

## Related

- [[Structured-Outputs|Structured Outputs]]
