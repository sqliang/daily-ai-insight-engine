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
tldr: 2021年，一位隐私专家投诉Elkjop集团将营销邮件同意与顾客俱乐部会员资格捆绑，违反GDPR关于自由同意的规定。2026年6月，挪威数据保护机构Datatilsynet对Elkjop处以2000万挪威克朗（约180万欧元）罚款，认定其强制同意安排违法。
objective_summary: 2021年7月，隐私专家The Privacy Guy向Elkjop集团数据保护官投诉，指出该集团将接收营销邮件作为顾客俱乐部会员的强制条件，违反GDPR第4(11)条和第7条关于自由同意的规定。投诉经瑞典监管机构IMY于2022年9月依据一站式机制移交至挪威Datatilsynet。2026年6月1日，Datatilsynet对Elkjop
  Nordic AS处以2000万挪威克朗罚款，认定其顾客俱乐部的同意机制为强制同意、不具体且信息不充分，同时该公司未按第6(4)条进行兼容性评估即将数据用于广告和转化追踪。原作者从GDPRhub维基偶然获知裁决结果，未收到任何监管机构通知，已要求IMY作出解释。
event_type: policy_and_safety
epistemic_status: verified_fact
entities:
  companies:
  - Elkjop Nordic AS
  - Integritetsskyddsmyndigheten (IMY)
  - Datatilsynet
  technologies:
  - GDPR
  - ePrivacy Directive
  key_people: []
key_logic_flow:
- 2021年7月，一位隐私专家发现Elkjop集团将取消营销邮件的唯一方式是取消顾客俱乐部会员资格，即营销同意与会员身份强制捆绑。
- 该专家向Elkjop数据保护官及瑞典监管机构IMY提出正式投诉，指出这种强制同意安排违反GDPR第4(11)条和第7条关于自由同意的规定。
- IMY于2022年9月依据GDPR第56(1)条一站式机制将案件移交至挪威Datatilsynet，因Elkjop Nordic AS的决策机构位于挪威。
- 2026年6月1日，Datatilsynet对Elkjop集团处以2000万挪威克朗（约180万欧元）罚款，认定其强制同意、同意不具体及信息不充分等多项违规。
- Datatilsynet同时认定该公司未按GDPR第6(4)条进行兼容性评估，即将会员数据用于广告和转化追踪。
- 原作者从社区运营的GDPRhub维基偶然获知裁决结果，未收到任何监管机构的主动通知，已要求IMY作出解释并可能启动欧盟侵权诉讼。
extract_result: success
object_mentions:
- object_type: project
  name: GDPRhub
  canonical_name: GDPRhub
  url: https://gdprhub.eu
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 原作者从GDPRhub（一个由志愿者运营的维基平台）偶然获知本案的裁决结果，而非从负责案件的监管机构直接得知。
  - GDPRhub被描述为志愿者运营的维基平台，专门收录GDPR执法案例和隐私监管决策的公开信息。
  article_id: 9cb4bd1cbda992a1
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