---
type: method
status: evergreen
aliases:
  - Mixed-Method Dataset Curation Pipeline
  - Dataset Engineering Workflow
  - Multi-Source Data Assembly
tags:
  - data-engineering
  - dataset-curation
  - llm-engineering
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/144-data-acquisition-and-annotation.md
    locator: pages 401-403
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - A dataset can be developed from multiple data sources via multiple acquisition channels.
      - "For example, the process of creating an (instruction, response) dataset might look as follows: [list of steps 1-6]"
      - For example, there might be several steps in which you realize that many of the annotations aren’t helpful, so you have to update the annotation guidelines and reannotate your data.
created: 2026-05-26T21:55:46.349374+00:00
updated: 2026-05-26T21:55:46.349374+00:00
ingestion_run: 8d527d59
---

# Mixed-Method Dataset Curation Pipeline

## Summary

A multi-stage, iterative process for building a high-quality dataset by combining, filtering, synthesizing, and manually annotating data from multiple disparate sources.

## Core Idea

Rarely is a single dataset sufficient. High-quality datasets are assembled through a 'mix-and-match' approach, requiring rigorous cleaning and iterative refinement (e.g., updating annotation guidelines based on initial results).

## Practical Use

When building an (instruction, response) dataset: 1. Start by sourcing existing datasets. 2. Filter out low-quality examples (instructions or responses). 3. Manually write responses for critical, high-quality instructions. 4. Identify data gaps and use AI models to synthesize new instructions based on templates. 5. Manually review and annotate all synthetic data.

## Related

- [[Data-Acquisition-Strategy|Data Acquisition Strategy]]
- [[Data-Annotation-Guidelines|Data Annotation Guidelines]]
