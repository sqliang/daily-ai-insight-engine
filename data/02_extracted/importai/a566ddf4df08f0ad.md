---
title: 'Import AI 463: Self-improving robots; a 10k Chinese GPU cluster; and an elegiac
  essay for the human era'
source: https://importai.substack.com/p/import-ai-463-self-improving-robots
author:
- '[[Jack Clark]]'
published: '2026-06-29'
created: '2026-06-30'
description: What eras bookend our interregnum?
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: a566ddf4df08f0ad
manifest_dates:
- '2026-06-30'
- '2026-07-01'
- '2026-07-02'
- '2026-07-03'
- '2026-07-04'
- '2026-07-05'
- '2026-07-06'
source_type: newsletter_rss
tldr: NVIDIA 发布了 ENPIRE 框架，这是一个让物理机器人能够像 AI agent 一样自主实验和学习的闭环系统。该系统包含自动评估和自动重置机制，每个工位配备两台
  I2RT 的 YAM 机械臂和一张 RTX 5090 显卡。
objective_summary: NVIDIA 研究人员开发了 ENPIRE 框架，这是一个用于物理机器人的自改进闭环系统。该框架包含四个核心模块：环境模块负责自动重置和验证，策略改进模块发起策略优化，rollout
  执行模块让多台物理机器人并行操作，进化模块由编码 agent 分析日志、查阅文献并改进训练代码。系统通过自动评估机制对每次实验进行评分，并通过自动重置将场景恢复到初始状态，从而大幅减少人工干预。每个实验工位配备两台
  I2RT 的 YAM 机械臂、一组摄像头和一台搭载 NVIDIA RTX 5090 的工作站。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - NVIDIA
  - I2RT
  technologies:
  - ENPIRE
  key_people: []
key_logic_flow:
- NVIDIA 研究人员开发了 ENPIRE 框架，这是一个让物理机器人实现自主实验和学习循环的软件框架。
- ENPIRE 包含四个核心模块：环境模块（自动重置和验证）、策略改进模块、rollout 执行模块（多台机器人并行操作）和进化模块（编码 agent 分析日志、查阅文献并改进代码）。
- 系统的两个关键部件是自动评估系统（对每次实验结果自动评分）和自动重置系统（将场景恢复到初始状态），两者均无需人工干预。
- 每个实验工位配备两台 I2RT 的 YAM 机械臂、一组摄像头和一台搭载 NVIDIA RTX 5090 的工作站。
extract_result: success
object_mentions:
- object_type: project
  name: ENPIRE
  canonical_name: NVIDIA ENPIRE
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - NVIDIA 研究人员开发了 ENPIRE 框架，这是一个用于物理机器人的闭环自改进系统，让机器人能够像 AI agent 一样进行自主实验和学习。
  - ENPIRE 包含环境模块、策略改进模块、rollout 执行模块和进化模块四个核心组件，通过自动评估和自动重置机制减少人工干预。
  - 该框架将物理机器人学习转化为可控的优化过程，agent 可以管理整个流程，从而最小化人力投入并允许进行公平的实验对比。
  article_id: a566ddf4df08f0ad
- object_type: product
  name: YAM (Yet Another Manipulator)
  canonical_name: I2RT YAM
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - 每个实验工位包含两台由 I2RT 公司提供的 YAM（Yet Another Manipulator）机械臂，采用固定双臂配置。
  - YAM 机械臂与一组摄像头和一台搭载 NVIDIA RTX 5090 的工作站共同组成 ENPIRE 系统的硬件基础设施。
  article_id: a566ddf4df08f0ad
---

# Import AI 463: Self-improving robots; a 10k Chinese GPU cluster; and an elegiac essay for the human era

### What eras bookend our interregnum?

Welcome to Import AI, a newsletter about AI research. Import AI runs on arXiv, cappuccinos, and feedback from readers. If you’d like to support this, please subscribe.

**NVIDIA sets up a crude self-improvement loop for real world robotics:**

*…What if you could take the best ideas from AI agents and put them into the real world?...*

Researchers with NVIDIA have developed ENPIRE, software to get physical robotics to go through the same kind of autonomous experimentation and execution loop that AI agents go through. The research gives us a taste of what it might look like for a superintelligence to attempt to use robots to instantiate itself in the physical world - though as with all things in robotics, the current examples are suggestive at best.

**What ENPIRE is:**The software is “a harness framework for coding agents that instantiates this physical feedback routine with four core modules: an Environment module (EN) for automatic reset and verification, a Policy Improvement module (PI) that launches policy refinement, a Rollout module (R) to evaluate policies with single or multiple physical robots operating in parallel, and an Evolution module (E) in which coding agents analyze logs, consult literature, improve training infrastructure and algorithm code to address failure modes”.

**ENPIRE works the same way that coding agents work - a scaffold supervises some physical robots**which are asked to complete tasks. The robots try to complete the tasks and attempt different strategies for completing stuff, trying and failing and learning. The system both evaluates their success and also resets itself when they fail. “This closed-loop system transforms real-world robot learning into a controllable optimization procedure that agents can manage, thus minimizing human effort while allowing fair ablations across training recipes and agent variants.”

Two of the key ingredients for making this work are an automatic evaluation system to help score “the outcome of each trial without human judgement”, as well as an automatic reset system which “returns the scene to a fresh initial state for the next trial”. (Both of these are tasks which have historically required lots of human effort, and it’s likely that more complicated tasks would also require human effort for evaluation and resets, so in some sense the complexity of tasks a system like this can attack is also defined by our ability to automatically evaluate and reset the system).

**Hardware details:**“Each station comprises two YAM (Yet Another Manipulator) arms from I2RT in a fixed bimanual configuration, a set of cameras, and a single workstation that runs the FastAPI server, policy inference, and the station’s agent.” Each workstation is running a NVIDIA RTX 5090.