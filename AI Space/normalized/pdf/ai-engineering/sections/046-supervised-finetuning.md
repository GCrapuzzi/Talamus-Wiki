---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 046
section-title: Supervised Finetuning
source-location: pages 104-106
previous-section: AI Space/normalized/pdf/ai-engineering/sections/045-post-training.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/047-preference-finetuning.md
classification: reusable-knowledge-candidate
---
# Supervised Finetuning

Figure 2-11. Shoggoth with a smiley face. Adapted from an original image shared by
anthrupad.
Note that a combination of pre-training, SFT, and preference finetuning is the popu‐
lar solution for building foundation models today, but it’s not the only solution. You
can skip any of the steps, as you’ll see shortly.
Supervised Finetuning
As discussed in Chapter 1, the pre-trained model is likely optimized for completion
rather than conversing. If you input “How to make pizza” into the model, the model
will continue to complete this sentence, as the model has no concept that this is sup‐
posed to be a conversation. Any of the following three options can be a valid comple‐
tion:
1. Adding more context to the question: “for a family of six?”
2. Adding follow-up questions: “What ingredients do I need? How much time
would it take?”
3. Giving the instructions on how to make pizza.
If the goal is to respond to users appropriately, the correct option is 3.
80 | Chapter 2: Understanding Foundation Models

[Visual content extracted via GLM-OCR]

Note that a combination of pre-training, SFT, and preference finetuning is the popular solution for building foundation models today, but it’s not the only solution. You can skip any of the steps, as you’ll see shortly.

Supervised Finetuning

As discussed in Chapter 1, the pre-trained model is likely optimized for completion rather than conversing. If you input “How to make pizza” into the model, the model will continue to complete this sentence, as the model has no concept that this is supposed to be a conversation. Any of the following three options can be a valid completion:

1. Adding more context to the question: “for a family of six?”
2. Adding follow-up questions: “What ingredients do I need? How much time would it take?”
3. Giving the instructions on how to make pizza.

If the goal is to respond to users appropriately, the correct option is 3.

We know that a model mimics its training data. To encourage a model to generate
the appropriate responses, you can show examples of appropriate responses. Such
examples follow the format ( prompt, response ) and are called demonstration data .
Some people refer to this process as behavior cloning : you demonstrate how the
model should behave, and the model clones this behavior.
Since different types of requests require different types of responses, your demonstra‐
tion data should contain the range of requests you want your model to handle, such
as question answering, summarization, and translation. Figure 2-12 shows a distribu‐
tion of types of tasks OpenAI used to finetune their model InstructGPT. Note that
this distribution doesn’t contain multimodal tasks, as InstructGPT is a text-only
model.
Figure 2-12. The distribution of prompts used to finetune InstructGPT. The graph is
created based on the numbers from the OpenAI paper.
Good teachers are important for humans to learn. Similarly, good labelers are impor‐
tant for AIs to learn how to conduct intelligent conversations. Unlike traditional data
labeling, which can often be done with little or no domain expertise, demonstration
Post-Training | 81

[Visual content extracted via GLM-OCR]

We know that a model mimics its training data. To encourage a model to generate the appropriate responses, you can show examples of appropriate responses. Such examples follow the format (prompt, response) and are called demonstration data. Some people refer to this process as behavior cloning: you demonstrate how the model should behave, and the model clones this behavior.

Since different types of requests require different types of responses, your demonstration data should contain the range of requests you want your model to handle, such as question answering, summarization, and translation. Figure 2-12 shows a distribution of types of tasks OpenAI used to finetune their model InstructGPT. Note that this distribution doesn’t contain multimodal tasks, as InstructGPT is a text-only model.

Figure 2-12. The distribution of prompts used to finetune InstructGPT. The graph is created based on the numbers from the OpenAI paper.

Good teachers are important for humans to learn. Similarly, good labelers are important for AIs to learn how to conduct intelligent conversations. Unlike traditional data labeling, which can often be done with little or no domain expertise, demonstration

data may contain complex prompts whose responses require critical thinking, infor‐
mation gathering, and judgment about the appropriateness of the user’s requests.
Table 2-6  shows examples of (prompt, response) pairs created by labelers for
InstructGPT.
Table 2-6. Examples of demonstration data used for InstructGPT.
Prompt Labeler’s response
Serendipity means the occurrence and
development of events by chance in a
happy or beneficial way. Use the word
in a sentence.
Running into Margaret and being intro
duced to Tom was a fortunate stroke of
serendipity.
Read the following text and answer
the three questions at the end.
[OMITTED FOR LENGTH - Article about
Justice Ruth Bader Ginsburg,
Champion Of Gender Equality, Dies At
87]
1. …
2. …
3. Why will Ginsburg’s death have
profound consequences for the court
and the country?
1. …
2. …
3. Ruth Bader Ginsburg was the leader of
the liberal wing, and because the court
is about to open a new term, the chief
justice no longer holds the controlling
vote in contested cases.
ELI5: What’s the cause of the
"anxiety lump" in our chest during
stressful or disheartening
experiences?
The anxiety lump in your throat is caused
by muscular tension keeping your glottis
dilated to maximize airflow. The clenched
chest or heartache feeling is caused by
the vagus nerve which tells the organs to
pump blood faster, stop digesting, and
produce adrenaline and cortisol.
Companies, therefore, often use highly educated labelers to generate demonstration
data. Among those who labeled demonstration data for InstructGPT, ~90% have at
least a college degree  and more than one-third have a master’s degree. If labeling
objects in an image might take only seconds, generating one (prompt, response) pair
can take up to 30 minutes, especially for tasks that involve long contexts like summa‐
rization. If it costs $10 for one (prompt, response) pair, the 13,000 pairs that OpenAI
used for InstructGPT would cost $130,000. That doesn’t yet include the cost of
designing the data (what tasks and prompts to include), recruiting labelers, and data
quality control.
82 | Chapter 2: Understanding Foundation Models
