---
title: Claude Code砸的坑，蚂蚁安全在尝试填上
source: https://www.qbitai.com/2026/07/448925.html
author:
- '[[鹭羽]]'
published: '2026-07-13'
created: '2026-07-13'
description: 最新开源两大安全框架
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: ae70b2debe6cd076
source_type: news_media
tldr: 蚂蚁集团开源了SingGuard-NSFA和SingGuard两大AI安全框架，分别面向智能体行为安全和多模态大模型感知安全。SingGuard-NSFA采用生成式推理与判别式分类头双模式，在三大评测基准上取得SOTA；SingGuard将安全规则作为运行时输入，通过RI-Mask实现多模态推理提速5倍以上。此举标志着行业从漏洞修补转向安全底层框架建设。
objective_summary: 蚂蚁集团AI安全实验室近期开源了两大安全框架：面向智能体安全的SingGuard-NSFA和面向多模态大模型的SingGuard。SingGuard-NSFA提供0.8B至9B四种尺寸，采用SFT生成式推理与判别式分类头双模式拦截，判别式延迟低至45至57毫秒，在用户请求安全、模型响应安全和跨数据集泛化三大评测基准上均取得SOTA。SingGuard提供0.8B至8B四种尺寸，将安全规则作为运行时输入，支持快慢思考分工与early
  exit自动切换，并提出了RI-Mask技术使多模态推理效率最高提升5倍以上。此前蚂蚁AI安全实验室曾发现OpenClaw多个高危漏洞并协助修复，还与清华大学联合开源了覆盖智能体全生命周期的ClawAegis安全方案。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - 蚂蚁集团
  - 蚂蚁AI安全实验室
  - 清华大学
  - 工信部NVDB
  - 信通院泰尔实验室
  technologies:
  - SingGuard-NSFA
  - SingGuard
  - ClawAegis
  - NSFA风险分类体系
  - RI-Mask
  - SFT
  - Llama Guard 3
  - OWASP
  - CIA三元组
  key_people: []
key_logic_flow:
- 工信部NVDB平台发布风险预警，指出Claude Code存在安全后门隐患，可在用户不知情的情况下收集敏感信息。
- 蚂蚁AI安全实验室此前曾发现OpenClaw等多个Agent产品的高危漏洞并协助官方修复，随后与清华大学联合开源了ClawAegis智能体全生命周期安全方案。
- 蚂蚁集团近期开源了两大安全框架：面向智能体行为安全的SingGuard-NSFA和面向多模态大模型感知安全的SingGuard。
- SingGuard-NSFA以CIA三元组为理论底座结合OWASP实践经验构建NSFA风险分类体系，通过SFT生成式推理与判别式分类头双模式拦截风险，其中判别式延迟低至45至57毫秒。
- SingGuard-NSFA在三大评测基准上均取得SOTA，最小的0.8B模型即可比肩8B竞品，9B版本在泛化任务上达到91.29%的F1值。
- SingGuard将安全规则作为运行时输入，不同业务域可现场下发各自红线，并采用快慢思考分工与early exit自动切换机制，RI-Mask技术使多模态推理最高提速5倍以上。
extract_result: success
object_mentions:
- object_type: project
  name: SingGuard-NSFA
  canonical_name: SingGuard-NSFA
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 蚂蚁开源了面向智能体安全的双模推理护栏框架SingGuard-NSFA，包括0.8B、2B、4B、9B四个尺寸版本。
  - SingGuard-NSFA采用SFT生成式推理与判别式分类头双模式同步进行风险拦截，判别式模式延迟可压到45至57毫秒。
  - SingGuard-NSFA在用户请求安全、模型响应安全和跨数据集泛化三大评测基准上均取得SOTA，最小的0.8B模型就能比肩8B竞品。
  article_id: ae70b2debe6cd076
