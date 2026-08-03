---
title: Pokémon Go Scans Trained the Navigation Tech for Military Drones
source: https://dronexl.co/2026/06/09/pokemon-go-scans-niantic-vantor-military-drone-navigation/
author:
- '[[vrganj]]'
published: '2026-06-11'
created: '2026-06-11'
description: 'Article URL: https://dronexl.co/2026/06/09/pokemon-go-scans-niantic-vantor-military-drone-navigation/
  Comments URL: https://news.ycombinator.com/item?id=48487029 Points: 201 # Comments:
  75'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 55dffce3e3a7dc73
source_type: community_discussion
tldr: 《精灵宝可梦Go》玩家拍摄的约300亿张环境扫描数据被Niantic Spatial用于训练视觉定位系统（VPS），该系统已通过与国防承包商Vantor的合作，将部署于GPS受干扰环境下的军用无人机和机器人导航，而绝大多数玩家对此毫不知情。
objective_summary: 2025年12月16日，Niantic Spatial与国防承包商Vantor（前身为Maxar Intelligence）宣布合作，将其视觉定位系统与Vantor的Raptor空中导航软件融合，为军用无人机和机器人提供不依赖卫星信号的导航能力。该系统的训练数据来源于《精灵宝可梦Go》玩家自2021年以来拍摄的约300亿张环境扫描，玩家在游戏内授权条款中同意了可转让、可再许可的许可协议，但多数人未意识到数据最终流向军事用途。Vantor否认将直接使用游戏数据，但拒绝说明已部署的模型是否曾在训练中用过这些扫描，专家指出一旦数据融入模型便几乎无法追溯。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - Niantic Spatial
  - Vantor
  - Maxar Intelligence
  - Google
  - Keyhole
  - In-Q-Tel
  - Scopely
  - Savvy Games Group
  - Coco Robotics
  - Shield AI
  - DroneXL
  technologies:
  - VPS
  - Visual Positioning System
  - Raptor
  - GPS
  - GEOINT
  key_people:
  - Brian McClendon
  - John Hanke
  - Floris De Hingh
  - Jeroen van den Hoven
  - Iris Muis
  - Adrian Hon
  - Haye Kesteloo
key_logic_flow:
- 《精灵宝可梦Go》自2021年起要求玩家拍摄现实世界地点的短视频以获取游戏内奖励，玩家授予了Niantic可转让、可再许可的数据许可协议。
- Niantic Spatial利用约300亿张玩家扫描数据训练了视觉定位系统（VPS），该系统通过摄像头画面匹配3D地图来定位，无需GPS卫星信号。
- 2025年12月16日，Niantic Spatial与国防承包商Vantor宣布合作，将VPS与Vantor的Raptor空中导航软件融合，用于GPS受干扰环境下的军用无人机和机器人导航。
- Vantor否认将直接使用《精灵宝可梦Go》数据，但拒绝说明已部署的模型是否曾使用这些扫描数据进行训练，代尔夫特理工大学教授指出一旦数据融入模型便几乎无法追溯。
- Niantic的根源可追溯至2003年获得CIA旗下风投In-Q-Tel资助的地图公司Keyhole，后被谷歌收购，其技术基因与国防领域有长期关联。
- 2025年Niantic结构分拆中，游戏业务以35亿美元出售给沙特主权财富基金旗下的Scopely，技术平台独立为Niantic Spatial，地图数据流向国防领域。
extract_result: success
object_mentions:
- object_type: product
  name: Pokémon Go
  canonical_name: Pokémon Go
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 《精灵宝可梦Go》自2021年起要求玩家录制现实世界地点的短视频以获取游戏内奖励，Niantic由此获得了约300亿张环境扫描数据。
  - 玩家授予了可转让、可再许可的扫描数据许可协议，但绝大多数玩家未意识到这些数据最终被用于训练军用无人机导航系统。
  article_id: 55dffce3e3a7dc73
