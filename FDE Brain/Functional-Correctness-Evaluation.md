---
type: concept
status: evergreen
aliases:
  - Functional Correctness Evaluation
  - Functional Correctness
  - Intended Functionality Check
tags:
  - ai-engineering
  - evaluation
  - testing
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/064-functional-correctness.md
    locator: pages 150-150
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Functional correctness evaluation means evaluating a system based on whether it performs the intended functionality.
      - Functional correctness is the ultimate metric for evaluating the performance of any application.
      - Code generation is an example of a task where functional correctness measurement can be automated.
      - Benchmarks for text-to-SQL... also rely on functional correctness.
created: 2026-05-26T21:55:45.685083+00:00
updated: 2026-05-26T21:55:45.685083+00:00
ingestion_run: 8d527d59
---

# Functional Correctness Evaluation

## Summary

Evaluating a system based on whether it performs its intended function, measuring if the application does what it is supposed to do, regardless of the underlying mechanism.

## Core Idea

Functional correctness is the ultimate metric for application performance because it directly measures utility. While difficult to measure generally, it is highly automatable for structured tasks like code generation or database querying.

## Practical Use

When deploying an LLM-powered application (e.g., a code generator or a text-to-SQL system), functional correctness must be verified by running the generated output against a comprehensive set of predefined test cases (unit tests) and comparing the actual output to the expected ground truth.

## Related

- Unit Testing
- Code Generation Benchmarks
- Test-Driven Development (TDD)