- object_type: project
  name: SingGuard
  canonical_name: SingGuard
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 蚂蚁开源了面向多模态大模型的安全框架SingGuard，同样包括0.8B、2B、4B、8B四个尺寸版本。
  - SingGuard将安全规则做成运行时输入，不同业务域可以现场下发各自的红线，模型据此逐条判定。
  - 蚂蚁提出了RI-Mask技术让共享的图文上下文只编码一次，多条规则并行判断，多模态推理最高可提速5倍以上。
  article_id: ae70b2debe6cd076
- object_type: project
  name: ClawAegis
  canonical_name: ClawAegis
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 蚂蚁与清华大学联合开源了ClawAegis，为智能体提供了一套覆盖产品全生命周期的安全方案。
  article_id: ae70b2debe6cd076
- object_type: product
  name: Claude Code
  canonical_name: Claude Code
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 工信部NVDB平台发布风险预警，明确指出Claude Code存在安全后门隐患，可在用户不知情的情况下收集敏感信息。
  article_id: ae70b2debe6cd076
- object_type: project
  name: OpenClaw
  canonical_name: OpenClaw
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 年初红遍全网的OpenClaw屡屡被曝出高危险漏洞，蚂蚁AI安全实验室曾发现其多个高危漏洞并协助官方完成修复。
  article_id: ae70b2debe6cd076
- object_type: project
  name: Llama Guard 3
  canonical_name: Llama Guard 3
  url: null
  confidence: low
  article_role: ecosystem_context
  evidence_snippets:
  - 文章提到给Llama Guard 3额外增加一个分类头，用户请求安全基准的F1值可直接提升17.6个百分点。
  article_id: ae70b2debe6cd076
impact_score:
  score: 7.5
  reason: 评分依据：这是一次重要的AI安全基础设施级开源事件，影响面广且时机精准。首先，事件背景是Claude Code后门漏洞和OpenClaw高危漏洞接连曝光，整个行业对AI
    Agent安全的焦虑达到峰值，蚂蚁此时开源两大安全框架正好切入行业最大痛点。其次，框架设计并非花架子——SingGuard-NSFA的NSFA分类体系基于CIA三元组+OWASP指南构建了系统性方法论，双模推理（生成式45-57ms+判别式链式推理）兼顾了实时性和可解释性，冻结骨干+轻量分类头的架构实现了原生可扩展，0.8B模型比肩8B竞品的效率优势也意味着部署门槛极低。再者，这不是孤立发布，而是蚂蚁从漏洞挖掘（OpenClaw等多个高危漏洞）到ClawAegis联合开源再到本次框架开源的体系化布局的一环，可信度较高。SingGuard的RI-Mask实现多模态推理5倍加速也是工程亮点。综合来看，这两套框架有潜力成为AI
    Agent安全领域的事实标准参考实现，改变局部竞争格局，但尚未达到ChatGPT发布或Transformer论文那种范式转移级别（缺乏理论突破，更多是工程集成创新），因此评分落在7.5。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 冻结骨干+轻量分类头的可扩展架构，新增风险只需补训小头而不影响已有检测能力
hype_assessment:
  level: medium
  reason: 判定依据：文章存在一定PR包装——标题和正文使用了'扼杀在摇篮之中''重新定义安全边界''安全基础设施'等稍显夸张的表述。但核心信息是扎实的：给出了具体可验证的技术指标（0.8B/2B/4B/9B四个尺寸、判别式45-57ms延迟、9B模型泛化F1
    91.29%、RI-Mask 5倍加速），并且引用了工信部NVDB、信通院泰尔实验室等第三方权威机构作为佐证。NSFA分类体系基于CIA+OWASP的方法论也是可追溯的。需要警惕的是SOTA声明是蚂蚁自身公布的，有待独立第三方复现验证。总体属于'有一定包装但干货占主体'的中等炒作水平。
