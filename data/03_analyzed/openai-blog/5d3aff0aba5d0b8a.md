---
title: Daybreak models are now available on AWS
source: https://openai.com/index/daybreak-models-are-now-available-on-aws
author: []
published: Tue, 11 Aug 2026 10:00:00 GMT
created: '2026-08-12'
manifest_dates:
- '2026-08-12'
- '2026-08-13'
- '2026-08-14'
description: OpenAI and AWS are making Daybreak cybersecurity capabilities available
  through Amazon Bedrock to support enterprise security workflows.
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 5d3aff0aba5d0b8a
source_type: tech_blog
tldr: OpenAI 宣布其网络安全模型产品 Daybreak（含 Blue 与 Red 两个访问层级）正式上线 Amazon Bedrock，企业可在现有 AWS
  环境中调用前沿网络防御与漏洞研究能力。
objective_summary: OpenAI 于 2026 年发布公告，将 Daybreak 网络安全模型能力通过 Amazon Bedrock 向符合条件的企业客户提供。Daybreak
  Blue 面向授权防御性安全工作，提供包括 GPT-5.6 Sol 在内的前沿通用模型；Daybreak Red 面向授权漏洞研究、漏洞利用验证和安全测试，提供专门训练的网络安全模型。客户获批加入
  Daybreak Access 后，可通过 Amazon Bedrock 控制台或 Responses API 的 bedrock-mantle 端点访问这些模型。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - OpenAI
  - Amazon Web Services
  technologies:
  - Daybreak
  - Daybreak Blue
  - Daybreak Red
  - GPT-5.6 Sol
  - Amazon Bedrock
  - Responses API
  - bedrock-mantle endpoint
  key_people: []
key_logic_flow:
- OpenAI 此前已将前沿模型与 Codex 引入 AWS，本次进一步把 Daybreak 能力通过 Amazon Bedrock 提供给企业客户。
- Daybreak Access 包含 Blue 与 Red 两个访问层级，分别服务于授权防御性安全工作和授权进攻性安全研究。
- Daybreak Blue 提供 GPT-5.6 Sol 等前沿通用模型，并配备针对防御性安全工作的安全护栏。
- Daybreak Red 提供专门训练的网络安全模型，支持漏洞研究、利用验证、安全测试、利用复现与缓解方案开发。
- 符合条件的企业客户在获批加入 Daybreak Access 后，可通过 Amazon Bedrock 控制台或 Responses API 的 bedrock-mantle
  端点调用模型。
- 该合作旨在让企业利用现有 AWS 的安全、治理与运维流程，将前沿 AI 网络安全能力投入生产。
object_mentions:
- object_type: product
  name: Daybreak
  canonical_name: OpenAI Daybreak
  url: https://openai.com/index/daybreak-models-are-now-available-on-aws
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - OpenAI 宣布 Daybreak 能力现可通过 Amazon Bedrock 提供，Blue 与 Red 两个访问层级均已在 AWS 上线。
  - Daybreak 模型用于加速漏洞研究、检测工程、事件响应、利用复现与缓解方案开发等复杂安全流程。
  - 企业客户获批加入 Daybreak Access 后，可通过 Amazon Bedrock 控制台或 Responses API 的 bedrock-mantle
    端点访问模型。
  article_id: 5d3aff0aba5d0b8a
- object_type: product
  name: Daybreak Access
  canonical_name: OpenAI Daybreak Access
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Daybreak Red 与 Daybreak Blue 均要求客户先注册并获批加入 Daybreak Access。
  - 通过 Daybreak Access，防御方可以在其现有 AWS 环境中使用 OpenAI 的前沿网络模型。
  - Daybreak Access 设有两个访问层级：Blue 面向防御性安全工作，Red 面向授权漏洞研究与利用验证。
  article_id: 5d3aff0aba5d0b8a
- object_type: product
  name: Daybreak Blue
  canonical_name: OpenAI Daybreak Blue
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Daybreak Blue 提供访问前沿通用模型的权限，包括 GPT-5.6 Sol，并配备面向授权防御性安全工作的安全护栏。
  - 该层级已在 AWS 上线，面向需要开展防御性安全工作的授权客户。
  - 与 Red 层级不同，Blue 侧重通用模型能力在防御场景中的安全使用。
  article_id: 5d3aff0aba5d0b8a
- object_type: product
  name: Daybreak Red
  canonical_name: OpenAI Daybreak Red
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Daybreak Red 提供访问专门训练的网络安全模型的权限，用于授权漏洞研究、利用验证与安全测试。
  - 该层级支持复杂工作流，包括利用复现与缓解方案开发。
  - Daybreak Red 与 Daybreak Blue 一样，需要客户先加入 Daybreak Access 才能使用。
  article_id: 5d3aff0aba5d0b8a
