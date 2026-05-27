---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 116
section-title: Agents
source-location: pages 299-299
previous-section: AI Space/normalized/pdf/ai-engineering/sections/115-rag-beyond-texts.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/117-agent-overview.md
classification: reusable-knowledge-candidate
---
# Agents

Figure 6-7. A RAG system that augments context with tabular data.
For the text-to-SQL step, if there are many available tables whose schemas can’t all fit
into the model context, you might need an intermediate step to predict what tables to
use for each query. Text-to-SQL can be done by the same generator that generates the
final response or a specialized text-to-SQL model.
In this section, we’ve discussed how tools such as retrievers and SQL executors can
enable models to handle more queries and generate higher-quality responses. Would
giving a model access to more tools improve its capabilities even more? Tool use is a
core characteristic of the agentic pattern, which we’ll discuss in the next section.
Agents
Intelligent agents are considered by many to be the ultimate goal of AI. The classic
book by Stuart Russell and Peter Norvig, Artificial Intelligence: A Modern Approach
(Prentice Hall, 1995) defines the field of artificial intelligence research  as “the study
and design of rational agents.”
The unprecedented capabilities of foundation models have opened the door to
agentic applications that were previously unimaginable. These new capabilities make
it finally possible to develop autonomous, intelligent agents to act as our assistants,
coworkers, and coaches. They can help us create a website, gather data, plan a trip, do
market research, manage a customer account, automate data entry, prepare us for
interviews, interview our candidates, negotiate a deal, etc. The possibilities seem end‐
less, and the potential economic value of these agents is enormous.
Agents | 275

[Visual content extracted via GLM-OCR]

For the text-to-SQL step, if there are many available tables whose schemas can’t all fit into the model context, you might need an intermediate step to predict what tables to use for each query. Text-to-SQL can be done by the same generator that generates the final response or a specialized text-to-SQL model.

In this section, we’ve discussed how tools such as retrievers and SQL executors can enable models to handle more queries and generate higher-quality responses. Would giving a model access to more tools improve its capabilities even more? Tool use is a core characteristic of the agentic pattern, which we’ll discuss in the next section.

Agents

Intelligent agents are considered by many to be the ultimate goal of AI. The classic book by Stuart Russell and Peter Norvig, Artificial Intelligence: A Modern Approach (Prentice Hall, 1995) defines the field of artificial intelligence research as “the study and design of rational agents.”

The unprecedented capabilities of foundation models have opened the door to agentic applications that were previously unimaginable. These new capabilities make it finally possible to develop autonomous, intelligent agents to act as our assistants, coworkers, and coaches. They can help us create a website, gather data, plan a trip, do market research, manage a customer account, automate data entry, prepare us for interviews, interview our candidates, negotiate a deal, etc. The possibilities seem endless, and the potential economic value of these agents is enormous.
