---
title: Claude Fable 5 Mythos 5
source: https://www.anthropic.com/news/claude-fable-5-mythos-5
author: []
published: '2026-06-09'
created: '2026-06-10'
description: ''
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: e11fcea9cd94bb20
source_type: tech_blog
tldr: Anthropic 发布 Claude Fable 5 和 Claude Mythos 5，后者专供网络防御用途
objective_summary: Anthropic 推出 Claude Fable 5（安全版）及 Claude Mythos 5（无限制版），后者通过 Project
  Glasswing 与美国政府合作部署。定价每百万输入令牌 10 美元、输出令牌 50 美元，为 Mythos Preview 的一半。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - Anthropic
  technologies: []
  key_people: []
key_logic_flow:
- Anthropic 发布了 Claude Fable 5（通用安全版）和 Claude Mythos 5（专为网络防御设计）两款新模型。
- Fable 5 在几乎所有基准测试中达到最先进水平，在软件工程、知识工作、视觉、科学研究和生命科学等领域表现领先。
- Fable 5 配备安全防护，涉及某些敏感话题的查询将被转至 Claude Opus 4.8 处理，平均触发率低于 5% 的会话。
- Claude Mythos 5 与 Fable 5 共享同一基础模型，但在部分领域移除了安全限制，通过 Project Glasswing 与美国政府合作部署。
- 两款模型的定价为每百万输入令牌 10 美元、输出令牌 50 美元，是 Claude Mythos Preview 价格的一半。
extract_result: success
---

# Claude Fable 5 and Claude Mythos 5

Today we’re launching **Claude Fable 5**: a Mythos-class1 model that we’ve made safe for general use.

Fable 5’s capabilities exceed those of any model we’ve ever made generally available. It is state-of-the-art on nearly all tested benchmarks of AI capability, showing exceptional performance in software engineering, knowledge work, vision, scientific research, and many other areas. The longer and more complex the task, the larger Fable 5’s lead over our other models.

Releasing a model this capable comes with risks. Without safeguards, Fable 5’s capabilities in areas like cybersecurity could be misused to cause serious damage. We’ve therefore launched the model with safeguards that mean queries on some topics will instead receive a response from our next-most-capable model, Claude Opus 4.8. To release the model both safely and quickly, we’ve tuned these safeguards conservatively—they’ll sometimes catch harmless requests, though they trigger, on average, in less than 5% of sessions. With more capable models arriving in the coming months, we’re working to improve our safeguards and reduce false positives as quickly as we can.

For a small group of cyberdefenders and infrastructure providers, we’re also launching **Claude Mythos 5**. It’s the same underlying model as Fable 5, but with the safeguards lifted in some areas.2 Mythos 5 will initially be deployed through Project Glasswing, in collaboration with the US government, as an upgrade to Claude Mythos Preview. It has the strongest cybersecurity capabilities of any model in the world. Soon, we intend to expand access to Mythos 5 through a broader trusted access program.

The capabilities of models like Fable 5 and Mythos 5 have the potential to do profound good for the world. We’ve seen the beginnings of this in Project Glasswing, where the models have helped cyber defenders secure critically important software. We’ve also seen it in life sciences research, where the models are positing novel hypotheses and speeding up the development of new therapeutics.

Fable 5 and Mythos 5 are being offered at $10 per million input tokens and $50 per million output tokens—less than half the price of Claude Mythos Preview. Today’s joint launch is another step towards our goal of bringing advanced AI capabilities to as many users as possible, as quickly and as safely as we can.

## Evaluating Claude Fable 5 and Claude Mythos 5

The table below compares the capabilities of Fable 5 and Mythos 5 to other leading models.


Fable 5 and Mythos 5 can work autonomously for longer than any previous Claude models. Below we discuss how these skills apply to software engineering, and cover the model’s improved capabilities in knowledge work, vision, memory, and life sciences research.