---
title: Lawmakers added $1 to car insurance policies. That money paid for Flock cameras
source: https://www.texastribune.org/2026/08/28/texas-flock-cameras-auto-insurance-fee-mvcpa-grants/
author:
- '[[DeepLogin]]'
published: '2026-08-29'
created: '2026-08-30'
manifest_dates:
- '2026-08-30'
description: 'Article URL: https://www.texastribune.org/2026/08/28/texas-flock-cameras-auto-insurance-fee-mvcpa-grants/
  Comments URL: https://news.ycombinator.com/item?id=49494182 Points: 295 # Comments:
  168'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: f74cafbb38d402aa
source_type: community_discussion
tldr: 德克萨斯州2023年为打击催化转换器盗窃而加的1美元汽车保险费，被用于大规模采购Flock车牌识别摄像头，至少3200台设备获得州资金支持。调查报道发布后，州长Abbott宣布暂停州级资金用于Flock摄像头，多名立法者表示对此不知情。
objective_summary: 2023年德克萨斯州立法机关一致通过法案，将汽车保险费提高1美元以打击催化转换器盗窃。德州论坛报调查发现，汽车犯罪预防管理局(MVCPA)将这笔费用中的至少3000万美元用于资助至少3200台Flock车牌识别摄像头，覆盖全州高速公路与街道。报道发布后，州长Greg
  Abbott办公室宣布暂停州级拨款用于Flock摄像头。该费用共筹得约8100万美元，其中5080万美元投入234笔拨款，涵盖警员、犯罪分析师、无人机及监控设备等用途。
event_type: policy_and_safety
epistemic_status: verified_fact
entities:
  companies:
  - Flock Safety
  - Texas Tribune
  - Texas Department of Public Safety
  - Motor Vehicle Crime Prevention Authority
  - DeFlock
  technologies:
  - LPR
  - AI
  - Vehicle Fingerprint
  key_people:
  - Greg Abbott
  - Miguel Rodriguez
  - Carol Alvarado
  - Jeff Leach
  - Brian Harrison
  - Mitch Little
  - Trevor Chandler
  - Kenneth Feagins
key_logic_flow:
- 2023年德克萨斯州立法机关一致通过以哈里斯县副警长Darren Almendarez命名的法案，在汽车保险费上增加1美元用于打击催化转换器盗窃，法案未提及车牌读取器。
- 汽车犯罪预防管理局将至少3000万美元投入Flock监控网络，通过95笔拨款资助约2000台摄像头，另拨1590万美元为DPS增设近1200台，合计至少3200台设备。
- 德州论坛报调查报道发布后，州长Greg Abbott办公室宣布暂停州级资金用于地方Flock摄像头拨款，并称相关州机构正澄清资金不得用于Flock摄像头。
- Flock摄像头利用人工智能生成车辆指纹，存储车牌、品牌、型号与颜色等细节，全国约7000个执法机构使用12万台设备，无需搜查令即可跨州检索数据。
- 2025年车牌读取器数据被搜索62000次，破获约1660起催化转换器盗窃案，但警察滥用数据事件频发，一名Lufkin警察因100项滥用官方信息罪名被起诉。
object_mentions:
- object_type: product
  name: Flock Cameras
  canonical_name: Flock Safety
  url: https://www.flocksafety.com
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Flock摄像头是美国使用最普遍的车牌读取器，利用人工智能生成车辆指纹，在无需搜查令的情况下供全国执法机构查询车辆数据。
  - 汽车犯罪预防管理局已将保险附加费中的至少3000万美元用于在全州布设至少3200台Flock摄像头，从El Paso一直延伸到路易斯安那州边境。
  article_id: f74cafbb38d402aa
- object_type: project
  name: DeFlock
  canonical_name: DeFlock
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - DeFlock是反监控监督组织，利用经核实的众包方式绘制了德州约13000台Flock摄像头的位置，据此估计保险附加费支付了德州四分之一摄像头的费用。
  article_id: f74cafbb38d402aa