- object_type: product
  name: Niantic Spatial Visual Positioning System
  canonical_name: Niantic Spatial VPS
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Niantic Spatial利用约300亿张玩家扫描数据训练了视觉定位系统（VPS），通过摄像头画面匹配3D地图来在无GPS信号时确定位置。
  - CTO Brian McClendon表示该技术适用于GPS经常失效的密集城市和信号被刻意屏蔽的战场等环境。
  article_id: 55dffce3e3a7dc73
- object_type: product
  name: Vantor Raptor
  canonical_name: Vantor Raptor
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Vantor的Raptor软件于2025年2月发布，利用无人机摄像头和专有3D地形数据实现空中定位。
  - Raptor与Niantic VPS融合后，可在无卫星链路的情况下实现空中与地面设备的实时坐标共享。
  article_id: 55dffce3e3a7dc73
- object_type: product
  name: Ingress
  canonical_name: Ingress
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Niantic在2014年通过游戏Ingress就已收集玩家的相机图像数据，其方法与后续Pokémon Go使用的相同。
  article_id: 55dffce3e3a7dc73
- object_type: company
  name: Keyhole
  canonical_name: Keyhole
  url: null
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - Niantic脱胎于地理数据公司Keyhole，后者在2003年获得CIA旗下风投In-Q-Tel资助，其服务在伊拉克战争期间用于支持美军。
  - 谷歌于2004年收购Keyhole，Keyhole CEO John Hanke后来领导了谷歌地图和谷歌地球团队。
  article_id: 55dffce3e3a7dc73
- object_type: product
  name: FirePoint
  canonical_name: FirePoint
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 乌克兰的FirePoint在约三年内建立了七代导航系统，最终采用地形匹配方案，使用廉价夜视摄像头实现无GPS飞行。
  article_id: 55dffce3e3a7dc73
- object_type: product
  name: Shield AI V-BAT
  canonical_name: Shield AI V-BAT
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Shield AI的V-BAT无人机在无线电链路失效时仍能继续飞行，体现了无GPS视觉定位导航在军事领域的关键价值。
  article_id: 55dffce3e3a7dc73
impact_score:
  score: 6.0
  reason: 该事件并非AI模型或算法的技术突破，但其揭示的数据同意伦理危机具有深远的行业影响。Pokémon Go通过游戏奖励机制收集约300亿张环境扫描数据，用户授予了可转让、可再许可的权限，这些数据最终被训练为视觉定位系统(VPS)并整合到军事无人机导航中。这起事件将AI数据治理的'同意困境'推向公众视野——游戏用户无法预见其数据被用于武器系统，且一旦数据融入模型训练，追溯和删除几乎不可能。这对所有依赖UGC（用户生成内容）训练AI的公司的数据合规策略构成了实质性冲击，可能引发监管收紧和用户信任危机。评分理由：虽然不是技术范式转移，但数据伦理风暴可能改变行业的数据采集和许可实践。
sentiment: negative
developer_sentiment:
  tone: skeptical
  primary_focus: 用户生成数据的同意边界与军事化应用伦理
hype_assessment:
  level: low
  reason: 该报道来自行业媒体 dronexl.co 的调查性文章，采用事实驱动叙事而非营销语言。文中未出现'颠覆''革命性'等PR滥用词汇，而是以具体的日期（2025年12月16日合作公告）、具体数据（300亿张扫描、7000万美元合同）、具体人物引述（TU
    Delft伦理教授、荷兰玩家）支撑论述。Vantor否认直接使用但拒绝排除模型训练数据的模糊立场被如实呈现，没有过度渲染或耸人听闻。判定为低炒作度。
