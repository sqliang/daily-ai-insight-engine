---
title: 不同模型厂同一家Agentic Infra，AGI时代的地基终于浮出水面
source: https://www.qbitai.com/2026/07/455805.html
author:
- '[[克雷西]]'
published: '2026-07-20'
created: '2026-07-21'
manifest_dates:
- '2026-07-21'
description: 大模型时代的共同选择
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 7bd242eb59bedf3d
source_type: news_media
tldr: 无问芯穹成为Kimi、智谱、MiniMax、阶跃星辰四家国产头部大模型公司的共同AI Infra合作伙伴，其Agentic MaaS平台日均Token调用量半年增长40倍。公司发布跨集群异构PD分离架构和智算集群运维智能体系统等核心技术，已部署触及37000P算力并覆盖16种主流芯片。
objective_summary: 无问芯穹在2026年WAIC上宣布与MiniMax签署战略合作，并邀请阶跃星辰发表主旨演讲，此前已为Kimi和智谱提供AI Infra服务，成为四家不同国产大模型公司的共同选择。该公司发布跨集群异构PD分离架构，实测首Token延迟降低51.5%、单Token成本降低37.5%，同时推出智算集群运维智能体系统实现故障自愈。截至2026年7月，其Agentic
  MaaS平台日均Token调用量较去年12月增长40倍，已部署37000P算力并覆盖16种主流芯片。
event_type: infrastructure_update
epistemic_status: pr_statement
entities:
  companies:
  - 无问芯穹
  - MiniMax
  - 阶跃星辰
  - 智谱
  - Kimi
  - 上海移动
  - 观猹
  technologies:
  - Agentic Infra
  - Agentic MaaS
  - PD分离
  - PDD架构
  - KV Cache
  - Radix Cache
  - 跨集群强化学习
  - Token工厂
  key_people:
  - 张鹏
  - 杨植麟
key_logic_flow:
- 无问芯穹已与四家国产头部大模型公司（Kimi、智谱、MiniMax、阶跃星辰）达成深度合作，成为多家不同模型厂商共同选择的AI Infra基础设施供应商。
- 2026年推理需求超过训练成为AI算力消耗主战场，中国日均Token调用量突破140万亿，但算力供给仍呈线性增长，形成供需缺口。
- 无问芯穹发布跨集群异构PD分离架构，将Prefill和Decode拆解部署，首创PDD三级链路（P、RelayDecode、MainDecode）解决广域网传输延迟问题。
- 无问芯穹推出智算集群运维智能体系统，实现7×24小时全天候值守和故障自愈，运维人效提升5倍以上、关键故障处理效率提升6倍。
- 无问芯穹构建"前店后厂一中心"体系：算力集散中心（Agentic Infra平台，37000P算力、16种芯片）、Token工厂（Agentic MaaS平台）和AI生产力商店（行业解决方案）。
- 无问芯穹实现了跨集群强化学习连续一周0中断稳定运行，并计划将跨域计算资源支撑规模拓展至十万卡以上。
object_mentions:
- object_type: product
  name: Agentic Infra 自主式基础设施平台
  canonical_name: 无问芯穹 Agentic Infra
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 一中心指的是「算力集散中心」，即Agentic Infra自主式基础设施平台，核心目标是实现智能资源规模最大化。
  - 这个集散中心已部署触达37000P算力，覆盖接入16种主流芯片。
  - 无问芯穹实现了跨集群强化学习连续一周0中断稳定运行，并计划拓展至十万卡以上规模。
  article_id: 7bd242eb59bedf3d
- object_type: product
  name: Agentic MaaS 大模型服务平台
  canonical_name: 无问芯穹 Agentic MaaS
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 后厂也就是「Token工厂」，即Agentic MaaS大模型服务平台，核心思路是「在规模之上向效率要产能」。
  - 截至7月，无问芯穹Agentic MaaS平台的日均Token调用量，较去年12月涨了40倍。
  article_id: 7bd242eb59bedf3d
