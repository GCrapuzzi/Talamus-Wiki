---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 114
section-title: Retrieval Optimization
source-location: pages 291-296
previous-section: AI Space/normalized/pdf/ai-engineering/sections/113-retrieval-algorithms.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/115-rag-beyond-texts.md
classification: reusable-knowledge-candidate
---
# Retrieval Optimization

Different algorithms can be used in sequence. First, a cheap, less precise retriever,
such as a term-based system, fetches candidates. Then, a more precise but more
expensive mechanism, such as k-nearest neighbors, finds the best of these candidates.
This second step is also called reranking.
For example, given the term “transformer”, you can fetch all documents that contain
the word transformer, regardless of whether they are about the electric device, the
neural architecture, or the movie. Then you use vector search to find among these
documents those that are actually related to your transformer query. As another
example, consider the query “Who’s responsible for the most sales to X?” First, you
might fetch all documents associated with X using the keyword X. Then, you use vec‐
tor search to retrieve the context associated with “Who’s responsible for the most
sales?”
Different algorithms can also be used in parallel as an ensemble. Remember that a
retriever works by ranking documents by their relevance scores to the query. You can
use multiple retrievers to fetch candidates at the same time, then combine these dif‐
ferent rankings together to generate a final ranking.
An algorithm for combining different rankings is called reciprocal rank fusion (RRF)
(Cormack et al., 2009). It assigns each document a score based on its ranking by a
retriever. Intuitively, if it ranks first, its score is 1/1 = 1. If it ranks second, its score is
½ = 0.5. The higher it ranks, the higher its score.
A document’s final score is the sum of its scores with respect to all retrievers. If a
document is ranked first by one retriever and second by another retriever, its score is
1 + 0.5 = 1.5. This example is an oversimplification of RRF, but it shows the basics.
The actual formula for a document D is more complicated, as follows:
Score(D) = ∑i=1
n 1
k + ri(D)
• n is the number of ranked lists; each rank list is produced by a retriever.
•ri(D) is the rank of the document by the retriever i.
• k is a constant to avoid division by zero and to control the influence of lowerranked documents. A typical value for k is 60.
Retrieval Optimization
Depending on the task, certain tactics can increase the chance of relevant documents
being fetched. Four tactics discussed here are chunking strategy, reranking, query
rewriting, and contextual retrieval.
RAG | 267

Chunking strategy
How your data should be indexed depends on how you intend to retrieve it later. The
last section covered different retrieval algorithms and their respective indexing strate‐
gies. There, the discussion was based on the assumption that documents have already
been split into manageable chunks. In this section, I’ll cover different chunking
strategies. This is an important consideration because the chunking strategy you use
can significantly impact the performance of your retrieval system.
The simplest strategy is to chunk documents into chunks of equal length based on a
certain unit. Common units are characters, words, sentences, and paragraphs. For
example, you can split each document into chunks of 2,048 characters or 512 words.
You can also split each document so that each chunk can contain a fixed number of
sentences (such as 20 sentences) or paragraphs (such as each paragraph is its own
chunk).
You can also split documents recursively using increasingly smaller units until each
chunk fits within your maximum chunk size. For example, you can start by splitting a
document into sections. If a section is too long, split it into paragraphs. If a paragraph
is still too long, split it into sentences. This reduces the chance of related texts being
arbitrarily broken off.
Specific documents might also support creative chunking strategies. For example,
there are splitters developed especially for different programming languages. Q&A
documents can be split by question or answer pair, where each pair makes up a
chunk. Chinese texts might need to be split differently from English texts.
When a document is split into chunks without overlap, the chunks might be cut off
in the middle of important context, leading to the loss of critical information. Con‐
sider the text “I left my wife a note”. If it’s split into “I left my wife” and “a note”,
neither of these two chunks conveys the key information of the original text. Over‐
lapping ensures that important boundary information is included in at least one
chunk. If you set the chunk size to be 2,048 characters, you can perhaps set the over‐
lapping size to be 20 characters.
The chunk size shouldn’t exceed the maximum context length of the generative
model. For the embedding-based approach, the chunk size also shouldn’t exceed the
embedding model’s context limit.
You can also chunk documents using tokens, determined by the generative model’s
tokenizer, as a unit. Let’s say that you want to use Llama 3 as your generative model.
You then first tokenize documents using Llama 3’s tokenizer. You can then split
documents into chunks using tokens as the boundaries. Chunking by tokens makes it
easier to work with downstream models. However, the downside of this approach is
that if you switch to another generative model with a different tokenizer, you’d need
to reindex your data.
268 | Chapter 6: RAG and Agents

