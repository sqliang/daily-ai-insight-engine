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
tldr: Sakana 发布 Fugu 多智能体编排模型，通过动态协调多个 LLM 提升复杂任务表现。
objective_summary: Sakana 发布 Fugu 和 Fugu Ultra 两款多智能体编排模型，本身是一个 LLM，能动态调用包括自身在内的多个
  LLM 组成智能体池。在自主 ML 研究中，Ultra 版 14 小时运行超 100 次实验，均分 0.9774 优于匿名前沿模型。在金融预测中实现 +19.43%
  收益。
event_type: framework_tools
epistemic_status: pr_statement
entities:
  companies:
  - Sakana
  technologies:
  - Fugu
  - Fugu Ultra
  - LLM
  - multi-agent system
  - AutoResearch
  key_people: []
key_logic_flow:
- Sakana 发布 Fugu 系列多智能体编排模型，Fugu 本身是一个 LLM，能够动态调用包括自身在内的多个 LLM 组成智能体池来处理任务。
- 用户只需向一个 OpenAI 兼容 API 端点发送请求，Fugu 自动完成模型选择、委派、验证和合成，无需开发者感知底层多智能体复杂性。
- Fugu 系列包含两个版本：标准版侧重性能与低延迟，Ultra 版针对高难度多步骤任务优化。
- 在自主 ML 研究测试中，Fugu Ultra 在 14 小时单 H100 GPU 上自主运行超 100 次实验迭代改进训练代码，均分 0.9774 优于 Gemini
  3.1 Pro、Opus 4.8 和 GPT 5.5 三个匿名前沿模型。
- 在金融时序预测测试中，Fugu Ultra 将初始 10000 美元增长至 11943.22 美元（+19.43% 平均回报），其他模型均低于 +15%。
extract_result: success
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