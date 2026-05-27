---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 119
section-title: Planning
source-location: pages 305-321
previous-section: AI Space/normalized/pdf/ai-engineering/sections/118-tools.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/120-agent-failure-modes-and-evaluation.md
classification: reusable-knowledge-candidate
---
# Planning

(write). An email API can read an email but can also respond to it. A banking API
can retrieve your current balance but can also initiate a bank transfer.
Write actions enable a system to do more. They can enable you to automate the
whole customer outreach workflow: researching potential customers, finding their
contacts, drafting emails, sending first emails, reading responses, following up,
extracting orders, updating your databases with new orders, etc.
However, the prospect of giving AI the ability to automatically alter our lives is
frightening. Just as you shouldn’t give an intern the authority to delete your produc‐
tion database, you shouldn’t allow an unreliable AI to initiate bank transfers. Trust in
the system’s capabilities and its security measures is crucial. You need to ensure that
the system is protected from bad actors who might try to manipulate it into perform‐
ing harmful actions.
When I talk about autonomous AI agents to a group of people, there is often some‐
one who brings up self-driving cars. “What if someone hacks into the car to kidnap
you?” While the self-driving car example seems visceral because of its physicality,
an AI system can cause harm without a presence in the physical world. It can manip‐
ulate the stock market, steal copyrights, violate privacy, reinforce biases, spread mis‐
information and propaganda, and more, as discussed in “Defensive Prompt
Engineering” on page 235 .
These are all valid concerns, and any organization that wants to leverage AI needs to
take safety and security seriously. However, this doesn’t mean that AI systems should
never be given the ability to act in the real world. If we can get people to trust a
machine to take us into space, I hope that one day, security measures will be suffi‐
cient for us to trust autonomous AI systems. Besides, humans can fail, too. Person‐
ally, I would trust a self-driving car more than the average stranger to drive me
around.
Just as the right tools can help humans be vastly more productive—can you imagine
doing business without Excel or building a skyscraper without cranes?—tools enable
models to accomplish many more tasks. Many model providers already support tool
use with their models, a feature often called function calling. Going forward, I would
expect function calling with a wide set of tools to be common with most models.
Planning
At the heart of a foundation model agent is the model responsible for solving a task.
A task is defined by its goal and constraints. For example, one task is to schedule a
two-week trip from San Francisco to India with a budget of $5,000. The goal is the
two-week trip. The constraint is the budget.
Agents | 281

Complex tasks require planning. The output of the planning process is a plan, which
is a roadmap outlining the steps needed to accomplish a task. Effective planning typi‐
cally requires the model to understand the task, consider different options to achieve
this task, and choose the most promising one.
If you’ve ever been in any planning meeting, you know that planning is hard. As an
important computational problem, planning is well studied and would require sev‐
eral volumes to cover. I’ll only be able to cover the surface here.
Planning overview
Given a task, there are many possible ways to decompose it, but not all of them will
lead to a successful outcome. Among the correct solutions, some are more efficient
than others. Consider the query, “How many companies without revenue have raised
at least $1 billion?” There are many possible ways to solve this, but as an illustration,
consider the two options:
1. Find all companies without revenue, then filter them by the amount raised.
2. Find all companies that have raised at least $1 billion, then filter them by
revenue.
The second option is more efficient. There are vastly more companies without reve‐
nue than companies that have raised $1 billion. Given only these two options, an
intelligent agent should choose option 2.
You can couple planning with execution in the same prompt. For example, you give
the model a prompt, ask it to think step by step (such as with a chain-of-thought
prompt), and then execute those steps all in one prompt. But what if the model
comes up with a 1,000-step plan that doesn’t even accomplish the goal? Without
oversight, an agent can run those steps for hours, wasting time and money on API
calls, before you realize that it’s not going anywhere.
To avoid fruitless execution, planning should be decoupled from execution. You ask
the agent to first generate a plan, and only after this plan is validated is it executed.
The plan can be validated using heuristics. For example, one simple heuristic is to
eliminate plans with invalid actions. If the generated plan requires a Google search
and the agent doesn’t have access to Google Search, this plan is invalid. Another sim‐
ple heuristic might be eliminating all plans with more than X steps. A plan can also
be validated using AI judges. You can ask a model to evaluate whether the plan seems
reasonable or how to improve it.
If the generated plan is evaluated to be bad, you can ask the planner to generate
another plan. If the generated plan is good, execute it. If the plan consists of external
tools, function calling will be invoked. Outputs from executing this plan will then
again need to be evaluated. Note that the generated plan doesn’t have to be an
282 | Chapter 6: RAG and Agents