information_entropy: high
domain_disruption:
  technical_innovation: 视觉定位系统(VPS)通过匹配摄像头图像与3D世界模型实现GPS拒止环境下的精确定位，结合Vantor的Raptor空中导航软件实现空地协同定位。其技术本质是利用大规模众包视觉数据构建可搜索的3D空间索引，使无人机和地面装备在没有卫星信号时仍能共享统一坐标框架。
  business_model: 游戏公司通过'奖励式数据采集'积累海量高价值空间数据，随后将数据使用权通过可转让、可再许可的条款打包出售给国防承包商。这一模式揭示了AI时代数据货币化的新路径：面向消费者的应用（游戏/社交）作为数据采集前端，B2G（面向政府）的防务解决方案作为变现出口。Niantic分拆为游戏（被沙特收购）和地图技术（独立为Niantic
    Spatial）两个实体后，后者向防务领域转型，体现了空间数据资产的独立商业价值。
engineering_complexity: production_ready
compound_value:
  score: 7.5
  reason: VPS技术填补了一个根本性且日益严重的市场真空——GPS拒止环境下的自主导航。随着电子战和GPS干扰从战场扩散至民用空域，该需求确定性极高。Niantic
    Spatial拥有约300亿张实景扫描数据，这一数据护城河在可预见的未来几乎无法复制，形成极强的网络效应（更多扫描→更优模型→更多客户→更多扫描）。国防领域的政府合同提供稳定且长期的现金流（Vantor已持有NGA
    7000万美元合同），且VPS可横跨军用无人机、地面机器人、AR眼镜、自动驾驶等多个终端场景，TAM天花板高。但6分扣在：数据同意的伦理争议可能导致监管限制（欧盟GDPR追溯风险、数据使用权诉讼），且当前盈利模式高度依赖国防领域，民用商业化路径尚未验证。综合来看，这是GPS-denied导航赛道的潜在基础设施，但伦理和监管不确定性需要在后续轮次定价中充分折现。
value_capture_layer: agent_middleware
moat_impact: creates_new_moat
key_beneficiaries:
- Niantic Spatial
- Vantor
- Anduril
- Shield AI
competitive_casualty:
- 传统 GPS 导航方案提供商
- 缺乏大规模实景数据的 VPS 初创公司
- 纯民用地图技术公司
market_opportunities:
- 数据溯源与同意管理工具——开发AI训练数据生命周期追溯平台，帮助企业和监管机构验证数据是否在用户知情同意下收集，尤其适用于存在军事/防务二次用途争议的场景
- 视觉定位系统（VPS）在非军事场景的商用落地——仓库机器人、室内导航、自动驾驶城市峡谷等GPS盲区领域需求旺盛，Niantic Spatial的VPS技术有巨大商业化溢出潜力，创业者可聚焦物流、零售、智慧城市等垂直场景
- 消费者数据伦理审计咨询——随着公众对游戏/社交数据被用于武器系统警觉性上升，面向游戏公司、地图科技公司提供数据伦理风险评估和合规体系设计服务将成为刚需
risk_matrix:
  regulatory: GDPR目的限制原则风险：用户授权仅限于游戏内扫描，未明示军事/防务用途，Niantic的"可转让、可再许可"条款可能不满足GDPR第5条目的限制原则，欧盟用户可提起集体诉讼；欧美防务数据出口管制也可能限制该技术跨境部署
  technological: VPS面临替代性技术路线竞争：基于基础模型的视觉SLAM（如Meta、Google、Apple的替代方案）和低成本惯性导航方案均可实现GPS拒止导航，架构过时或被通用视觉模型替代的风险存在
  competitive: 地图与防务巨头同时挤压：Google（Street View+VPS）、Apple（ARKit定位）、Maxar原身竞品以及Palantir等防务AI公司均在布局同类能力，Niantic
    Spatial可能面临大厂数据规模和军方关系双重挤压
  ethical: 这是该事件的核心争议：约30亿张扫描数据由用户在不知情场景下贡献，数据最终流向军事无人机导航系统，用户无法追溯或撤回同意；这构成了典型的"知情同意缺口"和数据伦理滑坡，且一旦AI模型完成训练，原始数据贡献无法被移除或追责
  additional:
  - Niantic Spatial与Vantor之间的数据隔离声明模棱两可（否认直接使用但拒绝澄清模型是否曾使用扫描数据训练），这种不透明姿态可能引发更广泛的公众信任危机，进而波及其游戏业务（如Scopely运营下的Pokémon
    Go用户流失）
confidence:
  impact: high
  compound: medium
  hype: high
actionable_insight: deep_dive
object_insights:
- object_type: product
  name: Pokémon Go
  canonical_name: Pokémon Go
  url: null
  positioning: 一款基于增强现实技术的移动游戏，通过引导玩家拍摄现实环境来收集海量视觉数据。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 全球移动游戏玩家
  - 增强现实技术爱好者
  - 休闲游戏用户
  product_signal: Niantic自2021年起通过游戏内奖励机制收集了约300亿张玩家环境扫描数据，为视觉定位系统提供了训练基础。
  market_signal: 2025年游戏业务以35亿美元出售给沙特主权财富基金旗下的Scopely，技术平台独立为Niantic Spatial。
  differentiation: 通过游戏化激励机制在用户无感知的情况下采集大规模现实世界视觉数据，形成竞争对手难以复制的数据壁垒。
  watch_reason: 作为全球最成功的增强现实游戏之一，其用户生成的环境扫描数据被用于军事导航系统训练，揭示了消费级应用数据向国防领域流动的重大隐私与伦理风险，值得持续跟踪。
  risk_notes:
  - 绝大多数玩家未意识到其游戏内扫描数据最终流向军事无人机导航系统，存在重大信任危机。
  - 授权协议包含可转让和可再许可的数据使用条款，但多数用户未充分理解其含义及数据最终流向。
  score: 7.0
  article_ids:
  - 55dffce3e3a7dc73
  evidence_snippets:
  - 《精灵宝可梦Go》自2021年起要求玩家录制现实世界地点的短视频以获取游戏内奖励，Niantic由此获得了约300亿张环境扫描数据。
  - 玩家授予了可转让、可再许可的扫描数据许可协议，但绝大多数玩家未意识到这些数据最终被用于训练军用无人机导航系统。
- object_type: product
  name: Niantic Spatial Visual Positioning System
  canonical_name: Niantic Spatial VPS
  url: null
  positioning: 基于海量现实世界扫描数据训练的视觉定位系统，通过摄像头画面与三维地图匹配实现无GPS环境下的精准定位。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 军用无人机与机器人系统
  - 国防与军事承包商
  - GPS受限环境下的定位需求方
  product_signal: 利用约300亿张玩家扫描数据训练了视觉定位系统，可在GPS失效的密集城市和信号被刻意屏蔽的战场等复杂环境中工作。
  market_signal: 2025年12月与国防承包商Vantor达成合作，将VPS与Raptor空中导航软件融合用于军用无人机和机器人导航。
  differentiation: 拥有全球规模最大的民用环境扫描数据集之一，可实现仅凭摄像头画面即可确定位置的视觉定位能力。
  watch_reason: Niantic Spatial VPS代表了消费级游戏数据驱动的视觉定位技术正从民用场景转向军事国防用途，其训练数据的伦理边界、技术能力边界以及向国防市场的商业化路径均值得持续深入跟踪。
  risk_notes:
  - 训练数据来源于游戏玩家的非知情同意，数据流向军事用途引发极大伦理争议。
  - Vantor拒绝说明已部署的模型是否曾使用玩家扫描数据进行训练，数据可追溯性存疑。
  score: 9.0
  article_ids:
  - 55dffce3e3a7dc73
  evidence_snippets:
  - Niantic Spatial利用约300亿张玩家扫描数据训练了视觉定位系统（VPS），通过摄像头画面匹配3D地图来在无GPS信号时确定位置。
  - Niantic Spatial首席技术官Brian McClendon表示该视觉定位系统适用于GPS经常失效的密集城市和信号被刻意屏蔽的战场等复杂环境。
