---
type: pattern
status: evergreen
aliases:
  - Data Generation Pipeline
  - Synthetic Data Pipeline
  - Data Simulation Loop
tags:
  - ai-engineering
  - ml-ops
  - data-strategy
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/145-data-augmentation-and-synthesis.md
    locator: pages 404-404
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - If you’re lucky, your evaluation examples can be augmented or used as seed examples to synthesize new data.
created: 2026-05-26T21:55:46.358015+00:00
updated: 2026-05-26T21:55:46.358015+00:00
ingestion_run: 8d527d59
---

# Data Generation Pipeline

## Summary

A structured process for programmatically creating, validating, and integrating artificial data into the ML lifecycle, reducing reliance on manual data collection and annotation.

## Core Idea

By automating data creation, teams can overcome the 'data bottleneck'—the challenge of acquiring sufficient, diverse, and labeled real-world data—allowing for faster iteration and testing of complex models.

## Practical Use

Establish a feedback loop where evaluation data guidelines are used as seeds to synthesize new, challenging test cases, thereby improving both model performance and annotation guidelines simultaneously.

## Related

- [[Data-Augmentation|Data Augmentation]]
- [[Data-Synthesis|Data Synthesis]]
- Evaluation Data Curation
