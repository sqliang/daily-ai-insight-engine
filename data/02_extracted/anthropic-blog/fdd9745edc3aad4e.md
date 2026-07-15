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
tldr: 美国解除对 Claude Fable 5 的出口管制，Anthropic 于7月1日重新部署该模型
objective_summary: 美国政府对 Anthropic 的 Claude Fable 5 和 Mythos 5 实施的出口管制于6月30日解除。Anthropic
  于7月1日向全球用户重新开放 Fable 5，覆盖 Claude 平台、Claude.ai、Claude Code 和 Claude Cowork。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - Anthropic
  - Amazon
  - Microsoft
  - Google
  - AWS
  - Google Cloud
  - Microsoft Foundry
  technologies: []
  key_people: []
key_logic_flow:
- 美国政府于6月12日对 Anthropic 的 Claude Fable 5 和 Claude Mythos 5 实施出口管制，Anthropic 因无法实时核实用户国籍而暂停了所有用户的访问
- 出口管制于6月30日解除，Fable 5 于7月1日起向全球用户重新开放，覆盖 Claude 平台、Claude.ai、Claude Code 和 Claude
  Cowork
- Fable 5 在 Pro、Max、Team 及部分 Enterprise 计划中，截至7月7日每周可用额度内免费使用，之后转为按用量计费
- Mythos 5 于6月26日获美国政府批准，已恢复对部分美国组织的访问权限，Anthropic 正争取扩大 Glasswing 项目合作伙伴的访问范围
- Anthropic 与 Amazon、Microsoft、Google 等 Glasswing 合作伙伴共同制定行业共享框架，用于统一评估和修复 AI 模型越狱问题的严重性分级
- Anthropic 正在加强与美国政府在新模型预发布测试、信息共享和研究协作方面的合作
extract_result: success
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