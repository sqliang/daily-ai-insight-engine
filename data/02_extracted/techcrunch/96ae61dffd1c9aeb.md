---
title: Databricks hits $188B valuation, extending its run as AI’s favorite second
  act
source: https://techcrunch.com/2026/07/17/databricks-hits-188b-valuation-extending-its-run-as-ais-favorite-second-act/
author:
- '[[Julie Bort]]'
published: '2026-07-17'
created: '2026-07-18'
manifest_dates:
- '2026-07-18'
- '2026-07-19'
description: Databricks has remade its image into an AI company and has published
  research on the cost savings of open weight AI models for coding.
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 96ae61dffd1c9aeb
source_type: news_media
tldr: Databricks 宣布新一轮融资，估值达 1880 亿美元，本轮由 Coatue 领投。这是其 18 个月来的第四次大额融资，公司成功从大数据 SaaS
  厂商转型为 AI 基础设施提供商。
objective_summary: 2026 年 7 月 17 日，Databricks 宣布由 Coatue 领投的新一轮融资，估值达 1880 亿美元。融资金额约
  30 亿美元，预计夏末完成交割。这是该公司自 2024 年 12 月以来第四次大规模融资，估值从 620 亿一路升至 1880 亿。Databricks 利用其企业数据平台基础，推出
  Lakebase、Unity、Omnigent 等 AI 产品，同时积极采用中国开源大模型（如 Z.ai 的 GLM 5.2）以降低 AI 成本。
event_type: capital_movement
epistemic_status: verified_fact
entities:
  companies:
  - Databricks
  - Coatue
  - Z.ai
  - Anthropic
  - OpenAI
  technologies:
  - AI agent
  - open-weight model
  - GLM 5.2
  key_people:
  - Ali Ghodsi
key_logic_flow:
- Databricks 宣布由 Coatue 领投的新一轮融资，估值达 1880 亿美元，融资金额约 30 亿美元。
- 这是 Databricks 在 18 个月内第四次大额融资：2024 年 12 月以 620 亿估值融资 100 亿，2025 年 9 月以 1000 亿估值融资
  10 亿，2026 年 2 月以 1340 亿估值融资 50 亿。
- Databricks 从 2013 年创立时的大数据 SaaS 厂商成功转型为 AI 基础设施提供商，推出 Lakebase（AI 代理数据库）、Unity（AI
  网关）和 Omnigent（多智能体管理框架）等 AI 产品。
- Databricks 是 2026 年企业采用低成本中文开源大模型趋势的代表案例，尤其推崇 Z.ai 的 GLM 5.2 模型用于代码生成。
- CEO Ali Ghodsi 公布内部测试结果，称开源模型（尤其是 GLM 5.2）在处理编程任务上已达到最高难度级别，且总成本低于 Anthropic 和 OpenAI
  的闭源模型。
object_mentions:
- object_type: product
  name: Lakebase
  canonical_name: Databricks Lakebase
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Databricks 推出了 Lakebase，这是其专为 AI 代理构建的数据库产品。
  article_id: 96ae61dffd1c9aeb
- object_type: product
  name: Unity
  canonical_name: Databricks Unity
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Databricks 推出了 Unity，这是其 AI 网关产品，用于管理和治理 AI 访问。
  article_id: 96ae61dffd1c9aeb
- object_type: product
  name: Omnigent
  canonical_name: Databricks Omnigent
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Databricks 推出了名为 Omnigent 的元编排框架，用于管理多个 AI 代理的协同工作。
  article_id: 96ae61dffd1c9aeb
- object_type: model
  name: GLM 5.2
  canonical_name: Z.ai GLM 5.2
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Databricks 积极采用 Z.ai 的 GLM 5.2 作为代码生成模型，内部测试显示其编程能力达到最高难度级别，且总成本低于 Anthropic 和
    OpenAI 的闭源模型。
  article_id: 96ae61dffd1c9aeb
extract_result: success
---

Databricks on Thursday announced a new round of funding that values the company at $188 billion. The round was led by Coatue.

Databricks didn’t disclose exactly how much it raised; it said the money isn’t in its hands yet and that the round will close later this summer. (Other outlets have since reported the raise is roughly $3 billion.) While it’s unusual for a company to announce before it gets the money, a VC tells TechCrunch that the deal is solid, with so many firms wanting in that the company had no reason to keep its shiny new valuation a secret.

In fact, Databricks has been on a year-and-a-half fundraising tear as it successfully transitioned its image into an AI provider and not just a yesteryear SaaS sensation. Yesteryear being back in the BC times (Before ChatGPT).

Only five months ago, in February, Databricks closed a $5 billion Series L raise at a $134 billion valuation. Five months before that, in September 2025, it raised $1 billion at a $100 billion valuation. And roughly nine months before that, in December 2024, it raised what was a record-breaking round at the time of $10 billion at a $62 billion valuation.

Databricks has raised so many rounds over the years that this latest one became the subject of memes about running out of letters of the alphabet. “Turning on alerts for when we get a Series AA,” one person posted.

But its image reconstruction has been legit. Founded in 2013, it initially grew to success back in the big data era, with software that enabled enterprises to store enormous amounts of data in the cloud, yet produce speedy analytics.

Because it already sat on troves of enterprise data, Databricks was then well-positioned to respond as companies started wanting AI with the same security and governance they expect from traditional enterprise software.

The company began rolling out one AI product after another, like Lakebase, its database built for AI agents, and Unity, its AI gateway, along with a “meta-harness” called Omnigent that manages multiple agents.

Databricks also increasingly became known as one of the big examples of enterprises adopting more affordable Chinese-based open-weight models (models whose underlying code is published for anyone to use and modify) for cost control, one of the big trends of 2026. It is a particular champion of Z.ai’s GLM 5.2 as a model for coding.

Last week Databricks CEO Ali Ghodsi shared the results of some internal benchmarking done to manage his own AI costs for his 3,000 software engineers.

The company compared AI models on the actual tasks its programmers do. Not surprisingly, in the blog post revealing the results, Databricks shared that “open models, and GLM 5.2 in particular, are now able to handle even the highest level of task difficulty” in coding, and at a total lower cost than proprietary models from Anthropic and OpenAI.