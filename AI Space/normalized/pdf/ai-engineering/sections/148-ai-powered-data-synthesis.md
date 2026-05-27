---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 148
section-title: AI-Powered Data Synthesis
source-location: pages 410-418
previous-section: AI Space/normalized/pdf/ai-engineering/sections/147-traditional-data-synthesis-techniques.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/149-model-distillation.md
classification: reusable-knowledge-candidate
---
# AI-Powered Data Synthesis

Similarly, it’s very common to simulate training data for robotics in a virtual environ‐
ment. Let’s say you want to train a robot to pour coffee, but you don’t know exactly
how each joint should move to make the action successful. You can simulate multiple
scenarios with different joint movements and use only the scenarios where coffee is
successfully poured to train the robot.
Simulations allow you to run multiple experiments with minimal costs while avoid‐
ing accidents and physical damage. A robot that works in simulations might not
work in the real world, but if it fails in simulations, it’ll likely fail in the real world. No
matter how sophisticated your simulations are, however, they are simplifications of
the real world. Sim2Real is a subfield that focuses on adapting algorithms that have
been trained in simulations to the real world.
Simulations are common to generate data to teach models to use tools. As mentioned
earlier, human-generated actions might not always be the most efficient for AI
agents. Simulations might help uncover actions that humans overlook. Given a query,
you can simulate different action sequences, execute these sequences, and validate
their outcomes. The most efficient action sequence is then used as the annotated
response for the query.
Simulations are particularly valuable for generating data for rare events. For example,
in finance, researchers can simulate scenarios such as a company successfully going
public or a significant bankruptcy to understand their market impacts. Manufactur‐
ers can simulate defects in materials or assemblies to generate data to train anomaly
detection and quality control models. Similarly, by simulating the Earth’s systems,
climate scientists can create variations in temperature changes, precipitation patterns,
and extreme weather scenarios. This synthetic data is then fed into AI models, ena‐
bling them to learn from a broader spectrum of possible futures.
Both rule-based and simulation-based techniques have been useful for many use
cases, but it wasn’t until AI become capable of generating realistic and high-quality
data that data synthesis really took off. Let’s look into those methods next.
AI-Powered Data Synthesis
Just as there are virtually infinite ways for humans to generate data, AI can also do so
in many ways. The techniques discussed here are not comprehensive, but they should
give you a good overview.
Powerful AI models open many new possibilities for simulations . AI can simulate the
outcomes of arbitrary programs. For example, “StableToolBench” ( Guo et al., 2024 )
demonstrates how to use AI to simulate APIs without having to evoke them. Imagine
you want to train a model to interact with a set of APIs. Instead of making actual API
calls—which might be costly or slow—you can use an AI model to simulate the
expected outcomes of those calls.
386 | Chapter 8: Dataset Engineering

AI can simulate humans. For example, imagine you want to train a bot to play chess.
A game played by humans might take too long. Matches with AI players would be
much faster. To train its Dota 2 bot, OpenAI used a simulator that enabled the bot to
play approximately 180 years’ worth of games every day. The bot learned by playing
against itself, an approach called self-play, which helped it develop and refine strate‐
gies over time ( OpenAI, 2019 ). Similarly, DeepMind used self-play to collect data
from millions of Go games to train AlphaGo (Silver et al., 2016).
Self-play is useful not just for game bots but also for general agents. You can have AIs
negotiate against each other using different strategies to see which one works better.
You can have one version of the model play the role of a customer with issues and
another play the customer support agent.
AI’s paraphrasing and translation abilities can be used to augment existing datasets.
For example, given the query “How to reset my password?”, AI can paraphrase it to
create three new queries:
1. “I forgot my password.”
2. “How can I change my password?”
3. “Steps to reset passwords.”
Yu et al. (2023)  rewrote the 15,000 examples in MATH and GSM-8K in different
ways to create MetaMath, a new dataset of almost 400,000 examples. They showed
that their models, trained on this new dataset, outperformed larger models on related
math benchmarks.
It’s common to use AI to translate data in high-resource languages (more available
online) into low-resource languages to help train models in low-resource languages.
This is useful for training a small model specializing in a low-resource language like
Quechua or Lao.
You can verify the quality of translations with back-translation. Let’s say the original
English sentence is X and the translated Lao sentence is Y. You can use another
model to translate the translation back into the original language, Xʹ, then compare
Xʹ with the original sentence X. If they are very different, the translation Y is likely
bad.
AI can translate not just natural languages but also programming languages. You can
use AI to translate code written in one language to another. The Llama 3 authors
used code translation of their SFT dataset with a wider range of programming lan‐
guages. In fact, the training of Llama 3 depends heavily on synthetic data, and the
authors used many creative techniques to generate useful data.
Data Augmentation and Synthesis | 387

