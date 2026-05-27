---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 055
section-title: Chapter 3. Evaluation Methodology
source-location: pages 137-137
previous-section: AI Space/normalized/pdf/ai-engineering/sections/054-summary.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/056-challenges-of-evaluating-foundation-models.md
classification: reusable-knowledge-candidate
---
# Chapter 3. Evaluation Methodology

1 In December 2023, Greg Brockman, an OpenAI cofounder, tweeted that “evals are surprisingly often all you
need.”
CHAPTER 3
Evaluation Methodology
The more AI is used, the more opportunity there is for catastrophic failure. We’ve
already seen many failures in the short time that foundation models have been
around. A man committed suicide after being encouraged by a chatbot. Lawyers sub‐
mitted false evidence hallucinated by AI . Air Canada was ordered to pay damages
when its AI chatbot gave a passenger false information. Without a way to quality con‐
trol AI outputs, the risk of AI might outweigh its benefits for many applications.
As teams rush to adopt AI, many quickly realize that the biggest hurdle to bringing
AI applications to reality is evaluation. For some applications, figuring out evaluation
can take up the majority of the development effort.1
Due to the importance and complexity of evaluation, this book has two chapters on
it. This chapter covers different evaluation methods used to evaluate open-ended
models, how these methods work, and their limitations. The next chapter focuses on
how to use these methods to select models for your application and build an evalua‐
tion pipeline to evaluate your application.
While I discuss evaluation in its own chapters, evaluation has to be considered in the
context of a whole system, not in isolation. Evaluation aims to mitigate risks and
uncover opportunities. To mitigate risks, you first need to identify the places where
your system is likely to fail and design your evaluation around them. Often, this may
require redesigning your system to enhance visibility into its failures. Without a clear
understanding of where your system fails, no amount of evaluation metrics or tools
can make the system robust.
