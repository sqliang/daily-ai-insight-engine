---
title: Sakana Fugu (3 minute read)
source: https://threadreaderapp.com/thread/2068862070062485867.html?utm_source=tldrai
author: []
published: ''
created: '2026-06-24'
description: TLDR AI 每日头条
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 14d95bec95cebb8d
source_type: news_media
tldr: Sakana 发布 Fugu 协调型模型，可动态调度多个底层 LLM 协同完成任务。Fugu Ultra 在自主 ML 研究中平均性能（0.9774）和金融预测回报率（+19.43%）均超过
  GPT 5.5、Gemini 3.1 Pro 和 Opus 4.8 等单体模型。
objective_summary: Sakana 于 2026 年 7 月发布名为 Fugu 的协调型模型（Orchestration Model），它本身是一个
  LLM，能够训练后调用自身或其他 LLM 实例组成代理池。Fugu 提供两个版本：Fugu（平衡性能与延迟）和 Fugu Ultra（旗舰版），均通过 OpenAI
  兼容 API 访问。在 Beta 测试中，Fugu Ultra 在自主 ML 研究任务上平均性能达 0.9774，在 50 周金融时间序列预测中实现 +19.43%
  的平均回报率，均优于 GPT 5.5、Gemini 3.1 Pro 和 Opus 4.8。Sakana 强调 Fugu 的多模型协调架构可规避单一供应商风险，是实现
  AI 主权的基础设施。
event_type: application_landing
epistemic_status: pr_statement
entities:
  companies:
  - Sakana
  technologies:
  - LLM
  - Orchestration Model
  - Multi-Agent System
  key_people: []
key_logic_flow:
- Sakana 发布 Fugu，这是一种协调型模型（Orchestration Model），本身也是一个 LLM，能够调用多个底层 LLM 实例（包括自身递归调用）组成动态代理池，通过单一
  OpenAI 兼容 API 对外提供服务。
- Fugu 提供两个版本：Fugu（平衡性能与延迟，适合日常编码和聊天交互）和 Fugu Ultra（旗舰版，专为 AI 研究、网络安全分析等高难度多步骤任务优化答案质量）。
- 在自主机器学习研究测试中，Fugu Ultra 在单张 H100 GPU 上运行超过 100 次实验，以平均性能 0.9774 和单次最佳成绩 0.9748 超越了
  GPT 5.5、Gemini 3.1 Pro 和 Opus 4.8 三个对照模型。
- 在 50 周金融时间序列预测测试中，Fugu Ultra 以 $10,000 本金实现 +19.43% 的平均回报率，而其他三个前沿模型回报率均低于 15%。
- Sakana 指出依赖单一公司模型存在地缘政治供应中断风险，Fugu 的动态模型路由架构可在不修改代码的情况下绕过供应商限制，为组织或国家实现 AI 主权提供技术基础。
- Fugu 经过 500 名用户的 Beta 测试，在数据科学、网络安全评估等全自动工作流中展示了几乎无需人工干预的持续任务推进能力。
extract_result: success
object_mentions:
- object_type: product
  name: Sakana Fugu
  canonical_name: Sakana Fugu
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Sakana Fugu 是一种协调型模型，本身也是一个 LLM，经过训练可调用包括自身实例在内的各种 LLM 组成动态代理池来协同完成复杂任务。
  - Fugu 提供两个版本：Fugu（平衡性能与延迟）和 Fugu Ultra（旗舰版，专为多步难题优化答案质量），均通过单一的 OpenAI 兼容 API 访问。
  - 在 500 名用户的 Beta 测试中，Fugu Ultra 在数据科学到网络安全评估的自动化任务中展示了几乎无需人工干预的持续工作能力。
  article_id: 14d95bec95cebb8d
- object_type: project
  name: AutoResearch
  canonical_name: AutoResearch
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - 研究团队使用 AutoResearch 工具让 Fugu Ultra 自主改进小型 GPT 模型的训练方案，在单张 H100 GPU 上运行了超过 100
    次实验。
  article_id: 14d95bec95cebb8d
---

Fugu stands shoulder-to-shoulder with leading models like Fable and Mythos across the industry's most rigorous engineering, scientific, and reasoning benchmarks.

