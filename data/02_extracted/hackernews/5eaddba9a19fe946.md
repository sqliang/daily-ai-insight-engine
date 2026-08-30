---
title: 'Verschlimmbesserung: The Word Your Software Updates Need'
source: https://geekyschmidt.com/post/2026-08-25-verschlimmbesserung/
author:
- '[[speckx]]'
published: '2026-08-28'
created: '2026-08-29'
manifest_dates:
- '2026-08-29'
description: 'Article URL: https://geekyschmidt.com/post/2026-08-25-verschlimmbesserung/
  Comments URL: https://news.ycombinator.com/item?id=49479072 Points: 133 # Comments:
  89'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 5eaddba9a19fe946
source_type: community_discussion
tldr: 一篇评论文章用德语词 Verschlimmbesserung（本想改进却弄得更糟）概括软件更新的副作用，批评许多 SaaS 更新为发布而发布、破坏用户依赖的工作流，援引
  Eliyahu Goldratt 的指标塑造行为观点，主张稳定性是特性、知道何时不发布是工程纪律。
objective_summary: geekyschmidt.com 于 2026 年 8 月 25 日发布评论文章，用德语词 Verschlimmbesserung
  指代"试图改进反而使事情更糟"的行为，并以此形容软件更新的副作用。文章批评 SaaS 产品团队为发布而发布，随意移动按钮、重命名菜单，却破坏了用户日常依赖的工作流程。作者引用
  Eliyahu Goldratt 关于衡量指标如何塑造团队行为的论点，指出工程师并非失败，而是在优化公司给定的指标。文章以 Office 2003 为例，论证新版本未必更好，主张稳定性是特性，知道何时不该发布是一种工程纪律。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies:
  - Microsoft
  technologies:
  - SaaS
  key_people:
  - Eliyahu Goldratt
key_logic_flow:
- 德语单词 Verschlimmbesserung 的含义是"试图改进反而使事情更糟"，文章用它来形容软件更新带来的副作用。
- 文章指出许多 SaaS 更新只是移动按钮、重命名菜单，却破坏了用户日常依赖的工作流程。
- 文章引用 Eliyahu Goldratt 的名言，认为衡量指标不理性，团队的行为也会不理性，团队只是在为给定的指标而优化。
- 当版本发布比产品本身更重要时，公司就在激励 Verschlimmbesserung 式的行为，而非真正的产品改进。
- 文章以 Office 2003 为例，论证新版本未必更好，稳定性本身就是一项特性。
- 作者主张知道何时不该发布是一种工程纪律，工程师团队并非失败，而是在适应公司设定的指标。
object_mentions:
- object_type: product
  name: Office 2003
  canonical_name: Microsoft Office 2003
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 文章以 Office 2003 为例，说明它因没有被强迫不断自我改版而至今依然非常实用，并以此论证新版本未必更好。
  article_id: 5eaddba9a19fe946
extract_result: success
---

**The German language has a word for what your last software update did.**

It is called **Verschlimmbesserung**: an attempted improvement that only makes things worse.

We have all lived through the SaaS update that moved a button, renamed a menu, and broke a workflow we relied on daily. Some product team shipped a “better experience” that solved a problem nobody had.

Eliyahu Goldratt nailed the root cause decades ago:


“Tell me how you measure me, and I will tell you how I will behave. If you measure me in an illogical way… do not complain about illogical behaviour…”

When point releases become more important than the product itself, you are incentivising Verschlimmbesserung. Your engineering teams are not failing. They are optimising for the metrics you gave them.

How you measure and incentivise your teams tells them exactly what you value. If the metric rewards churn, you get churn. If the metric rewards shipping, you get shipping; whether it improves anything or not.

Is new always better? Probably not. Office 2003 is still incredibly useful because nobody forced it to constantly reinvent itself.

Stability is a feature. Knowing when not to ship is an engineering discipline.

The Germans built a word for it. Perhaps we should start using it.