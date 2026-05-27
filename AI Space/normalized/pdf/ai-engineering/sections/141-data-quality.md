---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 141
section-title: Data Quality
source-location: pages 392-392
previous-section: AI Space/normalized/pdf/ai-engineering/sections/140-data-curation.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/142-data-coverage.md
classification: reusable-knowledge-candidate
---
# Data Quality

3 While I love writing, one of the things I absolutely do not enjoy is trying to condense everyone’s opinions into
one single definition. IBM defined data quality along seven dimensions: completeness, uniqueness, validity,
timeliness, accuracy, consistency, and fitness for purpose. Wikipedia added accessibility, comparability, credi‐
bility, flexibility, and plausibility. Many of these definitions focus on data quality in a broad range of use cases.
Here, I want to focus on data quality for finetuning.
Data Quality
A small amount of high-quality data can outperform a large amount of noisy data,
e.g., data that is irrelevant or inconsistent. The creators of the Yi model family found
that 10K carefully crafted instructions are superior to hundreds of thousands of noisy
instructions (Young et al., 2024).
Similarly, “LIMA: Less Is More for Alignment” ( Zhou et al., 2023 ) shows that a 65Bparameter Llama model, finetuned with 1,000 carefully curated prompts and respon‐
ses, can produce answers that are either equivalent or strictly preferred to GPT-4 in
43% of cases, as judged by human annotators. However, the downside of having too
few data examples is that LIMA is not as robust as product-grade models.
The Llama 3 team  also arrived at the same conclusion. Notably, they found that
human-generated data is more prone to errors and inconsistencies, particularly for
nuanced safety policies. This led them to develop AI-assisted annotation tools to
ensure high data quality.
Most people understand the importance of data quality, but what does it mean for
data to be high-quality? The short answer is that data is considered high-quality if it
helps you do your job efficiently and reliably. The long answers, however, differ for
different people.3 In general, data can be considered high-quality if it has the follow‐
ing six characteristics: relevant, aligned with task requirements, consistent, correctly
formatted, unique, and compliant. Some specific use cases might have other require‐
ments:
Relevant
The training examples should be relevant to the task you’re training the model to
do. For example, if the task is to answer legal questions today, a legal dataset
from the 19th century might not be relevant. However, if the task is about the
legal system in the 19th century, this dataset is highly relevant.
Aligned with task requirements
The annotations should align with the task’s requirements. For example, if the
task requires factual consistency, the annotations should be factually correct. If
the task requires creativity, the annotations should be creative. If the task
demands not just a score but also a justification for that score, the annotations
should include both scores and justifications. But if the task demands concise
answers, the annotations should be concise.
368 | Chapter 8: Dataset Engineering