- object_type: model
  name: GPT-5.6 Sol
  canonical_name: GPT-5.6 Sol
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Daybreak Blue 提供的前沿通用模型中明确包含 GPT-5.6 Sol。
  - GPT-5.6 Sol 作为 Daybreak Blue 可访问的模型之一，配备面向授权防御性安全工作的安全护栏。
  - OpenAI 未在文中进一步披露 GPT-5.6 Sol 的技术细节或训练数据。
  article_id: 5d3aff0aba5d0b8a
- object_type: product
  name: Amazon Bedrock
  canonical_name: Amazon Bedrock
  url: https://aws.amazon.com/bedrock/
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - OpenAI 选择通过 Amazon Bedrock 向符合条件的企业客户提供 Daybreak 能力。
  - 客户可在其已用于构建、保护和运行软件的 AWS 环境中使用 Daybreak。
  - 获批客户可通过 Amazon Bedrock 控制台访问 Daybreak Red 与 Daybreak Blue。
  article_id: 5d3aff0aba5d0b8a
- object_type: product
  name: Responses API
  canonical_name: OpenAI Responses API
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - 获批客户除 Bedrock 控制台外，还可通过 Responses API 的 bedrock-mantle 端点访问 Daybreak 模型。
  - 该 API 路径为客户提供了一种程序化调用 Daybreak 能力的方式。
  - 文中未详细说明 Responses API 在此场景下的完整功能或定价。
  article_id: 5d3aff0aba5d0b8a
extract_result: success
impact_score:
  score: 6.5
  reason: OpenAI 将 Daybreak 网络安全模型上架 Amazon Bedrock，是把前沿 AI 安全能力推向主流企业云渠道的关键一步。它不仅会加剧
    CrowdStrike、Palo Alto 等安全厂商与 AI 模型云厂商的竞争，也让 AWS 成为 OpenAI 面向 B 端落地的更深层管道。不过，这属于产品落地与渠道扩展，而非技术范式或模型能力本身的突破，因此评分在重要但非革命的区间。
sentiment: mixed
developer_sentiment:
  tone: skeptical
  primary_focus: Daybreak Red 的授权漏洞研究/利用验证能力带来的双重用途风险与访问控制
hype_assessment:
  level: medium
  reason: 原文使用 'next step in our work with AWS'、'frontier cyber models'、'put advanced
    cybersecurity capabilities to work in production' 等 PR 常见表达，强调战略意义与生产就绪，但没有出现
    '颠覆'、'革命性' 等极端词汇。整体是标准的产品可用性公告，部分措辞有包装成分，核心信息仍较扎实。
information_entropy: medium
domain_disruption:
  technical_innovation: 无新的模型架构或训练方法披露，本质上是 Daybreak Blue/Red 产品通过 Amazon Bedrock
    与 Responses API 的 bedrock-mantle 端点完成多云/渠道交付。
  business_model: 强化了 OpenAI 与 AWS 的 B 端绑定，使网络安全能力可通过现有 AWS 安全、治理、采购与运维流程售卖，降低企业采用门槛；同时
    Blue/Red 双层级访问模式构成基于合规资质的分级商业授权。
engineering_complexity: production_ready
compound_value:
  score: 6.5
  reason: 网络安全是企业最高预算优先级之一，Daybreak 通过 Amazon Bedrock 进入企业现有 AWS 安全、治理与采购流程，能显著降低采用摩擦并提高客户粘性。一旦企业将其嵌入漏洞研究、检测工程与事件响应工作流，迁移成本会随数据、策略和合规审查的积累而上升，形成长期复利。但该合作的本质是模型分发渠道扩展，而非技术范式突破；其价值高度依赖
    OpenAI 持续的网络安全模型领先性、AWS 的政企关系，以及 Daybreak Access 的审批与风控接受度。若未来出现模型能力平替或监管收紧 Red
    Team 用途，复利效应会被削弱。
