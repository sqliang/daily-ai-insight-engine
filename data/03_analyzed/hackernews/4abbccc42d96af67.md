---
title: 'OpenAI Jalapeño: Better than Nvidia Blackwell'
source: https://newsletter.semianalysis.com/p/openai-jalapeno-better-than-nvidia
author:
- '[[bmulholland]]'
published: '2026-08-25'
created: '2026-08-26'
manifest_dates:
- '2026-08-26'
description: 'https://www.bloomberg.com/news/articles/2026-08-25/openai-cl..., https://archive.ph/yCTrr
  Comments URL: https://news.ycombinator.com/item?id=49434378 Points: 477 # Comments:
  308'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 4abbccc42d96af67
source_type: community_discussion
tldr: SemiAnalysis 发布文章宣称 OpenAI 自研芯片 Jalapeño 性能优于英伟达 Blackwell。但本次抓取仅获得 Cloudflare
  反爬拦截页，正文内容缺失，所有信息仅来自标题与备用快照链接。
objective_summary: 'SemiAnalysis 通讯发布标题为《OpenAI Jalapeño: Better than Nvidia Blackwell》的文章，声称
  OpenAI 自研芯片 Jalapeño 的性能超越英伟达 Blackwell 平台。抓取管道在下载正文时遭遇 Cloudflare 反爬安全验证，仅返回错误页面，未获得任何正文内容。文章提供了
  archive.ph 备用快照链接（https://archive.ph/yCTrr），但本次抓取结果中同样不含快照正文。当前可验证的事实仅有文章标题与来源信息。'
event_type: infrastructure_update
epistemic_status: rumor_leak
entities:
  companies:
  - OpenAI
  - Nvidia
  - SemiAnalysis
  technologies:
  - Jalapeño
  - Blackwell
  key_people: []
key_logic_flow:
- 'SemiAnalysis 发布标题为“OpenAI Jalapeño: Better than Nvidia Blackwell”的文章，宣称 OpenAI
  自研芯片性能优于英伟达 Blackwell。'
- 文章正文抓取失败，管道仅获取到 Cloudflare 反爬验证页面，页面提示用户运行杀毒扫描或联系网络管理员。
- 正文中提供了 archive.ph 备用抓取链接，但快照内容同样未包含在本次抓取结果中，无法核实具体论点。
object_mentions:
- object_type: project
  name: OpenAI Jalapeño
  canonical_name: OpenAI Jalapeño
  url: null
  confidence: low
  article_role: primary_subject
  evidence_snippets:
  - '文章标题为“OpenAI Jalapeño: Better than Nvidia Blackwell”，宣称 OpenAI 的 Jalapeño 芯片性能优于英伟达
    Blackwell，但正文未能成功抓取，仅能依据标题确认该对象存在。'
  article_id: 4abbccc42d96af67
- object_type: product
  name: Nvidia Blackwell
  canonical_name: Nvidia Blackwell
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - 文章标题将 OpenAI Jalapeño 与英伟达 Blackwell 进行对比并声称前者性能更优，但正文内容缺失，无法获取更多对比细节。
  article_id: 4abbccc42d96af67
extract_result: success
compound_value:
  score: 6.5
  reason: 本次事件的核心信号是 OpenAI 自研推理芯片 Jalapeño 被 SemiAnalysis 宣称性能超越 Nvidia Blackwell。从资本视角看，若该宣称成立，意味着
    AI 算力价值链的利润分配将从通用 GPU 供应商向垂直整合的模型厂商转移：OpenAI 将获得显著的单位 token 成本优势与供应链自主权，且该优势会随推理需求指数级增长而持续复利——单芯片成本优势直接转化为毛利率优势，这是典型的基础设施级复利资产。但必须保持审慎：其一，本次抓取仅获得标题，正文被
    Cloudflare 拦截，认识论状态为 rumor_leak，缺乏可核实的能效、良率、单位成本等关键数据；其二，历史上'自研芯片超越 Blackwell'的宣称多次出现（Google
    TPU、AWS Trainium），实际落地均受制于生态与量产规模；其三，Jalapeño 据传为推理专用芯片，训练侧仍依赖 Nvidia。综合评分 6.5：具备成为
    AI 推理基础设施的长期复利潜力，但需在 12-18 个月内看到量产数据与真实 benchmark 验证方可上调。
