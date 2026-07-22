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
pipeline_stage: fact_extracted
id: 5e8c5bd85baeaf02
source_type: news_media
tldr: 谷歌AI Overview在搜索中频繁出现拼写错误，例如无法正确回答单词中字母数量的问题。根源在于LLM基于Transformer架构，将文本分解为token而非字母，不具备人类式的拼写理解能力。谷歌承认该问题并表示正在修复。
objective_summary: 2026年5月，谷歌AI Overview在Search中多次出现基础拼写错误，包括无法准确计算单词中的字母数量。谷歌向TechCrunch发表声明承认LLM在单词内计数方面存在已知挑战，并表示正在修复。阿尔伯塔大学AI研究员Matthew
  Guzdial解释称，基于Transformer架构的LLM并不实际阅读文本，而是将输入转换为编码，因此无法感知单个字母的存在。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - Google
  - TechCrunch
  - University of Alberta
  technologies:
  - LLM
  - Transformer
  - AI Overview
  key_people:
  - Matthew Guzdial
key_logic_flow:
- 谷歌AI Overview在搜索结果中出现多处拼写错误，包括无法正确回答单词中有多少个字母等简单问题。
- 这并非谷歌AI Overview首次出现问题，此前该功能曾引用讽刺网站内容，建议用户吃石头和在披萨上涂胶水。
- 谷歌向TechCrunch发表声明，承认LLM在单词内计数方面存在已知挑战，并表示正在修复这一问题。
- 阿尔伯塔大学AI研究员Matthew Guzdial解释称，LLM基于Transformer架构，并不实际阅读文本，而是将输入转换为数值编码。
- LLM将文本分解为token（可以是完整单词、音节或字母），而非像人类一样将句子理解为由字母组成的语言单位。
- 研究人员对能否从根本上解决LLM的拼写问题持悲观态度，认为基于token的架构存在固有限制。
extract_result: success
object_mentions:
- object_type: product
  name: AI Overviews
  canonical_name: Google AI Overviews
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 谷歌AI Overview在搜索中频繁出现基础拼写错误，例如无法正确计算单词中字母的数量。
  - 谷歌在发给TechCrunch的声明中承认LLM在单词内计数方面存在已知挑战，并表示正在修复。
  - AI Overview此前就曾因引用讽刺网站内容建议用户吃石头和涂胶水而引发争议。
  article_id: 5e8c5bd85baeaf02
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