For example, they used back-translation to generate code explanations and documen‐
tation. Starting with code snippets, they used AI to generate explanations and docu‐
mentation. They then again used AI to generate code snippets from the explanations
and documentation. Only if the generated code is considered faithful to the original
will the explanation and documentation be used to finetune the model.
AI can generate data for both pre-training and post-training, though synthetic data is
intentionally included much more often in post-training than in pre-training. One
possible explanation for this is that pre-training’s goal is to increase the model’s
knowledge, and while AI can synthesize existing knowledge in different formats, it’s
harder to synthesize new knowledge.
However, as the internet becomes flooded with AI-generated content, models that
rely on internet data are likely already pre-trained on synthetic data. There are also
synthetic datasets such as Cosmopedia (Allal et al., 2024), a 25-billion-token collec‐
tion of synthetic textbooks, blog posts, stories, posts, and WikiHow articles generated
by Mixtral-8x7B-Instruct-v0.1 (Jiang et al., 2024).
Data synthesis for post-training is also more common because post-training data,
including both instruction data and preference data, generally demands the most
effort to produce. Using AI to pick the better response among several responses is
more straightforward—much of it was already covered in Chapter 3. The main chal‐
lenge is to take into account the model’s biases, such as first-position bias, where the
model is more likely to prefer the first option. To avoid this, NVIDIA researchers
asked the AI judge twice, once with the response order swapped. They picked a valid
(prompt, winning, losing) triplet only when the AI judge picked the same winner
both times (NVIDIA, 2024).
The next section will focus on how to use AI to synthesize instruction data for super‐
vised finetuning.
Instruction data synthesis
During instruction finetuning, each example includes an instruction and a response.
AI can be used to synthesize the instructions, the responses, or both. For example,
you can use AI to generate instructions and humans to write responses. You can also
use humans to write instructions and AI to generate responses:
• For instruction generation, to ensure that you generate sufficient instructions to
cover your use case, you can start with a list of topics, keywords, and/or the
instruction types you want in your dataset. Then, for each item on this list, gen‐
erate a certain number of instructions. You can also begin with a set of templates
and generate a certain number of examples per template. Note that both the
topic list and templates can be generated by AI.
388 | Chapter 8: Dataset Engineering

• For response generation, you can generate one or more responses per instruction.

For instance, to create UltraChat (Ding et al., 2023), a multi-turn dialogue dataset, the authors first asked ChatGPT to generate 30 topics about various aspects of our daily lives, such as technology, food and drink, fashion, nature, education, finance, travel, etc. For each topic, they asked ChatGPT to generate 30 to 50 subtopics. The authors then used the same model to generate instructions and corresponding responses for these subtopics.

Similarly, to train Alpaca (Taori et al., 2023), Stanford researchers began with 175 (instruction, response) examples from the Self-Instruct seed dataset (Wang et al., 2022). These examples were originally written to cover a diverse and interesting range of uses. Alpaca authors then used a GPT-3 model, text-davinci-003, to generate 52,000 (instruction, response) pairs that mirrored these seed examples, as shown in Figure 8-5.

**Example seed task**

Instruction: Brainstorm a list of possible New Year’s resolutions.

Output:
• Lose weight
• Exercise more
• Eat healthier

**Example generated task**

Instruction: Brainstorm creative ideas for designing a conference room.

Output:
... incorporating flexible components, such as moveable walls and furniture ...

**Figure 8-5. A seed task and a generated task used to train Alpaca.**

There are also many creative ways to synthesize instruction data with certain characteristics. For example, just like it’s harder for humans to write longer content than shorter content, it’s harder for AI to generate high-quality long responses than short instructions. The longer the response, the more chance AI has to hallucinate. What if we use human-generated responses with AI-generated instructions? Some researchers, such as Köksal et al. (2023), Li et al. (2023), and Chen et al. (2023), follow the reverse instruction approach: take existing long-form, high-quality content like stories, books, and Wikipedia articles and use AI to generate prompts that would elicit such content. This yields higher-quality instruction data, avoiding AI-generated hallucinations in the responses.

