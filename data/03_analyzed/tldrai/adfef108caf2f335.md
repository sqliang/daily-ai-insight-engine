---
title: Facing US export controls, China's DeepSeek plans to make its own chips (2
  minute read)
source: https://arstechnica.com/ai/2026/07/facing-us-export-controls-chinas-deepseek-plans-to-make-its-own-chips/?utm_source=tldrai
author: []
published: ''
created: '2026-07-09'
description: TLDR AI 每日头条
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: adfef108caf2f335
source_type: news_media
tldr: DeepSeek计划自研推理芯片，以应对美国出口管制并减少对华为和英伟达的依赖
objective_summary: DeepSeek正计划进入芯片业务，专注数据中心推理芯片，已筹备约一年并招聘工程师。此举旨在减少对华为和英伟达的依赖，同时应对美国出口管制。OpenAI和Anthropic也在进行类似的芯片自研计划。
event_type: infrastructure_update
epistemic_status: rumor_leak
entities:
  companies:
  - DeepSeek
  - OpenAI
  - Anthropic
  - Nvidia
  - Huawei
  - Alibaba
  - Baidu
  - Broadcom
  technologies: []
  key_people: []
key_logic_flow:
- DeepSeek计划进入芯片业务，已筹备约一年，正在与硬件和硅片领域的潜在合作伙伴会面并招聘工程师。
- 该公司专注于数据中心推理芯片，而非训练芯片，目标是减少对华为和英伟达的依赖。
- 美国出口管制阻止了英伟达在中国市场的扩展，华为目前控制着中国约一半的数据中心芯片市场。
- 中国科技巨头阿里巴巴和百度也在推进自研芯片计划，DeepSeek并非唯一入局者。
- OpenAI与Broadcom联合发布了其首款推理芯片Jalapeño，旨在减少对英伟达的依赖并获取端到端技术栈控制。
- Anthropic也在探索定制芯片设计，但尚未有公开可见的里程碑进展。
extract_result: success
impact_score:
  score: 5.5
  reason: DeepSeek 自研推理芯片的计划是 AI 行业垂直整合趋势的又一印证，与 OpenAI 的 Jalapeño、Anthropic 的探索、以及阿里/百度的自研芯片形成呼应，共同标志着推理芯片从英伟达单极供应走向多极化的结构性变化。作为目前最具国际竞争力的中国大模型公司，DeepSeek
    的入局可能在中期改变中国数据中心推理芯片的竞争格局。但该计划仍处于早期筹备阶段（筹备约一年、招聘工程师中），短期内没有实际产品落地，冲击力有限，更多是战略信号层面的影响。
sentiment: mixed
developer_sentiment:
  tone: neutral
  primary_focus: 自研推理芯片能否降低 DeepSeek 模型的服务成本并保证供应链自主可控
hype_assessment:
  level: low
  reason: 路透社/Ars Technica 的报道基于三位知情人士信息，措辞客观克制。文章清晰标注了计划处于早期阶段（筹备约一年、招募工程师中），没有使用'颠覆'、'革命'等
    PR 包装词汇，同时交代了 OpenAI、Anthropic、阿里、百度也在做类似动作，提供了合理的行业参照系，不存在单独夸大。
information_entropy: medium
domain_disruption:
  technical_innovation: DeepSeek 计划设计数据中心推理专用芯片而非训练芯片，顺应了行业从通用 GPU 向推理专用 ASIC（如 OpenAI
    Jalapeño）演进的趋势。但具体架构设计、制程工艺和性能目标尚未披露，目前更多是战略方向的确定而非技术突破的展示。
  business_model: 自研芯片将使 DeepSeek 从纯模型提供商向垂直整合的 AI 基础设施公司转型，减少对华为昇腾和英伟达的依赖，获得更可控的推理成本结构与供应链韧性。这反映了在地缘政治压力下，头部
    AI 公司走向'芯片+模型+应用'全栈化商业模式的行业趋势。
