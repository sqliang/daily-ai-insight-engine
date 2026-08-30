---
title: Nvidia agrees to acquire Hugging Face for $13B
source: https://www.businessinsider.com/nvidia-in-talks-to-buy-hugging-face-13-billion-dollars-2026-8
author:
- '[[mfiguiere]]'
published: '2026-08-27'
created: '2026-08-27'
manifest_dates:
- '2026-08-27'
- '2026-08-28'
description: 'https://www.theinformation.com/articles/nvidia-agrees-buy-op... (paywalled)https://techcrunch.com/2026/08/24/hugging-face-reportedly-in...
  Comments URL: https://news.ycombinator.com/item?id=49458161 Points: 1090 # Comments:
  460'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: aec1fae1b903de5c
source_type: community_discussion
tldr: Nvidia 正在就收购 Hugging Face 进行谈判，潜在估值超过 130 亿美元，可能成为其迄今最大交易之一。双方尚未达成协议，谈判仍可能破裂；微软也曾接洽但谈判未继续。
objective_summary: Nvidia 近几周与 Hugging Face 就收购展开谈判，潜在交易对该平台的估值超过 130 亿美元，但双方尚未达成协议，谈判仍可能破裂。该消息来源于知情人士，Nvidia
  与 Hugging Face 均未回应置评请求。微软也曾与 Hugging Face 会面，但相关谈判已不在进行中。Nvidia 此前参与了 Hugging Face
  2023 年 2.35 亿美元的融资轮，并曾提出 5 亿美元投资邀约但被对方拒绝。
event_type: capital_movement
epistemic_status: rumor_leak
entities:
  companies:
  - Nvidia
  - Hugging Face
  - Microsoft
  - AMD
  - Intel
  - Business Insider
  - Financial Times
  technologies:
  - open-source AI
  key_people:
  - Clément Delangue
  - Julien Chaumond
  - Thomas Wolf
key_logic_flow:
- Nvidia 近几周与 Hugging Face 就收购进行谈判，潜在估值超过 130 亿美元，但双方尚未达成协议，谈判仍可能破裂。
- 该消息基于知情人士的说法，Nvidia 与 Hugging Face 均未回应置评请求，Business Insider 首先报道 Hugging Face 收到收购意向。
- 微软也曾与 Hugging Face 会面，但两位知情人士表示相关谈判已不在进行中。
- Nvidia 与 Hugging Face 早有交集：Nvidia 参与了其 2023 年 2.35 亿美元融资轮，且 Hugging Face 去年年底拒绝了
  Nvidia 提出的 5 亿美元投资邀约。
- 收购该平台可让 Nvidia 在开发者群体中获得更大立足点并推动更多工作负载运行于其芯片，但也会削弱 Hugging Face 的中立性，因其同时支持 AMD、Intel
  等竞争对手的硬件。
object_mentions:
- object_type: company
  name: Hugging Face
  canonical_name: Hugging Face
  url: https://huggingface.co
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Nvidia 正在就收购 Hugging Face 进行谈判，潜在交易对该平台估值超过 130 亿美元，可能成为该芯片巨头迄今最大的交易之一。
  - Hugging Face 位于开源 AI 生态系统的中心，托管数百万个 AI 模型和数据集，开发者可以在此基础上构建应用。
  - Nvidia 参与了 Hugging Face 2023 年 2.35 亿美元的融资轮，当时对其估值为 45 亿美元。
  article_id: aec1fae1b903de5c
extract_result: success
impact_score:
  score: 7.5
  reason: 从行业影响看，Hugging Face 是开源 AI 模型分发的事实中心，托管数百万模型与数据集，处于开发者生态的核心位置。若英伟达以超过 130
    亿美元将其收入囊中，将同时掌控 AI 算力供给（芯片）与开源模型分发入口，直接削弱开源生态的中立性，并对 AMD、Intel 等竞争对手形成生态压制，属于足以改变局部竞争格局级别的重大并购事件。但需注意两点下调因素：其一，该消息仍处于
    rumor_leak 状态，双方未证实且谈判明确可能破裂，存在较大不确定性；其二，这属于资本整合而非技术范式转移，不会像 ChatGPT 发布那样改变技术能力边界。综合评分为
    7.5 分。
sentiment: mixed
developer_sentiment:
  tone: skeptical
  primary_focus: Hugging Face 中立性丧失与英伟达 CUDA 生态锁定的风险
hype_assessment:
  level: medium
  reason: 该报道基于知情人士消息，属未证实传闻，文章明确承认谈判可能破裂，存在相当不确定性。标题中'130 亿美元'与'Nvidia 最大交易之一'等表述天然具备传播张力，容易引发市场对英伟达'垄断开源
    AI'的过度解读。但报道本身措辞克制，未使用'颠覆''革命'等煽动性词汇，且引用了 2023 年融资轮、去年 5 亿美元投资被拒等已报道事实作为背景支撑，并非空穴来风的概念炒作。综合判定为存在一定包装的中等水分。
information_entropy: high
domain_disruption:
  technical_innovation: 事件本身无技术突破，属资本并购。但若收购达成，技术层面的深层影响在于：英伟达将从芯片硬件层向上延伸至开源模型分发与协作层，掌控
    Hugging Face 的模型托管、数据集、推理 API 与开发者工作流入口，可能引导开源生态的模型优化、量化与部署工具链深度绑定 CUDA/Nvidia
    栈，从而在软件生态层面构筑新的护城河。
  business_model: 英伟达的商业模式核心是销售 GPU 算力。收购 Hugging Face 可形成'芯片+模型分发+开发者生态'的飞轮：开源社区在
    HF 上构建与共享模型，推理负载将天然流向英伟达芯片；同时 HF 的企业版、推理端点与商业订阅可打包进英伟达的 AI 企业套件，强化其对 AI 软件栈的纵向控制。反噬风险在于：中立性丧失可能促使社区与
    AMD/Intel 共同推动去中心化替代方案（如模型镜像、自托管平台），反而削弱 HF 的生态聚合价值。