information_entropy: high
domain_disruption:
  technical_innovation: 双模推理架构的设计突破：生成式模式通过链式推理输出基于NSFA定义的可解释风险分析（适用于离线合规审计），判别式模式通过单次前向传播直接输出各风险域置信度（45-57ms延迟，适用于实时在线拦截），两者共享同一冻结骨干网络。新增风险类型时仅需补训外挂的轻量分类头，无需重新训练整个模型，这显著降低了安全框架的维护成本。SingGuard将安全规则作为运行时输入的设计让不同业务域可以现场下发各自的红线规则，结合RI-Mask技术（图文上下文一次编码+多条规则并行判定）实现多模态推理5倍以上提速。此外，框架可作为插件接入现有系统（如给Llama
    Guard 3额外增加一个分类头即可提升F1 17.6个百分点），大幅降低了迁移成本。
  business_model: 蚂蚁选择全面开源两大安全框架，走的是'定义行业标准基础设施'的路线。类似于OWAMP在Web安全领域建立分类体系后被行业广泛采纳，蚂蚁的NSFA分类体系若被AI
    Agent开发者社区接受为参考标准，蚂蚁将在AI安全标准制定中获得话语权。商业模式上可能通过企业级支持服务、定制化分类头训练、安全审计与合规认证服务、以及企业版增强功能实现变现。对于蚂蚁自身而言，作为金融科技公司，开源安全框架能够降低整个AI生态的安全风险，间接提升用户对蚂蚁AI产品的信任度，这是一种'安全即基础设施'的战略布局。
engineering_complexity: production_ready
compound_value:
  score: 7.8
  reason: SingGuard-NSFA 和 SingGuard 瞄准的是 AI Agent 爆发时代最核心的刚性基础设施——行为安全与多模态安全。价值逻辑如下：(1)
    NSFA 分类体系有潜力成为智能体安全领域的行业标准，类似 OWASP 在 Web 安全的地位，一旦被广泛采用将产生强烈的网络效应和转换成本；(2) 骨干网络冻结+轻量分类头的可扩展架构，使新风险类型的适配成本极低，在
    Agent 风险快速演变的窗口期这是关键的架构优势，意味着 Ant Group 可以比竞品更快覆盖新漏洞；(3) 0.8B 模型比肩 8B 竞品的效率优势，使其在边缘端和实时拦截场景具备显著的部署壁垒。从
    Ant Group 的持续布局（漏洞挖掘→ClawAegis 全生命周期方案→SingGuard 框架）看，这不是单点产品而是系统性基础设施战略，安全能力在内部本就是一条持续演进的技术路径。主要风险在于：(a)
    开源限制了直接货币化能力，需观察企业版/MaaS 变现路径；(b) AI 安全标准尚未收敛，Meta（Llama Guard）、OpenAI 等巨头可能推出竞争方案；(c)
    蚂蚁作为中国公司的地缘因素可能限制全球开发者社区的 adoption。综合评估，具备成为 AI Agent 安全层基础设施的潜力，但需持续验证行业标准收敛方向和商业闭环能力。
