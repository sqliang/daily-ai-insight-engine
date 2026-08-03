---
title: 'GrocLM: Grocery Category Recommendation in E-Commerce with Large Language
  Models'
source: https://arxiv.org/abs/2607.24764
author:
- '[[Yuan Zhong, Chuanwei Ruan, Moein Hasani, Tejaswi Tenneti, Haixun Wang, Fenglong
  Ma]]'
published: '2026-07-29'
created: '2026-07-29'
manifest_dates:
- '2026-07-29'
description: 'arXiv:2607.24764v1 Announce Type: new Abstract: The rapid growth of
  online grocery shopping requires recommendation systems that capture cyclical purchasing
  behavior and diverse user intents. Traditional item-level methods face scalability
  and accuracy challenges, motivating category-level recommendation as a more structured
  and practical alternative. We present GROCLM, a fine-tuned language model for grocery
  category recommendation in a real-world production environment. GROCLM employs a
  two-stage LoRA-based training strategy to encode cyclical purchasing patterns directly
  into model parameters, enabling more effective utilization of rebuying signals compared
  to prompt-based conditioning. To ensure valid and controllable outputs, we further
  introduce a trie-based constrained decoding mechanism over a predefined category
  space. Experiments on both proprietary production data and a public benchmark demonstrate
  that GROCLM consistently outperforms strong baselines. In a live production restocking
  task, GROCLM achieves a 7.5% relative improvement in cart-adds per impression, while
  maintaining efficient inference by generating all categories jointly. These results
  highlight the effectiveness and practicality of integrating large language models
  into structured recommendation systems.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 2ee3d57a9a4ce9cd
source_type: academic_paper
tldr: 论文提出 GROCLM，一个针对线上杂货电商品类推荐微调的语言模型。它采用两阶段 LoRA 训练将周期性购买模式编码进模型参数，并用前缀树约束解码保证输出可控；在线上补货任务中每展示加购数相对提升
  7.5%，优于强基线模型。
objective_summary: GROCLM 是 arXiv 上发布的一篇论文，提出用于电商杂货品类推荐的微调语言模型，其研究背景是线上杂货购物的快速增长对推荐系统提出可扩展性与准确性挑战。研究团队采用两阶段
  LoRA 训练策略，把周期性购买模式直接编码进模型参数，并设计基于前缀树的约束解码机制限定在预定义品类空间内输出。实验基于专有生产数据与公开基准，结果显示 GROCLM
  一致优于强基线；在线上补货任务中每展示加购数取得 7.5% 的相对提升，并通过联合生成全部品类实现高效推理。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - LoRA
  - LLM
  - trie-based constrained decoding
  - grocery category recommendation
  - fine-tuned language model
  key_people: []
key_logic_flow:
- GROCLM 是一个针对电商杂货场景微调的语言模型，用于品类级推荐，以应对传统单品级方法在扩展性和准确性上的挑战。
- 模型采用两阶段 LoRA 微调训练策略，将周期性购买行为直接编码进模型参数，比基于提示的条件化方式更有效地利用复购信号。
- 为保障输出有效且可控，论文引入基于前缀树的约束解码机制，将生成范围限制在预定义品类空间内。
- 实验在专有生产数据和公开基准上展开，结果显示 GROCLM 一致优于强基线模型。
- 在线上补货任务中，GROCLM 取得每展示加购数 7.5% 的相对提升，并通过联合生成全部分类保持高效推理。
object_mentions:
- object_type: model
  name: GrocLM
  canonical_name: GrocLM
  url: https://arxiv.org/abs/2607.24764
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 论文提出 GROCLM，一个在真实生产环境中面向杂货品类推荐微调的语言模型，通过两阶段 LoRA 训练将周期性购买模式编码进模型参数。
  - GROCLM 在预定义品类空间上引入基于前缀树的约束解码机制，以保证输出有效且可控，并联合生成所有品类以维持高效推理。
  - 在线上补货任务中，GROCLM 相比强基线实现每展示加购数 7.5% 的相对提升，并在专有生产数据和公开基准上均表现更优。
  article_id: 2ee3d57a9a4ce9cd
extract_result: success
---

# Computer Science > Artificial Intelligence

# Title:GrocLM: Grocery Category Recommendation in E-Commerce with Large Language Models

View PDF HTML (experimental)Abstract:The rapid growth of online grocery shopping requires recommendation systems that capture cyclical purchasing behavior and diverse user intents. Traditional item-level methods face scalability and accuracy challenges, motivating category-level recommendation as a more structured and practical alternative. We present GROCLM, a fine-tuned language model for grocery category recommendation in a real-world production environment. GROCLM employs a two-stage LoRA-based training strategy to encode cyclical purchasing patterns directly into model parameters, enabling more effective utilization of rebuying signals compared to prompt-based conditioning. To ensure valid and controllable outputs, we further introduce a trie-based constrained decoding mechanism over a predefined category space. Experiments on both proprietary production data and a public benchmark demonstrate that GROCLM consistently outperforms strong baselines. In a live production restocking task, GROCLM achieves a 7.5% relative improvement in cart-adds per impression, while maintaining efficient inference by generating all categories jointly. These results highlight the effectiveness and practicality of integrating large language models into structured recommendation systems.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.