- object_type: project
  name: DFW DeFlock
  canonical_name: DFW DeFlock
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - DFW DeFlock组织者Kenneth Feagins称看到警察不当访问Flock网络的警报性趋势，该网络可累积人们居住、购物、礼拜和工作地点的数据。
  article_id: f74cafbb38d402aa
extract_result: success
impact_score:
  score: 5.5
  reason: 这是针对 AI 监控产业的调查性政策报道，而非技术范式突破。短期冲击集中在 GovTech 监控细分赛道：州长暂停州级拨款直接威胁 Flock
    Safety 在其第二大市场（德州）的扩张，且立法者'不知情'的表态可能引发其他州对同类隐性拨款通道的审计，抬高监控类 AI 政府采购的合规成本。但核心技术成熟且未发生改变，影响以区域政策面为主，尚未波及全国性行业格局，故评为中等偏上冲击。
sentiment: mixed
developer_sentiment:
  tone: skeptical
  primary_focus: 无搜查令的跨州车牌数据共享与 AI 车辆指纹识别带来的隐私边界问题
hype_assessment:
  level: low
  reason: 该报道基于拨款记录、会议纪要及 101 个市县议会公开文件的交叉核验，具体数字（3200 台摄像头、8100 万美元费用、62000 次数据检索、100
    项滥用指控）均可追溯，通篇未使用'颠覆'、'革命性'等营销词汇，属于扎实的实证调查而非概念炒作。
information_entropy: high
domain_disruption:
  technical_innovation: Flock 的车辆指纹（vehicle fingerprint）AI 是技术核心：在车牌识别之外，通过 AI 聚合品牌、型号、颜色、凹陷、保险杠贴纸等视觉特征构建跨州可检索的车辆身份库。其创新不在单点算法，而在'大规模分布式摄像头网络
    + 无搜查令跨机构数据共享'的工程架构，该报道揭示这一架构在公共资金资助下无监督扩张的真实规模。
  business_model: 以'打击车辆犯罪'为名的汽车保险附加费成为政府为私人监控企业买单的隐性财政通道——至少 3000 万美元经州拨款流向 Flock
    摄像头。州长暂停拨款的决定直接冲击 GovTech 监控厂商'公共拨款采购 + 订阅制服务'的商业模式，并可能促使其他州审计同类资金通道，提高监控类 AI
    政府采购的合规审查成本。
engineering_complexity: infrastructure
compound_value:
  score: 6.5
  reason: 投资逻辑拆解：①复利机制真实存在——Flock全国约120,000台设备、约7,000个执法机构接入，每新增一台摄像头都放大跨州数据检索的网络价值，'车辆指纹'数据库的长期积累形成高转换成本，执法流程一旦深度依赖便难以迁移，这是典型的'数据越用越值钱'复利结构；②需求端付费意愿得到验证——德州设备3年内从约7,500台增至约13,000台，其中约1/4由本事件所述公共资金支付，说明公共安全AI监控是刚需赛道，且Flock已占据LPR绝对主导地位；③但风险面显著——本次事件暴露其增长高度依赖单一公共资金渠道（州长叫停后约1/4德州设备的采购模式受阻），立法者'不知情'表明存在系统性政策尾部风险，隐私诉讼与第四修正案挑战将压制未来扩张速度；④综合判断，Flock作为执法监控细分赛道基础设施的地位已确立，3-5年后大概率仍是行业基石，但政策不确定性压制估值上限，故给6.5分而非更高。
