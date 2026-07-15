---
title: Apple sues OpenAI, accuses ex-employees of stealing trade secrets
source: https://9to5mac.com/2026/07/10/apple-sues-openai-trade-secret-theft/
author:
- '[[stock_toaster]]'
published: '2026-07-10'
created: '2026-07-11'
description: 'https://www.macrumors.com/2026/07/10/apple-sues-openai/ Comments URL:
  https://news.ycombinator.com/item?id=48865019 Points: 1041 # Comments: 531'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: ba0dc24cfcb77dd2
source_type: community_discussion
tldr: Apple 起诉 OpenAI，指控前员工窃取商业机密以助 OpenAI 硬件业务
objective_summary: Apple 于 2026 年 7 月 10 日向美国加州北区联邦地区法院起诉 OpenAI，指控前产品设计副总裁 Tang Tan
  和前高级工程师 Chang Liu 窃取商业机密用于 OpenAI 的硬件业务。Apple 称 OpenAI 利用内部情报获取苹果未公开的硬件设计信息，
event_type: policy_and_safety
epistemic_status: verified_fact
entities:
  companies:
  - Apple
  - OpenAI
  - io Products
  technologies: []
  key_people:
  - Tang Tan
  - Chang Liu
  - Jony Ive
  - Evans Hankey
  - Scott Cannon
key_logic_flow:
- Apple 于 2026 年 7 月 10 日向美国加州北区联邦地区法院提起诉讼，指控 OpenAI、前产品设计副总裁 Tang Tan 和前高级工程师 Chang
  Liu 窃取商业机密。
- Apple 声称 Tan 在面试苹果员工时利用内部项目代号等机密信息套取情报，并直接要求候选人携带苹果硬件零部件和原型进行「展示」。
- Apple 指控 Liu 离职后利用安全漏洞下载超过一千页的机密工程文件，未归还公司配发笔记本电脑，还指导其他被招募者准备窃密。
- Apple 称 OpenAI 通过一家受信任的苹果合作伙伴非法实施苹果专有的金属表面处理工艺，并向另一家长期供应商进行针对性询问。
- Apple 表示早在 2026 年 2 月就向 OpenAI 提出关切但未获回应，目前已有超过 400 名前苹果员工在 OpenAI 工作。
extract_result: success
impact_score:
  score: 6.5
  reason: 本次诉讼是苹果与OpenAI之间直接的法律对抗，涉及AI行业核心的人才流动与商业机密保护问题。苹果提供了具体且细节丰富的指控——从面试中使用内部项目代号套取情报、要求候选人携带苹果硬件零部件进行'展示'，到前工程师利用安全漏洞下载超过一千页机密工程文件——这些行为模式若被法庭采信，将对OpenAI的硬件业务（由Jony
    Ive主导，估值65亿美元）构成实质性打击。超过400名前苹果员工在OpenAI工作的数字说明这不是孤立事件，而是系统性的人才与情报转移。然而，这本质上是一场商业诉讼，而非技术范式转变；行业影响主要局限在AI公司与Big
    Tech之间的人才竞业策略和法律风险规避，不会改变AI基础技术发展轨迹。综合考虑重要性和局限性，给予6.5分。
sentiment: negative
developer_sentiment:
  tone: frustrated
  primary_focus: 大型科技公司之间的商业机密诉讼对AI人才流动自由的寒蝉效应
hype_assessment:
  level: low
  reason: 本文是对已正式提交的法庭诉状的事实性报道，内容基于具体的法律文件（加州北区联邦地区法院），包含详细的时间线、人物、行为描述和直接引用的诉状原文。没有使用'颠覆'、'革命性'等PR话术，信息源可靠（9to5Mac直接引用了苹果官方声明和法庭文件），不存在概念炒作或水分包装。
information_entropy: high
domain_disruption:
  technical_innovation: 无。本案为商业机密法律纠纷，不涉及任何技术创新或技术突破。
  business_model: 此案可能重塑AI初创公司从大型科技企业组建硬件团队的策略：OpenAI通过收购Jony Ive的io公司（含50+工程师）快速搭建硬件团队的模式，将因面临商业机密诉讼风险而变得更具法律挑战性。AI公司的硬件业务人才招募流程——特别是面试环节对候选人过往工作细节的询问——可能被迫更加合规化和审慎，增加AI硬件创业的法律摩擦成本。
