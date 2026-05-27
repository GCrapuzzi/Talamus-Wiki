---
type: pattern
status: evergreen
aliases:
  - Data Processing Workflow Optimization
  - Efficiency-First Data Cleaning
  - Computational Resource Allocation
tags:
  - workflow
  - optimization
  - data-engineering
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/151-inspect-data.md
    locator: pages 421-422
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - You can do these data processing steps in whichever order saves time and compute. For example, if it takes more time to clean each example than to deduplicate data, you might want to remove the duplicated examples first before cleaning them.
created: 2026-05-26T21:55:46.398154+00:00
updated: 2026-05-26T21:55:46.398154+00:00
ingestion_run: 8d527d59
---

# Data Processing Workflow Optimization

## Summary

A strategic approach to ordering data cleaning and processing steps to minimize computational time and resource usage.

## Core Idea

The order of operations matters. Prioritize the most computationally expensive or time-consuming steps (e.g., cleaning vs. deduplication) to run first, or conversely, run the fastest filtering steps first to reduce the dataset size before complex processing begins.

## Practical Use

If cleaning individual examples is slow, but deduplication is fast, run deduplication first to reduce the dataset size, then run the expensive cleaning process on the smaller subset. Always profile the cost of each step.

## Related

- Data Processing Pipeline Optimization
