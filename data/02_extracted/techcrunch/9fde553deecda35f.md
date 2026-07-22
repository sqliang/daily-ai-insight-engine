---
title: Patronus AI lands $50M to build ‘digital worlds’ that stress-test AI agents
source: https://techcrunch.com/2026/06/25/patronus-ai-lands-50m-to-build-digital-worlds-that-stress-test-ai-agents/
author:
- '[[Marina Temkin]]'
published: '2026-06-25'
created: '2026-06-26'
description: Agent-testing startup Patronus AI, founded by former Meta AI researchers,
  is experiencing nearly insatiable demand, its investor says.
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 9fde553deecda35f
source_type: news_media
tldr: Patronus AI 完成 5000 万美元 B 轮融资，用于构建模拟数字环境来压力测试 AI 代理的性能，公司年收入增长 15 倍，总融资额达 7000
  万美元。
objective_summary: Patronus AI 是一家 2023 年由前 Meta AI 研究员 Anand Kannappan 和 Rebecca
  Qian 创立的旧金山初创公司，通过构建名为"数字世界模型"的模拟环境，在强化学习训练后对 AI 代理进行压力测试，以此评估其在真实复杂任务中的可靠性。该公司于
  2026 年 6 月 25 日宣布完成 5000 万美元 B 轮融资，由 Greenfield Partners 领投，Notable Capital、Lightspeed、Datadog
  和 Samsung 参投，累计融资达 7000 万美元。公司过去一年收入增长 15 倍，客户覆盖几乎所有前沿 AI 实验室，目前主要聚焦软件工程和金融领域的可验证问题。
event_type: capital_movement
epistemic_status: verified_fact
entities:
  companies:
  - Patronus AI
  - Greenfield Partners
  - Notable Capital
  - Lightspeed
  - Datadog
  - Samsung
  - Meta
  - Waymo
  technologies:
  - AI agents
  - reinforcement learning
  - digital world models
  key_people:
  - Anand Kannappan
  - Rebecca Qian
  - Glenn Solomon
key_logic_flow:
- Patronus AI 由前 Meta AI 研究员 Anand Kannappan 和 Rebecca Qian 于 2023 年创立，总部位于旧金山，主要帮助模型厂商和公司构建模拟数字环境来评估
  AI 代理在复杂真实任务中的可靠性。
- 该公司于 2026 年 6 月 25 日宣布完成 5000 万美元 B 轮融资，由 Greenfield Partners 领投，Notable Capital、Lightspeed、Datadog
  和 Samsung 参投，累计融资达 7000 万美元。
- Patronus 使用名为"数字世界模型"的技术创建网站和内部系统的模拟副本，代理在这些环境中通过强化学习进行训练后压力测试，通过迭代奖励成功完成任务并惩罚错误。
- 公司将这一方法类比于 Waymo 先构建合成世界来测试自动驾驶汽车应对罕见危险场景的方式，区别在于 AI 代理倾向于走捷径，而 Patronus 擅长发现这些取巧行为。
- 公司过去一年收入增长 15 倍，客户覆盖几乎所有前沿 AI 实验室和众多新兴初创公司，目前主要聚焦软件工程和金融领域的可验证问题。
- 公司联合创始人 Kannappan 表示，未来计划扩展到难以验证的更多领域，并希望创建能让代理持续运行 10 小时甚至 10 周的测试环境。
extract_result: success
object_mentions:
- object_type: company
  name: Patronus AI
  canonical_name: Patronus AI
  url: https://www.patronus.ai
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Patronus AI 由前 Meta AI 研究员 Anand Kannappan 和 Rebecca Qian 于 2023 年创立，通过构建模拟数字环境来评估
    AI 代理在复杂真实任务中的可靠性。
  - 该公司于 2026 年 6 月 25 日宣布完成 5000 万美元 B 轮融资，由 Greenfield Partners 领投，多家机构参投，累计融资达
    7000 万美元。
  - 公司过去一年收入增长 15 倍，客户覆盖几乎所有前沿 AI 实验室和众多新兴初创公司，Notable Capital 描述其需求几乎供不应求。
  article_id: 9fde553deecda35f
- object_type: product
  name: Patronus Digital World Models
  canonical_name: Patronus Digital World Models
  url: null
  confidence: medium
  article_role: primary_subject
  evidence_snippets:
  - Patronus 使用名为"数字世界模型"的技术创建网站和内部系统的模拟副本，通过强化学习对 AI 代理进行训练后压力测试。
  - 该公司将这一方法类比于 Waymo 先构建合成世界来测试自动驾驶汽车应对罕见危险场景，帮助 AI 代理尝试各种不可预测的复杂场景。
  - Patronus 目前主要聚焦软件工程和金融领域的可验证问题，并计划未来扩展到难以验证的更多领域。
  article_id: 9fde553deecda35f
---

AI agents are becoming more sophisticated. They are evolving from answering questions to autonomously executing multi-step complex tasks.

But before these agents can be trusted to book trips or conduct financial analysis on behalf of users, model providers and the startups building such agents want to ensure that they perform reliably across a vast range of scenarios.

AI labs often use benchmarks to show off their model’s prowess, but a high score, even on an agent-oriented benchmark, doesn’t actually prove that an AI can accomplish various complex, real-world jobs correctly.

Patronus AI, a startup founded in 2023 by former Meta AI researchers Anand Kannappan and Rebecca Qian, is helping model makers and companies fine-tune models to do just that by building simulated digital environments in which to evaluate the agents’ performance.

The San Francisco-based startup must be solving an important problem. Virtually every frontier AI lab and many emerging startups are now customers, according to Glenn Solomon, a managing director at Notable Capital, who describes demand for the company’s simulated environments as nearly insatiable.

Patronus’ revenue has grown 15-fold over the past year, fueling significant investor interest. On Thursday, the company announced a $50 million Series B round led by Greenfield Partners, with participation from Notable Capital, Lightspeed, Datadog, and Samsung. The round brings the company’s total funding to $70 million.

Patronus uses what it calls “digital world models” to create replicas of websites and internal systems. In these environments, agents are stress-tested after training using reinforcement learning, which iteratively rewards successful task completion and penalizes errors.

AI labs see great value in these digital simulations because they give agents a chance to try different, sometimes unpredictable, scenarios. The company compares its approach to how Waymo trained autonomous cars by first building synthetic worlds to test vehicles against rare hazards, such as severe weather or a child running after a ball.

The difference with AI agents is that they tend to take shortcuts, which means they fail to complete the task correctly. “Patronus is really good at spotting the hacks and making sure they are holding the models accountable,” Solomon said.

Patronus is currently providing its simulated digital worlds for software engineering and finance, but these are just the start, according to Kannappan.

“Today we’re very focused on the problems that are verifiable, so the problems that you can immediately check and verify, but there are a ton more areas that are very non-verifiable or very hard to verify,” he said.

Just because these processes are verifiable doesn’t mean they are simple. “We want to be able to actually create the environment in which you can operate an agent that can run for 10 hours or 10 days or 10 weeks,” Kannappan said.