engineering_complexity: prototype
compound_value:
  score: 7.5
  reason: DeepSeek自研推理芯片是典型的垂直整合战略，旨在构建模型-芯片协同优化的飞轮效应。如果成功，将带来三大复利效应：(1) 每代芯片可针对DeepSeek模型架构深度优化，推理成本持续降低，形成硬件-软件协同的护城河；(2)
    减少对华为/英伟达的依赖意味着供应安全与成本结构的双重优势，尤其在出口管制持续收紧背景下；(3) 对标OpenAI+Broadcom的Jalapeño芯片路径已初步验证此逻辑——领先AI实验室控制芯片层正在成为行业趋势。但芯片设计是极高门槛的资本密集型行业，DeepSeek作为软件公司跨界硬件，执行风险不可忽视：人才争夺激烈、先进制程受限于地缘政治、首次流片成功率低。此外阿里和百度也在同步推进自研芯片，竞争不会缺席。整体给予7.5分——长期复利潜力突出，但需持续观察工程进度和流片结果，目前仍处于验证期。
value_capture_layer: hardware_compute
moat_impact: creates_new_moat
key_beneficiaries:
- DeepSeek
- Broadcom
- SMIC
competitive_casualty:
- Huawei
- Nvidia
- 中国AI芯片初创公司
market_opportunities:
- AI公司自研芯片趋势下，芯片设计服务（类似Broadcom的ASIC合作模式）和IP授权市场将持续增长，创业公司可切入定制化推理芯片设计咨询与验证服务环节
- 推理芯片（Inference Chip）作为差异化细分赛道，相比训练芯片设计门槛更低、场景更垂直（数据中心推理负载），适合聚焦特定场景的芯片初创企业布局
- 美国出口管制催生的国产替代需求为国内半导体EDA工具链、芯片仿真验证和先进封装配套产业带来窗口期，创业公司可围绕自主可控的芯片设计生态提供工具和服务
risk_matrix:
  regulatory: 美国出口管制可能进一步升级，将DeepSeek列入实体清单并切断其与台积电等代工厂的合作通道；中国监管层若将芯片自研纳入战略统筹，可能抬高行业准入门槛
  technological: 芯片设计复杂度极高、开发周期长达2-3年，DeepSeek在硬件领域无实践经验，约一年的筹备期远不足以应对从架构设计到流片验证的全链条技术挑战；且可能因缺乏EDA工具授权和先进制程产能而导致项目延宕或失败
  competitive: 英伟达在AI芯片领域拥有绝对生态优势，华为占据中国数据中心芯片约50%市场份额，同时阿里巴巴、百度等巨头亦在自研芯片赛道布局，DeepSeek作为新入局者面临多重夹击；OpenAI与Broadcom的Jalapeño芯片已率先发布，形成先发压力
  ethical: 无
  additional:
  - 芯片行业人才极度稀缺，DeepSeek在工程师招聘上将与华为、阿里巴巴等成熟芯片团队展开激烈争夺，人才成本高企且招聘周期长
  - 即使完成芯片设计，流片制造仍高度依赖台积电或中芯国际的先进制程产能，地缘政治风险可能中断供应链
confidence:
  impact: medium
  compound: medium
  hype: medium
actionable_insight: monitor
---

DeepSeek, the Chinese startup developing large language models that are competitive with those from US companies like OpenAI and Anthropic, is planning to enter the silicon business, according to Reuters.

Citing three people familiar with the matter, Reuters writes that DeepSeek has been working on a move into silicon for about a year. It has been meeting with potential partners in the hardware and silicon space and has been hiring engineers for the project.

The focus is on data center chips for inference, not training, and the goal is likely to reduce reliance on both Huawei and Nvidia.

Nvidia is the chipmaker for most AI companies in North America and Europe, but a United States export ban has prevented the company from achieving a similar presence in China. Huawei controls about half of the data center chip market there, and DeepSeek isn’t the only one trying to enter; Chinese tech giants like Alibaba and Baidu have been making moves, too.

While chip export controls in the US are a major reason this is an urgent concern for DeepSeek, US-based AI companies are making similar chip plans.

For example, OpenAI and Broadcom jointly announced Jalapeño, the former’s first chip designed for inference at scale, just a couple of weeks ago. Anthropic, too, has been exploring custom chip design, though there have not been any publicly visible milestones yet.

In OpenAI’s case, it’s partly a play to reduce its reliance on Nvidia, but it’s also a desire to have Apple-like control over the entire tech stack for its products. Further, getting in at the silicon and data center levels can be an advantage in a market where data center access is likely to remain constrained, with multiple companies competing for compute as they scale up their AI models and services.