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
tldr: Anthropic推出Claude Science，面向科学家的AI工作台
objective_summary: Anthropic于2026年7月15日发布Claude Science测试版，这是一个整合了60多种科学工具和连接器的AI工作台应用。它帮助科学家在单一环境中完成文献分析、多步骤研究设计、生成可重现的图文工件，并支持本地或远程HPC/SSH基础设施运行。
event_type: application_landing
epistemic_status: pr_statement
entities:
  companies:
  - Anthropic
  - Modal
  technologies:
  - MCP
  - HPC
  key_people: []
key_logic_flow:
- Anthropic 发布 Claude Science 测试版，这是一款面向科学家的 AI 工作台应用，旨在将分散的科学工具整合到单一研究环境中。
- 该应用内置 60 多种预配置的技能和连接器，覆盖基因组学、单细胞分析、蛋白质组学、结构生物学和化学信息学等领域。
- 用户通过通用协调代理与系统交互，该代理可调用专家代理和用户创建的自定义代理，并配备审核代理自动检查引用和计算错误。
- Claude Science 支持生成丰富的科学工件（3D 蛋白质结构、基因组浏览器轨迹、化学结构图等），每项输出附带完整的可追溯生成记录。
- 该应用可在 macOS/Linux 本地运行，也可通过 SSH 或 HPC 登录节点在远程基础设施上执行，敏感数据无需离开实验室自有系统。
- 计算任务可自动扩展（从单 GPU 到数百 GPU），审核代理在流水线运行中持续检查输出并自我修正错误。
extract_result: success
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