---
type: pattern
tags: [structured-outputs, JSON-mode, constrained-sampling, semantic-parsing, agentic]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#structured-outputs
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Structured Outputs

Techniques to get models to generate outputs in specific formats (JSON, SQL, YAML, regex, etc.). Critical for semantic parsing tasks and agentic workflows where outputs feed into downstream tools.

**Five approaches, from lightweight to heavyweight:**

1. **Prompting**: instruct the model to use a format. No guarantee of compliance. Can add a validation LLM call (AI-as-judge) but doubles cost/latency.

2. **Post-processing**: script common model mistakes (e.g., missing closing bracket). LinkedIn's defensive YAML parser: 90% → 99.99% validity. Works only when errors are predictable and minor. Tip: YAML is less verbose than JSON → fewer output tokens.

3. **Test time compute**: regenerate until output matches expected format.

4. **Constrained sampling**: filter the logit vector at each decoding step to allow only tokens valid under a grammar. Requires per-format grammar definitions. Can increase latency. Tools: guidance, outlines, instructor, llama.cpp.

5. **Finetuning**: most effective and general. Train on examples in desired format. Can add a classifier head for classification tasks (feature-based transfer) to guarantee output format.

OpenAI's JSON mode guarantees valid JSON syntax but not schema compliance or completeness (truncation risk).

As models improve at instruction-following, lightweight approaches become more reliable.
