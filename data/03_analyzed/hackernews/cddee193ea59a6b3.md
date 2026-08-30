---
title: Memory prices climb 500% in 12 months
source: https://www.tomshardware.com/pc-components/ram/memory-prices-climb-500-percent-in-12-months-up-to-10x-the-lowest-ever-tracked-prices-128gb-of-ddr5-now-usd3-399
author:
- '[[haunter]]'
published: '2026-08-17'
created: '2026-08-17'
manifest_dates:
- '2026-08-17'
description: ''
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: cddee193ea59a6b3
source_type: community_discussion
tldr: 内存（DRAM）价格12个月内暴涨约500%，128GB DDR5套件现价达$3,399，为历史最低价的10倍。AI数据中心需求抢占了几乎所有DRAM产能，DDR4及SSD/HDD价格同步上涨，业界预测供应紧张将持续至2027至2030年。
objective_summary: 据Tom's Hardware报道，2025年8月至2026年8月DDR5内存价格同比上涨接近500%，128GB DDR5套件达$3,399，是历史最低价记录的十倍。PCPartPicker数据显示64GB（2×32GB）DDR5-5600套件均价从约$191涨至$1,118，DDR4套件价格也上涨了120%至180%。德国ComputerBase报告欧洲内存均价自2025年9月以来上涨345%，硬盘与SSD价格同期上涨超过125%。深层原因是AI数据中心建设抢占DRAM产能，SK
  hynix、Samsung、Micron与CXMT四家厂商营收成倍增长，SK Hynix CEO与ADATA董事长均预测供应紧张将持续多年。
event_type: infrastructure_update
epistemic_status: verified_fact
entities:
  companies:
  - SK hynix
  - Samsung
  - Micron
  - CXMT
  - ADATA
  - ComputerBase
  - PCPartPicker
  - Tom's Hardware
  technologies:
  - DDR5
  - DDR4
  - DRAM
  key_people:
  - Kwak Noh-jung
  - Simon Chen
key_logic_flow:
- 2025年8月至2026年8月，DDR5内存价格同比上涨接近500%，128GB DDR5套件现价达$3,399，是历史最低跟踪价格的十倍。
- PCPartPicker数据显示，64GB（2×32GB）DDR5-5600套件均价从约$191涨至$1,118，而DDR4套件价格也因外溢需求上涨了120%至180%。
- 德国ComputerBase报告欧洲平均内存价格自2025年9月以来上涨345%，HDD与SSD价格同期上涨超过125%，显示涨价是全球性现象。
- 超大规模买家已提前锁定2027年几乎全部全球DRAM产能，DRAM芯片每公斤价值已超过黄金的一半，PC和手机厂商只能在剩余产能中争夺。
- SK hynix、Samsung、Micron与CXMT四家内存厂商营收在一年内成倍增长，SK Hynix CEO预测2027年将是供应最紧张的一年，ADATA董事长认为危机可能持续十年。
object_mentions:
- object_type: product
  name: PCPartPicker
  canonical_name: PCPartPicker
  url: https://pcpartpicker.com
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 文章引用了PCPartPicker的平均价格数据，对比2025年8月与2026年8月各规格DDR5和DDR4内存套件的价格变化。
  article_id: cddee193ea59a6b3
- object_type: company
  name: ComputerBase
  canonical_name: ComputerBase
  url: https://www.computerbase.de
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 德国科技网站ComputerBase报告欧洲平均内存价格较2025年9月上涨345%，同时硬盘和SSD价格也上涨超过125%。
  article_id: cddee193ea59a6b3
extract_result: success
impact_score:
  score: 7.0
  reason: 内存价格一年暴涨约500%是AI需求爆发向基础设施供应链传导的标志性事件：它直接抬高AI训练/推理与企业硬件成本，让SK海力士、三星、美光等内存厂商获得空前定价权，并促使超大规模买家以预付订金锁定2027年全球DRAM产能，深刻改变AI算力的成本结构与议价格局。但本质是供需错配的市场现象，而非新技术范式或产品发布，冲击力介于'改变局部竞争格局'与'行业范式转移'之间，故评7分。
