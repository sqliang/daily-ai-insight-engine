---
title: Anthropic hands the public Mythos-class AI
source: https://www.therundown.ai/p/anthropic-hands-the-public-mythos-class-ai
author:
- '[[Zach Mink]]'
published: '2026-06-10'
created: '2026-06-10'
description: 'PLUS: Automate financial research with Dexter'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: d30a6feac51b8bdc
source_type: newsletter_rss
tldr: Anthropic 发布 Claude Fable 5，向公众开放其顶级 Mythos 系列模型，在几乎所有 AI 基准测试中达到最先进水平，显著超越
  Opus 4.8 和 GPT 5.5。该模型将在所有 Claude 订阅层级中可用至6月22日，之后转为按量计费。
objective_summary: Anthropic 于4月通过 Project Glasswing 向150多家合作伙伴提供了 Mythos Preview
  模型，随后于近日发布了面向公众的 Claude Fable 5。Fable 是 Mythos 的受限版本，在处理网络安全、生物学和化学等敏感主题查询时会自动路由到
  Opus 4.8 处理。Fable 在编码、推理和知识工作等基准测试中大幅超越 Opus 4.8 和 GPT 5.5，达到最先进水平。该模型在所有 Claude
  订阅层级中可用至6月22日，之后将转为按使用量计费模式，价格为每百万输入标记10美元、每百万输出标记50美元。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - Anthropic
  - Google
  - Perplexity
  - Harvard Business School
  technologies: []
  key_people: []
key_logic_flow:
- Anthropic 最初于4月通过 Project Glasswing 向150多家合作伙伴发布了 Mythos Preview 模型，当时未向公众开放。
- Anthropic 随后发布了 Claude Fable 5，这是 Mythos 系列的受限版本，首次向所有公众开放。
- Fable 在处理网络安全、生物学和化学等敏感话题时会将查询路由到 Opus 4.8，以此作为安全限制措施。
- Fable 在几乎所有主要 AI 基准测试中达到最先进水平，在编码、推理和知识工作等维度上大幅超越 Opus 4.8 和 GPT 5.5。
- Fable 在所有 Claude 订阅层级中可用至6月22日，之后将转为按量计费模式，价格为每百万输入标记10美元、每百万输出标记50美元。
- 同时，Mythos 5 也已向 Project Glasswing 合作伙伴发布，提供成本更低、限制更少的网络安全使用场景。
extract_result: success
object_mentions:
- object_type: product
  name: Claude Fable 5
  canonical_name: Claude Fable 5
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Anthropic 发布 Claude Fable 5，向公众开放其顶级 Mythos 系列模型，在几乎所有 AI 基准测试中达到最先进水平。
  - Fable 是 Mythos 的受限版本，处理网络安全、生物学和化学等敏感查询时自动路由到 Opus 4.8 处理。
  - Fable 在所有 Claude 订阅层级中可用至6月22日，之后将按每百万输入标记10美元、每百万输出标记50美元计费。
  article_id: d30a6feac51b8bdc
- object_type: model
  name: Mythos Preview / Mythos 5
  canonical_name: Mythos 5
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 4月的 Mythos Preview 仅向 Project Glasswing 的150多家合作伙伴提供，在主流操作系统和浏览器上暴露出严重缺陷。
  - Mythos 5 向 Anthropic 的 Project Glasswing 合作伙伴发布，提供比 Mythos Preview 成本更低、限制更少的网络安全使用场景。
  article_id: d30a6feac51b8bdc
- object_type: model
  name: Opus 4.8
  canonical_name: Opus 4.8
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Fable 将网络安全、生物学和化学等敏感主题的查询路由到 Opus 4.8 处理，作为安全限制措施。
  - Fable 在编码、推理和知识工作等基准测试中大幅超越 Opus 4.8，达到新的最先进水平。
  article_id: d30a6feac51b8bdc
- object_type: model
  name: GPT 5.5
  canonical_name: GPT 5.5
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Fable 在编码、推理、知识工作等基准测试中显示出对 GPT 5.5 的巨大优势，达到最先进水平。
  article_id: d30a6feac51b8bdc
- object_type: project
  name: Project Glasswing
  canonical_name: Project Glasswing
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 4月的 Mythos Preview 仅通过 Project Glasswing 向150多家受信合作伙伴提供。
  - Mythos 5 通过 Project Glasswing 向合作伙伴发布，提供更低的成本和更少的限制。
  article_id: d30a6feac51b8bdc
---

Good morning, AI enthusiasts. Frontier releases usually trigger a week of benchmark arguments. Anthropic's new model just launched into a class of its own.

After months of drama over a Mythos too powerful for the public, Fable arrives as the compromise — with scores that, for once, make "best model in the world" uncontroversial… Even if the guardrails and future access are.

P.S.The Rundown just took its first strategic investment from Electrify to expand our newsletter content and beyond. Read about the deal here and read Rowan’s founder reflections here.

The Rundown: Anthropic just released Claude Fable 5, opening its top Mythos tier to the public for the first time — with a new set of guardrails compared to the original Mythos Preview and performance that is state-of-the-art on nearly all AI benchmarks.

The details:

April's initial Mythos Preview was only available to 150+ vetted partners via Project Glasswing, surfacing serious flaws across major OS and browsers.

Fable is a more restricted version of Mythos, with queries on topics like cybersecurity, biology, and chemistry routed to Opus 4.8 instead.

Fable hits new highs across major benchmarks, showing massive gains over Opus 4.8 and GPT 5.5 on coding, reasoning, knowledge work, and more.

Mythos 5 releases to Anthropic’s Project Glasswing partners, providing less restrictive use on cybersecurity at lower costs than Mythos Preview.

Fable is available in all Claude subscription tiers until June 22, then it will flip to separate usage credits priced at $10 / M input and $50 / M output tokens.

Why it matters: Every lab calls its latest release "the best model in the world"… What's rare is the rest of the AI world actually seeming to agree. Fable/Mythos lived up to the hype on benchmarks, but the question now turns to broader cost and access, with lots of content restrictions and June 22 looming as the cutoff before the credit pain kicks in.

The Rundown: Google for Startups' immersive training program kicked off yesterday, but there is still time to jump in. Join founders and developers learning how to move beyond basic chatbots to build robust, production-ready AI agents.

As the live series continues, you will learn how to:

Build a "hero" application that solves real-world customer intelligence problems

Take an agent from prototype in Google AI Studio to deployment on Google Cloud

Implement Gemini Live voice AI, Multimodal RAG, and bidirectional Vision Agents

Apply production-ready patterns to your own agentic systems

Register now to catch up and join the rest of the live training series.

The Rundown: Perplexity and Harvard Business School published a study on how AI agents change knowledge work, comparing the company's Computer platform against Search to measure outputs, time saved, and task complexity between the two paths.

The details: