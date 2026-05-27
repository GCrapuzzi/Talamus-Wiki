---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 121
section-title: Memory
source-location: pages 324-328
previous-section: AI Space/normalized/pdf/ai-engineering/sections/120-agent-failure-modes-and-evaluation.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/122-summary.md
classification: reusable-knowledge-candidate
---
# Memory

Tool failures can also happen because the agent doesn’t have access to the right tools
for the task. An obvious example is when the task involves retrieving the current
stock prices from the internet, and the agent doesn’t have access to the internet.
Tool failures are tool-dependent. Each tool needs to be tested independently. Always
print out each tool call and its output so that you can inspect and evaluate them. If
you have a translator, create benchmarks to evaluate it.
Detecting missing tool failures requires an understanding of what tools should be
used. If your agent frequently fails on a specific domain, this might be because it lacks
tools for this domain. Work with human domain experts and observe what tools they
would use.
Efficiency
An agent might generate a valid plan using the right tools to accomplish a task, but it
might be inefficient. Here are a few things you might want to track to evaluate an
agent’s efficiency:
• How many steps does the agent need, on average, to complete a task?
• How much does the agent cost, on average, to complete a task?
• How long does each action typically take? Are there any actions that are espe‐
cially time-consuming or expensive?
You can compare these metrics with your baseline, which can be another agent or a
human operator. When comparing AI agents to human agents, keep in mind that
humans and AI have very different modes of operations, so what’s considered effi‐
cient for humans might be inefficient for AI, and vice versa. For example, visiting 100
web pages might be inefficient for a human agent who can visit only one page at a
time, but trivial for an AI agent that can visit all the web pages at once.
In this chapter, we’ve discussed in detail how RAG and agent systems function. Both
patterns often deal with information that exceeds a model’s context limit. A memory
system that supplements the model’s context in handling information can signifi‐
cantly enhance its capabilities. Let’s now explore how a memory system works.
Memory
Memory refers to mechanisms that allow a model to retain and utilize information. A
memory system is especially useful for knowledge-rich applications like RAG and
multi-step applications like agents. A RAG system relies on memory for its augmen‐
ted context, which can grow over multiple turns as it retrieves more information. An
agentic system needs memory to store instructions, examples, context, tool invento‐
ries, plans, tool outputs, reflections, and more. While RAG and agents place greater
300 | Chapter 6: RAG and Agents

demands on memory, it is beneficial for any AI application that requires retaining
information.
An AI model typically has three main memory mechanisms:
Internal knowledge
The model itself is a memory mechanism, as it retains the knowledge from the
data it was trained on. This knowledge is its internal knowledge. A model’s inter‐
nal knowledge doesn’t change unless the model itself is updated. The model can
access this knowledge in all queries.
Short-term memory
A model’s context is a memory mechanism. Previous messages in a conversation
can be added to the model’s context, allowing the model to leverage them to gen‐
erate future responses. A model’s context can be considered its short-term mem‐
ory as it doesn’t persist across tasks (queries). It’s fast to access, but its capacity is
limited. Therefore, it’s often used to store information that is most important for
the current task.
Long-term memory
External data sources that a model can access via retrieval, such as in a RAG sys‐
tem, are a memory mechanism. This can be considered the model’s long-term
memory, as it can be persisted across tasks. Unlike a model’s internal knowledge,
information in the long-term memory can be deleted without updating the
model.
Humans have access to similar memory mechanisms. How to breathe is your internal
knowledge. You typically don’t forget how to breathe unless you’re in serious trouble.
Your short-term memory contains information immediately relevant to what you’re
doing, such as the name of a person you just met. Your long-term memory is aug‐
mented with books, computers, notes, etc.
Which memory mechanism to use for your data depends on its frequency of use.
Information essential for all tasks should be incorporated into the model’s internal
knowledge via training or finetuning. Information that is rarely needed should reside
in its long-term memory. Short-term memory is reserved for immediate, contextspecific information. These three memory mechanisms are illustrated in Figure 6-16.
Memory | 301

Figure 6-16. The hierarchy of information for an agent.
Memory is essential for humans to operate. As AI applications have evolved, develop‐
ers have quickly realized that memory is important for AI models, too. Many mem‐
ory management tools for AI models have been developed, and many model
providers have incorporated external memory. Augmenting an AI model with a
memory system has many benefits. Here are just a few of them:
Manage information overflow within a session
During the process of executing a task, an agent acquires a lot of new informa‐
tion, which can exceed the agent’s maximum context length. The excess informa‐
tion can be stored in a memory system with long-term memories.
Persist information between sessions
An AI coach is practically useless if every time you want the coach’s advice, you
have to explain your whole life story. An AI assistant would be annoying to use if
it keeps forgetting your preferences. Having access to your conversation history
can allow an agent to personalize its actions to you. For example, when you ask
for book recommendations, if the model remembers that you’ve previously loved
The Three-Body Problem, it can suggest similar books.
Boost a model’s consistency
If you ask me a subjective question twice, like rating a joke between 1 and 5, I’m
much more likely to give consistent answers if I remember my previous answer.
Similarly, if an AI model can reference its previous answers, it can calibrate its
future answers to be consistent.
302 | Chapter 6: RAG and Agents