sentiment: mixed
developer_sentiment:
  tone: frustrated
  primary_focus: 内存与HBM短缺推高AI算力成本，挤压个人开发者与中小团队的自建硬件和推理部署预算
hype_assessment:
  level: low
  reason: 标题使用RAMageddon/RAMpocalypse等戏剧化词汇博取眼球，但核心论断均有硬数据支撑：PCPartPicker与ComputerBase的价格追踪表可独立验证，500%涨幅、DDR4涨120%-180%、欧洲涨345%等均有具体数字，非凭空炒作。厂商对持续时间的分歧预测（2027-2030甚至十年）属观点而非事实，存在一定不确定性，但不足以构成概念炒作。
information_entropy: high
domain_disruption:
  technical_innovation: 非技术突破事件。本质技术驱动力是AI加速器对HBM与高带宽内存的需求井喷：HBM制造占用更多晶圆面积且堆叠工艺更复杂，叠加DRAM制程微缩逼近物理极限、良率提升放缓，导致传统DRAM供给弹性大幅降低；同时中国厂商CXMT在全球供应格局中快速崛起，改写原有产能版图。
  business_model: 内存从普通大宗商品转变为战略稀缺资源：超大规模买家以预付订金锁定未来数年产能，形成类似能源行业的长期承购协议模式；内存厂商获得空前定价权、营收成倍增长。对AI基础设施与SaaS生态而言，内存/HBM成为继GPU之后的新成本瓶颈，推理成本与服务器造价持续上行。
engineering_complexity: infrastructure
compound_value:
  score: 7.5
  reason: 该事件本质是AI数据中心建设对DRAM产能的虹吸效应，揭示了内存从大宗商品向战略稀缺资源的定价权迁移。投资逻辑链：①需求端——AI训练/推理对HBM及大容量内存的需求是结构性而非周期性增长，超大规模买家已提前锁定2027年几乎全部全球DRAM产能并支付预付款，需求确定性极高；②供给端——DRAM行业被SK
    hynix/Samsung/Micron/CXMT四家寡头垄断，新增产能建设周期长达2-3年且HBM堆叠工艺壁垒极高，短期无替代方案，供给刚性支撑长期定价权；③复利循环——四家厂商营收一年内成倍增长，将转化为更高资本开支与更先进工艺，形成'强者恒强'的自我强化飞轮。扣分项：内存是强周期商品，500%涨幅已显著偏离成本曲线，将刺激全球扩产（尤其CXMT及中国产能），且若AI资本开支周期证伪或HBM供给释放，价格可能快速回落；ADATA预测危机持续十年过于乐观，需持续验证AI需求能否消化新增供给。综合看，内存寡头在3-5年内仍是AI计算基础设施的确定受益者，具备基础设施级复利属性，但周期性反转风险使其暂未达到8分以上的极强复利档位。
