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
impact_score:
  score: 6.8
  reason: 该论文提出了一个极具原创性的架构思路——将AI工具语义发现嵌入DNS层级命名空间，把O(N)的语义搜索转化为O(log N)的域名解析。技术洞察力强（利用已有基础设施而非增加中间件），且提供了包含33,688个真实工具的异构基准和95.26%搜索空间削减的实证数据。但当前仍处于学术论文阶段，尚未在生产环境验证；DNS本身的缓存、TTL、安全（DNSSEC扩展兼容性）等工程化挑战未充分讨论。属于'重要架构创新，改变局部竞争格局'的层级，暂未达到行业范式转移级别。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 用DNS替代集中式注册表实现去中心化AI工具发现，O(log N)复杂度如何在实际MCP/A2A生态中落地
hype_assessment:
  level: low
  reason: 论文使用'radical framework'等修辞但整体上提供了充分的数据支撑：33,688个工具的异构基准、95.26%搜索空间削减、与SOTA相当的检索精度、UDP相比HTTP的延迟优势。消融实验和基准构建方法透明，没有空洞的'颠覆性'宣称，属于实打实的学术贡献。
information_entropy: high
domain_disruption:
  technical_innovation: 将DNS域名层级用于AI工具的功能性语义编码，提出三种协议兼容增强机制（部分展开名称实现渐进式解析、EDNS0意图载荷携带语义查询、逻辑子域支持去中心化治理），将昂贵的语义向量搜索转化为轻量级名称解析，从架构层面重新定义了AI互操作性基础设施的设计范式。
  business_model: 去中心化工具发现机制可能解构当前的AI工具集中式注册表/市场模式（如OpenAI Plugin Store、各种AI工具目录），降低平台垄断效应。任何组织或个人可在自有域名下注册AI工具，形成类似互联网DNS的分布式治理生态，长期可能催生工具注册的域名经济体系。
engineering_complexity: prototype
compound_value:
  score: 7.2
  reason: ToolDNS 提出了一个极具颠覆性的基础设施级方案：将 AI Agent 工具发现直接嵌入 DNS 命名空间，利用互联网最稳固的现有基础设施解决分布式工具发现的可扩展性瓶颈。其长期复利潜力体现在三个层面：1)
    网络效应极强——更多工具注册 → 更多 Agent 使用 → 更高质量命名空间的飞轮一旦启动难以逆转；2) 锁定效应显著——一旦业界形成基于 DNS 的工具命名和解析标准，切换成本将极高，类似域名系统的路径依赖；3)
    协议不可知策略——同时支持 MCP、A2A、RESTful 和 Skill 四种协议，不押注单一协议生态，提高了成为事实标准的可能性。但需保持谨慎：当前认知论状态为理论主张，实际部署需要协调
    DNS 运营商、标准化组织（IETF）、Agent 平台方和工具开发者多方利益，属于认知门槛高、周期长、回报不确定的布局。评分 7.2 反映了其巨大长期复利潜力与现阶段高度不确定性的对冲。
value_capture_layer: agent_middleware
moat_impact: democratizes_access
key_beneficiaries:
- Cloudflare
- AWS Route 53
- MCP 生态系统
- A2A 生态系统
- ICANN/DNS 注册局
competitive_casualty:
- 集中式工具注册平台（如 Toolhouse、Composio）
- 专有 Agent 中间件厂商
- API 聚合市场
- 自建工具发现层的 Agent 平台
market_opportunities:
- DNS基础设施提供商（如Cloudflare、AWS Route 53）可扩展AI工具发现作为增值服务，构建ToolDNS兼容的权威解析层，抢占AI代理时代的命名解析入口
- AI平台公司可借鉴ToolDNS的部分展开名称和EDNS0意图载荷机制，在不增加中间件的前提下将现有MCP/A2A工具目录的检索效率提升数个数量级
- 企业IT团队可基于DNS层级命名空间模式构建内部AI工具治理体系，使不同部门/安全等级的AI代理通过域名策略即可发现和授权工具调用，降低中心化注册表的运维成本
risk_matrix:
  regulatory: DNS命名空间治理涉及ICANN和各国域名管理机构，将AI工具语义嵌入域名体系可能触发域名滥用政策的重新解释，且EDNS0意图载荷若携带敏感查询信息可能面临数据本地化合规挑战
  technological: DNS协议存在消息大小硬限制（传统512字节/EDNS0上限约4096字节）、缓存一致性与TTL管理的固有缺陷，在工具元数据频繁更新或语义查询载荷较大时可能成为瓶颈；DNSSEC签名与验证额外增加延迟
  competitive: 现有AI工具生态（OpenAI GPTs Store、Anthropic MCP Hub、各大云厂商Agent市场）已形成网络效应和开发者心智占有，且这些平台有动力推广自有的专有发现协议而非开放的去中心化方案
  ethical: 工具发现的去中心化与民主化是一把双刃剑——恶意工具（数据窃取、系统提权、社会工程）同样可注册为可发现的DNS名称，AI代理可能在无人工干预情况下自动调用这些工具，放大安全风险
  additional:
  - DNS劫持/缓存投毒等传统DNS安全威胁将延伸到AI工具发现层面，攻击者可通过污染DNS响应将AI代理引导至恶意工具，形成新型攻击面
confidence:
  impact: medium
  compound: low
  hype: medium
actionable_insight: deep_dive
object_insights:
- object_type: project
  name: ToolDNS
  canonical_name: ToolDNS
  url: null
  positioning: ToolDNS是一个将AI工具语义发现嵌入DNS层级命名空间的开源研究框架，通过域名解析实现从O(N)到O(log N)的工具检索加速。
  technical_signal: 通过部分展开名称、EDNS0意图载荷和逻辑子域三种协议兼容增强，在33,688个工具基准上将搜索空间削减95.26%。
  adoption_signal: 论文构建并发布了覆盖MCP、A2A、RESTful和Skill四种协议的异构基准数据集，但尚未看到实际生产环境部署案例。
  ecosystem_relevance: 直接解决MCP、A2A等新兴AI工具协议生态中的核心发现难题，与当前AI代理互操作性标准化浪潮高度契合。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: ToolDNS以极低开销将工具发现复杂度降为O(log N)，其UDP原生设计比HTTP注册表延迟降低数个数量级，如果被主流AI协议生态采纳，可能成为AI代理互联互通的底层基础设施。
  risk_notes:
  - 框架依赖于DNS基础设施，DNS缓存和TTL策略可能影响工具发现的实时性和一致性。
  - 从论文到实际生态采纳仍有较大距离，需观察与MCP/A2A等协议社区的整合进展。
  score: 7.0
  article_ids:
  - be919bb3abbf337a
  evidence_snippets:
  - ToolDNS是一个将语义工具发现嵌入DNS层级命名空间的框架，通过嵌入功能性意图和组织信任将语义搜索转化为O(log N)名称解析。
  - ToolDNS在包含33,688个真实工具的异构基准上将每次查询的搜索空间削减95.26%，同时保持与最先进方案相当的检索精度。
  - 论文引入了部分展开名称、EDNS0意图载荷和逻辑子域三种协议兼容增强，以实现去中心化治理和语义剪枝。
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