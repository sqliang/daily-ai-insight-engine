---
title: Why Google’s AI can’t spell Google (or anything else)
source: https://techcrunch.com/2026/05/27/why-googles-ai-cant-spell-google-or-anything-else/
author:
- '[[Amanda Silberling]]'
published: '2026-05-28'
created: '2026-05-28'
description: Google is embarrassing itself, again.
tags:
- clippings
extraction_status: success
pipeline_stage: ingested
id: 5e8c5bd85baeaf02
---

How many Ps are in Google? According to Google, there are two.

There’s also is also “exactly 1 ‘r’ in the word ‘poop’,” Google’s AI Overview says, as well as two ‘d’s in the word journalism, yet spelled it: j-o-u-r-n-a-d-i-s-m. Google did at least identify that there is one P in the last name of the U.S. president, but spelled it as t-r-p-u-m.

You didn’t need to be a prophet to predict that Google’s AI-forward Search overhaul was going to go over poorly. We’ve done this before. The first time Google added AI Overviews to Search, the feature ended up citing satirical posts from The Onion and Reddit, advising people to eat rocks and put glue on their pizza.

This time around, as Google doubles down on its commitment to make generative AI the centerpiece of its 29-year-old flagship product, it’s not surprising to see it stumble.

“Counting within words has been a known challenge for LLMs, and we’re working to fix this particular issue,” Google told TechCrunch in an emailed statement.

These basic spelling errors may seem familiar. LLMs, the kind of artificial intelligence that powers chatbots and other text-generators, are not built to understand spelling. It’s been a running joke for years that whenever a company unveils a new AI model, you should ask it how many ‘r’s are in the word strawberry. These AI models — which can code an app in seconds, or solve problems that have stumped mathematicians for decades — are about as good as a kindergartener at spelling.

Google’s AI overview woes reach beyond silly spelling mistakes though. Google already patched an issue from last week in which searching the word “disregard” would yield what looked like a dictionary definition of the word, only the definition was shown as, “Understood. Let me know whenever you have a new prompt or question!” But these spelling errors have remained amusing because they’re so difficult to quash.

As researchers have previously explained when we’ve asked about these spelling conundrums, AI doesn’t perceive sentences as units of language made up of words and letters. Many LLMs are built on transformers models, which break down text into tokens, which can be full words, syllables, or letters, depending on the model. Instead of “reading” like a human would, the AI converts the text into numerical representations of itself, which are then contextualized to help the AI come up with a logical response.

“LLMs are based on this transformer architecture, which notably is not actually reading text. What happens when you input a prompt is that it’s translated into an encoding,” Matthew Guzdial, an AI researcher and assistant professor at the University of Alberta, told TechCrunch. “When it sees the word ‘the,’ it has this one encoding of what ‘the’ means, but it does not know about ‘T,’ ‘H,’ ‘E.’”

The token-based architecture that powers LLMs like Google’s AI overview is inherently limiting, and researchers haven’t been optimistic that they can solve the spelling problem.