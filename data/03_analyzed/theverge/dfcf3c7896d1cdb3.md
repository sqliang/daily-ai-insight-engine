---
title: Apple wants permission to buy memory from a blacklisted Chinese supplier
source: https://www.theverge.com/tech/958707/apple-ram-buy-memory-blacklisted-china-cxmt
author:
- '[[Terrence O’Brien]]'
published: '2026-06-27'
created: '2026-06-28'
description: Apple is looking to alleviate some of the pressure on its supply chain
  by seeking an exception from the Trump administration to buy RAM chips from CXMT,
  a company blacklisted by the Pentagon over ties to the People's Liberation Army,
  according to the Financial Times. The skyrocketing prices of RAM and storage have
  driven Apple [&#8230;]
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: dfcf3c7896d1cdb3
source_type: news_media
tldr: 苹果寻求特朗普政府批准，从被五角大楼列入黑名单的中国芯片供应商CXMT采购RAM芯片
objective_summary: 据《金融时报》报道，苹果因RAM和存储价格飙升而提高了全线产品价格，现向特朗普政府申请豁免，以合法从涉军黑名单企业长鑫存储（CXMT）采购内存芯片。此举面临国会中国委员会主席John
  Moolenaar的批评，称其将是个严重错误。
event_type: policy_and_safety
epistemic_status: verified_fact
entities:
  companies:
  - Apple
  - CXMT
  - Pentagon
  - Financial Times
  - Commerce Department
  - Trump administration
  - House China Committee
  technologies: []
  key_people:
  - Tim Cook
  - John Moolenaar
  - Donald Trump
key_logic_flow:
- 苹果正寻求特朗普政府豁免，以从被五角大楼列入黑名单的中国DRAM厂商长鑫存储（CXMT）采购内存芯片
- RAM和存储价格飙升已迫使苹果本周上调几乎所有产品线的价格，推动其寻找替代供应商
- 苹果在法律上不被禁止从CXMT购买芯片，但与涉华军事企业交易存在严重的声誉风险
- CXMT此前已被商务部列入拟议的"实体清单"追加名单，但因白宫正与中国进行贸易谈判而暂缓执行
- 众议院中国委员会主席John Moolenaar公开批评称，苹果若与涉华军事企业合作将是"一个严重错误"
extract_result: success
impact_score:
  score: 3.5
  reason: 该事件本质是地缘政治与供应链新闻，非AI技术突破。但内存（DRAM/HBM）是AI训练和推理基础设施的核心组件，苹果作为AI赛道重要玩家（Apple
    Intelligence）的采购困境，反映了上游存储涨价对全行业成本的压力传导。然而目前仅是申请豁免阶段，尚未落地，且对AI范式无直接影响，因此冲击力中等偏低。
sentiment: mixed
developer_sentiment:
  tone: skeptical
  primary_focus: 内存供应链紧张对AI基础设施部署成本和硬件可及性的潜在影响
hype_assessment:
  level: low
  reason: 该报道源自《金融时报》的实地调查，引用具体法律条款、国会人物公开表态和苹果定价变动等可验证事实，没有使用'颠覆''革命性'等夸张词汇，属于扎实的科技商业新闻报道。
information_entropy: medium
domain_disruption:
  technical_innovation: 无
  business_model: 若苹果获豁免，可能开创美国大型科技公司从涉华军事企业采购存储芯片的先例，削弱'去风险化'供应链策略的约束力，但CXMT目前主要生产成熟制程DRAM，与三星/SK海力士在HBM等AI关键存储领域差距较大，短期对AI算力供应链格局重塑有限。
engineering_complexity: production_ready
compound_value:
  score: 5.5
  reason: 该事件本身是一笔供应链交易谈判，不构成技术复利。但其深层信号——AI 对 HBM 和 DDR5 的井喷需求正导致全球 DRAM 产能紧张、价格飙升——具有中长期结构性意义。苹果作为全球议价能力最强的消费电子厂商，都被迫提价并寻求被制裁供应商，说明
    AI 对存储的消耗已开始挤压整个硬件成本结构。如果这一趋势持续（2-3 年内 HBM 产能扩张有限），将改变 AI 推理服务器的部署成本和终端设备的内存配置格局。该信号值得持续追踪，但仅靠单一数据点不足以给出高复利评分。
value_capture_layer: hardware_compute
moat_impact: creates_new_moat
key_beneficiaries:
- Samsung
- SK Hynix
- Micron Technology
- CXMT (长鑫存储)
competitive_casualty:
- 中小型消费电子硬件厂商
- 依赖低价内存的 AI 边缘设备创业公司
- 未提前锁定 DRAM 长协的服务器 OEM
market_opportunities:
- 非中国本土的DRAM制造商（如三星、SK海力士、美光）可借此机会加强与苹果的供应合作，填补CXMT可能带来的供应缺口并锁定长期订单
- 供应链风险合规咨询服务需求激增——帮助科技企业在美国出口管制与涉军黑名单制度下规划合法的替代采购方案，可作为一个细分专业服务方向
- 替代存储技术（如新型非易失性存储器、CXL内存池化方案）的创业公司可加速产品落地，以缓解DRAM供应集中化带来的价格风险
risk_matrix:
  regulatory: 极高监管风险：CXMT已被五角大楼列入涉军黑名单，且曾被商务部拟议列入实体清单。若苹果未获明确豁免即进行采购，可能面临出口管制违规、制裁或罚款；即使获得豁免，若中美贸易谈判破裂，CXMT随时可能被正式列入实体清单，导致供应中断连带法律责任
  technological: 技术供应风险：DRAM属于高度标准化的存储芯片，CXMT在制程工艺上落后于三星、SK海力士和美光。若苹果依赖CXMT供应，一旦供应被制裁切断，需快速切换回原有供应商，可能面临产能不足和价格波动
  competitive: 竞争格局风险：若苹果获得豁免，将引发其他美国科技企业（如戴尔、惠普、AMD）效仿寻求类似许可，可能导致对中国涉军芯片供应商的依赖面扩大，同时挤压美光等美国本土DRAM厂商的市场份额
  ethical: 国家安全伦理风险：与涉华军事企业交易可能间接支持中国军事现代化，在舆论和国会层面引发强烈反弹。众议院中国委员会主席已明确批评此举是'严重错误'，企业声誉和品牌形象将遭受重大冲击
  additional:
  - 地缘政治博弈风险：该事件发生在中美贸易谈判关键期，苹果的申请可能被政治化，成为谈判筹码或引发更大范围的科技供应链审查
  - 声誉连锁风险：苹果此前在用户隐私和供应链责任方面树立了高标准形象，与涉军黑名单企业的交易将严重损害这一品牌资产
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: monitor
---

Apple is looking to alleviate some of the pressure on its supply chain by seeking an exception from the Trump administration to buy RAM chips from CXMT, a company blacklisted by the Pentagon over ties to the People’s Liberation Army, according to the *Financial Times*. The skyrocketing prices of RAM and storage have driven Apple to raise prices on almost all of its products this week, so it makes sense that it would seek alternative sources.

# Apple wants permission to buy memory from a blacklisted Chinese supplier

The company can legally buy RAM from CXMT, but it would carry serious reputational risks.

The company can legally buy RAM from CXMT, but it would carry serious reputational risks.

Legally, Apple isn’t barred from buying chips from CXMT, but doing business with a company tied to the Chinese military would carry serious reputational risks. It’s possible that CXMT could still find itself the target of export controls for undermining US security. The company was on a list of proposed additions to the so-called “Entity List” by the Commerce Department, but held off because the White House was in the middle of trade negotiations with China.

It’s unclear if the administration would give its blessing to Apple. Tim Cook has spent significant time trying to build bridges with the Trump administration, presenting the president with gaudy statues and attending a screening of the *Melania* movie, directed by accused rapist Brett Ratner. But if the White House granted Apple permission, such a decision would likely face significant blowback. John Moolenaar, Republican chair of the House China committee, told the *Financial Times* that:

“Apple choosing to partner with a Chinese military company would be a grave mistake... Helping the [Chinese Communist Party] succeed in its plans to dominate critical supply chains will make our country’s tech industry and economy more dependent on China at a time when we must build secure tech supply chains with our allies,”


**Follow topics and authors**from this story to see more like this in your personalized homepage feed and to receive email updates.

## Most Popular

- Why is Apple asking me to pay more for Big Tech’s AI obsession?
- Anthropic’s Mythos 5 is back
- After covering Prime Day for 36 hours over four days, this is the one thing I bought
- Meta launches cheaper smart glasses without Ray-Ban
- Indie developers got tired of waiting for a new Star Fox, so they’re making their own