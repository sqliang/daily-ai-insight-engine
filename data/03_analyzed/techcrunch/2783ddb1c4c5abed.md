---
title: Crypto exchange OKX wants AI agents to hire and pay each other
source: https://techcrunch.com/2026/06/30/crypto-exchange-okx-wants-ai-agents-to-hire-and-pay-each-other/
author:
- '[[Jagmeet Singh]]'
published: '2026-06-30'
created: '2026-06-30'
description: OKX is bringing together payments, identity and reputation into a marketplace
  for AI agents.
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 2783ddb1c4c5abed
manifest_dates:
- '2026-06-30'
source_type: news_media
tldr: OKX 推出 AI 代理市场，支持代理间相互雇佣和自主支付
objective_summary: OKX 发布 OKX AI 市场，允许 AI 代理相互雇佣、使用稳定币自主结算并建立链上声誉，面向加密开发者和独立创业者，已完成
  50 家服务商内测后向开发者开放。
event_type: application_landing
epistemic_status: pr_statement
entities:
  companies:
  - OKX
  - CertiK
  - CoinAnk
  - GenLayer
  technologies:
  - AI Agent
  - Blockchain
  - Stablecoin
  key_people:
  - Star Xu
  - Haider Rafique
key_logic_flow:
- OKX 推出名为 OKX AI 的市场，允许 AI 代理相互雇佣、使用稳定币自主支付并建立链上声誉。
- 该市场基于 OKX 此前开发的数字钱包、稳定币支付和持久身份技术，在 50 家早期 AI 服务提供商内测后向开发者开放。
- OKX CEO Star Xu 称传统金融基础设施为人类设计，代理经济需要为自主软件设计的新基础设施。
- OKX CMO Haider Rafique 预测代理商务将在五年内成为万亿级市场，由小额支付和自主软件驱动。
- CertiK、CoinAnk 和 GenLayer 作为早期合作伙伴，分别提供安全评估、实时市场数据和争议解决服务。
- OKX 将把其交易所的欺诈检测、合规系统和内部基础设施应用于该市场，并分阶段扩大开放范围。
extract_result: success
impact_score:
  score: 4.5
  reason: OKX AI 市场是加密交易所在 AI 代理基础设施领域的一次重要产品落地，整合了数字钱包、稳定币支付和链上身份等已有技术组件。50家服务商内测后向开发者开放，且有
    CertiK、CoinAnk 等具体合作伙伴，说明产品具备基本可用性。但影响范围受限于加密原生生态，技术架构上并无突破性创新（属现有技术组合），且 CEO
    和 CMO 的万亿市场预测属于 PR 叙事绑架。短期行业冲击有限，主要在加密+AI交叉圈层产生讨论，不影响主流 AI 开发范式。
sentiment: mixed
developer_sentiment:
  tone: skeptical
  primary_focus: 加密生态锁定与自主代理支付的实际可行性——代理间商务是真实需求还是解决方案在寻找问题
hype_assessment:
  level: medium
  reason: 明显存在 PR 包装成分：CEO 引用 '一个人公司年入百万美元'、CMO 预测 '五年内万亿市场' 属于典型的未来叙事放大。但产品本身有实质内容——50家内测伙伴、具体用例（安全评估、市场数据、争议解决）、分阶段开放计划，并非空壳概念。属于'有干货但包装过度'的中等炒作级别。
information_entropy: medium
domain_disruption:
  technical_innovation: 无——将加密交易所已有基础设施（钱包、稳定币、合规系统）与 AI 代理框架集成，各组件均为成熟技术的组合应用，未涉及架构或算法层面的本质突破。
  business_model: 代理间自主商务的 marketplace 模式——通过稳定币微支付实现 AI 服务按需交易，从 SaaS 按席位收费转向按次/按查询计费，可能重塑
    AI 服务的消费和交付方式。但该模式依赖加密生态渗透率，短期内难以脱离币圈闭环。
engineering_complexity: prototype
compound_value:
  score: 7.0
  reason: 该事件的核心价值在于为'代理经济'构建底层的支付与信任基础设施。如果 AI 代理间的自主雇佣和结算成为主流范式，OKX 作为首批提供稳定币支付+链上声誉+纠纷解决一体化平台的角色将享有显著的先发优势和网络效应——每多一个代理参与交易，平台的价值和粘性就指数级增长。5年万亿级市场的预期虽然激进，但微支付+自主软件的方向确实存在结构性需求缺口（传统金融
    rails 不适合高频低值的代理间结算）。风险在于：代理经济爆发的确定性不足、竞争壁垒高度依赖 OKX 在加密领域的既有生态和合规能力、以及跨链/跨平台的互操作性挑战。7分对应'有潜力成为细分赛道基础设施，但需持续验证'上限。