- object_type: project
  name: 跨集群异构PD分离架构
  canonical_name: 跨集群异构PD分离架构
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 无问芯穹在今年WAIC官宣了一项自研的硬技术——跨集群异构PD分离，把Prefill和Decode拆开部署让不同芯片干各自最擅长的事。
  - 无问芯穹首创PDD架构，把传统PD链路拆成P、RelayDecode、MainDecode三级，解决了广域网传输延迟问题。
  - 实测该架构在首Token延迟降低51.5%的同时，单Token成本可降低37.5%。
  article_id: 7bd242eb59bedf3d
- object_type: product
  name: 智算集群运维智能体系统
  canonical_name: 智算集群运维智能体系统
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 无问芯穹这次发布了「智算集群运维智能体系统」，能够端到端地解决实际生产场景中的运维难题。
  - 该系统实现7×24小时全天候值守，运维人效提升5倍以上，关键故障处理效率提升6倍。
  article_id: 7bd242eb59bedf3d
- object_type: product
  name: 天问模型服务门户
  canonical_name: 天问
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 无问芯穹与上海移动联合打造了「天问」模型服务门户，作为面向企业用户的模型服务入口。
  article_id: 7bd242eb59bedf3d
- object_type: product
  name: TokenDance
  canonical_name: TokenDance
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 无问芯穹联合观猹做了一个面向开发者的「TokenDance」，对标OpenRouter。
  article_id: 7bd242eb59bedf3d
extract_result: success
impact_score:
  score: 7.0
  reason: 该事件标志着国产AI Infra层出现了一个跨模型厂商的公共基础设施选择。无问芯穹同时拿下Kimi、智谱、MiniMax、阶跃星辰四家竞争关系的头部大模型公司，这在当前碎片化的国产芯片生态和算力供需缺口背景下具有标志性意义。技术层面，跨集群异构PD分离架构（PDD三级链路）和首Token延迟降低51.5%、单Token成本降低37.5%的实测数据属于扎实的工程突破，但并非范式级创新——类似PD分离概念在业界已有探索。40倍Token调用量增长和37000P部署规模说明其已跨越早期验证阶段。综合评定：对国产AI生态竞争格局有实质改变，但影响范围主要在国内，未达到全球范式转移级别。
sentiment: neutral
developer_sentiment:
  tone: neutral
  primary_focus: 跨集群PD分离架构的实际效果和API调用成本是否真的能降低37.5%
hype_assessment:
  level: medium
  reason: 文章存在明显PR包装：'AGI时代的地基终于浮出水面''集齐四家就可以召唤神龙''大模型时代的共同选择'等修辞属于典型的概念炒作话术。'电池领域的宁德时代'类比也过度拔高其市场地位。但技术指标（TTFT降低51.5%、成本降低37.5%、40倍增长、37000P算力）有具体数据支撑，并非空谈。判定为中等水分——实质进展有，但表述方式存在显著放大。
information_entropy: medium
domain_disruption:
  technical_innovation: 跨集群异构PD分离架构是本文最值得关注的技术突破。将Prefill和Decode拆解到不同集群的异构芯片上执行，并首创PDD三级链路（Prefill→RelayDecode→MainDecode），利用RelayDecode在广域网传输KV
    Cache期间先行输出Token来掩盖数十秒级的网络延迟，同时将Radix Cache迁移到跨集群场景使传输数据量降低一个数量级。这套方案在工程层面解决了异构芯片间广域网推理的延迟不可控问题，属于系统架构层面的巧妙创新。
  business_model: 无问芯穹正在构建'模型厂商的公共基础设施层'商业模式，对标宁德时代在电池领域的生态位——让互相竞争的大模型厂商共享底层Infra。这种模式在碎片化的国产芯片生态中具有天然护城河：芯片适配工作量是沉没成本，一旦接入便形成锁定效应。与上海移动合作推出'天问'门户、与观猹推出对标OpenRouter的TokenDance，说明其正在从纯基础设施向AI分发平台延伸，构建算力→Token→应用的完整价值链路。
