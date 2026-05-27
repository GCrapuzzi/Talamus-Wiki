---
type: method
status: evergreen
aliases:
  - Automated Functional Testing (Code)
  - Unit Testing for LLMs
  - Execution Accuracy Check
tags:
  - ai-engineering
  - testing
  - deployment
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/064-functional-correctness.md
    locator: pages 150-150
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Code generation is an example of a task where functional correctness measurement can be automated.
      - The generated code can then be input into a Python interpreter to check whether the code is valid and if it is, whether it outputs the correct result of a given pair (num1, num2).
      - Code is typically validated with unit tests where code is executed in different scenarios to ensure that it generates the expected outputs.
created: 2026-05-26T21:55:45.687331+00:00
updated: 2026-05-26T21:55:45.687331+00:00
ingestion_run: 8d527d59
---

# Automated Functional Testing (Code)

## Summary

A structured method for verifying the output of code-generating LLMs by executing the generated code within a controlled interpreter environment and comparing the resulting output against known, expected test case outputs.

## Core Idea

This method transforms the abstract concept of 'correctness' into a concrete, executable process. It mimics standard software engineering practices (like unit testing) to provide quantifiable metrics for LLM performance.

## Practical Use

For any LLM task that produces executable code (Python, SQL, etc.), the engineering pipeline must include a step where the generated code is passed through a test harness (e.g., using Python's `exec()` or a dedicated SQL execution engine) and evaluated against a suite of input/output pairs. Benchmarks like HumanEval and Spider exemplify this.

## Related

- [[Functional-Correctness-Evaluation|Functional Correctness Evaluation]]
- Test Case Generation
- Interpreter Sandboxing
