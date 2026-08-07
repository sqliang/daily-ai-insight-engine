---
title: Anthropic Reportedly Signed a $10B Cloud Deal with Volta (3 minute read)
source: https://techcrunch.com/2026/08/04/anthropic-signs-10-billion-deal-with-ai-cloud-startup-volta/?utm_source=tldrai
author: []
published: ''
created: '2026-08-06'
manifest_dates:
- '2026-08-06'
description: TLDR AI 每日头条
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 1e6ae4b1e7bc25ab
source_type: news_media
tldr: 据彭博社援引匿名信源报道，Anthropic 与 AI 云初创公司 Volta 签署了为期六年、价值 100 亿美元的云计算协议。数据中心由 Bitdeer
  合作开发，位于挪威，容量 133 兆瓦，采用英伟达 Vera Rubin 芯片。
objective_summary: 2026 年 8 月，彭博社援引匿名信源称，Anthropic 与今年早些时候成立的 AI 云初创公司 Volta 达成一笔
  100 亿美元、为期六年的云计算协议。加密货币挖矿公司 Bitdeer 作为合作方参与开发位于挪威的数据中心，容量 133 兆瓦，由英伟达 Vera Rubin
  芯片架构驱动。Anthropic 尚未正式确认该消息，此前其已宣布与 SpaceX 和亚马逊的新算力合作。
event_type: infrastructure_update
epistemic_status: rumor_leak
entities:
  companies:
  - Anthropic
  - Volta
  - Bitdeer
  - Nvidia
  - Bloomberg
  - TechCrunch
  - SpaceX
  - Amazon
  technologies:
  - Vera Rubin
  key_people: []
key_logic_flow:
- 彭博社援引匿名信源报道，Anthropic 与今年早些时候成立的 AI 云初创公司 Volta 签署了为期六年、价值 100 亿美元的云计算协议。
- 加密货币挖矿公司 Bitdeer 作为 Volta 的合作方，将参与开发提供算力所需的数据中心。
- 该数据中心位于挪威，将交付 133 兆瓦容量，并由英伟达最新的 Vera Rubin 芯片架构提供动力。
- Volta 是英伟达云合作伙伴计划的成员，此前曾对外提及与一家 AI 实验室的合作但未透露具体公司名称。
- TechCrunch 已联系 Anthropic 求证，但该消息目前仅基于匿名信源，尚未得到官方确认。
- Anthropic 近几个月积极扩张算力，此前还宣布与 SpaceX 和亚马逊达成新的算力合作协议。
object_mentions:
- object_type: company
  name: Volta
  canonical_name: Volta
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 彭博社援引匿名信源报道，Anthropic 与今年早些时候成立的 AI 云初创公司 Volta 签署了为期六年、价值 100 亿美元的云计算协议。
  article_id: 1e6ae4b1e7bc25ab
- object_type: company
  name: Bitdeer
  canonical_name: Bitdeer
  url: null
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - 加密货币挖矿公司 Bitdeer 是 Volta 在这一交易中的合作方，将参与开发位于挪威、提供 133 兆瓦容量的数据中心。
  article_id: 1e6ae4b1e7bc25ab
- object_type: product
  name: Nvidia Vera Rubin
  canonical_name: Vera Rubin
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - 该数据中心将由英伟达最先进的 AI 芯片架构 Vera Rubin 系统提供算力，Volta 本身也是英伟达云合作伙伴计划的成员。
  article_id: 1e6ae4b1e7bc25ab
extract_result: success
impact_score:
  score: 6.5
  reason: 首先，这是 100 亿美元、为期六年的超大额算力采购，规模足以与微软/OpenAI 等既有合作相提并论，若属实将直接重塑 AI 云市场竞争格局——成立仅一年的初创云厂商
    Volta 拿到前沿实验室的巨额长期合同，且借助加密货币挖矿公司 Bitdeer 的能源基础设施建数据中心，是行业供给侧的标志性信号。其次，Anthropic
    近月连续与 SpaceX、亚马逊及本次 Volta 达成算力合作，显示前沿实验室正主动构建多元化的算力组合，对冲对少数超大规模云厂商的依赖。但该消息仅来自彭博社匿名信源（认识论状态为
    rumor_leak），Anthropic 尚未确认，存在不确定性；且基础设施采购属于资源布局而非技术范式改变，不改变模型训练或推理的技术路线，对普通开发者也无直接可感知影响。综合以上，短期冲击力中等偏上，评
    6.5 分。
sentiment: positive
developer_sentiment:
  tone: neutral
  primary_focus: 百亿算力采购对 Claude 训练规模、API 可用性与定价的潜在影响
hype_assessment:
  level: medium
  reason: 事件本身是匿名信源爆料，100 亿美元与六年期限等关键数字均未经 Anthropic 官方证实，存在误报或夸大风险，属于典型的传闻驱动叙事；但
    TechCrunch 报道措辞克制，通篇使用『reportedly』且明确标注『Anthropic 尚未确认』，未使用『颠覆』『革命』等 PR 滥用词汇。炒作水分主要来自交易传闻的规模本身，而非文章包装手法，故判定为中等。
