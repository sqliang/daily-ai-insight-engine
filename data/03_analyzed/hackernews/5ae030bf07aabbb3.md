---
title: Qwen 3.8
source: https://twitter.com/Alibaba_Qwen/status/2078759124914098291
author:
- '[[nh43215rgb]]'
published: '2026-07-19'
created: '2026-07-20'
manifest_dates:
- '2026-07-20'
description: 'https://www.qwencloud.com/pricing/token-plan Comments URL: https://news.ycombinator.com/item?id=48966120
  Points: 878 # Comments: 604'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 5ae030bf07aabbb3
source_type: community_discussion
tldr: 阿里巴巴通义千问团队宣布 Qwen 3.8 模型即将发布并以开放权重形式开源，该模型拥有 2.4T 参数，其预览版 Qwen3.8-Max-Preview
  已在 Token Plan、Qoder 和 QoderWork 平台上线供用户试用。
objective_summary: 阿里巴巴通义千问团队于 2026 年 7 月 21 日在 Twitter 上宣布，Qwen 3.8 模型即将发布并以开放权重形式开源。该模型拥有
  2.4T 参数，团队称其性能接近前沿 AI 模型，仅次于 Fable 5。模型预览版 Qwen3.8-Max-Preview 已率先在阿里旗下的 Token Plan、Qoder
  和 QoderWork 平台上架，用户可立即试用。
event_type: infrastructure_update
epistemic_status: pr_statement
entities:
  companies:
  - Alibaba
  - Alibaba Cloud
  technologies:
  - Qwen 3.8
  - Qwen3.8-Max-Preview
  key_people: []
key_logic_flow:
- 阿里巴巴通义千问团队宣布 Qwen 3.8 模型即将发布，并计划以开放权重形式开源。
- 该模型拥有 2.4T 参数，官方声称其性能接近前沿 AI 模型，仅次于 Fable 5。
- 预览版 Qwen3.8-Max-Preview 已在阿里旗下的 Token Plan、Qoder 和 QoderWork 三个平台上线。
- 用户可通过国际站 qwencloud.com 和中国站 platform.qianwenai.com 的 Token Plan 定价页面获取使用入口。
object_mentions:
- object_type: model
  name: Qwen 3.8
  canonical_name: Qwen 3.8
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 阿里巴巴通义千问团队宣布 Qwen 3.8 即将发布并以开放权重形式开源。
  - Qwen 3.8 拥有 2.4T 参数，团队称其性能接近前沿 AI 模型，仅次于 Fable 5。
  article_id: 5ae030bf07aabbb3
- object_type: product
  name: Qwen3.8-Max-Preview
  canonical_name: Qwen3.8-Max-Preview
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Qwen3.8-Max-Preview 已率先在阿里旗下的 Token Plan、Qoder 和 QoderWork 平台上线。
  - 用户无需等待完整发布即可立即试用 Qwen3.8-Max-Preview 版本。
  article_id: 5ae030bf07aabbb3
- object_type: product
  name: Token Plan
  canonical_name: Token Plan
  url: https://qwencloud.com/pricing/token-plan
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - Qwen3.8-Max-Preview 已在阿里的 Token Plan 平台上架供用户试用。
  - 国际用户可通过 qwencloud.com/pricing/token-plan 访问 Token Plan 定价页面。
  article_id: 5ae030bf07aabbb3
- object_type: product
  name: Qoder
  canonical_name: Qoder
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - Qwen3.8-Max-Preview 预览版已上架 Qoder 平台，用户可率先体验。
  article_id: 5ae030bf07aabbb3
- object_type: product
  name: QoderWork
  canonical_name: QoderWork
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - Qwen3.8-Max-Preview 预览版同时在 QoderWork 平台上线供用户使用。
  article_id: 5ae030bf07aabbb3
extract_result: success
impact_score:
  score: 7.8
  reason: 2.4T 参数的开源模型如果属实，将远超当前最大开源模型（Llama 3 405B、DeepSeek V3 671B），可能重新定义开源 LLM
    的能力天花板，对闭源前沿模型形成直接竞争压力。但该消息仅为一则 Twitter PR 声明，认识论状态为 pr_statement，缺乏独立基准测试和第三方验证，具体性能水分待模型正式发布后检验。综合重要性高但确定性不足，给予
    7.8 分。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 2.4T 开源模型的实际 Benchmark 表现、推理成本与硬件门槛
hype_assessment:
  level: medium
  reason: 官方声称'仅次于 Fable 5'是典型的 PR 对比话术（借助知名前沿模型抬高定位），但 2.4T 参数量级明确且预览版已在三个平台实际上线，提供了实质性支撑，并非纯概念炒作。存在一定包装但干货基础扎实。
information_entropy: low
domain_disruption:
  technical_innovation: 2.4T 参数的开源大模型（推测采用 MoE 架构以平衡总参数量与推理效率），若验证有效将大幅推高开源模型能力上限，迫使其他开源项目跟进参数量级竞赛
  business_model: 开放权重策略直接对闭源前沿模型形成降维打击——以远低于 API 调用的成本提供接近前沿水平的模型权重，加速 AI 模型商品化进程，可能引发新一轮开源
    vs 闭源定价博弈