engineering_complexity: infrastructure
compound_value:
  score: 8.0
  reason: 无问芯穹构建了罕见的'多模型厂商共同选择'的基础设施层位，四家互相竞争的国产头部基模公司（Kimi、智谱、MiniMax、阶跃星辰）同时深度绑定同一家Infra，形成了类似宁德时代在电池领域的'绕不开'卡位效应。这种跨厂商基础设施锁定创造强劲网络效应：支持的芯片种类越多（当前16种）、服务的客户模型越多、日均Token调用量半年增长40倍，平台的异构优化数据飞轮持续增强。跨集群PD分离架构（TTFT降低51.5%、单Token成本降低37.5%）、跨域强化学习连续一周0中断运行等核心技术构成工程壁垒。从VC视角看，这是AI推理需求爆发期'卖铲子'的稀缺标的——中国日均Token调用量突破140万亿、推理成本两年降280倍但总支出反升，供需缺口持续扩大，平台型基础设施的复利效应明确。风险点：超大规模云厂商（阿里云/华为云）可能自建竞品、芯片出口管制带来的供应链不确定性、技术路线迭代（如架构替代PD分离）的长期风险。
value_capture_layer: cloud_platform
moat_impact: creates_new_moat
key_beneficiaries:
- 无问芯穹
- Kimi
- 智谱
- MiniMax
- 阶跃星辰
competitive_casualty:
- 传统云厂商AI推理业务
- 其他独立AI Infra创业公司
- 自建推理基础设施的二线模型厂商
market_opportunities:
- AI Infra 聚合服务商模式验证了跨芯片、跨集群的统一调度存在巨大市场空白，创业者可聚焦于为中小企业提供轻量级的 Agentic MaaS 平台或垂直行业部署方案
- 跨集群异构 PD 分离架构及其 PDD 三级链路设计代表了推理优化的前沿方向，技术团队可围绕 KV Cache 迁移、Radix Cache 创新等领域构建差异化推理加速工具
- 智算集群运维智能体（AIOps for AI）是一个高价值细分赛道，将故障自愈与运维自动化封装为标准化产品，可面向中型算力中心提供 7×24 小时运维方案
risk_matrix:
  regulatory: 美国对华芯片出口管制可能影响无问芯穹覆盖的 16 种芯片供应链稳定性，同时中国对算力基础设施的监管政策可能要求共享平台承担额外的合规审查与数据安全义务
  technological: PD 分离架构依赖特定的网络条件与芯片生态，若新一代芯片架构（如存算一体、Chiplet 互连）大幅降低异构调度需求，该技术路线可能被边缘化；跨域强化学习
    0 中断稳定性在大规模扩展（十万卡级）时面临严峻挑战
  competitive: 阿里云、华为云、腾讯云等云计算巨头可能以更低价格和更强生态捆绑提供同类 Agentic Infra 服务，英伟达自身的 AI Enterprise
    套件也可能挤压第三方 Infra 平台的生存空间
  ethical: 算力基础设施的集中化可能形成单点故障风险，多家头部模型公司依赖同一家 Infra 供应商，一旦平台出现系统性故障将对整个国产大模型生态造成连锁影响
  additional:
  - 该公司高度依赖与头部模型厂商的合作关系，若任一核心客户自建 Infra 将显著削弱其议价能力和规模效应
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: monitor
object_insights:
- object_type: product
  name: Agentic Infra 自主式基础设施平台
  canonical_name: 无问芯穹 Agentic Infra
  url: null
  positioning: 无问芯穹旗下的算力集散中心，汇聚并弹性调度37000P算力与16种主流芯片，为大模型及应用层提供稳定、可扩展的跨异构算力底座，目标是实现智能资源规模最大化。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 国产大模型公司
  - 需要大规模算力的AI企业
  product_signal: 已部署触达37000P算力并覆盖接入16种主流芯片，实现了跨集群强化学习连续一周0中断稳定运行。
  market_signal: 成为Kimi、智谱、MiniMax、阶跃星辰四家国产头部大模型公司的共同AI Infra合作伙伴，市场验证充分且不可替代性初步显现。
  differentiation: 以"跨集群异构"方案解决国产芯片生态碎片化难题，将Radix Cache迁移至跨架构并首创PDD三级链路，在算力规模之上实现效率优化。
  watch_reason: 无问芯穹成为四家不同技术路线头部大模型公司的共同AI Infra选择，且Agentic MaaS日均Token调用半年增长40倍，预示着AI
    Infra层正在形成统一底层标准，值得持续跟踪其跨域计算能否突破十万卡级别。
  risk_notes:
  - 跨集群调度技术复杂度极高，十万卡级别扩展面临网络、平台、框架三层的系统性挑战。
  - 国产芯片生态持续变动可能影响其硬件覆盖范围和兼容性维护成本。
  score: 9.0
  article_ids:
  - 7bd242eb59bedf3d
  evidence_snippets:
  - 一中心指的是「算力集散中心」，即Agentic Infra自主式基础设施平台，核心目标是实现智能资源规模最大化。
  - 这个集散中心已部署触达37000P算力，覆盖接入16种主流芯片。
  - 无问芯穹实现了跨集群强化学习连续一周0中断稳定运行，并计划拓展至十万卡以上规模。
