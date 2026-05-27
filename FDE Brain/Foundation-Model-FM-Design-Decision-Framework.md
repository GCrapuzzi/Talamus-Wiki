---
type: framework
status: evergreen
aliases:
  - Foundation Model (FM) Design Decision Framework
  - FM capability determinants
  - FM design axes
tags:
  - ai-engineering
  - llm-architecture
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/038-chapter-2.-understanding-foundation-models.md
    locator: pages 73-73
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - differences in foundation models can be traced back to decisions about training data, model architecture and size, and how they are post-trained to align with human preferences.
created: 2026-05-26T21:55:45.497573+00:00
updated: 2026-05-26T21:55:45.497573+00:00
ingestion_run: 8d527d59
---

# Foundation Model (FM) Design Decision Framework

## Summary

A framework identifying the three primary factors that determine an FM's capabilities and limitations: Training Data, Model Architecture/Size, and Post-training Alignment.

## Core Idea

An FM's performance is not monolithic; its behavior is a function of these three distinct, consequential design decisions. Understanding this framework allows engineers to predict limitations and select appropriate models.

## Practical Use

When evaluating a model for a specific task, use this framework to hypothesize potential failure points. For example, if the model fails on niche topics, the limitation might be in the 'Training Data Distribution.' If it is unsafe, the issue is likely 'Alignment.'

## Related

- [[Model-Training-Data-Distribution|Model Training Data Distribution]]
- [[Model-Alignment-Post-training|Model Alignment (Post-training)]]
