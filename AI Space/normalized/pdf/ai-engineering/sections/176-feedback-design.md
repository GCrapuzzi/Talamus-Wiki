---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 176
section-title: Feedback Design
source-location: pages 504-513
previous-section: AI Space/normalized/pdf/ai-engineering/sections/175-extracting-conversational-feedback.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/177-feedback-limitations.md
classification: reusable-knowledge-candidate
---
# Feedback Design

8 Not only can you collect feedback about AI applications, you can use AI to analyze feedback, too.
Conversation length.    Another commonly tracked signal is the number of turns per
conversation. Whether this is a positive or negative signal depends on the application.
For AI companions, a long conversation might indicate that the user enjoys the con‐
versation. However, for chatbots geared toward productivity like customer support, a
long conversation might indicate that the bot is inefficient in helping users resolve
their issues.
Dialogue diversity.    Conversation length can also be interpreted together with dialogue
diversity, which can be measured by the distinct token or topic count. For example, if
the conversation is long but the bot keeps repeating a few lines, the user might be
stuck in a loop.
Explicit feedback is easier to interpret, but it demands extra effort from users. Since
many users may not be willing to put in this additional work, explicit feedback can be
sparse, especially in applications with smaller user bases. Explicit feedback also suf‐
fers from response biases. For example, unhappy users might be more likely to com‐
plain, causing the feedback to appear more negative than it is.
Implicit feedback is more abundant—what can be considered implicit feedback is
limited only by your imagination—but it’s noisier. Interpreting implicit signals can
be challenging. For example, sharing a conversation can either be a negative or a pos‐
itive signal. For example, one friend of mine mostly shares conversations when the
model has made some glaring mistakes, and another friend mostly shares useful con‐
versations with their coworkers. It’s important to study your users to understand why
they do each action.
Adding more signals can help clarify the intent. For example, if the user rephrases
their question after sharing a link, it might indicate that the conversation didn’t meet
their expectations. Extracting, interpreting, and leveraging implicit responses from
conversations is a small but growing area of research.8
Feedback Design
If you were unsure of what feedback to collect, I hope that the last section gave you
some ideas.
This section discusses when and how to collect this valuable feedback.
480 | Chapter 10: AI Engineering Architecture and User Feedback

9 I wish there were inpainting for text-to-speech. I find text-to-speech works well 95% of the time, but the other
5% can be frustrating. AI might mispronounce a name or fail to pause during dialogues. I wish there were
apps that let me edit just the mistakes instead of having to regenerate the whole audio.
When to collect feedback
Feedback can and should be collected throughout the user journey. Users should
have the option to give feedback, especially to report errors, whenever this need ari‐
ses. The feedback collection option, however, should be nonintrusive. It shouldn’t
interfere with the user workflow. Here are a few places where user feedback might be
particularly valuable.
In the beginning.    When a user has just signed up, user feedback can help calibrate the
application for the user. For example, a face ID app first must scan your face to work.
A voice assistant might ask you to read a sentence out loud to recognize your voice
for wake words (words that activate a voice assistant, like “Hey Google”). A language
learning app might ask you a few questions to gauge your skill level. For some appli‐
cations, such as face ID, calibration is necessary. For other applications, however, ini‐
tial feedback should be optional, as it creates friction for users to try out your
product. If a user doesn’t specify their preference, you can fall back to a neutral
option and calibrate over time.
When something bad happens.    When the model hallucinates a response, blocks a legit‐
imate request, generates a compromising image, or takes too long to respond, users
should be able to notify you of these failures. You can give users the option to down‐
vote a response, regenerate with the same model, or change to another model. Users
might just give conversational feedback like “You’re wrong”, “Too cliche”, or “I want
something shorter”.
Ideally, when your product makes mistakes, users should still be able to accomplish
their tasks. For example, if the model wrongly categorizes a product, users can edit
the category. Let users collaborate with the AI. If that doesn’t work, let them collabo‐
rate with humans. Many customer support bots offer to transfer users to human
agents if the conversation drags on or if users seem frustrated.
An example of human–AI collaboration is the inpainting functionality for image gen‐
eration.9 If a generated image isn’t exactly what the user needs, they can select a
region of the image and describe with a prompt how to make it better. Figure 10-14
shows an example of inpainting with DALL-E (OpenAI, 2021). This feature allows
users to get better results while giving developers high-quality feedback.
User Feedback | 481

