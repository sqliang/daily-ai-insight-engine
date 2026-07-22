---
title: Fable Safeguards Jailbreak Framework
source: https://www.anthropic.com/news/fable-safeguards-jailbreak-framework
author: []
published: '2026-07-03'
created: '2026-07-03'
description: ''
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: aaef033dfabe2831
manifest_dates:
- '2026-07-03'
- '2026-07-04'
- '2026-07-05'
- '2026-07-06'
- '2026-07-07'
- '2026-07-08'
source_type: tech_blog
tldr: Anthropic 在重新部署 Claude Fable 5 后，发布了其网络安全分类器的详细说明，并与 Glasswing 合作提出了一个 AI 越狱严重性评估框架草案，同时在
  HackerOne 上启动了安全漏洞报告项目。
objective_summary: Anthropic 在重新部署 Claude Fable 5 后，公开了该模型配套的网络安全分类器的详细说明，将网络安全使用行为分为四个类别以区分防御性和攻击性用途。同时，Anthropic
  与 Glasswing 合作发布了一个 AI 越狱严重性评估框架的早期草案，旨在为不同严重程度的越狱行为建立统一的风险描述标准。此外，Anthropic 在 HackerOne
  上启动了漏洞报告项目，邀请安全研究人员提交在 Fable 5 中发现的潜在网络越狱漏洞。
event_type: policy_and_safety
epistemic_status: verified_fact
entities:
  companies:
  - Anthropic
  - Glasswing
  technologies:
  - safety classifiers
  - AI jailbreak
  - cybersecurity safeguards
  key_people: []
key_logic_flow:
- Anthropic 在重新部署 Claude Fable 5 后，发布了其网络安全分类器的详细说明，列出了这些分类器旨在预防和未涵盖的危害类型。
- Anthropic 与 Glasswing 合作提出了一个 AI 越狱严重性评估框架草案，旨在为不同严重程度的越狱行为建立统一的风险描述标准。
- 网络安全领域对 AI 安全措施具有特殊挑战性，因为许多网络安全能力具有双重用途，既可防御也可攻击。
- Anthropic 不打算阻止 Fable 5 的所有网络安全活动，而是训练分类器区分四个类别的网络安全使用场景。
- Anthropic 在 HackerOne 上启动了漏洞报告项目，邀请安全研究员提交在 Fable 5 中发现的潜在网络越狱漏洞。
- Anthropic 希望通过与学术界、业界、公民社会和政府的讨论，建立能够实现技术防御用途同时防止滥用的标准。
extract_result: success
object_mentions:
- object_type: product
  name: Fable Safeguards
  canonical_name: Fable Safeguards
  url: https://www.anthropic.com/news/fable-safeguards-jailbreak-framework
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Anthropic 在重新部署 Claude Fable 5 后，发布了其网络安全分类器的详细说明，这些分类器用于检测和阻止危险的网络安全相关使用。
  - 这些分类器将网络安全使用分为四个类别，从最明显有潜在危害到最明显良性的用途，以区分防御性和攻击性行为。
  article_id: aaef033dfabe2831
- object_type: project
  name: AI Jailbreak Severity Framework
  canonical_name: AI Jailbreak Severity Framework
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Anthropic 与 Glasswing 合作提出了一个 AI 越狱严重性评估框架草案，旨在让 AI 开发者与政府用一致的术语讨论每次越狱的风险。
  - 该框架反映了 Anthropic 当前的思考，其目标是引发学术界、业界、公民社会和政府关于如何划定风险界限的讨论。
  article_id: aaef033dfabe2831
- object_type: project
  name: Fable 5 HackerOne Cyber Jailbreak Program
  canonical_name: Fable 5 HackerOne cyber jailbreak program
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Anthropic 在 HackerOne 上启动了一个项目，允许安全研究人员提交他们在 Fable 5 中发现的安全越狱漏洞以供审查。
  article_id: aaef033dfabe2831
impact_score:
  score: 5.5
  reason: 该事件并非技术范式突破，而是AI安全治理领域的重要标准化尝试。Anthropic公开Fable 5网络安全分类器的具体防护边界，并与Glasswing合作提出越狱严重性分级框架草案，若被业界采纳可能成为行业评估基准。但当前仍处于草案征求意见阶段，实际影响力取决于后续被监管机构和竞争对手接受的程度。短期来看属于重要但非颠覆性的安全合规事件。
sentiment: positive
developer_sentiment:
  tone: skeptical
  primary_focus: 安全分类器是否会过度限制合法网络安全用例（如渗透测试、漏洞扫描等双用途场景）
hype_assessment:
  level: low
  reason: 文章措辞克制，没有使用'颠覆性''革命性'等PR夸张词汇。明确标注框架为'early draft'（早期草案），公开邀请学术界和业界反馈批评，并详细列出了分类器阻止和不阻止的具体危害类型。整体基调是透明披露而非概念炒作。