- object_type: product
  name: Agentic MaaS 大模型服务平台
  canonical_name: 无问芯穹 Agentic MaaS
  url: null
  positioning: 无问芯穹旗下的"Token工厂"，在算力底座之上提供从网关、路由到推理实例的一站式服务技术栈，核心思路是在规模之上向效率要产能，实现模型部署的效果、成本与稳定性三重保障。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 大模型公司
  - AI应用开发企业
  - 需要大模型推理服务的客户
  product_signal: 截至7月日均Token调用量较去年12月增长40倍，与多家头部大模型公司深度合作打磨推理效率和服务稳定性。
  market_signal: 在推理需求超越训练成为AI算力主战场的背景下，面向Kimi、智谱、MiniMax、阶跃星辰等头部客户提供服务，规模增长势头强劲。
  differentiation: 建立准入测试标准确保模型精度与原厂API一致，结合PD分离架构实测首Token延迟降低51.5%且单Token成本降低37.5%。
  watch_reason: 日均Token调用半年增长40倍，在推理需求超越训练的时代背景下作为多家头部模型厂的共同MaaS平台，其增长曲线直接反映AI Infra行业的规模化进程和定价趋势。
  risk_notes:
  - MaaS赛道竞争激烈，阿里云、华为云等云厂商同样在积极布局类似服务。
  - 价格战可能压缩利润空间，且客户集中度较高存在依赖风险。
  score: 8.0
  article_ids:
  - 7bd242eb59bedf3d
  evidence_snippets:
  - 后厂也就是「Token工厂」，即Agentic MaaS大模型服务平台，核心思路是「在规模之上向效率要产能」。
  - 截至7月，无问芯穹Agentic MaaS平台的日均Token调用量，较去年12月涨了40倍。
- object_type: project
  name: 跨集群异构PD分离架构
  canonical_name: 跨集群异构PD分离架构
  url: null
  positioning: 无问芯穹自研的推理优化架构，将Prefill和Decode拆解到不同芯片集群独立部署，首创PDD三级链路解决广域网传输延迟难题，实现成本与延迟双降。
  technical_signal: 首创PDD架构将传统PD链路拆为P、RelayDecode、MainDecode三级，并将Radix Cache迁移到跨集群架构使传输数据量降低一个数量级。
  adoption_signal: 已在Agentic MaaS平台部署服务Kimi、智谱、MiniMax、阶跃星辰等头部客户，实测首Token延迟降低51.5%、单Token成本降低37.5%。
  ecosystem_relevance: 面向国产芯片生态碎片化现状，通过异构调度让不同类型芯片各自发挥优势，为国产算力集群提供可规模化的高效落地方案。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 首创的PDD三级链路是解决跨集群推理延迟难题的关键技术路径，首Token延迟降51.5%与成本降37.5%的双重优化效果使其成为AI
    Infra领域最值得关注的核心技术突破之一。
  risk_notes:
  - 跨集群PD分离依赖广域网传输，异构芯片间的通信兼容性可能成为扩展瓶颈。
  - RelayDecode机制在极致高并发场景下的可靠性和切回延迟有待持续验证。
  score: 8.0
  article_ids:
  - 7bd242eb59bedf3d
  evidence_snippets:
  - 无问芯穹在今年WAIC官宣了一项自研的硬技术——跨集群异构PD分离，把Prefill和Decode拆开部署让不同芯片干各自最擅长的事。
  - 无问芯穹首创PDD架构，把传统PD链路拆成P、RelayDecode、MainDecode三级，解决了广域网传输延迟问题。
  - 实测该架构在首Token延迟降低51.5%的同时，单Token成本可降低37.5%。
