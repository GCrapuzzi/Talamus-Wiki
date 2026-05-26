---
type: pattern
tags: [evaluation, ai-judge, llm-as-judge, production, bias]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#ai-as-a-judge
  - AI Space/normalized/pdf/ai-engineering.md#why-ai-as-a-judge
  - AI Space/normalized/pdf/ai-engineering.md#how-to-use-ai-as-a-judge
  - AI Space/normalized/pdf/ai-engineering.md#limitations-of-ai-as-a-judge
  - AI Space/normalized/pdf/ai-engineering.md#what-models-can-act-as-judges
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# AI as a Judge

Using an AI model to evaluate AI-generated outputs. Also called **LLM as a judge**. As of 2024, one of the most common evaluation methods in production (58% of evaluations on LangChain's platform).

**Why use it:**
- Fast, cheap relative to human evaluators, works without reference data
- Can evaluate on arbitrary criteria (correctness, toxicity, faithfulness, coherence, etc.)
- Can explain its reasoning—useful for auditing
- GPT-4's agreement with humans (85%) exceeded inter-human agreement (81%) on MT-Bench

**Three core usage patterns:**
1. **Pointwise scoring**: Score a response alone given the question
2. **Reference comparison**: Judge whether generated output matches a reference
3. **Pairwise comparison**: Pick the better of two responses (feeds into [[Comparative Evaluation]])

**Prompting an AI judge** requires: (1) task description, (2) detailed evaluation criteria, (3) scoring system. Classification scoring outperforms numerical; discrete (1–5) outperforms continuous. Include scored examples with justifications.

**An AI judge is a system** = model + prompt + sampling parameters. Changing any component changes the judge.

**Known biases:**
- **Self-bias**: Models favor their own outputs (GPT-4: +10% win rate; Claude-v1: +25%)
- **Position bias**: Favors first option in pairwise comparisons (opposite of human recency bias)
- **Verbosity bias**: Prefers longer responses even with factual errors over shorter correct ones

**Limitations:**
- **Inconsistency**: Same judge can produce different scores on repeated runs
- **Criteria ambiguity**: "Faithfulness" scores from MLflow, Ragas, and LlamaIndex are not comparable—different prompts, different scales
- **Judge drift**: Changing judge prompt/model over time breaks longitudinal comparisons
- **Cost/latency**: Multiple eval criteria multiply API calls; adds latency if used as production guardrail

**Rule**: Never trust an AI judge if you can't see the model and prompt used.

**Specialized judges** (smaller, task-specific) can outperform general-purpose judges:
- **Reward model**: Scores (prompt, response) pairs (e.g., Cappy, 360M params)
- **Reference-based judge**: Scores against reference (e.g., BLEURT, Prometheus)
- **Preference model**: Predicts which of two responses users prefer (e.g., PandaLM, JudgeLM)
