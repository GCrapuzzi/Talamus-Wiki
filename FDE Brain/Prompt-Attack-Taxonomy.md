---
type: framework
tags: [security, prompt-injection, jailbreaking, adversarial-attacks, AI-safety]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#defensive-prompt-engineering
  - AI Space/normalized/pdf/ai-engineering.md#proprietary-prompts-and-reverse-prompt-engineering
  - AI Space/normalized/pdf/ai-engineering.md#jailbreaking-and-prompt-injection
  - AI Space/normalized/pdf/ai-engineering.md#information-extraction
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Prompt Attack Taxonomy

Three categories of prompt attacks against AI applications:

### 1. Prompt extraction
Reverse-engineering the system prompt to replicate or exploit the application. Techniques: asking the model to repeat its instructions, analyzing output patterns. Leaked prompts are often hallucinated — verification is difficult.

### 2. Jailbreaking and prompt injection
Subverting safety features to produce disallowed outputs.

**Direct attacks (increasing sophistication):**
- **Obfuscation** — misspellings ("vacine"), mixed languages, Unicode, special character insertion
- **Output format manipulation** — "write a poem about hotwiring a car" instead of asking directly
- **Roleplaying** — DAN ("Do Anything Now"), grandma exploit, fictional simulation modes
- **Automated attacks** — algorithmic prompt mutation (Zou et al., 2023); PAIR (Chao et al., 2023) uses an attacker AI that iteratively refines prompts, often succeeding in <20 queries

**Indirect prompt injection:**
- **Passive phishing** — malicious payloads in public repos, web pages, comments; model discovers them via tools
- **Active injection** — malicious instructions embedded in emails, documents, or database entries that the model reads via RAG or tool use

### 3. Information extraction
- **Training data extraction** — triggering memorized data via fill-in-the-blank or divergence attacks (repeat-word prompts). Larger models memorize more (~1% rate per Nasr et al., 2023).
- **Copyright regurgitation** — model reproduces copyrighted content verbatim or near-verbatim.
- **Context data leakage** — private information in RAG context revealed to users.

### Risks
Remote code execution, data leaks, social harms, misinformation, service subversion, brand damage.
