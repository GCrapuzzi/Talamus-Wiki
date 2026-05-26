---
type: framework
tags: [evaluation, framework, ai-engineering]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#domain-specific-capability
  - AI Space/normalized/pdf/ai-engineering.md#generation-capability
  - AI Space/normalized/pdf/ai-engineering.md#instruction-following-capability
  - AI Space/normalized/pdf/ai-engineering.md#cost-and-latency
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# AI Evaluation Criteria Taxonomy

Four buckets of criteria for evaluating AI applications:

1. **Domain-specific capability** — can the model do the task at all? (coding, language understanding, legal knowledge). Constrained by architecture, size, and training data. Evaluated via domain-specific benchmarks, often using [[Multiple-Choice Question Evaluation|MCQs]] or functional correctness.
2. **Generation capability** — quality of open-ended outputs: fluency, coherence, [[Factual Consistency Verification|factual consistency]], safety. Legacy NLG metrics (fluency, coherence) matter less as models improve; hallucination and safety matter more.
3. **Instruction-following capability** — does the model follow format constraints, length limits, structured output requirements, content constraints, style rules? Evaluated via benchmarks like IFEval (25 auto-verifiable instruction types) and INFOBench (broader scope including content/style/linguistic constraints).
4. **Cost and latency** — time to first token, time per token, total query time, cost per token, TPM capacity.

Example: summarising a legal contract tests legal understanding (domain), summary coherence/faithfulness (generation), format compliance (instruction-following), and speed/price (cost/latency).
