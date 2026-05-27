---
type: method
status: evergreen
aliases:
  - Data Integrity Best Practices
  - Non-destructive Data Handling
  - Reproducible Data Pipelines
tags:
  - data-governance
  - reproducibility
  - data-safety
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/151-inspect-data.md
    locator: pages 421-422
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - "Avoid changing data in place. Consider keeping a copy of the original data for two reasons: [...] Bugs in your scripts can potentially corrupt your data."
created: 2026-05-26T21:55:46.399739+00:00
updated: 2026-05-26T21:55:46.399739+00:00
ingestion_run: 8d527d59
---

# Data Integrity Best Practices

## Summary

Operational guidelines for handling data transformations to ensure reproducibility, safety, and flexibility for future use.

## Core Idea

Never modify data in place. Always maintain a copy of the original raw data. This protects against script bugs corrupting the source and allows different teams or future iterations to process the data using varied methods.

## Practical Use

Before running any major data transformation script, commit the original raw dataset to version control and ensure the script operates on a dedicated copy. This guarantees that the original source data remains untouched.

## Related

- Data Version Control (DVC)
