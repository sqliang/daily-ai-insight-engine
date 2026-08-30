---
title: Nine PBS sues Iron Mountain over blocked access to archival data
source: https://current.org/2026/08/nine-pbs-sues-iron-mountain-over-blocked-access-to-archival-data/
author:
- '[[vinayakborkar]]'
published: '2026-08-13'
created: '2026-08-14'
manifest_dates:
- '2026-08-14'
description: 'Article URL: https://current.org/2026/08/nine-pbs-sues-iron-mountain-over-blocked-access-to-archival-data/
  Comments URL: https://news.ycombinator.com/item?id=49285418 Points: 309 # Comments:
  181'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: cfc940fac2fa9e44
source_type: community_discussion
tldr: 圣路易斯公共电视台Nine PBS起诉信息管理和数据中心公司Iron Mountain，要求取回超过50TB档案数据。此前其云存储供应商Open Source
  Storage突然倒闭并切断访问，Iron Mountain以基础设施所有权属于OSS为由拒绝归还。
objective_summary: 圣路易斯公共电视台Nine PBS于2025年7月28日在丹佛地区法院起诉Iron Mountain Data Centers，要求恢复对存储在丹佛数据中心超过50TB档案资料的访问权。Nine
  PBS的云存储供应商Open Source Storage在2026年3月6日合同到期后突然切断访问并停止运营，导致这些涵盖该机构70年历史的数据滞留于Iron
  Mountain设施中。Iron Mountain以OSS才是存放数据的物理基础设施所有方为由拒绝归还数据，尽管Nine PBS已获圣路易斯巡回法院默认判决确认其拥有数据所有权和立即占有权。
event_type: policy_and_safety
epistemic_status: verified_fact
entities:
  companies:
  - Nine PBS
  - Iron Mountain Data Centers
  - Open Source Storage
  - OSS
  technologies:
  - cloud storage
  - data center
  key_people:
  - Leah Freeman
  - Charles Wells
  - James Tramel
  - Ben Nicholson
  - Justine Ririe
key_logic_flow:
- Nine PBS自2019年起通过OSS前身供应商使用硬件、软件和云存储服务保存档案资料，并逐年续约合同。
- 2026年2月Nine PBS联系OSS商讨续约，OSS未予回应；3月6日合同到期当天，OSS突然切断访问且网站已无法访问。
- Nine PBS调查发现OSS与Iron Mountain存在独立的数据存储合作关系，其档案实际存放在Iron Mountain位于丹佛的数据中心。
- Nine PBS于3月13日向Iron Mountain发出要求保全并归还数据的律师函，但Iron Mountain当时未确认是否持有数据。
- Nine PBS在圣路易斯巡回法院起诉OSS并获默认判决，法院确认Nine PBS拥有数据所有权和立即占有权。
- Iron Mountain后来承认持有数据，但以OSS拥有物理基础设施所有权为由拒绝归还，Nine PBS遂于7月28日向丹佛地区法院起诉Iron Mountain。
object_mentions:
- object_type: company
  name: Iron Mountain Data Centers
  canonical_name: Iron Mountain
  url: https://www.ironmountain.com/data-centers
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Nine PBS in St. Louis filed a lawsuit against information management corporation
    Iron Mountain Data Centers July 28.
  - Iron Mountain has refused to return the materials to the station because its client,
    OSS, technically owned the physical services housing the data.
  - A district judge granted the motion for temporary and preliminary relief and set
    a hearing for Wednesday.
  article_id: cfc940fac2fa9e44
- object_type: company
  name: Open Source Storage
  canonical_name: Open Source Storage (OSS)
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - The lawsuit alleges that the station's cloud-storage vendor, Open Source Storage,
    abruptly cut off access to Nine PBS' data earlier this year without warning.
  - OSS, which had a separate relationship with Iron Mountain to provide data storage,
    went defunct, leaving Nine PBS' archives in a data center operated by Iron Mountain.
  - Nine PBS renewed its contracts with the data services vendor and subsequently
    OSS annually before the agreement was set to expire on March 6.
  article_id: cfc940fac2fa9e44
- object_type: product
  name: OSS cloud-storage service
  canonical_name: Open Source Storage cloud-storage service
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - An unidentified vendor described as OSS' predecessor provided hardware, software
    and cloud-storage services for storing the public broadcaster's archival materials
    and other data.
  - The contract provided 30 days for Nine PBS to retrieve its data from OSS' storage
    upon termination of services.
  - Nine PBS sent a demand letter to Iron Mountain offering to pay any reasonable
    costs associated with preserving and returning its data.
  article_id: cfc940fac2fa9e44
extract_result: success
impact_score:
  score: 4.2
  reason: 这是一起公共电视台与云存储/数据中心供应商之间的数据托管纠纷诉讼，虽然本身不属于AI技术突破，但它直接触及AI与数据基础设施的核心命题：数据可迁移性、供应商锁定和灾备合规。单一案例不会重塑行业格局，但会强化组织在选择云存储、评估供应商连续性方面的风险意识，对媒体、科研和企业AI数据治理具有一定警示意义。
