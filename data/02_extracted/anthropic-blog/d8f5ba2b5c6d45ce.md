---
title: Accelerating Scientific Research
source: https://www.anthropic.com/news/accelerating-scientific-research
author: []
published: '2026-08-27'
created: '2026-08-28'
manifest_dates:
- '2026-08-28'
- '2026-08-29'
description: ''
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: d8f5ba2b5c6d45ce
source_type: tech_blog
tldr: Anthropic 于 2025 年 10 月推出 Claude for Life Sciences，并通过 AI for Science 项目支持全球科研人员，其
  Opus 4.5 在科学类基准上显著提升。文章还介绍了斯坦福大学基于 Claude 的通用生物医学智能体 Biomni，它能整合数百种工具并覆盖超过 25 个生物学子领域。
objective_summary: Anthropic 于 2025 年 10 月推出 Claude for Life Sciences，这是一套连接器和技能套件，旨在让
  Claude 成为更好的科研协作工具。Anthropic 持续投入提升 Claude 的科研能力，Opus 4.5 在图表解读、计算生物学和蛋白质理解基准上显著改进，并通过
  AI for Science 项目向全球高影响力科研项目提供免费 API 额度。研究人员基于 Claude 构建的自定义系统覆盖实验规划、数据分析和项目压缩等科研全流程。斯坦福大学开发的
  Biomni 智能体平台将数百种生物医学工具整合为单一系统，支持自然语言请求，能在超过 25 个生物学子领域形成假设、设计实验方案并执行分析。
event_type: application_landing
epistemic_status: pr_statement
entities:
  companies:
  - Anthropic
  - Stanford University
  technologies:
  - Claude
  - Claude for Life Sciences
  - Opus 4.5
  key_people: []
key_logic_flow:
- Anthropic 于 2025 年 10 月推出 Claude for Life Sciences，这是一套连接器和技能套件，旨在让 Claude 成为更好的科研协作伙伴。
- Anthropic 持续投入将 Claude 打造为最具科研能力的模型，Opus 4.5 在图表解读、计算生物学和蛋白质理解基准上展现出显著改进。
- Anthropic 通过 AI for Science 项目为全球从事高影响力科研项目的研究人员提供免费 API 额度，并据此理解科学家使用 AI 的方式。
- 研究人员开发的自定义系统让 Claude 覆盖科研全流程，包括判断该做哪些实验、把通常耗时数月的项目压缩到数小时、在海量数据中发现人类容易忽视的模式。
- 斯坦福大学推出 Biomni 通用生物医学智能体平台，将数百种数据库、软件包和实验方案整合为单一系统，由 Claude 驱动的智能体自动导航。
- Biomni 支持研究者用自然语言提出请求并自动选择合适资源，能形成假设、设计实验协议，并在超过 25 个生物学子领域执行分析。
object_mentions:
- object_type: product
  name: Claude for Life Sciences
  canonical_name: Claude for Life Sciences
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Anthropic 于 2025 年 10 月推出 Claude for Life Sciences，这是一套连接器和技能套件，旨在让 Claude 成为更好的科研协作伙伴。
  article_id: d8f5ba2b5c6d45ce
- object_type: product
  name: Biomni
  canonical_name: Biomni
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Biomni 是斯坦福大学开发的通用生物医学智能体平台，将数百种工具、软件包和数据集整合为单一系统，由 Claude 驱动的智能体自动导航。
  article_id: d8f5ba2b5c6d45ce
- object_type: project
  name: AI for Science program
  canonical_name: Anthropic AI for Science
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Anthropic 通过 AI for Science 项目向全球从事高影响力科研项目的领先研究人员提供免费 API 额度。
  article_id: d8f5ba2b5c6d45ce
- object_type: model
  name: Opus 4.5
  canonical_name: Claude Opus 4.5
  url: null
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - Anthropic 表示 Opus 4.5 在图表解读、计算生物学和蛋白质理解基准上展现出显著改进，体现了其对科研能力的持续投入。
  article_id: d8f5ba2b5c6d45ce
extract_result: success
---

# How scientists are using Claude to accelerate research and discovery

Last October we launched Claude for Life Sciences—a suite of connectors and skills that made Claude a better scientific collaborator. Since then, we've invested heavily in making Claude the most capable model for scientific work, with Opus 4.5 showing significant improvements in figure interpretation, computational biology, and protein understanding benchmarks. These advances, informed by our partnerships with researchers in academia and industry, reflect our commitment to understanding exactly how scientists are using AI to accelerate progress.

We’ve also been working closely with scientists through our AI for Science program, which provides free API credits to leading researchers working on high-impact scientific projects around the world.

These researchers have developed custom systems that use Claude in ways that go far beyond tasks like literature reviews or coding assistance. In the labs we spoke to, Claude is a collaborator that works across all stages of the research process: making it easier and more cost-effective to understand which experiments to run, using a variety of tools to help compress projects that normally take months into hours, and finding patterns in massive datasets that humans might overlook. In many cases it’s eliminating bottlenecks, handling tasks that require deep knowledge and have previously been impossible to scale; in some it’s enabling entirely different research approaches than researchers have traditionally been able to take.

In other words, Claude is beginning to reshape how these scientists work—and point them towards novel scientific insights and discoveries.

## Biomni: a general-purpose biomedical agent with access to hundreds of tools and databases

One bottleneck in biological research is the fragmentation of tools: there are hundreds of databases, software packages, and protocols available, and researchers spend substantial time selecting from and mastering various platforms. That’s time that, in a perfect world, would be spent on running experiments, interpreting data, or pursuing new projects.

Biomni, an agentic AI platform from Stanford University, collects hundreds of tools, packages, and data-sets into a single system through which a Claude-powered agent can navigate. Researchers give it requests in plain English; Biomni automatically selects the appropriate resources. It can form hypotheses, design experimental protocols, and perform analyses across more than 25 biological subfields.