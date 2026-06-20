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