sentiment: negative
developer_sentiment:
  tone: skeptical
  primary_focus: 云存储托管链中的数据归属、供应商倒闭时的数据可迁移性，以及物理基础设施所有权与数据所有权分离带来的法律救济困境
hype_assessment:
  level: low
  reason: 这是一篇基于法院诉讼文件和当事方声明的新闻报道，提供了具体的时间线、数据量和法律程序细节，没有使用'颠覆'、'革命性'等PR夸张词汇，属于可验证的事实性事件。
information_entropy: medium
domain_disruption:
  technical_innovation: 无
  business_model: 提醒依赖第三方云存储和数据中心托管的机构，必须将供应商连续性、数据可迁移性条款和多云/异地备份纳入AI数据资产管理与合规框架，可能推动灾备与数据主权服务需求上升
engineering_complexity: production_ready
compound_value:
  score: 4.5
  reason: 本案本身是一场单一法律纠纷，不具备技术网络效应或规模复利。但它暴露了云存储供应链中'客户-转售商-数据中心'多层托管结构的产权模糊风险：当转售商（OSS）倒闭后，作为终端客户的
    Nine PBS 虽拥有数据所有权，却无法从物理托管方（Iron Mountain）取回数据。该事件将强化企业在数据备份、多云容灾、数据托管权（digital
    escrow）及供应商尽职调查上的支出意愿。然而，其价值更多体现为合规与风险预算的再分配，而非催生新平台级机会；3-5 年后相关判例可能沉淀为云存储/托管行业的标准合同条款，但不会成为行业基石性资产。
value_capture_layer: cloud_platform
moat_impact: strengthens_monopoly
key_beneficiaries:
- AWS
- Microsoft Azure
- Google Cloud
- Veeam
- Rubrik
- Commvault
competitive_casualty:
- Open Source Storage
- 小型云存储转售商
- 长尾云备份服务商
- 数据中心产权结构不透明的托管服务商
market_opportunities:
- 企业级数据托管与第三方存管服务需求将上升，可开发独立于云厂商的数据 escrow、所有权公证与灾难恢复解决方案
- 面向档案馆、媒体机构与合规敏感行业的多云/混合云数据可移植性咨询与迁移工具存在商业化空间
- 法律科技公司可针对云存储合同中的数据归属、供应商破产及物理基础设施权属条款提供智能审查与风险预警产品
risk_matrix:
  regulatory: 云存储与数据 custody 领域的立法和司法解释尚不完善，供应商破产、数据中心拒绝返还数据可能触发数据保护、公共档案保存及破产法层面的合规争议，且未来或面临更严格的数据可迁移性监管
  technological: 过度依赖单一云存储或中间商服务商会带来严重的供应商锁定与数据不可达风险，物理基础设施所有权与数据所有权分离的架构设计存在关键单点故障
  competitive: 头部云厂商可能借机强化数据主权、可迁移性保障与托管透明度服务，挤压中小型独立存储与中间件服务商的市场份额
  ethical: 公共媒体机构七十年历史档案数据被滞留，若无法恢复将对文化遗产保护、公共信息可及性造成不可逆损失，并引发公众对云服务商信任危机
  additional:
  - 供应链连带责任风险：客户与底层数据中心之间缺乏直接合同关系，中间商倒闭后数据取回路径断裂
  - 诉讼先例风险：本案判决可能影响未来数据所有权、占有权与基础设施权属的司法认定
confidence:
  impact: high
  compound: medium
  hype: low
actionable_insight: monitor
object_insights:
- object_type: product
  name: OSS cloud-storage service
  canonical_name: Open Source Storage cloud-storage service
  url: null
  positioning: Open Source Storage 是一家向公共电视台等客户提供硬件、软件与云存储托管服务的供应商，本案显示其已停止运营并切断客户数据访问。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 公共电视台
  - 需要长期档案托管的机构客户
  product_signal: 其服务被 Nine PBS 用于保存超过 50TB、跨越 70 年历史的档案资料，但合同到期当天即被无预警切断访问。
  market_signal: 服务商突然倒闭导致客户数据滞留于上游数据中心，暴露出云存储托管链条中的资产安全与业务连续性风险。
  differentiation: 文章未提供与竞品相比的技术或服务差异化信息，主要凸显其在经营失败和数据归还责任上的负面信号。
  watch_reason: 该案例是云存储供应商倒闭后客户数据被锁定的罕见实例，对依赖第三方托管的关键历史资产具有强烈警示意义，值得跟踪后续诉讼进展与行业监管反应。
  risk_notes:
  - 合同到期后供应商突然失联并切断访问，客户几乎无缓冲时间取回数据。
  - 数据实际存放的物理基础设施由上游合作方持有，导致所有权与占有权分离。
  - 服务商经营失败后，客户被迫通过多地诉讼才能取回自己的数字资产。
  score: 6.0
  article_ids:
  - cfc940fac2fa9e44
  evidence_snippets:
  - 被描述为 OSS 前身的未具名供应商自 2019 年起为公共电视台提供保存档案资料所需的硬件、软件和云存储服务。
  - 根据合同，服务终止后 Nine PBS 有 30 天时间从 OSS 的存储中取回其数据。
  - Nine PBS 向 Iron Mountain 发出律师函，表示愿意承担保全和归还其数据所产生的任何合理费用。
