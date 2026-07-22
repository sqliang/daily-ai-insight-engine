---
title: Claude Science, an AI Workbench for Scientists (4 minute read)
source: https://www.anthropic.com/news/claude-science-ai-workbench?utm_source=tldrai
author: []
published: ''
created: '2026-07-02'
description: TLDR AI 每日头条
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: e2cc0f4a4ecdec76
manifest_dates:
- '2026-07-02'
source_type: news_media
tldr: Anthropic 发布 Claude Science，一个面向科学家的 AI 工作台，整合了超过 60 种科学工具和技能，支持文献分析、多步研究执行和可复现工件的生成，兼容本地、SSH
  和 HPC 环境，即日起面向 Claude Pro、Max、Team 和 Enterprise 用户开放测试。
objective_summary: Anthropic 于 2026 年 7 月 22 日推出 Claude Science 测试版，这是一款集成科学研究的 AI
  工作台。该产品将 PubMed、Jupyter、R 等分散工具整合到单一环境中，提供超过 60 种预配置的基因组学、蛋白质组学、结构生物学等领域的技能和连接器。Claude
  Science 能生成附带完整代码和环境的可复现科学工件，管理 HPC 或 Modal 等计算资源的作业调度，并由评审代理自动检查引用和计算错误。产品支持 macOS、Linux
  本地运行，以及 SSH 远程或 HPC 登录节点部署。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - Anthropic
  - Modal
  technologies:
  - MCP
  - SSH
  - HPC
  key_people: []
key_logic_flow:
- Anthropic 推出 Claude Science，这是一款面向科学家的 AI 研究工作台产品，目前处于测试阶段。
- Claude Science 将 PubMed、Jupyter、R 等分散的研究工具整合到单一环境中，配备超过 60 种预配置的科学技能和连接器。
- 该平台能生成完全可复现的科学工件，包括 3D 蛋白质结构、基因组浏览器轨迹和化学结构等可视化内容。
- Claude Science 支持在本地、SSH 远程服务器或 HPC 集群上运行，敏感数据无需离开实验室自有基础设施。
- 产品内置评审代理，可自动检查引用准确性、计算错误和图表与代码的一致性，并进行自我修正。
- Claude Science 即日起向 Claude Pro、Max、Team 和 Enterprise 用户开放测试。
extract_result: success
object_mentions:
- object_type: product
  name: Claude Science
  canonical_name: Claude Science
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Anthropic 发布了 Claude Science 测试版，这是一个面向科学家的 AI 工作台，将研究所需的各类工具整合到单一环境中。
  - Claude Science 能够生成完全可复现的科学工件，包括 3D 蛋白质结构、基因组浏览器轨迹和化学结构等可视化内容。
  - Claude Science 支持在本地、SSH 远程服务器或 HPC 集群上运行，并自动管理计算资源的作业调度。
  article_id: e2cc0f4a4ecdec76
---

AI has the potential to dramatically accelerate the pace of scientific discovery and the development of healthcare interventions. Since launching our efforts in the life sciences last fall, we’ve worked to improve our model capabilities, make connections to the scientific ecosystem via MCPs and skills, and launch partnerships in an effort to realize this potential.

Today, we’re introducing our most significant expansion of these efforts: Claude Science, an AI workbench for scientists. Claude Science is an app that integrates the tools and packages that researchers most commonly use, produces auditable artifacts, and provides flexible access to computing resources.

## Introducing Claude Science

Scientific research is often tedious. Researchers must work across dozens of databases, each with their own schema, contend with file formats that require bespoke data pipelines and viewers, and transition between a roster of tools: PubMed, Jupyter, R, a cluster terminal, and more.

Claude Science brings these fragmented tools into a single research environment where scientists can conduct all stages of their work. It helps you analyze literature and execute multi-step research, produces detailed artifacts, and lets you iteratively refine figures and manuscripts until they’re ready for publication. Every output carries an auditable history of how it was made, so you can validate and reproduce the results. Like a Jupyter Notebook, you can access Claude Science wherever you already work—locally on macOS or Linux, or on a remote machine over SSH or with an HPC login node.

Users interact with a generalist coordinating agent with access to over 60 curated skills and connectors pre-configured for genomics, single-cell, proteomics, structural biology, cheminformatics, and more. These agents can spin up others and engage with specialist agents created by users. And a reviewer agent checks citations and calculations, flagging and correcting errors.

We are releasing Claude Science today in beta for Claude Pro, Max, Team, and Enterprise users, and will continue to refine the platform as we collect feedback from users.

**How it works**

**Rich scientific artifacts, fully reproducible. **Scientific research is inherently visual, so Claude Science generates figures and manuscripts alongside the code that created them. It natively renders rich scientific artifacts, including 3D protein structures, genome browser tracks, chemical structures, and more. You can chat with the agent about any detail, annotating figures and manuscripts in-line so the agent knows what to address to make them publication-ready.

When it generates a figure, Claude Science includes the exact code and environment that produced it, a plain-language description of how it was created, and the full message history. This allows you to understand the inputs, making the work easier to validate and reproduce even months later. You can ask Claude Science to make edits to figures in plain language—removing gridlines, for example, or changing an axis to log scale—and the agent will edit its own code.

**Manages your compute and scales on demand. **Large analyses—folding a protein, for example, or running a genomics pipeline over a massive dataset—often require researchers to shift their focus to setting up a computing job, waiting while it’s sent to a cluster, checking whether it succeeded or failed, and pulling the results back. Claude Science handles this process for you. It drafts a plan, asks before reaching new resources, and lets you review or revoke any decision before writing and submitting the job to the computing resources your lab already uses (your own HPC cluster over SSH, or your Modal account for compute on demand), scaling the analysis from a single GPU to hundreds as needed.

Because its agents work inside a running session that holds context in memory, even massive datasets only need to be loaded once. It runs on your lab’s own infrastructure—your laptop, Linux box, or HPC login node—so large or sensitive datasets never have to leave the systems they’re already on, and only the context needed for each step of the analysis is sent to Claude. As the pipeline runs, a reviewer agent inspects the outputs, flagging incorrect citations, untraceable numbers, and figures that don’t match their underlying code, and self-correcting as it goes. You can fork the session at any point to compare two approaches without losing the original thread.