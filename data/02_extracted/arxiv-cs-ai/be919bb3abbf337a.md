---
title: 'AI Tool Discovery at Scale: All You Need is DNS'
source: https://arxiv.org/abs/2607.18242
author:
- '[[Enhao Chen, Yulin Shao]]'
published: '2026-07-22'
created: '2026-07-22'
manifest_dates:
- '2026-07-22'
- '2026-07-23'
description: 'arXiv:2607.18242v1 Announce Type: new Abstract: The coming era of autonomous
  AI agents demands a discovery mechanism capable of navigating millions of tools,
  yet existing solutions buckle under O(N) complexity and centralized governance.
  Instead of building another fragile overlay, we propose ToolDNS, a radical framework
  that retrofits semantic tool discovery onto the Internet''s most resilient substrate:
  the Domain Name System (DNS). By embedding functional intent and organizational
  trust into a hierarchical namespace, ToolDNS transforms an expensive semantic search
  into a series of lightweight, O(log N) name resolutions. We introduce three protocol-compliant
  enhancements to enable decentralized governance and semantic pruning: partially
  unfolded names, EDNS0 intent payloads, and logical subdomains. To rigorously evaluate
  this approach across the fragmented tooling landscape, we construct and release
  a large-scale heterogeneous benchmark comprising 33,688 real-world tools spanning
  MCP, A2A, RESTful, and Skill protocols. On this dataset, ToolDNS slashes the per-query
  search space by 95.26% while matching state-of-the-art retrieval accuracy. Furthermore,
  its UDP-native design reduces discovery latency by orders of magnitude compared
  to HTTP-based registries. Our work demonstrates that scalable AI interoperability
  requires not more middleware, but a smarter utilization of the infrastructure already
  beneath our feet.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: be919bb3abbf337a
source_type: academic_paper
tldr: 论文提出ToolDNS框架，利用DNS层级命名空间将AI工具语义发现从O(N)复杂度降为O(log N)，在包含33,688个真实工具的异构基准上将每次查询的搜索空间削减95.26%，同时匹配最先进的检索精度并将发现延迟降低数个数量级。
objective_summary: 该论文于2026年7月提交至arXiv，提出ToolDNS框架，将功能性意图和组织信任嵌入DNS层级命名空间，将昂贵的语义工具搜索转化为轻量级的O(log
  N)名称解析过程。作者引入了三种协议兼容的增强机制：部分展开名称、EDNS0意图载荷和逻辑子域，以实现去中心化治理和语义剪枝。论文构建并发布了包含33,688个真实工具的异构基准数据集，覆盖MCP、A2A、RESTful和Skill协议，在此数据集上ToolDNS将每次查询的搜索空间削减95.26%，同时保持与最先进方案相当的检索精度。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - DNS
  - ToolDNS
  - EDNS0
  - MCP
  - A2A
  - REST
  key_people: []
key_logic_flow:
- 现有AI工具发现机制面临O(N)复杂度和中心化治理瓶颈，无法支持未来自主AI代理对百万级工具的发现需求。
- ToolDNS将功能性意图和组织信任嵌入DNS层级命名空间，把昂贵的语义搜索转化为轻量级的O(log N)域名解析过程。
- 论文引入三种协议兼容增强：部分展开名称实现渐进式解析、EDNS0意图载荷携带语义查询、逻辑子域支持去中心化治理。
- 作者构建并发布了覆盖33,688个真实工具的异构基准数据集，涵盖MCP、A2A、RESTful和Skill四种协议。
- ToolDNS在该基准上将每次查询的搜索空间削减95.26%，同时匹配最先进的检索精度。
- 基于UDP的原生设计相比HTTP注册表将发现延迟降低数个数量级，证明AI互操作性需要更智能地利用现有基础设施而非增加中间件。
object_mentions:
- object_type: project
  name: ToolDNS
  canonical_name: ToolDNS
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - ToolDNS是一个将语义工具发现嵌入DNS层级命名空间的框架，通过嵌入功能性意图和组织信任将语义搜索转化为O(log N)名称解析。
  - ToolDNS在包含33,688个真实工具的异构基准上将每次查询的搜索空间削减95.26%，同时保持与最先进方案相当的检索精度。
  - 论文引入了部分展开名称、EDNS0意图载荷和逻辑子域三种协议兼容增强，以实现去中心化治理和语义剪枝。
  article_id: be919bb3abbf337a
- object_type: dataset
  name: Large-Scale Heterogeneous Tool Benchmark
  canonical_name: Heterogeneous Tool Benchmark 33K
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 作者构建并发布了一个大规模异构基准数据集，包含33,688个真实世界的工具，覆盖MCP、A2A、RESTful和Skill四种协议。
  - 在该基准数据集上，ToolDNS将每次查询的搜索空间削减95.26%，同时匹配最先进的检索精度。
  article_id: be919bb3abbf337a
extract_result: success
---

# Computer Science > Artificial Intelligence

# Title:AI Tool Discovery at Scale: All You Need is DNS

View PDF HTML (experimental)Abstract:The coming era of autonomous AI agents demands a discovery mechanism capable of navigating millions of tools, yet existing solutions buckle under O(N) complexity and centralized governance. Instead of building another fragile overlay, we propose ToolDNS, a radical framework that retrofits semantic tool discovery onto the Internet's most resilient substrate: the Domain Name System (DNS). By embedding functional intent and organizational trust into a hierarchical namespace, ToolDNS transforms an expensive semantic search into a series of lightweight, O(log N) name resolutions. We introduce three protocol-compliant enhancements to enable decentralized governance and semantic pruning: partially unfolded names, EDNS0 intent payloads, and logical subdomains. To rigorously evaluate this approach across the fragmented tooling landscape, we construct and release a large-scale heterogeneous benchmark comprising 33,688 real-world tools spanning MCP, A2A, RESTful, and Skill protocols. On this dataset, ToolDNS slashes the per-query search space by 95.26% while matching state-of-the-art retrieval accuracy. Furthermore, its UDP-native design reduces discovery latency by orders of magnitude compared to HTTP-based registries. Our work demonstrates that scalable AI interoperability requires not more middleware, but a smarter utilization of the infrastructure already beneath our feet.

### Current browse context:

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.