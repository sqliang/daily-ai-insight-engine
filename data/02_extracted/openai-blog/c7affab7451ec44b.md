---
title: Building self-improving tax agents with Codex
source: https://openai.com/index/building-self-improving-tax-agents-with-codex
author: []
published: '2026-05-27'
created: '2026-05-28'
description: See how OpenAI, Thrive, and Crete built a self-improving tax agent with
  Codex, automating filings, improving accuracy, and accelerating workflows.
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: c7affab7451ec44b
source_type: tech_blog
tldr: OpenAI 与 Thrive Holdings 合作，基于 Codex 为克里特岛 30 多家会计事务所构建了 Tax AI 系统。在试点季度中处理了
  7,000 份纳税申报表，节省约三分之一的时间，准确率高达 97%，吞吐量提升约 50%，且系统通过闭环反馈实现了持续的自主改进。
objective_summary: OpenAI 与 Thrive Holdings 历经六个月合作，为克里特岛 30 多家会计事务所开发了 Tax AI 系统，用于自动化
  1040 和 1041 纳税申报准备。该系统基于 Codex 的智能体能力，将生产环境中的反馈转化为结构化信号，驱动模型无需工程师介入即可自主改进。在试点季度中，Tax
  AI 处理了 7,000 份申报表，节省从业人员约三分之一的准备时间，准确率达 97%，吞吐量提升约 50%。上线时仅 25% 的申报表达到 75% 字段正确率，六周内该比例跃升至
  86%。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - OpenAI
  - Thrive Holdings
  technologies:
  - Codex
  key_people: []
key_logic_flow:
- OpenAI 与 Thrive Holdings 合作六个月，为克里特岛 30 多家会计事务所构建 Tax AI 系统，以解决纳税申报中手动数据录入的效率瓶颈。
- Tax AI 利用 Codex 的智能体能力，将生产使用中的反馈转化为结构化信号，实现系统的自主持续改进，无需工程师逐个排查故障。
- 在试点季度中，Tax AI 处理了 7,000 份 1040 和 1041 纳税申报表，自动完成大部分耗时的数据录入和计算工作。
- 系统为从业人员节省约三分之一的纳税准备时间，申报表字段准确率高达 97%，整体吞吐量提升约 50%。
- 上线时仅 25% 的申报表达到 75% 字段正确率，六周内该比例提升至 86%，90% 和 100% 正确率指标也呈现类似的高速增长趋势。
extract_result: success
object_mentions:
- object_type: product
  name: Tax AI
  canonical_name: Tax AI (Thrive Holdings)
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Tax AI 在试点季度中处理了克里特岛会计事务所的 7,000 份纳税申报表，涵盖 1040 和 1041 表单类型。
  - 该系统为从业人员节省约三分之一的纳税准备时间，申报表准确率高达 97%，吞吐量提升约 50%。
  - 上线六周内，达到 75% 字段正确率的申报表比例从 25% 跃升至 86%，验证了系统的自主改进能力。
  article_id: c7affab7451ec44b
- object_type: product
  name: Codex
  canonical_name: Codex (OpenAI)
  url: null
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - OpenAI 前向部署工程师与 Thrive Holdings 团队利用 Codex 的智能体能力共同构建了 Tax AI 系统。
  - Tax AI 使用 Codex 将生产反馈转化为结构化信号，驱动系统无需工程师介入即可自主改进。
  article_id: c7affab7451ec44b
---

*How Thrive Holdings and OpenAI co-developed Tax AI for Crete accountants by fusing practitioner expertise with a Codex-driven loop*

Real-world systems behave differently in production than they do in a lab, breaking in ways that are hard to anticipate before deployment. Teams often discover those failures after launch, then spend weeks inspecting edge cases, adjusting prompts, and translating production feedback into durable product improvements. The feedback loop is manual and slow, and only improves when an engineer advances it. But today, with thoughtfully designed eval infrastructure, direct access to practitioners and real world environments, and the frontier agentic capabilities of Codex, you can build agents that self-improve.

In this post, we’ll unpack how we used Codex to build this type of agent. Over the past six months, OpenAI forward deployed engineers and researchers along with Thrive Holdings’ engineers collaborated to build Tax AI alongside and for __Crete__(opens in a new window)’s network of 30+ accounting firms to help prepare increasingly complex tax returns. Instead of relying on engineers to find and fix each failure, Tax AI uses Codex to turn production use into structured signals that fuel autonomous improvement.

Crete practitioners prepare tens of thousands of tax returns each season which requires working through millions of underlying documents. For medium- to large-complexity filings, data entry alone can take eight hours per return, often involving messy data sources, prior-year documents, and manual extraction and calculation. They pointed us to tax preparation as a significant bottleneck during the busiest stretch of tax season.

To solve this problem, Tax AI processed 7,000 tax returns across the Crete firms that participated in the pilot this tax season. The system automates much of the time-intensive process of preparing 1040 and 1041 tax returns, but even more compelling than the efficiency gains is that the system itself is measurably better than the version that was first deployed three months ago.

In Tax AI, practitioners upload source files along with any client-specific notes. Tax AI then creates a tax engine submission, ready for review. It saves practitioners about a third of their time on tax preparation, drafts returns with up to 97% accuracy, and increases throughput by about 50%, creating more room for them to spend time with clients.

We can quantify this improvement by understanding how accurately Tax AI can complete a return without needing correction later. We measure accuracy by checking what share of returns reach 75%, 90%, or 100% correct field completion. At launch, only a quarter of returns were at 75% correct field completion, but within six weeks, 86% hit that mark. The system showed even faster growth at the 90% and 100% correct field completion levels. These thresholds give us a practical view of how much practitioner follow-up different returns still require.