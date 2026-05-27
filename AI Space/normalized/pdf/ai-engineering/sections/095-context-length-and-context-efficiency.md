---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 095
section-title: Context Length and Context Efficiency
source-location: pages 242-243
previous-section: AI Space/normalized/pdf/ai-engineering/sections/094-system-prompt-and-user-prompt.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/096-prompt-engineering-best-practices.md
classification: reusable-knowledge-candidate
---
# Context Length and Context Efficiency

6 Even though Google announced experiments with a 10M context length in February 2024, I didn’t include
this number in the chart as it wasn’t yet available to the public.
Context Length and Context Efficiency
How much information can be included in a prompt depends on the model’s context
length limit. Models’ maximum context length has increased rapidly in recent years.
The first three generations of GPTs have 1K, 2K, and 4K context length, respectively.
This is barely long enough for a college essay and too short for most legal documents
or research papers.
Context length expansion soon became a race among model providers and practi‐
tioners. Figure 5-2 shows how quickly the context length limit is expanding. Within
five years, it grew 2,000 times from GPT-2’s 1K context length to Gemini-1.5 Pro’s
2M context length. A 100K context length can fit a moderate-sized book. As a refer‐
ence, this book contains approximately 120,000 words, or 160,000 tokens. A 2M con‐
text length can fit approximately 2,000 Wikipedia pages and a reasonably complex
codebase such as PyTorch.
Figure 5-2. Context length was expanded from 1K to 2M between February 2019 and
May 2024.6
Not all parts of a prompt are equal. Research has shown that a model is much better
at understanding instructions given at the beginning and the end of a prompt than in
the middle ( Liu et al., 2023 ). One way to evaluate the effectiveness of different parts
of a prompt is to use a test commonly known as the needle in a haystack (NIAH). The
218 | Chapter 5: Prompt Engineering

[Visual content extracted via GLM-OCR]

Context Length and Context Efficiency

How much information can be included in a prompt depends on the model’s context length limit. Models’ maximum context length has increased rapidly in recent years. The first three generations of GPTs have 1K, 2K, and 4K context length, respectively. This is barely long enough for a college essay and too short for most legal documents or research papers.

Context length expansion soon became a race among model providers and practitioners. Figure 5-2 shows how quickly the context length limit is expanding. Within five years, it grew 2,000 times from GPT-2’s 1K context length to Gemini-1.5 Pro’s 2M context length. A 100K context length can fit a moderate-sized book. As a reference, this book contains approximately 120,000 words, or 160,000 tokens. A 2M context length can fit approximately 2,000 Wikipedia pages and a reasonably complex codebase such as PyTorch.

Figure 5-2. Context length was expanded from 1K to 2M between February 2019 and May 2024.

Not all parts of a prompt are equal. Research has shown that a model is much better at understanding instructions given at the beginning and the end of a prompt than in the middle (Liu et al., 2023). One way to evaluate the effectiveness of different parts of a prompt is to use a test commonly known as the needle in a haystack (NIAH). The

7 Shreya Shankar shared a great writeup about a practical NIAH test she did for doctor visits (2024).
idea is to insert a random piece of information (the needle) in different locations in a
prompt (the haystack) and ask the model to find it. Figure 5-3 shows an example of a
piece of information used in Liu et al.’s paper.
Figure 5-3. An example of a needle in a haystack prompt used by Liu et al., 2023
Figure 5-4 shows the result from the paper. All the models tested seemed much better
at finding the information when it’s closer to the beginning and the end of the
prompt than the middle.
Figure 5-4. The effect of changing the position of the inserted information in the prompt
on models’ performance. Lower positions are closer to the start of the input context.
The paper used a randomly generated string, but you can also use real questions and
real answers. For example, if you have the transcript of a long doctor visit, you can
ask the model to return information mentioned throughout the meeting, such as the
drug the patient is using or the blood type of the patient. 7 Make sure that the infor‐
mation you use to test is private to avoid the possibility of it being included in the
model’s training data. If that’s the case, a model might just rely on its internal knowl‐
edge, instead of the context, to answer the question.
Introduction to Prompting | 219

[Visual content extracted via GLM-OCR]

idea is to insert a random piece of information (the needle) in different locations in a prompt (the haystack) and ask the model to find it. Figure 5-3 shows an example of a piece of information used in Liu et al.’s paper.

Figure 5-3. An example of a needle in a haystack prompt used by Liu et al., 2023

Figure 5-4 shows the result from the paper. All the models tested seemed much better at finding the information when it’s closer to the beginning and the end of the prompt than the middle.

Figure 5-4. The effect of changing the position of the inserted information in the prompt on models’ performance. Lower positions are closer to the start of the input context.

The paper used a randomly generated string, but you can also use real questions and real answers. For example, if you have the transcript of a long doctor visit, you can ask the model to return information mentioned throughout the meeting, such as the drug the patient is using or the blood type of the patient. Make sure that the information you use to test is private to avoid the possibility of it being included in the model’s training data. If that’s the case, a model might just rely on its internal knowledge, instead of the context, to answer the question.

7 Shreya Shankar shared a great writeup about a practical NIAH test she did for doctor visits (2024).