value_capture_layer: agent_middleware
moat_impact: creates_new_moat
key_beneficiaries:
- 蚂蚁集团(Ant Group)
- Anthropic(Claude Code生态)
- 清华大学
- 企业级AI Agent开发者
competitive_casualty:
- 传统内容安全厂商
- 商业闭源AI安全护城河产品
- 单点补丁式AI防护方案
market_opportunities:
- 企业级AI Agent产品团队可集成SingGuard-NSFA作为安全前置拦截层，在金融、医疗、企业自动化等强监管场景中构建合规防线，缩短自研安全模块的研发周期
- 基于SingGuard的可扩展分类头设计，安全服务商可针对垂直行业（如政务、电商、教育）开发定制化的风险分类微调方案，提供"框架+行业规则包"的增值服务
- 从漏洞修补到安全框架的范式转移催生了AI安全审计与合规咨询的新赛道，创业者可围绕NSFA分类体系为企业提供Agent行为安全的评估、审计与加固服务
risk_matrix:
  regulatory: SingGuard-NSFA以CIA三元组和OWASP指南为基础构建分类体系，但不同国家/地区的AI监管标准存在差异（如欧盟AI Act的高风险分类、中国生成式AI管理办法），框架的跨地域合规适配可能面临挑战；若框架本身被用于内容审查过度，可能引发新的合规争议
  technological: 骨干网络冻结+轻量分类头的设计虽实现了可扩展性，但风险分类体系的完备性依赖持续更新；若NSFA分类体系未能及时覆盖新型攻击手段（如prompt注入变种、工具滥用新形态），框架的防护有效性将随时间衰减；开源替代品可能出现性能更优的方案
  competitive: 微软、Google、AWS等云巨头及传统安全厂商（如Palo Alto Networks、Zscaler）可能快速跟进推出竞品框架，蚂蚁在AI安全领域的先发优势窗口有限；开源生态中可能分化出多个同类框架导致标准碎片化
  ethical: 行为安全框架若部署不当可能导致过度拦截，限制智能体的正常功能发挥，影响用户体验和工作效率；多模态安全规则作为运行时输入的设计若被滥用，可能成为大规模内容过滤和言论管控的工具，引发隐私与表达自由的伦理争议
  additional:
  - 框架依赖预定义风险分类体系的完备性，当出现分类体系未覆盖的新型风险时存在防护盲区；0.8B小模型虽宣称比肩8B竞品，但实际生产环境的长尾风险检出效果仍需大规模实测验证
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: deep_dive
object_insights:
- object_type: project
  name: SingGuard-NSFA
  canonical_name: SingGuard-NSFA
  url: null
  positioning: 面向智能体行为的双模推理护栏框架，以CIA三元组为理论底座结合OWASP实践构建NSFA风险分类体系，通过生成式推理与判别式分类头双模式实现风险前置拦截。
  technical_signal: 采用SFT生成式推理与判别式分类头双模式同步拦截风险，判别式延迟低至45至57毫秒，骨干网络冻结使新增风险仅需补训轻量分类头即可扩展。
  adoption_signal: 最小的0.8B模型即可比肩8B竞品，9B版在泛化任务上达91.29% F1值，降低了各规模团队的部署门槛。
  ecosystem_relevance: 作为开源框架可嵌入已有Agent体系，兼容Llama Guard等方案，给Llama Guard增加分类头后用户请求安全F1提升17.6个百分点。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 蚂蚁作为支付与风控安全领域长期积累的公司，将AI安全从被动漏洞修补升级到底层框架建设，SingGuard-NSFA在三大评测基准上均取得SOTA，其可扩展架构应对新型风险的能力值得持续跟踪。
  risk_notes:
  - 框架效果验证主要基于蚂蚁自建评测基准，缺乏第三方独立评估机构的大规模复现验证。
  - 当前仅覆盖智能体行为安全，与多模态安全框架SingGuard的协同边界尚不清晰。
  score: 8.0
  article_ids:
  - ae70b2debe6cd076
  evidence_snippets:
  - 蚂蚁开源了面向智能体安全的双模推理护栏框架SingGuard-NSFA，包括0.8B、2B、4B、9B四个尺寸版本。
  - SingGuard-NSFA采用SFT生成式推理与判别式分类头双模式同步进行风险拦截，判别式模式延迟可压到45至57毫秒。
  - SingGuard-NSFA在用户请求安全、模型响应安全和跨数据集泛化三大评测基准上均取得SOTA，最小的0.8B模型就能比肩8B竞品。
