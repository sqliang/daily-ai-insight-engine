---
title: 'MosaicLeaks: Can your research agent keep a secret?'
source: https://huggingface.co/blog/ServiceNow/mosaicleaks
author: []
published: '2026-06-18'
created: '2026-06-19'
description: ''
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 2eb5bcc3ad88b97e
source_type: tech_blog
tldr: ServiceNow 提出了 MosaicLeaks 任务，用于评估深度研究智能体在混合公私有信息查询时通过外部搜索泄露敏感信息的风险。实验表明仅优化任务性能会加重泄露，他们提出的隐私感知训练方法
  PA-DR 将完整信息泄露率从 34.0% 降至 9.9%。
objective_summary: ServiceNow 发布了一篇关于深度研究智能体隐私泄露风险的研究，提出了 MosaicLeaks 评估任务和 PA-DR
  训练方法。该研究将隐私泄露分为意图泄露、答案泄露和完整信息泄露三个层级，并发现仅优化任务性能会加剧泄露。PA-DR 方法将严格链成功率从 48.7% 提升至 58.7%，同时将完整信息泄露率从
  34.0% 降至 9.9%。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - ServiceNow
  technologies:
  - MosaicLeaks
  - PA-DR
  - RL
  key_people: []
key_logic_flow:
- 深度研究智能体在混合使用本地私密文档和外部工具时，其外部搜索查询可能被对手累积分析，从而推断出私密信息，这就是马赛克效应隐私风险。
- ServiceNow 提出了 MosaicLeaks 评估任务，这是一种包含交错公私有信息的多跳问答深度研究任务，以智能体的外部查询日志作为泄露通道来评估隐私泄露程度。
- 他们将泄露分为三个层级：意图泄露（对手可以推断研究目标）、答案泄露（对手可以回答私人问题）和完整信息泄露（对手可以发现并陈述私密事实）。
- 实验表明现有智能体频繁泄露私密信息，且仅针对任务性能进行训练会使隐私泄露更加严重。
- 他们提出了隐私感知深度研究训练方法 PA-DR，将严格链成功率从 48.7% 提升至 58.7%。
- PA-DR 将完整信息泄露率从 34.0% 降至 9.9%，显著增强了智能体在混合信息查询场景下的隐私保护能力。
extract_result: success
object_mentions:
- object_type: project
  name: MosaicLeaks
  canonical_name: ServiceNow MosaicLeaks
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - MosaicLeaks 提出了一种新的深度研究任务，包含交错公私有信息的多跳问题，用于评估智能体在混合查询中的隐私泄露风险。
  - MosaicLeaks 将智能体的网络查询视为泄露通道，对手仅通过累积的查询日志来推断私密的企业信息。
  article_id: 2eb5bcc3ad88b97e
- object_type: project
  name: Privacy-Aware Deep Research (PA-DR)
  canonical_name: PA-DR
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - PA-DR 是一种马赛克泄露感知的强化学习训练方法，将严格链成功率从 48.7% 提升至 58.7%。
  - PA-DR 将答案泄露和完整信息泄露率从 34.0% 降至 9.9%，显著降低了智能体在深度研究任务中的隐私泄露风险。
  article_id: 2eb5bcc3ad88b97e
impact_score:
  score: 6.5
  reason: 该研究揭示了深度研究代理的一个系统性安全漏洞——外部查询日志可被第三方利用马赛克效应推断私密信息，这是一个真实且被行业低估的风险点。但 MosaicLeaks
    本质上是评估基准而非工程解决方案，PA-DR 方法的 34.0%→9.9% 降幅虽显著，仍需在更大规模、更多模型族上验证泛化性。短期内会引发企业级 AI 代理部署的安全审查，但不足以改变行业竞争格局。评分
    6.5：重要安全发现，影响可控，非范式转移。
sentiment: mixed
developer_sentiment:
  tone: skeptical
  primary_focus: 代理的外部查询日志成为隐私泄露通道，且任务性能越优泄露越严重
hype_assessment:
  level: low
  reason: 文章为 HuggingFace 博客形式的研究报告，内容扎实：给出了具体基准任务设计、三级泄漏分类体系、多模型实验结果、以及可复现的 PA-DR
    训练方法。未使用'颠覆'、'革命性'等 PR 滥用语，实验数据完整包含消融研究和量化指标。判定为低炒作。
