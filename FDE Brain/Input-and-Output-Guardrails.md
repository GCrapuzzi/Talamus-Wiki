---
type: pattern
tags: [guardrails, safety, pii, production-systems]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#step-2-put-in-guardrails
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Input and Output Guardrails

Guardrails placed at system boundaries to mitigate risk. Two categories:

### Input guardrails
- **PII / sensitive data detection** — personal info, faces, IP keywords. If detected: block the query or mask with placeholders (e.g., `[PHONE NUMBER]`) and unmask via a PII reverse dictionary on output.
- **Prompt-attack defense** — catch injection, jailbreaks before they reach the model.

### Output guardrails
- **Failure detection** — empty responses, malformatted JSON, hallucinations, toxic content, brand-risk statements, unauthorized tool invocations.
- **Policy specification** — retry logic (probabilistic re-generation), parallel redundant calls (latency-safe retries), human escalation (sentiment-triggered or turn-count-triggered transfer).

### Trade-offs
- **Reliability vs latency** — guardrails add latency; some teams skip them for speed.
- **Streaming complication** — output guardrails are hard to apply to partial streamed tokens; unsafe content may reach users before evaluation completes.
- **Self-hosted vs third-party** — third-party APIs bundle guardrails but require sending data externally; self-hosting eliminates external-leak risk but needs custom guardrails.
- **False refusal rate** — overly strict guardrails block legitimate requests, degrading UX.
