---
title: Cybersecurity researchers aren't happy about the guardrails on Anthropic's
  Fable
source: https://techcrunch.com/2026/06/10/cybersecurity-researchers-arent-happy-about-the-guardrails-on-anthropics-fable/
author:
- '[[speckx]]'
published: '2026-06-10'
created: '2026-06-11'
description: 'Article URL: https://techcrunch.com/2026/06/10/cybersecurity-researchers-arent-happy-about-the-guardrails-on-anthropics-fable/
  Comments URL: https://news.ycombinator.com/item?id=48478969 Points: 426 # Comments:
  378'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: c3ab8c2b1dbfd6f4
source_type: community_discussion
tldr: Anthropic 发布 Fable 模型，因网络安全护栏过严遭研究人员批评。
objective_summary: Anthropic 于 2026 年 6 月发布网络安全模型 Fable，设置了严格的安全护栏限制网络安全和生物学相关请求。多名安全研究人员批评护栏基于关键词匹配过于宽泛，误伤正常安全工作。Fable
  触发护栏后会降级到 Claude Opus 4.8。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - Anthropic
  - IBM X-Force
  - Tolmo
  - OpenAI
  technologies:
  - Fable
  - Mythos
  - Claude Opus 4.8
  key_people:
  - Valentina "Chompie" Palmiotti
  - Matt Suiche
  - Lorenzo Franceschi-Bicchierai
key_logic_flow:
- Anthropic 发布了其最新网络安全模型 Fable，作为此前发布的 Mythos 模型的公开受限版本。
- Fable 设置严格的安全护栏，任何与网络安全或生物学相关的请求（如阅读博客、代码审查）都会触发护栏并降级到 Claude Opus 4.8。
- IBM X-Force 安全研究员 Palmiotti 指出，即便是阅读博客文章等无害任务也会被护栏拒绝。
- 网络安全专家 Suiche 批评护栏基于关键词匹配而非语义理解，请求编写安全代码也会被误判为网络安全工作而触发降级。
- Suiche 同时表示理解这种保守策略，认为 Anthropic 会在与新一代网络安全公司合作中逐步放宽护栏。
- Anthropic 通过 Cyber Verification Program 允许认证专业人士减少限制；OpenAI 有类似项目 Trusted Access
  for Cyber。
impact_score:
  score: 5.5
  reason: Anthropic 发布网络安全模型 Fable 因安全护栏过严遭研究人员集中批评，这一事件凸显了 AI 安全工具在'安全性'与'可用性'之间的核心矛盾。虽然不是范式转移级别的事件，但
    Fable 作为备受关注的 Mythos 的公开版本，其护栏设计失误可能倒逼 Anthropic 及行业重新思考关键词匹配方案的工程合理性，并加速认证准入机制的标准化。影响范围主要在
    AI 安全赛道的从业者圈层。
sentiment: negative
developer_sentiment:
  tone: frustrated
  primary_focus: 基于关键词匹配的安全护栏过度宽泛，导致阅读博客、代码审查、编写安全代码等正常网络安全工作被误拦截并降级到 Claude Opus
    4.8
hype_assessment:
  level: low
  reason: TechCrunch 报道为客观新闻，未出现'颠覆性''革命性'等 PR 夸大用语，文章提供了具体的批评案例（如 Palmiotti 的阅读博客被拒、Suiche
    的编写安全代码被降级），属于实打实的问题追踪而非概念炒作
information_entropy: medium
domain_disruption:
  technical_innovation: 无 - 报道焦点是安全护栏设计的工程缺陷（关键词匹配）而非模型架构或训练方法的技术突破，Fable 本身是 Mythos
    的受限公开版本
  business_model: Anthropic 的 Cyber Verification Program 认证准入机制，叠加 OpenAI 的 Trusted
    Access for Cyber，正在形成'认证专业人士放宽护栏限制'的分级服务商业模式，可能成为 AI 安全工具商用化的行业标配
engineering_complexity: production_ready
compound_value:
  score: 6.5
  reason: '从 VC 视角分析：Anthropic 发布 Fable 不是一次简单的模型迭代，而是其网络安全 AI 战略的''前哨站''。核心投资逻辑有三层——


    第一层（短期看空）：当前基于关键词匹配的护栏机制极其粗糙，阅读博客、代码审查等正常安全活动均被降级至 Claude Opus 4.8，顶尖安全研究人员（如
    Palmiotti、Suiche）公开表达不满，短期采用率和口碑受损。


    第二层（中期中性）：Anthropic 的''先严后宽''策略在高风险领域有其合理性——宁可过度拦截也不能漏放。Cyber Verification Program
    作为认证准入门槛，帮助 Anthropic 逐步积累可信用户群和真实安全用例数据，为护栏从关键词匹配向语义理解演进提供训练素材。Suiche 的评论（''先多捕后放松''）印证了这是有意为之的策略而非技术无能。


    第三层（长期看多）：如果 Anthropic 能够将 Cyber Verification Program 打造为网络安全 AI 领域的''标准准入协议''，辅以
    Project Glasswing 在企业端的数百家组织渗透，将在该垂直赛道建立强大的信任+声誉护城河——纯粹的资本和时间壁垒，竞争对手即使模型能力追上也难以短期复制。考虑到
    Anthropic 从 Mythos（仅限少数组织）到 Fable（公开受限版）再到放宽 Mythos 到数百家组织，正在一步步扩大安全 AI 的覆盖面。


    给予 6.5 分的核心原因：方向正确（安全 AI 是确定性增长赛道）但执行风险高，关键词护栏路线存在技术天花板，且过度保守可能将顶尖研究人员推向 OpenAI
    的 Trusted Access for Cyber 项目，存在窗口期竞争风险。'
