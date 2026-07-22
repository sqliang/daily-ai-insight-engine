---
title: Cybersecurity researchers aren't happy about the guardrails on Anthropic's
  Fable
source: https://techcrunch.com/2026/06/10/cybersecurity-researchers-arent-happy-about-the-guardrails-on-anthropics-fable/
author:
- '[[speckx]]'
published: '2026-06-10'
created: '2026-06-11'
description: 'Article URL: https://techcrunch.com/2026/06/10/cybersecurity-researchers-arent-happy-about-the-guardrails-on-anthropics-fable/
  Comments URL: https://news.ycombinator.com/item?id=48478969 Points: 426 # Comments:
  378'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: c3ab8c2b1dbfd6f4
source_type: community_discussion
tldr: Anthropic 发布了其网络安全模型 Fable 的公开受限版本，但大量安全研究人员抱怨其基于关键词的防护栏过于严格，连阅读博客文章或代码审查等无害请求也会被拒绝。
objective_summary: 2026年6月10日，Anthropic 发布了 Fable 模型，作为其网络安全模型 Mythos 的公开受限版本。Fable
  内置了基于关键词的防护栏，涉及网络安全或生物学话题的请求会被触发并回退到 Claude Opus 4.8。多位安全研究人员公开抱怨防护栏过于敏感，称阅读博客文章和代码审查等任务也会被拒绝。Anthropic
  要求网络安全专业人士申请 Cyber Verification Program 以解除部分限制。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - Anthropic
  - IBM
  - Tolmo
  - OpenAI
  - TechCrunch
  technologies:
  - Fable
  - Mythos
  - Claude Opus 4.8
  key_people:
  - Valentina Palmiotti
  - Matt Suiche
  - Lorenzo Franceschi-Bicchierai
key_logic_flow:
- Anthropic 在周二发布了 Fable 模型，将其定位为网络安全模型 Mythos 的公开受限版本。
- Fable 内置了针对网络安全和生物学话题的关键词防护栏，触发时会自动回退到 Claude Opus 4.8 模型。
- IBM X-Force 安全研究员 Valentina Palmiotti 表示 Fable 拒绝任何可能与网络安全相关的请求，包括阅读博客文章等无害任务。
- Tolmo 安全专家 Matt Suiche 指出防护栏基于关键词匹配，连编写安全代码的请求也会被当作网络安全工作处理。
- Anthropic 要求网络安全专业人士申请 Cyber Verification Program 以获得更少限制的 Claude 访问权限，OpenAI 有类似的
  Trusted Access for Cyber 计划。
- Suiche 认为早期版本收紧防护栏比放宽更安全，Anthropic 可能会在后续迭代中逐步放松限制。
extract_result: success
object_mentions:
- object_type: model
  name: Fable
  canonical_name: Anthropic Fable
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Anthropic 于周二发布了最新模型 Fable，将其定位为网络安全模型 Mythos 的公开受限版本。
  - 安全研究员 Valentina Palmiotti 表示 Fable 拒绝任何可能与网络安全相关的请求，包括阅读博客文章等无害任务。
  - Fable 在触发防护栏后会回退到 Claude Opus 4.8，且防护栏基于关键词匹配检测网络安全相关话题。
  article_id: c3ab8c2b1dbfd6f4
- object_type: model
  name: Mythos
  canonical_name: Anthropic Mythos
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Anthropic 在四月发布 Mythos 时，通过 Project Glasswing 将其限制在有限的机构中使用，用于保护关键软件和基础设施。
  - 上周 Anthropic 将 Mythos 的访问权限扩大到 15 个国家的数百家组织。
  article_id: c3ab8c2b1dbfd6f4
- object_type: project
  name: Project Glasswing
  canonical_name: Project Glasswing
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - Anthropic 在四月发布 Mythos 时将其限定在 Project Glasswing 框架内，旨在将模型部署到保护关键软件和基础设施的场景中。
  article_id: c3ab8c2b1dbfd6f4
- object_type: model
  name: Claude Opus 4.8
  canonical_name: Claude Opus 4.8
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Fable 在触发防护栏后会自动回退到 Claude Opus 4.8 模型继续进行对话。
  article_id: c3ab8c2b1dbfd6f4
- object_type: project
  name: Cyber Verification Program
  canonical_name: Anthropic Cyber Verification Program
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - Anthropic 要求网络安全专业人士申请 Cyber Verification Program，获得批准后可减少使用 Claude 进行网络安全工作的限制。
  article_id: c3ab8c2b1dbfd6f4
- object_type: project
  name: Trusted Access for Cyber
  canonical_name: OpenAI Trusted Access for Cyber
  url: null
  confidence: low
  article_role: ecosystem_context
  evidence_snippets:
  - OpenAI 有类似的 Trusted Access for Cyber 计划，为网络安全专业人士提供受限较少的模型访问权限。
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

Apart from guardrails inside its models, Anthropic requires cybersecurity professionals to apply to the Cyber Verification Program. If they get approved, the applicants have fewer limitations on using Claude for cybersecurity work. OpenAI has a similar program called Trusted Access for Cyber.