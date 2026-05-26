---
type: method
tags: [evaluation, code-generation, benchmarks, pass-at-k]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#functional-correctness
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Functional Correctness Evaluation

Evaluate a system by whether it performs the intended functionality—the ultimate metric for any application.

Best suited for tasks with **automatically verifiable outcomes**:
- **Code generation**: Execute generated code against unit tests. Benchmarks: HumanEval, MBPP, Spider (text-to-SQL), BIRD-SQL.
- **Game bots**: Measure game score directly.
- **Optimization tasks**: Measure objective value (e.g., energy saved by a scheduling AI).

**pass@k metric**: Generate $k$ code samples per problem. A problem is solved if *any* sample passes all test cases. Final score = fraction of solved problems. By construction, pass@1 ≤ pass@3 ≤ pass@10.

**Limitation**: Many complex tasks lack easily measurable end-to-end objectives. AI may handle only a subtask, and evaluating a partial solution is often harder than evaluating the final outcome (chess analogy: evaluating a single move is harder than evaluating win/loss).
