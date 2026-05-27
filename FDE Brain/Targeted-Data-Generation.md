---
type: pattern
status: evergreen
aliases:
  - Targeted Data Generation
  - Data Coverage Improvement
  - Adversarial Data Synthesis
tags:
  - ai-engineering
  - data-engineering
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/146-why-data-synthesis.md
    locator: pages 405-406
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - You can generate data with targeted characteristics to improve model performance...
      - It’s especially common to use AI to synthesize adversarial examples.
      - It’s also possible to generate data for the rare class to address the challenges of class imbalance.
created: 2026-05-26T21:55:46.361409+00:00
updated: 2026-05-26T21:55:46.361409+00:00
ingestion_run: 8d527d59
---

# Targeted Data Generation

## Summary

The practice of generating synthetic data with specific, controlled characteristics to ensure model robustness and performance in niche or challenging scenarios.

## Core Idea

It allows engineers to explicitly cover data gaps (e.g., very short texts, very long texts, toxic phrases, rare classes) that are underrepresented or missing in real-world datasets, thereby improving model generalization.

## Practical Use

Generating adversarial examples to test model vulnerabilities, creating synthetic data for rare classes to address class imbalance, or generating specific behavioral datasets (e.g., toxic vs. safe conversations).

## Related

- Adversarial Examples
- Class Imbalance Handling
- [[Data-Augmentation|Data Augmentation]]