Figure 10-14. An example of how inpainting works in DALL-E. Image by OpenAI.
482 | Chapter 10: AI Engineering Architecture and User Feedback

[Visual content extracted via GLM-OCR]

Figure 10-14. An example of how inpainting works in DALL-E. Image by OpenAI.

10 When I ask this question at events I speak at, the responses are conflicted. Some people think showing full
responses gives more reliable feedback because it gives users more information to make a decision. At the
same time, some people think that once users have read full responses, there’s no incentive for them to click
on the better one.
When the model has low confidence.    When a model is uncertain about an action, you
can ask the user for feedback to increase its confidence. For example, given a request
to summarize a paper, if the model is uncertain whether the user would prefer a
short, high-level summary or a detailed section-by-section summary, the model can
output both summaries side by side, assuming that generating two summaries
doesn’t increase the latency for the user. The user can choose which one they prefer.
Comparative signals like this can be used for preference finetuning. An example of
comparative evaluation in production is shown in Figure 10-15.
Figure 10-15. Side-by-side comparison of two ChatGPT responses.
Showing two full responses for the user to choose means asking that user for explicit
feedback. Users might not have time to read two full responses or care enough to give
thoughtful feedback. This can result in noisy votes. Some applications, like Google
Gemini, show only the beginning of each response, as shown in Figure 10-16. Users
can click to expand the response they want to read. It’s unclear, however, whether
showing full or partial responses side by side gives more reliable feedback.10
User Feedback | 483

[Visual content extracted via GLM-OCR]

When the model has low confidence. When a model is uncertain about an action, you can ask the user for feedback to increase its confidence. For example, given a request to summarize a paper, if the model is uncertain whether the user would prefer a short, high-level summary or a detailed section-by-section summary, the model can output both summaries side by side, assuming that generating two summaries doesn’t increase the latency for the user. The user can choose which one they prefer. Comparative signals like this can be used for preference finetuning. An example of comparative evaluation in production is shown in Figure 10-15.

Figure 10-15. Side-by-side comparison of two ChatGPT responses.

Showing two full responses for the user to choose means asking that user for explicit feedback. Users might not have time to read two full responses or care enough to give thoughtful feedback. This can result in noisy votes. Some applications, like Google Gemini, show only the beginning of each response, as shown in Figure 10-16. Users can click to expand the response they want to read. It’s unclear, however, whether showing full or partial responses side by side gives more reliable feedback.

10 When I ask this question at events I speak at, the responses are conflicted. Some people think showing full responses gives more reliable feedback because it gives users more information to make a decision. At the same time, some people think that once users have read full responses, there’s no incentive for them to click on the better one.

Figure 10-16. Google Gemini shows partial responses side by side for comparative feed‐
back. Users have to click on the response they want to read more about, which gives
feedback about which response they find more promising.
Another example is a photo organization application that automatically tags your
photos, so that it can respond to queries like “Show me all the photos of X”. When
unsure if two people are the same, it can ask you for feedback, as Google Photos does
in Figure 10-17.
Figure 10-17. Google Photos asks for user feedback when unsure. The two cat images
were generated by ChatGPT.
You might wonder: how about feedback when something good happens? Actions
that users can take to express their satisfaction include thumbs up, favoriting, or
sharing. However, Apple’s human interface guideline  warns against asking for both
positive and negative feedback. Your application should produce good results by
default. Asking for feedback on good results might give users the impression that
good results are exceptions. Ultimately, if users are happy, they continue using your
application.
484 | Chapter 10: AI Engineering Architecture and User Feedback

[Visual content extracted via GLM-OCR]

Figure 10-16. Google Gemini shows partial responses side by side for comparative feedback. Users have to click on the response they want to read more about, which gives feedback about which response they find more promising.

Another example is a photo organization application that automatically tags your photos, so that it can respond to queries like “Show me all the photos of X”. When unsure if two people are the same, it can ask you for feedback, as Google Photos does in Figure 10-17.

