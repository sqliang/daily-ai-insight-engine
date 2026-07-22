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
tldr: Thomas Dimson 和 Joey Flynn 创办了 AI 虚荣搜索工具 In the Weights，通过查询多个大语言模型来评估一个人被 AI
  记忆的强度分数，上线后反响远超预期。
objective_summary: 前 OpenAI 员工 Thomas Dimson 和 Joey Flynn 创建了 In the Weights 网站，该工具通过向
  Grok、Gemini、GPT、Claude、Llama 等多个 AI 模型询问特定姓名并聚类回答，为每个人生成一个强度分数。网站旨在衡量离开网络搜索后 AI
  模型对某人的记忆程度，上线后因满足了人们对比自己在 AI 中'权重'的好奇心而获得大量关注。
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
  - GPT
  - Claude
  - Llama
  key_people:
  - Thomas Dimson
  - Joey Flynn
  - Macauley Culkin
key_logic_flow:
- Thomas Dimson 和 Joey Flynn 在离开 OpenAI 后创建了 AI 虚荣搜索工具 In the Weights。
- 该网站通过向 Grok、Gemini、GPT、Claude、Llama 等多个 AI 模型提问'<名字>是谁'来获取回答。
- 系统将不同模型的相似回答聚类并为每个人分配一个强度分数，旨在衡量模型不借助网络搜索时对某人的记忆程度。
- 例如作者获得了 641 分（前 6%），而 Macaulay Culkin 以 988 分位居榜首，与歌唱家 Luciano Pavarotti 并列。
- 结果还会显示哪些模型返回了哪些回答，并标记潜在的幻觉内容，例如 GPT-5.4 Mini 将作者标记为'模糊的名字'。
- Dimson 表示该工具上线后反响远超预期，击中了人们想知道自己是否能在超级智能中'永生'的好奇心。
extract_result: success
object_mentions:
- object_type: product
  name: In the Weights
  canonical_name: In the Weights
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Thomas Dimson 和 Joey Flynn 创建了 In the Weights 网站，该工具通过查询多个 AI 模型来评估一个人被 AI 记忆的程度并分配强度分数。
  - 网站会查询包括 Grok、Gemini、GPT、Claude、Llama 在内的不同模型，并以提问'<名字>是谁'的方式获取回答后再聚类评分。
  - Dimson 表示该工具上线后反响远超预期，击中了人们想知道自己是否能在超级智能中'永生'的好奇心。
  article_id: abec0710ffac301a
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