- object_type: project
  name: SingGuard
  canonical_name: SingGuard
  url: null
  positioning: 面向多模态大模型感知安全的开源框架，将安全规则作为运行时输入支持动态下发，通过快慢思考分工与RI-Mask技术实现多模态高效安全审核。
  technical_signal: 将安全规则作为运行时输入，支持不同业务域现场下发红线；快慢思考分工与early exit自动切换；RI-Mask使多模态推理最高提速5倍以上。
  adoption_signal: RI-Mask技术使多模态推理最高提速5倍以上，降低了多模态安全审核的性能门槛，有利于大规模部署。
  ecosystem_relevance: 开源方式提供，规则作为运行时输入的设计使其可灵活适配不同业务场景的安全需求，推动多模态安全基础设施标准化。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 多模态AI应用快速增长，感知层安全风险日益突出，SingGuard将安全规则动态化的创新思路和RI-Mask带来的5倍推理加速在行业中有较强的差异化价值。
  risk_notes:
  - 规则作为运行时输入的设计依赖业务方制定高质量安全规则，规则质量直接影响防护效果。
  - 多模态场景下的安全攻击手段仍在快速演化，框架对新攻击模式的覆盖度待验证。
  score: 7.0
  article_ids:
  - ae70b2debe6cd076
  evidence_snippets:
  - 蚂蚁开源了面向多模态大模型的安全框架SingGuard，同样包括0.8B、2B、4B、8B四个尺寸版本。
  - SingGuard将安全规则做成运行时输入，不同业务域可以现场下发各自的红线，模型据此逐条判定。
  - 蚂蚁提出了RI-Mask技术让共享的图文上下文只编码一次，多条规则并行判断，多模态推理最高可提速5倍以上。
- object_type: project
  name: ClawAegis
  canonical_name: ClawAegis
  url: null
  positioning: 蚂蚁与清华大学联合开源的智能体全生命周期安全方案，覆盖从开发、部署到运行的系统化安全防护。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: 作为学术与产业合作的成果，连接清华大学研究能力与蚂蚁安全工程实践，与SingGuard-NSFA共同构成蚂蚁AI安全体系的互补组件。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 与SingGuard-NSFA形成互补——ClawAegis覆盖智能体全生命周期安全，两者组合构成蚂蚁AI安全布局从漏洞挖掘到底层框架建设的完整图景。
  risk_notes:
  - 文章中对ClawAegis的技术细节描述较少，其实际能力和边界需更多独立信息验证。
  score: 5.0
  article_ids:
  - ae70b2debe6cd076
  evidence_snippets:
  - 蚂蚁与清华大学联合开源了ClawAegis，为智能体提供了一套覆盖产品全生命周期的安全方案。
- object_type: product
  name: Claude Code
  canonical_name: Claude Code
  url: null
  positioning: Anthropic推出的AI编程代理产品，被工信部NVDB平台发布安全后门风险预警，可在用户不知情的情况下收集敏感信息。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - AI开发者
  - 软件工程师
  product_signal: 具备AI代码生成与执行能力的编程代理产品，但被工信部NVDB平台指出存在可在用户不知情下收集敏感信息的安全后门隐患。
  market_signal: 作为AI编程助手头部产品被国家级漏洞平台发布风险预警，引发市场对Agent产品安全可信度的广泛讨论和监管关注。
  differentiation: 与OpenClaw等Agent产品共同面临安全漏洞频发的行业性挑战，其被官方预警点名反映了AI编程代理安全设计的普遍不足。
  watch_reason: Claude Code作为AI编程代理的代表性产品被官方安全预警点名，反映了Agent产品从功能创新到安全可信之间的鸿沟，其后续安全整改将影响整个AI编程助手品类的信任重建。
  risk_notes:
  - 工信部NVDB明确指出的安全后门隐患可能导致企业用户信任下降和采购决策收紧。
  - 被国内监管机构点名可能影响其在中国市场的可用性和合规进程。
  score: 6.0
  article_ids:
  - ae70b2debe6cd076
  evidence_snippets:
  - 工信部NVDB平台发布风险预警，明确指出Claude Code存在安全后门隐患，可在用户不知情的情况下收集敏感信息。