12 Because most agentic workflows are sufficiently complex to involve multiple components, most agents are
multi-agent.
end-to-end plan for the whole task. It can be a small plan for a subtask. The whole
process looks like Figure 6-9.
Figure 6-9. Decoupling planning and execution so that only validated plans are
executed.
Your system now has three components: one to generate plans, one to validate plans,
and another to execute plans. If you consider each component an agent, this is a
multi-agent system.12
To speed up the process, instead of generating plans sequentially, you can generate
several plans in parallel and ask the evaluator to pick the most promising one. This is
another latency/cost trade-off, as generating multiple plans simultaneously will incur
extra costs.
Planning requires understanding the intention behind a task: what’s the user trying
to do with this query? An intent classifier is often used to help agents plan. As shown
in “Break Complex Tasks into Simpler Subtasks” on page 224, intent classification
can be done using another prompt or a classification model trained for this task. The
intent classification mechanism can be considered another agent in your multi-agent
system.
Knowing the intent can help the agent pick the right tools. For example, for customer
support, if the query is about billing, the agent might need access to a tool to retrieve
a user’s recent payments. But if the query is about how to reset a password, the agent
might need to access documentation retrieval.
Agents | 283

[Visual content extracted via GLM-OCR]

end-to-end plan for the whole task. It can be a small plan for a subtask. The whole process looks like Figure 6-9.

Figure 6-9. Decoupling planning and execution so that only validated plans are executed.

Your system now has three components: one to generate plans, one to validate plans, and another to execute plans. If you consider each component an agent, this is a multi-agent system.12

To speed up the process, instead of generating plans sequentially, you can generate several plans in parallel and ask the evaluator to pick the most promising one. This is another latency/cost trade-off, as generating multiple plans simultaneously will incur extra costs.

Planning requires understanding the intention behind a task: what’s the user trying to do with this query? An intent classifier is often used to help agents plan. As shown in “Break Complex Tasks into Simpler Subtasks” on page 224, intent classification can be done using another prompt or a classification model trained for this task. The intent classification mechanism can be considered another agent in your multi-agent system.

Knowing the intent can help the agent pick the right tools. For example, for customer support, if the query is about billing, the agent might need access to a tool to retrieve a user’s recent payments. But if the query is about how to reset a password, the agent might need to access documentation retrieval.

12 Because most agentic workflows are sufficiently complex to involve multiple components, most agents are multi-agent.

Some queries might be out of the scope of the agent. The intent
classifier should be able to classify requests as IRRELEVANT so
that the agent can politely reject those instead of wasting FLOPs
coming up with impossible solutions.
So far, we’ve assumed that the agent automates all three stages: generating plans, vali‐
dating plans, and executing plans. In reality, humans can be involved at any of those
stages to aid with the process and mitigate risks. A human expert can provide a plan,
validate a plan, or execute parts of a plan. For example, for complex tasks for which
an agent has trouble generating the whole plan, a human expert can provide a highlevel plan that the agent can expand upon. If a plan involves risky operations, such as
updating a database or merging a code change, the system can ask for explicit human
approval before executing or let humans execute these operations. To make this pos‐
sible, you need to clearly define the level of automation an agent can have for each
action.
To summarize, solving a task typically involves the following processes. Note that
reflection isn’t mandatory for an agent, but it’ll significantly boost the agent’s perfor‐
mance:
1. Plan generation : come up with a plan for accomplishing this task. A plan is a
sequence of manageable actions, so this process is also called task decomposition.
2. Reflection and error correction: evaluate the generated plan. If it’s a bad plan, gen‐
erate a new one.
3. Execution: take the actions outlined in the generated plan. This often involves
calling specific functions.
4. Reflection and error correction : upon receiving the action outcomes, evaluate
these outcomes and determine whether the goal has been accomplished. Identify
and correct mistakes. If the goal is not completed, generate a new plan.
You’ve already seen some techniques for plan generation and reflection in this book.
When you ask a model to “think step by step”, you’re asking it to decompose a task.
When you ask a model to “verify if your answer is correct”, you’re asking it to reflect.
Foundation models as planners
An open question is how well foundation models can plan. Many researchers believe
that foundation models, at least those built on top of autoregressive language models,
cannot. Meta’s Chief AI Scientist Yann LeCun states unequivocally that autoregres‐
sive LLMs can’t plan  (2023). In the article “Can LLMs Really Reason and Plan?”
Kambhampati (2023)  argues that LLMs are great at extracting knowledge but not
planning. Kambhampati suggests that the papers claiming planning abilities of LLMs
confuse general planning knowledge extracted from the LLMs with executable plans.
284 | Chapter 6: RAG and Agents

