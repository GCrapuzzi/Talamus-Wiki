---
type: operation
status: evergreen
aliases:
  - Comparative Feedback Collection Playbook
  - User Preference Collection
  - Subjective Evaluation Workflow
tags:
  - operational-playbook
  - ai-engineering
  - data-collection
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/072-ranking-models-with-comparative-evaluation.md
    locator: pages 172-175
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - A very important thing to keep in mind is that not all questions should be answered by preference. Many questions should be answered by correctness instead.
      - Preference-based voting only works if the voters are knowledgeable in the subject.
      - This approach generally works in applications where AI serves as an intern or assistant, helping users speed up tasks they know how to do...
created: 2026-05-26T21:55:45.761729+00:00
updated: 2026-05-26T21:55:45.761729+00:00
ingestion_run: 8d527d59
---

# Comparative Feedback Collection Playbook

## Summary

A set of operational guidelines for designing user-facing evaluation tasks to maximize the quality and reliability of comparative feedback.

## Core Idea

Comparative feedback is most reliable when the user is knowledgeable in the subject matter and when the task is inherently subjective (preference-based). It is unsuitable for questions requiring factual correctness, as preference voting can lead to misaligned training signals.

## Practical Use

Before launching a feedback loop, classify the task: If the answer is factual ('Is X linked to Y?'), use a correctness check. If the answer is subjective ('Which style is better?'), use comparative voting. Always ensure the user is an expert or semi-expert in the domain.

## Related

- [[Pointwise-vs.-Comparative-Evaluation|Pointwise vs. Comparative Evaluation]]
