---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 104
section-title: Defensive Prompt Engineering
source-location: pages 259-259
previous-section: AI Space/normalized/pdf/ai-engineering/sections/103-organize-and-version-prompts.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/105-proprietary-prompts-and-reverse-prompt-engineering.md
classification: reusable-knowledge-candidate
---
# Defensive Prompt Engineering

12 Outputs that can cause brand risks and misinformation are discussed briefly in Chapter 4.
13 One such remote code execution risk was found in LangChain in 2023. See GitHub issues: 814 and 1026.
will be automatically forced to update to this new prompt. In other words, if you ver‐
sion your prompts together with your code in git, it’s very challenging for a team to
choose to stay with an older version of a prompt for their application.
Many teams use a separate prompt catalog  that explicitly versions each prompt so
that different applications can use different prompt versions. A prompt catalog
should also provide each prompt with relevant metadata and allow prompt search. A
well-implemented prompt catalog might even keep track of the applications that
depend on a prompt and notify the application owners of newer versions of that
prompt.
Defensive Prompt Engineering
Once your application is made available, it can be used by both intended users and
malicious attackers who may try to exploit it. There are three main types of prompt
attacks that, as application developers, you want to defend against:
Prompt extraction
Extracting the application’s prompt, including the system prompt, either to repli‐
cate or exploit the application
Jailbreaking and prompt injection
Getting the model to do bad things
Information extraction
Getting the model to reveal its training data or information used in its context
Prompt attacks pose multiple risks for applications; some are more devastating than
others. Here are just a few of them:12
Remote code or tool execution
For applications with access to powerful tools, bad actors can invoke unauthor‐
ized code or tool execution. Imagine if someone finds a way to get your system to
execute an SQL query that reveals all your users’ sensitive data or sends unau‐
thorized emails to your customers. As another example, let’s say you use AI to
help you run a research experiment, which involves generating experiment code
and executing that code on your computer. An attacker can find ways to get the
model to generate malicious code to compromise your system.13
Data leaks
Bad actors can extract private information about your system and your users.
Defensive Prompt Engineering | 235