[Visual content extracted via GLM-OCR]

Some queries might be out of the scope of the agent. The intent classifier should be able to classify requests as IRRELEVANT so that the agent can politely reject those instead of wasting FLOPs coming up with impossible solutions.

So far, we’ve assumed that the agent automates all three stages: generating plans, validating plans, and executing plans. In reality, humans can be involved at any of those stages to aid with the process and mitigate risks. A human expert can provide a plan, validate a plan, or execute parts of a plan. For example, for complex tasks for which an agent has trouble generating the whole plan, a human expert can provide a high-level plan that the agent can expand upon. If a plan involves risky operations, such as updating a database or merging a code change, the system can ask for explicit human approval before executing or let humans execute these operations. To make this possible, you need to clearly define the level of automation an agent can have for each action.

To summarize, solving a task typically involves the following processes. Note that reflection isn’t mandatory for an agent, but it’ll significantly boost the agent’s performance:

1. **Plan generation**: come up with a plan for accomplishing this task. A plan is a sequence of manageable actions, so this process is also called task decomposition.
2. **Reflection and error correction**: evaluate the generated plan. If it’s a bad plan, generate a new one.
3. **Execution**: take the actions outlined in the generated plan. This often involves calling specific functions.
4. **Reflection and error correction**: upon receiving the action outcomes, evaluate these outcomes and determine whether the goal has been accomplished. Identify and correct mistakes. If the goal is not completed, generate a new plan.

You’ve already seen some techniques for plan generation and reflection in this book. When you ask a model to “think step by step”, you’re asking it to decompose a task. When you ask a model to “verify if your answer is correct”, you’re asking it to reflect.

**Foundation models as planners**

An open question is how well foundation models can plan. Many researchers believe that foundation models, at least those built on top of autoregressive language models, cannot. Meta’s Chief AI Scientist Yann LeCun states unequivocally that autoregressive LLMs can’t plan (2023). In the article “Can LLMs Really Reason and Plan?” Kambhampati (2023) argues that LLMs are great at extracting knowledge but not planning. Kambhampati suggests that the papers claiming planning abilities of LLMs confuse general planning knowledge extracted from the LLMs with executable plans.

“The plans that come out of LLMs may look reasonable to the lay user, and yet lead
to execution time interactions and errors.”
However, while there is a lot of anecdotal evidence that LLMs are poor planners, it’s
unclear whether it’s because we don’t know how to use LLMs the right way or
because LLMs, fundamentally, can’t plan.
Planning, at its core, is a search problem . You search among different paths to the
goal, predict the outcome (reward) of each path, and pick the path with the most
promising outcome. Often, you might determine that no path exists that can take you
to the goal.
Search often requires backtracking. For example, imagine you’re at a step where there
are two possible actions: A and B. After taking action A, you enter a state that’s not
promising, so you need to backtrack to the previous state to take action B.
Some people argue that an autoregressive model can only generate forward actions. It
can’t backtrack to generate alternate actions. Because of this, they conclude that
autoregressive models can’t plan. However, this isn’t necessarily true. After executing
a path with action A, if the model determines that this path doesn’t make sense, it can
revise the path using action B instead, effectively backtracking. The model can also
always start over and choose another path.
It’s also possible that LLMs are poor planners because they aren’t given the toolings
needed to plan. To plan, it’s necessary to know not only the available actions but also
the potential outcome of each action . As a simple example, let’s say you want to walk
up a mountain. Your potential actions are turn right, turn left, turn around, or go
straight ahead. However, if turning right will cause you to fall off the cliff, you might
not want to consider this action. In technical terms, an action takes you from one
state to another, and it’s necessary to know the outcome state to determine whether
to take an action.
This means it’s not sufficient to prompt a model to generate only a sequence of
actions like what the popular chain-of-thought prompting technique does. The paper
“Reasoning with Language Model is Planning with World Model” ( Hao et al., 2023 )
argues that an LLM, by containing so much information about the world, is capable
of predicting the outcome of each action. This LLM can incorporate this outcome
prediction to generate coherent plans.
Even if AI can’t plan, it can still be a part of a planner. It might be possible to aug‐
ment an LLM with a search tool and state tracking system to help it plan.
Agents | 285

Foundation Model (FM) Versus Reinforcement Learning (RL) Planners
The agent is a core concept in RL, which is defined in Wikipedia as a field “concerned
with how an intelligent agent ought to take actions in a dynamic environment in
order to maximize the cumulative reward.”
RL agents and FM agents are similar in many ways. They are both characterized by
their environments and possible actions. The main difference is in how their planners
work. In an RL agent, the planner is trained by an RL algorithm. Training this RL
planner can require a lot of time and resources. In an FM agent, the model is the
planner. This model can be prompted or finetuned to improve its planning capabili‐
ties, and generally requires less time and fewer resources.
However, there’s nothing to prevent an FM agent from incorporating RL algorithms
to improve its performance. I suspect that in the long run, FM agents and RL agents
will merge.
Plan generation
The simplest way to turn a model into a plan generator is with prompt engineering.
Imagine that you want to create an agent to help customers learn about products at
Kitty Vogue. You give this agent access to three external tools: retrieve products by
price, retrieve top products, and retrieve product information. Here’s an example of a
prompt for plan generation. This prompt is for illustration purposes only. Production
prompts are likely more complex:
SYSTEM PROMPT
Propose a plan to solve the task. You have access to 5 actions:
get_today_date()
fetch_top_products(start_date, end_date, num_products)
fetch_product_info(product_name)
generate_query(task_history, tool_output)
generate_response(query)
The plan must be a sequence of valid actions.
Examples
Task: "Tell me about Fruity Fedora"
Plan: [fetch_product_info, generate_query, generate_response]
Task: "What was the best selling product last week?"
Plan: [fetch_top_products, generate_query, generate_response]
286 | Chapter 6: RAG and Agents

Task: {USER INPUT}
Plan:
There are two things to note about this example:
• The plan format used here—a list of functions whose parameters are inferred by
the agent—is just one of many ways to structure the agent control flow.
• The generate_query function takes in the task’s current history and the most
recent tool outputs to generate a query to be fed into the response generator. The
tool output at each step is added to the task’s history.
Given the user input “What’s the price of the best-selling product last week”, a gener‐
ated plan might look like this:
1. get_time()
2. fetch_top_products()
3. fetch_product_info()
4. generate_query()
5. generate_response()
You might wonder, “What about the parameters needed for each function?” The
exact parameters are hard to predict in advance since they are often extracted from
the previous tool outputs. If the first step, get_time(), outputs “2030-09-13”, then
the agent can reason that the parameters for the next step should be called with the
following parameters:
retrieve_top_products(
      start_date=“2030-09-07”,
      end_date=“2030-09-13”,
      num_products=1
)
Often, there’s insufficient information to determine the exact parameter values for a
function. For example, if a user asks, “What’s the average price of best-selling prod‐
ucts?”, the answers to the following questions are unclear:
• How many best-selling products does the user want to look at?
• Does the user want the best-selling products last week, last month, or of all time?
This means that models frequently have to guess, and guesses can be wrong.
Because both the action sequence and the associated parameters are generated by AI
models, they can be hallucinated. Hallucinations can cause the model to call an
invalid function or call a valid function but with wrong parameters. Techniques for
improving a model’s performance in general can be used to improve a model’s plan‐
ning capabilities.
Agents | 287

Here are a few approaches to make an agent better at planning:
• Write a better system prompt with more examples.
• Give better descriptions of the tools and their parameters so that the model
understands them better.
• Rewrite the functions themselves to make them simpler, such as refactoring a
complex function into two simpler functions.
• Use a stronger model. In general, stronger models are better at planning.
• Finetune a model for plan generation.
Function calling.    Many model providers offer tool use for their models, effectively
turning their models into agents. A tool is a function. Invoking a tool is, therefore,
often called function calling . Different model APIs work differently, but in general,
function calling works as follows:
1. Create a tool inventory.
Declare all the tools that you might want a model to use. Each tool is described
by its execution entry point (e.g., its function name), its parameters, and its doc‐
umentation (e.g., what the function does and what parameters it needs).
2. Specify what tools the agent can use.
Because different queries might need different tools, many APIs let you specify a
list of declared tools to be used per query. Some let you control tool use further
by the following settings:
required
The model must use at least one tool.
none
The model shouldn’t use any tool.
auto
The model decides which tools to use.
Function calling is illustrated in Figure 6-10. This is written in pseudocode to make it
representative of multiple APIs. To use a specific API, please refer to its
documentation.
288 | Chapter 6: RAG and Agents

Figure 6-10. An example of a model using two simple tools.
Given a query, an agent defined as in Figure 6-10  will automatically generate what
tools to use and their parameters. Some function calling APIs will make sure that
only valid functions are generated, though they won’t be able to guarantee the correct
parameter values.
For example, given the user query “How many kilograms are 40 pounds?”, the agent
might decide that it needs the tool lbs_to_kg_tool with one parameter value of 40.
The agent’s response might look like this:
response = ModelResponse(
   finish_reason='tool_calls' ,
   message=chat.Message(
       content=None,
       role='assistant' ,
       tool_calls=[
           ToolCall(
               function=Function(
                   arguments='{"lbs":40}' ,
                   name='lbs_to_kg' ),
               type='function' )
       ])
)
Agents | 289

