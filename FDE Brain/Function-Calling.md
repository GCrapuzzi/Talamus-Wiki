---
type: operation
tags: [function-calling, tool-use, agents, api]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#planning
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Function Calling

The mechanism by which model providers enable tool use, turning models into agents.

### Workflow
1. **Declare tool inventory**: each tool defined by function name, parameters, documentation
2. **Specify tools per query**: API lets you control tool use:
   - `required` — must use at least one tool
   - `none` — no tools allowed
   - `auto` — model decides
3. **Model generates**: which tools to call and their parameter values
4. **Execute**: invoke the function with generated parameters
5. **Use output**: feed tool output back to generate final response

### Key considerations
- Some APIs guarantee valid function names but cannot guarantee correct parameter values
- Parameters are often extracted from previous tool outputs, so exact values can't be predicted in advance
- Models frequently guess ambiguous parameters — guesses can be wrong
- **Always inspect** parameter values the system uses for each function call

Both action sequences and parameters can be hallucinated. Better prompts, tool descriptions, simpler functions, stronger models, and finetuning all help.
