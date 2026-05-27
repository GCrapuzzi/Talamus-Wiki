---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 165
section-title: Chapter 10. AI Engineering Architecture and User Feedback
source-location: pages 473-473
previous-section: AI Space/normalized/pdf/ai-engineering/sections/164-summary.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/166-ai-engineering-architecture.md
classification: reusable-knowledge-candidate
---
# Chapter 10. AI Engineering Architecture and User Feedback

CHAPTER 10
AI Engineering Architecture
and User Feedback
So far, this book has covered a wide range of techniques to adapt foundation models
to specific applications. This chapter will discuss how to bring these techniques
together to build successful products.
Given the wide range of AI engineering techniques and tools available, selecting the
right ones can feel overwhelming. To simplify this process, this chapter takes a grad‐
ual approach. It starts with the simplest architecture for a foundation model applica‐
tion, highlights the challenges of that architecture, and gradually adds components to
address them.
We can spend eternity reasoning about how to build a successful application, but the
only way to find out if an application actually achieves its goal is to put it in front of
users. User feedback has always been invaluable for guiding product development,
but for AI applications, user feedback has an even more crucial role as a data source
for improving models. The conversational interface makes it easier for users to give
feedback but harder for developers to extract signals. This chapter will discuss differ‐
ent types of conversational AI feedback and how to design a system to collect the
right feedback without hurting user experience.
AI Engineering Architecture
A full-fledged AI architecture can be complex. This section follows the process that a
team might follow in production, starting with the simplest architecture and progres‐
sively adding more components. Despite the diversity of AI applications, they share
many common components. The architecture proposed here has been validated at
