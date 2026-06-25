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
tldr: Anthropic 发布 Fable 模型，因网络安全护栏过严遭研究人员批评。
objective_summary: Anthropic 于 2026 年 6 月发布网络安全模型 Fable，设置了严格的安全护栏限制网络安全和生物学相关请求。多名安全研究人员批评护栏基于关键词匹配过于宽泛，误伤正常安全工作。Fable
  触发护栏后会降级到 Claude Opus 4.8。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - Anthropic
  - IBM X-Force
  - Tolmo
  - OpenAI
  technologies:
  - Fable
  - Mythos
  - Claude Opus 4.8
  key_people:
  - Valentina "Chompie" Palmiotti
  - Matt Suiche
  - Lorenzo Franceschi-Bicchierai
key_logic_flow:
- Anthropic 发布了其最新网络安全模型 Fable，作为此前发布的 Mythos 模型的公开受限版本。
- Fable 设置严格的安全护栏，任何与网络安全或生物学相关的请求（如阅读博客、代码审查）都会触发护栏并降级到 Claude Opus 4.8。
- IBM X-Force 安全研究员 Palmiotti 指出，即便是阅读博客文章等无害任务也会被护栏拒绝。
- 网络安全专家 Suiche 批评护栏基于关键词匹配而非语义理解，请求编写安全代码也会被误判为网络安全工作而触发降级。
- Suiche 同时表示理解这种保守策略，认为 Anthropic 会在与新一代网络安全公司合作中逐步放宽护栏。
- Anthropic 通过 Cyber Verification Program 允许认证专业人士减少限制；OpenAI 有类似项目 Trusted Access
  for Cyber。
extract_result: success
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