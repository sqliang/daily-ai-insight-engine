---
title: 'Governed Persistent Memory: Source-Bound State Semantics and Fail-Closed Release
  for Long-Horizon Agents'
source: https://arxiv.org/abs/2608.12476
author:
- '[[Guodong Xu]]'
published: '2026-08-15'
created: '2026-08-15'
manifest_dates:
- '2026-08-15'
description: 'arXiv:2608.12476v1 Announce Type: new Abstract: Long-term agent memory
  is usually treated as select--store--retrieve, but retrieval does not decide whether
  contradictory, superseded, retracted, deleted, or stale records may support an outgoing
  claim. We introduce Governed Persistent Memory (GPM), an auditable bitemporal state-transition
  model with source-bound admission, derived lifecycle state, current public barriers,
  and fail-closed structured release. Five executable clauses cover ledger integrity,
  source binding, conflict isolation, non-revival after retraction or deletion, and
  exact claim closure over a fresh view at one verified head. On a prespecified hash-frozen
  3,600-case GPM-ReleaseBench, GPM matches all complete outcomes; the strongest of
  three intentionally simple complete policies matches 1,800/3,600 and makes unmatched
  releases on 50% of violation cases. A separate sealed end-to-end service evaluation
  exercises real ingestion and release across eight query families. In its publicly
  disclosed V3 arm, the governed lane is correct on 2,400/2,400 clusters versus 600/2,400
  for ungoverned local Qwen2.5-7B; it repairs all 1,800 baseline failures with no
  regression (one-sided 95% lower bounds 99.875% and 99.834%). A later V5 reseal over
  Chinese- and English-command arms, with generation-date pinning and no post-freeze
  reducer amendment, again obtains 2,400/2,400 per arm. A production-code-independent
  finite model explores 331,776 semantic and 1,990,656 query states without a full-contract
  counterexample, and a 100,000-trace three-engine differential yields zero mismatches.
  These are bounded contract and implementation results, not open-world model accuracy
  or evidence of world truth. Governed answers in the sealed service evaluation are
  deterministic service outputs; the 7B result is the ungoverned comparison, not a
  claim that a language model itself became perfectly accurate.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 3e5bbba96a6cde57
source_type: academic_paper
tldr: 论文提出 Governed Persistent Memory（GPM），一种可审计的双时态状态转换模型，为长时程智能体实现源绑定、生命周期状态与失败关闭的持久记忆管理。在
  3600 例基准与密封服务评测中，受管通道正确率显著优于未受管的本地 Qwen2.5-7B，作者强调这是有界合约与实现结果。
objective_summary: 论文提出 GPM，一种可审计的双时态状态转换模型，用于解决长时程智能体在检索时无法判定冲突、过期、撤回或删除记录是否支撑输出声明的问题，核心包括源绑定准入、派生生命周期状态与失败关闭的结构化释放。GPM
  定义五个可执行条款，并在哈希冻结的 3600 例 GPM-ReleaseBench 上匹配全部完整结果。在密封端到端服务评测 V3 分支中，受管通道在 2400/2400
  集群上正确，未受管的本地 Qwen2.5-7B 仅 600/2400，且修复全部 1800 个基线失败无回归；V5 重新密封的中英文分支再次各取得 2400/2400。作者明确这些是有界合约与实现结果，而非开放世界模型准确率或世界真实性证据。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies:
  - Alibaba
  technologies:
  - GPM
  - Qwen2.5-7B
  - bitemporal state-transition model
  key_people: []
key_logic_flow:
- GPM 将长时程智能体记忆从简单的选择—存储—检索扩展为可审计的双时态状态转换模型，引入源绑定准入、派生生命周期状态、当前公开壁垒和失败关闭的结构化释放。
- GPM 定义五个可执行条款，覆盖账本完整性、源绑定、冲突隔离、撤回或删除后禁止复活，以及在单一验证头部的新鲜视图上实现精确声明闭合。
- 在哈希冻结的 3600 例 GPM-ReleaseBench 上，GPM 匹配所有完整结果，而最强的三种简单策略中最好者仅匹配 1800/3600，并在 50%
  的违规案例上做出不匹配释放。
- 密封端到端服务评测覆盖八个查询家族，V3 分支中受管通道在 2400/2400 集群上正确，未受管的本地 Qwen2.5-7B 仅 600/2400，且修复全部
  1800 个基线失败且无回归。