- object_type: product
  name: 智算集群运维智能体系统
  canonical_name: 智算集群运维智能体系统
  url: null
  positioning: 无问芯穹推出的智算集群运维解决方案，利用AI智能体实现7×24小时全天候值守和故障自愈，将运维范式从"人找问题"转变为"问题自动解决"。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 智算中心运维团队
  - 大模型公司基础设施部门
  product_signal: 实现7×24小时全天候值守，运维人效提升5倍以上，关键故障处理效率提升6倍，可端到端解决实际生产中的运维难题。
  market_signal: 作为无问芯穹服务头部大模型客户的配套基础设施能力，在大型智算集群从万卡向十万卡扩展的背景下需求明确。
  differentiation: 将智能体技术深度应用于智算集群运维，实现从故障检测到自愈的全流程自动化，切换了"人找问题"到"问题找人"的运维范式。
  watch_reason: 随着国产大模型集群规模持续扩张，运维智能体将成为智算基础设施的关键组成部分，其故障自愈能力和人效提升数据值得追踪行业落地效果。
  risk_notes:
  - 智能体系统在复杂故障场景下的自愈能力边界尚未公开披露。
  - 高度自动化运维可能引入新的系统级风险，人工兜底机制的设计至关重要。
  score: 6.0
  article_ids:
  - 7bd242eb59bedf3d
  evidence_snippets:
  - 无问芯穹这次发布了「智算集群运维智能体系统」，能够端到端地解决实际生产场景中的运维难题。
  - 该系统实现7×24小时全天候值守，运维人效提升5倍以上，关键故障处理效率提升6倍。
- object_type: product
  name: 天问模型服务门户
  canonical_name: 天问
  url: null
  positioning: 无问芯穹与上海移动联合打造的企业级模型服务门户，作为面向企业用户的模型服务统一入口，将Agentic MaaS能力向企业端规模化输出。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 企业级AI模型用户
  - 上海移动企业客户
  product_signal: 由无问芯穹与上海移动联合打造，作为面向企业用户的模型服务入口，将Agentic MaaS能力通过运营商渠道向企业端输出。
  market_signal: 通过与上海移动合作切入运营商生态，借助其企业客户资源拓展B端市场，但公开的用户规模和业务效果数据有限。
  differentiation: 以运营商联合运营模式构建企业模型服务入口，区别于纯线上MaaS平台，获客渠道具有独占性优势。
  watch_reason: 作为无问芯穹与运营商合作的B端模型服务门户，其企业获客模式和实际落地效果是观察AI Infra行业To B渠道拓展路径的重要样本。
  risk_notes:
  - 公开信息极少，尚不清楚实际用户规模和业务效果，判断为早期试水阶段。
  - 运营商合作模式的系统灵活性和产品迭代速度可能慢于纯互联网模式。
  score: 4.0
  article_ids:
  - 7bd242eb59bedf3d
  evidence_snippets:
  - 无问芯穹与上海移动联合打造了「天问」模型服务门户，作为面向企业用户的模型服务入口。
