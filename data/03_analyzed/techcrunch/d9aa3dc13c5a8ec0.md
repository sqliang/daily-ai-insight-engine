---
title: 'AI is hurting Apple in more ways than one: it may force iPhone price increases'
source: https://techcrunch.com/2026/06/17/ai-is-hurting-apple-in-more-ways-than-one-it-may-force-iphone-price-increases/
author:
- '[[Kirsten Korosec]]'
published: '2026-06-17'
created: '2026-06-18'
description: CEO Tim Cook said in a recent interview that the situation is "unsustainable."
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: d9aa3dc13c5a8ec0
source_type: news_media
tldr: AI引发全球存储芯片短缺，苹果CEO Tim Cook警告iPhone/Mac/iPad可能涨价
objective_summary: AI对硬件的巨大需求导致全球存储芯片短缺（RAMageddon），苹果CEO Tim Cook向WSJ表示芯片成本已上涨四倍，涨价"不可避免"。TechInsights估计下一代iPhone
  Pro需加价270美元才能维持利润率。苹果今年因未能兑现AI承诺支付2.5亿美元和解金。
event_type: infrastructure_update
epistemic_status: verified_fact
entities:
  companies:
  - Apple
  - Wall Street Journal
  - Financial Times
  - TechInsights
  technologies:
  - DRAM
  - NAND
  - AI
  key_people:
  - Tim Cook
  - John Ternus
key_logic_flow:
- AI对硬件的巨大需求导致全球DRAM和NAND存储芯片短缺，业内称之为"RAMageddon"
- 苹果CEO Tim Cook向WSJ表示芯片成本已较去年上涨四倍，产品涨价"不可避免"且"不可持续"
- 今年4月Cook在创纪录季度销售后已预警成本将影响业绩，继任CEO John Ternus也发出同样警告
- 存储芯片专家向金融时报表示iPhone几乎必然受涨价影响，苹果9月新机发布提供了调价窗口
- TechInsights估算苹果需将下一代iPhone Pro加价270美元才能维持当前利润率（iPhone 17 Pro起售价1099美元）
- AI至今未为苹果带来收益：公司因未兑现AI承诺支付2.5亿美元和解金，WWDC展示的Siri改造等进展反而意味着更多内存需求
impact_score:
  score: 6.5
  reason: 该事件揭示了AI基础设施需求向消费电子端传导的实质性经济影响。Tim Cook向WSJ的公开表态、TechInsights的270美元加价测算、以及2.5亿美元和解金，构成了从供应链到终端定价的完整证据链。这并非技术范式转移，但标志着AI行业的外部性（存储芯片挤占效应）首次被全球最大家电消费品牌公开承认为不可持续的成本压力。对投资者和硬件供应链从业者而言，这是一个改变局部竞争格局（存储芯片定价权、消费电子产品利润率重构）的重要信号，但短期内不改变AI技术本身的演进方向。评分6.5：介于'重要产品发布/局部竞争格局改变'区间，接近但不达到7分的上限，因为现象本身是渐发性的供需失衡而非突发性变革。
sentiment: negative
developer_sentiment:
  tone: skeptical
  primary_focus: AI基础设施扩张导致的存储芯片短缺正在推高消费硬件成本，开发者担心终端设备的AI推理能力升级反而会因涨价而延缓用户采用
hype_assessment:
  level: low
  reason: 文章核心事实均有可靠来源支撑：Tim Cook的WSJ原话、TechInsights的定量测算、FT引用的存储专家意见、以及2.5亿美元和解金的公开记录。'RAMageddon'一词虽有包装色彩，但本质是业内对HBM挤占通用DRAM产能这一结构性问题的既有称呼，并非本文杜撰。没有出现'颠覆''革命性'等PR滥用语，整体叙事克制且基于可验证的商业事实。
information_entropy: medium
domain_disruption:
  technical_innovation: AI训练/推理对HBM（高带宽内存）的爆发式需求，正在通过晶圆厂产能分配机制挤压通用DRAM和NAND Flash的供给，形成AI基础设施向消费电子端的成本传导链。这一结构性矛盾倒逼存储芯片架构创新（如存算一体、CXL互联）和封装工艺升级，但本文未涉及具体技术突破。
  business_model: 苹果的硬件溢价模式面临根本挑战：若AI芯片成本四倍的涨幅无法被供应链吸收，将迫使消费电子厂商在'AI终端功能投入'与'终端定价竞争力'之间做出取舍，可能加速硬件订阅制、以旧换新补贴、或捆绑AI服务的分层定价等商业模式转型。