Regardless of which strategy you choose, chunk sizes matter. A smaller chunk size
allows for more diverse information. Smaller chunks mean that you can fit more
chunks into the model’s context. If you halve the chunk size, you can fit twice as
many chunks. More chunks can provide a model with a wider range of information,
which can enable the model to produce a better answer.
Small chunk sizes, however, can cause the loss of important information. Imagine a
document that contains important information about the topic X throughout the
document, but X is only mentioned in the first half. If you split this document into
two chunks, the second half of the document might not be retrieved, and the model
won’t be able to use its information.
Smaller chunk sizes can also increase computational overhead. This is especially an
issue for embedding-based retrieval. Halving the chunk size means that you have
twice as many chunks to index and twice as many embedding vectors to generate and
store. Your vector search space will be twice as big, which can reduce the query speed.
There is no universal best chunk size or overlap size. You have to experiment to find
what works best for you.
Reranking
The initial document rankings generated by the retriever can be further reranked to
be more accurate. Reranking is especially useful when you need to reduce the number
of retrieved documents, either to fit them into your model’s context or to reduce the
number of input tokens.
One common pattern for reranking is discussed in “Combining retrieval algorithms”
on page 266. A cheap but less precise retriever fetches candidates, then a more precise
but more expensive mechanism reranks these candidates.
Documents can also be reranked based on time, giving higher weight to more recent
data. This is useful for time-sensitive applications such as news aggregation, chat with
your emails (e.g., a chatbot that can answer questions about your emails), or stock
market analysis.
Context reranking differs from traditional search reranking in that the exact position
of items is less critical. In search, the rank (e.g., first or fifth) is crucial. In context
reranking, the order of documents still matters because it affects how well a model
can process them. Models might better understand documents at the beginning and
end of the context, as discussed in “Context Length and Context Efficiency”  on page
218. However, as long as a document is included, the impact of its order is less signif‐
icant compared to search ranking.
RAG | 269

Query rewriting

Query rewriting is also known as query reformulation, query normalization, and sometimes query expansion. Consider the following conversation:

User: When was the last time John Doe bought something from us?
AI: John last bought a Fruity Fedora hat from us two weeks ago, on January 3, 2030.
User: How about Emily Doe?

The last question, “How about Emily Doe?”, is ambiguous without context. If you use this query verbatim to retrieve documents, you’ll likely get irrelevant results. You need to rewrite this query to reflect what the user is actually asking. The new query should make sense on its own. In this case, the query should be rewritten to “When was the last time Emily Doe bought something from us?”

While I put query rewriting in “RAG” on page 253, query rewriting isn’t unique to RAG. In traditional search engines, query rewriting is often done using heuristics. In AI applications, query rewriting can also be done using other AI models, using a prompt similar to “Given the following conversation, rewrite the last user input to reflect what the user is actually asking”. Figure 6-4 shows how ChatGPT rewrote the query using this prompt.

Given the following conversation, rewrite the last user input to reflect what the user is actually asking.

User: When was the last time John Doe bought something from us?
AI: John last bought a Fruity Fedora hat from us two weeks ago, on January 3, 2030.
User: How about Emily Doe?

When was the last time Emily Doe bought something from us?

Figure 6-4. You can use other generative models to rewrite queries.

Query rewriting can get complicated, especially if you need to do identity resolution or incorporate other knowledge. For example, if the user asks “How about his wife?” you will first need to query your database to find out who his wife is. If you don’t have this information, the rewriting model should acknowledge that this query isn’t solvable instead of hallucinating a name, leading to a wrong answer.