value_capture_layer: foundation_model
moat_impact: creates_new_moat
key_beneficiaries:
- Anthropic
- Tolmo
- Project Glasswing 合作组织
- Cyber Verification Program 认证安全公司
competitive_casualty:
- 传统网络安全厂商（缺乏 AI 原生能力）
- 未建立安全认证体系的 AI 模型供应商
- OpenAI（需加速 Trusted Access for Cyber 以维持竞争力）
market_opportunities:
- 创业公司可针对安全研究场景开发未过度限制的网络安全AI助手，填补Fable护栏过严留下的空白
- Anthropic的Cyber Verification Program模式为AI安全厂商开辟了'认证专业访问'的商业路径，可复制为企业级安全AI订阅服务
- 现有安全工具（如代码审查、漏洞分析SaaS）可集成轻量级本地AI模型，避免云端护栏误判，提供不受限的安全编码辅助
risk_matrix:
  regulatory: 关键词匹配的护栏可能误拦正常的国家安全漏洞披露和研究活动，引发安全社区对'过度过滤阻碍关键基础设施防护'的监管讨论
  technological: 基于关键词匹配的护栏策略技术含量较低，未来可能被基于语义理解的新一代护栏架构取代，导致当前方案的快速过时
  competitive: OpenAI已有Trusted Access for Cyber同类项目，若其护栏更精准将吸引安全研究人员迁移；同时新兴创业公司可推出无护栏限制的开源安全模型，挤压Fable的生态空间
  ethical: 过严护栏可能阻碍合法的网络安全研究和漏洞发现，间接增加软件供应链风险；降级回Opus 4.8导致安全专业人员被迫使用能力较弱的模型，降低防护效率
  additional: []
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: monitor
---

Anthropic released its latest model Fable on Tuesday, billing it as a public and limited version of its powerful and much-hyped cybersecurity model Mythos.

But not everyone is happy with the restrictions, and a number of cybersecurity researchers and professionals have aired complaints online.

“[Fable] rejects any request that could be tangentially cyber related. Even innocuous tasks like reading a blog post,” said Valentina “Chompie” Palmiotti, a well-known security researcher who works at IBM X-Force.

When a prompt triggers its guardrails, Fable pauses the chat and says that its “safety measures flagged this message for cybersecurity or biology topics.”

The guardrails were put in place to limit the risk that Fable could be used to develop malware or compromise software — a long-standing concern within Anthropic. The restrictions on biology come from a similar concern around developing biological weapons.

When the AI giant released Mythos in April, it restricted the model to a limited number of companies and organizations in what it called Project Glasswing, an effort to deploy the model to secure critical software and infrastructure. Last week, Anthropic expanded access to Mythos to hundreds of organizations in 15 countries.

But despite the good intentions, many cybersecurity experts are still put off by the haphazard nature of the restrictions. Matt Suiche, a cybersecurity veteran, told TechCrunch that “if you ask it to write secure code, it assumes it is cybersecurity related work instead of software engineering best practices, and you get downgraded.” Fable is programmed to fall back to Claude Opus 4.8 if it hits a guardrail. “It seems to be keyword based, so anything in the lexical field of ‘cybersecurity’ triggers the guardrails.”


#### Contact Us

Do you have more information about how hackers are using AI? Or how cybersecuity companies are using AI? We’d love to hear from you. From a non-work device and network, you can contact Lorenzo Franceschi-Bicchierai securely on Signal at +1 917 257 1382, or via Telegram and Keybase @lorenzofb, or email.“But it is understandable as we are still in the early days and they are still adapting their guardrails. I am sure they are going to evolve over time as Anthropic and other frontier model companies will collaborate more with the current new generation of cybersecurity companies,” said Suiche, who is a member of the technical staff at Tolmo, an AI cybersecurity startup. “It’s better to catch more people than not enough when you do such a release and to relax the guardrails over time.”

Another researcher griped on X that “even asking for a code review” triggers Fable’s guardrails.

Anthropic did not immediately respond to a request for comment.

Apart from guardrails inside its models, Anthropic requires cybersecurity professionals to apply to the Cyber Verification Program. If they get approved, the applicants have fewer limitations on using Claude for cybersecurity work. OpenAI has a similar program called Trusted Access for Cyber.