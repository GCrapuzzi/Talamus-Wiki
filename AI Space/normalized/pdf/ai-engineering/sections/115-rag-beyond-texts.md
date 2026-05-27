---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 115
section-title: RAG Beyond Texts
source-location: pages 297-298
previous-section: AI Space/normalized/pdf/ai-engineering/sections/114-retrieval-optimization.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/116-agents.md
classification: reusable-knowledge-candidate
---
# RAG Beyond Texts

RAG Beyond Texts
The last section discussed text-based RAG systems where the external data sources
are text documents. However, external data sources can also be multimodal and tabu‐
lar data.
Multimodal RAG
If your generator is multimodal, its contexts might be augmented not only with text
documents but also with images, videos, audio, etc., from external sources. I’ll use
images in the examples to keep the writing concise, but you can replace images with
any other modality. Given a query, the retriever fetches both texts and images rele‐
vant to it. For example, given “What’s the color of the house in the Pixar movie Up?”
the retriever can fetch a picture of the house in Up to help the model answer, as
shown in Figure 6-6.
Figure 6-6. Multimodal RAG can augment a query with both text and images. (*The
real image from Up is not used, for copyright reasons.)
If the images have metadata—such as titles, tags, and captions—they can be retrieved
using the metadata. For example, an image is retrieved if its caption is considered rel‐
evant to the query.
If you want to retrieve images based on their content, you’ll need to have a way to
compare images to queries. If queries are texts, you’ll need a multimodal embedding
model that can generate embeddings for both images and texts. Let’s say you use
CLIP (Radford et al., 2021) as the multimodal embedding model. The retriever works
as follows:
RAG | 273

[Visual content extracted via GLM-OCR]

RAG Beyond Texts

The last section discussed text-based RAG systems where the external data sources are text documents. However, external data sources can also be multimodal and tabular data.

Multimodal RAG

If your generator is multimodal, its contexts might be augmented not only with text documents but also with images, videos, audio, etc., from external sources. I’ll use images in the examples to keep the writing concise, but you can replace images with any other modality. Given a query, the retriever fetches both texts and images relevant to it. For example, given “What’s the color of the house in the Pixar movie Up?” the retriever can fetch a picture of the house in Up to help the model answer, as shown in Figure 6-6.

Figure 6-6. Multimodal RAG can augment a query with both text and images. (*The real image from Up is not used, for copyright reasons.)

If the images have metadata—such as titles, tags, and captions—they can be retrieved using the metadata. For example, an image is retrieved if its caption is considered relevant to the query.

If you want to retrieve images based on their content, you’ll need to have a way to compare images to queries. If queries are texts, you’ll need a multimodal embedding model that can generate embeddings for both images and texts. Let’s say you use CLIP (Radford et al., 2021) as the multimodal embedding model. The retriever works as follows:

1. Generate CLIP embeddings for all your data, both texts and images, and store
them in a vector database.
2. Given a query, generate its CLIP embedding.
3. Query in the vector database for all images and texts whose embeddings are close
to the query embedding.
RAG with tabular data
Most applications work not only with unstructured data like texts and images but
also with tabular data. Many queries might need information from data tables to
answer. The workflow for augmenting a context using tabular data is significantly
different from the classic RAG workflow.
Imagine you work for an ecommerce site called Kitty Vogue that specializes in cat
fashion. This store has an order table named Sales, as shown in Table 6-3.
Table 6-3. An example of an order table, Sales, for the imaginary ecommerce site Kitty
Vogue.
Order ID Timestamp Product ID Product Unit price ($) Units Total
1 … 2044 Meow Mix Seasoning 10.99 1 10.99
2 … 3492 Purr & Shake 25 2 50
3 … 2045 Fruity Fedora 18 1 18
… … … … … … …
To generate a response to the question “How many units of Fruity Fedora were sold
in the last 7 days?”, your system needs to query this table for all orders involving
Fruity Fedora and sum the number of units across all orders. Assume that this table
can be queried using SQL. The SQL query might look like this:
SELECT SUM(units) AS total_units_sold
FROM Sales
WHERE product_name = 'Fruity Fedora'
AND timestamp >= DATE_SUB(CURDATE(), INTERVAL 7 DAY);
The workflow is as follows, visualized in Figure 6-7. To run this workflow, your sys‐
tem must have the ability to generate and execute the SQL query:
1. Text-to-SQL: based on the user query and the provided table schemas, determine
what SQL query is needed. Text-to-SQL is an example of semantic parsing, as
discussed in Chapter 2.
2. SQL execution: execute the SQL query.
3. Generation: generate a response based on the SQL result and the original user
query.
274 | Chapter 6: RAG and Agents
