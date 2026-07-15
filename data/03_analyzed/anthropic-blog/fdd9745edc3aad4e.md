---
title: Redeploying Fable 5
source: https://www.anthropic.com/news/redeploying-fable-5
author: []
published: '2026-07-01'
created: '2026-07-01'
description: ''
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: fdd9745edc3aad4e
manifest_dates:
- '2026-07-01'
- '2026-07-02'
- '2026-07-03'
- '2026-07-04'
- '2026-07-05'
- '2026-07-06'
- '2026-07-07'
- '2026-07-08'
source_type: tech_blog
tldr: 美国解除对 Claude Fable 5 的出口管制，Anthropic 于7月1日重新部署该模型
objective_summary: 美国政府对 Anthropic 的 Claude Fable 5 和 Mythos 5 实施的出口管制于6月30日解除。Anthropic
  于7月1日向全球用户重新开放 Fable 5，覆盖 Claude 平台、Claude.ai、Claude Code 和 Claude Cowork。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - Anthropic
  - Amazon
  - Microsoft
  - Google
  - AWS
  - Google Cloud
  - Microsoft Foundry
  technologies: []
  key_people: []
key_logic_flow:
- 美国政府于6月12日对 Anthropic 的 Claude Fable 5 和 Claude Mythos 5 实施出口管制，Anthropic 因无法实时核实用户国籍而暂停了所有用户的访问
- 出口管制于6月30日解除，Fable 5 于7月1日起向全球用户重新开放，覆盖 Claude 平台、Claude.ai、Claude Code 和 Claude
  Cowork
- Fable 5 在 Pro、Max、Team 及部分 Enterprise 计划中，截至7月7日每周可用额度内免费使用，之后转为按用量计费
- Mythos 5 于6月26日获美国政府批准，已恢复对部分美国组织的访问权限，Anthropic 正争取扩大 Glasswing 项目合作伙伴的访问范围
- Anthropic 与 Amazon、Microsoft、Google 等 Glasswing 合作伙伴共同制定行业共享框架，用于统一评估和修复 AI 模型越狱问题的严重性分级
- Anthropic 正在加强与美国政府在新模型预发布测试、信息共享和研究协作方面的合作
extract_result: success
impact_score:
  score: 5.5
  reason: 此事件本质为地缘政治监管事件，而非技术突破。Fable 5 早在6月9日就已发布，此次是出口管制解除后的重新部署。短期行业影响体现在三个方面：一是为前沿AI模型的出口管制建立了先例——从管制到解除仅18天，表明美国政府认可Anthropic的安全措施已达到要求；二是Anthropic与Amazon、Microsoft、Google共同制定的越狱严重性分级框架若推广开来，将改变整个行业的安全评估标准；三是影响了全球开发者对Claude模型的可用性信任。综合来看，这是一个重要的监管和行业治理事件，但并非技术范式转移，评分5.5。
sentiment: positive
developer_sentiment:
  tone: neutral
  primary_focus: Fable 5 在经历三周服务中断后恢复可用，开发者关切出口管制的反复性对模型可用性和API稳定性的长期影响
hype_assessment:
  level: low
  reason: Anthropic 的这篇文章措辞克制、事实陈述为主。没有使用'颠覆式''革命性'等 PR 滥用词汇，而是详细梳理了时间线、安全更新、行业框架和政府合作的具体内容。内容务实，水分很低。
information_entropy: medium
domain_disruption:
  technical_innovation: 无重大技术创新突破，但文中提出的跨行业越狱严重性分级框架若落地，将推动AI安全评估从各行其是走向标准化，这是工程治理层面的重要进展
  business_model: Glasswing 合作伙伴模式（政府核准+有限范围部署+行业联合安全框架）可能成为未来前沿AI模型发布的标准流程，重塑了超大规模AI模型与政府监管之间的协作关系
engineering_complexity: production_ready
compound_value:
  score: 8.0
  reason: 该事件的核心价值不在模型重新上线本身，而在于Anthropic借此建立了三重复利机制：第一，与美国政府形成深度协作关系（预发布测试、信息共享、研究协作），这种监管信任是极难复制的政治资本，将在未来模型审批中持续降低不确定性；第二，携手Amazon、Microsoft、Google三大云巨头制定越狱评估的行业共享框架，一旦成为事实标准，Anthropic将在行业安全治理中占据规则制定者地位，后来者必须适配其标准；第三，Fable
    5全球重新上线意味着用户数据飞轮重启，模型使用量的增长直接反哺安全能力提升。三点叠加形成'监管信任→行业标准→数据飞轮'的正循环，3-5年后Anthropic大概率成为AI安全治理领域不可绕过的节点。风险在于出口管制仍可被重新激活，但已建立的协作关系降低了这种概率。
