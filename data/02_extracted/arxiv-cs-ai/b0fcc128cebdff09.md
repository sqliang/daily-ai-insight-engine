---
title: Personalization, Personas, and Forecasting in Value Alignment
source: https://arxiv.org/abs/2607.24782
author:
- '[[James Wedgwood, Pratiksha Thaker, Neil Kale, Virginia Smith]]'
published: '2026-07-30'
created: '2026-07-30'
manifest_dates:
- '2026-07-30'
description: ''
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: b0fcc128cebdff09
source_type: academic_paper
tldr: 一篇 arXiv 论文通过世界价值观调查（WVS）测试了 GPT-5.4、Claude Sonnet 4.6、Gemini 2.5 Flash 和 Qwen3-235B
  在个性化、人设扮演与第三人称预测三种提示框架下的文化价值对齐表现，发现第三人称预测对多数模型的方向对齐最强，提示框架会显著改变模型行为与测量到的对齐度。
objective_summary: 该论文（arXiv 2607.24782）使用世界价值观调查（WVS）的 101 道衍生问题，在 13 个语言-国家切片上评估
  GPT-5.4、Claude Sonnet 4.6、Gemini 2.5 Flash 和 Qwen3-235B 四款模型。研究者对比了仅语言基线、用户国家、人设国家和第三人称四种提示设置，共采集
  21,008 行模型响应。结果显示提示框架是文化对齐的一阶决定因素：国家线索会显著改变回答，但并非所有位移都朝向匹配的人类回答分布。第三人称预测对四款托管模型中的三款产生最强的方向性对齐，而个性化与人设扮演效果较弱且不稳定；对齐增益集中在宗教性、性别角色和工作导向物质价值观等维度，制度信任与民主相关问题仍难以对齐。
event_type: policy_and_safety
epistemic_status: theoretical_claim
entities:
  companies:
  - OpenAI
  - Anthropic
  - Google
  - Alibaba
  - World Values Survey
  technologies:
  - LLM
  - value alignment
  - prompt engineering
  key_people: []
key_logic_flow:
- 研究以世界价值观调查（WVS）的 101 道衍生问题为基础，覆盖 13 个语言-国家切片，用于测试大型语言模型在个性化、人设扮演和预测三种提示框架下的文化价值对齐。
- 研究评估了 GPT-5.4、Claude Sonnet 4.6、Gemini 2.5 Flash 和 Qwen3-235B 四款模型，累计采集 21,008 行模型响应，并对比仅语言基线、用户国家、人设国家与第三人称四种提示条件。
- 结果表明提示框架是文化对齐的一阶决定因素，国家线索会显著改变模型回答，但并非所有位移都朝向匹配的人类回答分布移动。
- 第三人称预测框架对四款托管模型中的三款产生最强的方向性对齐，而个性化和人设扮演两种框架的效果较弱且稳定性不足。
- 对齐增益集中在宗教性、性别角色和工作导向物质价值观等突出维度，而制度信任与民主相关的问题仍然难以实现对齐。
- 论文结论认为提示框架在文化价值抽取中并非表面选择，它会同时改变模型行为与测量到的对齐程度。
object_mentions:
- object_type: paper
  name: Personalization, Personas, and Forecasting in Value Alignment
  canonical_name: Personalization, Personas, and Forecasting in Value Alignment
  url: https://arxiv.org/abs/2607.24782
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 该论文通过世界价值观调查评估提示框架对大型语言模型文化价值对齐的影响，是本文的核心研究对象。
  - 论文在 21,008 行模型响应上对比四种提示条件，发现第三人称预测对多数模型的方向性对齐效果最强。
  article_id: b0fcc128cebdff09
- object_type: model
  name: GPT-5.4
  canonical_name: GPT-5.4
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 论文在 101 道 WVS 衍生问题上评估了 GPT-5.4 的文化对齐表现，并将其与其他三款模型的结果进行对比。
  article_id: b0fcc128cebdff09
- object_type: model
  name: Claude Sonnet 4.6
  canonical_name: Claude Sonnet 4.6
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 论文将 Claude Sonnet 4.6 纳入评估，用于比较不同提示框架下的文化价值对齐表现。
  article_id: b0fcc128cebdff09
- object_type: model
  name: Gemini 2.5 Flash
  canonical_name: Gemini 2.5 Flash
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 论文评估了 Gemini 2.5 Flash 在 13 个语言-国家切片上的价值对齐表现，并记录其回答位移。
  article_id: b0fcc128cebdff09
- object_type: model
  name: Qwen3-235B
  canonical_name: Qwen3-235B
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 论文将 Qwen3-235B 作为被评估模型之一，测试其在不同提示框架下的文化对齐表现。
  article_id: b0fcc128cebdff09
- object_type: dataset
  name: World Values Survey (WVS)
  canonical_name: World Values Survey
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 论文使用世界价值观调查（WVS）的 101 道衍生问题作为评测模型文化价值对齐的基准数据。
  article_id: b0fcc128cebdff09
extract_result: success
---

# Computer Science > Artificial Intelligence

# Title:Personalization, Personas, and Forecasting in Value Alignment

View PDF HTML (experimental)Abstract:LLM behavior may be conditioned by human identity in several ways: they may be asked to adapt to users, role-play populations, or forecast how people would answer value-laden questions. We test whether these framings are interchangeable using the World Values Survey (WVS). We evaluate GPT-5.4, Claude Sonnet 4.6, Gemini 2.5 Flash, and Qwen3-235B on 101 WVS-derived questions across 13 language-country slices, comparing a language-only baseline with user-country, persona-country, and third-person prompts. Across 21,008 model-response rows, prompt framing is a first-order determinant of cultural alignment: country cues often shift answers substantially, but not all shifts move toward matched human response distributions. Third-person forecasting yields the strongest directional alignment for three of the four hosted models, while personalization and role-play are weaker or less stable. Alignment gains concentrate on salient value dimensions such as religiosity, gender roles, and work-oriented material values, whereas institutional trust and democracy-related questions remain difficult. These results show that prompt framing is not a cosmetic choice in cultural value elicitation; it changes both model behavior and measured alignment.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.