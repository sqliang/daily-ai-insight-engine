---
title: harveyai/harvey-labs
source: https://github.com/harveyai/harvey-labs
author: []
published: ''
created: '2026-08-10'
manifest_dates:
- '2026-08-10'
- '2026-08-12'
description: 'A benchmark built to evaluate and improve agent capabilities for supporting
  legal work. Legal Agent Benchmark (LAB): An open-source benchmark for evaluating
  agents on real legal work. Harvey LAB is an open-source project aimed at benchmarking
  LLM agents'' abilities to perform legal work in realistic environments. LAB consists
  of two parts: a dataset of tasks containing agent instructions, documents, and rubrics
  as well as an execution harness for running and evaluating agents against those
  tasks. LAB is an ongoing project and we expect to consistently add to and refine
  the task set and execution harness. Read the announcement post: Introducing Harvey''s
  Legal Agent Benchmark Getting Started Start with the full walkthrough in docs/tutorial.md
  — it takes one realistic M&A data-room assignment end to end: setup, task inspection,
  agent run, scoring, report review, and comparison dashboards. Additional Documentation
  Guide Description Architecture Task model, harness, tools, adapters, reports, and
  sweeps Evaluation Methodology All-pass rubric scoring and LLM judge behavior Contributing
  Add tasks, model adapters, evaluation improvements, and docs Citation If you use
  Harvey LAB in your research, please cite it as: @misc{harveylab2026, title = {Harvey
  LAB: The Legal Agent Benchmark}, author = {{Harvey AI}}, year = {2026}, version
  = {v1.0}, url = {https://github.com/harveyai/harvey-labs/tree/v1.0}, note = {Announcement:
  \url{https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark}} }'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: b1dcbece28dae08b
source_type: community_discussion
tldr: Harvey AI 发布开源基准 Harvey LAB，用于在真实法律工作环境中评估 LLM 智能体的法律工作能力，由任务数据集与执行框架两部分构成，目前仍在持续迭代。
objective_summary: Harvey AI 于 2026 年发布开源项目 Harvey LAB（Legal Agent Benchmark），其目标是在真实法律工作场景中评估
  LLM 智能体的能力。LAB 由两部分组成：一是包含智能体指令、文档与评分量规的任务数据集，二是用于运行和评估智能体的执行框架。项目提供 M&A 数据室任务的端到端演练文档，采用全通过量规评分与
  LLM 评判员评估方法，并给出 v1.0 版本引用格式。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - Harvey AI
  technologies:
  - LLM
  - LLM agents
  - LLM-as-judge
  - Legal Agent Benchmark (LAB)
  key_people: []
key_logic_flow:
- Harvey AI 发布开源项目 Harvey LAB，用于在真实法律工作环境中评估 LLM 智能体的法律工作能力。
- LAB 由两部分构成：一个包含智能体指令、文档与评分量规的任务数据集，以及一个用于运行和评估智能体的执行框架。
- 项目文档提供 M&A 数据室任务的端到端演练，涵盖环境搭建、任务检查、智能体运行、评分、报告审阅与对比仪表盘。
- LAB 的评估方法采用全通过量规评分与 LLM 评判员行为，架构涉及任务模型、工具、适配器、报告与 sweeps。
- 该项目仍处于持续开发阶段，官方计划不断补充和优化任务集与执行框架，并已提供 v1.0 版本的学术引用格式。
object_mentions:
- object_type: project
  name: harveyai/harvey-labs
  canonical_name: Harvey LAB (Legal Agent Benchmark)
  url: https://github.com/harveyai/harvey-labs
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Harvey LAB 是 Harvey AI 发布的开源项目，用于在真实法律工作环境中评估 LLM 智能体的法律工作能力。
  - LAB 由两部分组成：一个包含智能体指令、文档与评分量规的任务数据集，以及一个用于运行和评估智能体的执行框架。
  - LAB 提供 M&A 数据室任务的端到端演练文档，并采用全通过量规评分与 LLM 评判员行为进行评测。
  - Harvey LAB 仍在持续开发中，官方计划不断补充任务集与执行框架，并已发布 v1.0 版本及对应引用格式。
  article_id: b1dcbece28dae08b
extract_result: success
---

**Legal Agent Benchmark (LAB): An open-source benchmark for evaluating agents on real legal work.**

Harvey LAB is an open-source project aimed at benchmarking LLM agents' abilities to perform legal work in realistic environments.

LAB consists of two parts: a dataset of *tasks* containing agent instructions, documents, and rubrics as well as an *execution harness* for running and evaluating agents against those tasks.

LAB is an ongoing project and we expect to consistently add to and refine the task set and execution harness.

Read the announcement post: Introducing Harvey's Legal Agent Benchmark

Start with the full walkthrough in **docs/tutorial.md** — it takes one realistic M&A data-room assignment end to end: setup, task inspection, agent run, scoring, report review, and comparison dashboards.

| Guide | Description |
|---|---|
| Architecture | Task model, harness, tools, adapters, reports, and sweeps |
| Evaluation Methodology | All-pass rubric scoring and LLM judge behavior |
| Contributing | Add tasks, model adapters, evaluation improvements, and docs |

If you use Harvey LAB in your research, please cite it as:

```
@misc{harveylab2026,
title = {Harvey LAB: The Legal Agent Benchmark},
author = {{Harvey AI}},
year = {2026},
version = {v1.0},
url = {https://github.com/harveyai/harvey-labs/tree/v1.0},
note = {Announcement: \url{https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark}}
}
```