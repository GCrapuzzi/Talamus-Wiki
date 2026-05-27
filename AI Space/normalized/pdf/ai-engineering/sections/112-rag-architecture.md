---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 112
section-title: RAG Architecture
source-location: pages 280-280
previous-section: AI Space/normalized/pdf/ai-engineering/sections/111-rag.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/113-retrieval-algorithms.md
classification: reusable-knowledge-candidate
---
# RAG Architecture

Anthropic suggested that for Claude models, if “your knowledge
base is smaller than 200,000 tokens (about 500 pages of material),
you can just include the entire knowledge base in the prompt that
you give the model, with no need for RAG or similar methods”
(Anthropic, 2024). It’d be amazing if other model developers pro‐
vide similar guidance for RAG versus long context for their
models.
RAG Architecture
A RAG system has two components: a retriever that retrieves information from
external memory sources and a generator that generates a response based on the
retrieved information. Figure 6-2 shows a high-level architecture of a RAG system.
Figure 6-2. A basic RAG architecture.
In the original RAG paper, Lewis et al. trained the retriever and the generative model
together. In today’s RAG systems, these two components are often trained separately,
and many teams build their RAG systems using off-the-shelf retrievers and models.
However, finetuning the whole RAG system end-to-end can improve its performance
significantly.
The success of a RAG system depends on the quality of its retriever. A retriever has
two main functions: indexing and querying. Indexing involves processing data so that
it can be quickly retrieved later. Sending a query to retrieve data relevant to it is called
querying. How to index data depends on how you want to retrieve it later on.
Now that we’ve covered the primary components, let’s consider an example of how a
RAG system works. For simplicity, let’s assume that the external memory is a data‐
base of documents, such as a company’s memos, contracts, and meeting notes. A
256 | Chapter 6: RAG and Agents

[Visual content extracted via GLM-OCR]

Anthropic suggested that for Claude models, if “your knowledge base is smaller than 200,000 tokens (about 500 pages of material), you can just include the entire knowledge base in the prompt that you give the model, with no need for RAG or similar methods” (Anthropic, 2024). It’d be amazing if other model developers provide similar guidance for RAG versus long context for their models.

RAG Architecture

A RAG system has two components: a retriever that retrieves information from external memory sources and a generator that generates a response based on the retrieved information. Figure 6-2 shows a high-level architecture of a RAG system.

Figure 6-2. A basic RAG architecture.

In the original RAG paper, Lewis et al. trained the retriever and the generative model together. In today’s RAG systems, these two components are often trained separately, and many teams build their RAG systems using off-the-shelf retrievers and models. However, finetuning the whole RAG system end-to-end can improve its performance significantly.

The success of a RAG system depends on the quality of its retriever. A retriever has two main functions: indexing and querying. Indexing involves processing data so that it can be quickly retrieved later. Sending a query to retrieve data relevant to it is called querying. How to index data depends on how you want to retrieve it later on.

Now that we’ve covered the primary components, let’s consider an example of how a RAG system works. For simplicity, let’s assume that the external memory is a database of documents, such as a company’s memos, contracts, and meeting notes. A
