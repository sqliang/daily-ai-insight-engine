---
title: Meta也来卖铲子了！小扎：模型可以慢，GPU必须赚
source: https://www.qbitai.com/2026/07/443339.html
author:
- '[[听雨]]'
published: '2026-07-05'
created: '2026-07-06'
description: 正考虑推出Meta Compute
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: bb2db71ddcc0ac3d
manifest_dates:
- '2026-07-06'
source_type: news_media
tldr: Meta因模型进展落后，计划推出Meta Compute将GPU算力出租给外部客户变现
objective_summary: 据彭博社和SemiAnalysis报道，Meta因自研AI模型进展不及预期，正考虑推出基础设施服务Meta Compute，将已签约超5GW的算力容量向外部客户开放，包括算力租赁和第三方模型托管。消息公布后Meta股价大涨近9%。
event_type: infrastructure_update
epistemic_status: verified_fact
entities:
  companies:
  - Meta
  - Bloomberg
  - SemiAnalysis
  - Anthropic
  - OpenAI
  - Google
  - Amazon
  - Microsoft
  - CoreWeave
  - Nebius
  - SpaceX
  technologies:
  - GPU
  - LLM
  - Claude
  - Gemini
  - Muse Spark
  - Watermelon
  key_people:
  - Mark Zuckerberg
  - Alexandre Wang
key_logic_flow:
- Meta因自研模型进展落后于OpenAI、Anthropic和Google，且Gemini使用受限、内部AI agent推进缓慢，转而将基础设施商业化作为Plan
  B
- Meta正在考虑推出Meta Compute，将已签约超5GW的数据中心算力开放给外部客户，包括算力租赁和第三方模型托管
- Meta的算力资源将用于四个方向：自研模型训练（Muse Spark和Watermelon）、广告推荐系统升级、高价算力租赁、以及类似Amazon Bedrock的模型服务平台
- 据SemiAnalysis报道，Meta正与Anthropic就Claude私有实例访问权进行最终谈判，计划将第三方模型部署在自己的基础设施上对外销售
- 消息公布后Meta股价大涨近9%，而CoreWeave、Nebius等neocloud公司股价遭遇抛售
- Meta预计2026年资本开支达1250亿至1450亿美元，下一代模型Watermelon正在训练中，据称算力投入比前代高一个数量级
extract_result: success
impact_score:
  score: 7.0
  reason: Meta手握超5GW签约数据中心容量，以'算力租赁+第三方模型托管'双模式入局AI云市场。这一决策的冲击力来源于三重因素：其一，Meta的体量巨大——5GW相当于数十个超大规模数据中心，仅需拿出200MW即可创造年100亿美元收入；其二，直接威胁现有格局——同时冲击AWS/Azure/GCP三大云厂商和CoreWeave等neocloud公司，消息公布后CoreWeave、Nebius股价已遭抛售；其三，与Anthropic的Claude私有实例谈判意味着Meta可能成为模型分发渠道，改变模型生态的权力结构。不过，该计划尚处传闻/谈判阶段，未正式发布产品，且Meta内部模型进展不顺是诱因而非优势，因此评分为7.0而非更高。
sentiment: mixed
developer_sentiment:
  tone: skeptical
  primary_focus: Meta进军云计算后，Llama开源策略是否会收紧，以及Meta云服务的定价是否会导致中小GPU云厂商被挤压
hype_assessment:
  level: medium
  reason: 文章标题'模型可以慢，GPU必须赚'使用了强烈的反差叙事和'卖铲子'的淘金热隐喻，具有一定的情绪煽动性。文章中'灵光一闪''啧啧，这油水是真不少'等措辞偏向网文化表达。但核心信息源自彭博社和SemiAnalysis的可靠报道，披露了具体数据（5GW容量、1250-1450亿资本开支、与Anthropic谈判细节等），实质性内容充足，不属于空洞的概念炒作。
information_entropy: high
domain_disruption:
  technical_innovation: 无显著技术突破。Meta的算力基础设施已存在，核心变化是将内部资源外部化——通过类似SpaceX的90天可取消合同模式实现算力弹性调度，属于商业模式的创新而非技术架构的革新。
  business_model: Meta从纯模型开发商向'IaaS算力租赁+MaaS模型托管'双平台模式转型，直接与AWS Bedrock、Azure Foundry、Google
    Vertex正面竞争。其独特优势在于：存量超5GW的算力可快速变现，广告平台提供垂直SaaS变现通道，且与Anthropic的谈判若落地将拥有业界最强模型之一的分发权。这将重塑AI云市场格局——可能引发neocloud行业洗牌，同时也为模型公司提供了除三大云之外的新分发渠道。