value_capture_layer: end_application
moat_impact: creates_new_moat
key_beneficiaries:
- Flock Safety
- 德州公共安全部（DPS）
- 联邦执法科技供应商
competitive_casualty:
- 小型车牌识别（LPR）初创公司
- 传统安防监控硬件厂商
- 依赖州级拨款的德州地方警察局
market_opportunities:
- 面向智能监控领域，可布局基于边缘计算与数据最小化的隐私合规型车牌识别方案，在监管趋严背景下抢占对第四修正案敏感客户的替代市场
- 可面向公民监督组织与地方政府开发政务AI支出透明度工具（对标DeFlock），提供专项资金流向追踪、监控摄像头选址测绘与FOIA自动化申请的SaaS/众包平台
- 随着无搜查令跨机构数据共享面临法律挑战，可针对执法机构推出AI监控数据合规审计与治理咨询服务（数据留存、访问权限、共享边界）
risk_matrix:
  regulatory: 高。该事件已直接触发州长叫停州级资金、立法者公开表示事先不知情，预示针对LPR/AI车牌识别技术的州级立法限制与第四修正案诉讼将增多；联邦层面的监控数据监管也可能加强，欧盟AI
    Act对生物识别监控的限制可作为参照。
  technological: 中。车辆指纹识别技术成熟但可替代性增强，牌照伪造、对抗攻击与数据投毒可削弱其有效性；若监管收紧，集中式云端数据库方案可能被边缘端或去中心化方案替代。
  competitive: 中。Flock在LPR市场的主导地位面临监管与舆论双重挤压，地方政府暂停采购、隐私合规型竞品入场，将重塑监控硬件与数据服务市场格局。
  ethical: 高。无搜查令即可跨州共享车辆行踪数据构成大规模监控，存在警察滥用数据（如Lufkin警察事件）、对少数族裔社区不成比例的监控影响，以及将'打击催化转换器盗窃'专项费用挪用于全州监控网络的使命漂移问题。
  additional:
  - 专项资金挪用与财政透明度风险：保险费专项收入被用于监控网络引发公众信任危机，可能触发审计与问责
  - 集中化车辆行踪数据库成为黑客与内鬼的高价值攻击目标，存在大规模隐私数据泄露的潜在风险
confidence:
  impact: high
  compound: medium
  hype: high
actionable_insight: deep_dive
object_insights:
- object_type: product
  name: Flock Cameras
  canonical_name: Flock Safety
  url: https://www.flocksafety.com
  positioning: 美国最普及的车牌识别摄像头产品，以AI生成车辆指纹并通过全国执法网络共享数据，正因州资金介入而深陷监控扩张争议。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 各地执法机构与警察局
  - 德州公共安全部（DPS）等州级部门
  product_signal: 利用人工智能生成车辆指纹，存储车牌、品牌、型号、颜色及凹痕贴纸等细节，全国约7000个执法机构可免搜查令跨州检索数据。
  market_signal: 全国约7000个执法机构使用12万台设备，德州约13000台位居全美第二，仅2025年数据即被搜索62000次并破获约1660起催化转换器盗窃案。
  differentiation: 作为全美使用最普遍的车牌读取器，其无需搜查令即可跨辖区共享数据的模式，显著区别于传统仅供本地使用的车牌读取设备。
  watch_reason: Flock摄像头深度卷入德州用汽车保险附加费大规模采购的争议，州长已暂停州级资金支持，且立法者自认对资金用途不知情，其监控扩张、隐私与数据滥用风险将持续发酵，值得跟踪后续监管走向。
  risk_notes:
  - 州长已宣布暂停州级资金用于地方Flock摄像头拨款，资金来源与合法性面临重大不确定性。
  - 警察滥用数据事件频发，一名Lufkin警察因100项滥用官方信息罪名被起诉，隐私风险突出。
  - 立法者表示通过法案时从未讨论监控摄像头，资金用途偏离立法初衷，可能引发立法审查。
  - 124笔拨款缺乏清晰的公开采购记录，实际摄像头数量可能高于已披露的3200台。
  score: 9.0
  article_ids:
  - f74cafbb38d402aa
  evidence_snippets:
  - Flock摄像头是美国使用最普遍的车牌读取器，利用人工智能生成车辆指纹，在无需搜查令的情况下供全国执法机构查询车辆数据。
  - 汽车犯罪预防管理局已将保险附加费中的至少3000万美元用于在全州布设至少3200台Flock摄像头，从El Paso一直延伸到路易斯安那州边境。