engineering_complexity: production_ready
compound_value:
  score: 6.0
  reason: 此事件的核心长期价值在于它对AI硬件竞争格局的信号效应和制度性影响。首先，Apple 的起诉直接针对 OpenAI 的硬件业务（由 Jony Ive
    领导的消费者 AI 设备），若诉讼成立，将迫使 OpenAI 在硬件研发上'隔离'来自 Apple 的技术信息，可能导致其硬件产品上市延迟 12-18 个月，为
    Apple 自身的 AI-on-device 战略争取窗口期。其次，更重要的是诉讼的震慑效应——它大幅提高了 AI 公司从硬件巨头挖角的人才流动成本和法律风险，未来
    AI 初创公司在招募 Apple、Samsung 等硬件企业核心工程师时将面临更严格的合规审查和诉讼可能性，这会系统性抑制'模型公司跨界做硬件'这一战略路径的有效性。第三，此案可能催生针对
    AI 领域人才流动和商业秘密保护的新判例，形成制度性壁垒。综合来看，虽非行业范式级事件，但对 AI 硬件竞争版图有中长期的实质性重塑作用。
value_capture_layer: hardware_compute
moat_impact: strengthens_monopoly
key_beneficiaries:
- Apple
- Google
- Samsung
- Meta
competitive_casualty:
- OpenAI
- io Products
- AI 硬件初创公司
market_opportunities:
- 企业内部威胁检测与数据防泄露（DLP）方案在 AI 行业将迎来爆发需求，特别是针对离职员工在面试期间的数据异常访问和批量下载行为的实时监控工具
- AI 行业人才竞业限制与商业秘密合规咨询将成为法律服务新蓝海，可帮助企业在招聘竞品员工时建立面试合规审查流程，防范间接窃密风险
- 面向科技企业的员工离职安全审计 SaaS 工具存在市场机会，覆盖设备追踪与回收、权限即时回收、离职前文件下载审计以及面试期间泄密风险管控
risk_matrix:
  regulatory: 本案可能推动美国各州和联邦层面加强对 AI 企业间人才流动中的商业秘密保护立法，OpenAI 面临禁令救济及巨额赔偿风险，若败诉可能直接影响其硬件业务线发展
  technological: 事件暴露了企业内部访问控制和安全架构的薄弱环节（前员工利用安全漏洞下载逾千页机密工程文件），提示所有 AI 和硬件企业需重新审视内部数据访问权限分级与审计体系
  competitive: 此诉讼将加剧科技巨头之间的'人才壁垒'，Apple 与 OpenAI 关系进一步恶化，可能限制未来双方在 AI 硬件、芯片等领域的合作空间，并形成更激烈的竞业对抗格局
  ethical: 案件揭示利用招聘流程系统性套取竞品机密的伦理问题，涉及面试中要求候选人携带竞品零部件'展示'、诱导准离职员工准备泄密材料等行为，引发 AI 行业招聘伦理的严肃反思
  additional: []
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: monitor
---

Apple has filed a lawsuit against OpenAI today, accusing the company of trade secret theft. Specifically, Apple alleges that its former employees have stolen trade secrets “for the benefit of OpenAI.”

“This case is about Apple’s former employees stealing Apple’s trade secrets for the benefit of OpenAI. Apple brings this suit to put a stop to it,” the lawsuit says.

## Apple statement

In a statement to *9to5Mac*, an Apple spokesperson said:

“At Apple, our teams are constantly developing breakthrough technologies to create the best products and services in the world, and protecting their work and intellectual property is something we take very seriously. Recently, significant evidence has emerged suggesting individuals employed by OpenAI wrongfully took Apple’s secret and confidential information regarding our unreleased technologies, processes, and products. We will always defend our teams’ hard work and innovations, and we are taking all appropriate steps to do so.”


Update: Read OpenAI’s response here.

**Apple accuses OpenAI of trade secret theft**

The lawsuit names Chang Liu and Tang Tan as two of the defendants. Tang Tan served as VP of product design at Apple, leading iPhone and Apple Watch product design. He departed the company in February 2024 to work with Jony Ive. Chang Liu, meanwhile, worked at Apple for eight years and was a senior system electrical engineer before departing to join OpenAI in January 2026.

Apple’s lawsuit also names OpenAI and io Products as defendants.

OpenAI’s hardware efforts are being led by Jony Ive, Apple’s former chief design officer. OpenAI acquired Ive’s startup io as part of a $6.5 billion deal last year. OpenAI’s takeover of the company included more than 50 engineers, developers, and other employees. In its original announcement, OpenAI touted that Ive founded io in collaboration with Scott Cannon, Evans Hankey, and Tan.

