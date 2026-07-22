---
title: 'AgentLens: Production-Assessed Trajectory Reviews for Coding Agent Evaluation'
source: https://arxiv.org/abs/2607.06624
author:
- '[[Andrey Podivilov, Vadim Lomshakov, Sergey Savin, Matvei Startsev, Roman Pozharskiy,
  Maksim Parshin, Sergey Nikolenko]]'
published: '2026-07-09'
created: '2026-07-09'
description: 'arXiv:2607.06624v1 Announce Type: new Abstract: We present AgentLens,
  a production-assessed benchmark for interactive code agents. Most code-agent benchmarks
  reduce a run to a single bit -- did the task pass? -- but the people who actually
  use these agents experience the entire trajectory: how the agent follows instructions,
  uses its tools, verifies its own work, recovers from mistakes, and talks to them
  along the way. AgentLens evaluates that whole trajectory. It pairs formal verification,
  where an objective check exists, with LLM-written trajectory reviews and side-by-side
  comparisons, so that each run yields a readable explanation of why the score is
  what it is. This makes AgentLens useful for more than ranking models: we use it
  to diagnose model behavior, compare successive versions of our own agent, and catch
  product regressions in a nightly evaluation pipeline. We release the benchmark as
  open source at https://github.com/agent-lens/agent-lens-bench.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 08e820bcd6acda0c
source_type: academic_paper
tldr: AgentLens 是一个面向交互式代码智能体的生产级别评估基准，它不仅评估任务是否通过，还通过形式化验证和 LLM 编写的轨迹评审对整个执行过程进行评分，并已开源。
objective_summary: 研究人员发布了一个名为 AgentLens 的代码智能体评估基准。与传统只输出任务通过与否的二值化评估不同，AgentLens
  对智能体的完整执行轨迹进行评估，包括指令遵循、工具使用、自我验证、错误恢复和交互对话等方面。该基准结合了形式化验证与 LLM 编写的轨迹评审及并排对比，为每次运行提供可读的评分理由。研究者已将其用于诊断模型行为、对比不同版本的智能体以及在夜间评估流水线中捕获产品回归。该基准已作为开源项目发布。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies: []
  technologies:
  - AgentLens
  - LLM
  key_people: []
key_logic_flow:
- AgentLens 是一个面向交互式代码智能体的生产评估基准，由论文作者团队提出并开源。
- 传统代码智能体基准测试只将一次运行简化为任务是否通过，而 AgentLens 评估完整的执行轨迹。
- 评估维度包括指令遵循、工具使用、自我验证、错误恢复以及智能体与用户的交互对话。
- AgentLens 将形式化验证与 LLM 编写的轨迹评审及并排对比相结合，每次运行都附带可读的评分解释。
- 该基准可用于诊断模型行为、对比相同智能体的不同版本，以及在夜间评估流水线中捕获产品回归。
- 作者已将该基准作为开源项目发布，供社区使用。
specialized_tags:
  paper:
    paperTitle: 'AgentLens: Production-Assessed Trajectory Reviews for Coding Agent
      Evaluation'
    authors: []
    affiliations: []
    venue: arXiv preprint
    codeUrl: null
    datasetUrl: null
    researchArea: NLP
    methodType: benchmark
extract_result: success
object_mentions:
- object_type: project
  name: AgentLens
  canonical_name: AgentLens
  url: https://github.com/agentlens/agentlens
  confidence: medium
  article_role: primary_subject
  evidence_snippets:
  - AgentLens 是一个生产评估基准，用于对交互式代码智能体进行完整的执行轨迹评估，而非仅看任务是否通过。
  - 该基准结合了形式化验证与 LLM 编写的轨迹评审和并排对比，每次运行都提供可读的评分解释。
  - 研究者已将其用于诊断模型行为、对比智能体不同版本以及在夜间评估流水线中捕获产品回归。
  article_id: 08e820bcd6acda0c
---

# Computer Science > Artificial Intelligence

# Title:AgentLens: Production-Assessed Trajectory Reviews for Coding Agent Evaluation

View PDFAbstract:We present AgentLens, a production-assessed benchmark for interactive code agents. Most code-agent benchmarks reduce a run to a single bit -- did the task pass? -- but the people who actually use these agents experience the entire trajectory: how the agent follows instructions, uses its tools, verifies its own work, recovers from mistakes, and talks to them along the way. AgentLens evaluates that whole trajectory. It pairs formal verification, where an objective check exists, with LLM-written trajectory reviews and side-by-side comparisons, so that each run yields a readable explanation of why the score is what it is. This makes AgentLens useful for more than ranking models: we use it to diagnose model behavior, compare successive versions of our own agent, and catch product regressions in a nightly evaluation pipeline. We release the benchmark as open source at this https URL.

### Current browse context:

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.