information_entropy: medium
domain_disruption:
  technical_innovation: 事件本质是算力采购而非技术突破。真正的技术驱动点有二：一是英伟达 Vera Rubin 新架构首次大规模集群化部署（133
    兆瓦级），代表下一代 AI 芯片进入规模化落地阶段；二是将加密货币挖矿公司 Bitdeer 既有的能源与电力基础设施改造成 AI 数据中心，为 AI 算力供给侧开辟了『能源套利式』的新工程路径，绕过传统数据中心的电网审批与建设周期瓶颈。
  business_model: 商业模式重塑意义显著：AI 云初创公司 Volta 通过与 Bitdeer（能源）绑定的三方拼盘模式，在缺乏超大规模云厂商背景的情况下拿下
    100 亿美元长期合同，验证了『能源资源 + 英伟达云合作伙伴计划 + 前沿实验室需求』的新型算力供给商业模式。对前沿实验室而言，这标志着从绑定单一大云厂商转向多元算力组合对冲的战略范式，长期看可能削弱
    AWS/Azure/GCP 对顶级模型厂商的议价杠杆。
engineering_complexity: prototype
compound_value:
  score: 6.5
  reason: 该事件本质是前沿大模型实验室锁定多年期算力供给的一个信号，长期复利逻辑在于三点：其一，算力仍是前沿模型竞争的硬约束，Anthropic 通过分散化采购（Volta、SpaceX、亚马逊多线并行）构建对超大云厂商的议价缓冲，这种采购模式具备持续性；其二，Bitdeer
    复用加密货币矿场在电力与数据中心建设上的能力转向 AI 算力，挪威水电与冷凉气候构成成本护城河，验证了'新玩家可切入算力中间层'的产业路径，该细分赛道有望沉淀为长期基础设施；其三，英伟达
    Vera Rubin 获得又一规模化落地场景，加速新架构生态成熟。但需注意：该消息目前仅基于匿名信源，属于 rumor_leak；Volta 今年刚成立、无交付记录，133MW
    容量相较 Stargate 等 GW 级项目体量有限，六年后是否仍是行业基石存在不确定性，故给 6.5 分而非更高。
value_capture_layer: hardware_compute
moat_impact: creates_new_moat
key_beneficiaries:
- Anthropic
- NVIDIA
- Volta
- Bitdeer
competitive_casualty:
- OpenAI
- AWS/Azure/GCP 等超大规模云厂商
- 传统第三方 GPU 云厂商
market_opportunities:
- 关注传统加密货币矿场向 AI 算力基础设施转型的趋势，可探索矿企闲置电力与地块资源承接 AI 数据中心改造与托管服务的业务机会
- 围绕英伟达 Vera Rubin 新一代芯片架构的部署与运维需求，可布局面向下一代 GPU 集群的液冷散热、高速网络与调度优化等配套服务
- 北欧地区凭借水电等绿色能源正成为 AI 数据中心选址新热点，可关注挪威等地算力园区的建设配套、电力消纳与合规咨询服务机会
risk_matrix:
  regulatory: 该交易仍处于未经证实的传闻阶段，若属实，百亿美元级算力协议可能引发反垄断与国家安全审查；挪威数据中心涉及欧盟 AI Act、能源与数据跨境合规；与加密货币矿企
    Bitdeer 合作可能带来牌照与合规审查风险。
  technological: Volta 为今年刚成立的新公司，Vera Rubin 为英伟达最新架构，存在交付延期与供应链不确定风险；Bitdeer 的矿场改造经验在大型
    AI 训练负载下的可靠性尚未经过验证。
  competitive: AI 算力军备竞赛激烈，OpenAI、谷歌、xAI 等均在争夺算力资源，云厂商间价格战与生态挤压可能使该大额合约的实际回报不及预期；若交易最终落空，Anthropic
    在算力竞争中将短暂落后于对手。
  ethical: 133 兆瓦数据中心的能耗规模引发环保与能源分配关切（尽管挪威以清洁水电为主）；Anthropic 与加密货币挖矿公司深度绑定可能带来 ESG
    与品牌声誉风险。
  additional:
  - 交易真实性风险：目前仅为彭博社匿名信源爆料，Anthropic 未正式确认，存在谈判破裂、金额夸大或合作方变动的可能
  - 履约与财务风险：Volta 作为初创公司能否承担 100 亿美元、六年期大额订单的资金与工程能力存在较大不确定性
confidence:
  impact: medium
  compound: low
  hype: high
actionable_insight: monitor
---

Anthropic has been on a cloud partnership spree in recent months, and its latest move is reportedly a $10 billion deal with AI cloud startup Volta.

Bloomberg originally reported that Volta, founded earlier this year, will provide cloud compute to the Claude maker over a six-year period.

Volta has a partner in this deal, Bitdeer, a crypto-mining company that will help develop the data center to provide the compute capacity. That facility will be located in Norway and will deliver a 133 megawatt capacity. It will be fueled by Nvidia’s Vera Rubin systems, the chipmaker’s state-of-the-art AI chip architecture.

Volta is part of Nvidia’s Cloud Partner program, which is a consortium of AI cloud providers that use Nvidia’s GPUs in their data centers.

Volta had spoken about a deal with an AI lab but hadn’t named the specific company it was working with. Bloomberg originally cited anonymous sources familiar with the deal. TechCrunch reached out to Anthropic for more information.

Anthropic has sought to aggressively expand its compute capacity over the last several months as it wages a corporate battle with its competitors. The company also recently announced new compute deals with the likes of SpaceX and Amazon.