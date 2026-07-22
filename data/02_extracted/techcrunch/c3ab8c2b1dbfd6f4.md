---
title: Cybersecurity researchers aren’t happy about the guardrails on Anthropic’s
  Fable
source: https://techcrunch.com/2026/06/10/cybersecurity-researchers-arent-happy-about-the-guardrails-on-anthropics-fable/
author:
- '[[Lorenzo Franceschi-Bicchierai]]'
published: '2026-06-10'
created: '2026-06-11'
description: Cybersecurity researchers are complaining that Anthropic's new model
  Fable has guardrails that are too strict for any cybersecurity work.
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: c3ab8c2b1dbfd6f4
source_type: news_media
tldr: Anthropic 发布 Fable 模型作为网络安全模型 Mythos 的公开受限版本，因其基于关键词的过度防护机制触发安全无关请求被拒，引发网络安全研究人员的广泛批评。
objective_summary: Anthropic 于 2026 年 6 月发布了 Fable 模型，定位为 Mythos 的公开受限版本。当用户请求涉及网络安全或生物学领域时，Fable
  的防护机制会暂停对话并回退到 Claude Opus 4.8。IBM X-Force 研究员 Valentina Palmiotti 指出连阅读博客文章都会被阻止，Tolmo
  的 Matt Suiche 认为防护机制基于关键词且过于敏感但可以理解。Mythos 于四月通过 Project Glasswing 项目限量发布，上周已扩展到
  15 个国家的数百家组织。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - Anthropic
  - IBM X-Force
  - Tolmo
  technologies:
  - Fable
  - Mythos
  - Claude Opus 4.8
  key_people:
  - Valentina Palmiotti
  - Matt Suiche
  - Lorenzo Franceschi-Bicchierai
key_logic_flow:
- Anthropic 发布了 Fable 模型，将其定位为网络安全模型 Mythos 的公开且功能受限的版本。
- Fable 内置基于关键词的防护机制，会阻止任何与网络安全或生物学相关的请求，触发时暂停对话并回退到 Claude Opus 4.8。
- IBM X-Force 研究员 Valentina Palmiotti 批评 Fable 连阅读博客文章这类无害任务也会被错误拦截。
- Mythos 于四月通过 Project Glasswing 项目限量发布给少数组织，上周已扩展到 15 个国家的数百家组织。
- Tolmo 的 Matt Suiche 认为防护机制过于敏感但可以理解，早期宁可误杀过多也不放过是合理的，机制会随时间逐步放宽。
- 有多位网络安全专家在 X 平台上抱怨，即使是请求代码审查这种常规任务也会触发 Fable 的防护机制。
extract_result: success
object_mentions:
- object_type: product
  name: Fable
  canonical_name: Anthropic Fable
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Anthropic 发布了最新模型 Fable，将其定位为强大的网络安全模型 Mythos 的公开且功能受限的版本。
  - Fable 的防护机制会阻止任何可能涉及网络安全或生物学的请求，触发时暂停对话并回退到 Claude Opus 4.8。
  - 网络安全研究人员批评 Fable 的防护机制过于激进，连阅读博客文章或代码审查等无害任务都会被阻止。
  article_id: c3ab8c2b1dbfd6f4
- object_type: product
  name: Mythos
  canonical_name: Anthropic Mythos
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Anthropic 于四月发布了网络安全模型 Mythos，并通过 Project Glasswing 项目限制为少数组织使用。
  - 上周 Anthropic 将 Mythos 的访问权限扩展到 15 个国家的数百家组织，用于保护关键软件和基础设施。
  - Fable 被定位为 Mythos 的公开且功能受限的版本，作为更广泛的安全防护措施的一部分。
  article_id: c3ab8c2b1dbfd6f4
- object_type: project
  name: Project Glasswing
  canonical_name: Project Glasswing
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Anthropic 通过 Project Glasswing 项目将 Mythos 部署于关键软件和基础设施的安全防护。
  - Project Glasswing 最初将 Mythos 的访问限制在少数公司和组织范围内。
  article_id: c3ab8c2b1dbfd6f4
- object_type: product
  name: Claude Opus 4.8
  canonical_name: Claude Opus 4.8
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 当 Fable 触发防护机制时，会回退到 Claude Opus 4.8 模型继续对话。
  article_id: c3ab8c2b1dbfd6f4
---

Anthropic released its latest model Fable on Tuesday, billing it as a public and limited version of its powerful and much-hyped cybersecurity model Mythos.

But not everyone is happy with the restrictions, and a number of cybersecurity researchers and professionals have aired complaints online.

“[Fable] rejects any request that could be tangentially cyber related. Even innocuous tasks like reading a blog post,” said Valentina “Chompie” Palmiotti, a well-known security researcher who works at IBM X-Force.

When a prompt triggers its guardrails, Fable pauses the chat and says that its “safety measures flagged this message for cybersecurity or biology topics.”

The guardrails were put in place to limit the risk that Fable could be used to develop malware or compromise software — a long-standing concern within Anthropic. The restrictions on biology come from a similar concern around developing biological weapons.

When the AI giant released Mythos in April, it restricted the model to a limited number of companies and organizations in what it called Project Glasswing, an effort to deploy the model to secure critical software and infrastructure. Last week, Anthropic expanded access to Mythos to hundreds of organizations in 15 countries.

But despite the good intentions, many cybersecurity experts are still put off by the haphazard nature of the restrictions. Matt Suiche, a cybersecurity veteran, told TechCrunch that “if you ask it to write secure code, it assumes it is cybersecurity related work instead of software engineering best practices, and you get downgraded.” Fable is programmed to fall back to Claude Opus 4.8 if it hits a guardrail. “It seems to be keyword based, so anything in the lexical field of ‘cybersecurity’ triggers the guardrails.”


#### Contact Us

Do you have more information about how hackers are using AI? Or how cybersecuity companies are using AI? We’d love to hear from you. From a non-work device and network, you can contact Lorenzo Franceschi-Bicchierai securely on Signal at +1 917 257 1382, or via Telegram and Keybase @lorenzofb, or email.“But it is understandable as we are still in the early days and they are still adapting their guardrails. I am sure they are going to evolve over time as Anthropic and other frontier model companies will collaborate more with the current new generation of cybersecurity companies,” said Suiche, who is a member of the technical staff at Tolmo, an AI cybersecurity startup. “It’s better to catch more people than not enough when you do such a release and to relax the guardrails over time.”

Another researcher griped on X that “even asking for a code review” triggers Fable’s guardrails.

Anthropic did not immediately respond to a request for comment.