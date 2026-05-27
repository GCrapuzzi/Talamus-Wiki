---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 097
section-title: Write Clear and Explicit Instructions
source-location: pages 244-246
previous-section: AI Space/normalized/pdf/ai-engineering/sections/096-prompt-engineering-best-practices.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/098-provide-sufficient-context.md
classification: reusable-knowledge-candidate
---
# Write Clear and Explicit Instructions

Similar tests, such as RULER ( Hsieh et al., 2024 ), can also be used to evaluate how
good a model is at processing long prompts. If the model’s performance grows
increasingly worse with a longer context, then perhaps you should find a way to
shorten your prompts.
System prompt, user prompt, examples, and context are the key components of a
prompt. Now that we’ve discussed what a prompt is and why prompting works, let’s
discuss the best practices for writing effective prompts.
Prompt Engineering Best Practices
Prompt engineering can get incredibly hacky, especially for weaker models. In the
early days of prompt engineering, many guides came out with tips such as writing
“Q:” instead of “Questions:” or encouraging models to respond better with the
promise of a “$300 tip for the right answer”. While these tips can be useful for some
models, they can become outdated as models get better at following instructions and
more robust to prompt perturbations.
This section focuses on general techniques that have been proven to work with a wide
range of models and will likely remain relevant in the near future. They are distilled
from prompt engineering tutorials created by model providers, including OpenAI,
Anthropic, Meta, and Google, and best practices shared by teams that have success‐
fully deployed generative AI applications. These companies also often provide libra‐
ries of pre-crafted prompts that you can reference—see Anthropic, Google, and
OpenAI.
Outside of these general practices, each model likely has its own quirks that respond
to specific prompt tricks. When working with a model, you should look for prompt
engineering guides specific to it.
Write Clear and Explicit Instructions
Communicating with AI is the same as communicating with humans: clarity helps.
Here are a few tips on how to write clear instructions.
Explain, without ambiguity, what you want the model to do
If you want the model to score an essay, explain the score system you want to use. Is
it from 1 to 5 or 1 to 10? If there’s an essay the model’s uncertain about, do you want
it to pick a score to the best of its ability or to output “I don’t know”?
As you experiment with a prompt, you might observe undesirable behaviors that
require adjustments to the prompt to prevent them. For example, if the model out‐
puts fractional scores (4.5) and you don’t want fractional scores, update your prompt
to tell the model to output only integer scores.
220 | Chapter 5: Prompt Engineering

Ask the model to adopt a persona
A persona can help the model to understand the perspective it’s supposed to use to
generate responses. Given the essay “I like chickens. Chickens are fluffy and they give
tasty eggs.”, a model out of the box might give it a score of 2 out of 5. However, if you
ask the model to adopt the persona of a first-grade teacher, the essay might get a 4.
See Figure 5-5.
Figure 5-5. Asking a model to adopt a persona can help the model use the right perspec‐
tive to answer your queries.
Provide examples
Examples can reduce ambiguity about how you want the model to respond. Imagine
you’re building a bot to talk to young children. Given the question “Will Santa bring
me presents on Christmas?”, a model might respond that Santa Claus is a fictional
character and, therefore, can’t bring anyone Christmas presents. This answer
wouldn’t endear your bot to your users.
To prevent this, you can provide the model with examples of how to respond to ques‐
tions about fictional characters, such as saying that tooth fairies exist, as demon‐
strated in Table 5-1.
Prompt Engineering Best Practices | 221

[Visual content extracted via GLM-OCR]

Ask the model to adopt a persona

A persona can help the model to understand the perspective it’s supposed to use to generate responses. Given the essay “I like chickens. Chickens are fluffy and they give tasty eggs.”, a model out of the box might give it a score of 2 out of 5. However, if you ask the model to adopt the persona of a first-grade teacher, the essay might get a 4. See Figure 5-5.

Figure 5-5. Asking a model to adopt a persona can help the model use the right perspective to answer your queries.

Provide examples

Examples can reduce ambiguity about how you want the model to respond. Imagine you’re building a bot to talk to young children. Given the question “Will Santa bring me presents on Christmas?”, a model might respond that Santa Claus is a fictional character and, therefore, can’t bring anyone Christmas presents. This answer wouldn’t endear your bot to your users.

To prevent this, you can provide the model with examples of how to respond to questions about fictional characters, such as saying that tooth fairies exist, as demonstrated in Table 5-1.

Table 5-1. Providing an example can nudge the model toward the response you want.
Inspired by Claude’s prompt engineering tutorial .
User prompt AI response
Without
example
Will Santa bring me
presents on Christmas?
Santa Claus is a fictional character that
kids believe in, bringing magic and
excitement to Christmas with stories of his
sleigh, reindeer, and gift-giving journey on
Christmas Eve. Many parents encourage this
belief, as it adds a layer of fun and wonder
for children.
With
example
Q: Is the tooth fairy
real?
A: Of course! Put your
tooth under your pillow
tonight. The tooth fairy
might visit and leave
you something.
Q: Will Santa bring me
presents on Christmas?
A:
Yes, absolutely! Santa loves to bring
presents to kids who believe in him and have
been kind all year. Just make sure you’re
extra good, leave out some cookies, and you
might wake up to find gifts under the tree
on Christmas morning!
This might sound obvious, but if you’re worried about input token length, opt for
example formats that use fewer tokens. For example, the second prompt in Table 5-2
should be preferred over the first prompt, if both have equal performance.
Table 5-2. Some example formats are more expensive than others.
Prompt # tokens
(GPT-4)
Label the following item as edible or inedible.
Input: chickpea
Output: edible
Input: box
Output: inedible
Input: pizza
Output:
Label the following item as edible or inedible.
chickpea --> edible
box --> inedible
pizza -->
222 | Chapter 5: Prompt Engineering