11 The implication of this is that, in theory, it’s possible to train a model that can continually improve upon
itself. However, whether this is possible in practice is another story.
It’s possible to use reverse instruction to develop increasingly powerful models
without adding manually annotated data.11 Li et al. (2023) shows how this works:
1. Start with a small number of seed examples to train a weak model.
2. Use this weak model to generate instructions for existing high-quality content to
create high-quality instruction data.
3. Finetune the weak model with this new high-quality instruction data.
4. Repeat until desirable performance is reached.
A creative approach is to use synthetic data to finetune a model for understanding
longer contexts. For example, if your current model processes a maximum of 8K
tokens but you want it to handle 128K tokens, the long-context finetuning process
might look like this:
• Split long documents into shorter chunks (e.g., under 8K tokens).
• For each short chunk, generate several (question, answer) pairs.
• For each (question, answer) pair, use the original long document, which may
exceed 8K tokens but be shorter than your target length, as the context. This
trains the model to use the extended context to answer questions.
The level of detail in the Llama 3 paper ( Dubey et al., 2024) makes it an excellent case
study for instruction data synthesis. I’ve already mentioned two ways in which Llama
3 synthesized data: code translation and code back-translation. Both of these meth‐
ods generate more data from existing code snippets. However, the authors also used
AI to synthesize coding instruction data from scratch, using the following workflow:
1. Use AI to generate a large collection of programming problem descriptions that
span a diverse range of topics.
2. Given a problem description and a programming language, generate a solution.
Dubey et al. found that including general rules of good programming and CoT
reasoning helped improve response quality.
390 | Chapter 8: Dataset Engineering

12 They “observed that about 20% of solutions were initially incorrect but self-corrected, indicating that the
model learned from the execution feedback and improved its performance.”
To ensure the quality of the generated data, they employed a rigorous correctness
analysis and error correction pipeline:
1. Run generated code through parsers and linters to catch syntactic errors such as
missing imports and uninitialized variables.
2. Use unit tests to catch runtime execution errors. Interestingly enough, they used
AI to generate these unit tests.
3. When a solution fails at any step, prompt the model to revise the code. The
prompt included the original problem description, the faulty solution, and feed‐
back from the parser, linter, and unit tests. Only examples that pass all checks are
included in the final supervised finetuning dataset.12
Combining all three methods together—code translation, code back-translation, and
code generation—Llama 3’s data synthesis workflow is quite impressive. To summa‐
rize, here’s how these three methods work together:
1. Use AI to generate problem descriptions.
2. Use AI to generate solutions for each problem in different programming
languages.
3. Use AI to generate unit tests to test the generated code.
4. Prompt AI to fix errors in the synthesized code.
5. Use AI to translate generated code to different programming languages. Filter
out translated code that doesn’t pass tests.
6. Use AI to generate conversations about the code, including code explanation and
adding documentation. Filter out generated explanations and documentation
that doesn’t pass back-translation verification.
Using this pipeline, Dubey et al. were able to generate over 2.7 million synthetic
coding-related examples for the supervised finetuning of Llama 3.1.
Data verification
Given the importance of data quality in the model’s performance, it’s crucial that we
have a way to verify the quality of data. The quality of AI-generated data can be
measured the same way you’d evaluate other AI outputs—by functional correctness
and AI judges.
Data Augmentation and Synthesis | 391

While this section focuses on synthetic data, most of the techniques can be used to
evaluate the quality of training data in general.
Recall the concept of evaluation-driven development from Chapter 4, where compa‐
nies are more likely to create applications they can evaluate. Similarly, people tend to
synthesize data they can verify. Coding is one of the most popular foundation model
use cases because it can be functionally evaluated, and for the same reason, codingrelated examples are among the most commonly synthesized data. Most of the syn‐
thetic data used to train Llama 3 is coding-related. All three methods the authors
used to synthesize data result in data that can be programmatically verified, x, by
code execution and back-translation.
For synthetic data that can’t be verified by functional correctness, it’s common to use
AI verifiers. An AI verifier can be a general-purpose AI judge or a specialized scorer.
There are many ways to frame the verification problem. In the simplest form, the AI
verifier can assign each generated example a score from 1 to 5 or classify each exam‐
ple as good or bad. You can also describe to a foundation model the quality require‐
ments and instruct the model to determine if a data example meets these
requirements.
If you care about the factual consistency of data, you can use the factual inconsistency
detection techniques discussed in Chapter 4 to filter out examples that are likely to
contain hallucinations.
Depending on the use case and the generated data, you can also get creative. For
instance, if you want synthetic data to mimic real data, its quality can be measured by
how difficult it is to distinguish between the two. You could train an AI content
detector to identify AI-generated data—if it’s easy to differentiate between real and
synthetic data, the synthetic data isn’t good. Or, if you want the synthetic data to
resemble high-quality academic work, you could train a classifier to predict whether a
generated paper would be accepted at a prestigious conference like NeurIPS (the
Conference and Workshop on Neural Information Processing Systems) and discard
any papers predicted to be clear rejects.
You can have a model to detect the topic of each generated example and then remove
examples whose topics are irrelevant to your task. If you expect all data to follow a
similar pattern, you can also use anomaly detection to identify outliers—outlier
examples might be of low quality.
Just like real data, synthetic data can also be filtered using heuristics. In general, you
might want to remove examples that are empty or too short for your application. If
an example is too long, you might want to truncate or remove it. You can filter out
data by keywords, by user/author, by creation date, by metadata, or by source. For
example, the Self-Instruct authors (Wang et al., 2022) filtered out generated examples
using the following heuristics:
392 | Chapter 8: Dataset Engineering

