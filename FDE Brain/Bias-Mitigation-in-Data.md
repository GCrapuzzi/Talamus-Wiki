---
type: playbook
status: evergreen
aliases:
  - Bias Mitigation in Data
  - Fairness Through Data Augmentation
  - Counter-Stereotype Data Synthesis
tags:
  - ai-ethics
  - bias-mitigation
  - data-governance
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/147-traditional-data-synthesis-techniques.md
    locator: pages 407-409
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - If you’re concerned that there’s a gender bias in your data... you can replace typically gendered words with their opposites, such as “she” with “he”...
      - Snap (2022) has a great case study on how they augment their assets to create unrepresented corner cases and mitigate implicit biases in their data.
created: 2026-05-26T21:55:46.372606+00:00
updated: 2026-05-26T21:55:46.372606+00:00
ingestion_run: 8d527d59
---

# Bias Mitigation in Data

## Summary

Systematically augmenting training data to ensure representation across sensitive attributes (e.g., gender, race, body type) and counteract implicit biases present in the original dataset.

## Core Idea

Bias mitigation requires proactive data intervention. By generating synthetic examples that deliberately swap or balance typically associated attributes (e.g., swapping 'she' for 'he' when describing a professional role), the model learns to decouple the concept from the biased attribute.

## Practical Use

When developing HR or medical AI models, use augmentation to ensure that performance metrics are consistent regardless of the demographic group represented in the data, thereby improving fairness and ethical compliance.

## Related

- [[Data-Augmentation-Techniques|Data Augmentation Techniques]]
- Fairness Metrics