- object_type: product
  name: Vantor Raptor
  canonical_name: Vantor Raptor
  url: null
  positioning: 面向军用无人机和机器人的空中导航软件，利用摄像头与专有三维地形数据实现无卫星信号环境下的自主定位。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 美国国防机构
  - 军用无人机运营商
  - 战场导航系统集成商
  product_signal: 2025年2月发布的Raptor软件利用无人机摄像头和专有三维地形数据实现空中定位，并与Niantic VPS融合实现了无卫星链路的实时坐标共享。
  market_signal: 与Niantic Spatial VPS完成融合后计划2026年初进行集成系统实地测试，目标是在电子战环境中实现数千台设备的统一坐标框架。
  differentiation: 背靠前Maxar Intelligence转型而来的国防承包商资质，持有美国国家地理空间情报局七千万美元合同。
  watch_reason: Vantor Raptor在整合了消费级游戏数据训练的Niantic VPS之后，代表了军事导航技术利用民用数据基础设施的新方向，其技术路径、数据溯源和伦理争议均值得持续关注与深入分析。
  risk_notes:
  - 依赖第三方训练数据存在伦理和法律争议，可能影响技术部署和公众声誉。
  - 视觉导航系统在强电子战环境中的实际抗干扰能力仍需实战验证。
  score: 6.0
  article_ids:
  - 55dffce3e3a7dc73
  evidence_snippets:
  - Vantor的Raptor软件于2025年2月发布，利用无人机摄像头和专有三维地形数据实现空中定位。Raptor与Niantic VPS融合后，可在无卫星链路的情况下实现空中与地面设备的实时坐标共享。
- object_type: product
  name: Ingress
  canonical_name: Ingress
  url: null
  positioning: Niantic早期开发的增强现实手机游戏，率先通过玩家拍摄现实场景来收集环境视觉数据。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 增强现实游戏玩家
  - Niantic早期用户
  product_signal: Niantic早在2014年就通过Ingress收集玩家的相机图像数据，其方法与后续Pokémon Go使用的扫描机制完全相同。
  market_signal: Ingress为Niantic积累了早期数据收集方法论，为其后续包括Pokémon Go在内的游戏产品数据获取策略奠定了技术基础。
  differentiation: 作为Niantic数据收集体系的开端，Ingress验证了游戏化数据众包模式在视觉定位领域的可行性。
  watch_reason: Ingress作为Niantic数据收集体系的起点，展示了公司长达十年以上的视觉数据收集历史，揭示了从游戏数据到军事导航的完整技术演进链条，作为关键背景信息值得持续跟踪与分析。
  risk_notes:
  - 文章对Ingress的提及较为简略，直接证据和细节描述相对有限，其军事用途的直接关联性较弱。
  score: 3.0
  article_ids:
  - 55dffce3e3a7dc73
  evidence_snippets:
  - Niantic早在2014年就通过游戏Ingress收集玩家的相机图像数据，其数据收集方法与后续Pokémon Go使用的扫描机制完全相同。
- object_type: product
  name: FirePoint
  canonical_name: FirePoint
  url: null
  positioning: 乌克兰的无人机导航系统开发商，通过多代技术迭代最终采用地形匹配方案实现无GPS飞行。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 乌克兰军方
  - 低成本无人机导航系统需求方
  product_signal: FirePoint在约三年内建立了七代导航系统，最终采用地形匹配方案，使用廉价夜视摄像头实现无GPS飞行。
  market_signal: FirePoint的技术演进路径展示了战场对低成本无GPS导航的迫切需求，与视觉定位技术方向高度一致。
  differentiation: 采用廉价夜视摄像头和地形匹配方案实现了低成本高可靠性的无GPS导航能力。
  watch_reason: FirePoint在乌克兰战场实战环境中快速迭代七代导航系统的经验，为无GPS视觉导航技术在军事领域的可行性和紧迫性提供了有力佐证，是理解该领域技术需求背景的重要参照案例。
  risk_notes:
  - 文章仅将FirePoint作为参考案例提及，其具体技术细节、团队规模和当前状态信息均较为有限。
  score: 3.0
  article_ids:
  - 55dffce3e3a7dc73
  evidence_snippets:
  - 乌克兰的FirePoint在约三年内建立了七代导航系统，最终采用地形匹配方案，使用廉价夜视摄像头实现无GPS飞行。
