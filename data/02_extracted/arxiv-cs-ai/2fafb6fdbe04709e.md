---
title: 'Mnemosyne: Agentic Transaction Processing for Validating and Repairing AI-generated
  Workflows'
source: https://arxiv.org/abs/2607.00269
author:
- '[[Edward Y. Chang, Longling Geng, Emily J. Chang]]'
published: '2026-07-02'
created: '2026-07-02'
description: 'arXiv:2607.00269v1 Announce Type: new Abstract: LLMs, solvers, and agent
  teams increasingly generate workflow actions, repairs, and plans, but a generated
  action may be syntactically valid yet stale, infeasible, conflicting, or destructive
  of the evidence that triggered a repair. We introduce Agentic Transaction Processing
  (ATP), a transaction model that treats generated actions as untrusted proposals
  until they pass deterministic admission under a declared, executable constraint
  set C. The principle is two-sided: a proposal is not truth, and no proposal foresees
  every disruption: anything may propose, but only the runtime admits and commits,
  and when an unforeseen disruption strikes it repairs reactively within bounds rather
  than trusting a fresh proposal. Relative to C, committed-state correctness becomes
  independent of the competence, honesty, or learning of the proposing layer. We realize
  ATP in Mnemosyne, a runtime with an append-only transition log, effective-state
  projection, dependency-safe compensation, and active commitment records, and prove
  four safety properties relative to C (authority separation, serial-equivalent generative
  admission, evidence-preserving repair, and obligation containment) together with
  a bounded-reactive-repair guarantee for its localized repair protocol (LCRP). A
  reproducible artifact rejects the targeted violations across nine falsification
  tests while still admitting valid work, at under 6% projection-and-validation overhead,
  and bounded local repair edits an order of magnitude fewer operations than global
  recompute. Mnemosyne is open source: https://github.com/eyuchang/Mnemosyne/tree/arxiv-atp-rq1-rq9b-r8-v2.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 2fafb6fdbe04709e
manifest_dates:
- '2026-07-02'
source_type: academic_paper
tldr: Mnemosyne 提出 Agentic 事务处理模型，用于验证和修复 AI 生成的 workflow。
objective_summary: 论文提出 Agentic Transaction Processing (ATP) 模型，将 AI 生成的操作视为未受信任的提案，需通过声明性约束集
  C 的确定性准入后才由运行时提交。Mnemosyne 运行时实现了追加日志、有效状态投影、依赖安全补偿和活跃提交记录，在9项测试中拒绝违规操作，
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - LLM
  - Agentic Transaction Processing (ATP)
  - Localized Constrained Repair Protocol (LCRP)
  key_people: []
key_logic_flow:
- AI 生成的操作存在语法正确但过时、不可行、冲突或破坏证据的问题，现有方法缺乏事务性安全保障。
- 论文提出 Agentic Transaction Processing (ATP) 模型，核心原则是任何组件都可提议，但仅运行时负责准入和提交。
- Mnemosyne 运行时实现 ATP 模型，包含追加式事务日志、有效状态投影、依赖安全补偿和活跃提交记录。
- 论文证明 ATP 相对于约束集 C 的四个安全属性：权威分离、序列等价生成准入、保留证据的修复和义务约束。
- 局部约束修复协议（LCRP）提供有界响应修复保证，编辑操作量比全局重算少一个数量级。
- 实验在9项 falsification 测试中成功拒绝违规操作，投影与验证开销低于6%。
specialized_tags:
  paper:
    paperTitle: 'Mnemosyne: Agentic Transaction Processing for Validating and Repairing
      AI-generated Workflows'
    authors: []
    affiliations: []
    venue: arXiv preprint
    codeUrl: null
    datasetUrl: null
    researchArea: Systems
    methodType:
    - LLM-based
    - theoretical
extract_result: success
---

# Computer Science > Artificial Intelligence

# Title:Mnemosyne: Agentic Transaction Processing for Validating and Repairing AI-generated Workflows

View PDF HTML (experimental)Abstract:LLMs, solvers, and agent teams increasingly generate workflow actions, repairs, and plans, but a generated action may be syntactically valid yet stale, infeasible, conflicting, or destructive of the evidence that triggered a repair. We introduce Agentic Transaction Processing (ATP), a transaction model that treats generated actions as untrusted proposals until they pass deterministic admission under a declared, executable constraint set C. The principle is two-sided: a proposal is not truth, and no proposal foresees every disruption: anything may propose, but only the runtime admits and commits, and when an unforeseen disruption strikes it repairs reactively within bounds rather than trusting a fresh proposal. Relative to C, committed-state correctness becomes independent of the competence, honesty, or learning of the proposing layer. We realize ATP in Mnemosyne, a runtime with an append-only transition log, effective-state projection, dependency-safe compensation, and active commitment records, and prove four safety properties relative to C (authority separation, serial-equivalent generative admission, evidence-preserving repair, and obligation containment) together with a bounded-reactive-repair guarantee for its localized repair protocol (LCRP). A reproducible artifact rejects the targeted violations across nine falsification tests while still admitting valid work, at under 6% projection-and-validation overhead, and bounded local repair edits an order of magnitude fewer operations than global recompute. Mnemosyne is open source: this https URL.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.