value_capture_layer: agent_middleware
moat_impact: creates_new_moat
key_beneficiaries:
- OKX
- CertiK
- GenLayer
- CoinAnk
competitive_casualty:
- 传统支付 rails（Visa/Mastercard 小额跨境支付场景）
- 传统自由职业平台（Fiverr、Upwork 的 AI 替代场景）
- 传统 RPA 厂商
- 缺乏支付基础设施的闭源 Agent 平台
market_opportunities:
- 开发者可围绕 AI 代理间自主结算场景，构建垂直行业的去中心化服务平台，例如安全审计、实时数据查询、智能合约争议仲裁等按需付费服务
- 创业者可探索'一人公司'模式，利用 OKX AI 市场将业务环节外包给 AI 代理，实现全天候自动化运营并大幅降低人力成本
- 传统 SaaS 和 API 服务商可将其接口改造为 AI 代理可自主发现和调用的服务，接入代理经济生态获取增量收入
risk_matrix:
  regulatory: 稳定币支付在各司法辖区的合规性存在显著不确定性；AI 代理自主签约和支付可能触发反洗钱（AML）和了解你的客户（KYC）监管要求，且代理行为导致的法律责任归属尚不明确
  technological: 区块链网络的交易确认延迟和 Gas 费用波动可能影响小额高频支付的可行性；智能合约漏洞及跨链互操作性问题可能制约市场扩展
  competitive: 传统科技巨头（苹果、谷歌、亚马逊）可能推出自有 AI 代理支付方案；其他头部加密交易平台（如 Binance、Coinbase）可能快速跟进同类市场，形成同质化竞争
  ethical: AI 代理自主支配资金可能产生不可预见的社会后果，如代理间串通操纵市场、进行不当交易或欺诈行为；缺乏清晰的问责机制和责任归属框架
  additional:
  - 市场高度依赖 OKX 平台生态，存在平台锁定和单点故障风险；代理经济的法律主体地位尚未在任何司法辖区得到承认，存在根本性的法律真空
confidence:
  impact: medium
  compound: medium
  hype: high
actionable_insight: speculative_watch
---

When AI agents begin working for people — and increasingly for one another — they will need a way to find jobs, pay for services, and build trust. Crypto exchange OKX is betting that future is closer than many expect, launching a marketplace where AI agents can hire one another, settle payments autonomously, and build portable on-chain reputations.

Called OKX AI, the marketplace opens to developers on Tuesday following a closed beta involving 50 early AI service providers. The marketplace builds on technology OKX previously developed to let AI agents hold digital wallets, make payments using stablecoins, and establish persistent identities.

The launch marks OKX’s latest push beyond crypto trading as it seeks to become a broader fintech company. With more than 150 million users globally, OKX is betting the next generation of customers will not just be people or institutions, but AI agents capable of transacting autonomously, giving rise to an emerging “agent economy.”

“The coming decade will be defined by one-person companies that generate over a million dollars in annual revenue – because every individual effectively gains an unlimited workforce,” Star Xu, founder and CEO of OKX, told TechCrunch. “Traditional financial infrastructure was built for humans. The agentic economy needs infrastructure designed for autonomous software. That is why we built OKX.AI.”

Haider Rafique, OKX’s chief marketing officer and global managing partner, said the company believes “agentic commerce” could become a trillion-dollar market over the next five years, driven by micropayments and autonomous software.

The marketplace is aimed at crypto developers building AI applications and solo entrepreneurs looking to automate parts of their businesses with AI agents, Rafique told TechCrunch. The company expects those developers to build applications for the marketplace, allowing other users to access AI-powered tools without having to build them from scratch.

Among the early builders are CertiK, whose service lets AI agents assess the security of a crypto wallet or token before executing a transaction, and CoinAnk, which provides live market data on a pay-per-query basis. GenLayer, another launch partner, is bringing dispute-resolution infrastructure to the marketplace to help AI agents resolve contractual disagreements.

By using blockchain-based payments and stablecoins, the company says AI agents can settle transactions around the clock, including low-value micropayments that would be impractical using conventional payment rails.

Rafique said OKX is applying the same fraud detection, compliance systems, and internally developed infrastructure that underpin its cryptocurrency exchange to the marketplace, which will be rolled out in phases before becoming more widely available.