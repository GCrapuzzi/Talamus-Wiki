---
type: pattern
status: evergreen
aliases:
  - RAG with Tabular Data
  - Structured Data RAG
  - Text-to-SQL RAG
tags:
  - ai-engineering
  - rag
  - database
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/115-rag-beyond-texts.md
    locator: pages 297-298
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - The workflow for augmenting a context using tabular data is significantly different from the classic RAG workflow.
      - To run this workflow, your system must have the ability to generate and execute the SQL query:
      - "1. Text-to-SQL: based on the user query and the provided table schemas, determine what SQL query is needed."
created: 2026-05-26T21:55:46.077631+00:00
updated: 2026-05-26T21:55:46.077631+00:00
ingestion_run: 8d527d59
---

# RAG with Tabular Data

## Summary

A specialized workflow for answering questions based on structured data (tables) by translating natural language into executable SQL queries.

## Core Idea

Unlike standard RAG, which retrieves text chunks, this pattern requires the system to perform semantic parsing (NL to SQL), execute the resulting query against a database, and then use the structured result to generate the final answer.

## Practical Use

Answering quantitative questions that require aggregation or filtering across database records (e.g., 'How many units of X were sold in the last 7 days?').

## Related

- Text-to-SQL
- [[Semantic-Parsing|Semantic Parsing]]
