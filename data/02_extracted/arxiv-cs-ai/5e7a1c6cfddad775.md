---
title: 'Representation Affects Retrieval: A Case Study of Skill Discovery and Routing
  in a Multimodal Agent Harness'
source: https://arxiv.org/abs/2608.20389
author:
- '[[Kevin Dela Rosa]]'
published: '2026-08-24'
created: '2026-08-24'
manifest_dates:
- '2026-08-24'
description: 'arXiv:2608.20389v1 Announce Type: new Abstract: A production agent harness
  must discover and rank, from a growing library of skills, the one most appropriate
  for a user''s task. At small scale this selection happens in context: the LLM planner
  chooses among skill representations exposed in its system prompt, without an explicit
  embedding-based retrieval step. We treat this in-context selection as the small-N
  counterpart to embedding-based skill retrieval at scale, and present a case study
  of how Tinycloud, a production multimodal video agent harness, represents its skills
  for the planner. The harness ships skills under two recurring representations: tool-skills
  that wrap a single external API or system tool and serve as primitive vocabulary,
  and workflow-skills that orchestrate tool-skill calls plus a template render to
  produce one named deliverable. The harness exposes them via two surfaces in the
  system prompt: an inlined-body surface (full instructions, scripts, templates) for
  autoloaded skills, and a one-line listing for on-demand skills. A six-task selection
  ablation across three exposure regimes (all-on, default, all-off) shows that full
  autoload selects the gold skill on every task; all-off slows execution and produces
  hard discovery failures; and the production default misroutes one task because its
  lexical signal collides with an autoloaded tool-skill that pulls planner attention
  away from a listed workflow-skill. The headline finding is that in-prompt exposure
  of skills is not monotonically helpful: partial exposure can create lexical competition
  that suppresses correct selection. We connect this small-N observation to recent
  retrieval-based skill-routing work at large scale, and frame this contribution as
  a case study rather than a benchmark.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 5e7a1c6cfddad775
source_type: academic_paper
tldr: 论文以生产级多模态视频智能体 harness Tinycloud 为案例，研究技能表示如何影响 LLM 规划器的上下文内选择。六任务消融实验显示，提示词内技能暴露并非单调有益，部分暴露会造成词汇竞争并抑制正确路由选择。
objective_summary: 这篇 arXiv 论文以 Tinycloud 生产级多模态视频智能体 harness 为案例，研究技能表示对 LLM 规划器上下文内选择的影响。Tinycloud
  将技能分为封装单一外部 API 的工具技能与编排调用并生成命名交付物的流程技能，并通过内联正文与单行列表两种表面暴露给规划器。六任务消融实验对比全开、默认、全关三种暴露模式，结果显示全自动加载在每项任务上选中黄金技能，全关闭拖慢执行并产生硬性发现失败，而生产默认配置在一个任务上因词汇信号冲突而错误路由。论文的核心结论是技能暴露并非越多越好，并将这一小规模观察与大规模嵌入检索式技能路由研究联系起来。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - multimodal agent harness
  - tool-skills
  - workflow-skills
  - skill routing
  - embedding-based retrieval
  - LLM planner
  - in-context selection
  key_people: []
key_logic_flow:
- 论文以生产级多模态视频智能体 harness Tinycloud 为例，研究其技能在系统提示词中的表示方式如何影响 LLM 规划器的上下文内选择。
- Tinycloud 的技能分为两类：封装单一外部 API 或系统工具的工具技能，以及编排工具技能调用并渲染模板以产生命名交付物的流程技能。
- 系统提示词通过两种表面暴露技能：内联正文表面承载完整指令、脚本与模板用于自动加载技能，单行列表则用于按需技能。
- 六任务消融实验对比全开、默认、全关三种暴露模式，结果显示全自动加载在每项任务上都选中黄金技能，全关闭则拖慢执行并产生硬性发现失败。
- 生产默认配置在一个任务上发生错误路由，因为其词汇信号与自动加载的工具技能冲突，把规划器注意力从列出的流程技能上引开。
- 核心结论是提示词内技能暴露并非单调有益，部分暴露可能产生词汇竞争从而抑制正确选择，论文将其定位为案例研究而非基准评测。
object_mentions:
- object_type: project
  name: Tinycloud
  canonical_name: Tinycloud
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Tinycloud 是一个生产级多模态视频智能体 harness，论文以它为例研究技能表示对规划器选择的影响。
  - Tinycloud 将技能组织为工具技能与流程技能两类，并通过系统提示词中的内联正文与单行列表两种表面暴露给 LLM 规划器。
  - 针对 Tinycloud 的六任务消融实验表明，全自动加载在每项任务上都选中黄金技能，而生产默认配置会因词汇竞争错误路由一个任务。
  article_id: 5e7a1c6cfddad775
extract_result: success
---

# Computer Science > Artificial Intelligence

# Title:Representation Affects Retrieval: A Case Study of Skill Discovery and Routing in a Multimodal Agent Harness

View PDF HTML (experimental)Abstract:A production agent harness must discover and rank, from a growing library of skills, the one most appropriate for a user's task. At small scale this selection happens in context: the LLM planner chooses among skill representations exposed in its system prompt, without an explicit embedding-based retrieval step. We treat this in-context selection as the small-N counterpart to embedding-based skill retrieval at scale, and present a case study of how Tinycloud, a production multimodal video agent harness, represents its skills for the planner. The harness ships skills under two recurring representations: tool-skills that wrap a single external API or system tool and serve as primitive vocabulary, and workflow-skills that orchestrate tool-skill calls plus a template render to produce one named deliverable. The harness exposes them via two surfaces in the system prompt: an inlined-body surface (full instructions, scripts, templates) for autoloaded skills, and a one-line listing for on-demand skills. A six-task selection ablation across three exposure regimes (all-on, default, all-off) shows that full autoload selects the gold skill on every task; all-off slows execution and produces hard discovery failures; and the production default misroutes one task because its lexical signal collides with an autoloaded tool-skill that pulls planner attention away from a listed workflow-skill. The headline finding is that in-prompt exposure of skills is not monotonically helpful: partial exposure can create lexical competition that suppresses correct selection. We connect this small-N observation to recent retrieval-based skill-routing work at large scale, and frame this contribution as a case study rather than a benchmark.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.