information_entropy: medium
domain_disruption:
  technical_innovation: 提出了网络安全分类器的四级危害分级体系（从最危险到最良性），以及AI越狱严重性分级框架，为业界提供了可复用的AI安全风险评估方法论。但具体实现细节和分类阈值尚未公开，技术深度有限。
  business_model: 通过安全透明度和标准制定建立企业级信任壁垒，配合HackerOne漏洞奖励计划强化安全生态。此举有利于Anthropic在政府和企业级B2B市场构建合规性竞争优势，推动'安全即服务'的差异化定价策略。
engineering_complexity: production_ready
compound_value:
  score: 7.5
  reason: 从VC视角看，Anthropic此次动作的核心价值不在于Fable 5的重新部署，而在于其主动制定AI越狱严重性分级框架的标准化尝试。这一框架如果被学术界、产业界和监管机构广泛采纳，将产生类似CVSS（通用漏洞评分系统）在网络安全领域的基础设施效应——成为行业通行的风险沟通语言。标准一旦确立，网络效应和转换成本会形成长期复利：监管政策引用该框架、企业采购以此评估模型风险、保险产品基于该分级定价。Anthropic同时公开了安全分类器的详细设计边界（dual-use区分逻辑），这既是透明度承诺，也隐性地设定了行业安全基准的门槛。HackerOne赏金计划则构建了外部安全研究者的生态飞轮。综合来看，该事件建立了三重积累效应：品牌信任资产（安全领导者认知）、标准话语权（定义风险语言）、生态锁定（研究者+企业合规需求）。但需注意，框架仍为早期草案（'early
    draft'），尚未获得OpenAI、Google等竞争对手的背书，标准化进程存在不确定性，因此评分设定在7.5而非更高。
value_capture_layer: foundation_model
moat_impact: creates_new_moat
key_beneficiaries:
- Anthropic
- Glasswing
- HackerOne
competitive_casualty:
- OpenAI
- Google DeepMind
- Mistral AI
- 尚未建立系统化安全评估框架的AI初创公司
market_opportunities:
- 安全咨询公司可基于 Anthropic 的越狱严重性分级框架开发第三方 AI 安全评估与审计服务，帮助企业在部署大模型前评估越狱风险等级
- 企业级 AI 安全平台可集成类似的安全分类器规则引擎，为垂直行业（如金融、医疗、政务）提供定制化的网络安全防护边界配置方案
- 安全研究人员可借助 HackerOne 漏洞奖励计划积累 AI 越狱攻防经验，形成针对大模型安全测试的专项技能和工具链
risk_matrix:
  regulatory: 越狱严重性分级框架若成为行业标准，未建立对应安全评估体系的 AI 开发者可能面临合规压力；各国监管机构可能将该框架纳入 AI 法案的评估参考基准
  technological: 安全分类器与越狱攻击是持续的猫鼠游戏，公开分类器防护边界可能为攻击者提供绕过线索；框架目前仅为草案，分级标准和分类方法可能随后续反馈大幅调整
  competitive: 主要 AI 厂商可能各自推出不同的安全分类标准和越狱分级体系，导致行业碎片化，增加跨平台部署的合规成本；Anthropic 率先定义标准可能获得先发优势，挤压后来者话语权
  ethical: 安全分类器公开详述了不予防范的危害类型，可能被恶意行为者利用来规避检测；网络安全能力的双重用途（dual use）本质使得严格区分善意与恶意使用的边界在实际操作中存在伦理模糊地带
  additional: []
confidence:
  impact: high
  compound: medium
  hype: low
actionable_insight: strategic_invest
object_insights:
- object_type: product
  name: Fable Safeguards
  canonical_name: Fable Safeguards
  url: https://www.anthropic.com/news/fable-safeguards-jailbreak-framework
  positioning: Anthropic 为 Claude Fable 5 配备的网络安全分类器系统，通过四类别分类法区分防御性与攻击性网络安全使用行为。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - AI 安全研究人员
  - 网络安全防御团队
  - Claude Fable 5 企业用户
  product_signal: Fable Safeguards 将网络安全使用行为分为四个类别，从最明显有潜在危害到最明显良性用途，以区分防御性和攻击性行为。
  market_signal: Anthropic 在重新部署 Fable 5 后公开网络安全分类器细节，体现了模型安全透明度的持续提升。
  differentiation: 不同于全面封锁网络安全活动的传统做法，Fable Safeguards 采用四类别分类法实现精准管控而非一刀切。
  watch_reason: Fable Safeguards 代表了 AI 安全领域的前沿实践，其四类别分类法为行业树立了双重用途技术管控的标杆，值得持续跟踪以观察行业采纳和后续迭代方向。
  risk_notes:
  - 网络安全领域的双重用途特性使得分类器难以做到完美区分，可能存在误判和绕过的风险。
  score: 8.0
  article_ids:
  - aaef033dfabe2831
  evidence_snippets:
  - Anthropic 在重新部署 Claude Fable 5 后，发布了其网络安全分类器的详细说明，这些分类器用于检测和阻止危险的网络安全相关使用。
  - 这些分类器将网络安全使用分为四个类别，从最明显有潜在危害到最明显良性的用途，以区分防御性和攻击性行为。
