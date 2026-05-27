---
type: concept
status: evergreen
aliases:
  - Data Annotation Guidelines
  - Annotation Schema
  - Labeling Protocol
tags:
  - data-quality
  - annotation
  - llm-engineering
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/144-data-acquisition-and-annotation.md
    locator: pages 401-403
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Annotation is challenging not just because of the annotation process but also due to the complexity of creating clear annotation guidelines.
      - For example, you need to explicitly state what a good response looks like, and what makes it good.
created: 2026-05-26T21:55:46.350990+00:00
updated: 2026-05-26T21:55:46.350990+00:00
ingestion_run: 8d527d59
---

# Data Annotation Guidelines

## Summary

A formal, detailed set of rules and criteria required for both manual and AI-powered annotation, defining what constitutes 'good' or 'correct' data points.

## Core Idea

Annotation is challenging because the guidelines must explicitly define subjective concepts (e.g., 'What is the difference between responses that deserve a score of 3 and 4?') to ensure consistency and reduce ambiguity across annotators.

## Practical Use

Before starting annotation, create a guideline document that addresses edge cases, defines scoring criteria, and provides clear examples of both acceptable and unacceptable data. This document must be updated iteratively as the project progresses.

## Related

- [[Data-Acquisition-Strategy|Data Acquisition Strategy]]
- Dataset Curation Pipeline
