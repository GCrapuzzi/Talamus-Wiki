---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 175
section-title: Extracting Conversational Feedback
source-location: pages 499-503
previous-section: AI Space/normalized/pdf/ai-engineering/sections/174-user-feedback.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/176-feedback-design.md
classification: reusable-knowledge-candidate
---
# Extracting Conversational Feedback

It’s important to remember that user feedback is user data. Leveraging user feedback
requires the same cautions needed when leveraging any data. User privacy should be
respected. Users have the right to know how their data is being used.
Extracting Conversational Feedback
Traditionally, feedback can be explicit or implicit . Explicit feedback is information
users provide in response to explicit requests for feedback in the application, such as
thumbs up/thumbs down, upvote/downvote, star rating, or a yes/no answer to the
question “Did we solve your problem?” Explicit feedback is fairly standard across
applications—there are only so many ways you can ask a person if they like some‐
thing. Therefore, explicit feedback is better understood.
Implicit feedback is information inferred from user actions. For example, if someone
buys a product recommended to them, it means it was a good recommendation.
What can be considered implicit feedback depends on what actions a user can do
within each application and is, therefore, highly application-dependent. Foundation
models enable a new world of applications and, with them, many genres of implicit
feedback.
The conversational interface that many AI applications use makes it easier for users
to give feedback. Users can encourage good behaviors and correct errors the same
way they would give feedback in daily dialogues. The language that a user uses to give
directions to AI can convey feedback about both the application’s performance  and
the user’s preference .
As an example, imagine you’re using an AI assistant to help you plan your trip to
Australia. You ask the AI to find a hotel for three nights in Sydney. It responds with
three recommendations as follows:
Here are three hotel suggestions in Sydney for a 3-night stay:
1. Historic Rocks Boutique Hotel (The Rocks)
• Price: ~$400/night
• Neighborhood: Charming streets and close to iconic sights.
2. Stylish Surry Hills House Hotel (Surry Hills)
• Price: ~$200/night
• Neighborhood: Trendy, with vibrant cafes and art galleries.
3. Chill Bondi Beachside Hotel (Bondi Beach)
• Price: ~$300/night
• Neighborhood: Beachside, ideal for relaxation and city exploration.
User Feedback | 475

How you respond to these three recommendations reveals your preference. For
example, if you respond with “Yes book me the one close to galleries”, you show an
interest in art. On the other hand, the response “Is there nothing under $200?”
reveals a price-conscious preference and suggests that the assistant doesn’t quite get
you yet.
User feedback, extracted from conversations, can be used for evaluation, develop‐
ment, and personalization:
• Evaluation: derive metrics to monitor the application
• Development: train the future models or guide their development
• Personalization: personalize the application to each user
Implicit conversational feedback can be inferred from both the content of user mes‐
sages and their patterns of communication. Because feedback is blended into daily
conversations, it’s also challenging to extract. While intuition about conversational
cues can help you devise an initial set of signals to look for, rigorous data analysis and
user studies are necessary to understand.
While conversational feedback has enjoyed greater attention thanks to the popularity
of conversational bots, it had been an active research area for several years before
ChatGPT came out. The reinforcement learning community has been trying to get
RL algorithms to learn from natural language feedback since the late 2010s, many of
them with promising results; see Fu et al. (2019); Goyal et al. (2019); Zhou and Small
(2020); and Sumers et al. (2020) ). Natural language feedback is also of great interest
for early conversational AI applications such as Amazon Alexa ( Ponnusamy et al.,
2019; Park et al., 2020), Spotify’s voice control feature ( Xiao et al., 2021), and Yahoo!
Voice (Hashimoto and Sassano, 2018).
Natural language feedback
Feedback extracted from the content of messages is called natural language feedback.
Here are a couple of natural language feedback signals that tell you how a conversa‐
tion is going. It’s useful to track these signals in production to monitor your applica‐
tion’s performance.
Early termination.    If a user terminates a response early, e.g., stopping a response gen‐
eration halfway, exiting the app (for web and mobile apps), telling the model to stop
(for voice assistants), or simply leaving the agent hanging (e.g., not responding to the
agent with which option you want it to go ahead with), it’s likely that the conversa‐
tion isn’t going well.
476 | Chapter 10: AI Engineering Architecture and User Feedback