value_capture_layer: hardware_compute
moat_impact: strengthens_monopoly
key_beneficiaries:
- SK hynix
- Samsung
- Micron
- CXMT
- NVIDIA
competitive_casualty:
- PC与手机OEM厂商
- 中小服务器及白牌厂商
- 中小AI初创公司
- 传统企业IT采购方
market_opportunities:
- 建议 AI 推理与模型服务厂商将'低内存占用'提升为一级战略目标，通过量化、KV Cache 压缩、稀疏化与投机解码等手段降低单次请求的 DRAM 消耗——在内存价格高企的环境下，这类优化将直接转化为成本竞争力和毛利率优势
- 具备采购能力的厂商应通过长单与预付款锁定内存产能（超大规模买家已提前锁定 2027 年全球产能），中小企业则可借道按需计费的云厂商弹性内存池规避硬件涨价，供应链金融与备货套利存在套利窗口
- 内存短缺为替代技术打开快速落地窗口：CXL 内存池化、计算型存储、近存计算以及面向边缘的低内存推理方案有望获得更快采纳，创业团队可聚焦这些方向的工程化与商业化
risk_matrix:
  regulatory: 地缘与技术出口管制风险上升：CXMT 等中国厂商高速扩产可能触发美国进一步限制先进 DRAM/HBM 设备与技术出口，形成新一轮供应链管制博弈；此外
    DRAM 行业历史上多次因价格操纵遭反垄断调查，此轮暴涨可能引发监管介入与价格干预
  technological: 内存行业强周期反转风险——历史上 DRAM 高价期后往往伴随产能集中扩张与需求回落，若 AI 投资退潮或架构转向（CXL 内存池化、近存计算、更高效的压缩算法）导致单位算力内存需求下降，2028
    年后可能出现供需反转与价格崩塌，按当前高价锁定的长期产能将面临减值
  competitive: 四大厂商营收暴增将触发新一轮资本开支竞赛与新产能入场（含 CXMT 扩产），竞争格局可能重塑；云厂商凭借锁定产能获得显著成本优势，进一步挤压中小
    AI 企业的算力与内存获取能力，形成生态级马太效应
  ethical: 终端消费者、教育机构与中小企业被迫承受超高硬件成本，加剧数字鸿沟；显卡、游戏主机、手机等全品类连带涨价推高全社会数字化成本，可能诱发囤货与黄牛炒作；AI
    数据中心对基础资源的虹吸效应正引发'AI 成本外部化'的公众负面情绪
  additional:
  - 宏观经济风险：若全球金融市场对 AI 叙事出现大幅回调，内存需求与价格可能剧烈反转，形成新一轮供应链冲击并放大系统性金融波动
  - 供应链集中度风险：内存制造高度集中于少数厂商与少数地区，自然灾害或地缘冲突一旦冲击核心产能，供应紧张将被进一步放大
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: strategic_invest
object_insights:
- object_type: product
  name: PCPartPicker
  canonical_name: PCPartPicker
  url: https://pcpartpicker.com
  positioning: PCPartPicker是面向PC装机用户的配件选购与价格对比平台，提供配件兼容性校验、多零售商实时比价与历史价格追踪服务。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - PC装机与DIY爱好者
  - 计划组装或升级电脑的消费者
  - 硬件行业媒体与分析师
  product_signal: PCPartPicker为PC装机提供配件兼容性校验与多零售商比价，其平均价格数据可量化追踪内存等核心配件的价格走势。
  market_signal: PCPartPicker数据反映DDR5内存均价一年内上涨近500%，64GB套件从191美元涨至1118美元，成为内存市场供需失衡的量化证据。
  differentiation: PCPartPicker以兼容性筛选与历史均价追踪见长，其均价数据被Tom's Hardware等科技媒体引为市场价格基准，具备数据权威性。
  watch_reason: PCPartPicker的平均价格数据被主流科技媒体持续引用，是观察内存与存储市场供需变化的关键量化窗口。在AI数据中心抢占DRAM产能、供应紧张或持续至2030年的背景下，其价格追踪能力使其成为跟踪内存危机演进与消费者承受度的重要指标，值得纳入专题持续监测。
  risk_notes:
  - PCPartPicker数据为平台聚合均价，与个别零售商实际成交价存在偏差，作为市场基准存在一定误差。
  - 内存价格上涨由AI需求驱动，若AI市场回调则均价数据可能快速逆转，PCPartPicker数据趋势未必代表长期方向。
  score: 4.0
  article_ids:
  - cddee193ea59a6b3
  evidence_snippets:
  - 文章引用了PCPartPicker的平均价格数据，对比2025年8月与2026年8月各规格DDR5和DDR4内存套件的价格变化。
---

We're officially in dire straits. There's almost no way, if you're reading this site, that you aren't aware that memory prices have become entirely divorced from reality. Some are calling it the RAMpocalypse; I prefer "RAMageddon." Whatever you want to call it, though, the reality for PC builders right now is just grim. To put this in perspective, just take a look at our RAM price tracking post:

