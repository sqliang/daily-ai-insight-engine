---
title: I told them forced consent was unlawful. 5 years later it cost Elkjop €1.8M
source: https://www.thatprivacyguy.com/blog/elkjop-forced-consent-fine/
author:
- '[[speckx]]'
published: '2026-06-18'
created: '2026-06-19'
description: 'https://web.archive.org/web/20260618212028/https://www.thatp...https://archive.ph/I4zjA
  Comments URL: https://news.ycombinator.com/item?id=48589501 Points: 382 # Comments:
  219'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 9cb4bd1cbda992a1
source_type: community_discussion
tldr: 挪威Datatilsynet对Elkjop处以2000万克朗罚款，因其客户俱乐部强制同意营销属非法
objective_summary: 2021年7月，一位隐私专家向Elkjop投诉其客户俱乐部将接收营销与会员资格捆绑。该投诉经瑞典IMY转交挪威Datatilsynet，于2026年6月1日被处以2000万挪威克朗（约180万欧元）罚款，认定其同意机制违反GDPR多项条款。
event_type: policy_and_safety
epistemic_status: verified_fact
entities:
  companies:
  - Elkjop Nordic AS
  - Elgiganten
  - Datatilsynet
  - IMY
  - GDPRhub
  technologies: []
  key_people:
  - That Privacy Guy
key_logic_flow:
- 2021年7月，作者向Elkjop集团DPO投诉其客户俱乐部将取消营销邮件与取消会员资格捆绑，违反GDPR第21(2)条、第4(11)条和第7条关于自由同意权的规定。
- Elkjop书面回复确认接收营销/优惠是会员资格的条件，将合法的拒绝权变成了准入门槛，书面坐实了违规事实。
- 作者发出第18条限制处理请求和第15条主体访问请求，并向瑞典监管机构IMY提起正式投诉（案件编号DI-2021-6660）。
- 2022年9月，IMY根据GDPR一站式服务机制（第56(1)条）将案件移交挪威Datatilsynet，因实际控制者Elkjop Nordic AS主营业地位于挪威。
- 2026年6月1日，Datatilsynet对Elkjop集团处以2000万挪威克朗（约180万欧元）罚款，认定其同意无效（强迫、不具体、信息不充分），且未经第6(4)条兼容性评估擅自将数据用于广告和转化追踪。
- 作者通过志愿者运营的GDPRhub维基而非监管机构获知处罚结果，正追究IMY未履行第77(2)条告知义务的责任，并计划对Elkjop提起民事诉讼。
impact_score:
  score: 3.5
  reason: 该事件是挪威数据保护机构对零售企业捆绑营销同意的执法案例，罚款180万欧元，属于GDPR常规执法而非AI领域事件。对AI行业的间接影响在于：强化了'同意必须自由给予'的监管立场，这可能影响依赖用户数据做模型训练的企业（如将数据收集与使用服务捆绑的场景），但约束力有限，不构成行业范式变化。
sentiment: positive
developer_sentiment:
  tone: neutral
  primary_focus: GDPR自由同意原则对用户数据收集与AI训练数据合规路径的潜在影响
hype_assessment:
  level: low
  reason: 这是挪威Datatilsynet正式发布的执法决定（案件编号DI-2021-6660），有明确的处罚金额、法律依据和完整的事实链条。文章以当事人第一人称叙述，提供了投诉原文、监管机构移交过程等具体细节，不存在PR包装或概念炒作。
information_entropy: high
domain_disruption:
  technical_innovation: 无
  business_model: 捆绑同意模式被认定为违法——将营销同意设为会员资格的准入条件，违反GDPR第4(11)条和第7条关于自由同意权的规定。该判例将对Nordic乃至欧洲依赖此类捆绑同意机制的零售会员体系产生合规压力，需重新设计同意交互流程。