Figure 10-17. Google Photos asks for user feedback when unsure. The two cat images were generated by ChatGPT.

You might wonder: how about feedback when something good happens? Actions that users can take to express their satisfaction include thumbs up, favoriting, or sharing. However, Apple’s human interface guideline warns against asking for both positive and negative feedback. Your application should produce good results by default. Asking for feedback on good results might give users the impression that good results are exceptions. Ultimately, if users are happy, they continue using your application.

However, many people I’ve talked to believe users should have the option to give
feedback when they encounter something amazing. A product manager for a popular
AI-powered product mentioned that their team needs positive feedback because it
reveals the features users love enough to give enthusiastic feedback about. This allows
the team to concentrate on refining a small set of high-impact features rather than
spreading resources across many with minimal added value.
Some avoid asking for positive feedback out of concern it may clutter the interface or
annoy users. However, this risk can be managed by limiting the frequency of feed‐
back requests. For example, if you have a large user base, showing the request to only
1% of users at a time could help gather sufficient feedback without disrupting the
experience for most users. Keep in mind that the smaller the percentage of users
asked, the greater the risk of feedback biases. Still, with a large enough pool, the feed‐
back can provide meaningful product insights.
How to collect feedback
Feedback should seamlessly integrate into the user’s workflow. It should be easy for
users to provide feedback without extra work. Feedback collection shouldn’t disrupt
user experience and should be easy to ignore. There should be incentives for users to
give good feedback.
One example often cited as good feedback design is from the image generator app
Midjourney. For each prompt, Midjourney generates a set of (four) images and gives
the user the following options, as shown in Figure 10-18:
1. Generate an unscaled version of any of these images.
2. Generate variations for any of these images.
3. Regenerate.
All these options give Midjourney different signals. Options 1 and 2 tell Midjourney
which of the four photos is considered by the user to be the most promising. Option
1 gives the strongest positive signal about the chosen photo. Option 2 gives a weaker
positive signal. Option 3 signals that none of the photos is good enough. However,
users might choose to regenerate even if the existing photos are good just to see what
else is possible.
User Feedback | 485

A close up picture of a grinning, winking llama in police uniform in Zootopia style that makes you want to go on an adventure with – @chiphuyen (fast)

Figure 10-18. Midjourney’s workflow allows the app to collect implicit feedback.

Code assistants like GitHub Copilot might show their drafts in lighter colors than the final texts, as shown in Figure 10-19. Users can use the Tab key to accept a suggestion or simply continue typing to ignore the suggestion, both providing feedback.

Figure 10-19. GitHub Copilot makes it easy to both suggest and reject a suggestion.

One of the biggest challenges of standalone AI applications like ChatGPT and Claude
is that they aren’t integrated into the user’s daily workflow, making it hard to collect
high-quality feedback the way integrated products like GitHub Copilot can. For
example, if Gmail suggests an email draft, Gmail can track how this draft is used or
edited. However, if you use ChatGPT to write an email, ChatGPT doesn’t know
whether the generated email is actually sent.
The feedback alone might be helpful for product analytics. For example, seeing just
the thumbs up/thumbs down information is useful for calculating how often people
are happy or unhappy with your product. For deeper analysis, though, you would
need context around the feedback, such as the previous 5 to 10 dialogue turns. This
context can help you figure out what went wrong. However, getting this context
might not be possible without explicit user consent, especially if the context might
contain personally identifiable information.
For this reason, some products include terms in their service agreements that allow
them to access user data for analytics and product improvement. For applications
without such terms, user feedback might be tied to a user data donation flow, where
users are asked to donate (e.g., share) their recent interaction data along with their
feedback. For example, when submitting feedback, you might be asked to check a box
to share your recent data as context for this feedback.
Explaining to users how their feedback is used can motivate them to give more and
better feedback. Do you use a user’s feedback to personalize the product to this user,
to collect statistics about general usage, or to train a new model? If users are con‐
cerned about privacy, reassure them that their data won’t be used to train models or
won’t leave their device (only if these are true).
Don’t ask users to do the impossible. For example, if you collect comparative signals
from users, don’t ask them to choose between two options they don’t understand. For
example, I was once stumped when ChatGPT asked me to choose between two possi‐
ble answers to a statistical question, as shown in Figure 10-20 . I wish there was an
option for me to say, “I don’t know”.
User Feedback | 487