|
|
|
DDR5-5200 16GB |
$52 |
|
DDR5-5600 16GB |
$199 |
|
DDR5-5600 32GB |
$72 |
|
DDR5-6000 16GB |
$197 |
|
DDR5-6000 32GB |
$72 |
|
DDR5-6000 48GB |
$144 |
|
DDR5-6000 64GB |
$159 |
|
DDR5-6000 96GB |
$189 |
|
DDR5-6400 128GB |
$329 |
|
DDR5-6600 32GB |
$158 |

That's right: 128GB DDR5 kits are fully ten times more expensive than the lowest price we've ever seen. Things improve as you step down the memory capacities and speed tiers, but not as much as we'd like. You're still looking at $392 for a memory kit that was just $72 last year.

To reinforce the point, I pulled the latest average price data from PCPartPicker, comparing where we are today (August 2026) to exactly one year ago. This data is somewhat approximate, but it should be broadly accurate.

Memory Kit Speed & Size |
August 2025 Average Price |
August 2026 Average Price |
Change (YoY) |
|---|---|---|---|
4800 MT/s 2×16GB |
$90 |
$425 |
+$335 |
5200 MT/s 2×16GB |
$100 |
$480 |
+$380 |
5600 MT/s 2×16GB |
$116 |
$528 |
+$412 |
6000 MT/s 2×16GB |
$108 |
$572 |
+$463 |
5600 MT/s 2×32GB |
$191 |
$1118 |
+$927 |
6000 MT/s 2×32GB |
$222 |
$1272 |
+$1050 |

The numbers speak for themselves; in just 12 months, the cost of DDR5 memory has essentially exploded. We are looking at year-over-year increases nearing 500% for high-capacity kits. A standard 64GB (2x32GB) DDR5-5600 kit that would have cost you under $200 last summer is now demanding over $1,100. It is a 5x multiplier on a component that used to be a fairly boring and predictable line item in a PC build budget.

Memory Kit Speed & Size |
August 2025 Average Price |
August 2026 Average Price |
Change (YoY) |
|---|---|---|---|
3200 MT/s 2×8GB |
$63 |
$163 |
+$100 |
3600 MT/s 2×8GB |
$75 |
$165 |
+$90 |
3200 MT/s 2×16GB |
$105 |
$281 |
+$176 |
3600 MT/s 2×16GB |
$120 |
$307 |
+$187 |
3200 MT/s 2×32GB |
$222 |
$614 |
+$392 |
3600 MT/s 2×32GB |
$300 |
$789 |
+$489 |

If you plan to just wait it out on an older AM4 or LGA1700 motherboard with DDR4, you'd better hope your memory holds out too, because DDR4 isn't safe from the fallout. With DDR5 entirely out of reach for most builders, the resulting scramble for older platforms running DDR4 memory has created a massive knock-on effect, and as a result, DDR4 kits are up anywhere from 120% to nearly 180% across the board. Nowhere near as bad as DDR5 pricing, but it still stings when a kit that was $105 last year is $281 this year.

This phenomenon is by no means exclusive to the US, either. German tech site *ComputerBase* have also been tracking this global trend, reporting just this week that average RAM prices in Europe have skyrocketed by 345% compared to September 2025. Their data shows the squeeze is bleeding into other components too, with hard drive and SSD prices both climbing over 125% in that same timeframe.

