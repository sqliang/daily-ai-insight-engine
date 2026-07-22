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
tldr: arXiv 论文提出 Agentic Transaction Processing (ATP) 事务模型，将 AI 生成的动作视为不可信提案，只有通过确定性约束集
  C 准入后才能提交。论文基于 ATP 实现了运行时系统 Mnemosyne，包含追加式转换日志、有效状态投影、依赖安全补偿和主动提交记录，并证明了四项安全属性。
objective_summary: 该论文提出了 Agentic Transaction Processing (ATP) 事务模型，将 LLM、求解器和智能体团队生成的工作流动作视为不可信提案，需通过声明的确定性约束集
  C 的准入检查后才能由运行时提交。作者基于 ATP 实现了 Mnemosyne 运行时系统，采用追加式转换日志、有效状态投影、依赖安全补偿和主动提交记录等机制。论文证明了
  ATP 相对于约束集 C 的四项安全属性：权限分离、序列等价生成准入、证据保留修复和约束包含。可复现的实验表明，Mnemosyne 在九项伪造测试中拒绝了所有目标违规行为，同时仍允许有效工作流通过，投影与验证开销低于
  6%，局部修复协议 (LCRP) 修改的操作数比全局重新计算少一个数量级。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies: []
  technologies:
  - ATP
  - LCRP
  - LLM
  key_people: []
key_logic_flow:
- 论文指出现有问题：LLM 和智能体生成的工作流动作虽然语法正确，但可能因过时、不可行、冲突或破坏触发修复的证据而导致系统错误。
- 论文提出 Agentic Transaction Processing (ATP) 事务模型，核心原则是双重认定——提案不可信，且任何提案无法预见所有干扰；只有运行时负责准入和提交。
- ATP 模型要求所有生成动作必须通过声明的确定性约束集 C 的准入检查后才能被提交执行。
- 论文实现了 Mnemosyne 运行时系统，包含追加式转换日志、有效状态投影、依赖安全补偿和主动提交记录四个核心组件。
- 论文证明了 ATP 相对于约束集 C 的四项安全属性：权限分离、序列等价生成准入、证据保留修复和约束包含。
- 实验表明 Mnemosyne 在九项测试中拒绝了所有目标违规行为，投影与验证开销低于 6%，局部修复协议 (LCRP) 相比全局重新计算效率高出一个数量级。
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
object_mentions:
- object_type: project
  name: Mnemosyne
  canonical_name: Mnemosyne
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 论文基于 Agentic Transaction Processing 模型实现了 Mnemosyne 运行时系统，包含追加式转换日志、有效状态投影、依赖安全补偿和主动提交记录等机制。
  - Mnemosyne 在九项伪造测试中拒绝了所有目标违规行为，同时仍允许有效工作流通过，投影与验证开销低于 6%。
  - '论文标题为 Mnemosyne: Agentic Transaction Processing for Validating and Repairing
    AI-generated Workflows，Mnemosyne 是该工作的核心贡献。'
  article_id: 2fafb6fdbe04709e
- object_type: project
  name: Agentic Transaction Processing (ATP)
  canonical_name: Agentic Transaction Processing
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 论文提出了 Agentic Transaction Processing (ATP) 事务模型，将生成的动作视为不可信提案，直到它们通过声明的确定性约束集的准入检查。
  - ATP 模型的核心原则是：提案不等于事实，且没有提案能预见所有干扰；任何东西都可以提议，但只有运行时负责准入和提交。
  - 相对于约束集 C，ATP 保证已提交状态的正確性与提议层的能力、诚实性或学习无关。
  article_id: 2fafb6fdbe04709e
- object_type: project
  name: Localized Constraint Repair Protocol (LCRP)
  canonical_name: LCRP
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 论文证明了 Mnemosyne 的局部修复协议 (LCRP) 具有有界反应式修复保证。
  - LCRP 在实验中修改的操作数比全局重新计算少一个数量级。
  article_id: 2fafb6fdbe04709e
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