engineering_complexity: production_ready
compound_value:
  score: 7.5
  reason: AI 驱动存储芯片短缺（RAMageddon）是一个结构性趋势，而非周期性波动。AI 训练和推理对 HBM/DRAM 的消耗呈指数级增长，而存储芯片供应链（晶圆厂产能、HBM
    先进封装）短期无法快速扩产，供需缺口将持续存在。对于上游存储芯片制造商，这意味着长期定价权增强和利润率扩张的复利效应。此趋势的核心投资逻辑在于：AI 对硬件的需求正从
    GPU 侧蔓延至存储侧，形成对整个半导体供应链的系统性拉动。只要 AI 模型参数量和推理规模继续增长（3-5 年内看不到边际递减），存储芯片就将处于供不应求格局。7.5
    分对应细分赛道基础设施级别——存储芯片制造是 AI 时代的物理基础设施，但需警惕产能扩张后的周期性风险。
value_capture_layer: hardware_compute
moat_impact: strengthens_monopoly
key_beneficiaries:
- Samsung
- SK Hynix
- Micron Technology
competitive_casualty:
- Apple
- 中小消费电子厂商
market_opportunities:
- 创业公司可聚焦研发低内存占用的高效AI模型架构（如量化、蒸馏、稀疏化技术），帮助终端设备厂商在不增加硬件成本前提下运行AI功能
- 存储芯片替代技术（如存内计算、CXL互联、新型非易失性存储器）的产业化落地迎来窗口期，可缓解DRAM/NAND供需矛盾
- 硬件供应链风险管理与价格对冲服务需求激增，专业采购优化和长期产能锁定的咨询方案具备商业化潜力
risk_matrix:
  regulatory: 苹果若因芯片成本大幅提价，可能面临消费者保护诉讼或反垄断审查（尤其是欧洲DMA框架下的价格歧视调查）；多国对高端存储芯片的出口管制可能进一步加剧短缺
  technological: 若存算一体或近存计算等新型架构成熟，传统DRAM/NAND溢价逻辑将被打破；但短期内无替代技术能大规模量产，技术替代风险较低
  competitive: 三星、美光等存储厂商可能优先向利润率更高的AI数据中心客户供货，挤压消费电子份额；Android阵营若率先采用替代方案或自行消化成本，将加剧苹果价格劣势
  ethical: AI驱动的硬件涨价加剧数字不平等——消费电子产品因AI需求涨价，低收入群体面临更大的数字接入鸿沟；苹果将AI成本转嫁给消费者而非自行吸收，引发公平性质疑
  additional:
  - 供应链地理集中风险：全球先进DRAM/NAND产能高度集中于韩国和中国台湾，地缘政治冲突可能导致供给中断风险被AI需求放大
confidence:
  impact: high
  compound: medium
  hype: high
actionable_insight: strategic_invest
---

It’s been called RAMageddon: AI’s insatiable demand for hardware has caused a worldwide shortage of memory chips. Now outgoing Apple CEO Tim Cook is warning its customers that your next Mac, iPhone, or iPad could be more expensive thanks to surging memory and storage chips costs.

In a recent interview, Cook told the WSJ that price increases are “unavoidable,” in spite of efforts to absorb chip costs that have increased fourfold since last year. He described the situation as “unsustainable.”

Cook didn’t name which products will be affected or when prices will rise, but he’s raised the alarm about the impacts of RAMageddon before. In April, after delivering record quarterly sales, he said that these higher costs could impact Apple’s next business results. Incoming CEO John Ternus also warned about the issue that same month.

If Apple raises prices, the iPhone seems almost certain to be impacted, memory supply experts told the Financial Times. The company is expected to launch its next iPhone in September, which gives it the opportunity to announce increased prices. Of course, Apple sells many other devices that contain memory (DRAM) and storage (NAND) chips, including the Apple Watch, Mac, iPad, and Apple Vision Pro.

It’s not clear how much more expensive any of these products will be, although research firm TechInsights gave the WSJ its estimate. It said Apple would need to add another $270 to the next iPhone Pro to keep its profit margin intact. The iPhone 17 Pro starts at $1,099.

So far AI has not been a particular boon to Apple. The company is already under pressure to figure out its AI strategy for its devices. It even paid a $250 million settlement earlier this year to end a false advertising lawsuit filed after it failed to deliver the AI features it promised two years ago.

The company’s Worldwide Developers conference held earlier this month showed progress on fulfilling those previous AI promises, including an overhaul of Siri. Of course, more on-device processing could mean more need for memory — a trajectory that seems destined to end with consumers paying more for Apple products.