9 Some teams have told me that their retrieval systems work best when the data is organized in a question-andanswer format.
Contextual retrieval
The idea behind contextual retrieval is to augment each chunk with relevant context
to make it easier to retrieve the relevant chunks. A simple technique is to augment a
chunk with metadata like tags and keywords. For ecommerce, a product can be aug‐
mented by its description and reviews. Images and videos can be queried by their
titles or captions.
The metadata may also include entities automatically extracted from the chunk. If
your document contains specific terms like the error code EADDRNOTAVAIL (99),
adding them to the document’s metadata allows the system to retrieve it by that key‐
word, even after the document has been converted into embeddings.
You can also augment each chunk with the questions it can answer. For customer
support, you can augment each article with related questions. For example, the article
on how to reset your password can be augmented with queries like “How to reset
password?”, “I forgot my password”, “I can’t log in”, or even “Help, I can’t find my
account”. 9
If a document is split into multiple chunks, some chunks might lack the necessary
context to help the retriever understand what the chunk is about. To avoid this, you
can augment each chunk with the context from the original document, such as the
original document’s title and summary. Anthropic used AI models to generate a
short context, usually 50-100 tokens, that explains the chunk and its relationship to
the original document. Here’s the prompt Anthropic used for this purpose
(Anthropic, 2024):
<document>
{{WHOLE_DOCUMENT}}
</document>
Here is the chunk we want to situate within the whole document:
<chunk>
{{CHUNK_CONTENT}}
</chunk>
Please give a short succinct context to situate this chunk within the
overall document for the purposes of improving search retrieval of the
chunk. Answer only with the succinct context and nothing else.
RAG | 271

The generated context for each chunk is prepended to each chunk, and the augmen‐
ted chunk is then indexed by the retrieval algorithm. Figure 6-5 visualizes the process
that Anthropic follows.
Figure 6-5. Anthropic augments each chunk with a short context that situates this
chunk within the original document, making it easier for the retriever to find the rele‐
vant chunks given a query. Image from “Introducing Contextual Retrieval” (Anthropic,
2024).
Evaluating Retrieval Solutions
Here are some key factors to keep in mind when evaluating a retrieval solution:
• What retrieval mechanisms does it support? Does it support hybrid search?
• If it’s a vector database, what embedding models and vector search algorithms
does it support?
• How scalable is it, both in terms of data storage and query traffic? Does it work
for your traffic patterns?
• How long does it take to index your data? How much data can you process (such
as add/delete) in bulk at once?
• What’s its query latency for different retrieval algorithms?
• If it’s a managed solution, what’s its pricing structure? Is it based on the docu‐
ment/vector volume or on the query volume?
This list doesn’t include the functionalities typically associated with enterprise solu‐
tions such as access control, compliance, data plane and control plane separation, etc.
272 | Chapter 6: RAG and Agents

[Visual content extracted via GLM-OCR]

The generated context for each chunk is prepended to each chunk, and the augmented chunk is then indexed by the retrieval algorithm. Figure 6-5 visualizes the process that Anthropic follows.

Figure 6-5. Anthropic augments each chunk with a short context that situates this chunk within the original document, making it easier for the retriever to find the relevant chunks given a query. Image from “Introducing Contextual Retrieval” (Anthropic, 2024).

Evaluating Retrieval Solutions

Here are some key factors to keep in mind when evaluating a retrieval solution:

• What retrieval mechanisms does it support? Does it support hybrid search?
• If it’s a vector database, what embedding models and vector search algorithms does it support?
• How scalable is it, both in terms of data storage and query traffic? Does it work for your traffic patterns?
• How long does it take to index your data? How much data can you process (such as add/delete) in bulk at once?
• What’s its query latency for different retrieval algorithms?
• If it’s a managed solution, what’s its pricing structure? Is it based on the document/vector volume or on the query volume?

This list doesn’t include the functionalities typically associated with enterprise solutions such as access control, compliance, data plane and control plane separation, etc.
