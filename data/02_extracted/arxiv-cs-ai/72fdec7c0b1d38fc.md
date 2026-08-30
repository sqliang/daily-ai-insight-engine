---
title: 'DeAR: Decentralized Agentic Reasoning via Capability Grounding and Collaborative
  Thought Navigation'
source: https://arxiv.org/abs/2608.17282
author:
- '[[Xing Wei, Changmeng Zheng, XiaoYong Wei, Xiufen Ye, Qing Li]]'
published: '2026-08-20'
created: '2026-08-20'
manifest_dates:
- '2026-08-20'
description: ''
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 72fdec7c0b1d38fc
source_type: academic_paper
tldr: DeAR 是一种去中心化智能体推理框架，针对集中式协议的路由瓶颈和静态角色分配问题，提出以自主对等协作替代中央控制，核心包含能力定位、思维图导航与拓扑更新三种机制，在
  9 个多模态推理和文本问答基准上持续优于近期基线方法。
objective_summary: arXiv 预印本论文提出 DeAR（Decentralized Agentic Reasoning）框架，针对现有集中式智能体推理系统的路由瓶颈与静态角色分配问题，提出从中央控制转向自主对等协作。框架由三种机制构成：去中心化能力定位实现按查询的智能体专业化，思维图导航实现针对性的对等交互，拓扑更新实现自适应错误纠正。作者在
  9 个多模态推理与文本问答基准上进行评测，结果显示 DeAR 一致优于近期基线方法，验证了去中心化自适应协作可提升知识密集型推理任务的准确性。论文源码将在接收后开放。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies:
  - arXiv
  technologies:
  - DeAR
  - Agentic Reasoning
  - Multi-Agent Collaboration
  - Multimodal Reasoning
  key_people: []
key_logic_flow:
- 现有智能体推理系统通常依赖集中式协议，存在路由瓶颈和静态角色分配问题，在处理复杂多模态查询时容易失效。
- DeAR 提出从中央控制转向自主对等协作的框架，以解决集中式架构的可扩展性与适应性不足。
- 机制一为去中心化能力定位，根据具体查询实现智能体的动态专业化分工，取代静态角色分配。
- 机制二为思维图导航，让智能体在拓扑结构上开展针对性的对等交互，避免无差别广播。
- 机制三为拓扑更新，使智能体网络具备自适应的错误纠正能力。
- 在 9 个多模态推理和文本问答基准上的评测显示，DeAR 一致优于近期基线方法，源码将在论文接收后公开。
object_mentions:
- object_type: paper
  name: DeAR
  canonical_name: DeAR
  url: https://arxiv.org/abs/2608.17282
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - DeAR 是一个从集中控制转向自主对等协作的智能体推理框架，旨在解决集中式协议的路由瓶颈与静态角色分配问题。
  - DeAR 由去中心化能力定位、思维图导航和拓扑更新三种机制构成，在 9 个多模态推理与文本问答基准上持续优于近期基线方法。
  - 论文注明 DeAR 的源代码将在接收后开放，当前 arXiv 页面仅提供摘要与作者评测结论。
  article_id: 72fdec7c0b1d38fc
extract_result: success
---

# Computer Science > Artificial Intelligence

# Title:DeAR: Decentralized Agentic Reasoning via Capability Grounding and Collaborative Thought Navigation

View PDF HTML (experimental)Abstract:Existing agentic reasoning systems typically rely on centralized protocols. This design introduces routing bottlenecks and static role allocations that often fail when handling complex multimodal queries. We propose DeAR (Decentralized Agentic Reasoning), a framework that shifts from central control to autonomous peer-to-peer collaboration. DeAR is built on three mechanisms: (1) decentralized capability grounding for query-dependent agent specialization, (2) thought map navigation for targeted peer interactions, and (3) topology update for adaptive error correction. Evaluations across 9 diverse multimodal reasoning and text-based QA benchmarks indicate that DeAR consistently outperforms recent baseline methods, validating that decentralized and adaptive collaboration among agents enhances accuracy in knowledge-intensive reasoning tasks. The source code will be available at https://open_upon_acceptance.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.