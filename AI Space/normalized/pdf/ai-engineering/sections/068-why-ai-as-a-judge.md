---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 068
section-title: Why AI as a Judge?
source-location: pages 161-161
previous-section: AI Space/normalized/pdf/ai-engineering/sections/067-ai-as-a-judge.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/069-how-to-use-ai-as-a-judge.md
classification: reusable-knowledge-candidate
---
# Why AI as a Judge?

16 In 2017, I presented at a NeurIPS workshop MEWR (Machine translation Evaluation metric Without Refer‐
ence text), an evaluation method that leverages stronger language models to automatically evaluate machine
translations. Sadly, I never pursued this line of research because life got in the way.
While the idea of using AI to automate evaluation has been around for a long time, 16
it only became practical when AI models became capable of doing so, which was
around 2020 with the release of GPT-3. As of this writing, AI as a judge has become
one of the most, if not the most, common methods for evaluating AI models in pro‐
duction. Most demos of AI evaluation startups I saw in 2023 and 2024 leveraged AI
as a judge in one way or another. LangChain’s State of AI  report in 2023 noted that
58% of evaluations on their platform were done by AI judges. AI as a judge is also an
active area of research.
Why AI as a Judge?
AI judges are fast, easy to use, and relatively cheap compared to human evaluators.
They can also work without reference data, which means they can be used in produc‐
tion environments where there is no reference data.
You can ask AI models to judge an output based on any criteria: correctness, repeti‐
tiveness, toxicity, wholesomeness, hallucinations, and more. This is similar to how
you can ask a person to give their opinion about anything. You might think, “But you
can’t always trust people’s opinions.” That’s true, and you can’t always trust AI’s
judgments, either. However, as each AI model is an aggregation of the masses, it’s
possible for AI models to make judgments representative of the masses. With the
right prompt for the right model, you can get reasonably good judgments on a wide
range of topics.
Studies have shown that certain AI judges are strongly correlated to human evalua‐
tors. In 2023, Zheng et al. found that on their evaluation benchmark, MT-Bench, the
agreement between GPT-4 and humans reached 85%, which is even higher than the
agreement among humans (81%). AlpacaEval authors ( Dubois et al., 2023 ) also
found that their AI judges have a near perfect (0.98) correlation with LMSYS’s Chat
Arena leaderboard, which is evaluated by humans.
Not only can AI evaluate a response, but it can also explain its decision, which can be
especially useful when you want to audit your evaluation results. Figure 3-7 shows an
example of GPT-4 explaining its judgment.
Its flexibility makes AI as a judge useful for a wide range of applications, and for
some applications, it’s the only automatic evaluation option. Even when AI judg‐
ments aren’t as good as human judgments, they might still be good enough to guide
an application’s development and provide sufficient confidence to get a project off
the ground.
AI as a Judge | 137