- object_type: project
  name: AI Jailbreak Severity Framework
  canonical_name: AI Jailbreak Severity Framework
  url: null
  positioning: 由 Anthropic 与 Glasswing 合作提出的 AI 越狱严重性评估框架草案，旨在为不同严重程度的越狱行为建立统一的风险描述标准。
  technical_signal: 该框架提出了 AI 越狱严重性的标准化评估方法，旨在让 AI 开发者与政府用一致的术语描述每次越狱的风险等级。
  adoption_signal: null
  ecosystem_relevance: 该框架旨在引发学术界、业界、公民社会和政府关于如何划定 AI 越狱风险界限的讨论，推动行业统一标准的建立。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 该框架是行业中少有的针对 AI 越狱严重性的标准化尝试，如能推动行业共识，将对 AI 安全监管和模型防护策略产生深远影响，值得持续关注其迭代与采纳进程。
  risk_notes:
  - 该框架目前仅为早期草案，尚需学术界、业界和政府广泛讨论才能形成行业共识，不确定性较高。
  score: 7.0
  article_ids:
  - aaef033dfabe2831
  evidence_snippets:
  - Anthropic 与 Glasswing 合作提出了一个 AI 越狱严重性评估框架草案，旨在让 AI 开发者与政府用一致的术语讨论每次越狱的风险。
  - 该框架反映了 Anthropic 当前的思考，其目标是引发学术界、业界、公民社会和政府关于如何划定风险界限的讨论。
- object_type: project
  name: Fable 5 HackerOne Cyber Jailbreak Program
  canonical_name: Fable 5 HackerOne cyber jailbreak program
  url: null
  positioning: Anthropic 在 HackerOne 上启动的安全漏洞报告项目，邀请安全研究人员提交在 Fable 5 中发现的安全越狱漏洞以供审查。
  technical_signal: Anthropic 在 HackerOne 上启动了专门的安全漏洞报告项目，为发现 Fable 5 越狱漏洞的研究人员提供了官方提交与审查渠道。
  adoption_signal: null
  ecosystem_relevance: 该项目为安全研究社区提供了正式渠道与 Anthropic 协作发现 AI 安全漏洞，有助于构建更广泛的 AI 安全防御生态。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 作为 AI 安全领域的官方漏洞报告项目，其运行效果和发现的真实越狱案例将为行业提供重要的安全实践参考和风险基线，值得持续跟踪其运行成果。
  risk_notes:
  - 该项目依赖于安全研究社区的参与积极性，漏洞报告的质量和响应效率尚需在实践中验证。
  score: 6.0
  article_ids:
  - aaef033dfabe2831
  evidence_snippets:
  - Anthropic 在 HackerOne 上启动了一个项目，允许安全研究人员提交他们在 Fable 5 中发现的安全越狱漏洞以供审查。
---

# More details on Fable 5’s cyber safeguards and our jailbreak framework

Claude Fable 5 has been re-deployed and is now available globally for all users. We’re taking this opportunity to share further information in two areas.

First, we provide more information on the **cybersecurity safeguards**—specifically, the *safety classifiers*—that we launched with the model. These are the AI systems that accompany the model that detect and block dangerous (or potentially dangerous) cybersecurity uses. Here, we provide a detailed list of the types of harms Fable 5’s classifiers are, and are not, designed to prevent.

Second, we lay out an early draft version of **our proposed AI jailbreak severity framework**, on which we’ve been working with our Glasswing partners. AI jailbreaks are unusual ways of prompting an AI model to bypass its safeguards, thus unblocking the behaviors (like dangerous or potentially dangerous cybersecurity tasks) we seek to prevent.

Jailbreaks vary in severity: sometimes they only unblock minor undesirable behaviors, and sometimes they unblock a wide range of harmful outputs, making a model much more dangerous. Yet there is no agreed-upon framework for describing a given jailbreak’s severity. Such a framework would allow AI developers to speak to governments (and vice versa) in consistent terms about the risks posed by each jailbreak.

What we’re sharing today reflects our current thinking. Our hope is to spark a helpful discussion across academia, industry, civil society, and government about how and where these lines should be drawn. We welcome feedback and critique on this framework at cyber-safeguards@anthropic.com. We’ve also launched a HackerOne program where security researchers can submit potential cyber jailbreaks they discover in Fable 5 for our review.

We believe that by working together, we can establish a standard that enables the defensive uses of this technology while preventing its misuse.

## Fable 5’s cyber safeguards

Areas such as cybersecurity are particularly challenging for AI safeguards because they are often *dual use*. That is, many cybersecurity capabilities can be used for benign *or* harmful purposes. For example, we want to allow cyber defenders to use our models to scan their codebases to find software vulnerabilities—but this same capability could, in the wrong hands, be the precursor to a cyberattack.

For that reason, we do not intend to block *all* cybersecurity-related activities for Fable 5. Instead, we train our safety classifiers to discern between four categories of cybersecurity use, from the most clearly potentially dangerous to the most clearly potentially benign. These are summarized in the table below: