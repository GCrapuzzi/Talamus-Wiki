---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 117
section-title: Agent Overview
source-location: pages 300-301
previous-section: AI Space/normalized/pdf/ai-engineering/sections/116-agents.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/118-tools.md
classification: reusable-knowledge-candidate
---
# Agent Overview

10 Artificial Intelligence: A Modern Approach (1995) defines an agent as anything that can be viewed as perceiv‐
ing its environment through sensors and acting upon that environment through actuators.
AI-powered agents are an emerging field, with no established theo‐
retical frameworks for defining, developing, and evaluating them.
This section is a best-effort attempt to build a framework from the
existing literature, but it will evolve as the field does. Compared to
the rest of the book, this section is more experimental.
This section will start with an overview of agents, and then continue with two aspects
that determine the capabilities of an agent: tools and planning. Agents, with their new
modes of operations, have new modes of failures. This section will end with a discus‐
sion on how to evaluate agents to catch these failures.
Even though agents are novel, they are built upon concepts that have already
appeared in this book, including self-critique, chain-of-thought, and structured out‐
puts.
Agent Overview
The term agent has been used in many different engineering contexts, including but
not limited to a software agent, intelligent agent, user agent, conversational agent,
and reinforcement learning agent. So, what exactly is an agent?
An agent is anything that can perceive its environment and act upon that environ‐
ment.10 This means that an agent is characterized by the environment it operates in
and the set of actions it can perform.
The environment an agent can operate in is defined by its use case. If an agent is
developed to play a game (e.g., Minecraft, Go, Dota), that game is its environment. If
you want an agent to scrape documents from the internet, the environment is the
internet. If your agent is a cooking robot, the kitchen is its environment. A selfdriving car agent’s environment is the road system and its adjacent areas.
The set of actions an AI agent can perform is augmented by the tools it has access to.
Many generative AI-powered applications you interact with daily are agents with
access to tools, albeit simple ones. ChatGPT is an agent. It can search the web, exe‐
cute Python code, and generate images. RAG systems are agents, and text retrievers,
image retrievers, and SQL executors are their tools.
There’s a strong dependency between an agent’s environment and its set of tools. The
environment determines what tools an agent can potentially use. For example, if the
environment is a chess game, the only possible actions for an agent are the valid chess
moves. However, an agent’s tool inventory restricts the environment it can operate
276 | Chapter 6: RAG and Agents

[Visual content extracted via GLM-OCR]

AI-powered agents are an emerging field, with no established theoretical frameworks for defining, developing, and evaluating them. This section is a best-effort attempt to build a framework from the existing literature, but it will evolve as the field does. Compared to the rest of the book, this section is more experimental.

This section will start with an overview of agents, and then continue with two aspects that determine the capabilities of an agent: tools and planning. Agents, with their new modes of operations, have new modes of failures. This section will end with a discussion on how to evaluate agents to catch these failures.

Even though agents are novel, they are built upon concepts that have already appeared in this book, including self-critique, chain-of-thought, and structured outputs.

Agent Overview

The term agent has been used in many different engineering contexts, including but not limited to a software agent, intelligent agent, user agent, conversational agent, and reinforcement learning agent. So, what exactly is an agent?

An agent is anything that can perceive its environment and act upon that environment. This means that an agent is characterized by the environment it operates in and the set of actions it can perform.

The environment an agent can operate in is defined by its use case. If an agent is developed to play a game (e.g., Minecraft, Go, Dota), that game is its environment. If you want an agent to scrape documents from the internet, the environment is the internet. If your agent is a cooking robot, the kitchen is its environment. A self-driving car agent’s environment is the road system and its adjacent areas.

The set of actions an AI agent can perform is augmented by the tools it has access to. Many generative AI-powered applications you interact with daily are agents with access to tools, albeit simple ones. ChatGPT is an agent. It can search the web, execute Python code, and generate images. RAG systems are agents, and text retrievers, image retrievers, and SQL executors are their tools.

There’s a strong dependency between an agent’s environment and its set of tools. The environment determines what tools an agent can potentially use. For example, if the environment is a chess game, the only possible actions for an agent are the valid chess moves. However, an agent’s tool inventory restricts the environment it can operate.

10 Artificial Intelligence: A Modern Approach (1995) defines an agent as anything that can be viewed as perceiving its environment through sensors and acting upon that environment through actuators.

in. For example, if a robot’s only action is swimming, it’ll be confined to a water envi‐
ronment.
Figure 6-8 shows a visualization of SWE-agent ( Yang et al., 2024 ), an agent built on
top of GPT-4. Its environment is the computer with the terminal and the file system.
Its set of actions include navigate repo, search files, view files, and edit lines.
Figure 6-8. SWE-agent (Yang et al., 2024) is a coding agent whose environment is the
computer and whose actions include navigation, search, and editing. Adapted from an
original image licensed under CC BY 4.0.
An AI agent is meant to accomplish tasks typically provided by the users in the
inputs. In an AI agent, AI is the brain that processes the information it receives,
including the task and feedback from the environment, plans a sequence of actions to
achieve this task, and determines whether the task has been accomplished.
Let’s get back to the RAG system with tabular data in the Kitty Vogue example. This
is a simple agent with three actions: response generation, SQL query generation, and
SQL query execution. Given the query “Project the sales revenue for Fruity Fedora
over the next three months”, the agent might perform the following sequence of
actions:
1. Reason about how to accomplish this task. It might decide that to predict future
sales, it first needs the sales numbers from the last five years. Note that the
agent’s reasoning is shown as its intermediate response.
2. Invoke SQL query generation to generate the query to get sales numbers from the
last five years.
3. Invoke SQL query execution to execute this query.
4. Reason about the tool outputs and how they help with sales prediction. It might
decide that these numbers are insufficient to make a reliable projection, perhaps
because of missing values. It then decides that it also needs information about
past marketing campaigns.
Agents | 277

[Visual content extracted via GLM-OCR]

in. For example, if a robot’s only action is swimming, it’ll be confined to a water environment.

Figure 6-8 shows a visualization of SWE-agent (Yang et al., 2024), an agent built on top of GPT-4. Its environment is the computer with the terminal and the file system. Its set of actions include navigate repo, search files, view files, and edit lines.

Figure 6-8. SWE-agent (Yang et al., 2024) is a coding agent whose environment is the computer and whose actions include navigation, search, and editing. Adapted from an original image licensed under CC BY 4.0.

An AI agent is meant to accomplish tasks typically provided by the users in the inputs. In an AI agent, AI is the brain that processes the information it receives, including the task and feedback from the environment, plans a sequence of actions to achieve this task, and determines whether the task has been accomplished.

Let’s get back to the RAG system with tabular data in the Kitty Vogue example. This is a simple agent with three actions: response generation, SQL query generation, and SQL query execution. Given the query “Project the sales revenue for Fruity Fedora over the next three months”, the agent might perform the following sequence of actions:

1. Reason about how to accomplish this task. It might decide that to predict future sales, it first needs the sales numbers from the last five years. Note that the agent’s reasoning is shown as its intermediate response.
2. Invoke SQL query generation to generate the query to get sales numbers from the last five years.
3. Invoke SQL query execution to execute this query.
4. Reason about the tool outputs and how they help with sales prediction. It might decide that these numbers are insufficient to make a reliable projection, perhaps because of missing values. It then decides that it also needs information about past marketing campaigns.
