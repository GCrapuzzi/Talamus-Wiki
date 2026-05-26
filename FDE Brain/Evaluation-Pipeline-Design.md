---
type: framework
tags: [evaluation, pipeline, methodology, ai-engineering]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#design-your-evaluation-pipeline
  - AI Space/normalized/pdf/ai-engineering.md#step-1-evaluate-all-components-in-a-system
  - AI Space/normalized/pdf/ai-engineering.md#step-2-create-an-evaluation-guideline
  - AI Space/normalized/pdf/ai-engineering.md#step-3-define-evaluation-methods-and-data
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Evaluation Pipeline Design

End-to-end process for building a reliable evaluation pipeline for AI applications:

**Step 1: Evaluate all components independently**
- Evaluate intermediate outputs per component, not just end-to-end results
- Distinguish **turn-based** evaluation (quality of each output) from **task-based** evaluation (did the system complete the task? in how many turns?)
- Task-based is more important but harder — task boundaries are ambiguous in conversational settings

**Step 2: Create evaluation guidelines**
- Define what good *and* bad look like (a correct response isn't always a good response)
- Create scoring rubrics with examples for each criterion (binary, 1–5, continuous)
- Validate rubrics with humans — if humans can't follow the rubric, refine it
- Tie evaluation metrics to business metrics (e.g., 80% factual consistency → automate 30% of support requests; 98% → automate 90%)
- Determine the **usefulness threshold** — minimum score for the application to be worth deploying

**Step 3: Define methods and data**
- Mix methods per criterion (cheap classifier on 100% of data + expensive AI judge on 1%)
- Use logprobs when available for confidence estimation
- Maintain human evaluation as North Star (LinkedIn: up to 500 daily conversations manually reviewed)
- **Slice evaluation data** by user segments, traffic sources, error-prone categories, and out-of-scope inputs to avoid [[Simpson's Paradox]] and find improvement areas
- Bootstrap evaluation sets to test reliability; use statistical significance for comparisons
- Rule of thumb: 3× decrease in score difference to detect → 10× more samples needed (10 samples for 30% diff, 10K for 1% diff)

**Step 4: Evaluate the evaluation pipeline itself**
- Do better responses get higher scores? Do better metrics lead to better business outcomes?
- Run pipeline twice — are results reproducible? Set AI judge temperature to 0.
- Check metric correlations — perfectly correlated metrics are redundant
- Monitor cost/latency overhead of evaluation itself