Error correction.    If a user starts their follow-up with “No, …” or “I meant, …”, the
model’s response is likely off the mark.
To correct errors, users might try to rephrase their requests. Figure 10-12 shows an
example of a user’s attempt to correct the model’s misunderstanding. Rephrase
attempts can be detected using heuristics or ML models.
Figure 10-12. Because the user both terminates the generation early and rephrases the
question, it can be inferred that the model misunderstood the intent of the original
request.
Users can also point out specific things the model should’ve done differently. For
example, if a user asks the model to summarize a story and the model confuses a
character, this user can give feedback such as: “Bill is the suspect, not the victim.” The
model should be able to take this feedback and revise the summary.
This kind of action-correcting feedback is especially common for agentic use cases
where users might nudge the agent toward more optional actions. For example, if a
user assigns the agent the task of doing market analysis about company XYZ, this
user might give feedback such as “You should also check XYZ GitHub page” or
“Check the CEO’s X profile”.
Sometimes, users might want the model to correct itself by asking for explicit confir‐
mation, such as “Are you sure?”, “Check again”, or “Show me the sources”. This
doesn’t necessarily mean that the model gives wrong answers. However, it might
User Feedback | 477

[Visual content extracted via GLM-OCR]

Error correction. If a user starts their follow-up with “No, …” or “I meant, …”, the model’s response is likely off the mark.

To correct errors, users might try to rephrase their requests. Figure 10-12 shows an example of a user’s attempt to correct the model’s misunderstanding. Rephrase attempts can be detected using heuristics or ML models.

Figure 10-12. Because the user both terminates the generation early and rephrases the question, it can be inferred that the model misunderstood the intent of the original request.

Users can also point out specific things the model should’ve done differently. For example, if a user asks the model to summarize a story and the model confuses a character, this user can give feedback such as: “Bill is the suspect, not the victim.” The model should be able to take this feedback and revise the summary.

This kind of action-correcting feedback is especially common for agentic use cases where users might nudge the agent toward more optional actions. For example, if a user assigns the agent the task of doing market analysis about company XYZ, this user might give feedback such as “You should also check XYZ GitHub page” or “Check the CEO’s X profile”.

Sometimes, users might want the model to correct itself by asking for explicit confirmation, such as “Are you sure?”, “Check again”, or “Show me the sources”. This doesn’t necessarily mean that the model gives wrong answers. However, it might

mean that your model’s answers lack the details the user is looking for. It can also
indicate general distrust in your model.
Some applications let users edit the model’s responses directly. For example, if a user
asks the model to generate code, and the user corrects the generated code, it’s a very
strong signal that the code that got edited isn’t quite right.
User edits also serve as a valuable source of preference data. Recall that preference
data, typically in the format of (query, winning response, losing response), can be
used to align a model to human preference. Each user edit makes up a preference
example, with the original generated response being the losing response and the
edited response being the winning response.
Complaints.    Often, users just complain about your application’s outputs without try‐
ing to correct them. For example, they might complain that an answer is wrong, irrel‐
evant, toxic, lengthy, lacking detail, or just bad. Table 10-1  shows eight groups of
natural language feedback resulting from automatic clustering the FITS (Feedback
for Interactive Talk & Search) dataset (Xu et al., 2022).
Table 10-1. Feedback types derived from automatic clustering the FITS dataset (Xu et al.,
2022). Results from Yuan et al. (2023).
Group Feedback type Num. %
1 Clarify their demand again. 3702 26.54%
2 Complain that the bot (1) does not answer the question or (2) gives irrelevant information or (3)
asks the user to find out the answer on their own.
2260 16.20%
3 Point out specific search results that can answer the question. 2255 16.17%
4 Suggest that the bot should use the search results. 2130 15.27%
5 State that the answer is (1) factually incorrect, or (2) not grounded in the search results. 1572 11.27%
6 Point out that the bot’s answer is not specific/accurate/complete/detailed. 1309 9.39%
7 Point out that the bot is not confident in its answers and always begins its responses with “I am
not sure” or “I don’t know”.
582 4.17%
8 Complain about repetition/rudeness in bot responses. 137 0.99%
Understanding how the bot fails the user is crucial in making it better. For example, if
you know that the user doesn’t like verbose answers, you can change the bot’s prompt
to make it more concise. If the user is unhappy because the answer lacks details, you
can prompt the bot to be more specific.
Sentiment.    Complaints can also be general expressions of negative sentiments (frus‐
tration, disappointment, ridicule, etc.) without explaining the reason why, such as
“Uggh”. This might sound dystopian, but analysis of a user’s sentiments throughout
conversations with a bot might give you insights into how the bot is doing. Some call
centers track users’ voices throughout the calls. If a user gets increasingly loud,
478 | Chapter 10: AI Engineering Architecture and User Feedback