- object_type: project
  name: OpenClaw
  canonical_name: OpenClaw
  url: null
  positioning: 开源的AI Agent产品框架，年初因多个高危漏洞被广泛关注，蚂蚁AI安全实验室曾协助其完成漏洞修复。
  technical_signal: null
  adoption_signal: 年初红遍全网，获得较大规模开发者关注和使用，但随后频繁曝出高危漏洞影响信任度。
  ecosystem_relevance: 作为开源Agent框架，其漏洞发现与修复过程推动了Agent安全生态的成熟，也为ClawAegis等安全方案的出现提供了实践基础。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 作为Agent安全问题的典型案例，OpenClaw的漏洞从发现到修复的完整链条反映了开源Agent框架安全治理的演进路径，对行业有警示和借鉴意义。
  risk_notes:
  - 多次曝出高危漏洞反映Agent框架在基础安全设计上尚不成熟。
  - 该文中仅作为背景引用，OpenClaw最新安全状态和发展动态需进一步核实。
  score: 4.0
  article_ids:
  - ae70b2debe6cd076
  evidence_snippets:
  - 年初红遍全网的OpenClaw屡屡被曝出高危险漏洞，蚂蚁AI安全实验室曾发现其多个高危漏洞并协助官方完成修复。
---

# Claude Code砸的坑，蚂蚁安全在尝试填上

最新开源两大安全框架

鹭羽 发自 凹非寺

量子位 | 公众号 QbitAI


2026年，AI安全终于被推到了台前。

就在前两天，工信部NVDB平台发布风险预警，明确指出**Claude Code存在**安全后门隐患，可在用户不知情的情况下收集敏感信息。

时间线拨回更早，年初红遍全网的**OpenClaw**也屡屡被曝出高危险漏洞。

从横空出世到快速普及，再到漏洞频发、信任受损，这几乎是当前Agent产品共同的发展轨迹。

现在的AI能力是越来越大了，但闯出的祸也跟滚雪球似的。

滥用工具、恶意代码生成、提示注入等诸如此类的行为风险，早已不是一两个补丁就能彻底解决的。

面对新的风险形态，一个越来越明显的趋势是，行业开始把注意力从“漏洞修补”转向“安全框架”本身。

最近蚂蚁开源的**SingGuard-NSFA**和**SingGuard**，就是其中比较值得关注的一次尝试。

前者看住智能体的行为，后者看住多模态大模型的感知。

其目的也很明确，就是在AI动手之前，将安全风险扼杀在摇篮之中。

之所以聊到这个项目，也是因为它的背景比较有意思。做这个框架的团队来自**蚂蚁**，一家在安全领域拥有长期积累的公司。

先是支付安全、风控体系，再到如今的AI安全，安全能力在这家公司内部本身就是一条持续演进的技术路径。

# AI安全，正在换一套打法

其实OpenClaw也好，Claude Code也罢，它们的背后都指向同一个事实：**风险的源头，已经从内容变成了行为本身。**

过去做AI安全，本质还是互联网时代的那套打法，只需要紧盯模型输出完成内容审核即可。

但大模型早就不满足于聊天了，调工具、跑代码，它的手越伸越长，能触及的风险自然也越来越多。

光盯着模型说什么，显然不够，现在真正的问题是还要看**模型做了什么**。

偏偏这一块，是传统内容安全分类体系无法企及的盲区。

在此基础之上，多模态也来横插一脚。现在风险不止于文本，还可能藏在图像细节、图文组合，甚至模型自己的响应中。

更棘手的是，不同业务的安全红线也在持续动态变化，昨天合规，今天换个场景就可能踩线。

已知风险平时靠打打补丁还能勉强应付，所谓兵来将挡水来土掩，那么未知风险和不断变化的规则又如何解决呢？

所以答案很清晰了，单靠打补丁抑制风险是治标不治本，行业缺的不是一个又一个补丁，归根结底是一套能定义安全边界、应对未知风险和规则变动的**底层框架**。

# 两套框架，一个方向

蚂蚁安全最近开源的两大安全框架，就是冲着这个底层问题来的。

先看面向智能体安全的双模推理护栏框架**SingGuard-NSFA**，包括0.8B、2B、4B、9B四个尺寸。

它的核心思想是把安全检查前置到智能体执行之前，然后在请求拦截和响应兜底两端同时设卡，共同发力把防线从文本合规推进到行为安全。

支撑起这个判断的，是一套系统性的**NSFA风险分类体系**和**多语种评测基准**。