- object_type: product
  name: TokenDance
  canonical_name: TokenDance
  url: null
  positioning: 无问芯穹联合观猹推出的面向开发者的多模型统一调用入口，对标OpenRouter，提供一站式模型API聚合服务。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - AI应用开发者
  - 需要多模型调用的技术团队
  product_signal: 对标OpenRouter，面向开发者提供多模型统一调用服务，是无问芯穹在开发者生态领域的重要布局尝试。
  market_signal: 对标OpenRouter的模式跟随海外趋势，但国内市场对类似聚合服务的需求规模和付费意愿尚不明确。
  differentiation: 依托无问芯穹底层算力池与多家头部模型厂商的合作关系，在成本和服务质量上可能具备独特优势。
  watch_reason: 作为中国市场对标OpenRouter的重要尝试，TokenDance通过统一接口聚合多家模型服务，其能否在国内复制OpenRouter的成功值得持续关注。
  risk_notes:
  - 公开信息极为有限，产品尚处于早期验证阶段。
  - OpenRouter模式在国内面临合规要求和变现模式的挑战。
  score: 4.0
  article_ids:
  - 7bd242eb59bedf3d
  evidence_snippets:
  - 无问芯穹联合观猹做了一个面向开发者的「TokenDance」，对标OpenRouter。
---

# 不同模型厂同一家Agentic Infra，AGI时代的地基终于浮出水面

大模型时代的共同选择

##### 克雷西 发自 上海

量子位 | 公众号 QbitAI

先说一件有意思的事。

就在今天的WAIC论坛上，MiniMax和阶跃星辰，同时出现在了一家AI Infra公司的论坛现场，前者参加战略合作签约，后者发布主旨演讲。

苗头其实更早就出现了。4个月前的中关村论坛上，智谱张鹏和Kimi杨植麟就曾与这家公司联合创始人兼CEO同框，参与圆桌论坛，并被现场点名该公司已为Kimi、智谱提供服务。

四家国产头部基模公司，先后跟同一家AI Infra达成了深度合作。开句玩笑话——集齐四家，就可以召唤神龙了。

这家AI Infra公司，正是**无问芯穹**。

这个身位有点像「电池领域的宁德时代」——造车的人可以「兄弟登山，各自努力」，但电池这一层，绕不开就是绕不开。无问芯穹想做的，就是**大模型时代的共同选择**。

问题也因此变得更有趣了：

他们到底看中了这家公司什么？

答案要从两头找。

**需求端**，2026年推理开始反超训练，成为AI算力消耗的主战场，推理成本两年降了280倍，企业的AI总支出却没降反升，中国日均Token调用量已经突破140万亿，一年涨了四成，需求呈指数级往上冲。

**供给端**却完全是另一副面孔。物理算力的扩产逻辑还是线性的，多修几个机房、多买几张卡，缺口却在三五年内都填不平。

一边指数增长，一边线性爬坡，中间那道口子，就是无问芯穹想站进去的位置。

更难的是，模型部署得好不好，外人很难判断。

一个请求发下去，模型正常回复了，但输出的精度可能已经悄悄掉了三成，这种问题常规监控查不出来。

等到用户在业务里察觉到不对劲，模型的招牌已经砸了。

这道看不见的门槛，才会真正决定哪家供应商能留在牌桌上。

## 为什么国产大模型优选无问芯穹？

Token经济全面爆发以来，推理需求正在加速，算力缺口也在持续扩大。

但MaaS这门生意的门槛，比外界想象的高得多。

Kimi、智谱、MiniMax、阶跃星辰为什么都点了头，自然有他们自己的算盘，但本质上是同时把三件事押了上去——

**比如：模型效果会不会打折，成本烧不烧得起，出了问题稳不稳得住。**

先说**效果**。

前面提到的那种隐蔽滑坡，是这个行业最让人头疼的地方。

有第三方供应商部署模型后，精度比原厂掉了30%，客户自己甚至察觉不到，直到业务指标开始下滑才回头排查。

无问芯穹在这件事上的做法，是定了一套准入测试标准。

这套标准，会从工具调用的一致性，到推理模式的精度对齐，逐项进行核验，每一个新模型上架前都要过这道关。

结果是，客户无论走无问芯穹还是原厂API，体验几乎感觉不到差别。

再来是**成本**。

无问芯穹在今年WAIC官宣了一项自研的硬技术——跨集群异构PD分离。

大模型推理里的Prefill和Decode是两个负载完全不同的阶段，硬件需求也不一样，拆开部署能让不同类型的芯片各自干最擅长的事。

但拆到不同机房后，会撞上一个新问题。

