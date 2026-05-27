---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 142
section-title: Data Coverage
source-location: pages 393-395
previous-section: AI Space/normalized/pdf/ai-engineering/sections/141-data-quality.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/143-data-quantity.md
classification: reusable-knowledge-candidate
---
# Data Coverage

4 One painful bug I still remember is when a float column in my data was wrongly stored as integers, which
round these values, leading to perplexing behaviors.
5 While this doesn’t refer to the uniqueness of your data, having data that nobody else has can be extremely
valuable.
I used “aligned” instead of “accurate” or “correct” because, depending on the
task, an accurate or correct response might not be what a user wants.
Consistent
Annotations should be consistent across examples and annotators. If you ask two
annotators to annotate the same example, their annotations shouldn’t be too dif‐
ferent. If the task is to score essays from 1 to 5, would two essays with the same
score be of the same quality? Inconsistent annotations can confuse the model,
making it harder for the model to learn.
Having a good annotation guideline is essential for having annotations that are
both aligned with task requirements and consistent.
Correctly formatted
All examples should follow the format expected by the model. Redundant for‐
matting tokens can interfere with the model’s learning, and, therefore, they
should be removed. For example, if you scrape product reviews from a website,
you should remove HTML tags. Beware of trailing white spaces, new lines,
inconsistent casing, and numerical formats.4
Sufficiently unique
This refers to unique examples in your data. 5 In the context of model training,
duplications can introduce biases and cause data contamination. I use “suffi‐
ciently unique” because specific use cases can tolerate different levels of duplica‐
tions.
Compliant
Data should be compliant with all relevant internal and external policies (includ‐
ing laws and regulations). For example, if you’re not allowed to use PII data to
train your models, your data shouldn’t contain any PII data.
Before setting out to create data, it’s important to think about what each of these
characteristics means for you. The techniques discussed in this section aim to pro‐
duce data with these characteristics.
Data Coverage
A model’s training data should cover the range of problems you expect it to solve.
Real-world users often have a wide range of problems, and the way they express those
problems can vary significantly. Having data that captures the diverse usage patterns
Data Curation | 369

of your application is key for the model to perform well. Coverage requires sufficient
data diversity, which is why many refer to this attribute as data diversity.
For example, if some users construct detailed instructions with abundant references
while some other users prefer short instructions, your finetuning data should include
both detailed and short instructions. If user queries typically have typos, you should
include examples with typos. If your application works with multiple programming
languages, your training data should include the programming languages your users
care about.
Different applications have different dimensions of diversity. For example, a Frenchto-English tool doesn’t need language diversity but might benefit from diversity in
topics, lengths, and speaking styles. On the other hand, a chatbot that recommends
products to global customers doesn’t necessarily need domain diversity, but linguistic
and cultural diversity will be important.
For general-purpose use cases like chatbots, the finetuning data should be diverse,
representing a wide range of topics and speaking patterns. Ding et al., (2023)  believe
that the most straightforward way to further improve the performance of chat lan‐
guage models is to increase the quality and diversity of data employed in the training
process. To develop Nemotron ( Adler et al., 2024 ), NVIDIA researchers focused on
creating a dataset with task diversity, topic diversity, and instruction diversity, which
includes instructions for different output formats, instructions with different output
lengths, and instructions for open-ended answers as well as yes-or-no answers. “The
Data Addition Dilemma” ( Shen et al., 2024) demonstrated that in some cases, adding
more heterogeneous data can lead to worse performance.
Meta shared that Llama 3 doesn’t deviate significantly from older Llama versions in
terms of model architecture. Llama 3’s performance gains are “primarily driven by
improvements in data quality and diversity as well as by increased training scale.”
The Llama 3 paper has rich details on data coverage through all three phases of train‐
ing: pre-training, supervised finetuning, and preference finetuning. While this chap‐
ter focuses on post-training data, it’s useful to look at the data mix  for the same
model across all different training phases to compare and highlight the considera‐
tions for each phase.
A diversity axis that is consistent in all three phases is domain diversity, though what
exactly diverse means differs, as shown in Table 8-1. This table shows only high-level
domains and doesn’t include finer-grained topics, like “geometry”, which is a subcategory in math. Post-training data also has different diversity axes not shown in the
table, such as the number of tokens (both for context and response) and the number
of turns. Llama 3 uses synthetic data for post-training, so another dimension is the
ratio of human-generated data to AI-generated data.
370 | Chapter 8: Dataset Engineering

Table 8-1. For Llama 3, different training phases have different optimal domain mixes.
Pre-training Supervised finetuning Preference finetuning
General knowledge (English) 50% 52.66% 81.99%
Math and reasoning 25% 21.19% 5.89%
Coding 17% 14.89% 6.93%
Multilingual 8% 3.01% 5.19%
Exam-like X 8.14% X
Long context X 0.11% X
It’s interesting to note that during pre-training and supervised finetuning, the num‐
ber of combined math, reasoning, and code tokens accounts for almost half of the
training data. While I don’t know exactly what percentage of the internet data is math
and code, I believe that it’s far below 50%. Llama 3 authors shared that annealing the
model on small amounts of high-quality code and math data (training the model
using an increasingly smaller learning rate with increasingly more code and math
data) can boost the performance of their models on key benchmarks. This confirms a
common belief that high-quality code and math data is more effective than natural
language text in boosting the model’s reasoning capabilities.
The percentage of code and math data during preference finetuning is much smaller
(12.82% combined), likely because the goal is to reflect the real distribution of user
preferences.
This brings up a question: How do we decide on the right data mix? A simple
approach is to choose a data mix that accurately reflects the real-world application
usage. You can also use experiments to find optimal data mixes. For example, Meta
performed scaling law experiments similar to what is discussed in “Scaling extrapola‐
tion” on page 74 . For each candidate data mix, they trained several small models on a
data mix and used that to predict the performance of a large model on that mix. The
final model mix is the best-guess mix derived from the experiment results.
To evaluate the impact of data diversity and quality, Zhou et al. (2023) carried out an
interesting experiment where they trained a 7B-parameter language model on three
datasets of the same size—2,000 examples—but with different characteristics. The
first is high-quality but not diverse. The second is diverse but low-quality. The third
is both diverse and high-quality. Figure 8-1 shows the generation quality of the three
resulting models.
Data Curation | 371