- object_type: project
  name: DeFlock
  canonical_name: DeFlock
  url: null
  positioning: 反监控监督组织，以经核实的众包方式绘制Flock摄像头分布地图，为公众与媒体提供监控覆盖的关键事实依据。
  technical_signal: 采用经核实的众包方法定位约13000台Flock摄像头，其测绘能力成为估算德州监控规模的重要数据来源。
  adoption_signal: 德州论坛报调查依赖其地图估算保险附加费支付了德州四分之一摄像头的费用，数据被主流媒体采用并影响州长决策。
  ecosystem_relevance: 在监控扩张与隐私争议中充当独立制衡力量，其数据直接支撑立法者与媒体对Flock网络的监督与问责。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: 区别于政府与厂商口径，以第三方众包核实方式独立测绘监控覆盖，提供无法从官方渠道获得的透明数据。
  watch_reason: DeFlock的反监控测绘数据持续揭示Flock在德州的真实覆盖规模，随着州资金争议发酵，其地图与估算将成为衡量政策影响和监控扩张的关键第三方证据。
  risk_notes:
  - 其规模估算基于众包核实，实际摄像头数量仍无法精确验证，数据可能存在覆盖盲区。
  - 作为非官方监督组织，其统计口径与政府或厂商数据存在差异，引用时需注意估算性质。
  score: 6.0
  article_ids:
  - f74cafbb38d402aa
  evidence_snippets:
  - DeFlock是反监控监督组织，利用经核实的众包方式绘制了德州约13000台Flock摄像头的位置，据此估计保险附加费支付了德州四分之一摄像头的费用。
- object_type: project
  name: DFW DeFlock
  canonical_name: DFW DeFlock
  url: null
  positioning: 德克萨斯州达拉斯-沃斯堡地区的反监控基层组织，关注警察对Flock车牌识别网络的不当访问问题。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: 作为本地反监控力量，代表社区对Flock网络数据累积与警察滥用风险的直接关切，补充州级监督视角。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: DFW DeFlock的基层观察持续记录警察不当访问Flock网络的趋势，其反馈可能是衡量数据滥用程度与推动隐私整改的早期信号，值得跟踪其在德州反监控运动中的作用。
  risk_notes:
  - 组织信息仅来源于一位组织者的表述，缺乏公开可验证的量化证据，观察结论有待进一步证实。
  - 作为区域性基层组织的公开活动有限，其影响力与数据的系统性存在不确定性。
  score: 4.0
  article_ids:
  - f74cafbb38d402aa
  evidence_snippets:
  - DFW DeFlock组织者Kenneth Feagins称看到警察不当访问Flock网络的警报性趋势，该网络可累积人们居住、购物、礼拜和工作地点的数据。
---

In 2023, the Texas Legislature unanimously passed a law raising auto insurance costs for Texans by $1 to combat rampant catalytic converter theft.


Three years later, a little-known state agency has devoted at least $30 million of that fee toward supercharging the state’s Flock surveillance network, placing cameras along highways and streets from El Paso to the Louisiana border,** **an analysis by The Texas Tribune found.

The Motor Vehicle Crime Prevention Authority, led by a board mostly appointed by Gov. Greg Abbott, has turned the $1 fee hike into at least 3,200 Flock cameras.

The agency has awarded no fewer than 95 grants to help law enforcement agencies purchase and maintain about 2,000 Flock cameras. Another $15.9 million is helping the Texas Department of Public Safety add almost 1,200 more.


The effort is far from over. In early August, the agency approved another $3 million to help DPS install 583 more cameras along Texas tollways over the next year.

Miguel Rodriguez, chair of the Motor Vehicle Crime Prevention Authority, said during an August 2023 meeting that he hoped to use proceeds from the fee increase to “cover the entire state” with cameras.

Rodriguez, who is also the Laredo Police Chief, sees the cameras as a powerful law enforcement tool, particularly to combat criminal organizations.

“That kind of capability directly disrupts the operational advantage these transnational criminal organizations rely on, and it strengthens our ability to protect both Texas communitiesand the broader region,” he said in an email.

But on Friday evening, after multiple requests for comment from the Tribune about its findings, Abbott’s office said the governor was pausing all state funding for local grants to be used for Flock cameras.

“To the extent that cities get any funding for those cameras, most of it comes from the federal government. To the extent any funding comes from Texas agencies, those agencies are clarifying that those funds cannot be used for Flock cameras,” Abbott spokesperson Andrew Mahaleris said in a statement shared first with the Tribune.