value_capture_layer: foundation_model
moat_impact: strengthens_monopoly
key_beneficiaries:
- OpenAI
- Amazon Web Services
- Amazon Bedrock
competitive_casualty:
- 独立网络安全AI初创公司
- 单一安全模型供应商
- 非AWS云安全服务商
- 传统渗透测试与安全咨询厂商
market_opportunities:
- AWS 生态集成商与托管服务提供商可围绕 Daybreak 开发合规咨询、访问申请代理和安全运营落地服务，形成面向金融、能源等强监管行业的垂直解决方案。
- 企业安全团队可将 Daybreak Red 能力整合进现有漏洞管理平台与 DevSecOps 流水线，开发自动化的漏洞验证、利用复现和缓解方案生成工具。
- 安全培训和红蓝对抗演练厂商可基于 Daybreak 模型构建交互式攻防模拟产品，拓展授权渗透测试与安全意识培训市场。
risk_matrix:
  regulatory: 双重访问层级（Blue/Red）涉及进攻性网络安全能力，可能触发出口管制、受控网络武器法规及各国网络安全审查；客户资格审核与使用日志留存将成为合规重点。
  technological: 模型输出可能被滥用于生成真实漏洞利用代码或绕过安全机制，存在被红队/黑产逆向或 Prompt 越狱导致能力泄漏的技术风险。
  competitive: 微软、Google Cloud 及 Palo Alto、CrowdStrike 等安全厂商可能加速将自有或第三方 AI 安全模型嵌入云平台，形成生态与渠道竞争。
  ethical: Daybreak Red 的进攻性安全能力若被误用或扩散，可能助长恶意攻击、扩大攻防不对称性；偏见或幻觉可能导致误报漏洞或错误的缓解建议。
  additional:
  - AWS 单一渠道依赖风险：若未来 AWS 服务策略、定价或区域可用性调整，企业客户迁移成本较高。
  - 品牌与信任风险：OpenAI 安全模型若发生现实世界的安全事件，可能引发公众对 AI 网络武器化的强烈反弹。
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: strategic_invest
object_insights:
- object_type: product
  name: Daybreak
  canonical_name: OpenAI Daybreak
  url: https://openai.com/index/daybreak-models-are-now-available-on-aws
  positioning: OpenAI 面向企业安全团队推出的前沿 AI 网络安全模型套件，现通过 Amazon Bedrock 在 AWS 环境中提供。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 企业安全团队
  - 漏洞研究人员
  - 检测工程师
  - 事件响应人员
  - 合规与治理负责人
  product_signal: 提供 Blue（防御性安全）与 Red（漏洞研究/利用验证）两个访问层级，支持从漏洞发现到修复验证的端到端安全流程。
  market_signal: 与 AWS 深度合作，将前沿网络安全能力嵌入企业现有云治理与合规流程，降低采购与落地门槛。
  differentiation: 将通用前沿模型（GPT-5.6 Sol）与专门训练的网络安全模型整合在同一访问体系内，覆盖攻防两端。
  watch_reason: Daybreak 是 OpenAI 进入企业网络安全垂直市场的关键产品，借助 AWS Bedrock 的渠道和治理框架，有望快速触达大型企业客户，并可能成为
    AI 安全能力落地的主流形态。
  risk_notes:
  - 需要获批加入 Daybreak Access，访问门槛可能限制早期采用范围。
  score: 8.0
  article_ids:
  - 5d3aff0aba5d0b8a
  evidence_snippets:
  - OpenAI 宣布 Daybreak 能力现可通过 Amazon Bedrock 提供，Blue 与 Red 两个访问层级均已在 AWS 上线。
  - Daybreak 模型用于加速漏洞研究、检测工程、事件响应、利用复现与缓解方案开发等复杂安全流程。
  - 企业客户获批加入 Daybreak Access 后，可通过 Amazon Bedrock 控制台或 Responses API 的 bedrock-mantle
    端点访问模型。
- object_type: product
  name: Daybreak Access
  canonical_name: OpenAI Daybreak Access
  url: null
  positioning: OpenAI 对企业客户开放的 Daybreak 能力访问审批与权限管理体系。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 企业安全负责人
  - CISO
  - 合规团队
  - 获得授权的攻防研究人员
  product_signal: 通过分级访问控制（Blue/Red）区分防御性安全与进攻性安全研究的授权范围。
  market_signal: 反映 OpenAI 对网络安全模型采取受控分发的商业化策略，强调合规与责任使用。
  differentiation: 以双层授权机制平衡能力开放与风险治理，区别于一般 API 的直接订阅模式。
  watch_reason: Daybreak Access 的审批标准和覆盖范围将直接影响 OpenAI 网络安全产品的市场渗透速度，也是观察其负责任 AI 治理能力的重要窗口。
  risk_notes:
  - 审批流程与标准尚不透明，可能导致客户获取周期较长并影响早期渗透。
  score: 6.0
  article_ids:
  - 5d3aff0aba5d0b8a
  evidence_snippets:
  - Daybreak Red 与 Daybreak Blue 均要求客户先注册并获批加入 Daybreak Access。
  - 通过 Daybreak Access，防御方可以在其现有 AWS 环境中使用 OpenAI 的前沿网络模型。
  - Daybreak Access 设有两个访问层级：Blue 面向防御性安全工作，Red 面向授权漏洞研究与利用验证。