something is wrong. Conversely, if someone starts a conversation angry but ends
happily, the conversation might have resolved their issue.
Natural language feedback can also be inferred from the model’s responses. One
important signal is the model’s refusal rate. If a model says things like “Sorry, I don’t
know that one” or “As a language model, I can’t do …”, the user is probably
unhappy.
Other conversational feedback
Other types of conversational feedback can be derived from user actions instead of
messages.
Regeneration.    Many applications let users generate another response, sometimes
with a different model. If a user chooses regeneration, it might be because they’re not
satisfied with the first response. However, it might also be that the first response is
adequate, but the user wants options to compare. This is especially common with cre‐
ative requests like image or story generation.
Regeneration signals might also be stronger for applications with usage-based billing
than those with subscriptions. With usage-based billing, users are less likely to regen‐
erate and spend extra money out of idle curiosity.
Personally, I often choose regeneration for complex requests to ensure the model’s
responses are consistent. If two responses give contradicting answers, I can’t trust
either.
After regeneration, some applications might explicitly ask to compare the new
response with the previous one, as shown in Figure 10-13. This better or worse data,
again, can be used for preference finetuning.
Figure 10-13. ChatGPT asks for comparative feedback when a user regenerates another
response.
Conversation organization.    The actions a user takes to organize their conversations—
such as delete, rename, share, and bookmark—can also be signals. Deleting a conver‐
sation is a pretty strong signal that the conversation is bad, unless it’s an embarrass‐
ing conversation and the user wants to remove its trace. Renaming a conversation
suggests that the conversation is good, but the auto-generated title is bad.
User Feedback | 479

[Visual content extracted via GLM-OCR]

something is wrong. Conversely, if someone starts a conversation angry but ends happily, the conversation might have resolved their issue.

Natural language feedback can also be inferred from the model’s responses. One important signal is the model’s refusal rate. If a model says things like “Sorry, I don’t know that one” or “As a language model, I can’t do …”, the user is probably unhappy.

Other conversational feedback

Other types of conversational feedback can be derived from user actions instead of messages.

Regeneration. Many applications let users generate another response, sometimes with a different model. If a user chooses regeneration, it might be because they’re not satisfied with the first response. However, it might also be that the first response is adequate, but the user wants options to compare. This is especially common with creative requests like image or story generation.

Regeneration signals might also be stronger for applications with usage-based billing than those with subscriptions. With usage-based billing, users are less likely to regenerate and spend extra money out of idle curiosity.

Personally, I often choose regeneration for complex requests to ensure the model’s responses are consistent. If two responses give contradicting answers, I can’t trust either.

After regeneration, some applications might explicitly ask to compare the new response with the previous one, as shown in Figure 10-13. This better or worse data, again, can be used for preference finetuning.

Figure 10-13. ChatGPT asks for comparative feedback when a user regenerates another response.

Conversation organization. The actions a user takes to organize their conversations—such as delete, rename, share, and bookmark—can also be signals. Deleting a conversation is a pretty strong signal that the conversation is bad, unless it’s an embarrassing conversation and the user wants to remove its trace. Renaming a conversation suggests that the conversation is good, but the auto-generated title is bad.