The $1 per year fee increase has raised an estimated $81 million, allowing the authority to funnel $50.8 million into 234 grants that have helped reimburse police departments for officers, crime analysts and attorneys to prosecute vehicular crimes, as well as drones and other surveillance devices.

The Tribune found agency grants to police departments ranged from $7,000 for two Flock cameras in Bellmead, near Waco, to almost $1.7 million for 201 cameras in Dallas. Some city networks — like the 165 cameras in Laredo and 150 in El Paso — were entirely subsidized by the grants.

The state agency does not detail how much of its grant money went to Flock cameras. Instead, the Tribune tracked the grants by reviewing the vehicle authority’s meeting records, as well as documents, agendas and discussions from 101 city councils and county commissions that approved or discussed Flock-related grants.

It is likely the authority has paid for more Flock cameras than the Tribune analysis found because 124 grants lack clear public documentation about what was purchased.


The statewide effort to proliferate Flock cameras comes as backlash is mounting over the surveillance, including from some members of the Legislature, where the $1 fee was approved without opposition.

“The sheer volume of information captured is not something that is entertained, in my view, by the Fourth Amendment,” said Rep. Mitch Little, R-Lewisville.

State Sen. Carol Alvarado and Rep. Jeff Leach, the bill’s author and House sponsor, said surveillance cameras were never discussed when the bill was considered. Alvarado said she was surprised to learn from the Tribune that the insurance fee was funding AI-supported license plate readers.

“I did not have that in mind when we passed the bill,” said Alvarado, D-Houston. “When I think of combating crime, I’m thinking … more boots on the ground, hiring more officers to tackle the crime or some type of undercover work.”


Alvarado said there is a “fine line” between protecting the public from crime and protecting people’s privacy, but said she did not plan to file legislation to shift the grant requirements.


Flock cameras, the nation’s most commonly used license plate reader, create a “vehicle fingerprint” with the use of artificial intelligence — storing each vehicle’s license plate, make, model, color and details such as dents and bumper stickers in a database accessible by law enforcement across the country without having to obtain a search warrant.

The exact number of Flock cameras in Texas is unclear. DeFlock, an anti-surveillance watchdog that has mapped the locations of Flock cameras using verified crowdsourcing, has identified about 13,000 in the state. By that count, the insurance fee increase has paid for one in four Texas cameras.

That also represents a sharp increase in Flock cameras in the state since December 2023, when a company spokesperson told the vehicle authority’s board that there were about 7,500 cameras in the state.

Flock does not disclose how many cameras it has in the field, but Texas is estimated to have the second most in the nation, after California. Nationally, Flock officials say, about 7,000 law enforcement agencies use a total of 120,000 cameras and other surveillance products.

In Texas, state agencies don’t rely solely on vehicle authority grants to add surveillance devices, and Abbott’s office pointed to federal grants for funding the cameras. DPS, for example, has a $28.5 million contract for Flock cameras. But the grants have helped get the cameras into the hands of the state’s smaller police departments that may have struggled with the cost of the equipment.

Departments that opt in to Flock’s national lookup program can search each other’s data from anywhere in the country, allowing vehicles to be tracked with unprecedented efficiency.

The ability to share data “has been one of the most effective ways Flock has been able to help find, just last year, over 10,000 missing persons,” Flock spokesperson Trevor Chandler said in an interview.

But for a rapidly growing coalition of Texans opposed to the cameras, the Flock network is a dangerous combination of invasive surveillance and limited oversight that undermines privacy rights.

Kenneth Feagins, an organizer with DFW DeFlock, one of several new grassroots anti-surveillance groups in the state, said he sees an “alarming trend” of police improperly accessing a network that can amass data on where people live, shop, worship and work.

“For me, it’s always been the question of, well, how much liberty are we willing to trade for safety?” Feagins said.

Recently revealed examples of misuse — including police officers using Flock data to stalk ex-partners and co-workers — have sharpened those concerns.

