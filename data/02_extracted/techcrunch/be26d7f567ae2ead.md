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
tldr: AWS正在洽谈向其他公司出售自研AI芯片Trainium，以更直接地挑战英伟达。CEO Andy Jassy在股东信中称，若芯片业务独立运营并向第三方销售，年收入运行率可达约500亿美元。当前Trainium及下一代Trainium4产能均已售罄。
objective_summary: Amazon AI负责人Peter DeSantis向彭博社透露，AWS正在与多家公司洽谈出售其AI芯片Trainium用于数据中心部署。该计划源于CEO
  Andy Jassy在4月股东信中的表态，他称自研芯片需求旺盛，若作为独立业务对外销售，年收入运行率约500亿美元。AWS此前因云服务瀑布效应收益而抵制直接出售芯片，当前Trainium及下一代Trainium4产能均已售罄，制造端受限于台积电的产能分配。
event_type: infrastructure_update
epistemic_status: pr_statement
entities:
  companies:
  - Amazon
  - AWS
  - Nvidia
  - TSMC
  - Bloomberg
  - TechCrunch
  technologies:
  - Trainium
  - Trainium4
  key_people:
  - Peter DeSantis
  - Andy Jassy
  - Doron Aronson
key_logic_flow:
- AWS正在洽谈向其他公司直接出售其自研AI芯片Trainium，用于数据中心部署，此举将更直接地挑战英伟达在AI芯片领域的主导地位。
- Amazon AI负责人Peter DeSantis向彭博社透露了相关谈判，但未指明潜在买家身份。
- CEO Andy Jassy在4月年度股东信中表示，自研AI芯片需求极其旺盛，正考虑未来向第三方出售整机架芯片。
- Jassy称如果芯片业务作为独立公司运营并向第三方销售，年收入运行率可达约500亿美元，相当于Intel的年度营收水平。
- AWS此前一直抵制直接出售芯片，因为其利润主要来自芯片驱动的云服务瀑布效应，包括存储、安全、网络和监控等配套服务收入。
- 当前Trainium芯片及下一代Trainium4的产能均已瞬间售罄，出售芯片可能加剧供应紧张，而制造端依赖台积电且面临英伟达的产能挤占。
extract_result: success
object_mentions:
- object_type: product
  name: Trainium
  canonical_name: AWS Trainium
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - AWS正在洽谈向其他公司出售其AI芯片Trainium，用于数据中心部署，这是对英伟达AI芯片主导地位的重大挑战。
  - Andy Jassy在年度股东信中表示当前Trainium芯片产能几乎瞬间售罄。
  - AWS发言人Doron Aronson确认公司未来可能向第三方出售整机架芯片，此前AWS一直拒绝直接出售请求。
  article_id: be26d7f567ae2ead
- object_type: product
  name: Trainium4
  canonical_name: AWS Trainium4
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Andy Jassy称下一代AI芯片Trainium4的产能也已售罄，而该芯片距离正式可用还有超过一年时间。
  - Trainium4产能售罄发生在AWS正式将OpenAI模型纳入其服务阵容之前。
  article_id: be26d7f567ae2ead
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