engineering_complexity: production_ready
compound_value:
  score: 8.0
  reason: Qwen 系列已建立起持续开源大模型的可靠节奏（Qwen→Qwen2→Qwen2.5→Qwen3→Qwen3.8），每次发布都在积累社区生态和开发者信任。2.4T
    参数规模的开放权重模型若性能真如宣称的'仅次于 Fable 5'，将是开源模型对闭源前沿模型的一次重大逼近。开源权重策略形成经典飞轮效应：更多开发者使用和微调
    → 更多衍生模型和社区贡献 → 模型质量进一步提升 → 吸引更多用户。阿里巴巴通过 Token Plan / Qoder / QoderWork + 阿里云底座实现流量变现和平台锁定，而非依赖模型
    API 收费，这为持续投入提供了可持续的商业闭环。长期看，Qwen 有潜力成为 AI 开源生态的'Linux 级'基础设施。风险点在于性能宣称尚未经第三方独立验证，且
    2.4T 参数的开源模型推理成本极高，实际可用性可能受限于硬件门槛。
value_capture_layer: foundation_model
moat_impact: creates_new_moat
key_beneficiaries:
- Alibaba Cloud
- Alibaba
- Qwen 社区开发者
- Token Plan / Qoder 平台用户
- 开源 AI 生态
competitive_casualty:
- OpenAI
- Anthropic
- 中国中小 AI 初创公司（智谱、百川等）
- 闭源高定价推理 API 提供商
market_opportunities:
- 企业可基于 Qwen 3.8 的开放权重进行垂直领域微调，尤其在中文法律、医疗、金融等高价值场景中构建私有化部署的行业大模型
- 模型推理优化与部署服务商可针对 2.4T 参数规模开发模型量化、蒸馏和分布式推理方案，降低企业使用超大规模开源模型的硬件门槛
- 阿里生态内的开发者可借助 Token Plan、Qoder 等平台率先体验并构建 AI 原生应用，抢占基于 Qwen 3.8 的插件与工具链生态位
risk_matrix:
  regulatory: 中美 AI 芯片与模型出口管制可能影响 Qwen 3.8 的国际分发与跨境使用；中国境内 AI 监管备案要求可能限制该模型在特定行业的商用部署
  technological: 2.4T 参数量的实际推理成本极高，多数开发者缺乏运行该规模模型的硬件条件；官方性能声称（仅次于 Fable 5）尚需第三方基准验证，存在宣传夸大的可能性
  competitive: Meta Llama 系列、Fable 等前沿开源模型已占据开发者心智，且 Qwen 3.8 发布时机较晚，面临开源社区生态挤压和用户迁移成本的双重挑战
  ethical: 超大规模开放权重模型显著降低滥用门槛，可能被用于生成深度伪造内容、自动化网络攻击或大规模虚假信息传播，且内容审查难度随参数规模剧增
  additional: []
confidence:
  impact: medium
  compound: medium
  hype: high
actionable_insight: monitor
object_insights:
- object_type: product
  name: Qwen3.8-Max-Preview
  canonical_name: Qwen3.8-Max-Preview
  url: null
  positioning: Qwen3.8-Max-Preview 是阿里通义千问团队推出的 Qwen 3.8 模型预览版，拥有 2.4T 参数且即将开放权重开源，当前已在
    Token Plan、Qoder 等平台上线供用户体验。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - AI 开发者与研究者
  - 大模型应用开发者
  - 需要前沿开源模型的团队
  product_signal: Qwen3.8-Max-Preview 已在阿里旗下 Token Plan、Qoder 和 QoderWork 三个平台同步上线，用户可立即试用无需等待完整发布。
  market_signal: 官方声称 Qwen3.8 性能接近前沿 AI 模型，仅次于 Fable 5，表明其在大模型竞技场中具备强劲竞争力。
  differentiation: 2.4T 参数的庞大规模配合即将开放权重的开源策略，Qwen 3.8 有望成为当前最大的开源模型之一。
  watch_reason: Qwen 3.8 以 2.4T 参数规模冲击开源大模型天花板，性能声称仅次于 Fable 5，其正式发布后的开源影响力及社区采用情况值得持续跟踪。
  risk_notes:
  - 模型尚处于预览阶段，正式发布后的实际性能表现有待第三方评测验证。
  - 2.4T 参数的部署成本极高，可能限制其实际应用场景和开发者的采用范围。
  score: 8.0
  article_ids:
  - 5ae030bf07aabbb3
  evidence_snippets:
  - Qwen3.8-Max-Preview 已率先在阿里旗下的 Token Plan、Qoder 和 QoderWork 平台上线。
  - 用户无需等待完整发布即可立即试用 Qwen3.8-Max-Preview 版本。
---

Qwen3.8 is launching and going open-weight soon!🌐
With a massive 2.4T parameters, this model is continuously evolving. We believe it’s one of the most powerful model available today, compatible to leading frontier AI models , second only to Fable 5.
You don't have to wait to test it. Just now, the Qwen3.8-Max-Preview made its debut on Alibaba’s Token Plan, Qoder, and QoderWork. Be among the very first to try it out.
Can't wait to hear what you build. Stay tuned! 🚀
Token Plan
international：qwencloud.com/pricing/token-…
China：platform.qianwenai.com/pricing/token-…