---

By Billy Hathorn - Own work, CC BY-SA 3.0

Nine PBS in St. Louis filed a lawsuit against information management corporation Iron Mountain Data Centers July 28, seeking to recover over 50 terabytes of archival materials stored in one of the company’s Denver-based data centers.

The lawsuit filed in Denver District Court alleges that the station’s cloud-storage vendor, Open Source Storage, abruptly cut off access to Nine PBS’ data earlier this year without warning. It states OSS, which had a separate relationship with Iron Mountain to provide data storage, went “defunct,” leaving Nine PBS’ archives in a data center operated by Iron Mountain.

Iron Mountain has refused to return the materials to the station because its client, OSS, technically owned “the physical services housing the data” within Iron Mountain, according to the complaint.

The station requested temporary and preliminary relief that would prevent Iron Mountain from deleting, modifying or overwriting its materials in the suit. A district judge granted the motion and set a hearing for Wednesday.

In a statement to Current, Nine PBS VP and CCO Leah Freeman confirmed the station’s lawsuit against Iron Mountain and its dedication to retrieving the archival materials and programming, which she says span over “70 years of our organization’s history.”

“We are committed to ensuring we can recover and restore full access to this valuable content, which Nine PBS rightfully owns, as it holds significant historical importance for St. Louis.”

According to the lawsuit, the blocked materials include historical items such as Nine PBS’ coverage on the history of East St. Louis, the COVID-19 pandemic and the Great Flood of 1993, which ravaged along the Mississippi and Missouri rivers.

**‘No choice but to file’**

Nine PBS entered a relationship with a company described in the complaint as “OSS’ predecessor” in 2019. This unidentified vendor provided “hardware, software and cloud-storage services” for storing the public broadcaster’s archival materials and other data.

Nine PBS renewed its contracts with the data services vendor and subsequently OSS annually, the complaint states.

When Nine PBS attempted to schedule a meeting with OSS in February to discuss renewing for 2026, OSS didn’t respond or indicate “any intention not to renew the agreement.” The agreement was set to expire on March 6.

The contract provided 30 days for Nine PBS to retrieve its data from OSS’ storage “upon termination of services.” But on March 6, OSS cut off the station’s access without warning, according to the complaint. When Nine PBS attempted to contact OSS to sort out the problem, it discovered that OSS’ website was defunct and the company had delinquency status with the Colorado Secretary of State.

To ensure the station’s data remained secure, Nine PBS investigated further and discovered that OSS had a relationship with Iron Mountain, according to the complaint.

Nine PBS sent a demand letter March 13, demanding that Iron Mountain preserve and return its data and offering “to pay any reasonable costs associated with its demand.” Iron Mountain neither confirmed nor denied the data was in its possession, the lawsuit states.

Nine PBS filed a lawsuit against OSS and its “purported” president Charles Wells in the St. Louis Circuit Court April 16, the complaint states. The broadcaster later paused the litigation after James Tramel, a “managing partner of the group that officially acquired” OSS’ assets, confirmed that Nine PBS’ data was secure within Iron Mountain’s Denver data center.

After communicating with Nine PBS for about a month, Tramel stopped responding. Weeks later, an automatic reply email from his account stated that he was no longer affiliated with OSS. Tramel revealed in a subsequent phone call that he “had been defrauded” into purchasing OSS, according to the complaint. At this point, the company’s previous owners, including Wells, Ben Nicholson, and Justine Ririe, resumed control of OSS’ operations.

After Nine PBS attempted to contact OSS leadership without success, the station returned to the St. Louis Circuit Court and obtained a default judgment against OSS. The court’s ruling stated that the station both owned its data and had an “immediate right to possess the data,” according to the complaint. The judgment also ordered OSS to return the data to Nine PBS “and/or facilitate its transfer to a new vendor.”

An attorney representing Nine PBS contacted Iron Mountain about returning the data, and noted that “litigation was imminent in Colorado,” and the company admitted that it possessed the data, the complaint states. Iron Mountain initially indicated that it wanted to avoid litigation and comply with Nine PBS’ request, but later refused to do so, citing OSS’ ownership of the infrastructure that houses the data.

Nine PBS’ complaint states that, following multiple unsuccessful attempts to retrieve its digital property, it “had no choice but to file this lawsuit to force Iron Mountain to protect and ultimately provide” the data.

Iron Mountain did not respond to a request for comment.