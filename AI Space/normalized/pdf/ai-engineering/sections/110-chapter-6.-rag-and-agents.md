---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 110
section-title: Chapter 6. RAG and Agents
source-location: pages 277-277
previous-section: AI Space/normalized/pdf/ai-engineering/sections/109-summary.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/111-rag.md
classification: reusable-knowledge-candidate
---
# Chapter 6. RAG and Agents

CHAPTER 6
RAG and Agents
To solve a task, a model needs both the instructions on how to do it, and the neces‐
sary information to do so. Just like how a human is more likely to give a wrong
answer when lacking information, AI models are more likely to make mistakes and
hallucinate when they are missing context. For a given application, the model’s
instructions are common to all queries, whereas context is specific to each query. The
last chapter discussed how to write good instructions to the model. This chapter
focuses on how to construct the relevant context for each query.
Two dominating patterns for context construction are RAG, or retrieval-augmented
generation, and agents. The RAG pattern allows the model to retrieve relevant infor‐
mation from external data sources. The agentic pattern allows the model to use tools
such as web search and news APIs to gather information.
While the RAG pattern is chiefly used for constructing context, the agentic pattern
can do much more than that. External tools can help models address their shortcom‐
ings and expand their capabilities. Most importantly, they give models the ability to
directly interact with the world, enabling them to automate many aspects of our lives.
Both RAG and agentic patterns are exciting because of the capabilities they bring to
already powerful models. In a short amount of time, they’ve managed to capture the
collective imagination, leading to incredible demos and products that convince many
people that they are the future. This chapter will go into detail about each of these
patterns, how they work, and what makes them so promising.
RAG
RAG is a technique that enhances a model’s generation by retrieving the relevant
information from external memory sources. An external memory source can be an
internal database, a user’s previous chat sessions, or the internet.
