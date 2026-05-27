---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 139
section-title: Chapter 8. Dataset Engineering
source-location: pages 387-388
previous-section: AI Space/normalized/pdf/ai-engineering/sections/138-summary.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/140-data-curation.md
classification: reusable-knowledge-candidate
---
# Chapter 8. Dataset Engineering

1 The increasing importance of data is reflected in how data effort changed from GPT-3 to GPT-4. In the con‐
tribution list for GPT-3 (OpenAI, 2020), only two people were credited with data collecting, filtering, and
deduplicating, and conducting overlap analysis on the training data. This dramatically changed three years
later. For GPT-4 (OpenAI, 2023), eighty people were credited for being involved in different data processes.
This list doesn’t yet include data annotators that OpenAI contracted through data providers. For something
that sounds as simple as a ChatML format, eleven people were involved, and many of them are senior
researchers. Back in their 2016 AMA (ask me anything) thread, Wojciech Zaremba, one of OpenAI’s
cofounders, said that they intended to conduct most of their research using publicly available datasets.
CHAPTER 8
Dataset Engineering
The quality of a model depends on the quality of its training data. The best ML team
in the world with infinite compute can’t help you finetune a good model if you don’t
have data. The goal of dataset engineering is to create a dataset that allows you to
train the best model, ideally within your allocated budget.
As fewer companies can afford to develop models from scratch, more are turning to
data to differentiate their AI performance. As models demand more data, data han‐
dling becomes more challenging and demands more investments in talent and
infrastructure.1
Data operations have evolved from side tasks that people handle when they have time
to dedicated roles. Many AI companies now employ data labelers, dataset creators,
and data quality engineers, either integrated into or working alongside their core
engineering teams.
If the model landscape is confusing enough with numerous offerings, the data land‐
scape is even more complex, with an ever-growing array of datasets and techniques
being introduced. This chapter gives you an overview of the data landscape and con‐
siderations to take into account when building your own dataset.

It begins with data curation, addressing questions like What data do you need? How
much? What does it mean for data to be of high quality? It then discusses techniques
for data synthesis and processing. Data curation, generation, and processing don’t
follow a linear path. You’ll likely have to go back and forth between different steps.
For the same model, different training phases aim to teach the model different capa‐
bilities, and, therefore, require datasets with different attributes. For example, data
quantity for pre-training is often measured in the number of tokens, whereas data
quantity for supervised finetuning is often measured in the number of examples.
However, at a high level, their curation processes follow the same principle. This
chapter focuses on post-training data because that’s more relevant to application
developers. However, I’ll also include lessons from pre-training data when these les‐
sons are insightful for post-training.
There are best practices you can follow and tools that you can use to automate parts
of the process. However, data will mostly just be toil, tears, and sweat.
A Data-Centric View of AI
The increasing focus on data during AI development has given rise to data-centric AI,
as opposed to model-centric AI:
• Model-centric AI tries to improve AI performance by enhancing the models
themselves. This involves designing new architectures, increasing the sizes of the
models, or developing new training techniques.
• Data-centric AI tries to improve AI performance by enhancing the data. This
involves developing new data processing techniques and creating high-quality
datasets that allow better models to be trained with fewer resources.
In the early days of deep learning, many AI benchmarks were model-centric. Given a
dataset like ImageNet, people try to train the best possible model using the same data‐
set. In recent years, more benchmarks have become data-centric. Given the same
model, people try to develop a dataset that gives this model the best performance.
In 2021, Andrew Ng launched a data-centric AI competition  where participants
needed to improve upon the same base dataset by applying techniques such as fixing
incorrect labels, adding edge case examples, augmenting data, etc.
In 2023, DataComp ( Gadre et al., 2023 ) hosted a competition whose goal was to cre‐
ate the best dataset for training a CLIP model ( Radford et al., 2021 ). A standardized
script trains a CLIP model on each submitted dataset. The quality of a dataset is eval‐
uated based on its resulting model’s performance on 38 downstream tasks. In 2024,
they hosted a similar competition to evaluate datasets for language models with scales
from 412M to 7B parameters ( Li et al., 2024 ). Other similar data-centric benchmarks
include DataPerf (MLCommons, 2023) and dcbench (Eyuboglu and Karlaš, 2022).
364 | Chapter 8: Dataset Engineering
