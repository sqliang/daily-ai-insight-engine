---
title: Facing US export controls, China's DeepSeek plans to make its own chips (2
  minute read)
source: https://arstechnica.com/ai/2026/07/facing-us-export-controls-chinas-deepseek-plans-to-make-its-own-chips/?utm_source=tldrai
author: []
published: ''
created: '2026-07-09'
description: TLDR AI 每日头条
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: adfef108caf2f335
source_type: news_media
tldr: 中国 AI 初创公司 DeepSeek 计划自研数据中心推理芯片，以应对美国出口管制并减少对华为和英伟达的依赖。该项目已进行约一年，正在招聘工程师并寻找硬件合作伙伴。
objective_summary: DeepSeek 正在计划进入芯片制造领域，专注于数据中心推理芯片而非训练芯片。该项目已持续约一年，公司正在与硬件和芯片领域的潜在合作伙伴会面并招聘工程师。此举旨在减少对华为和英伟达的依赖，美国对华芯片出口管制是主要驱动力之一。与此同时，OpenAI
  与 Broadcom 刚联合发布了其首款推理芯片 Jalapeño，Anthropic 也在探索定制芯片设计。
event_type: infrastructure_update
epistemic_status: rumor_leak
entities:
  companies:
  - DeepSeek
  - OpenAI
  - Anthropic
  - Broadcom
  - Huawei
  - Nvidia
  - Alibaba
  - Baidu
  - Reuters
  technologies:
  - inference chip
  - data center chip
  - large language model
  key_people: []
key_logic_flow:
- DeepSeek 计划进入芯片制造领域，项目已进行约一年，目前正在与硬件和芯片潜在合作伙伴会面并招聘工程师。
- 该公司将专注于数据中心推理芯片而非训练芯片，目标之一是减少对华为和英伟达的依赖。
- 美国对华芯片出口管制是该计划紧迫性的主要原因，华为目前控制着中国约一半的数据中心芯片市场。
- 中国科技巨头阿里巴巴和百度也在进行类似的芯片自研布局。
- OpenAI 与 Broadcom 刚联合发布了其首款推理芯片 Jalapeño，旨在减少对英伟达的依赖并实现对技术栈的全面控制。
- Anthropic 也在探索定制芯片设计，但尚未有公开可见的里程碑进展。
extract_result: success
object_mentions:
- object_type: product
  name: Jalapeño
  canonical_name: OpenAI Jalapeño
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - OpenAI 与 Broadcom 联合宣布了 Jalapeño，这是 OpenAI 首款专为大规模推理设计的芯片。
  - OpenAI 自研芯片部分是为了减少对英伟达的依赖，同时也希望获得类似苹果对技术栈的全面控制。
  article_id: adfef108caf2f335
- object_type: project
  name: DeepSeek Custom Chip Project
  canonical_name: DeepSeek Custom Chip Project
  url: null
  confidence: medium
  article_role: primary_subject
  evidence_snippets:
  - 路透社援引三位知情人士报道，DeepSeek 已推进芯片自研约一年，正在与硬件和芯片领域的潜在合作伙伴会面。
  - DeepSeek 芯片项目专注于数据中心推理芯片而非训练芯片，目标之一是减少对华为和英伟达的依赖。
  - DeepSeek 正在为该芯片项目招聘工程师，美国出口管制是该计划紧迫性的主要原因。
  article_id: adfef108caf2f335
---

DeepSeek, the Chinese startup developing large language models that are competitive with those from US companies like OpenAI and Anthropic, is planning to enter the silicon business, according to Reuters.

Citing three people familiar with the matter, Reuters writes that DeepSeek has been working on a move into silicon for about a year. It has been meeting with potential partners in the hardware and silicon space and has been hiring engineers for the project.

The focus is on data center chips for inference, not training, and the goal is likely to reduce reliance on both Huawei and Nvidia.

Nvidia is the chipmaker for most AI companies in North America and Europe, but a United States export ban has prevented the company from achieving a similar presence in China. Huawei controls about half of the data center chip market there, and DeepSeek isn’t the only one trying to enter; Chinese tech giants like Alibaba and Baidu have been making moves, too.

While chip export controls in the US are a major reason this is an urgent concern for DeepSeek, US-based AI companies are making similar chip plans.

For example, OpenAI and Broadcom jointly announced Jalapeño, the former’s first chip designed for inference at scale, just a couple of weeks ago. Anthropic, too, has been exploring custom chip design, though there have not been any publicly visible milestones yet.

In OpenAI’s case, it’s partly a play to reduce its reliance on Nvidia, but it’s also a desire to have Apple-like control over the entire tech stack for its products. Further, getting in at the silicon and data center levels can be an advantage in a market where data center access is likely to remain constrained, with multiple companies competing for compute as they scale up their AI models and services.