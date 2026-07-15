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
tldr: AgentLens 是一款从完整执行轨迹评估编码 AI Agent 的开源基准框架。
objective_summary: AgentLens 是一个生产环境验证的编码 Agent 评估基准。它不满足于任务通过/失败的二元结果，而是评估整条执行轨迹——包括指令遵循、工具使用、自我验证、错误恢复和用户交互。形式化验证与
  LLM 轨迹评审相结合，为每次运行输出可读的评分解释。已开源。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies: []
  technologies:
  - AgentLens
  key_people: []
key_logic_flow:
- AgentLens 是一个面向交互式编码 Agent 的生产环境验证评估基准。
- 现有基准将 Agent 执行简化为单一通过/失败结果，AgentLens 则评估完整的执行轨迹。
- 评估维度涵盖指令遵循、工具使用、自我验证、错误恢复以及与用户的交互过程。
- 它结合形式化验证（有客观检查标准的情形）与 LLM 编写的轨迹评审及对比分析。
- 每次运行生成可读的评分解释，说明得分原因。
- 该基准已被用于诊断模型行为、比较 Agent 版本迭代以及在产品级夜间评估管线中捕获回归问题。
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