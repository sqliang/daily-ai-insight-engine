---
title: In the Weights is your new AI-centric vanity search
source: https://techcrunch.com/2026/06/20/in-the-weights-is-your-new-ai-centric-vanity-search/
author:
- '[[Anthony Ha]]'
published: '2026-06-20'
created: '2026-06-21'
description: So ... what's your In the Weights score?
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: abec0710ffac301a
source_type: news_media
tldr: In the Weights 推出AI虚荣搜索，衡量个人在LLM参数中的被记忆程度
objective_summary: 前OpenAI员工Thomas Dimson和Joey Flynn创建了In the Weights网站，通过向Grok、Gemini、GPT、Claude、Llama等多个AI模型提问来评估模型对个人的"记忆"强度，并给出分数和排行榜。该工具旨在反映LLM时代信息检索方式的变化。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - OpenAI
  - Global Illumination
  - TechCrunch
  technologies:
  - Grok
  - Gemini
  - GPT-5.4 Mini
  - Claude
  - Llama
  key_people:
  - Thomas Dimson
  - Joey Flynn
  - Macaulay Culkin
  - Luciano Pavarotti
  - Anthony Ha
key_logic_flow:
- Thomas Dimson和Joey Flynn创建了In the Weights网站，用于衡量个人是否被AI模型的训练参数所"记住"。
- 该工具同时查询Grok、Gemini、GPT-5.4 Mini、Claude、Llama等多个AI模型，通过聚类相似描述并分配强度分数来评估记忆程度。
- 结果显示哪些模型返回了哪些答案，并高亮显示模型可能产生的幻觉内容。
- Dimson表示，2026年Google虚荣搜索已不再合适，因为越来越多流量转向了LLM。
- Dimson和Flynn此前通过其设计公司Global Illumination被收购而加入OpenAI，离职后创建了这一项目。
extract_result: success
---

Anyone who’s Googled themselves recently knows that it doesn’t quite hit the way it used to. Sure, there’s everything going on with Google search itself, but there’s also an inescapable feeling that web search isn’t the canonical source of information that it used to be, with just as many people learning about who you and I might be from chatbots.

Thomas Dimson and Joey Flynn had a similar feeling, leading them to create In the Weights. The “weights” in question are the numerical parameters that shape an AI model’s training and output, so the website purports to measure how well “a model is able to recall someone without using tools like web search.”

“Being in the weights means your existence was deemed important in the process of creating superhuman artificial intelligence,” the website says.

To achieve this, In the Weights supposedly queries different models (including Grok, Gemini, multiple versions of GPT, Claude, and Llama, plus lesser known models) with a question similar to, “Who is <name>? Give up to 10 results, each with a short description and confidence.” It then “cluster[s] similar descriptions together and assign[s] a strength score.”

For example, this humble tech blogger received a strength score of 641, placing me in the top 6% of names. I was feeling pretty good until I saw that multiple TechCrunch colleagues scored even higher. And the leaderboard has been shifting as I write this post, with “Home Alone” star Macaulay Culkin currently in the top slot with a strength score of 988, neck-and-neck with opera singer Luciano Pavarotti.

The results also show which models returned which answers for a given name, and they highlight potential hallucinations — apparently GPT-5.4 Mini says that Anthony Ha is an “ambiguous name form that could refer to multiple people with the initials A.H.A.”

Asked why he built In the Weights, Dimson told TechCrunch via email that he and Flynn were looking to “get the creative juices flowing again” after leaving OpenAI (which they both joined through the acquisition of their design startup Global Illumination).

Dimson said he was thinking about how “Google vanity searches are the wrong objective in 2026 as more traffic moves to LLMs” and about the fact that “so many lives are encoded somehow in a bunch of floating point numbers inside the AI brain.” He also said the direction of the site was “sealed” by a tongue-in-cheek blog post riffing on AI weights and Terry Bisson’s classic short story “They’re Made Out of Meat.”

“Reception has been insane so far, we thought this would be a mild curiosity but it seems like it has struck a nerve of wanting to see if you live forever in the super intelligence (the comparison factor doesn’t hurt either!)” Dimson added.