A Lufkin officer was indicted Aug. 24 on 100 counts of misusing official information, which Abbott cited as a concerning development during a Friday radio interview. Officers in Baytown, Harris County, Fort Bend County, Temple and Pasadena also have been arrested, disciplined or investigated.

“There’s a lot of malicious things that can be done with this data, and those things are no longer hypothetical,” Feagins said.

## Cameras “changed the game” for police

The Motor Vehicle Crime Prevention Authority was established by the Legislature in 1991 to combat automobile theft.

The authority is led by a DPS official and six governor-appointed board members — two from law enforcement, two from the insurance industry and two consumer representatives.

The vehicle authority primarily flexes its muscle via grants funded by fees added to annual auto insurance premiums — $1 initially, rising to $2 in 2011 and $4 in 2019 — that largely went to fund task force efforts for police departments.

In 2023, with catalytic converter theft spiking across Texas, lawmakers approved adding another $1 to the insurance fee in a bill named for Harris County Deputy Darren Almendarez, who was shot to death after interrupting catalytic converter thieves in a grocery store parking lot.

The legislation made no reference to license plate readers, and Rep. Brian Harrison, who voted for the bill, said he wasn’t aware of any conversations about using the fee increase that way. The Midlothian Republican filed bills that year and in 2025 to require a warrant before police could access license plate reader data.

“In a million years, I never could have even contemplated that this would be used to fund what is effectively warrantless surveillance,” Harrison said. “Otherwise, I can’t imagine it would have gotten unanimous support. I sure as hell wouldn’t have voted for it if I knew some bureaucrat was going to redirect the money to Flock cameras.”

Anticipating millions from the $1 insurance fee hike, the vehicle authority in 2023 asked law enforcement for advice on how best to spend the money. Automatic license plate readers like Flock cameras were by far the top choice for combatting catalytic converter theft, beating out overtime for investigators and additional training.

The cameras, Rodriguez said, are particularly helpful for addressing catalytic converter theft, a “mobile, high-volume, low-witness crime” where the vehicle used is often the only lead.

Without technological help, departments were left working with partial descriptions taken from grainy surveillance footage of suspect vehicles, Rodriguez said.

Data from the license plate readers, known in law enforcement as LPRs, was searched 62,000 times in 2025, leading to about 1,660 cleared catalytic converter theft cases, a report from the authority said.

Pasadena Police Sgt. Douglas Buckert said the cameras “changed the game” for catalytic converter theft investigations.

“The number of leads we’ve gotten since our department has deployed Flock cameras is outrageous,” Buckert told the authority in early 2024. “I could have six more investigators and not get it all done.”

Grant-funded cameras, much more than other technology, have also expanded the reach of police in investigations far beyond catalytic converter cases, department officials say.

Dallas Police Sgt. Bryan Roden told board members during a January meeting that an authority grant let his department increase its network from 100 to 300 cameras, helping to bust a million-dollar tire theft ring and solve a hit and run. Working with the Department of Homeland Security, Dallas police located a fugitive wanted for cocaine manufacturing by using Flock cameras he regularly passed to build a “pattern of life assessment,” Roden said.

Temple Police crime analyst Mike Treehern told the Tribune that the cameras helped decrease the number of stolen vehicles in his city, where 84% of their Flock cameras are funded by the state grant.

“It’s absolutely helped us, and we would not have anywhere near the amount of cameras that we do without [vehicle authority] funds,” Treehern said.

The grant has also been a force multiplier for smaller departments. In Cibolo, a city north of San Antonio with a population of 36,000, an authority grant multiplied the number of Flock cameras from 11 to 52.

“Honestly, a lot of our surrounding communities started looking at them, specifically through the [Motor Vehicle Crime Prevention Authority],” Cibolo Police Lt. John Wells told board members in a January meeting. “Seguin was looking at them, Guadalupe County, the New Braunfels Police Department, all of our neighbors, so we started looking as well.”

Hannah Foust, founder of DeFlock Carrollton, said the cameras give police surveillance power well in excess of what’s needed to stop car thieves.