- V5 重新密封涵盖中英文指令分支，采用生成日期固定且不做冻结后归约修正，两个分支均再次取得 2400/2400。
- 与生产代码无关的有限模型探索 331776 个语义状态和 1990656 个查询状态而无完整合约反例，10 万条轨迹的三引擎差分测试零失配；作者明确这些结果是有界合约与实现结果而非世界真实性证据。
object_mentions:
- object_type: model
  name: Governed Persistent Memory
  canonical_name: Governed Persistent Memory (GPM)
  url: https://arxiv.org/abs/2608.12476
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 论文提出 GPM，一种可审计的双时态状态转换模型，为长时程智能体提供源绑定准入、派生生命周期状态和失败关闭的结构化释放。
  - GPM 定义五个可执行条款，覆盖账本完整性、源绑定、冲突隔离、撤回或删除后禁止复活，以及精确声明闭合。
  article_id: 3e5bbba96a6cde57
- object_type: dataset
  name: GPM-ReleaseBench
  canonical_name: GPM-ReleaseBench
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 在预置哈希冻结的 3600 例 GPM-ReleaseBench 上，GPM 匹配所有完整结果，而最强的简单策略只匹配 1800/3600。
  - 该基准对比受管 GPM 与简单策略，结果显示简单策略在 50% 的违规案例上产生不匹配释放，而 GPM 匹配全部完整结果。
  article_id: 3e5bbba96a6cde57
- object_type: model
  name: Qwen2.5-7B
  canonical_name: Qwen2.5-7B
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 在密封服务评测 V3 分支中，未受管的本地 Qwen2.5-7B 在 2400 个集群中仅正确 600 个，作为受管通道的对照基线。
  - 作者强调 V3 分支中的 7B 结果是未受管对照，而非声称语言模型本身达到了完全准确。
  article_id: 3e5bbba96a6cde57
extract_result: success
impact_score:
  score: 5.5
  reason: 该论文直击长时程智能体记忆的一致性与可审计性这一真实痛点——检索时无法判定冲突、过期、撤回或删除记录是否支撑对外声明。但影响范围主要停留在架构设计/框架层面：GPM
    是 Alibaba 提出的有界合约模型，而非开放世界范式，作者也明确声明结果是'有界合约与实现结果'而非世界真实性证据。相比范式转移级事件，它更接近'改变局部竞争格局'——为可治理的
    Agent 记忆提供了可验证的参考架构，可能影响 LangChain/LlamaIndex 类生态的记忆组件设计与合规型 Agent 平台建设，但短期内不会重塑行业格局，故给予中等偏上评分。
sentiment: positive
developer_sentiment:
  tone: skeptical
  primary_focus: 2400/2400 的完美结果是否依赖自建基准与密封评测协议，失败关闭机制能否泛化到开放世界与真实生产规模
hype_assessment:
  level: low
  reason: 论文刻意采用防御性措辞，通篇强调'有界合约与实现结果，而非开放世界模型准确率或世界真实性证据'；评测采用哈希冻结的预注册基准、密封端到端服务评测与三引擎差分测试，没有使用'颠覆''革命性'等
    PR 词汇，也未夸大 Qwen2.5-7B 对比结论（明确说明 7B 结果只是未受管对照而非模型本身变准确），判定为实打实的干货。
information_entropy: high
domain_disruption:
  technical_innovation: 将双时态（bitemporal）数据库建模与形式化合约引入智能体记忆层，实现源绑定准入、派生生命周期状态与失败关闭的结构化释放；核心突破是把记忆检索从软性的语义相似匹配升级为可审计、可验证的状态机，通过五个可执行条款保证任何对外声明精确闭合于单一验证头部的新鲜视图，并配以有限模型穷举（33
    万+ 语义状态）与三引擎差分测试做实现验证。
  business_model: 面向合规敏感行业（金融、医疗、法律等）的'可审计智能体记忆'治理层，可作为企业级 Agent 平台的中间件或审计基础设施商业化，或作为可观测性/合规审计产品的差异化能力打包进现有
    Agent 框架生态，填补'Agent 输出可追责'这一新兴市场空白。
engineering_complexity: prototype
compound_value:
  score: 5.5
  reason: 评估需区分问题空间与具体贡献两层。从问题空间看，长时程 Agent 的记忆完整性、可审计性与来源绑定是企业级部署的核心瓶颈——企业要求检索输出可追溯、可撤回、可合规审计，这一需求随
    Agent 从 Demo 走向生产而持续放大，叠加欧盟 AI 法案等监管对可审计性的要求，3-5 年后大概率仍是基础设施级刚需。但具体到 GPM 本身，作者明确声明当前结果是有界合约与实现结果、非开放世界准确率证据，价值形态是研究范式与评测基准（GPM-ReleaseBench、密封评测方法论、有限模型状态探索），而非可直接变现的产品或专利壁垒；其复利效应高度依赖后续被主流框架（LangChain/LangGraph、Mem0、Letta
    等）采纳为记忆治理标准的程度。赛道价值高、单点贡献尚需生态验证，故给予中等偏上评分。
