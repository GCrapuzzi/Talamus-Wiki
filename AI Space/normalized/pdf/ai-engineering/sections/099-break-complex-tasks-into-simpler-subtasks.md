---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 099
section-title: Break Complex Tasks into Simpler Subtasks
source-location: pages 248-250
previous-section: AI Space/normalized/pdf/ai-engineering/sections/098-provide-sufficient-context.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/100-give-the-model-time-to-think.md
classification: reusable-knowledge-candidate
---
# Break Complex Tasks into Simpler Subtasks

You can either provide the model with the necessary context or give it tools to gather
context. The process of gathering necessary context for a given query is called context
construction. Context construction tools include data retrieval, such as in a RAG
pipeline, and web search. These tools are discussed in Chapter 6.
How to Restrict a Model’s Knowledge to Only Its Context
In many scenarios, it’s desirable for the model to use only information provided in
the context to respond. This is especially common for roleplaying and other simula‐
tions. For example, if you want a model to play a character in the game Skyrim, this
character should only know about the Skyrim universe and shouldn’t be able to
answer questions like “What’s your favorite Starbucks item?”
How to restrict a model to only the context is tricky. Clear instructions, such as
“answer using only the provided context”, along with examples of questions it
shouldn’t be able to answer, can help. You can also instruct the model to specifically
quote where in the provided corpus it draws its answer from. This approach can
nudge the model to generate only answers that are supported by the context.
However, since there’s no guarantee that the model will follow all instructions,
prompting alone may not reliably produce the desired outcome. Finetuning a model
on your own corpus is another option, but pre-training data can still leak into its
responses. The safest method is to train a model exclusively on the permitted corpus
of knowledge, though this is often not feasible for most use cases. Additionally, the
corpus may be too limited to train a high-quality model.
Break Complex Tasks into Simpler Subtasks
For complex tasks that require multiple steps, break those tasks into subtasks. Instead
of having one giant prompt for the whole task, each subtask has its own prompt.
These subtasks are then chained together. Consider a customer support chatbot. The
process of responding to a customer request can be decomposed into two steps:
1. Intent classification: identify the intent of the request.
2. Generating response: based on this intent, instruct the model on how to respond.
If there are ten possible intents, you’ll need ten different prompts.
The following example from OpenAI’s prompt engineering guide  shows the intent
classification prompt and the prompt for one intent (troubleshooting). The prompts
are lightly modified for brevity:
224 | Chapter 5: Prompt Engineering

Prompt 1 (intent classification)
SYSTEM
You will be provided with customer service queries. Classify each query
into a primary category and a secondary category. Provide your output in
json format with the keys: primary and secondary.
Primary categories: Billing, Technical Support, Account Management, or
General Inquiry.
Billing secondary categories:
- Unsubscribe or upgrade
- …
Technical Support secondary categories:
- Troubleshooting
- …
Account Management secondary categories:
- …
General Inquiry secondary categories:
- …
USER
I need to get my internet working again.
Prompt 2 (response to a troubleshooting request)
SYSTEM
You will be provided with customer service inquiries that require trouble
shooting in a technical support context. Help the user by:
- Ask them to check that all cables to/from the router are connected.
Note that it is common for cables to come loose over time.
- If all cables are connected and the issue persists, ask them which
router model they are using.
- If the customer's issue persists after restarting the device and
waiting 5 minutes, connect them to IT support by outputting {"IT support
requested"}.
Prompt Engineering Best Practices | 225

9 This parallel processing example is from Anthropic’s prompt engineering guide .
- If the user starts asking questions that are unrelated to this topic
then confirm if they would like to end the current chat about trouble
shooting and classify their request according to the following scheme:
<insert primary/secondary classification scheme from above here>
USER
I need to get my internet working again.
Given this example, you might wonder, why not further decompose the intent classi‐
fication prompt into two prompts, one for the primary category and one for the sec‐
ond category? How small each subtask should be depends on each use case and the
performance, cost, and latency trade-off you’re comfortable with. You’ll need to
experiment to find the optimal decomposition and chaining.
While models are getting better at understanding complex instructions, they are still
better with simpler ones. Prompt decomposition not only enhances performance but
also offers several additional benefits:
Monitoring
You can monitor not just the final output but also all intermediate outputs.
Debugging
You can isolate the step that is having trouble and fix it independently without
changing the model’s behavior at the other steps.
Parallelization
When possible, execute independent steps in parallel to save time. Imagine ask‐
ing a model to generate three different story versions for three different reading
levels: first grade, eighth grade, and college freshman. All these three versions can
be generated at the same time, significantly reducing the output latency.9
Effort
It’s easier to write simple prompts than complex prompts.
226 | Chapter 5: Prompt Engineering