- object_type: product
  name: Shield AI V-BAT
  canonical_name: Shield AI V-BAT
  url: null
  positioning: Shield AI开发的垂直起降无人机，具备在无线电链路完全失效时自主继续飞行的导航能力。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 美国军方
  - 无人机作战部队
  product_signal: V-BAT无人机在无线电链路失效时仍能继续飞行，充分体现了无GPS视觉定位导航技术在军事领域的关键价值。
  market_signal: V-BAT展示了军事航空领域对不依赖GPS的自主导航方案的真实需求和广阔市场空间。
  differentiation: 在通信完全中断的情况下仍能维持飞行，代表了无人机在电子战环境中的高生存能力标准。
  watch_reason: Shield AI V-BAT在通信完全中断时仍能持续飞行的实战能力，展示了无GPS导航技术在军事领域的核心价值和市场紧迫需求，是理解视觉定位系统军事应用背景的重要行业参照案例。
  risk_notes:
  - 文章仅将Shield AI V-BAT作为行业背景参考案例提及，与本文核心议题无直接技术关联。
  score: 3.0
  article_ids:
  - 55dffce3e3a7dc73
  evidence_snippets:
  - Shield AI开发的V-BAT无人机在无线电链路失效时仍能继续飞行，充分体现了无GPS视觉定位导航技术在军事领域的关键价值。
---

Hundreds of millions of Pokémon Go players spent years filming the streets, parks, and buildings around them to earn in-game rewards. Those roughly 30 billion environmental scans are now owned by **Niantic Spatial**, and they helped train a camera-based navigation model that a U.S. defense contractor is preparing to put into drones and other military robots. Most of the players had no idea.

The pipeline runs from a mobile game to the battlefield in three steps. Players scanned the physical world. Niantic Spatial turned those scans into a 3D map that lets a machine locate itself by sight when satellite signals fail. And in December 2025, Niantic Spatial announced a partnership with **Vantor**, the defense and intelligence firm formerly known as Maxar Intelligence, to fuse that ground-level system with Vantor’s aerial navigation software for use in GPS-denied operations.

I have spent years covering how drones lose their way the moment an electronic warfare unit switches on a jammer, a problem that has spread from the battlefield into civilian airspace, from Ukrainian workshops cycling through navigation generations to American programs scrambling for alternatives. The unsettling part of this story is not the technology. It is where the training data came from, and whether the people who supplied it would have agreed had anyone explained the destination.

## Pokémon Players Filmed Their Surroundings for Rewards and Fed a 3D Map

Since 2021, Pokémon Go has asked players to record short videos of real-world locations, called Pokéstops, to earn extra in-game items. Scanning all the buildings, streets, and trees in a 360-degree sweep was optional, and Niantic asked separately for permission to keep the footage. Granting it meant agreeing to extra terms.

Those terms handed Niantic a transferable, sublicensable license to the scans, meaning the company could resell the imagery to third parties. Floris De Hingh, a 34-year-old Dutch player who downloaded the game on its first available day in 2016, told Trouw he never connected the footage he captured to a system that would steer military drones. “I was just playing a game,” he said. He had even scanned the inside of his own apartment.