engineering_complexity: production_ready
compound_value:
  score: 5.5
  reason: 该判例本身非技术平台，不直接产生复利效应，但其监管信号价值不容低估。Datatilsynet明确认定'捆绑同意'、'强迫同意'和'加入即同意营销'在GDPR下违法，直接挑战了数字经济中最普遍的默认数据采集模式——包括Meta等巨头的'付费或同意'(pay-or-consent)模型。从VC视角看，这为隐私合规赛道创造了结构性需求增长：企业将被迫从'最低合规'转向'实质合规'，利好隐私工程、同意管理平台和隐私增强技术。但5年才落地暴露了监管效率瓶颈，且单一零售商罚款的威慑力有限，后续需要更多执法案例形成累积效应。因此评分中性偏正面——有长期行业重塑潜力，但需持续验证执法一致性。
value_capture_layer: end_application
moat_impact: creates_new_moat
key_beneficiaries:
- OneTrust
- Securiti
- BigID
- Transcend
- GDPRhub
- Apple
competitive_casualty:
- Meta (pay-or-consent model in EU)
- 依赖强迫同意模式的零售商与SaaS平台
- 传统数据经纪商
- 未合规的数字广告网络
market_opportunities:
- 合规咨询公司可针对客户忠诚度计划中的强制同意问题，推出专门的 GDPR 合规审计服务，帮助零售商避免类似罚款
- 创业团队可开发新一代同意管理平台（CMP），确保同意真正满足"自由给予、具体、知情"的 GDPR 标准，而非流于形式的弹窗工具
- 面向企业的隐私合规自动化工具可新增 6(4) 条兼容性评估模块，帮助企业在将数据用于广告追踪等二次用途前自动完成合法性评估
risk_matrix:
  regulatory: 该处罚明确了捆绑同意（forced consent）在 GDPR 下的违法性，是对"不同意就不可用服务"商业模式的直接打击。所有依赖客户俱乐部、会员制将营销同意与会员资格捆绑的企业均面临类似执法风险，且罚款金额参考此案例可能持续走高。AI
    企业若将模型训练数据收集与产品使用强行捆绑，同样面临此类合规风险。
  technological: 无
  competitive: 依赖强制同意获取营销数据的零售商在用户隐私意识提升和监管趋严的双重压力下将失去竞争优势；率先采用"自由同意"模式的企业可将其作为品牌信任的差异化卖点。
  ethical: 企业将消费者的法定拒绝权异化为付费会员的"入场券"，本质上是利用信息不对称和不平等议价地位剥夺用户自主选择权；此外，未经 6(4) 条兼容性评估将数据用于广告和转化追踪，反映了企业对用户数据用途不透明的系统性问题。
  additional:
  - 投诉人通过志愿者运营的 GDPRhub 维基而非监管机构获知处罚结果，暴露出 GDPR 一站式服务机制中监管机构对投诉人告知义务的履行严重缺失，可能触发欧盟侵权程序
confidence:
  impact: high
  compound: medium
  hype: low
actionable_insight: deep_dive
---

Back in the summer of 2021 I was a member of the Elgiganten Kundklubb, the customer club the Elkjop group runs across the Nordics, and like a lot of members I was buried under marketing emails. So I did the obvious thing and went looking for a way to switch them off. What I found instead was the problem that has taken five years to put right - the only way to stop the marketing was to cancel my membership of the club altogether.

I wrote to their Data Protection Officer on 30th July and set out, in plain terms, why that arrangement breaks the law. Under Article 21(2) of the GDPR every person has an absolute right to object to direct marketing. Under the ePrivacy Directive, marketing by email is only lawful where I have given my consent, or where there is an existing customer relationship and I am offered a simple way to opt out both at the point my details are collected and in every message after that. And consent, to be worth anything at all, has to be freely given - which under Article 4(11) and Article 7 means it cannot be bundled into, or made a condition of, something else. Forcing me to surrender my membership and the benefits that come with it, just to exercise a right I already hold, is the textbook example of consent that is not freely given.

## They put the violation in writing

The reply I received a few days later did me the favour of putting the violation on the record. Their position, in their own words, was that "in order to receive marketing / offers, it is a condition to be a member of the customer club." That one sentence is the whole case. They had taken a right I am entitled to exercise for free and turned it into the price of admission.