蚂蚁以经典的CIA三元组，也就是机密性、完整性、可用性为理论底座，再结合三份OWASP大模型与智能体安全指南的实践经验，把智能体可能出现的风险依次拆解排列。

然后借助SFT生成式推理与判别式分类头，两种模式同步进行风险拦截：

**生成式模式：逐条输出基于NSFA定义的链式推理分析，让每一步判断都有据可查，适用于离线合规审计；****判别式模式：每次前向传播就直接给出各风险域的置信度，延迟可以压到45～57ms，可用于高吞吐的实时在线拦截。**

这里还有个讨巧的设计，由于骨干网络是冻结的，真正下判断的是外挂在上面的轻量分类头，所以以后一旦冒出新风险，只需要补训一个小头就行，轻松实现原生可扩展。

换言之，这套架构还能当插件用，比如给Llama Guard 3额外增加一个分类头，用户请求安全基准的F1值直接提升17.6个百分点。

从整体效果来看，SingGuard-NSFA在3大评测基准（用户请求安全、模型响应安全、跨数据集泛化）上均取得**SOTA**，最小的0.8B模型就能比肩8B竞品，9B大小更是在泛化上达到91.29% F1，精度与召回更加均衡。

另一个开源框架则是面向多模态大模型的**SingGuard**，同样包括0.8B、2B、4B、8B四个尺寸。

它最大的特点，是把安全规则做成了运行时输入。不同业务域可以现场下发各自的红线，模型据此逐条判定。

也就是说，它回答的不只是有没有风险，也包括是否违反当前防控规则。

推理侧同样讲究**快慢分工**，快思考负责低延迟秒判，慢思考负责逐规则深度推理，两者之间还能通过early exit自动切换，在效率和准确性之间寻找平衡。

针对线上多条规则并行审核的效率瓶颈，蚂蚁还提出了RI-Mask，让共享的图文上下文只编码一次，多条规则并行判断，这样多模态推理最高可提速5倍以上。

显然，SingGuard-NSFA和SingGuard这两个框架各自面向的对象有所不同，一个更关注AI行为，另一个更关注AI感知，但它们的底色是一致的，都强调**过程可解释**、**新增风险可扩展**。

具体触犯了哪条规则、依据是什么，审核和追溯都拿得出理由，不是黑箱操作或简单下结论；新增风险都仅需轻量扩展，不影响已有的检测能力。

如果说很多安全产品解决的是具体问题，那么这一类框架更像是在定义未来智能体运行所依赖的安全基础设施。

再把时间线拉长来看，这次开源其实不是孤立事件。

今年早些时候，在全网关注OpenClaw漏洞的同时，**蚂蚁AI安全实验室**就曾发现多个高危漏洞并协助官方完成修复。

随后，蚂蚁与清华大学联合开源了**ClawAegis**，为智能体提供了一套覆盖产品全生命周期的安全方案。

再到最新的安全框架开源，这条脉络其实相当清晰：从漏洞挖掘到场景化解法，再到可复用的底层框架。

显然蚂蚁在AI安全上的布局，是在逐步收束成体系。

前不久，蚂蚁智能体安全产品还通过了信通院泰尔实验室的最高等级评级。这类第三方认证，至少也说明在工程落地上，蚂蚁确实走在了前面。

可以说，靠补丁续命的时代已经过去了，行业需要有人往前一步，去定义风险的边界，去搭建一套大家都能稳稳站上去的底座。

Claude Code、OpenClaw带来的讨论，某种程度上只是开始。随着Agent越来越深入办公、开发和生活场景，AI安全也将进入新的阶段。

相比不断追赶漏洞，**如何建立一套能够持续适应风险变化的安全基础设施**，或许才是整个行业下一步真正需要解决的问题。

从这个角度再回头看最近的这些开源动作，它们真正值得关注的，不只是性能指标，而是开始尝试回答一个更底层的问题：

**AI时代的安全边界**，究竟应该如何定义。

*版权所有，未经授权不得以任何形式转载及使用，违者必究。*