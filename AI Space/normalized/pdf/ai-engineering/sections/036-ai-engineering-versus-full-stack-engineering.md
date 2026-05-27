---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 036
section-title: AI Engineering Versus Full-Stack Engineering
source-location: pages 70-70
previous-section: AI Space/normalized/pdf/ai-engineering/sections/035-ai-engineering-versus-ml-engineering.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/037-summary.md
classification: reusable-knowledge-candidate
---
# AI Engineering Versus Full-Stack Engineering

26 Streamlit, Gradio, and Plotly Dash are common tools for building AI web apps.
27 Anton Bacaj told me that “AI engineering is just software engineering with AI models thrown in the stack.”
There need to be tools that provide interfaces for standalone AI applications or make
it easy to integrate AI into existing products. Here are just some of the interfaces that
are gaining popularity for AI applications:
• Standalone web, desktop, and mobile apps.26
• Browser extensions that let users quickly query AI models while browsing.
• Chatbots integrated into chat apps like Slack, Discord, WeChat, and WhatsApp.
• Many products, including VSCode, Shopify, and Microsoft 365, provide APIs
that let developers integrate AI into their products as plug-ins and add-ons.
These APIs can also be used by AI agents to interact with the world, as discussed
in Chapter 6.
While the chat interface is the most commonly used, AI interfaces can also be voicebased (such as with voice assistants) or embodied (such as in augmented and virtual
reality).
These new AI interfaces also mean new ways to collect and extract user feedback. The
conversation interface makes it so much easier for users to give feedback in natural
language, but this feedback is harder to extract. User feedback design is discussed in
Chapter 10.
A summary of how the importance of different categories of app development
changes with AI engineering is shown in Table 1-6.
Table 1-6. The importance of different categories in app development for AI engineering
and ML engineering.
Category Building with traditional ML Building with foundation models
AI interface Less important Important
Prompt engineering Not applicable Important
Evaluation Important More important
AI Engineering Versus Full-Stack Engineering
The increased emphasis on application development, especially on interfaces, brings
AI engineering closer to full-stack development. 27 The rising importance of interfaces
leads to a shift in the design of AI toolings to attract more frontend engineers. Tradi‐
tionally, ML engineering is Python-centric. Before foundation models, the most
popular ML frameworks supported mostly Python APIs. Today, Python is still popu‐
46 | Chapter 1: Introduction to Building AI Applications with Foundation Models