PD分离之后，需要在异构芯片之间用广域网以太网传输KV Cache，面临着带宽低、延迟高的情况，等于两个接力选手各自都跑得很出色，但在交棒的时候，却掉了链子。

为此，无问芯穹首先把Decode实例设计的Radix Cache技术，创新性地迁移到了这套跨集群架构里，让传输的数据量直接降低一个数量级。

接着，他们又首创了PDD架构，把传统的PD链路拆成P、RelayDecode、MainDecode三级。

遇到传输延迟高的请求，RelayDecode先顶上去把Token吐给用户，用户完全感觉不到这段实际长达数十秒的延迟，等数据传完，再无缝切给MainDecode接手。

实测显示，该架构在首Token延迟（TTFT）降低51.5%的同时，单Token成本可降低37.5%。

最后是**稳定性**。

集群规模一大，故障往往藏得很深。

大模型推理背后要管理数十上百个集群，扛住全国每天上T规模的流量分发，服务器一旦宕机，靠人盯着屏幕根本来不及反应。

无问芯穹这次发布了“智算集群运维智能体系统”，能够端到端地解决实际生产场景中的运维难题，7×24小时全天候值守，让智算集群的运维从“人找问题”转变为“问题找人”，和“问题自己解决”，实现了运维人效提升5倍以上，关键故障处理效率提升6倍。

## 前店后厂一中心，构建系统竞争力

三件事都解决了，仅仅只是构成了Token工厂这一层的地基。

无问芯穹真正要交出去的答卷，是把算力、Token、生产力串成一个完整的系统，对应它自己提出的那个公式——

**AI生产力 = 智能资源规模 × Token转化效率 × AI生产力转化效率。**

一中心，指的是**「算力集散中心」**，即Agentic Infra自主式基础设施平台。

国产芯片生态天然碎片化，无问芯穹把散落各处的算力资源统一汇聚、弹性调度、按需利用，为模型与应用层筑牢充足、稳定、可扩展的算力底座。核心目标非常明确：实现智能资源规模最大化。

这个集散中心已部署触达**37000P算力**，覆盖接入**16种主流芯片**。

跨集群强化学习的挑战，同样是在这一层被啃下来的。无问芯穹认为，在Post-training的Scaling Law持续发展的当下，强化学习成为解锁智能的关键。

其算力需求的硬件种类更加复杂，规模量级也更加庞大，基于异构和超大算力规模的双重刚需，跨集群强化学习因此成为智能规模化及持续进化的新锚点，这也是无问芯穹Agentic Infra自主式基础设施平台重点布局与攻克的核心场景。

无问芯穹把网络、平台、框架三层的优化贯穿到底，成功实现了跨域强化学习训练连续一周0中断稳定运行，让大规模跨域强化学习不仅可以“跑得通”，还能“跑得快、跑得稳”。

未来，无问芯穹还将针对并行策略、通信融合、智能算子、极致容错等核心技术持续深耕，将跨域计算资源的支撑规模，持续拓展至十万卡级以上。

后厂，也就是**「Token工厂」**，即Agentic MaaS大模型服务平台。

这是前面讲的效果、成本、稳定性三重优势真正兑现的地方，核心思路是“在规模之上向效率要产能”，也是一整套从网关、路由到底层推理实例的完整服务技术栈，“层层可优化、处处有增量”。

在这个「工厂」里，除了上文提到的新技术“跨集群异构PD分离架构”，无问芯穹还和多家头部大模型公司深度合作，在真实业务场景里持续打磨推理效率和服务稳定性，业务规模又反过来推动技术迭代得更快。

公司官宣：截至7月，无问芯穹Agentic MaaS平台的日均Token调用量，较去年12月涨了40倍。

它还与上海移动联合打造了“天问”模型服务门户，联合观猹做了一个面向开发者的「TokenDance」，对标OpenRouter。

前店，是把攒下的能力覆盖千行百业的**「AI生产力商店」**，即Agentic Infra行业解决方案。

这套解决方案已覆盖文娱游戏、医疗健康、法律终端、能源电力等多个行业领域，把技术势能全面转化为各行业能用、好用、可复用的落地价值。