“I do think that motor vehicle theft is a concern, it’s an issue,” Foust said. “[But] I do think that this grant program, and the way it’s been used … it really shifts the focus to a broader surveillance program, as opposed to focusing on catalytic converter prevention.”

### $1 fee hike helped DPS expand its Flock network

The authority’s most significant investment in Flock came in 2025 when it signed a three-year, $15.9 million contract with DPS to install 1,183 cameras in a project largely overseen by DPS Major Sharon Jones, the board’s self-described “pro Flock” member who left the position Aug. 1.


The contract aims to bolster DPS’ network of cameras and make it accessible to local law enforcement agencies in places that otherwise could not be easily reached — including local municipalities that are resistant to the surveillance.

Patrick McBroom, police commander for the Panhandle Auto Burglary and Theft Unit, said DPS cameras help his task force monitor interstate traffic at the Oklahoma and New Mexico borders — areas of Texas beyond the view of 138 grant-funded cameras his team monitors.

“All those roads leading out and into Texas have DPS cameras on them, so if we have stolen items that may be going out of state, we’re able to look at those cameras to see if those vehicles have left the state,” McBroom said.

During an April conversation about the DPS contract, Rodriguez noted the state police force’s cameras could improve surveillance in areas where locals are unwilling to install their own cameras. A growing number of cities and counties, including Austin, have canceled their Flock contracts in the face of residents’ privacy concerns.

“I think that if for whatever reason you are within those jurisdictions that do not want Flock, let’s get together with DPS, [so] that, you know, we can put those in state right-of-way. And there’s nothing that they can tell us,” Rodriguez said to Jones.

Rodriguez told the Tribune that the DPS network provides a needed crime-fighting tool in areas** **hostile to Flock cameras and similar devices.

Almost 100 municipalities in the U.S. have ended their Flock contracts in response to public outcry, including several in Texas, such as Bandera and Hood County. Both had received grants for their cameras but ended their contracts after issues with Flock installation and in response to public uproar over their use.

As criticism over the cameras has exploded — including devices that were cut down or vandalized as acts of protest — agency board members have expressed frustration at what they see as misinformation that clouds the positive impact from the cameras.

“We’ll have a larger conversation regarding the need to educate the public, and we must put a stamp on those who are spreading false information on license plate readers,” Jones said in a July grant meeting.

### “A concern for our privacy”

Foust started Carrollton’s DeFlock group after her neighbors expressed frustration at the cameras’ rapid spread. Spotting a camera along the route her children walk to school gave her pause; seeing one go up in front of her community recreation center made her act.

“You can’t enter or exit that complex without passing a Flock camera, and that’s also my polling place, so that really gave me a strong reaction,” Foust said. “They were in places that we normally feel very safe at, and there’s no concerns for our safety, for our children’s well-being, but there suddenly was a concern for our privacy.”

Foust is open to discuss a variety of solutions to her concerns, including action by the Texas Legislature, but said the first step is getting city officials to be transparent about their use.

“I think before we can have a true and honest conversation about what legislation might look like or what guardrails or safeguards could be put in place, I think we need to start on a level playing field of understanding,” Foust said. “What is the system, what is it capable of, and how could it be set up in a way that’s supposedly safe?”

Harrison and Little said they intend to file bills next legislative session banning the devices because they believe the cameras violate the Fourth Amendment’s protection against unreasonable searches. Little said he’s particularly concerned about whether vast amounts of personal data is securely stored and whether Flock, a private company, should be able to access it.

“The people in Lewisville, Texas have a reasonable expectation of privacy from police officers in Pampa, Texas, and yet they can observe all that data,” Little said. “So the sharing of it across state lines, across jurisdictional lines, to me is highly problematic.”

Harrison said he was “shocked and dismayed” that so few Republicans had spoken out against Flock cameras and what he calls blatant constitutional violations. He also said state officials should take more immediate action to “shut off” Flock grants because legislators never intended to use the insurance fee increase for cameras.

“I think the Legislature shouldn’t take this sitting down. I think the governor should act on this,” Harrison said. “If that’s happening, what that means is there’s clearly no explicit legislative intent or direction for that to be happening.”