engineering_complexity: infrastructure
compound_value:
  score: 8.0
  reason: Hugging Face 是开源 AI 生态的基础性分发与协作枢纽，承载数百万模型/数据集/Spaces，具备极强的双边网络效应：开发者越多→上传的资产越多→平台对开发者的价值越大，这种自增强飞轮使其成为
    AI 界的'GitHub'。即便以 130 亿美元估值收购，其战略意义远超财务回报——若并入 Nvidia，将形成'GPU 霸主 + 开源开发者生态入口'的垂直整合，把硬件垄断延伸到软件分发层，驱动更多训练/推理工作负载锁定在
    CUDA 生态，3-5 年后大概率仍是行业基石。但需谨慎的两点：一是 HF 当前商业化收入与 130 亿估值存在差距，变现路径仍待验证；二是收购会破坏其跨硬件中立性（同时支持
    AMD/Intel），可能促使部分社区流向替代平台（ModelScope、企业自建 hub），存在生态碎片化风险。综合网络效应、转换成本与战略卡位，给予 8.0
    分。
value_capture_layer: agent_middleware
moat_impact: strengthens_monopoly
key_beneficiaries:
- NVIDIA
- Hugging Face
competitive_casualty:
- AMD
- Intel
- Together AI
- Replicate
- Baseten
market_opportunities:
- 创业者可抓住 Hugging Face 中立性可能受损的窗口期，打造或押注中立的第三方模型中心/注册平台，承接对厂商中立性敏感的开源社区与企业开发者。
- 企业 AI 团队应着手建设内部模型注册表与多硬件适配层，将模型资产管理从单一芯片/云供应商解耦，以降低潜在收购落地后的生态锁定风险。
- 若收购推进，建议关注与 NVIDIA 推理栈（NIM/NeMo）深度集成的工具链与微调服务机会，围绕 Hugging Face 生态的算力需求将加速向 NVIDIA
  体系倾斜。
risk_matrix:
  regulatory: 超 130 亿美元的收购将面临 FTC、欧盟及中国等多辖区反垄断审查；Hugging Face 作为开源 AI 生态关键基础设施，监管可能附加中立性承诺、数据共享或开放访问条件，极端情况下甚至否决交易。
  technological: 若交易落地，Hugging Face 的平台中立性受损，开源社区与开发者可能迁移至更中立或去中心化的模型分发方案（如 ModelScope、OpenRouter
    或社区 fork），平台存在被替代的技术风险。
  competitive: 微软、AMD、Intel 等竞争巨头可能在交易后加速扶持中立替代平台或自建模型中心；Nvidia 的芯片+平台垂直整合亦会挤压第三方工具商生存空间，加剧生态战争。
  ethical: 开源模型托管公地被芯片巨头私有化可能削弱开放科学的信任基础；模型与数据分发的高度集中化带来访问控制、社区治理及全球开发者公平访问等伦理风险。
  additional:
  - 交易仍处于传闻阶段，谈判可能破裂，基于未证实信息进行重大决策存在误判风险
  - Hugging Face 创始团队与组织文化能否在收购后保留存在整合风险，核心人才流失可能显著削弱平台价值
confidence:
  impact: medium
  compound: medium
  hype: high
actionable_insight: monitor
---

Nvidia has been in talks to acquire Hugging Face, the popular AI platform for sharing and building with open-source models, in what could be one of the chip giant's biggest deals yet.

The two parties have had acquisition conversations in recent weeks about a deal that would value Hugging Face at more than $13 billion, according to a person familiar with the matter. The companies have not yet reached a deal, and the talks could still fall apart, the person said. Business Insider on Sunday was the first to report that Hugging Face was fielding takeover interest.

Nvidia and Hugging Face did not respond to requests for comment.

Nvidia has increasingly ramped up dealmaking with its enormous cash pile. The company said Wednesday that it has $18 billion committed to equity investments for the rest of its fiscal year, on top of $47.9 billion it already holds in private companies.

Microsoft also met with Hugging Face, but the person familiar and a second person said talks are not ongoing.

Nvidia already has a relationship with Hugging Face. The chipmaker participated in its $235 million funding round in 2023 that valued it at $4.5 billion.

Hugging Face turned down a $500 million investment offer from Nvidia late last year that would have valued it at $7 billion, the Financial Times previously reported. Hugging Face said at the time it did not want a dominant investor that could sway decisions.

Hugging Face sits at the center of the open-source AI ecosystem, hosting millions of AI models and datasets that developers can build on. Owning the platform could give Nvidia a bigger foothold with those developers — and potentially drive more workloads onto its chips.

Hugging Face was founded in 2016 by French entrepreneurs Clément Delangue, Julien Chaumond, and Thomas Wolf.

But Nvidia ownership could also complicate one of Hugging Face's strengths: its neutrality. The platform supports models and hardware from across the industry, including Nvidia competitors such as AMD and Intel.

*Have a tip?*

*Contact Katie Roof via email at kroof@businessinsider.com or Signal at @kroof.26*

*Contact Geoff Weiss via email at *__gweiss@businessinsider.com__* or Signal at @geoffweiss.25.*

*Contact Ashley Stewart via email at *__astewart@businessinsider.com__* or Signal at +1-425-344-8242.*

*Use a personal email address and a nonwork device; *__here's our guide to sharing information securely__*.*