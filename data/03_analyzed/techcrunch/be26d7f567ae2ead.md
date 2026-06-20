---
title: Amazon hopes to challenge Nvidia more directly by selling its AI chips
source: https://techcrunch.com/2026/06/18/amazon-hopes-to-challenge-nvidia-more-directly-by-selling-its-ai-chips/
author:
- '[[Julie Bort]]'
published: '2026-06-18'
created: '2026-06-19'
description: AWS is in talks to sell its chips to other data centers. CEO Andy Jassy
  has said this represents a $50 billion opportunity for the company.
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: be26d7f567ae2ead
source_type: news_media
tldr: AWS考虑向第三方出售Trainium AI芯片，直接挑战Nvidia的芯片主导地位
objective_summary: AWS AI负责人Peter DeSantis向Bloomberg透露，AWS正洽谈向第三方出售Trainium AI芯片。CEO
  Andy Jassy此前在股东信中称芯片业务若独立运营年收入可达约500亿美元。目前该计划处于早期商谈阶段。
event_type: capital_movement
epistemic_status: pr_statement
entities:
  companies:
  - Amazon
  - Amazon Web Services (AWS)
  - Nvidia
  - TSMC
  - Bloomberg
  technologies:
  - Trainium
  - Trainium4
  key_people:
  - Peter DeSantis
  - Andy Jassy
  - Doron Aronson
key_logic_flow:
- AWS AI负责人Peter DeSantis向Bloomberg透露，AWS正与多家公司洽谈出售其自研AI芯片Trainium用于数据中心部署。
- CEO Andy Jassy在4月年度股东信中首次暗示可能对外销售芯片，称芯片业务若独立运营年收入可达约500亿美元。
- 当前Trainium芯片及尚未上市的Trainium4的产能均已售罄，对外销售将面临产能分配难题。
- 直接出售芯片可能削弱AWS的瀑布效应收益——芯片带来的云服务连锁收入（存储、安全、网络、监控等）。
- Nvidia当前营收运行率约为3260亿美元，500亿美元的竞争体量虽不足以动摇其地位，但已接近Intel的年收入规模。
- AWS表示该计划仍处于非常早期的讨论阶段，历史上曾多次拒绝直接出售芯片的请求。
impact_score:
  score: 6.8
  reason: AWS作为全球最大云服务商考虑对外销售自研AI芯片Trainium，直接挑战Nvidia在AI芯片市场的主导地位，这是一个重大的战略转向信号。虽然仍处于早期商谈阶段——AWS历史上曾多次拒绝直接出售芯片的请求——但如果落地，将深刻改变AI芯片的竞争格局。CEO
    Andy Jassy声称芯片业务若独立运营年收入可达约500亿美元，体量已接近Intel年收入。但产能矛盾突出：当前Trainium及下一代Trainium4的产能均已售罄，对外销售需优先解决供应链瓶颈（TSMC产能已被Nvidia大量占据），短期内对Nvidia的实质性冲击有限。综合来看，这是一次重要的战略表态而非即时的市场冲击，评分6.8。
sentiment: mixed
developer_sentiment:
  tone: excited
  primary_focus: Trainium能否打破Nvidia CUDA生态的锁定效应，以及对外销售后软件栈和开发工具链的完善程度
hype_assessment:
  level: medium
  reason: 文中引用的'500亿美元年收入'是AWS CEO在股东信中基于'如果芯片业务独立运营'的假设性测算，并非实际营收，被作为核心新闻点放大传播。该假设忽略了AWS从芯片带来的云服务连锁收入（瀑布效应）以及当前产能全部售罄的现实约束。文章本身报道克制，明确标注'早期商谈阶段'并引用了AWS发言人的谨慎措辞，但该消息在传播链条中容易被简化为'AWS要颠覆Nvidia'，存在一定包装成分。
information_entropy: high
domain_disruption:
  technical_innovation: Trainium作为AWS自研的AI训练/推理专用ASIC，在能效比和总拥有成本上已具备与Nvidia竞争的实力。此次战略转向意味着AWS认为其芯片架构已成熟到可以脱离云服务独立对外销售。Trainium4尚未上市即已售罄，说明其技术路线获得了内部大规模客户的认可。不过，对外销售需要构建独立的软件栈、开发者工具链和客户支持体系，这些工程投入才是真正的技术门槛。
  business_model: AWS正在考虑打破其赖以成功的'瀑布效应'商业模式——过去通过自研芯片将客户锁定在AWS云上，赚取存储、安全、网络、监控等连带收入。直接出售芯片意味着AWS愿意部分放弃云服务超额收益，转型为芯片供应商角色。若此模式落地，可能倒逼其他云厂商（GCP、Azure）加速自研芯片对外销售，重塑云计算行业的芯片供应链格局。
