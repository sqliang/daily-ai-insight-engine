---
title: Cybersecurity researchers aren’t happy about the guardrails on Anthropic’s
  Fable
source: https://techcrunch.com/2026/06/10/cybersecurity-researchers-arent-happy-about-the-guardrails-on-anthropics-fable/
author:
- '[[Lorenzo Franceschi-Bicchierai]]'
published: '2026-06-10'
created: '2026-06-11'
description: Cybersecurity researchers are complaining that Anthropic's new model
  Fable has guardrails that are too strict for any cybersecurity work.
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: c3ab8c2b1dbfd6f4
source_type: news_media
tldr: Anthropic 发布 Fable，因过度限制网络安全话题遭研究人员批评
objective_summary: Anthropic 于周二发布 Fable 模型（Mythos 的受限公开版），内置针对网络安全和生物学的安全护栏导致大量正常请求被拒绝，多位安全研究员公开表达不满。Fable
  在触发护栏时会降级回退到 Claude Opus 4.8。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - Anthropic
  - IBM X-Force
  - Tolmo
  - TechCrunch
  technologies:
  - Fable
  - Mythos
  - Claude Opus 4.8
  key_people:
  - Valentina "Chompie" Palmiotti
  - Matt Suiche
  - Lorenzo Franceschi-Bicchierai
key_logic_flow:
- Anthropic 于周二发布 Fable 模型，将其定位为网络安全模型 Mythos 的受限公开版。
- Fable 内置了基于关键词的安全护栏，任何与网络安全或生物学相关的话题（包括阅读博客、代码审查等无害任务）都会被拒绝，并提示"安全措施标记了此消息"。
- 当触发护栏时，Fable 会自动降级回退到 Claude Opus 4.8 模型。
- IBM X-Force 安全研究员 Valentina Palmiotti 表示 Fable 甚至拒绝"阅读博客文章"这一类无害请求。
- Tolmo 安全研究员 Matt Suiche 指出护栏基于关键词匹配，"网络安全"词域内的任何内容都会触发限制，但同时表示早期阶段收紧限制比放松更合理，护栏预计会逐步进化。
- Mythos 于今年 4 月通过 Project Glasswing 以有限范围发布，上周已扩展至 15 个国家的数百个组织。
impact_score:
  score: 6.0
  reason: Anthropic 发布 Fable 作为 Mythos 的受限公开版，是 AI 安全模型从企业内测走向公众的重要一步。然而，关键词匹配的安全护栏过度拦截正常安全研究任务（如代码审查、阅读博客），引发网络安全研究社区的公开不满。这一事件加剧了业界对'AI
    安全 vs. 实用性'权衡的讨论，短期内会影响安全从业者对 Anthropic 模型的信任和使用意愿，可能促使其他 AI 公司在发布安全模型时重新评估护栏策略。事件本身并非范式转移，但作为头部
    AI 公司的产品发布+社区争议，足以在局部竞争格局中产生显著影响。
sentiment: negative
developer_sentiment:
  tone: frustrated
  primary_focus: 基于关键词的安全护栏过度拦截，连代码审查和阅读博客等正常安全研究任务都被拒绝，且降级回退到旧模型 Claude Opus 4.8
hype_assessment:
  level: medium
  reason: Anthropic 将 Fable 定位为 Mythos 的'受限公开版'，本身带有 PR 包装色彩——'强大且备受关注'等描述暗示了 Marketing
    导向。但 TechCrunch 报道提供了具体研究者证言（引用 IBM X-Force 和 Tolmo 研究员），以及护栏触发机制的技术细节（关键词匹配、降级回退），并非空洞概念炒作。存在一定包装成分，但有真实用户反馈和数据支撑。
information_entropy: medium
domain_disruption:
  technical_innovation: Fable 本身并非技术突破，而是 Mythos 的安全过滤版本。其关键词匹配的护栏系统在触发时降级回退到 Claude
    Opus 4.8，技术架构上属于安全部署层面的约束，而非模型能力创新。这一设计暴露了当前 AI 安全护栏粗糙（关键词而非语义理解）的技术局限性。
  business_model: Anthropic 通过'有限公开版'策略（Fable）逐步扩大 Mythos 的覆盖面，从 Glasswing 项目的数百家组织扩展到公众，展示了
    AI 安全模型在受限条件下商业化的路径——先企业内测再有限公测，逐步放宽安全约束。这种'渐进式开放'可能成为高风险 AI 模型发布的行业范式。
engineering_complexity: production_ready
compound_value:
  score: 7.5
  reason: Anthropic 正在构建垂直领域（网络安全）专用模型的双层策略——Mythos（受限企业版）和 Fable（公开版），这是基础模型公司从通用向行业专用化转型的关键信号。从复利视角看：第一，网络安全
    AI 市场规模大（全球数百亿美元的端点安全、威胁检测市场），且安全团队的付费意愿极强，Mythos 已在 15 国数百组织部署，验证了产品-市场契合度；第二，Anthropic
    借此建立了垂直领域数据飞轮——Project Glasswing 的真实安全用例反馈持续优化模型，形成技术与数据的双重护城河积累；第三，当前护栏争议本质是'早期必然的矫枉过正'，安全研究员
    Matt Suiche 明确表示'早期阶段收紧比放松更合理，护栏会逐步进化'，说明社区对渐进式解禁有合理预期；第四，该模式具有平台化扩展潜力——Mythos
    的行业专用化方法论可复制到生物、法律、金融等高风险垂直领域。3-5 年后，Anthropic 在行业专用基础模型领域的先发优势大概率成为其第二增长曲线核心支柱。扣分点：护栏收敛速度存在不确定性；Mythos
    的实际安全效果（能否真正阻止攻击）仍需更长时间验证；关键词匹配式的护栏机制显得粗糙，可能影响开发者信任。
value_capture_layer: foundation_model
moat_impact: creates_new_moat
key_beneficiaries:
- Anthropic
- Tolmo
- Project Glasswing 合作组织
competitive_casualty:
- 小型 AI 安全初创公司
- 缺乏 AI 能力的传统安全厂商
market_opportunities:
- 创业公司可开发针对网络安全垂直领域的精细微调模型，填补 Anthropic Fable 因过度限制留下的安全编码与代码审查需求空白
- 市场对智能安全护栏的需求明确——有机会构建基于语义理解而非关键词匹配的分级安全系统，既能防止滥用又不误伤正常安全研究
- AI 模型降级回退机制（Fable→Claude Opus 4.8）催生模型路由和分级推理编排工具的创业空间
risk_matrix:
  regulatory: Anthropic 的保守策略虽降低了滥用风险，但过度限制可能引发消费者权益或反竞争方面的关注；若未来各国出台 AI 安全法规，类似关键词匹配的粗放式护栏可能被要求达到更高精度标准
  technological: 基于关键词匹配的护栏技术相对粗糙，容易被针对性绕过（如改述或使用专业术语变体），同时过度拦截会驱动用户转向无此类限制的开源模型或竞品
  competitive: OpenAI、Google 等竞争对手可能推出面向网络安全场景的精细化受限模型，Anthropic 的过度限制策略可能将核心安全研究用户群推向竞品
  ethical: 过度拦截网络安全研究请求（如阅读博客、代码审查）实际上削弱了 AI 助力防御的能力，在防止滥用的同时可能对社会整体安全态势产生反效果
  additional:
  - Anthropic 的品牌声誉风险——安全研究社区是 AI 安全领域的关键利益相关方，疏远该群体可能影响未来合作与模型采纳
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