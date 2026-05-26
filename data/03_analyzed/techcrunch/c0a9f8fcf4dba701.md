---
title: 'Report: Google and SpaceX in talks to put data centers into orbit'
source: https://techcrunch.com/2026/05/12/report-google-and-spacex-in-talks-to-put-data-centers-into-orbit/
author:
- '[[Rebecca Bellan]]'
published: '2026-05-12'
created: '2026-05-13'
description: Google and SpaceX are in talks to build data centers in orbit, pitching
  space as the future home for AI compute, even as costs today remain far higher than
  on the ground.
tags:
- clippings
id: c0a9f8fcf4dba701
source_type: news_media
tldr: Google与SpaceX据报谈判建设轨道数据中心，用于AI算力部署
objective_summary: 《华尔街日报》援引知情人士消息称，Google与SpaceX正就将数据中心送入轨道进行谈判。SpaceX计划以太空数据中心作为AI算力成本优势进行1.75万亿美元IPO。Google还计划2027年前发射原型卫星（Project
  Suncatcher），并与其他火箭公司接触。
event_type: infrastructure_update
epistemic_status: rumor_leak
entities:
  companies:
  - Google
  - SpaceX
  - xAI
  - Anthropic
  - The Wall Street Journal
  - TechCrunch
  technologies:
  - AI
  key_people:
  - Elon Musk
key_logic_flow:
- 《华尔街日报》援引知情人士消息称，Google与SpaceX正在谈判将数据中心送入轨道。
- SpaceX即将进行1.75万亿美元IPO，其核心卖点是太空数据中心将在未来几年成为AI算力最便宜的场所。
- Anthropic上周与SpaceX达成协议，使用xAI在孟菲斯的数据中心计算资源，未来可能在轨道数据中心方面合作（SpaceX于2月收购了xAI）。
- Google还在与其他火箭发射公司接触，并计划在2027年前发射原型卫星，该计划名为Project Suncatcher，于2025年底公布。
- Elon Musk声称轨道数据中心运营成本更低，且不受美国地面数据中心面临的本地社区反对影响。
- TechCrunch指出，考虑卫星建造和发射成本后，目前地面数据中心仍比轨道数据中心便宜得多。
impact_score:
  score: 5.5
  reason: Google与SpaceX两大巨头探索轨道数据中心，SpaceX更是以此作为1.75万亿美元IPO的核心叙事，事件本身具有眼球效应和远期战略信号价值。但文章明确处于传闻阶段（rumor_leak），TechCrunch自身也指出考虑卫星建造和发射成本后，地面数据中心仍远比轨道方案便宜，短期内无法落地。综合判断：话题度高但实际行业冲击力中等偏上，尚不构成竞争格局的真实改变。
sentiment: mixed
developer_sentiment:
  tone: skeptical
  primary_focus: 轨道数据中心的网络延迟、硬件维护可行性和真实成本结构
hype_assessment:
  level: medium
  reason: 存在明显的PR叙事包装——'1.75万亿美元IPO'、'AI算力最便宜场所'等表述具有强烈炒作色彩，且Elon Musk本人也在造势。但文章本身保持了相对审慎的立场，引用了地面数据中心更便宜的事实数据，未完全沦为单向宣传稿。
information_entropy: low
domain_disruption:
  technical_innovation: 轨道数据中心概念涉及太空真空环境下的被动散热、太阳能直供电、无地域限制的算力部署等工程设想，但当前停留在概念阶段，缺乏已验证的技术路径或原型验证。
  business_model: 试图构建'太空算力即服务'的新商业模式，以太空环境零冷却成本和免于地面社区反对为卖点，但卫星制造成本和发射成本是现实的商业壁垒，尚无可行的单位算力经济学论证。
engineering_complexity: conceptual
market_opportunities:
- 卫星制造与太空级硬件供应链迎来新需求，可关注耐辐射芯片、太空散热系统、轻量化服务器机架等垂直组件的研发与供应机会
- 地面站通信与星地数据传输基础设施将成为轨道数据中心的配套刚需，可布局低延迟激光通信终端、卫星地面网关等方向
- 轨道数据中心保险与风险评估赛道空白，创业者可探索面向太空资产的精算模型、在轨故障应急方案咨询等创新服务
risk_matrix:
  regulatory: 轨道数据中心涉及外层空间国际法空白（《外空条约》未明确商业数据中心管辖权）、美国ITAR出口管制对太空级AI芯片的限制、FCC频谱分配冲突及轨道碎片污染防治法规，合规路径高度不确定
  technological: 当前太空发射与卫星建造成本远超地面数据中心，在轨硬件无法维修更换导致寿命有限，太空辐射对芯片可靠性的影响未经验证，且星地通信延迟难以满足AI训练的低延迟需求，技术可行性存疑
  competitive: 地面数据中心通过液冷、核能供电和芯片效率提升正在快速降低成本，SpaceX与Google的先天联盟可能挤压Anthropic、微软等竞对的可用发射资源，引发AI算力生态的地缘化分裂
  ethical: 太空数据中心可能加剧轨道碎片问题与太空军备竞赛担忧，Elon Musk通过SpaceX+xAI的纵向整合控制从发射到算力的全链条，形成AI基础设施的超级垄断，且太空算力的可及性将加剧全球AI能力不平等
  additional:
  - SpaceX 1.75万亿美元IPO若以太空AI算力为核心叙事，一旦技术落地不及预期可能引发AI资本市场大幅回调
  - 轨道数据中心作为国家级战略资产，可能成为地缘冲突中网络攻击或反卫星武器的优先目标，物理安全风险被低估
confidence:
  impact: medium
  compound: low
  hype: high
actionable_insight: monitor
---

Google and SpaceX are in talks to launch orbital data centers in space, reports The Wall Street Journal, citing sources familiar with the matter.

The potential deal comes as SpaceX gears up for its $1.75 trillion IPO later this year, selling investors on the idea that data centers in space will be the cheapest place to put AI compute within the next few years. It also follows Anthropic’s deal with SpaceX last week to use computing resources from xAI’s data center in Memphis, Tennessee, with the potential to work together on orbital ones in the future. (SpaceX acquired xAI in February.)

Google is reportedly talking to other rocket-launch companies as well. The company also plans to launch prototype satellites by 2027 as part of an initiative called Project Suncatcher, announced late last year.

Elon Musk has created hype for orbital data centers, claiming they are cheaper to operate. Advocates also point out they are free from the local backlash that U.S. ground-based buildouts attract. However, as TechCrunch recently reported, today’s terrestrial data centers are much cheaper than those in orbit once satellite construction and launch costs are factored in.

Google invested $900 million in SpaceX in 2015, according to regulatory filings.

TechCrunch has reached out to Google and SpaceX for comment.