engineering_complexity: production_ready
compound_value:
  score: 7.5
  reason: 此事件标志着 AWS 从'芯片自用'到'芯片外售'的战略范式转变，潜在年收入规模达 ~$500 亿（接近 Intel 年收入），具备极强的长期复利效应。核心复利逻辑有三层：(1)
    芯片生态锁定效应——一旦客户在 Trainium 上部署训练/推理工作负载，迁移成本极高，形成硬件+软件双重锁定；(2) 规模制造飞轮——外售带来的更大订单量可降低单位成本、加速下一代架构迭代，反向强化内外部竞争力；(3)
    与 AWS 云服务的瀑布效应协同——即使外售芯片，客户仍需配套的存储/网络/安全等 AWS 服务，形成混合变现模式。但扣分项同样显著：该计划仍处于'非常早期的商谈阶段'，历史上
    AWS 多次拒绝此类请求；现有 Trainium 及下一代 Trainium4 产能均已售罄，台积电产能瓶颈短期内难以突破；Nvidia 当前 $3260
    亿营收运行率意味着即使 $500 亿也只是其 ~15%，超越需数年；且直接出售芯片会削弱瀑布效应收益（每卖一片芯片意味着损失该芯片在 AWS 上产生的 3-5
    倍云服务连锁收入），内部激励机制存在根本矛盾。综合判定为 7.5 分——赛道空间和复利潜力真实存在，但执行路径极其陡峭，需持续观察产能分配策略和实际客户签约。3-5
    年后若成功落地，大概率成为 AI 算力基础设施的核心玩家之一。
value_capture_layer: hardware_compute
moat_impact: democratizes_access
key_beneficiaries:
- Amazon
- AWS
- TSMC
- 大型 AI 模型公司
- 云计算客户
competitive_casualty:
- NVIDIA
- AMD
- AI 芯片初创公司（Cerebras、Groq、SambaNova 等）
- Intel
market_opportunities:
- 第三方数据中心运营商和云服务商可借此获得Nvidia之外的高性能AI芯片供应选择，降低单一供应商锁定风险
- 云托管服务商（MSP）和AI基础设施集成商可围绕Trainium构建差异化推理优化方案，服务成本敏感型AI推理客户
- AI应用开发者可提前研究Trainium软件栈与生态，抢占可能更低的推理成本带来的部署红利
risk_matrix:
  regulatory: 先进AI芯片出口管制政策（如对华禁运）可能限制Trainium的全球市场拓展范围，增加合规复杂度
  technological: Trainium软件生态（编译器、框架集成、算子库）相比Nvidia CUDA的成熟度差距显著，客户从CUDA迁移的成本和技术风险较高
  competitive: Nvidia在AI芯片市场的品牌护城河和生态壁垒短期内不可撼动；AMD、Google TPU、微软等也在争夺同类市场；AWS对外卖芯片可能与其部分云客户的芯片业务产生利益冲突
  ethical: 产能若优先对外销售可能加剧AWS现有云客户的芯片供应等待；大型芯片制造的高能耗与碳排放问题
  additional:
  - 产能瓶颈——Trainium当前及下一代Trainium4的产能均已售罄，台积电产能被Nvidia大量占用，扩产面临激烈竞争
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: monitor
---

If Amazon Web Services has its way, the cloud giant is going to push even deeper into Nvidia’s market, in what might be one of the biggest challenges to Nvidia’s AI chip dominance we’ve seen so far.

Amazon’s AI chief Peter DeSantis told Bloomberg that AWS is in talks to sell its AI chip Trainium to other companies for use in data centers. DeSantis declined to specify which companies could be the buyers of these chips.

Such talk about selling chips is in the early stages, the company tells TechCrunch. They stem from Amazon CEO Andy Jassy’s annual shareholder letter in early April, in which he said the company’s homegrown AI chips were so coveted that he was thinking about selling them:

If our chips business was a standalone business, and sold chips produced this year to AWS and other third parties (as other leading chips companies do), our annual run rate would be ~$50 billion. There’s so much demand for our chips that it’s quite possible we’ll sell racks of them to third parties in the future.


How much of a challenge could Amazon be to Nvidia? A $50 billion competitor wouldn’t exactly tank Nvidia — which is currently on a $326 billion revenue run rate — if it keeps delivering quarters like the last one. But it’s akin to Intel’s annual revenue.

AWS has so far resisted selling its AI chips for a lot of reasons. The biggest is that the money AWS actually makes on its chips is a waterfall effect. Sure, it charges customers directly for the AI tokens those chips process on its cloud, but it also gets to charge for a host of other services companies need for their AI apps, including storage, security, networking, and monitoring services.

Equally important, Amazon has touted the capacity of its chips has been selling out faster than it can produce them. In that same shareholder letter in April, Jassy said the current Trainium chip capacity had sold out almost instantly. So, too, he said, had the capacity for the next one, Trainium4, which won’t even be available for more than a year. This was before AWS formally added OpenAI to the models it was serving up.

So selling its chips to others means it would likely have to leave current customers on waiting lists, unless it could somehow manufacture a surplus of chips through its manufacturing partners such as TSMC. But it would have to miraculously elbow Nvidia out of the way to do that with TSMC, which has recently supplanted Apple to become the foundry’s largest customer.

AWS spokesperson Doron Aronson (who hosted me during a recent private tour of the AWS chip design facility) also confirmed that AWS may sell these chips. “While we’ve historically declined requests to sell chips directly, Andy noted it’s quite possible we’ll sell racks of them to third parties in the future.”