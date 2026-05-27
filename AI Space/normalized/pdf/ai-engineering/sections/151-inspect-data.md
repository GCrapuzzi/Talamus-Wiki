---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 151
section-title: Inspect Data
source-location: pages 421-422
previous-section: AI Space/normalized/pdf/ai-engineering/sections/150-data-processing.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/152-deduplicate-data.md
classification: reusable-knowledge-candidate
---
# Inspect Data

With a large amount of data, each of these processing steps can
take hours, if not days. Tips to help optimize efficiency during the
process include:
• You can do these data processing steps in whichever order
saves time and compute. For example, if it takes more time to
clean each example than to deduplicate data, you might want
to remove the duplicated examples first before cleaning them.
But if deduplication takes more time than filtering out lowquality data, filter out low-quality data first.
• Always do trial runs to validate that your processing scripts
work as expected before applying the scripts to all your data.
• Avoid changing data in place. Consider keeping a copy of the
original data for two reasons:
— You or another team might need to process the data in dif‐
ferent ways for other applications.
— Bugs in your scripts can potentially corrupt your data.
Inspect Data
Let’s say that after combing through public and internal data, you’ve gathered a raw
dataset. The first thing to do is inspect the data to get a sense of its quality. Get the
data’s information and statistics. Where does the data come from? How has it been
processed? What else has it been used for?
Plot the distribution of tokens (to see what tokens are common), input lengths,
response lengths, etc. Does the data use any special tokens? Can you get a distribu‐
tion of the topics and languages in the data? How relevant are these topics and lan‐
guages to your task?
You can be creative in the statistics to use to understand your data. For example, a
group of Microsoft researchers (2023)  used the distribution of (verb, direct object,
noun) pairs and response length to compare the difference between GPT-3’s and
GPT-4’s generations for the same set of instructions, as shown in Figure 8-6  and
Figure 8-7. This type of analysis is helpful not only to evaluate data but also to evalu‐
ate models.
Data Processing | 397

[Visual content extracted via GLM-OCR]

With a large amount of data, each of these processing steps can take hours, if not days. Tips to help optimize efficiency during the process include:

• You can do these data processing steps in whichever order saves time and compute. For example, if it takes more time to clean each example than to deduplicate data, you might want to remove the duplicated examples first before cleaning them. But if deduplication takes more time than filtering out low-quality data, filter out low-quality data first.

• Always do trial runs to validate that your processing scripts work as expected before applying the scripts to all your data.

• Avoid changing data in place. Consider keeping a copy of the original data for two reasons:

  — You or another team might need to process the data in different ways for other applications.

  — Bugs in your scripts can potentially corrupt your data.

Inspect Data

Let’s say that after combing through public and internal data, you’ve gathered a raw dataset. The first thing to do is inspect the data to get a sense of its quality. Get the data’s information and statistics. Where does the data come from? How has it been processed? What else has it been used for?

Plot the distribution of tokens (to see what tokens are common), input lengths, response lengths, etc. Does the data use any special tokens? Can you get a distribution of the topics and languages in the data? How relevant are these topics and languages to your task?

You can be creative in the statistics to use to understand your data. For example, a group of Microsoft researchers (2023) used the distribution of (verb, direct object, noun) pairs and response length to compare the difference between GPT-3’s and GPT-4’s generations for the same set of instructions, as shown in Figure 8-6 and Figure 8-7. This type of analysis is helpful not only to evaluate data but also to evaluate models.

Figure 8-6. One statistic you can use is the distribution of (verb, direct object noun) in
your data. Image from “Instruction Tuning with GPT-4” (Peng et al., 2023).
Figure 8-7. The distribution of response length for GPT-4 and GPT-3. Image from
“Instruction Tuning with GPT-4” (Peng et al., 2023).
GPT-4 seems to have a broader and more diverse range of verb-noun pairings and
tends to generate longer responses.
Plot these distributions by data source, time, annotator, etc. Do you notice any ques‐
tion patterns that tend to get longer/shorter responses or higher/lower scores? Are
there any outliers? What might be the cause of these outliers? What to do with them?
If the scores are supposed to follow a normal distribution, do scores by all annotators
follow a normal distribution? You might notice that some annotators tend to give
much shorter responses or bias toward higher scores, and it’s up to you to decide
what to do with their annotations.
If each example has more than one annotation, compute the inter-annotator disa‐
greement. Check the examples with conflicting annotations and resolve the conflicts.
398 | Chapter 8: Dataset Engineering

[Visual content extracted via GLM-OCR]

Figure 8-6. One statistic you can use is the distribution of (verb, direct object noun) in your data. Image from “Instruction Tuning with GPT-4” (Peng et al., 2023).

Figure 8-7. The distribution of response length for GPT-4 and GPT-3. Image from “Instruction Tuning with GPT-4” (Peng et al., 2023).

GPT-4 seems to have a broader and more diverse range of verb-noun pairings and tends to generate longer responses.

Plot these distributions by data source, time, annotator, etc. Do you notice any question patterns that tend to get longer/shorter responses or higher/lower scores? Are there any outliers? What might be the cause of these outliers? What to do with them?

If the scores are supposed to follow a normal distribution, do scores by all annotators follow a normal distribution? You might notice that some annotators tend to give much shorter responses or bias toward higher scores, and it’s up to you to decide what to do with their annotations.

If each example has more than one annotation, compute the inter-annotator disagreement. Check the examples with conflicting annotations and resolve the conflicts.