The collected scans, around 30 billion of them according to Trouw, became the raw material for a Visual Positioning System, or **VPS**. Where GPS depends on a satellite signal, VPS works out where a camera is by matching what it sees against a detailed 3D model of the world. Two recognizable reference points a few pixels wide can be enough to fix a location. Niantic Spatial CTO Brian McClendon, who previously led the team behind Google Maps, Google Earth, and Street View, has said the approach suits robots operating where GPS regularly drops out, such as dense cities, and where signals are deliberately blocked, such as war zones.

## Vantor Will Pair the Ground Map With Aerial Drone Navigation

The Vantor partnership, announced on December 16, 2025, joins two positioning systems into one. Niantic Spatial handles localization on the ground by aligning a camera feed against its model. Vantor’s Raptor software, launched in February 2025, does the same job in the air using a drone’s camera and Vantor’s proprietary 3D terrain data. Combined, the companies say, a drone overhead and a vehicle or dismounted operator below can share the same coordinates in real time with no satellite link. The principle is already turning up on the other side of the front, where a downed Russian drone was found matching live camera feeds against preloaded terrain imagery rather than trusting a single GPS module.

Vantor’s own framing is blunt about the problem it targets. The joint release names GPS “unavailability, spoofing, interference, and jamming” as the vulnerability, and lists autonomous drones, vehicles, augmented reality glasses, and other field assets as the platforms meant to run on the shared system. Niantic Spatial’s go-to-market lead told defense outlet Tectonic the goal is thousands of devices operating on one coordinate framework in an electronic-warfare-heavy environment. Field testing of the integrated system is planned for early 2026.

Vantor is not a startup dabbling in defense. Rebranded from Maxar Intelligence on October 1, 2025, it is a prime contractor to the National Geospatial-Intelligence Agency, holding a follow-on award worth $70 million under the agency’s Global Enhanced GEOINT Delivery program, which serves more than 400,000 U.S. government users. This is a company built around national security imagery, now adding GPS-independent navigation to its catalog.

## Vantor Denies Using the Pokémon Game Data, Then Declines to Rule It Out

Asked directly whether the military-bound system relies on Pokémon Go imagery, Vantor told Trouw it would not use the game’s data. The company then declined to say whether the model it plans to deploy was trained on those scans in the past. Niantic Spatial, responding to earlier questions about a separate deal, said the scans were used to train an “early version” of its navigation model. On the defense partnership specifically, the company said it had no new information to share.

That gap is the heart of the dispute. Jeroen van den Hoven, a professor of ethics and technology at TU Delft, told Trouw the conclusion is hard to avoid. “Without the huge number of scans from all those gamers, the development of this system would never have progressed so quickly,” he said. He added that AI models begin with a dataset and then absorb far more data until the original contributions blur into patterns that can no longer be traced. Once a scan is folded into the model, in other words, proving it is or is not in there becomes nearly impossible.

Van den Hoven did not condemn battlefield VPS outright. If it helps Ukraine win a just war against an aggressor, he said, that is a good development. His worry is the system falling into the wrong hands, and the broader pattern of players being misled about where their data goes. He called the episode a red flag.

## Niantic’s Roots Run Back to a CIA-Backed Mapping Firm

The military turn looks less like a swerve once you trace the company’s lineage. Niantic grew out of Keyhole, a geographic data firm that took funding in 2003 from In-Q-Tel, the venture arm financed by the CIA. An In-Q-Tel release from that year stated Keyhole’s services were used to support U.S. troops during the Iraq War. Google bought Keyhole the following year, and Keyhole CEO John Hanke went on to lead the team behind Google Maps, Google Earth, and Street View.

Hanke formed Niantic Labs inside Google in 2010, then spun it out in 2015. The company collected camera imagery from players once before, through its 2014 game Ingress, using the same method later applied in Pokémon Go. In 2025 the structure split again: Scopely, owned by Saudi Arabia’s Savvy Games Group and ultimately the kingdom’s Public Investment Fund, acquired Niantic’s games business for $3.5 billion in a deal that closed in late May, while the technology platform spun off as the standalone Niantic Spatial under Hanke. The games went to a Saudi sovereign wealth fund. The map went to defense.

