---
type: pattern
status: evergreen
aliases:
  - Defining Evaluation Criteria
  - Defining 'Good' Responses
  - Scope Boundary Definition
tags:
  - ai-engineering
  - prompt-engineering
  - safety
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/088-step-2.-create-an-evaluation-guideline.md
    locator: pages 226-227
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - If you don’t know what bad responses look like, you won’t be able to catch them.
      - A correct response is not always a good response.
      - "For example, for a customer support application, a good response might be defined using three criteria: Relevance: the response is relevant to the user’s query. Factual consistency: the response is factually consistent with the context. Safety: the response isn’t toxic."
created: 2026-05-26T21:55:45.865614+00:00
updated: 2026-05-26T21:55:45.865614+00:00
ingestion_run: 8d527d59
---

# Defining Evaluation Criteria

## Summary

The process of moving beyond simple correctness to defining qualitative standards for 'goodness' and establishing clear boundaries for out-of-scope inputs and responses.

## Core Idea

A 'correct' response is not always a 'good' response. Evaluation criteria must be multi-faceted, covering functional quality (e.g., Relevance, Factual Consistency) and safety/guardrails (e.g., Toxicity, Scope Adherence).

## Practical Use

For a customer support chatbot, define criteria like 'Relevance' (is it on topic?), 'Factual Consistency' (does it match the provided context?), and 'Safety' (is it toxic?). Crucially, define the scope: if the chatbot should not answer about elections, define the input pattern, detection method, and required response for out-of-scope queries.

## Related

- [[AI-Evaluation-Guideline-Playbook|AI Evaluation Guideline Playbook]]
- [[Scoring-Rubric-Design|Scoring Rubric Design]]
