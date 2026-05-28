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
tldr: Google AI Overview因token架构缺陷无法正确拼写单词，连"Google"都拼错，研究人员认为该问题难以根除。
objective_summary: 2026年5月，Google搜索中集成的新版AI Overview再次出现严重拼写错误，无法正确统计单词中的字母数量或拼写单词。Google向TechCrunch承认LLM在单词内计数字母是一个已知挑战，并表示正在修复。AI研究员Matthew
  Guzdial解释了根本原因：LLM基于token而非
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - Google
  - TechCrunch
  - The Onion
  - Reddit
  - University of Alberta
  technologies:
  - LLM
  - Transformer
  - tokenization
  - AI Overview
  - generative AI
  key_people:
  - Matthew Guzdial
key_logic_flow:
- Google在2026年5月将其旗舰搜索引擎全面转向以AI Overview为核心，但新版AI Overview出现基础性拼写错误，例如无法正确计数单词中的字母数量、将"Trump"拼为"t-r-p-u-m"
- 这并非Google首次在AI Overview上出问题——第一版曾引用The Onion和Reddit的讽刺帖文，建议用户吃石头、在披萨上涂胶水
- Google向TechCrunch发表声明承认该问题，称"单词内计数字母是LLM的已知挑战，正在修复此特定问题"
- AI研究员Matthew Guzdial解释了根本技术原因：LLM基于Transformer架构将文字切分为token进行数值编码，模型不知道'T'、'H'、'E'这些单个字母的存在
- 研究人员对能否彻底解决LLM的拼写问题持悲观态度，认为基于token的架构从根本上限制了模型对字母级别的理解能力
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