value_capture_layer: foundation_model
moat_impact: creates_new_moat
key_beneficiaries:
- Anthropic
- Amazon
- Microsoft
- Google
- AWS
- Google Cloud
- Microsoft Foundry
competitive_casualty:
- 未与美国政府建立监管信任关系的中小型AI实验室
- 缺乏安全合规能力的新进入基础模型公司
market_opportunities:
- 企业可抓住Fable 5全球重新开放的窗口期，将最新Claude模型集成到跨境业务场景中，利用其增强的安全防护能力降低合规风险
- Anthropic与云厂商共建的越狱评估行业框架为AI安全审计赛道创造了标准化服务机会，第三方安全评测机构可基于此框架提供模型安全认证服务
- 出口管制合规自动化工具（实时国籍验证、模型访问地理围栏）成为刚需方向，创业者可开发面向AI公司的合规中间件产品
risk_matrix:
  regulatory: 美国政府对此类前沿模型实施出口管制的先例已确立，未来任何新发布的高能力模型都可能面临类似的突袭式管制风险，企业对该模型的长期可用性存在不确定性
  technological: Fable 5因越狱漏洞被管制的事件说明强能力模型的安全护栏仍不完善，后续版本或竞品模型若出现更严重的越狱问题可能再次触发监管干预
  competitive: Anthropic与Amazon、Microsoft、Google等云厂商深度绑定共建行业框架，可能形成由少数巨头主导的AI安全标准壁垒，挤压中小模型厂商的生存空间
  ethical: Mythos 5作为低防护版本的有限恢复暴露了AI双重用途困境——用于防御性网络安全的模型技术同样可被恶意改造用于攻击，政府深度参与模型测试也引发AI军事化担忧
  additional:
  - Glasswing项目下的政府-企业合作模式可能演变为事实上的行业准入制度，非合作方获取前沿模型能力的渠道将受挤压
confidence:
  impact: high
  compound: medium
  hype: high
actionable_insight: deep_dive
---

# Redeploying Fable 5

On Friday, June 12, the US government applied export controls to our newest models, Claude Fable 5 and Claude Mythos 5. This required us to restrict access to foreign nationals, whether inside or outside the United States. Because the order took effect immediately and we had no reliable way to verify nationality in real-time, we suspended access to both models for all users.

**As of today, June 30, the export controls on Fable 5 and Mythos 5 have been lifted.**

Fable 5 will be available starting tomorrow, Wednesday, July 1, to users globally on the Claude Platform, Claude.ai, Claude Code, and Claude Cowork. For Pro, Max, Team, and select Enterprise plans,1 Fable 5 will be included for up to 50% of weekly usage limits through July 7, after which it will be available via usage credits. We will re-enable access on AWS, Google Cloud, and Microsoft Foundry as quickly as possible.

We have also restored access to Mythos 5 for a set of US organizations, following the US government’s approval on June 26. We continue to coordinate with the government to expand access to the broader set of domestic and international partners in the Glasswing program.

In the remainder of this post, we provide further details and updates in four areas:

*A timeline of events, including updates we made to our safeguards*. We discuss the events that led to the export control directive and how we addressed it with new safeguards.*Our general approach to safeguards*. We provide more context on how we use safety classifiers to detect potentially dangerous cybersecurity uses of our models.*A shared industry framework*. Although we have reached a constructive resolution, these events have made clear that the industry needs a consistent way to assess and fix potential “jailbreaks” of AI models (techniques that bypass a model’s safeguards).2A shared standard for judging the severity of a given jailbreak would help AI developers triage new findings as they arise, launch highly capable models with greater safety, and communicate the level of risk consistently to government and industry partners. Together with Amazon, Microsoft, Google, and other Glasswing partners, we’ve started to develop such a framework, and we outline it below.*Deeper government collaboration*. We’re also strengthening our level of collaboration with the US government on new pre-release testing, information sharing, and research collaboration. We describe this deeper collaboration in the final section.

## Timeline and safeguard updates

We released Fable 5 and Mythos 5 on Tuesday, June 9. They both share the same underlying model, but Fable 5 was released with strong safeguards to make it safer for general use. Mythos 5, which has fewer safeguards, was only released to a small number of trusted Project Glasswing partners for use in defensive cybersecurity.