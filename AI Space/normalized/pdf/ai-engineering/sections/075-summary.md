---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 075
section-title: Summary
source-location: pages 180-182
previous-section: AI Space/normalized/pdf/ai-engineering/sections/074-the-future-of-comparative-evaluation.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/076-chapter-4.-evaluate-ai-systems.md
classification: reusable-knowledge-candidate
---
# Summary

Comparative evaluation can give us discriminating signals about models that can’t be
obtained otherwise. For offline evaluation, it can be a great addition to evaluation
benchmarks. For online evaluation, it can be complementary to A/B testing.
Summary
The stronger AI models become, the higher the potential for catastrophic failures,
which makes evaluation even more important. At the same time, evaluating openended, powerful models is challenging. These challenges make many teams turn
toward human evaluation. Having humans in the loop for sanity checks is always
helpful, and in many cases, human evaluation is essential. However, this chapter
focused on different approaches to automatic evaluation.
This chapter starts with a discussion on why foundation models are harder to evalu‐
ate than traditional ML models. While many new evaluation techniques are being
developed, investments in evaluation still lag behind investments in model and appli‐
cation development.
Since many foundation models have a language model component, we zoomed into
language modeling metrics, including perplexity and cross entropy. Many people I’ve
talked to find these metrics confusing, so I included a section on how to interpret
these metrics and leverage them in evaluation and data processing.
This chapter then shifted the focus to the different approaches to evaluate openended responses, including functional correctness, similarity scores, and AI as a
judge. The first two evaluation approaches are exact, while AI as a judge evaluation is
subjective.
Unlike exact evaluation, subjective metrics are highly dependent on the judge. Their
scores need to be interpreted in the context of what judges are being used. Scores
aimed to measure the same quality by different AI judges might not be comparable.
AI judges, like all AI applications, should be iterated upon, meaning their judgments
change. This makes them unreliable as benchmarks to track an application’s changes
over time. While promising, AI judges should be supplemented with exact evalua‐
tion, human evaluation, or both.
When evaluating models, you can evaluate each model independently, and then rank
them by their scores. Alternatively, you can rank them using comparative signals:
which of the two models is better? Comparative evaluation is common in sports,
especially chess, and is gaining traction in AI evaluation. Both comparative evalua‐
tion and the post-training alignment process need preference signals, which are
expensive to collect. This motivated the development of preference models: special‐
ized AI judges that predict which response users prefer.
156 | Chapter 3: Evaluation Methodology

While language modeling metrics and hand-designed similarity measurements have
existed for some time, AI as a judge and comparative evaluation have only gained
adoption with the emergence of foundation models. Many teams are figuring out
how to incorporate them into their evaluation pipelines. Figuring out how to build a
reliable evaluation pipeline to evaluate open-ended applications is the topic of the
next chapter.
Summary | 157