[Visual content extracted via GLM-OCR]

Given a query, an agent defined as in Figure 6-10 will automatically generate what tools to use and their parameters. Some function calling APIs will make sure that only valid functions are generated, though they won’t be able to guarantee the correct parameter values.

For example, given the user query “How many kilograms are 40 pounds?”, the agent might decide that it needs the tool lbs_to_kg_tool with one parameter value of 40. The agent’s response might look like this:

```python
response = ModelResponse(
    finish_reason='tool_calls',
    message=chat.Message(
        content=None,
        role='assistant',
        tool_calls=[
            ToolCall(
                function=Function(
                    arguments=['lbs':40'],
                    name='lbs_to_kg'],
                    type='function')
        ]
    )
)
```

From this response, you can evoke the function lbs_to_kg(lbs=40) and use its out‐
put to generate a response to the users.
When working with agents, always ask the system to report what
parameter values it uses for each function call. Inspect these values
to make sure they are correct.
Planning granularity.    A plan is a roadmap outlining the steps needed to accomplish a
task. A roadmap can be of different levels of granularity. To plan for a year, a quarterby-quarter plan is higher-level than a month-by-month plan, which is, in turn,
higher-level than a week-to-week plan.
There’s a planning/execution trade-off. A detailed plan is harder to generate but eas‐
ier to execute. A higher-level plan is easier to generate but harder to execute. An
approach to circumvent this trade-off is to plan hierarchically. First, use a planner to
generate a high-level plan, such as a quarter-to-quarter plan. Then, for each quarter,
use the same or a different planner to generate a month-to-month plan.
So far, all examples of generated plans use the exact function names, which is very
granular. A problem with this approach is that an agent’s tool inventory can change
over time. For example, the function to get the current date get_time() can be
renamed to get_current_time(). When a tool changes, you’ll need to update your
prompt and all your examples. Using the exact function names also makes it harder
to reuse a planner across different use cases with different tool APIs.
If you’ve previously finetuned a model to generate plans based on the old tool inven‐
tory, you’ll need to finetune the model again on the new tool inventory.
To avoid this problem, plans can also be generated using a more natural language,
which is higher-level than domain-specific function names. For example, given the
query “What’s the price of the best-selling product last week”, an agent can be
instructed to output a plan that looks like this:
1. get current date
2. retrieve the best-selling product last week
3. retrieve product information
4. generate query
5. generate response
290 | Chapter 6: RAG and Agents

[Visual content extracted via GLM-OCR]

From this response, you can evoke the function `lbs_to_kg(lbs=40)` and use its output to generate a response to the users.

When working with agents, always ask the system to report what parameter values it uses for each function call. Inspect these values to make sure they are correct.

**Planning granularity.** A plan is a roadmap outlining the steps needed to accomplish a task. A roadmap can be of different levels of granularity. To plan for a year, a quarter-by-quarter plan is higher-level than a month-by-month plan, which is, in turn, higher-level than a week-to-week plan.

There’s a planning/execution trade-off. A detailed plan is harder to generate but easier to execute. A higher-level plan is easier to generate but harder to execute. An approach to circumvent this trade-off is to plan hierarchically. First, use a planner to generate a high-level plan, such as a quarter-to-quarter plan. Then, for each quarter, use the same or a different planner to generate a month-to-month plan.

So far, all examples of generated plans use the exact function names, which is very granular. A problem with this approach is that an agent’s tool inventory can change over time. For example, the function to get the current date `get_time()` can be renamed to `get_current_time()`. When a tool changes, you’ll need to update your prompt and all your examples. Using the exact function names also makes it harder to reuse a planner across different use cases with different tool APIs.

If you’ve previously finetuned a model to generate plans based on the old tool inventory, you’ll need to finetune the model again on the new tool inventory.

To avoid this problem, plans can also be generated using a more natural language, which is higher-level than domain-specific function names. For example, given the query “What’s the price of the best-selling product last week”, an agent can be instructed to output a plan that looks like this:

1. get current date
2. retrieve the best-selling product last week
3. retrieve product information
4. generate query
5. generate response