information_entropy: high
domain_disruption:
  technical_innovation: 将情报学中的马赛克效应（Mosaic Effect）正式引入 AI 代理安全评估体系，设计了需要交织使用公开和私有信息的多跳问题基准
    MosaicLeaks，并提出了隐私感知强化学习（PA-DR）方法，在提升严格链成功率的同时将泄漏率从 34.0% 降至 9.9%，首次量化了任务性能与隐私泄漏之间的耦合关系。
  business_model: 可能推动企业级 AI 代理部署增加'查询日志隐私审计'作为合规要求，影响代理即服务（Agent-as-a-Service）产品的安全架构设计——未来代理产品可能需要内置查询脱敏或差分隐私机制，增加企业采购的安全评估环节。
engineering_complexity: prototype
compound_value:
  score: 7.0
  reason: MosaicLeaks 揭示了深度研究代理在结合私有文档与外部工具时的一个根本性隐私漏洞——马赛克效应，这是企业级 AI Agent 规模化部署中迟早会遇到的合规瓶颈。PA-DR
    方法给出了可量化的解决方案（泄漏率从 34% 降至 9.9%），如果该基准被行业采纳为标准评估套件，将形成类似 SafetyBench 的基础设施级影响力。但当前仍处于研究阶段，尚未看到生态采纳信号或产品化路径，因此评分锁定在
    7 分——有潜力成为 Agent 安全评测的行业基准，但需观察后续社区采用率和 ServiceNow 的产品化节奏。
value_capture_layer: agent_middleware
moat_impact: creates_new_moat
key_beneficiaries:
- ServiceNow
- Enterprise AI agent platforms
- AI governance & safety tooling companies
competitive_casualty:
- 隐私保护薄弱的 AI Agent 初创公司
- 忽视外部查询安全性的深度研究代理产品
market_opportunities:
- 企业可部署 MosaicLeaks 评测套件作为内部审计工具，在深度研究代理上线前系统性检测查询日志中的隐私泄漏风险，形成合规检查的标准流程
- 服务商可基于 PA-DR 方法提供隐私保护微调服务，为金融、医疗等强监管行业定制防泄漏的深度研究代理，收取年费或按模型定制计费
- 中间件创业机会：开发查询日志实时脱敏与拦截代理，在私有文档与外部搜索之间注入过滤层，阻断马赛克效应泄漏路径
risk_matrix:
  regulatory: GDPR、CCPA、HIPAA 等隐私法规要求对个人数据进行充分保护，深度研究代理的查询日志泄漏可能构成数据泄露事件，面临巨额罚款；欧盟
    AI Act 要求高风险 AI 系统具备充分的透明度和隐私保护措施，MosaicLeaks 揭示的泄漏风险可能触发合规审查
  technological: PA-DR 方法在实验室环境下有效但尚未在大规模、多类型代理架构上验证泛化能力；随着代理工具链（MCP 协议、浏览器自动化等）不断扩展，泄漏路径可能超出当前基准测试覆盖范围；强化学习训练可能存在
    reward hacking 风险，使代理在评测中表现良好但实际场景中仍泄漏信息
  competitive: 头部云厂商（Google、Microsoft、AWS）可能将类似隐私保护能力直接内置于其 Agent 平台，挤压第三方工具和中间件的市场空间；开源社区可能快速复现
    PA-DR 方法并推出免费替代方案，降低商业变现的壁垒
  ethical: 马赛克效应使得外部攻击者无需访问私有文档或推理过程即可推断高度敏感信息（如患者身份、企业并购计划），即使单个查询看似无害，组合后仍可能造成严重隐私侵犯；企业部署研究代理前若未充分评估此风险，可能对客户、合作伙伴和员工造成不可逆的隐私伤害
  additional: []
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: strategic_invest
object_insights:
- object_type: project
  name: MosaicLeaks
  canonical_name: ServiceNow MosaicLeaks
  url: null
  positioning: 深度研究智能体隐私泄露评估基准，通过交错公私有信息的多跳问答任务，以外部搜索查询日志为泄露通道，系统评估智能体在混合查询场景中的信息泄露风险。
  technical_signal: 定义了意图泄露、答案泄露和完整信息泄露三个递进层级的评估指标，为量化深度研究智能体的隐私风险提供了可操作的评测框架。
  adoption_signal: null
  ecosystem_relevance: 填补了 AI 智能体隐私安全评估的方法论空白，直接回应了企业级深度研究应用部署中日益突出的马赛克效应隐私威胁。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 随着深度研究智能体在企业场景中的快速渗透，隐私泄露已成为关键安全瓶颈；MosaicLeaks 提供的系统化评估框架是理解和缓解这一风险的基础工具，对
    AI 安全领域具有持续参考价值。
  risk_notes:
  - 评估场景为合成任务，真实世界的隐私攻击手段可能比查询日志分析更复杂和多样化。
  - 基准本身不提供隐私保护方案，需要与其他防御方法配合使用才能形成完整防护。
  score: 7.0
  article_ids:
  - 2eb5bcc3ad88b97e
  evidence_snippets:
  - MosaicLeaks 提出了一种新的深度研究任务，包含交错公私有信息的多跳问题，用于评估智能体在混合查询中的隐私泄露风险。
  - MosaicLeaks 将智能体的网络查询视为泄露通道，对手仅通过累积的查询日志来推断私密的企业信息。