engineering_complexity: production_ready
compound_value:
  score: 7.8
  reason: Meta已签约超5GW数据中心容量，仅2026年上半年就签下5GW+，全年资本开支高达1250-1450亿美元——这些基础设施投入已经成为沉没成本。将算力对外租赁是典型的边际成本趋零、潜在回报极高的资产货币化策略：据SemiAnalysis测算，仅拿出200MW对外租赁按SpaceX式neocloud定价即可创造约100亿美元年收入，且利润率极高。核心复利逻辑有三层：第一，Meta的基础设施规模已逼近主流超大规模云厂商，5GW容量意味着即使只利用10%产能对外服务，也能跻身全球Top云服务商之列；第二，90天取消条款赋予Meta极大的动态调度能力——外部需求旺盛时出租获利，自研模型需要时可随时收回，相当于一个自带下行保护的看涨期权；第三，若与Anthropic的Claude私有实例谈判落地，Meta可复制Amazon
    Bedrock模式，将第三方最强模型部署在自己的基础设施上对外销售，从纯算力租赁升级为'算力+模型'平台，显著提升客户粘性和利润率。但风险也不容忽视：Meta完全缺乏B2B企业级服务经验与客户信任积累，该策略本质上是模型进展不及预期的Plan
    B，若Watermelon等下一代模型持续无法跻身第一梯队，故事长期可持续性存疑。综合来看，这不是昙花一现的题材炒作，而是基于真实物理资产（5GW签约容量+在建数据中心）的战略转型，具备强复利效应潜力，但企业服务执行力仍需持续验证。
value_capture_layer: hardware_compute
moat_impact: creates_new_moat
key_beneficiaries:
- Meta
- NVIDIA
- Anthropic
competitive_casualty:
- CoreWeave
- Nebius
- 中小型Neocloud厂商
market_opportunities:
- 第三方模型服务平台迎来新竞争者与集成机会，企业客户可期待更丰富的模型选择与更具竞争力的定价方案
- 算力租赁二级市场可能兴起，创业公司可通过算力转租、算力期货等创新模式降低AI推理和训练成本
- 广告推荐系统的算力需求升级为AI SaaS服务商创造了垂直行业集成机会，可基于Meta平台构建销售与营销AI Agent
risk_matrix:
  regulatory: Meta同时扮演模型开发者与基础设施提供者的双重身份，可能引发反垄断监管关注，尤其在美国与欧盟针对AI基础设施的市场支配力审查将加强
  technological: Meta自研模型进度落后于OpenAI、Anthropic和Google，若Watermelon等下一代模型无法实现突破，基础设施商业化的差异化优势将被削弱，沦为纯算力批发商
  competitive: Meta同时与AWS、Azure、GCP三大云巨头及CoreWeave、Nebius等neocloud公司正面竞争，且后者已建立成熟客户关系和生态，Meta在云服务领域缺乏品牌认知和运营经验
  ethical: 超大规模数据中心持续扩张将加剧能源消耗与环境影响，同时托管第三方模型可能带来模型安全责任划分不明的伦理与法律风险
  additional:
  - Meta内部人才流失与员工士气问题可能影响基础设施业务的组织执行力和服务质量
confidence:
  impact: high
  compound: medium
  hype: high
actionable_insight: strategic_invest
---

# Meta也来卖铲子了！小扎：模型可以慢，GPU必须赚

正考虑推出Meta Compute

##### 听雨 发自 凹非寺

量子位 | 公众号 QbitAI

模型搞不出起色，小扎开始盯上基础设施了。

起因是Meta遭受了接二连三的打击：Gemini模型被限制使用、小扎承认内部AI agent技术推进比预期慢、员工士气跌到20年谷底……

总之真是流年不利。

但是没关系，小扎灵光一闪，又有了Plan B。

既然自研模型赶不上，那咱可以**卖GPU**啊！！

据彭博社报道，Meta正考虑推出**Meta Compute**，把庞大的AI基建开放给外部客户。

好家伙，果然都是卖铲子的天下…

## Meta要卖GPU了

既然要卖铲子，那么Meta手里有多少铲子？

据SemiAnalysis报道，Meta的数据中心和算力采购不但不会放慢，反而还会继续加速。

仅今年前6个月，Meta就已经在云和托管数据中心上签下了超过5GW的容量。这还不包括它正在加速推进的自建数据中心。

Meta正在建设中的两个最大数据中心园区，加起来就代表了2.5GW的容量。

而从2024年初以来，Meta签下的数据中心和算力相关交易，也已经接近10GW。

地图上这些密密麻麻的点位，就是小扎卖GPU的底气。

这堆算力有几个去向：

第一，继续喂给自家模型，比如亚历山大王的MSL已经推出的Muse Spark，以及正在训练中的下一代模型Watermelon。

