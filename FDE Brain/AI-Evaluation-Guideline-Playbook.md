---
type: operation
status: evergreen
aliases:
  - AI Evaluation Guideline Playbook
  - LLM Evaluation Pipeline Setup
  - Generative AI System Evaluation Framework
tags:
  - ai-engineering
  - evaluation
  - llm-ops
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/088-step-2.-create-an-evaluation-guideline.md
    locator: pages 226-227
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Creating a clear evaluation guideline is the most important step of the evaluation pipeline.
      - When creating the evaluation guideline, it’s important to define not only what the application should do, but also what it shouldn’t do.
created: 2026-05-26T21:55:45.863454+00:00
updated: 2026-05-26T21:55:45.863454+00:00
ingestion_run: 8d527d59
---

# AI Evaluation Guideline Playbook

## Summary

A structured, multi-step process for defining comprehensive, unambiguous criteria to evaluate the performance and safety of generative AI applications.

## Core Idea

Evaluation must define not only what constitutes a 'correct' output but also what constitutes a 'good' output, what inputs are out of scope, and how to score deviations. Ambiguity in the guideline leads to unreliable and misleading scores.

## Practical Use

Before building an AI application, use this playbook to define criteria (e.g., Relevance, Factual Consistency, Safety). Develop detailed scoring rubrics with examples, validate them with human subject matter experts, and map the resulting technical metrics (e.g., 80% consistency) to measurable business outcomes (e.g., automating 30% of requests).

## Related

- [[Defining-Evaluation-Criteria|Defining Evaluation Criteria]]
- [[Metric-to-Business-Mapping|Metric-to-Business Mapping]]
- [[Scoring-Rubric-Design|Scoring Rubric Design]]