Hankey led Apple’s design team for several years after Ive departed the company. She departed in 2022 before reuniting with Ive as part of io. Cannon also previously worked at Apple.

Ive, Hankey, and Cannon are not personally mentioned anywhere in Apple’s initial filing today.

## The complaint

Apple says it first raised concerns with OpenAI directly in February, asking the company to investigate and address the issue. OpenAI, however, never responded. Apple says the conduct detailed in the filing is “the tip of the iceberg.”

This is the tip of the iceberg. Apple lacks visibility into what’s been happening behind closed doors at OpenAI, where such misconduct is normalized and exemplified by leadership. This much is clear, however: at every level, from members of its Technical Staff to its Chief Hardware Officer, and in coordination with business partners, OpenAI has been stealing Apple’s trade secrets and confidential information. As a natural result, OpenAI’s nascent hardware business now rests.


The complaint, filed in the U.S. District Court for the Northern District of California, alleges that Tan used insider knowledge of Apple’s confidential projects to grill job candidates in interviews and learn more confidential information. Additionally, Tan directed job candidates still working at Apple to bring actual Apple hardware components and samples for “show and tell” sessions.

When interviewing Apple employees for jobs at OpenAI, Mr. Tan uses Apple’s confidential information to gain access to even more insider knowledge. He has used an Apple internal project codename to ask, “What’s the plan[?]” for an unannounced Apple product.

He has directed job candidates still working for Apple to bring “Actual parts” from Apple to their interviews for “show and tell” sessions in which he and his team at OpenAI can elicit still more Apple confidential information. These directions to bring Apple’s parts to OpenAI job interviews surprised at least one of the candidates, who commented that he “didn’t even know we could take those from the office.”

OpenAI has been instructing Apple employees to bring “CAD/design artifacts” and “prototypes” to their interviews and to divulge details about their work such as “subsystem and component selection,” the “tools or methodologies you use for system integration, such as CAD software, simulation tools,” and “Vendor selection and communication/collaboration with vendors.”


Furthermore, Apple says a candidate began “screenshotting and downloading files relating to a highly confidential Apple project” hours before interviewing with Tan, who then “solicited more information about that same Apple project” once the interview started. This became an “established pattern,” Apple says.

Tan also allegedly possessed and distributed an internal Apple “Need to Know” document to new OpenAI hires before they gave their notice to Apple. The document included Apple’s departure security protocols. As part of its investigation, Apple found a “pattern by employees who depart for OpenAI of taking steps to evade the security processes intended to protect Apple’s confidential information.”

Meanwhile, Apple also claims former engineer Liu exploited a security bug to download confidential engineering files after leaving the company. Rather than report the exploit, Liu allegedly joked about it in messages (“LOL,” “so funny”). Liu also failed to return an Apple-issued laptop after his departure.

Apple alleges that Liu downloaded a “compilation of technical files with over a thousand pages” with details of work he did at Apple. This included detailed manufacturing documents covering the complex circuit boards used in Apple hardware products.

Liu also allegedly coached another Apple employee at the time, whom he was recruiting to OpenAI, on which confidential materials to study before her own OpenAI interview.

Finally, Apple alleges that OpenAI had a trusted Apple partner carry out Apple’s proprietary metal-finishing technique, misleading the partner into believing it had Apple’s permission to do so. Apple also says OpenAI approached a second longtime Apple supplier that works on power and battery manufacturing, using insider terminology to ask “targeted questions” about specific Apple components.

The suit seeks injunctive relief and damages, and comes as OpenAI works to bring its first consumer hardware device to market.

Apple’s lawsuit also comes after *Bloomberg* reported that OpenAI was preparing “legal action” against Apple over how its partnership to integrate ChatGPT into Siri played out. Today’s lawsuit from Apple, however, says that agreement is not at issue here.

Tan and Liu are just two of many Apple employees who have departed for OpenAI. Today’s filing says that there are over 400 former Apple employees now working at OpenAI.

There have been various rumors about OpenAI’s hardware efforts so far. In April, Ming-Chi Kuo reported that OpenAI is developing its own smartphone, which could launch in 2028. *The Information* has also reported on OpenAI’s work on a HomePod-style smart speaker.

You can read the full filing below and find the PDF linked here.

**Chance’s favorites: **

- Bring wireless CarPlay to any car
- “Apple: The First 50 Years” by David Pogue
- Logitech MX Master 4
- Belkin 3-in-1 MagSafe Charger
- Beats Woven USB-C Charging Cables
- AirPods Pro 3: $222 (Reg. $249)

**Follow Chance**: Threads, Bluesky, Instagram, and Mastodon.