In fact, the situation is so severe that hyperscale buyers have reportedly already locked in almost all of the global DRAM production capacity for 2027, handing over advance deposits to guarantee their supply of precious DRAM, which is now among the highest-value commodities in the world by weight; mainstream DRAM chips are worth over half as much per kilogram as solid gold. PC and smartphone makers are simply fighting over the scraps, as low-priority markets compared to the extremely lucrative AI datacenter buildouts. And lucrative they are indeed; all four memory vendors (SK hynix, Samsung, Micron, and China's CXMT) have increased revenues by double, triple, or even more, all in just the space of one year.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

For consumer prices to drop, we would essentially need a major contraction in the AI market, which would mean a massive correction in financial markets worldwide. Absent that, the people actually making the chips don't see an end in sight. SK Hynix CEO Kwak Noh-jung recently warned that 2027 will be the worst year for memory supply in the industry's history, forecasting that demand will outstrip their ability to produce it well into 2030. ADATA's Chairman, Simon Chen, was even more pessimistic, suggesting this DRAM crisis could last another 10 years and dismissing the idea of an "AI bubble" bursting anytime soon.

The era of cheap, plentiful memory is over, at least for now. If you need RAM today, you're either going to have to bite the bullet and pay the premium, or learn to get by with less. Make sure you check out our RAM price tracking post for the best deals we found on memory, as well as some tips on how to secure solid deals yourself.

*Follow** Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Zak is a freelance contributor to Tom's Hardware with decades of PC benchmarking experience who has also written for HotHardware and The Tech Report. A modern-day Renaissance man, he may not be an expert on anything, but he knows just a little about nearly everything.

-
Very glad I upgraded to AM5 about 6 months ago. That said, direct RAM prices aren't really the worst part. Every single GPU and every video game console and so forth are all badly affected by this as well. It's a significant overall inflation on many digital products.Reply
-
A few years ago when there was a used car shortage, I could have sold my then 5-year old vehicle for more than I bought it for new, defying normal depreciation expectations. That didn't last long-term, and this won't either, because it can't.Reply


To some extent, it is just the market at work, doing what it's supposed to do - in times of demand severely outpacing supply, high prices help to ensure it's at least still possible to get what you need if you really need it - even if it's essentially being highly discouraged - and also for the longer-term, the profit potential encourages increasing supply.


But for anyone who doesn't absolutely have to upgrade/replace memory now/in the next couple years, it makes sense to wait. I think it will probably be 2029/2030 before I think about buying any more hardware, unless the AI bubble bursts and things rapidly change before then.


For games - and software in general - this is also something developers need to be thinking about when making projections about what hardware customers are likely to have, and the associated tradeoffs - because there's always sort of a balance to strike between quantity of features and optimization/runtime efficiency, and also what kinds of features are worth building into the product. -
Replyinverse137 said:This is not "greed" this is supply vs demand in action.


Just curious, if you call this "greed," then what did you call the low point?

If the memory makers hadn't increased prices, it would be much worse today - it would be another one of those cases where scalpers buy up most of the product readily available. And anyone else who gets the opportunity to do so at MSRP would buy the maximum amount possible - even more than they would have purchased normally/without the shortage - just because they don't know if they'd get the chance to do so again at a reasonable price later.


So the vast majority of people who needed memory for a new system - if they could get it at all - would be forced into buying from a seller of questionable repute on Ebay, facing the possibility of getting scammed, and having to wonder if they'd be able to get warranty coverage. While the high prices are unwelcome, I'd still rather see high retail prices from reputable sellers than deal with that. -
Reply

I've found it easy to get good used memory on ebay. Ignore sellers with low ratings or near zero sales, ignore China.timsSOFTWARE said:forced into buying from a seller of questionable repute on Ebay, facing the possibility of getting scammed, and having to wonder if they'd be able to get warranty coverage.


There are sellers with thousands or tens of thousands of sales and 99-100% rating.


I get no warranty beyond maybe 30 days, but it seems the value of those is questionable these days. -
The saddest thing is there's someone who's getting ready to build a brand new PC anyway in some pseudo attempt to "stick it to the man" Yeah Im gonna drop $1000 on two sticks of ram, that'll learn em!!!!!Reply
-
Reply

That doesn't sound like a common scenario. Which is why sales are dropping.teeejay94 said:The saddest thing is there's someone who's getting ready to build a brand new PC anyway in some pseudo attempt to "stick it to the man" Yeah Im gonna drop $1000 on two sticks of ram, that'll learn em!!!!!


A sad thing is that people who need CPU performance (for real work) will have to bite the bullet and pay the DDR5 premium.


For example, a Ryzen 9 9950X is around 40-45% faster (TechPowerUp, PassMark) than a Ryzen 9 5950X. 24-core Zen 6 could be around 150% faster than a Ryzen 9 5950X. Even if you have to pay $900 on a 64 GB kit, it could be worth it.