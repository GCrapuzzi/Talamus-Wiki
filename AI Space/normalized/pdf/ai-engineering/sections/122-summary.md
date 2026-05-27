---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 122
section-title: Summary
source-location: pages 329-330
previous-section: AI Space/normalized/pdf/ai-engineering/sections/121-memory.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/123-chapter-7.-finetuning.md
classification: reusable-knowledge-candidate
---
# Summary

Summary
Given the popularity of RAG and the potential of agents, early readers have men‐
tioned that this is the chapter they’re most excited about.
This chapter started with RAG, the pattern that emerged first between the two. Many
tasks require extensive background knowledge that often exceeds a model’s context
window. For example, code copilots might need access to entire codebases, and
research assistants may need to analyze multiple books. Originally developed to over‐
come a model’s context limitations, RAG also enables more efficient use of informa‐
tion, improving response quality while reducing costs. From the early days of
foundation models, it was clear that the RAG pattern would be immensely valuable
for a wide range of applications, and it has since been rapidly adopted across both
consumer and enterprise use cases.
RAG employs a two-step process. It first retrieves relevant information from external
memory and then uses this information to generate more accurate responses. The
success of a RAG system depends on the quality of its retriever. Term-based retriev‐
ers, such as Elasticsearch and BM25, are much lighter to implement and can provide
strong baselines. Embedding-based retrievers are more computationally intensive but
have the potential to outperform term-based algorithms.
Embedding-based retrieval is powered by vector search, which is also the backbone of
many core internet applications such as search and recommender systems. Many
vector search algorithms developed for these applications can be used for RAG.
The RAG pattern can be seen as a special case of agent where the retriever is a tool
the model can use. Both patterns allow a model to circumvent its context limitation
and stay more up-to-date, but the agentic pattern can do even more than that. An
agent is defined by its environment and the tools it can access. In an AI-powered
agent, AI is the planner that analyzes its given task, considers different solutions, and
picks the most promising one. A complex task can require many steps to solve, which
requires a powerful model to plan. A model’s ability to plan can be augmented with
reflection and a memory system to help it keep track of its progress.
The more tools you give a model, the more capabilities the model has, enabling it to
solve more challenging tasks. However, the more automated the agent becomes, the
more catastrophic its failures can be. Tool use exposes agents to many security risks
discussed in Chapter 5 . For agents to work in the real world, rigorous defensive
mechanisms need to be put in place.
Both RAG and agents work with a lot of information, which often exceeds the maxi‐
mum context length of the underlying model. This necessitates the introduction of a
memory system for managing and using all the information a model has. This chap‐
ter ended with a short discussion on what this component looks like.
Summary | 305

RAG and agents are both prompt-based methods, as they influence the model’s qual‐
ity solely through inputs without modifying the model itself. While they can enable
many incredible applications, modifying the underlying model can open up even
more possibilities. How to do so will be the topic of the next chapter.
306 | Chapter 6: RAG and Agents