- object_type: project
  name: Privacy-Aware Deep Research (PA-DR)
  canonical_name: PA-DR
  url: null
  positioning: 一种马赛克泄露感知的强化学习训练方法，通过在深度研究任务中引入隐私约束，同步提升任务性能并降低智能体在混合公私有信息查询中的信息泄露风险。
  technical_signal: 采用马赛克泄露感知的强化学习策略，将严格链成功率从 48.7% 提升至 58.7%，同时将完整信息泄露率从 34.0% 降至
    9.9%，实现了性能与隐私的双重优化。
  adoption_signal: null
  ecosystem_relevance: 为深度研究智能体的隐私保护提供了可复用的训练范式，直接证明了隐私约束与任务性能并非零和博弈，对企业级 AI 系统的安全部署具有重要指导意义。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 在深度研究智能体快速走向实用化的关键窗口期，PA-DR 展示了隐私保护与任务性能可以兼得的具体路径；其训练范式有望成为 AI 智能体隐私安全的标准组件，值得持续跟踪技术演进和社区采纳情况。
  risk_notes:
  - 仅在合成基准上完成验证，真实环境中的隐私攻防对抗可能削弱其防护效果。
  - 隐私约束的泛化性尚未在更多样化的深度研究任务中检验，可能面临性能权衡。
  score: 8.0
  article_ids:
  - 2eb5bcc3ad88b97e
  evidence_snippets:
  - PA-DR 是一种马赛克泄露感知的强化学习训练方法，将严格链成功率从 48.7% 提升至 58.7%。
  - PA-DR 将答案泄露和完整信息泄露率从 34.0% 降至 9.9%，显著降低了智能体在深度研究任务中的隐私泄露风险。
---

Deep research agents increasingly combine private local documents with external tools like web retrieval, creating a privacy risk: an agent's external queries may leak sensitive information. **MosaicLeaks** proposes a new deep-research task with multi-hop questions that interleave public and private information. Across the models we tested, agents frequently leaked private information, and training only for task performance made it worse. We propose a mosaic-leakage-aware RL training method, **Privacy-Aware Deep Research (PA-DR)**, which raises strict chain success (the share of chains where every hop is answered correctly) from 48.7% to 58.7% while reducing answer/full-information leakage from 34.0% to 9.9%.

A research agent at a healthcare firm is working through a routine question, and along the way it fires off a handful of ordinary-looking web searches. One references a cloud-migration milestone, one a January 2024 security disclosure, one narrows down which vendor got hit. No single query necessarily gives away the whole secret. But anyone watching the agent's outbound traffic can reassemble the fragments: MediConn had migrated 70% of its infrastructure to the cloud by January 2025, a fact that lived only in private documents. This is the mosaic effect, and it's the failure mode at the centre of MosaicLeaks.

MosaicLeaks treats those web queries as the leakage channel: the adversary never sees the private documents or the agent's reasoning, only the cumulative query log, and tries to infer private enterprise information from it.

We measure leakage in three ways, depending on what the adversary can infer from the observed queries:

| Leakage type | What the adversary sees | What counts as leakage |
|---|---|---|
Intent leakage |
Only the agent's web-query log | The adversary can infer the private research questions or goals the agent was trying to answer |
Answer leakage |
The web-query log plus a question about private information | The adversary can answer those private questions without seeing the private documents |
Full-information leakage |
Only the web-query log | The adversary can state verifiably true private claims, even without being given the questions |

These three represent increasing levels of concern. Intent leakage reveals *what the agent is investigating*. Answer leakage means the query log holds enough to answer a private question someone already has in hand. Full-information leakage is the strongest case: the observer can discover and state private facts without being told what to look for.