---
title: Redeploying Fable 5
source: https://www.anthropic.com/news/redeploying-fable-5
author: []
published: '2026-07-01'
created: '2026-07-01'
description: ''
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: fdd9745edc3aad4e
manifest_dates:
- '2026-07-01'
- '2026-07-02'
- '2026-07-03'
- '2026-07-04'
- '2026-07-05'
- '2026-07-06'
- '2026-07-07'
- '2026-07-08'
source_type: tech_blog
tldr: 美国出口管制解除后，Anthropic 宣布 Claude Fable 5 于7月1日起面向全球用户恢复可用，Claude Mythos 5 已向部分美国组织恢复访问，并正与政府协调扩大
  Glasswing 项目的合作伙伴范围。
objective_summary: Anthropic 于6月30日宣布，美国政府对 Claude Fable 5 和 Claude Mythos 5 实施的出口管制已解除。Fable
  5 将于7月1日起面向全球用户通过 Claude Platform、Claude.ai、Claude Code 和 Claude Cowork 重新上线，并在
  AWS、Google Cloud 和 Microsoft Foundry 上尽快恢复。Mythos 5 已于6月26日获美国政府批准，恢复对一批美国组织的访问权限。Anthropic
  正与 Amazon、Microsoft、Google 等 Glasswing 合作伙伴共同开发行业统一的越狱评估框架，并深化与美国政府在预发布测试、信息共享和研究协作方面的合作。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - Anthropic
  - Amazon
  - Microsoft
  - Google
  technologies:
  - Claude Fable 5
  - Claude Mythos 5
  key_people: []
key_logic_flow:
- 6月12日，美国政府对 Anthropic 最新模型 Claude Fable 5 和 Claude Mythos 5 实施出口管制，要求限制外国人访问，Anthropic
  因此暂停了所有用户对这两个模型的访问权限。
- 截至6月30日，美国政府对 Fable 5 和 Mythos 5 的出口管制已正式解除。
- Fable 5 将于7月1日起面向全球用户恢复可用，覆盖 Claude Platform、Claude.ai、Claude Code 和 Claude Cowork
  等平台，并在之后尽快在 AWS、Google Cloud 和 Microsoft Foundry 上恢复。
- Mythos 5 已于6月26日获美国政府批准，恢复了对一批美国组织的访问权限，Anthropic 正与政府协调扩大 Glasswing 项目的国内外合作伙伴范围。
- Anthropic 联合 Amazon、Microsoft、Google 等 Glasswing 合作伙伴，共同开发行业统一的越狱评估框架和严重性判定标准。
- Anthropic 正在深化与美国政府在预发布测试、信息共享和研究协作方面的合作。
extract_result: success
object_mentions:
- object_type: model
  name: Claude Fable 5
  canonical_name: Claude Fable 5
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Fable 5 将于7月1日起面向全球用户在 Claude Platform、Claude.ai、Claude Code 和 Claude Cowork 上重新可用。
  - Fable 5 与 Mythos 5 共享同一底层模型，但 Fable 5 配备了更强的安全防护措施以适用于通用场景。
  - 受美国出口管制影响，Fable 5 曾于6月12日起暂停对所有用户的访问权限。
  article_id: fdd9745edc3aad4e
- object_type: model
  name: Claude Mythos 5
  canonical_name: Claude Mythos 5
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Mythos 5 的安全防护较少，仅向少量受信任的 Project Glasswing 合作伙伴开放用于防御性网络安全场景。
  - 美国政府在6月26日批准后，Mythos 5 已恢复向一批美国组织提供访问权限。
  - Anthropic 正与政府协调，以扩大 Mythos 5 在 Glasswing 项目中面向更多国内外合作伙伴的访问范围。
  article_id: fdd9745edc3aad4e
- object_type: project
  name: Project Glasswing
  canonical_name: Project Glasswing
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Project Glasswing 是 Anthropic 与少量受信任合作伙伴共同参与的防御性网络安全项目，Mythos 5 仅向该项目合作伙伴开放。
  - Anthropic 正与 Amazon、Microsoft、Google 等 Glasswing 合作伙伴共同开发行业统一的越狱评估框架。
  - Anthropic 将继续与政府协调，以扩大 Glasswing 项目的国内外合作伙伴范围。
  article_id: fdd9745edc3aad4e
---

# Redeploying Fable 5

On Friday, June 12, the US government applied export controls to our newest models, Claude Fable 5 and Claude Mythos 5. This required us to restrict access to foreign nationals, whether inside or outside the United States. Because the order took effect immediately and we had no reliable way to verify nationality in real-time, we suspended access to both models for all users.

**As of today, June 30, the export controls on Fable 5 and Mythos 5 have been lifted.**

Fable 5 will be available starting tomorrow, Wednesday, July 1, to users globally on the Claude Platform, Claude.ai, Claude Code, and Claude Cowork. For Pro, Max, Team, and select Enterprise plans,1 Fable 5 will be included for up to 50% of weekly usage limits through July 7, after which it will be available via usage credits. We will re-enable access on AWS, Google Cloud, and Microsoft Foundry as quickly as possible.

We have also restored access to Mythos 5 for a set of US organizations, following the US government’s approval on June 26. We continue to coordinate with the government to expand access to the broader set of domestic and international partners in the Glasswing program.

In the remainder of this post, we provide further details and updates in four areas:

*A timeline of events, including updates we made to our safeguards*. We discuss the events that led to the export control directive and how we addressed it with new safeguards.*Our general approach to safeguards*. We provide more context on how we use safety classifiers to detect potentially dangerous cybersecurity uses of our models.*A shared industry framework*. Although we have reached a constructive resolution, these events have made clear that the industry needs a consistent way to assess and fix potential “jailbreaks” of AI models (techniques that bypass a model’s safeguards).2A shared standard for judging the severity of a given jailbreak would help AI developers triage new findings as they arise, launch highly capable models with greater safety, and communicate the level of risk consistently to government and industry partners. Together with Amazon, Microsoft, Google, and other Glasswing partners, we’ve started to develop such a framework, and we outline it below.*Deeper government collaboration*. We’re also strengthening our level of collaboration with the US government on new pre-release testing, information sharing, and research collaboration. We describe this deeper collaboration in the final section.

## Timeline and safeguard updates

We released Fable 5 and Mythos 5 on Tuesday, June 9. They both share the same underlying model, but Fable 5 was released with strong safeguards to make it safer for general use. Mythos 5, which has fewer safeguards, was only released to a small number of trusted Project Glasswing partners for use in defensive cybersecurity.