第二，用在广告推荐系统上。SemiAnalysis认为，Meta可能希望把广告推荐系统的复杂度再放大10倍，用更多训练和推理算力提升广告收入。

第三，做类似SpaceX的neocloud交易，把一部分算力以高价租给外部客户。

如果按SpaceX那类高算力租赁合同来算，每GW年收入可达约500亿美元。

Meta只要拿出200MW算力给外部客户，就能带来100亿美元年收入，而且是超高利润率。

啧啧，这油水是真不少~

而且SpaceX开创了一种新模式：合同三年，但双方都可以在90天内取消——实际上相当于3个月一签，自动续约。

这意味着Meta可以随时把算力收回来给MSL用。

第四，托管第三方模型。

SemiAnalysis甚至判断，Meta正在与Anthropic进行最终谈判，以获得Claude的私有实例访问权。

未来，Meta会做类似Amazon的Bedrock、Microsoft的Foundry、Google的Vertex这样的模型服务平台。

也就是说，Meta可以把Claude这类第三方模型部署在自己的基础设施上，再打包卖给企业客户。

对Meta来说，这至少有三层用途：

第一，当然是内部使用。

Google刚刚限制了Meta对Gemini的使用，而Meta可能反手就把Claude作为替代。

毕竟Meta自己的AI项目需要大量高质量模型token。

而Claude也正好是目前最强的模型之一。

二是对外销售。Meta可以像亚马逊的Bedrock一样卖Claude-as-a-service。

客户不用自己找Anthropic签约、部署、运维，只要通过Meta的平台调用模型就行。

三是垂直应用。Meta可以利用自己的广告平台，构建销售与营销SaaS，集成前沿AI Agent。

SemiAnalysis预计，Meta可能很快宣布类似协议，Anthropic就是头号对象，但OpenAI或Google也可能加入。

如果Meta的算力业务成形，那么它的对手就不只是OpenAI、Anthropic、Google这些模型公司了。

它还会站到AWS、Azure、Google Cloud，以及CoreWeave、Nebius这些AI云厂商对面。

消息一出，资本市场也立刻闻风而动。

Meta股价大涨近9%，而CoreWeave、Nebius这些 neocloud公司则遭遇抛售。

华尔街显然听懂了小扎的新故事：

**虽然咱模型还没赢，但GPU可以先赚钱啊！**

## 为啥要卖算力：搞模型太烧钱

小扎从模型转向卖铲子，最直接的原因是：


**研发模型，真的太烧钱了！！！**

Meta官方给出的2026年资本开支指引，已经上调到1250亿-1450亿美元。

作为对比，Meta今年一季度的资本开支就已经达到198.4亿美元。

但是反观Meta的模型进度，不禁让人捏了一把冷汗：

Llama系列开源，生态影响力很大，但也很难直接转变成收入。

而Meta最新的自研模型Muse Spark，也还没有真正把Meta送回第一梯队。

现在Meta内部又在训练下一代模型**Watermelon**（西瓜），据称算力投入比Avocado高一个数量级。

亚历山大王表示：大家别着急，Watermelon已经赶上GPT-5.5的水平了。

同时，Muse Spark当前的版本也即将更新，在编程能力和智能体方面将取得重大提升。

当用户问Meta什么时候能推出与Claude Opus旗鼓相当的模型时，王表示：

很快就会了！


（小王你别说了，你倒是发呀）

说到底，Meta的AI雄心一直围绕着一个简单目标展开：

**追上OpenAI、Anthropic和Google。**

为此，小扎没少砸钱。芯片、数据中心、人才，几乎样样都按最高规格投入。

但问题是，钱砸下去了，Meta还没能真正说服开发者和客户，让他们相信自家模型已经站上行业最前沿。

当模型进度无法立刻兑现，算力就成了最容易被华尔街理解的资产。

因为GPU和数据中心至少可以被定价。

这些资源可以出租，可以托管模型，可以卖API，可以服务广告主，可以做AI agent SaaS，也可以在内部继续提升广告推荐系统。

就好比，原本Meta是在向市场讲一个很远的故事：

相信我，我们会做出超级智能。


但现在这故事听起来近多了：

就算超级智能没那么快出来，这些GPU也不是沉没成本。


当然，卖算力不代表Meta放弃自研模型。**小扎的Plan A依然是超级智能**。

继续抢人，继续堆卡，继续训练更大的模型，继续追赶御三家。

在追求ASI的路上，小扎永不言败！

只不过，前沿模型竞争的不确定性太高，中途总得难免妥协亿下下~

参考链接：

[1]https://newsletter.semianalysis.com/p/meta-compute-everyone-wants-to-be

[2]https://www.bloomberg.com/news/articles/2026-07-01/meta-is-building-a-cloud-business-to-sell-excess-ai-compute

*版权所有，未经授权不得以任何形式转载及使用，违者必究。*