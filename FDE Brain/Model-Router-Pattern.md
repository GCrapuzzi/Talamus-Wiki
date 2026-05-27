---
type: pattern
status: evergreen
aliases:
  - Model Router Pattern
  - Query Router
  - Intent-based Routing
tags:
  - ai-engineering
  - architecture
  - llm-deployment
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/169-step-3.-add-model-router-and-gateway.md
    locator: pages 480-483
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Instead of using one model for all queries, you can have different solutions for different types of queries.
      - A router typically consists of an intent classifier that predicts what the user is trying to do.
      - This can help you save costs. Instead of using one expensive model for all queries, you can route simpler queries to cheaper models.
created: 2026-05-26T21:55:46.528097+00:00
updated: 2026-05-26T21:55:46.528097+00:00
ingestion_run: 8d527d59
---

# Model Router Pattern

## Summary

An architectural pattern that directs incoming user queries to the most appropriate specialized model or solution based on predicted user intent, optimizing performance and cost.

## Core Idea

Instead of using a single general-purpose model for all queries, a router uses an intent classifier to determine the user's goal (e.g., billing vs. troubleshooting). This allows for specialized, higher-performing models for specific tasks and enables routing simple queries to cheaper models, thereby managing complexity and cost.

## Practical Use

Implement an intent classifier (e.g., using BERT or a smaller LLM) at the entry point of a customer support chatbot. If the intent is 'password reset,' route the query to an FAQ retrieval system; if the intent is 'billing error,' route it to a human operator queue; otherwise, route it to the general troubleshooting chatbot.

## Related

- [[Intent-Classifier|Intent Classifier]]
- [[Model-Gateway|Model Gateway]]
- AI Application Architecture
