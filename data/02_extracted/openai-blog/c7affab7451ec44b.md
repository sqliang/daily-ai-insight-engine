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
tldr: OpenAI与Thrive Holdings利用Codex为Crete会计事务所构建自进化税务代理Tax AI，试点处理7000份税表，准确率达97%。
objective_summary: 过去六个月，OpenAI派驻工程师与Thrive Holdings合作，为Crete旗下30余家会计事务所开发Tax AI系统，用于自动处理1040和1041税表。系统利用Codex的智能体能力将生产使用转化为结构化信号以驱动自主改进。在试点中处理了7000份税表，节省约三分之一准备时间，
event_type: application_landing
epistemic_status: pr_statement
entities:
  companies:
  - OpenAI
  - Thrive Holdings
  - Crete
  technologies:
  - Codex
  - Tax AI
  key_people: []
key_logic_flow:
- Crete会计事务所的从业人员在税季高峰期间，中等至复杂税表的数据录入每份需耗时8小时，涉及数百万份底层文档、往年数据和手工提取计算，税务准备工作成为严重瓶颈。
- OpenAI与Thrive Holdings合作，将前沿部署工程师和研究员派驻至Crete网络，与一线从业人员直接协作开发Tax AI系统。
- Tax AI基于Codex的智能体能力构建，通过精心设计的评估基础设施、一线从业人员直接反馈和真实生产环境，将使用数据转化为结构化信号，实现系统的自主改进。
- 从业人员上传源文件和客户备注后，Tax AI自动创建税务引擎提交草案供审核，涵盖1040和1041类型税表的准备流程。
- 系统在试点期间处理了7000份税表，字段完成准确率从上线初期的25%（75%正确率阈值）在六周内提升至86%，90%和100%正确率阈值增长更快。
- 最终效果：节省约三分之一税务准备时间，草拟税表准确率最高达97%，吞吐量提升约50%。
---

*How Thrive Holdings and OpenAI co-developed Tax AI for Crete accountants by fusing practitioner expertise with a Codex-driven loop*

Real-world systems behave differently in production than they do in a lab, breaking in ways that are hard to anticipate before deployment. Teams often discover those failures after launch, then spend weeks inspecting edge cases, adjusting prompts, and translating production feedback into durable product improvements. The feedback loop is manual and slow, and only improves when an engineer advances it. But today, with thoughtfully designed eval infrastructure, direct access to practitioners and real world environments, and the frontier agentic capabilities of Codex, you can build agents that self-improve.

In this post, we’ll unpack how we used Codex to build this type of agent. Over the past six months, OpenAI forward deployed engineers and researchers along with Thrive Holdings’ engineers collaborated to build Tax AI alongside and for __Crete__(opens in a new window)’s network of 30+ accounting firms to help prepare increasingly complex tax returns. Instead of relying on engineers to find and fix each failure, Tax AI uses Codex to turn production use into structured signals that fuel autonomous improvement.

Crete practitioners prepare tens of thousands of tax returns each season which requires working through millions of underlying documents. For medium- to large-complexity filings, data entry alone can take eight hours per return, often involving messy data sources, prior-year documents, and manual extraction and calculation. They pointed us to tax preparation as a significant bottleneck during the busiest stretch of tax season.

To solve this problem, Tax AI processed 7,000 tax returns across the Crete firms that participated in the pilot this tax season. The system automates much of the time-intensive process of preparing 1040 and 1041 tax returns, but even more compelling than the efficiency gains is that the system itself is measurably better than the version that was first deployed three months ago.

In Tax AI, practitioners upload source files along with any client-specific notes. Tax AI then creates a tax engine submission, ready for review. It saves practitioners about a third of their time on tax preparation, drafts returns with up to 97% accuracy, and increases throughput by about 50%, creating more room for them to spend time with clients.

We can quantify this improvement by understanding how accurately Tax AI can complete a return without needing correction later. We measure accuracy by checking what share of returns reach 75%, 90%, or 100% correct field completion. At launch, only a quarter of returns were at 75% correct field completion, but within six weeks, 86% hit that mark. The system showed even faster growth at the 90% and 100% correct field completion levels. These thresholds give us a practical view of how much practitioner follow-up different returns still require.