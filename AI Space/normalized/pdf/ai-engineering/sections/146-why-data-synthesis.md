---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 146
section-title: Why Data Synthesis
source-location: pages 405-406
previous-section: AI Space/normalized/pdf/ai-engineering/sections/145-data-augmentation-and-synthesis.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/147-traditional-data-synthesis-techniques.md
classification: reusable-knowledge-candidate
---
# Why Data Synthesis

notes, contracts, financial statements, product descriptions, images, video commer‐
cials, etc. This makes it easier to generate data and enables more synthetic data use
cases.
While synthetic data promises to significantly reduce the pressure for humangenerated data, synthetic data doesn’t completely replace human data. In many use
cases, as discussed in “Limitations to AI-generated data” on page 393 , mixing humanand AI-generated data often produces the best value.
Why Data Synthesis
Synthetic data is appealing for many reasons. You can synthesize data to improve the
golden data trio: quantity, coverage, and quality. You can also synthesize data to miti‐
gate privacy concerns and distill models:
To increase data quantity
The biggest reason for data synthesis is that it allows you to produce data at scale,
promising an abundant supply of data for training and testing AI models. More
data, in theory, helps models generalize to a wider range of tasks. This is espe‐
cially helpful where real-world data is scarce or difficult to obtain, such as data
for rare weather conditions, data for deep sea exploration, or data involving acci‐
dents for self-driving cars.
To increase data coverage
You can generate data with targeted characteristics to improve model perfor‐
mance or to get a model to express specific behaviors. For example, you can gen‐
erate very short texts or very long texts. You can create conversations that
contain toxic phrases for a toxic detection model. Vice versa, if real-world data is
toxic, you can synthesize safe data. It’s especially common to use AI to synthesize
adversarial examples. It’s also possible to generate data for the rare class to
address the challenges of class imbalance. As described in “TrueTeacher”, Gekh‐
man et al. (2022)  used LLMs to generate factually inconsistent summaries that
they then used to train models to detect factual inconsistency.
In their paper, “Discovering Language Model Behaviors with Model-Written
Evaluations” ( Perez et al., 2022 ), Anthropic discussed various data synthesis
techniques to generate specific datasets that can test 154 different AI behaviors,
including personality traits, political views, ethical stances, and social biases.
They found that in head-to-head comparisons between LM (language model)-
generated and human-generated datasets, “LM-written datasets approach the
quality of human-written ones, sometimes even exceeding them.”
In other words, you can use synthetic data to increase data coverage: generate
targeted data to cover the areas where existing data is insufficient.
Data Augmentation and Synthesis | 381

9 One obvious example that I didn’t include in the main text is when you want to train a model to detect AIgenerated content. You need AI-generated content as training examples.
To increase data quality
Even though the common perception is that synthetic data is often of lower qual‐
ity than human-generated data, sometimes, the reverse can be true. Sometimes,
humans might have fundamental limitations that cause human-generated data to
be of lower quality than AI-generated data.  One example is tool use data dis‐
cussed earlier—humans and AI have fundamentally different modes of opera‐
tions and tool preferences. Another example is in generating complex math
problems—AI can generate questions that are far more complex than what an
average human expert might conceive.9
Some teams also prefer using AI to generate preference data. While each individ‐
ual human can be somewhat consistent in their preference, performance across
different people tends to vary significantly, influenced not only by each person’s
preference but also by mood and motivations. AI-generated preference ratings,
in contrast, can be far more consistent and reliable.
To mitigate privacy concerns
Synthetic data is often the only option for use cases where you can’t use humangenerated data due to privacy concerns. For instance, in healthcare, where legis‐
lation makes it hard, if not impossible, to use real patient records to train a
model, you can generate synthetic patient records that do not contain any sensi‐
tive information. In insurance, you can use synthetic claims instead of using real
claims that include sensitive personal and financial information.
To distill models
Sometimes, you might want to train a model to imitate the behavior of another
model. The goal is often to create a cheaper and/or faster model (the distilled
model) with performance comparable to that of the original model. This is done
by training the distilled model using data generated by the original model.
These are just five of the many reasons why people turn to data synthesis. Because of
its undeniable appeal, more models are being trained with synthetic data and more
techniques are being developed to synthesize data.
382 | Chapter 8: Dataset Engineering
