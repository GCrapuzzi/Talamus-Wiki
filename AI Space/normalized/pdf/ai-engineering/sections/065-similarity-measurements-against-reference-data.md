---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 065
section-title: Similarity Measurements Against Reference Data
source-location: pages 151-157
previous-section: AI Space/normalized/pdf/ai-engineering/sections/064-functional-correctness.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/066-introduction-to-embedding.md
classification: reusable-knowledge-candidate
---
# Similarity Measurements Against Reference Data

11 The challenge is that while many complex tasks have measurable objectives, AI isn’t quite good enough to
perform complex tasks end-to-end, so AI might be used to do part of the solution. Sometimes, evaluating a
part of a solution is harder than evaluating the end outcome. Imagine you want to evaluate someone’s ability
to play chess. It’s easier to evaluate the end game outcome (win/lose/draw) than to evaluate just one move.
Test cases (each assert statement represents a test case)
def check(candidate):
      assert candidate([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3) == True
      assert candidate([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.05) == False
      assert candidate([1.0, 2.0, 5.9, 4.0, 5.0], 0.95) == True
      assert candidate([1.0, 2.0, 5.9, 4.0, 5.0], 0.8) == False
      assert candidate([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.1) == True
      assert candidate([1.1, 2.2, 3.1, 4.1, 5.1], 1.0) == True
      assert candidate([1.1, 2.2, 3.1, 4.1, 5.1], 0.5) == False
When evaluating a model, for each problem a number of code samples, denoted as k,
are generated. A model solves a problem if any of the k code samples it generated
pass all of that problem’s test cases. The final score, called pass@k, is the fraction of
the solved problems out of all problems. If there are 10 problems and a model solves
5 with k = 3, then that model’s pass@3 score is 50%. The more code samples a model
generates, the more chance the model has at solving each problem, hence the greater
the final score. This means that in expectation, pass@1 score should be lower than
pass@3, which, in turn, should be lower than pass@10.
Another category of tasks whose functional correctness can be automatically evalu‐
ated is game bots. If you create a bot to play Tetris, you can tell how good the bot is
by the score it gets. Tasks with measurable objectives can typically be evaluated using
functional correctness. For example, if you ask AI to schedule your workloads to
optimize energy consumption, the AI’s performance can be measured by how much
energy it saves.11
Similarity Measurements Against Reference Data
If the task you care about can’t be automatically evaluated using functional correct‐
ness, one common approach is to evaluate AI’s outputs against reference data. For
example, if you ask a model to translate a sentence from French to English, you can
evaluate the generated English translation against the correct English translation.
Each example in the reference data follows the format (input, reference responses).
An input can have multiple reference responses, such as multiple possible English
translations of a French sentence. Reference responses are also called ground truths or
canonical responses. Metrics that require references are reference-based, and metrics
that don’t are  reference-free.
Exact Evaluation | 127

Since this evaluation approach requires reference data, it’s bottlenecked by how much
and how fast reference data can be generated. Reference data is generated typically by
humans and increasingly by AIs. Using human-generated data as the reference
means that we treat human performance as the gold standard, and AI’s performance
is measured against human performance. Human-generated data can be expensive
and time-consuming to generate, leading many to use AI to generate reference data
instead. AI-generated data might still need human reviews, but the labor needed to
review it is much less than the labor needed to generate reference data from scratch.
Generated responses that are more similar to the reference responses are considered
better. There are four ways to measure the similarity between two open-ended texts:
1. Asking an evaluator to make the judgment whether two texts are the same
2. Exact match: whether the generated response matches one of the reference
responses exactly
3. Lexical similarity: how similar the generated response looks to the reference
responses
4. Semantic similarity: how close the generated response is to the reference respon‐
ses in meaning (semantics)
Two responses can be compared by human evaluators or AI evaluators. AI evaluators
are increasingly common and will be the focus of the next section.
This section focuses on hand-designed metrics: exact match, lexical similarity, and
semantic similarity. Scores by exact matching are binary (match or not), whereas the
other two scores are on a sliding scale (such as between 0 and 1 or between –1 and 1).
Despite the ease of use and flexibility of the AI as a judge approach, hand-designed
similarity measurements are still widely used in the industry for their exact nature.
128 | Chapter 3: Evaluation Methodology

This section discusses how you can use similarity measurements to evaluate the quality of a generated output. However, you can also use similarity measurements for many other use cases, including but not limited to the following:

**Retrieval and search**
find items similar to a query

**Ranking**
rank items based on how similar they are to a query

**Clustering**
cluster items based on how similar they are to each other

**Anomaly detection**
detect items that are the least similar to the rest

**Data deduplication**
remove items that are too similar to other items

Techniques discussed in this section will come up again throughout the book.

**Exact match**

It’s considered an exact match if the generated response matches one of the reference responses exactly. Exact matching works for tasks that expect short, exact responses such as simple math problems, common knowledge queries, and trivia-style questions. Here are examples of inputs that have short, exact responses:

• “What’s 2 + 3?”
• “Who was the first woman to win a Nobel Prize?”
• “What’s my current account balance?”
• “Fill in the blank: Paris to France is like ___ to England.”

There are variations to matching that take into account formatting issues. One variation is to accept any output that contains the reference response as a match. Consider the question “What’s 2 + 3?” The reference response is “5”. This variation accepts all outputs that contain “5”, including “The answer is 5” and “2 + 3 is 5”.

However, this variation can sometimes lead to the wrong solution being accepted.
Consider the question “What year was Anne Frank born?” Anne Frank was born on
June 12, 1929, so the correct response is 1929. If the model outputs “September 12,
1929”, the correct year is included in the output, but the output is factually wrong.
Beyond simple tasks, exact match rarely works. Given the original French sentence
“Comment ça va?”, there are multiple possible English translations, such as “How are
you?”, “How is everything?”, and “How are you doing?” If the reference data contains
only these three translations and a model generates “How is it going?”, the model’s
response will be marked as wrong. The longer and more complex the original text,
the more possible translations there are. It’s impossible to create an exhaustive set of
possible responses for an input. For complex tasks, lexical similarity and semantic
similarity work better.
Lexical similarity
Lexical similarity measures how much two texts overlap. You can do this by first
breaking each text into smaller tokens.
In its simplest form, lexical similarity can be measured by counting how many tokens
two texts have in common. As an example, consider the reference response “My cats
scare the mice”  and two generated responses:
• “My cats eat the mice”
• “Cats and mice fight all the time”
Assume that each token is a word. If you count overlapping of individual words only,
response A contains 4 out of 5 words in the reference response (the similarity score is
80%), whereas response B contains only 3 out of 5 (the similarity score is 60%).
Response A is, therefore, considered more similar to the reference response.
One way to measure lexical similarity is approximate string matching , known collo‐
quially as fuzzy matching. It measures the similarity between two texts by counting
how many edits it’d need to convert from one text to another, a number called edit
distance. The usual three edit operations are:
1. Deletion: “b rad” -> “bad”
2. Insertion: “bad” -> “ba rd”
3. Substitution: “b ad” -> “b ed”
Some fuzzy matchers also treat transposition, swapping two letters (e.g., “ma ts” ->
“ma st”), to be an edit. However, some fuzzy matchers treat each transposition as two
edit operations: one deletion and one insertion.
130 | Chapter 3: Evaluation Methodology

12 You might also want to do some processing depending on whether you want “cats” and “cat” or “will not”
and “won’t” to be considered two separate tokens.
For example, “bad” is one edit to “bard” and three edits to “cash”, so “bad” is consid‐
ered more similar to “bard” than to “cash”.
Another way to measure lexical similarity is n-gram similarity , measured based on
the overlapping of sequences of tokens, n-grams, instead of single tokens. A 1-gram
(unigram) is a token. A 2-gram (bigram) is a set of two tokens. “My cats scare the
mice” consists of four bigrams: “my cats”, “cats scare”, “scare the”, and “the mice”.
You measure what percentage of n-grams in reference responses is also in the gener‐
ated response.12
Common metrics for lexical similarity are BLEU, ROUGE, METEOR++, TER,
and CIDEr. They differ in exactly how the overlapping is calculated. Before founda‐
tion models, BLEU, ROUGE, and their relatives were common, especially for transla‐
tion tasks. Since the rise of foundation models, fewer benchmarks use lexical
similarity. Examples of benchmarks that use these metrics are WMT, COCO Cap‐
tions, and GEMv2.
A drawback of this method is that it requires curating a comprehensive set of refer‐
ence responses. A good response can get a low similarity score if the reference set
doesn’t contain any response that looks like it. On some benchmark examples, Adept
found that its model Fuyu performed poorly not because the model’s outputs were
wrong, but because some correct answers were missing in the reference data.
Figure 3-5 shows an example of an image-captioning task in which Fuyu generated a
correct caption but was given a low score.
Not only that, but references can be wrong. For example, the organizers of the WMT
2023 Metrics shared task, which focuses on examining evaluation metrics for
machine translation, reported that they found many bad reference translations in
their data. Low-quality reference data is one of the reasons that reference-free metrics
were strong contenders for reference-based metrics in terms of correlation to human
judgment (Freitag et al., 2023).
Another drawback of this measurement is that higher lexical similarity scores don’t
always mean better responses. For example, on HumanEval, a code generation
benchmark, OpenAI found that BLEU scores for incorrect and correct solutions were
similar. This indicates that optimizing for BLEU scores isn’t the same as optimizing
for functional correctness (Chen et al., 2021).
Exact Evaluation | 131

Figure 3-5. An example where Fuyu generated a correct option but was given a low
score because of the limitation of reference captions.
Semantic similarity
Lexical similarity measures whether two texts look similar, not whether they have the
same meaning. Consider the two sentences “What’s up?” and “How are you?” Lexi‐
cally, they are different—there’s little overlapping in the words and letters they use.
However, semantically, they are close. Conversely, similar-looking texts can mean
very different things. “Let’s eat, grandma” and “Let’s eat grandma” mean two com‐
pletely different things.
Semantic similarity  aims to compute the similarity in semantics. This first requires
transforming a text into a numerical representation, which is called an embedding.
For example, the sentence “the cat sits on a mat” might be represented using an
embedding that looks like this: [0.11, 0.02, 0.54] . Semantic similarity is, there‐
fore, also called embedding similarity.
132 | Chapter 3: Evaluation Methodology

[Visual content extracted via GLM-OCR]

Semantic similarity

Lexical similarity measures whether two texts look similar, not whether they have the same meaning. Consider the two sentences “What’s up?” and “How are you?” Lexically, they are different—there’s little overlapping in the words and letters they use. However, semantically, they are close. Conversely, similar-looking texts can mean very different things. “Let’s eat, grandma” and “Let’s eat grandma” mean two completely different things.

Semantic similarity aims to compute the similarity in semantics. This first requires transforming a text into a numerical representation, which is called an embedding. For example, the sentence “the cat sits on a mat” might be represented using an embedding that looks like this: $[0.11, 0.02, 0.54]$. Semantic similarity is, therefore, also called embedding similarity.

“Introduction to Embedding” on page 134  discusses how embeddings work. For now,
let’s assume that you have a way to transform texts into embeddings. The similarity
between two embeddings can be computed using metrics such as cosine similarity.
Two embeddings that are exactly the same have a similarity score of 1. Two opposite
embeddings have a similarity score of –1.
I’m using text examples, but semantic similarity can be computed for embeddings of
any data modality, including images and audio.  Semantic similarity for text is some‐
times called semantic textual similarity.
While I put semantic similarity in the exact evaluation category, it
can be considered subjective, as different embedding algorithms
can produce different embeddings. However, given two embed‐
dings, the similarity score between them is computed exactly.
Mathematically, let A be an embedding of the generated response, and B be an
embedding of a reference response. The cosine similarity between A and B is compu‐
ted as fracA · B | | A | | | | B | | , with:
•A·B being the dot product of A and B
• | | A | |  being the Euclidean norm (also known as L2 norm) of A. If A is [0.11,
0.02, 0.54], | | A | | = 0.112 + 0.022 + 0.542
Metrics for semantic textual similarity include BERTScore (embeddings are gener‐
ated by BERT) and MoverScore (embeddings are generated by a mixture of
algorithms).
Semantic textual similarity doesn’t require a set of reference responses as comprehen‐
sive as lexical similarity does. However, the reliability of semantic similarity depends
on the quality of the underlying embedding algorithm. Two texts with the same
meaning can still have a low semantic similarity score if their embeddings are bad.
Another drawback of this measurement is that the underlying embedding algorithm
might require nontrivial compute and time to run.
Before we move on to discuss AI as a judge, let’s go over a quick introduction to
embedding. The concept of embedding lies at the heart semantic similarity, and is the
backbone of many topics we explore throughout the book, including vector search in
Chapter 6 and data deduplication in Chapter 8.
Exact Evaluation | 133

[Visual content extracted via GLM-OCR]

“Introduction to Embedding” on page 134 discusses how embeddings work. For now, let’s assume that you have a way to transform texts into embeddings. The similarity between two embeddings can be computed using metrics such as cosine similarity. Two embeddings that are exactly the same have a similarity score of 1. Two opposite embeddings have a similarity score of −1.

I’m using text examples, but semantic similarity can be computed for embeddings of any data modality, including images and audio. Semantic similarity for text is sometimes called semantic textual similarity.

While I put semantic similarity in the exact evaluation category, it can be considered subjective, as different embedding algorithms can produce different embeddings. However, given two embeddings, the similarity score between them is computed exactly.

Mathematically, let A be an embedding of the generated response, and B be an embedding of a reference response. The cosine similarity between A and B is computed as $\frac{A \cdot B}{|A| ||B| |}$, with:

• $A \cdot B$ being the dot product of A and B
• $|A| ||B| = \sqrt{0.11^2 + 0.02^2 + 0.54^2}$

Metrics for semantic textual similarity include BERTScore (embeddings are generated by BERT) and MoverScore (embeddings are generated by a mixture of algorithms).

Semantic textual similarity doesn’t require a set of reference responses as comprehensive as lexical similarity does. However, the reliability of semantic similarity depends on the quality of the underlying embedding algorithm. Two texts with the same meaning can still have a low semantic similarity score if their embeddings are bad. Another drawback of this measurement is that the underlying embedding algorithm might require nontrivial compute and time to run.

Before we move on to discuss AI as a judge, let’s go over a quick introduction to embedding. The concept of embedding lies at the heart semantic similarity, and is the backbone of many topics we explore throughout the book, including vector search in Chapter 6 and data deduplication in Chapter 8.