13 Chameleon (Lu et al., 2023) calls this translator a program generator.
Using more natural language helps your plan generator become robust to changes in
tool APIs. If your model was trained mostly on natural language, it’ll likely be better
at understanding and generating plans in natural language and less likely to halluci‐
nate.
The downside of this approach is that you need a translator to translate each natural
language action into executable commands. 13 However, translating is a much simpler
task than planning and can be done by weaker models with a lower risk of hallucina‐
tion.
Complex plans.    The plan examples so far have been sequential: the next action in the
plan is always executed after the previous action is done. The order in which actions
can be executed is called a control flow. The sequential form is just one type of control
flow. Other types of control flows include the parallel, if statement, and for loop. The
following list provides an overview of each control flow, including sequential for
comparison:
Sequential
Executing task B after task A is complete, likely because task B depends on task
A. For example, the SQL query can be executed only after it’s been translated
from the natural language input.
Parallel
Executing tasks A and B at the same time. For example, given the query “Find me
best-selling products under $100”, an agent might first retrieve the top 100 bestselling products and, for each of these products, retrieve its price.
If statement
Executing task B or task C depending on the output from the previous step. For
example, the agent first checks NVIDIA’s earnings report. Based on this report, it
can then decide to sell or buy NVIDIA stocks.
For loop
Repeat executing task A until a specific condition is met. For example, keep on
generating random numbers until a prime number.
These different control flows are visualized in Figure 6-11.
Agents | 291

Figure 6-11. Examples of different orders in which a plan can be executed.
In traditional software engineering, conditions for control flows are exact. With AIpowered agents, AI models determine control flows. Plans with non-sequential con‐
trol flows are more difficult to both generate and translate into executable
commands.
When evaluating an agent framework, check what control flows it supports. For
example, if the system needs to browse ten websites, can it do so simultaneously? Par‐
allel execution can significantly reduce the latency perceived by users.
Reflection and error correction
Even the best plans need to be constantly evaluated and adjusted to maximize their
chance of success. While reflection isn’t strictly necessary for an agent to operate, it’s
necessary for an agent to succeed.
Reflection can be useful in many places during a task process:
• After receiving a user query to evaluate if the request is feasible.
• After the initial plan generation to evaluate whether the plan makes sense.
• After each execution step to evaluate if it’s on the right track.
• After the whole plan has been executed to determine if the task has been
accomplished.
292 | Chapter 6: RAG and Agents

[Visual content extracted via GLM-OCR]

In traditional software engineering, conditions for control flows are exact. With AI-powered agents, AI models determine control flows. Plans with non-sequential control flows are more difficult to both generate and translate into executable commands.

When evaluating an agent framework, check what control flows it supports. For example, if the system needs to browse ten websites, can it do so simultaneously? Parallel execution can significantly reduce the latency perceived by users.

Reflection and error correction

Even the best plans need to be constantly evaluated and adjusted to maximize their chance of success. While reflection isn’t strictly necessary for an agent to operate, it’s necessary for an agent to succeed.

Reflection can be useful in many places during a task process:

- After receiving a user query to evaluate if the request is feasible.
- After the initial plan generation to evaluate whether the plan makes sense.
- After each execution step to evaluate if it’s on the right track.
- After the whole plan has been executed to determine if the task has been accomplished.

14 This reminds me of the actor-critic (AC) agent method (Konda and Tsitsiklis, 1999) in reinforcement learn‐
ing.
Reflection and error correction are two different mechanisms that go hand in hand.
Reflection generates insights that help uncover errors to be corrected.
Reflection can be done with the same agent using self-critique prompts. It can also be
done with a separate component, such as a specialized scorer: a model that outputs a
concrete score for each outcome.
First proposed by ReAct ( Yao et al., 2022 ), interleaving reasoning and action has
become a common pattern for agents. Yao et al. used the term “reasoning” to encom‐
pass both planning and reflection. At each step, the agent is asked to explain its
thinking (planning), take actions, then analyze observations (reflection), until the
task is considered finished by the agent. The agent is typically prompted, using exam‐
ples, to generate outputs in the following format:
Thought 1: …
Act 1: …
Observation 1: …
… [continue until reflection determines that the task is finished] …
Thought N: …
Act N: Finish [Response to query]
Figure 6-12 shows an example of an agent following the ReAct framework respond‐
ing to a question from HotpotQA ( Yang et al., 2018 ), a benchmark for multi-hop
question answering.
You can implement reflection in a multi-agent setting: one agent plans and takes
actions, and another agent evaluates the outcome after each step or after a number of
steps.14
If the agent’s response failed to accomplish the task, you can prompt the agent to
reflect on why it failed and how to improve. Based on this suggestion, the agent gen‐
erates a new plan. This allows agents to learn from their mistakes. For example, given
a coding generation task, an evaluator might evaluate that the generated code fails ⅓
of test cases. The agent then reflects the reason it failed is because it didn’t take into
account arrays where all numbers are negative. The actor then generates new code,
taking into account all-negative arrays.
Agents | 293