- object_type: product
  name: Daybreak Blue
  canonical_name: OpenAI Daybreak Blue
  url: null
  positioning: Daybreak 中面向授权防御性安全工作的访问层级，提供前沿通用模型及配套安全护栏。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 企业蓝队
  - SOC 分析师
  - 检测工程师
  - 事件响应人员
  product_signal: 包含 GPT-5.6 Sol 等前沿通用模型，并针对防御性安全场景设置安全护栏。
  market_signal: 满足企业在现有 AWS 环境中开展检测工程、事件响应等防御工作的需求。
  differentiation: 在通用模型能力基础上叠加防御场景的安全护栏，区别于面向红队研究的专门安全模型。
  watch_reason: Blue 层级是 Daybreak 在企业侧最容易规模化采用的部分，其安全护栏设计和模型表现将决定防御性 AI 助手能否进入主流安全运营流程。
  risk_notes:
  - 安全护栏若过严可能降低实际工作效率，需要在合规与可用性之间取得平衡。
  score: 7.0
  article_ids:
  - 5d3aff0aba5d0b8a
  evidence_snippets:
  - Daybreak Blue 提供访问前沿通用模型的权限，包括 GPT-5.6 Sol，并配备面向授权防御性安全工作的安全护栏。
  - 该层级已在 AWS 上线，面向需要开展防御性安全工作的授权客户。
  - 与 Red 层级不同，Blue 侧重通用模型能力在防御场景中的安全使用。
- object_type: product
  name: Daybreak Red
  canonical_name: OpenAI Daybreak Red
  url: null
  positioning: Daybreak 中面向授权漏洞研究、利用验证与安全测试的高级访问层级。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 漏洞研究人员
  - 红队测试人员
  - 安全研究员
  - 渗透测试团队
  product_signal: 提供专门训练的网络安全模型，支持漏洞研究、利用验证、利用复现与缓解方案开发。
  market_signal: 瞄准高端安全研究和红队测试市场，采用严格审批制控制访问范围。
  differentiation: 聚焦进攻性安全研究，提供经过专门训练的网络安全模型，而非通用模型。
  watch_reason: Red 层级代表了 OpenAI 向高风险安全研究能力输出的尝试，其访问控制、模型能力和实际研究效果将成为行业关注焦点。
  risk_notes:
  - 授权漏洞研究与潜在滥用风险之间的边界需要持续观察。
  score: 7.0
  article_ids:
  - 5d3aff0aba5d0b8a
  evidence_snippets:
  - Daybreak Red 提供访问专门训练的网络安全模型的权限，用于授权漏洞研究、利用验证与安全测试。
  - 该层级支持复杂工作流，包括利用复现与缓解方案开发。
  - Daybreak Red 与 Daybreak Blue 一样，需要客户先加入 Daybreak Access 才能使用。
---

Earlier this year, OpenAI frontier models and Codex became generally available on AWS, giving enterprises a new path to bring advanced AI into production. Today, we’re sharing the next step in our work with AWS: making Daybreak capabilities available through Amazon Bedrock.

With Daybreak Access, defenders can use frontier cyber models within their existing AWS environments. Daybreak Blue and Daybreak Red access levels are both available in AWS:

**Daybreak Blue**provides access to frontier general-purpose models, including GPT‑5.6 Sol, with safeguards tailored to authorized defensive security work.**Daybreak Red**provides access to our purpose-trained cybersecurity models for authorized vulnerability research, exploit validation, and security testing.

These models help accelerate vulnerability research, detection engineering, and incident response, from initial discovery through a validated fix. They also support complex workflows such as exploit reproduction and mitigation development.

For enterprises, adopting specialized cybersecurity capabilities requires more than model performance. It also requires security review, governance, procurement, access controls, and an operating model teams can support.

Through Amazon Bedrock, eligible customers can use Daybreak, including Daybreak Red and Daybreak Blue, within the AWS environments where they already build, secure, and operate software. This gives security teams a clearer path to apply frontier AI through familiar AWS security, governance, and operational workflows.

Together, OpenAI and AWS are helping more organizations put advanced cybersecurity capabilities to work in production.

Daybreak Red and Daybreak Blue require enrollment in Daybreak Access. Once approved, you can access the model through the Amazon Bedrock console or the Responses API using the bedrock-mantle endpoint. To learn more, see the documentation.(opens in a new window)