13 The same issue can happen with human annotations. If the human labeler uses the knowledge they have but
the model doesn’t to answer a question, they are effectively teaching the model to hallucinate.
• Repetitive examples
• Instructions that are too long or too short
• Examples with the same instruction but different responses
• Examples where the output is a repetition of the input
Even though there are many techniques to evaluate synthetic data, evaluation
remains challenging. As with other AI applications, the ultimate quality test for AIgenerated data is its real-world performance—whether it can improve the model’s
performance—and synthetic data has passed this test for many models.
Limitations to AI-generated data
Given the increasing usefulness of synthetic data, it’s exciting to imagine the possibil‐
ity of never having to worry about human-annotated data again. However, while the
role of synthetic data will certainly continue to grow in importance over time, AIgenerated data might never entirely replace human-generated data. There are many
reasons why, but the four major ones are the difference in quality, the limitations of
imitation, potential model collapse, and the way AI generation of data obscures its
lineage.
Quality control.    AI’s generated data can be of low quality, and, as people never tire of
saying, “garbage in, garbage out.” As mentioned earlier, people will be hesitant to use
synthetic data if they can’t verify its quality. Being able to develop reliable methods
and metrics to evaluate data will be essential in making synthetic data more useful.
Superficial imitation.    As warned by “The False Promise of Imitating Proprietary
LLMs” ( Gudibande et al., 2023 ), the perceived performance achieved by mimicking
might be superficial. This research shows that the imitation models are good at mim‐
icking the style of the teacher models but might struggle with factual accuracy and
generalization to tasks outside the training data.
Worse, imitation can force the student model to hallucinate. Imagine if the teacher
model is capable of answering complex math questions, so its responses to those
questions are solutions. Training a student model on these solutions effectively
teaches it to produce answers that look like solutions, even if the student model isn’t
capable of solving these questions.13 Gudibande et al. (2023) suggest that for improve‐
ment in reasoning capabilities, we need to focus on improving the quality of the base
models.
Data Augmentation and Synthesis | 393

14 The concept was also later explained by the same authors in “AI Models Collapse When Trained on Recur‐
sively Generated Data”  (Nature, July 2024).
Potential model collapse.    It’s also unclear how much AI-generated data a model can
train on. Some studies have shown that recursively using AI-generated data in train‐
ing causes irreversible defects in the resulting models, degrading their performance
over time. In “The Curse of Recursion: Training on Generated Data Makes Models
Forget”, Shumailov et al. (2023) named this phenomenon model collapse and demon‐
strated its occurrences in models including Variational Autoencoders, Gaussian mix‐
ture models, and LLMs. Model collapse can happen during both pre-training and
post-training.14
One possible explanation is that AI models are more likely to generate probable
events (e.g., not having cancer) and less likely to generate improbable events (e.g.,
having cancer). Over multiple iterations, probable events become over-represented,
whereas improbable events become under-represented in the generated data. This
causes models to output more common events over time while forgetting rare events.
In “Is Model Collapse Inevitable?” Gerstgrasser et al. (2024)  argue that while model
collapse is inevitable if the entire training dataset is synthetic, it can be avoided by
mixing synthetic data with real data. Bertrand et al. (2023)  and Dohmatob et al.
(2024) show similar results. However, none of these papers has a definitive recom‐
mendation for the proportion of synthetic data to real data.
Some people have been able to improve model performance using a large amount of
synthetic data. For example, “Common 7B Language Models Already Possess Strong
Math Capabilities” ( Li et al., 2024) demonstrates that synthetic data is nearly as effec‐
tive as real data in finetuning Llama 2-7B models on math problems. In their experi‐
ments, synthetic data shows no clear saturation when scaled up to approximately one
million samples. Similarly, Nemotron-4 340B-Instruct  (NVIDIA, 2024) used 98%
synthetic data during its instruction finetuning and preference finetuning phase.
However, these experiments were carried out for only one model iteration.
AI-generated data might also perpetuate biases. “Data Feedback Loops: Model-driven
Amplification of Dataset Biases” ( Taori and Hashimoto, 2023 ) demonstrates that
when models are trained on datasets that include previous model outputs, any exist‐
ing biases in the model can be amplified. The authors find that the more faithful the
model’s outputs to the characteristics of the original training distribution, the more
stable the feedback loop, thus minimizing the risk of bias amplification.
394 | Chapter 8: Dataset Engineering