Figure 6-12. A ReAct agent in action. Image from the ReAct paper (Yao et al., 2022).
The image is licensed under CC BY 4.0.
This is the approach that Reflexion ( Shinn et al., 2023 ) took. In this framework,
reflection is separated into two modules: an evaluator that evaluates the outcome and
a self-reflection module that analyzes what went wrong. Figure 6-13 shows examples
of Reflexion agents in action. The authors used the term “trajectory” to refer to a
plan. At each step, after evaluation and self-reflection, the agent proposes a new tra‐
jectory.
Compared to plan generation, reflection is relatively easy to implement and can bring
surprisingly good performance improvement. The downside of this approach is
latency and cost. Thoughts, observations, and sometimes actions can take a lot of
tokens to generate, which increases cost and user-perceived latency, especially for
tasks with many intermediate steps. To nudge their agents to follow the format, both
ReAct and Reflexion authors used plenty of examples in their prompts. This increases
the cost of computing input tokens and reduces the context space available for other
information.
294 | Chapter 6: RAG and Agents

[Visual content extracted via GLM-OCR]

This is the approach that Reflexion (Shinn et al., 2023) took. In this framework, reflection is separated into two modules: an evaluator that evaluates the outcome and a self-reflection module that analyzes what went wrong. Figure 6-13 shows examples of Reflexion agents in action. The authors used the term “trajectory” to refer to a plan. At each step, after evaluation and self-reflection, the agent proposes a new trajectory.

Compared to plan generation, reflection is relatively easy to implement and can bring surprisingly good performance improvement. The downside of this approach is latency and cost. Thoughts, observations, and sometimes actions can take a lot of tokens to generate, which increases cost and user-perceived latency, especially for tasks with many intermediate steps. To nudge their agents to follow the format, both ReAct and Reflexion authors used plenty of examples in their prompts. This increases the cost of computing input tokens and reduces the context space available for other information.

Figure 6-13. Examples of how Reflexion agents work. Images from the Reflexion Git‐
Hub repo.
Tool selection
Because tools often play a crucial role in a task’s success, tool selection requires care‐
ful consideration. The tools to give your agent depend on the environment and the
task, but they also depend on the AI model that powers the agent.
There’s no foolproof guide on how to select the best set of tools. Agent literature con‐
sists of a wide range of tool inventories. For example, Toolformer (Schick et al., 2023)
finetuned GPT-J to learn five tools. Chameleon ( Lu et al., 2023) uses 13 tools. On the
other hand, Gorilla ( Patil et al., 2023 ) attempted to prompt agents to select the right
API call among 1,645 APIs.
More tools give the agent more capabilities. However, the more tools there are, the
harder it is to efficiently use them. It’s similar to how it’s harder for humans to master
a large set of tools. Adding tools also means increasing tool descriptions, which might
not fit into a model’s context.
Like many other decisions while building AI applications, tool selection requires
experimentation and analysis. Here are a few things you can do to help you decide:
• Compare how an agent performs with different sets of tools.
• Do an ablation study to see how much the agent’s performance drops if a tool is
removed from its inventory. If a tool can be removed without a performance
drop, remove it.
Agents | 295

[Visual content extracted via GLM-OCR]

Tool selection

Because tools often play a crucial role in a task’s success, tool selection requires careful consideration. The tools to give your agent depend on the environment and the task, but they also depend on the AI model that powers the agent.

There’s no foolproof guide on how to select the best set of tools. Agent literature consists of a wide range of tool inventories. For example, Toolformer (Schick et al., 2023) finetuned GPT-J to learn five tools. Chameleon (Lu et al., 2023) uses 13 tools. On the other hand, Gorilla (Patil et al., 2023) attempted to prompt agents to select the right API call among 1,645 APIs.

More tools give the agent more capabilities. However, the more tools there are, the harder it is to efficiently use them. It’s similar to how it’s harder for humans to master a large set of tools. Adding tools also means increasing tool descriptions, which might not fit into a model’s context.

Like many other decisions while building AI applications, tool selection requires experimentation and analysis. Here are a few things you can do to help you decide:

- Compare how an agent performs with different sets of tools.
- Do an ablation study to see how much the agent’s performance drops if a tool is removed from its inventory. If a tool can be removed without a performance drop, remove it.

