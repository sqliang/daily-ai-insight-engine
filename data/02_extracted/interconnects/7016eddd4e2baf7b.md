---
title: Open and closed models are on different exponentials
source: https://www.interconnects.ai/p/open-and-closed-models-are-on-different
author:
- '[[Nathan Lambert]]'
published: '2026-06-01'
created: '2026-06-04'
description: Where marginally higher intelligence drives value, and where it doesn't.
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 7016eddd4e2baf7b
source_type: newsletter_rss
tldr: 闭源模型与开源模型处于不同发展曲线上。2026年初的编程代理产品首次证明市场愿为更高智能支付显著溢价。头部实验室（Anthropic、OpenAI、Google）需通过延迟开放最强模型、控制Token供应等策略来维持高利润率。
objective_summary: 文章分析认为闭源与开源AI模型处于不同的发展轨迹，核心经济分歧在于用户是否愿意为更优智能持续支付高额溢价。2026年初的编程代理产品在达到Opus
  4.5和Codex 5.2等模型智能阈值后，首次证明存在一个巨大市场愿意为更高模型智能支付高额溢价。头部闭源实验室将不得不采取延迟开放最强模型、控制Token供应等策略来保护高利润率场景，但短期内市场仍受算力供应限制和Token补贴驱动。
event_type: infrastructure_update
epistemic_status: theoretical_claim
entities:
  companies:
  - Anthropic
  - OpenAI
  - Google
  technologies:
  - coding agents
  key_people: []
key_logic_flow:
- 闭源模型与开源模型处于不同的发展曲线上，核心经济差异在于用户是否愿意为更高智能支付高额溢价。
- 2026年初的编程代理产品首次证明存在一个巨大的AI市场愿意为更优智能支付高额溢价。
- API业务的利润率将不可避免地下降，头部实验室需要通过延迟开放最强模型、控制Token供应和保护高利润率场景来应对。
- Claude Opus 4.5和OpenAI Codex 5.2等模型已经达到让编程代理改变用户使用习惯的智能阈值。
- 头部闭源实验室（Anthropic、OpenAI、Google）在给定成本下总能制造出最高效的智能模型。
- 闭源模型的垂直集成优势（硬件与软件整合）可以在任何提升模型性能的方向上体现，而开源模型需要适配多种不同的服务环境。
extract_result: success
object_mentions:
- object_type: model
  name: Opus 4.5
  canonical_name: Claude Opus 4.5
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 文章指出Opus 4.5是编程代理改变用户习惯的智能阈值之一，达到该阈值后用户在使用编程代理时的净产出明显提升。
  article_id: 7016eddd4e2baf7b
- object_type: model
  name: Codex 5.2
  canonical_name: OpenAI Codex 5.2
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 文章将Codex 5.2作为编程代理改变用户习惯的参考阈值，认为在该智能水平上代理已成为复杂知识工作的有效辅助工具。
  article_id: 7016eddd4e2baf7b
---

# Open and closed models are on different exponentials

### Where marginally higher intelligence drives value, and where it doesn't.

The largest debate that’ll define the future balance of power between the open and closed AI model ecosystems is primarily economic — it’s if users of AI will continue to pay dramatically more, i.e. large margins, for the top closed models. Early 2026 is a seminal time for the AI industry, as the coding agents1 have shown the first area where a huge AI market will continue to pay a substantial premium for better intelligence.

The other side of this dichotomy is the inevitable decay of API businesses at these same labs. These labs will realize they need to protect their best models, rolling them out later in APIs to both protect token supply, avoid distillation, and stick to use-cases with higher margins. All of these effects will be clearly visible in 5-10 year timelines, as in the near term markets, prices, margins, and demand will be dictated by a rapid buildout of compute (supply-limited in the near term) and mass subsidization of tokens (through continued investment in new AI companies).

The core of this argument rests in the obvious habit changes that are setting in with coding agents past the Opus 4.5 and Codex 5.2 thresholds. People are not making this switch because they are lazy, but because their net output is obviously higher when using an agent as an implementation aid for complex knowledge work. For people who rely on coding agents to work, they will always pay more for the best rather than settle for good enough. There are so many ways to make the product better, speed, intelligence, specialized models, etc.

I would pay $2000/month for the tools today, especially knowing they’ll get much better. At the same time, it is likely that many companies are forcing agents and usage onto people that actually will get very little out of them in their current form, which helps the AI buildout (or bubble) continue.

The best closed labs — right now this list is just Anthropic and OpenAI, but it’s reasonable to expect Google to catch up — will always make the most efficient models for intelligence at a given cost. Building models is a mass capital investment of talent, data, and compute. These systems, a combination of model weights, harnesses, tools, and serving infrastructure have massive returns on integration (where open models are designed to work across many, diverse serving situations). These integration benefits — the integration of hardware and new forms of software — can be expressed in any possible way of making models better.