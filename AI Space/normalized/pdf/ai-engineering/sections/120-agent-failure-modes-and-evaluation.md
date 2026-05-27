---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 120
section-title: Agent Failure Modes and Evaluation
source-location: pages 322-323
previous-section: AI Space/normalized/pdf/ai-engineering/sections/119-planning.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/121-memory.md
classification: reusable-knowledge-candidate
---
# Agent Failure Modes and Evaluation

Earlier in this section, we mentioned that the success of an agent in an environment
depends on its tool inventory and its planning capabilities. Failures in either aspect
can cause the agent to fail. The next section will discuss different failure modes of an
agent and how to evaluate them.
Agent Failure Modes and Evaluation
Evaluation is about detecting failures. The more complex a task an agent performs,
the more possible failure points there are. Other than the failure modes common to
all AI applications discussed in Chapters 3 and 4, agents also have unique failures
caused by planning, tool execution, and efficiency. Some of the failures are easier to
catch than others.
To evaluate an agent, identify its failure modes and measure how often each of these
failure modes happens.
I created a simple benchmark to illustrate these different failure modes that you can
see on the book’s  GitHub repository . There are also agent benchmarks and leader‐
boards such as the Berkeley Function Calling Leaderboard , the AgentOps evaluation
harness, and the TravelPlanner benchmark.
Planning failures
Planning is hard and can fail in many ways. The most common mode of planning
failure is tool use failure. The agent might generate a plan with one or more of these
errors:
Invalid tool
For example, it generates a plan that contains bing_search, but bing_search
isn’t in the agent’s tool inventory.
Valid tool, invalid parameters.
For example, it calls lbs_to_kg with two parameters. lbs_to_kg is in the tool
inventory but requires only one parameter, lbs.
Valid tool, incorrect parameter values
For example, it calls lbs_to_kg with one parameter, lbs, but uses the value 100
for lbs when it should be 120.
Another mode of planning failure is goal failure: the agent fails to achieve the goal.
This can be because the plan doesn’t solve a task, or it solves the task without follow‐
ing the constraints. To illustrate this, imagine you ask the model to plan a two-week
trip from San Francisco to Hanoi with a budget of $5,000. The agent might plan a trip
from San Francisco to Ho Chi Minh City, or plan a two-week trip from San Francisco
to Hanoi that will be way over the budget.
298 | Chapter 6: RAG and Agents

A common constraint that is often overlooked by agent evaluation is time. In many
cases, the time an agent takes matters less, because you can assign a task to an agent
and only need to check in when it’s done. However, in many cases, the agent becomes
less useful with time. For example, if you ask an agent to prepare a grant proposal
and the agent finishes it after the grant deadline, the agent isn’t very helpful.
An interesting mode of planning failure is caused by errors in reflection. The agent is
convinced that it’s accomplished a task when it hasn’t. For example, you ask the agent
to assign 50 people to 30 hotel rooms. The agent might assign only 40 people and
insist that the task has been accomplished.
To evaluate an agent for planning failures, one option is to create a planning dataset
where each example is a tuple (task, tool inventory). For each task, use the agent
to generate a K number of plans. Compute the following metrics:
1. Out of all generated plans, how many are valid?
2. For a given task, how many plans does the agent have to generate, on average, to
get a valid plan?
3. Out of all tool calls, how many are valid?
4. How often are invalid tools called?
5. How often are valid tools called with invalid parameters?
6. How often are valid tools called with incorrect parameter values?
Analyze the agent’s outputs for patterns. What types of tasks does the agent fail more
on? Do you have a hypothesis why? What tools does the model frequently make mis‐
takes with? Some tools might be harder for an agent to use. You can improve an
agent’s ability to use a challenging tool by better prompting, more examples, or fine‐
tuning. If all fail, you might consider swapping this tool for something easier to use.
Tool failures
Tool failures happen when the correct tool is used, but the tool output is wrong. One
failure mode is when a tool just gives the wrong outputs. For example, an image cap‐
tioner returns a wrong description, or an SQL query generator returns a wrong SQL
query.
If the agent generates only high-level plans and a translation module is involved in
translating from each planned action to executable commands, failures can happen
because of translation errors.
Agents | 299