Figure 10-20. An example of ChatGPT asking a user to select the response the user pre‐
fers. However, for mathematical questions like this, the right answer shouldn’t be a
matter of preference.
Add icons and tooltips to an option if they help people understand it. Avoid a design
that can confuse users. Ambiguous instructions can lead to noisy feedback. I once
hosted a GPU optimization workshop, using Luma to collect feedback. When I was
reading the negative feedback, I was confused. Even though the responses were posi‐
tive, the star ratings were 1/5. When I dug deeper, I realized that Luma used emojis to
represent numbers in their feedback collection form, but the angry emoji, corre‐
sponding to a one-star rating, was put where the five-star rating should be, as shown
in Figure 10-21.
Be mindful of whether you want users’ feedback to be private or public. For example,
if a user likes something, do you want this information shown to other users? In its
early days, Midjourney’s feedback—someone choosing to upscale an image, generate
variations, or regenerate another batch of images—was public.
488 | Chapter 10: AI Engineering Architecture and User Feedback

[Visual content extracted via GLM-OCR]

Add icons and tooltips to an option if they help people understand it. Avoid a design that can confuse users. Ambiguous instructions can lead to noisy feedback. I once hosted a GPU optimization workshop, using Luma to collect feedback. When I was reading the negative feedback, I was confused. Even though the responses were positive, the star ratings were 1/5. When I dug deeper, I realized that Luma used emojis to represent numbers in their feedback collection form, but the angry emoji, corresponding to a one-star rating, was put where the five-star rating should be, as shown in Figure 10-21.

Be mindful of whether you want users’ feedback to be private or public. For example, if a user likes something, do you want this information shown to other users? In its early days, Midjourney’s feedback—someone choosing to upscale an image, generate variations, or regenerate another batch of images—was public.

11 See “Ted Cruz Blames Staffer for ‘Liking’ Porn Tweet”  (Nelson and Everett, POLITICO, September 2017) and
“Kentucky Senator Whose Twitter Account ‘Liked’ Obscene Tweets Says He Was Hacked”  (Liam Niemeyer,
WKU Public Radio, March 2023).
Figure 10-21. Because Luma put the angry emoji, corresponding to a one-star rating,
where a five-star rating should’ve been, some users mistakenly picked it for positive
reviews.
The visibility of a signal can profoundly impact user behavior, user experience, and
the quality of the feedback. Users tend to be more candid in private—there’s a lower
chance of their activities being judged 11—which can result in higher-quality signals.
In 2024, X (formerly Twitter) made “likes” private. Elon Musk, the owner of X,
claimed a significant uptick in the number of likes after this change.
However, private signals can reduce discoverability and explainability. For example,
hiding likes prevents users from finding tweets their connections have liked. If X rec‐
ommends tweets based on the likes of the people you follow, hiding likes could result
in users’ confusion about why certain tweets appear in their feeds.
User Feedback | 489

[Visual content extracted via GLM-OCR]

The visibility of a signal can profoundly impact user behavior, user experience, and the quality of the feedback. Users tend to be more candid in private—there’s a lower chance of their activities being judged$^{11}$—which can result in higher-quality signals. In 2024, X (formerly Twitter) made “likes” private. Elon Musk, the owner of X, claimed a significant uptick in the number of likes after this change.

However, private signals can reduce discoverability and explainability. For example, hiding likes prevents users from finding tweets their connections have liked. If X recommends tweets based on the likes of the people you follow, hiding likes could result in users’ confusion about why certain tweets appear in their feeds.

11 See “Ted Cruz Blames Staffer for ‘Liking’ Porn Tweet” (Nelson and Everett, POLITICO, September 2017) and “Kentucky Senator Whose Twitter Account ‘Liked’ Obscene Tweets Says He Was Hacked” (Liam Niemeyer, WKU Public Radio, March 2023).