value_capture_layer: hardware_compute
moat_impact: creates_new_moat
key_beneficiaries:
- OpenAI
- Broadcom
- TSMC
competitive_casualty:
- Nvidia
- Cerebras
- Groq
market_opportunities:
- AI 推理芯片的多元竞争将加速推理成本长期下行，建议 AI 应用层团队提前评估算力成本结构，布局对推理成本敏感的高频场景
- 定制 AI 芯片（ASIC/XPU）设计服务、先进封装、Chiplet 及推理工具链存在结构性机会，可关注与 OpenAI 芯片供应链（如 Broadcom、台积电先进制程）相关的一二级标的
- 自研芯片趋势强化了多供应商算力架构需求，建议关注非英伟达推理芯片（TPU、Trainium、自研 ASIC）生态上的迁移工具与混合调度平台机会
risk_matrix:
  regulatory: 若 Jalapeño 属实并采用先进制程，将落入美国对华先进算力芯片出口管制框架；同时'性能超越 Blackwell'的单方声明未经验证，存在夸大宣传与误导资本市场的信息合规风险
  technological: 正文完全缺失、论点无法核实，'优于 Blackwell' 仅凭标题；自研芯片存在流片延期、实际性能不及预期、软件生态（CUDA 替代）不足等被证伪或迭代淘汰风险
  competitive: 英伟达 CUDA 生态护城河与 Rubin 系列迭代可能压制新进入者；谷歌 TPU、亚马逊 Trainium、微软 Maia 等自研芯片均已量产落地，OpenAI
    若推进不及预期将失去先发优势
  ethical: 未经证实的'碾压级'芯片声明经标题传播可能引发资本市场非理性波动与信息误导；算力进一步向少数巨头集中也可能加剧行业马太效应与芯片人才争夺
  additional:
  - 情报真实性风险：本次抓取仅获标题、正文被 Cloudflare 拦截、archive.ph 快照亦未取回，任何基于该信息的决策都面临高误判概率，须以官方披露或可信全文快照交叉验证后再行动
confidence:
  impact: medium
  compound: low
  hype: medium
actionable_insight: monitor
impact_score:
  score: 6.5
  reason: SemiAnalysis 是半导体与 AI 基础设施领域最受信任的独立分析机构之一，其关于 OpenAI 自研芯片的爆料若属实，将直接影响英伟达在
    AI 算力市场的统治地位，属于改变局部竞争格局级别的事件。但本次抓取仅获得标题与 Cloudflare 反爬错误页，正文完全缺失，性能对比口径、测试条件、成本数据均无法核实，事件仍处于
    rumor_leak 认识论状态。因此冲击力评估介于"重要事件"与"无法验证的传闻"之间，给予中等偏上分数。
sentiment: mixed
developer_sentiment:
  tone: skeptical
  primary_focus: Jalapeño 芯片相对 Blackwell 的性能与成本数据是否真实可信
hype_assessment:
  level: medium
  reason: 标题使用 "Better than Nvidia Blackwell" 这一强对比式吸睛措辞，属于典型的夸张性表述；SemiAnalysis 历史上以扎实的内部信源与数据分析著称，但本次正文缺失、仅有标题，无法核查其数据严谨性，存在一定的标题党水分，尚不足以定性为纯概念炒作。
information_entropy: low
domain_disruption:
  technical_innovation: OpenAI 自研芯片 Jalapeño（据外部报道为与博通合作、面向推理负载的定制 ASIC）若在性能或能效上超越
    Blackwell，将验证"为特定工作负载定制化的专用芯片优于通用 GPU"的技术路线。但本次报道正文缺失，该论断仍属未经证实的传闻，无法确认真实架构细节。
  business_model: 若 OpenAI 能以显著更低成本自供推理算力，将大幅降低对英伟达的依赖，削弱英伟达在 AI 算力市场的定价权与生态锁定，并激化"模型公司垂直整合自研芯片"与"GPU
    平台商"两种商业模式的正面竞争。
engineering_complexity: prototype
---

> 备用抓取来源：https://archive.ph/yCTrr

##
What can I do to prevent this in the future?


If you are on a personal connection, like at home, you can run an anti-virus scan on your device to make sure it is not infected with malware.

If you are at an office or shared network, you can ask the network administrator to run a scan across the network looking for misconfigured or infected devices.