Beyond Bigger Models: Why are Orchestration Models the Next Frontier

Progress in AI has been driven largely by giant, monolithic models. But the most powerful systems of the future will be collaborative ecosystems.

Today, this orchestration is no longer just a technical optimization. It has become a geopolitical and operational imperative.

For an organization or a nation, relying on a single company's model for critical infrastructure, finance, or governance is a material vulnerability. This risk is no longer a hypothetical possibility, but a reality.

As we have seen with recent export controls imposed on models like Fable and Mythos, access can disappear overnight.

Collective intelligence is the practical hedge against this concentration of power. Because Fugu orchestrates an underlying pool of swappable agents, it simply routes around vendor restrictions.

By orchestrating the world’s models, we are delivering the resilient blueprint required for true AI sovereignty.

How does it work?

Sakana Fugu is itself an LLM, trained to call various LLMs in an agent pool, including instances of itself recursively. Fugu dynamically orchestrates the world's best models to tackle complex, multi-step tasks.

As shown in this figure, Fugu is a multi-agent system that behaves like a single model. You send a request to one endpoint, and Fugu decides how to handle it internally.

Fugu manages model selection, delegation, verification, and synthesis automatically. It solves tasks directly when that is enough, or coordinates a team of expert models when a problem calls for more. The complexity of a multi-agent system never reaches your code.

At launch, Sakana Fugu comes in two models accessed via a single OpenAI-compatible API:

• Fugu balances strong performance with low latency for everyday work. It fits naturally into tools like Codex for coding, as well as chatbots and interactive services. You can also opt specific agents out of its pool for data compliance.

• Fugu Ultra is our flagship model tuned for maximum answer quality on hard, multi-step problems. It coordinates a deeper pool of expert agents for demanding work like AI research, cybersecurity analysis, and patent investigations.

Benchmarks tell only part of the story.

Fugu’s real value shows up in long, messy, real-world workflows. During our beta with 500 users, we saw Fugu Ultra drive meaningful progress in fully automated tasks from data science to complete cybersecurity assessments.

Our early users saw Fugu explore, interpret failures, and sustain progress with almost zero human intervention. The feedback has been incredible. Here is what they are saying:

Use Case 1: Autonomous ML Research

Can an AI autonomously improve another AI’s training recipe?

We tasked Fugu Ultra with improving a small GPT model using AutoResearch. Over 14 hours on a single H100 GPU, Fugu ran > 100 experiments. It iteratively edited the training code, ran tests, and kept any changes that successfully lowered the validation error rate.

Watch the animation. The callouts track every time Fugu Ultra autonomously discovered a new improvement across batch size, model depth, learning rates, and optimizer settings.

We pitted Fugu against three frontier models (Gemini 3.1 Pro, Opus 4.8, and GPT 5.5). To keep the focus purely on agentic behavior rather than brand wars, we anonymized them as Models A, B, and C.

The Results:

• Fugu Ultra (bold red) finished with the best mean performance (0.9774).
• Fugu Ultra also achieved the best single run of the entire experiment (0.9748), leading every single baseline.

For long horizon, agentic ML research, using Fugu to dynamically orchestrate a pool of strong models significantly outperforms relying on any individual monolithic model.

Use Case 2: Financial Time Series Prediction

Can an AI agent navigate sequential, no-look-ahead market decisions?

Just for fun, we tested Fugu Ultra on 50 weeks of historical data for an anonymized equity (STOCK_X). Starting with $10,000, the agent processes weekly market data (prices, volume, moving averages, volatility) and decides whether to buy, hold, or sell.

After each action, the next week's price is revealed. The model must adapt purely from feedback, without ever seeing the future.

The Results across five identical 50-week runs:

• Fugu Ultra grew the portfolio to $11,943.22 (a +19.43% mean return).
• The other frontier models (Models A, B, and C) all capped out at less than a +15% return.

(Mandatory disclaimer: Past performance does not guarantee future results, and results may not transfer to other assets, time periods, or live markets.)

Use Case 3: One-Shot Blindfold Chess

Can an AI hold an entire game state in memory without drifting?