## The Consent Question Reaches Far Beyond One Game

Pokémon Go is not the only camera in your pocket feeding a map. Meta’s smart glasses continuously scan a wearer’s surroundings, Apple’s AR hardware builds 3D models of interiors, and Waymo’s self-driving cars reconstruct detailed street layouts. Niantic Spatial has signaled interest in more indoor footage specifically, and in March 2025 it announced a deal with Coco Robotics to guide delivery robots already rolling through U.S. cities and Helsinki.

Iris Muis, a data-ethics expert at Utrecht University’s Data School, framed the trap plainly: a user cannot picture how their data might be used later. Maybe in five years there is an application with effects you fundamentally disagree with. British game designer Adrian Hon has gone further, advising Pokémon Go players to stop making scans and consider smaller games less likely to resell data. De Hingh, who quit the game over a year ago because he was tired of the updates rather than the data terms, called the news an enormous eye-opener. “A game should stay a game,” he said.

## DroneXL’s Take

The navigation problem this solves is real, and DroneXL has documented it from the trenches. When I wrote about Ukraine’s FirePoint in March, the detail that stuck was not the 200 strike drones a day. It was that the company had built seven generations of navigation systems in roughly three years, landing on a terrain-matching setup that uses a cheap night camera to fly without GPS. Russia can jam GPS. It cannot jam a drone that does not need it. Visual positioning is the same insight, scaled up and packaged for export.

So I am not going to pretend GPS-denied navigation is sinister on its face. It is one of the most important capability gaps in the industry, the reason Shield AI’s V-BAT keeps flying when radio links die, the reason the Pentagon’s Drone Dominance evaluations are adding GPS denial to Phase II this year. The discomfort here is narrower and sharper. The training data came from people who thought they were catching Pikachu, under a license most never read, sold up a chain that ends at a sovereign wealth fund and a defense prime. Consent obtained for a game is not consent for a weapons program, even if the end use turns out to be defensible.

Vantor’s non-answer is what I would watch. The company says it will not use Pokémon Go data and refuses to say whether the model it is fielding was already trained on it. Those are not the same statement, and the difference is the whole story. Van den Hoven is right that once scans are baked into a model, tracing them back is close to impossible, which conveniently makes the denial unfalsifiable. The early-2026 field tests will tell us whether this air-to-ground system is real or a press release. They will not tell us whose footage is inside the model, and so far nobody at either company will.

*Sources: Trouw, Volkskrant.*

*DroneXL uses automated tools to support research and source retrieval. All reporting and editorial perspectives are by Haye Kesteloo.*

Check out our Classic Line of T-Shirts, Polos, Hoodies and more in our new store today!

## MAKE YOUR VOICE HEARD

Proposed legislation threatens your ability to use drones for fun, work, and safety. The **Drone Advocacy Alliance** is fighting to ensure your voice is heard in these critical policy discussions.Join us and tell your elected officials to protect your right to fly.

## Get your Part 107 Certificate

Pass the Part 107 test and take to the skies with the Pilot Institute. We have helped thousands of people become airplane and commercial drone pilots. Our courses are designed by industry experts to help you pass FAA tests and achieve your dreams.

Copyright © DroneXL.co 2026. All rights reserved. The content, images, and intellectual property on this website are protected by copyright law. Reproduction or distribution of any material without prior written permission from DroneXL.co is strictly prohibited. For permissions and inquiries, please contact us first. DroneXL.co is a proud partner of the Drone Advocacy Alliance. Be sure to check out DroneXL's sister site, EVXL.co, for all the latest news on electric vehicles.

FTC: DroneXL.co is an Amazon Associate and uses affiliate links that can generate income from qualifying purchases. We do not sell, share, rent out, or spam your email.