value_capture_layer: agent_middleware
moat_impact: creates_new_moat
key_beneficiaries:
- Alibaba
- Qwen
- LangChain
- Mem0
- Letta
competitive_casualty:
- 非受管的本地小模型 Agent 部署
- 无审计能力的 Agent 记忆中间件
- 仅依赖向量检索的朴素记忆方案
market_opportunities:
- 企业级 Agent 平台可将 GPM 的源绑定准入与失败关闭释放语义内置为合规记忆模块，为金融、医疗等强监管行业提供可审计、可追溯的长期记忆能力
- 创业者可基于冲突隔离与撤回/删除后禁止复活原则，开发面向 RAG 与 Agent 记忆系统的防陈旧信息与防幻觉审计工具，填补现有向量数据库缺少生命周期治理的空白
- 建议关注将双时态状态转换模型以插件或标准层形式接入主流 Agent 编排框架（如 LangChain、LlamaIndex）的落地机会，降低记忆治理的集成门槛
risk_matrix:
  regulatory: 该技术本身偏合规友好（天然支持撤回/删除后的信息停用，契合 GDPR 删除权等要求），但若厂商将'可审计'声明包装为法律合规证明，可能因作者明确否认开放世界正确性而面临虚假宣传或合规验收风险；跨司法辖区落地时需谨慎界定审计证据的效力边界
  technological: 论文结论是有界合约与实现结果而非开放世界准确率，在真实开放域 Agent 场景下的泛化性尚未验证；存在被更轻量方案或模型原生事实能力提升（如更强的检索与推理底座）所替代的风险
  competitive: OpenAI、Anthropic、Google 等头部厂商正将记忆治理内建到 Agent 平台，独立论文/开源形态可能被平台内建能力挤压；以
    Qwen 为对比基线的自建基准也存在被质疑客观性的竞争风险
  ethical: 可审计账本与全量用户轨迹记录可能加剧隐私侵犯与数据最小化原则的冲突；同时治理机制可能给用户造成'系统绝对正确'的错觉，而作者明确否认世界真实性证据，存在过度信任的伦理隐患
  additional:
  - 基准与实现均由作者自建，存在自我评估偏差风险，需等待第三方复现
  - 2400/2400 与 100% 正确率等表述易被误读为通用能力，需持续跟踪其在开放环境中的退化表现
confidence:
  impact: medium
  compound: medium
  hype: low
actionable_insight: deep_dive
---

# Computer Science > Artificial Intelligence

# Title:Governed Persistent Memory: Source-Bound State Semantics and Fail-Closed Release for Long-Horizon Agents

View PDF HTML (experimental)Abstract:Long-term agent memory is usually treated as select--store--retrieve, but retrieval does not decide whether contradictory, superseded, retracted, deleted, or stale records may support an outgoing claim. We introduce Governed Persistent Memory (GPM), an auditable bitemporal state-transition model with source-bound admission, derived lifecycle state, current public barriers, and fail-closed structured release. Five executable clauses cover ledger integrity, source binding, conflict isolation, non-revival after retraction or deletion, and exact claim closure over a fresh view at one verified head.

On a prespecified hash-frozen 3,600-case GPM-ReleaseBench, GPM matches all complete outcomes; the strongest of three intentionally simple complete policies matches 1,800/3,600 and makes unmatched releases on 50% of violation cases. A separate sealed end-to-end service evaluation exercises real ingestion and release across eight query families. In its publicly disclosed V3 arm, the governed lane is correct on 2,400/2,400 clusters versus 600/2,400 for ungoverned local Qwen2.5-7B; it repairs all 1,800 baseline failures with no regression (one-sided 95% lower bounds 99.875% and 99.834%). A later V5 reseal over Chinese- and English-command arms, with generation-date pinning and no post-freeze reducer amendment, again obtains 2,400/2,400 per arm. A production-code-independent finite model explores 331,776 semantic and 1,990,656 query states without a full-contract counterexample, and a 100,000-trace three-engine differential yields zero mismatches.

These are bounded contract and implementation results, not open-world model accuracy or evidence of world truth. Governed answers in the sealed service evaluation are deterministic service outputs; the 7B result is the ungoverned comparison, not a claim that a language model itself became perfectly accurate.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.