So I escalated. I served a formal restriction of processing under Article 18, I sent a full subject access request under Article 15 - the legal basis they were relying on, the legitimate interest balancing test, the recipients, the sub-processors, the international transfers, the profiling, all of it - and I filed a complaint with the Swedish supervisory authority, Integritetsskyddsmyndigheten (IMY), which issued the reference DI-2021-6660. The company's answer to all of this was to point me at a vague privacy policy, and then, when that did not wash, to stretch the deadline on my access request out to ninety days while citing "complexity" and "limited internal resources".

## How a Swedish complaint became a Norwegian fine

This is where the machinery of the GDPR comes in. The customer club is run by the Norwegian parent, Elkjop Nordic AS, and on the facts it is the parent that holds the real decision making power over the purposes and the means of the processing. So in September 2022 IMY decided it was not the right authority to deal with this at all. Under the one-stop-shop in Article 56(1), the competent regulator is the one for the controller's main establishment, and that establishment sits in Norway. IMY handed the investigation and my complaint to Datatilsynet, the Norwegian DPA, which accepted the case. And then, as these things tend to, it went quiet for a very long time.

On 1 June 2026 it stopped being quiet. Datatilsynet fined the Elkjop group NOK 20 million, a little over €1.8 million, and it found precisely what I had told them in 2021. The consent the company was relying on for its customer club was not valid - it was forced, it was not specific, and members were not properly informed. On top of that, the company had taken the personal data it gathered through the club and put it to further use for advertising and conversion tracking, without ever carrying out the compatibility assessment that Article 6(4) demands before you repurpose people's data like that. The decision runs through Articles 4(11), 5(1)(a), 5(2), 6(1)(a), 6(1)(f) and 6(4) - the lawfulness, the fairness, the transparency and the accountability of the entire arrangement.

I want to be clear about why this matters well beyond one retailer and one fine. Forced consent, pay-or-consent, bundled consent, the whole "agree to everything or you cannot use the service" model - it is everywhere, and it is the default way an enormous part of the digital economy operates. It is also unlawful, for the same simple reason every single time - if you cannot say no without losing something you are entitled to keep, you have not freely consented to anything. Five years and a seven figure fine later, that point is now sitting in a published decision for anyone to read.

## I had to read about it on a wiki

And yet there is a part of this story I am not willing to let slide, because it is its own small scandal.

I did not find out about this decision from IMY. I did not find out from Datatilsynet. I found out from GDPRhub, a volunteer-run wiki, on a random Thursday morning, nearly five years after I filed my complaint and well after the decision had already been made.

Under Article 77(2) of the GDPR a supervisory authority is under a binding legal obligation to keep a complainant informed of the progress and the outcome of their complaint. It is not a courtesy and it is not discretionary - it is written into the law. I filed my complaint with IMY, IMY passed it on, the case ended in a multi-million euro enforcement action, and not one of the authorities involved thought to tell the person who started it.

So this morning I wrote to IMY and asked them, in writing, to explain themselves. I have given them five working days. If the answer is what I suspect it will be, I will be filing under the European Union's infringement procedure, because a supervisory authority that cannot meet its most basic obligation to the people it exists to protect is exactly the sort of thing the Commission is supposed to look at. I have walked the Commission down this road before, over Phorm and the United Kingdom's failure to properly implement the EU rules on the confidentiality of communications, and I am entirely willing to do it again.

I have been saying for years that privacy is personal, and I mean it in the most literal way I can. This was my club membership, my inbox, my data and my complaint. The law was on my side in 2021 and it is on my side now. The company that told me to leave or put up with it has paid for that choice.

The only things still outstanding are an explanation from the Regulator that was meant to have my back the whole way through and civil litigation against Elkjop group now that the regulatory process has run its course - a litigation that is going to be so much more extensive now we have further details of further illegal processing of that personal data.

If they had listened to me in 2021, they would have avoided the fine, they would have made their processing lawful, they would have avoided the brand damage and the resulting litigation.

When I write to you as DPO with a complaint, it would be wise for you to take note. I am not a layperson, I am an expert on this law that I helped to create and I do not stop just because these actions are inconvenient, it is my life's work. Pay attention, when I write to you I am giving you free advice and you should treat as such instead of getting defensive and refusing to change.