[Visual content extracted via GLM-OCR]

Memory is essential for humans to operate. As AI applications have evolved, developers have quickly realized that memory is important for AI models, too. Many memory management tools for AI models have been developed, and many model providers have incorporated external memory. Augmenting an AI model with a memory system has many benefits. Here are just a few of them:

Manage information overflow within a session
During the process of executing a task, an agent acquires a lot of new information, which can exceed the agent’s maximum context length. The excess information can be stored in a memory system with long-term memories.

Persist information between sessions
An AI coach is practically useless if every time you want the coach’s advice, you have to explain your whole life story. An AI assistant would be annoying to use if it keeps forgetting your preferences. Having access to your conversation history can allow an agent to personalize its actions to you. For example, when you ask for book recommendations, if the model remembers that you’ve previously loved The Three-Body Problem, it can suggest similar books.

Boost a model’s consistency
If you ask me a subjective question twice, like rating a joke between 1 and 5, I’m much more likely to give consistent answers if I remember my previous answer. Similarly, if an AI model can reference its previous answers, it can calibrate its future answers to be consistent.

Maintain data structural integrity
Because text is inherently unstructured, the data stored in the context of a textbased model is unstructured. You can put structured data in the context. For
example, you can feed a table into the context line-by-line, but there’s no guaran‐
tee that the model will understand that this is supposed to be a table. Having a
memory system capable of storing structured data can help maintain the struc‐
tural integrity of your data. For example, if you ask an agent to find potential
sales leads, this agent can leverage an Excel sheet to store the leads. An agent can
also leverage a queue to store the sequence of actions to be performed.
A memory system for AI models typically consists of two functions:
• Memory management: managing what information should be stored in the
short-term and long-term memory.
• Memory retrieval: retrieving information relevant to the task from long-term
memory.
Memory retrieval is similar to RAG retrieval, as long-term memory is an external
data source. In this section, I’ll focus on memory management. Memory manage‐
ment typically consists of two operations: add and delete memory. If memory storage
is limited, deletion might not be necessary. This might work for long-term memory
because external memory storage is relatively cheap and easily extensible. However,
short-term memory is limited by the model’s maximum context length and, there‐
fore, requires a strategy for what to add and what to delete.
Long-term memory can be used to store the overflow from short-term memory. This
operation depends on how much space you want to allocate for short-term memory.
For a given query, the context input into the model consists of both its short-term
memory and information retrieved from its long-term memory. A model’s shortterm capacity is, therefore, determined by how much of the context should be alloca‐
ted for information retrieved from long-term memory. For example, if 30% of the
context is reserved, then the model can use at most 70% of the context limit for shortterm memory. When this threshold is reached, the overflow can be moved to longterm memory.
Like many components previously discussed in this chapter, memory management
isn’t unique to AI applications. Memory management has been a cornerstone of all
data systems, and many strategies have been developed to use memory efficiently.
The simplest strategy is FIFO, first in, first out. The first to be added to the shortterm memory will be the first to be moved to the external storage. As a conversation
gets longer, API providers like OpenAI might start removing the beginning of the
conversation. Frameworks like LangChain might allow the retention of N last mes‐
sages or N last tokens. In a long conversation, this strategy assumes that the early
Memory | 303

15 For human conversations, the opposite might be true if the first few messages are pleasantries.
16 Usage-based strategies, such as removing the least frequently used information, is more challenging, since
you’ll need a way to know when a model uses a given piece of information.
messages are less relevant to the current discussion. However, this assumption can be
fatally wrong. In some conversations, the earliest messages might carry the most
information, especially when the early messages state the purpose of the conversa‐
tion.15 While FIFO is straightforward to implement, it can cause the model to lose
track of important information.16
More-sophisticated strategies involve removing redundancy. Human languages con‐
tain redundancy to enhance clarity and compensate for potential misunderstandings.
If there’s a way to automatically detect redundancy, the memory footprint will be
reduced significantly.
One way to remove redundancy is by using a summary of the conversation. This
summary can be generated using the same or another model. Summarization,
together with tracking named entities, can take you a long way. Bae et al. (2022) took
this a step further. After obtaining the summary, the authors wanted to construct a
new memory by joining the memory with the key information that the summary
missed. The authors developed a classifier that, for each sentence in the memory and
each sentence in the summary, determines if only one, both, or neither should be
added to the new memory.
Liu et al. (2023), on the other hand, used a reflection approach. After each action, the
agent is asked to do two things:
1. Reflect on the information that has just been generated.
2. Determine if this new information should be inserted into the memory, should
merge with the existing memory, or should replace some other information,
especially if the other information is outdated and contradicts new information.
When encountering contradicting pieces of information, some people opt to keep the
newer ones. Some people ask AI models to judge which one to keep. How to handle
contradiction depends on the use case. Having contradictions can cause an agent to
be confused but can also help it draw from different perspectives.
304 | Chapter 6: RAG and Agents