• Look for tools that the agent frequently makes mistakes on. If a tool proves too
hard for the agent to use—for example, extensive prompting and even finetuning
can’t get the model to learn to use it—change the tool.
• Plot the distribution of tool calls to see what tools are most used and what tools
are least used. Figure 6-14  shows the differences in tool use patterns of GPT-4
and ChatGPT in Chameleon (Lu et al., 2023).
Figure 6-14. Different models and tasks express different tool use patterns. Image from
Lu et al. (2023). Adapted from an original image licensed under CC BY 4.0.
Experiments by Lu et al. (2023) also demonstrate two points:
1. Different tasks require different tools. ScienceQA, the science question answer‐
ing task, relies much more on knowledge retrieval tools than TabMWP, a tabular
math problem-solving task.
2. Different models have different tool preferences. For example, GPT-4 seems to
select a wider set of tools than ChatGPT. ChatGPT seems to favor image caption‐
ing, while GPT-4 seems to favor knowledge retrieval.
When evaluating an agent framework, evaluate what planners and
tools it supports. Different frameworks might focus on different
categories of tools. For example, AutoGPT focuses on social media
APIs (Reddit, X, and Wikipedia), whereas Composio focuses on
enterprise APIs (Google Apps, GitHub, and Slack).
As your needs will likely change over time, evaluate how easy it is
to extend your agent to incorporate new tools.
296 | Chapter 6: RAG and Agents

[Visual content extracted via GLM-OCR]

• Look for tools that the agent frequently makes mistakes on. If a tool proves too hard for the agent to use—for example, extensive prompting and even finetuning can’t get the model to learn to use it—change the tool.

• Plot the distribution of tool calls to see what tools are most used and what tools are least used. Figure 6-14 shows the differences in tool use patterns of GPT-4 and ChatGPT in Chameleon (Lu et al., 2023).

Figure 6-14. Different models and tasks express different tool use patterns. Image from Lu et al. (2023). Adapted from an original image licensed under CC BY 4.0.

Experiments by Lu et al. (2023) also demonstrate two points:

1. Different tasks require different tools. ScienceQA, the science question answering task, relies much more on knowledge retrieval tools than TabMWP, a tabular math problem-solving task.

2. Different models have different tool preferences. For example, GPT-4 seems to select a wider set of tools than ChatGPT. ChatGPT seems to favor image captioning, while GPT-4 seems to favor knowledge retrieval.

When evaluating an agent framework, evaluate what planners and tools it supports. Different frameworks might focus on different categories of tools. For example, AutoGPT focuses on social media APIs (Reddit, X, and Wikipedia), whereas Composio focuses on enterprise APIs (Google Apps, GitHub, and Slack).

As your needs will likely change over time, evaluate how easy it is to extend your agent to incorporate new tools.

As humans, we become more productive not just by using the tools we’re given, but
also by creating progressively more powerful tools from simpler ones. Can AI create
new tools from its initial tools?
Chameleon (Lu et al., 2023) proposes the study of tool transition: after tool X, how
likely is the agent to call tool Y? Figure 6-15 shows an example of tool transition. If
two tools are frequently used together, they can be combined into a bigger tool. If an
agent is aware of this information, the agent itself can combine initial tools to contin‐
ually build more complex tools.
Figure 6-15. A tool transition tree by Lu et al. (2023). Adapted from an original image
licensed under CC BY 4.0.
Vogager ( Wang et al., 2023 ) proposes a skill manager to keep track of new skills
(tools) that an agent acquires for later reuse. Each skill is a coding program. When
the skill manager determines a newly created skill is to be useful (e.g., because it’s
successfully helped an agent accomplish a task), it adds this skill to the skill library
(conceptually similar to the tool inventory). This skill can be retrieved later to use for
other tasks.
Agents | 297

[Visual content extracted via GLM-OCR]

As humans, we become more productive not just by using the tools we’re given, but also by creating progressively more powerful tools from simpler ones. Can AI create new tools from its initial tools?

Chameleon (Lu et al., 2023) proposes the study of tool transition: after tool X, how likely is the agent to call tool Y? Figure 6-15 shows an example of tool transition. If two tools are frequently used together, they can be combined into a bigger tool. If an agent is aware of this information, the agent itself can combine initial tools to continually build more complex tools.

Figure 6-15. A tool transition tree by Lu et al. (2023). Adapted from an original image licensed under CC BY 4.0.

Vogager (Wang et al., 2023) proposes a skill manager to keep track of new skills (tools) that an agent acquires for later reuse. Each skill is a coding program. When the skill manager determines a newly created skill is to be useful (e.g., because it’s successfully helped an agent accomplish a task), it adds this skill to the skill library (conceptually similar to the tool inventory). This skill can be retrieved later to use for other tasks.
