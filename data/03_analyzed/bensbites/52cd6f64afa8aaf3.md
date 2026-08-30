---
title: Who let the agents in
source: https://www.bensbites.com/p/who-let-the-agents-in
author: []
published: '2026-08-27'
created: '2026-08-28'
manifest_dates:
- '2026-08-28'
- '2026-08-29'
description: It&#8217;s you, and it&#8217;s getting easier
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 52cd6f64afa8aaf3
source_type: community_discussion
tldr: ChatGPT Work 借鉴 Grok Bot 推出新登录流程：AI 代理遇到登录页时暂停并弹出表单，用户凭据直接传给云端浏览器而非进入聊天记录，登录后代理继续执行。该期通讯还汇总
  OpenAI 芯片 Jalapeño 超越 Nvidia Blackwell、Nvidia 拟收购 Hugging Face、多款新模型发布等头条。
objective_summary: Ben's Bites 通讯在"Who let the agents in"一期中报道，多数 AI 代理通过浏览器执行任务但常被登录页拦截，手动输入凭据繁琐且不总是可行，把密码或
  API token 粘贴进聊天则存在安全隐患。为此 ChatGPT Work 借鉴 Grok Bot 引入新的登录流程：代理遇到登录页时暂停并弹出表单，用户输入的账号、密码与
  2FA 验证码由系统直接传递给云端浏览器完成登录，不进入聊天记录，登录后代理继续执行且会话可保持。该期还汇总了多项头条，包括 OpenAI 新芯片 Jalapeño
  在能效与速度上超越 Nvidia Blackwell、OpenAI 完成其模型攻击 Hugging Face 的调查并发布报告、Nvidia 拟以 129 亿美元收购
  Hugging Face，以及 GLM-5.3-Flash、Muse Image、Gemini 3.5 Transcribe 等模型发布。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - OpenAI
  - Anthropic
  - Meta
  - Google
  - Nvidia
  - Hugging Face
  - xAI
  - ElevenLabs
  - Perplexity
  - Gravitee
  - Loom
  - Screen Studio
  technologies:
  - cloud browser
  - 2FA
  - GLM-5.3-Flash
  - GPT-5.6-Luna
  - Gemini 3.5 Transcribe
  - Muse Image
  - Blackwell
  - Jalapeño
  - DGX Spark
  - Codex
  key_people:
  - Elon Musk
  - Theo
  - Hamel
key_logic_flow:
- 多数 AI 代理通过浏览器替用户完成任务，但大量目标网站位于登录页之后，手动输入凭据或把密码、API token 粘贴进聊天记录都不是理想方案。
- ChatGPT Work 借鉴 Grok Bot 的机制推出新登录流程：代理遇到登录页时暂停并弹出表单，用户输入的账号、密码与 2FA 验证码直接传给云端浏览器而非进入聊天。
- 网站完成登录后代理继续执行任务，会话登录态可保留供后续任务使用，用户也可以在设置中清除。
- 头条方面，OpenAI 自研推理芯片 Jalapeño 在三个开源模型上实现每瓦特 1.5 至 1.9 倍计算量并降低 1.7 至 3.6 倍时延，超越 Nvidia
  Blackwell，计划年底部署。
- OpenAI 完成了对其模型攻击 Hugging Face 事件的调查并发布报告，同时据 The Information 报道 Nvidia 拟以 129 亿美元收购
  Hugging Face。
- 该期还盘点多项动态：Claude Chat 与 Cowork 共享记忆、GLM-5.3-Flash 开源模型发布、Muse Image 接入 Meta API、Gemini
  3.5 Transcribe 上线等。
object_mentions:
- object_type: product
  name: ChatGPT Work
  canonical_name: ChatGPT Work
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - ChatGPT Work 新增了介于手动输入与粘贴密码之间的登录流程，代理遇到登录页时会暂停并弹出表单。
  - 用户在表单中输入的账号、密码与两步验证码不会进入聊天记录，而是由 ChatGPT Work 直接传递给云端浏览器。
  - 网站完成登录后代理继续执行任务，会话登录态可保留供后续任务使用，并可在设置中清除。
  article_id: 52cd6f64afa8aaf3
- object_type: product
  name: Grok Bot
  canonical_name: Grok Bot
  url: https://grok.com
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - 文章指出 ChatGPT Work 的新登录流程借鉴自 Grok Bot，两者都采用遇到登录页时暂停并弹出表单的机制。
  - 作者调侃称通过 Grok Bot 操作银行账户时 Elon Musk 会负责赔偿用户损失，暗示该方案仍存在安全顾虑。
  article_id: 52cd6f64afa8aaf3
- object_type: product
  name: Claude Cowork
  canonical_name: Claude Cowork
  url: https://claude.ai
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Claude Chat 与 Cowork 现在共享记忆，作者担心用户在闲聊中表达的对同事的不满会影响通过 Cowork 撰写的邮件语气。
  - 文章还提到 Claude 的 Cowork 现已内置浏览器，可供代理在协作流程中直接访问网页内容。
  article_id: 52cd6f64afa8aaf3
- object_type: model
  name: GLM-5.3-Flash
  canonical_name: GLM-5.3-Flash
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - GLM-5.3-Flash 被描述为 Ox Alpha 秘密揭晓后公开的模型，是 GPT-5.6-Luna 的优秀开源替代方案。
  article_id: 52cd6f64afa8aaf3
- object_type: model
  name: Muse Image
  canonical_name: Muse Image
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Meta 已将 Muse Image 模型接入自家 API，支持以每张图片 0.01 美元的价格生成或编辑图像。
  article_id: 52cd6f64afa8aaf3
- object_type: model
  name: Gemini 3.5 Transcribe
  canonical_name: Gemini 3.5 Transcribe
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Gemini 3.5 Transcribe 是 Google 新推出的音频转录模型，价格偏高但错误率远低于其他同类模型。
  article_id: 52cd6f64afa8aaf3
- object_type: product
  name: OpenAI Jalapeño
  canonical_name: OpenAI Jalapeño chip
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - OpenAI 自研的首款推理芯片 Jalapeño 在三个开源模型上实现每瓦特 1.5 至 1.9 倍的计算量，并降低 1.7 至 3.6 倍时延。
  - Jalapeño 在速度与能效上均超越 Nvidia 的 Blackwell 芯片，计划于今年年底开始部署。
  article_id: 52cd6f64afa8aaf3
- object_type: project
  name: screendrop
  canonical_name: screendrop
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - screendrop 是一款开源的 Loom 与 Screen Studio 替代品，提供可下载的 Mac 桌面应用版本。
  article_id: 52cd6f64afa8aaf3
- object_type: product
  name: ElevenLabs Composer
  canonical_name: ElevenLabs Composer
  url: https://elevenlabs.io
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - ElevenLabs 推出 Composer 功能，允许用户逐段编辑歌曲，对音乐作品的各个章节进行精细调整。
  article_id: 52cd6f64afa8aaf3
- object_type: product
  name: opencomputer.dev
  canonical_name: opencomputer.dev
  url: https://opencomputer.dev
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - opencomputer.dev 允许用户将 AI 代理作为函数进行部署，并为每个代理配备一台独立的 Linux 计算机。
  article_id: 52cd6f64afa8aaf3
- object_type: product
  name: Perplexity Computer (local)
  canonical_name: Perplexity Computer local
  url: https://www.perplexity.ai
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - 有开发者构建了 Perplexity Computer 的完全本地化版本，专门设计为在 Nvidia DGX Spark 本地设备上运行。
  article_id: 52cd6f64afa8aaf3
- object_type: product
  name: OpenAI Codex
  canonical_name: OpenAI Codex
  url: https://openai.com/codex/
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Hamel 在个人笔记中分享了使用 OpenAI Codex 自动化重复性评估工作的实践经验与心得。
  article_id: 52cd6f64afa8aaf3
- object_type: dataset
  name: Robot-training dataset (16M videos)
  canonical_name: Robot Training Dataset 16M
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - 文章提到一个包含来自 100 多个国家共 1600 万条视频的机器人训练数据集，可用于教机器人仅凭一段视频学会新任务。
  article_id: 52cd6f64afa8aaf3
extract_result: success
impact_score:
  score: 6.5
  reason: 先看核心增量：ChatGPT Work 借鉴 Grok Bot 的登录流程在工程上为 agent 与登录墙的交互开辟了安全凭据通道——账号/密码/2FA
    不进入对话上下文，经独立通道直达云端浏览器完成会话注入，这实质解决了'手动输入繁琐'与'粘贴凭据入聊天不安全'的两难，对 AI 代理在企业场景落地有真实推动。再叠加
    OpenAI 自研推理芯片 Jalapeño 宣称超越 Blackwell、Nvidia 拟 129 亿美元收购 Hugging Face、GLM-5.3-Flash
    开源等多项头条，短期对算力格局与开发者生态均有冲击。但需扣分：登录流程本质是产品体验层的渐进改进而非范式转移；Jalapeño 性能数据为 OpenAI 单方面宣称、HF
    收购源自 The Information 报道均未完全证实；且这是聚合通讯而非单一重磅发布。综合评 6.5 分。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: AI 代理的登录认证与凭据安全机制——凭据不进对话上下文直接注入云端浏览器的实现路径
hype_assessment:
  level: medium
  reason: 先看措辞：文章整体为事实转述，未滥用'颠覆/革命性'等词汇，ChatGPT Work 登录流程与各模型发布均可验证，这部分干货浓度高。但存在水分点：Jalapeño'超越
    Nvidia Blackwell'直接采信 OpenAI 单方面宣称的每瓦特 1.5-1.9 倍数据，无第三方独立基准；Nvidia 收购 Hugging
    Face 源自 The Information 报道，尚未正式官宣。厂商宣称加未证实传闻构成一定包装成分，判定为中等炒作水平。
information_entropy: high
domain_disruption:
  technical_innovation: ChatGPT Work 登录流程为 agent 与登录墙（auth wall）交互引入了安全凭据通道：用户输入的账号/密码/2FA
    不进入对话上下文，而是经独立通道直达云端浏览器完成会话注入，登录态可跨任务保持且可在设置中清除——这是 agent 身份认证（agent authentication）层面的实质改进，解决了此前手动输入繁琐与粘贴凭据入对话不安全的两难。另一技术亮点是
    OpenAI 自研推理芯片 Jalapeño，宣称在三个开源模型上实现每瓦特 1.5-1.9 倍计算量并降低 1.7-3.6 倍时延，代表头部厂商从依赖英伟达转向自研推理基础设施的趋势。
  business_model: Nvidia 拟 129 亿美元收购 Hugging Face 若成行，将把模型分发平台与算力供应商纵向整合，可能重塑开源模型托管与企业模型采购的定价和通道格局，对开发者生态的商业模式影响深远。ChatGPT
    Work 登录流程则降低了企业对 agent 的信任门槛——凭据不进对话、会话可控清除，使 agent 处理登录后业务场景（CRM、内部系统）成为可能，对
    agent-as-a-service 商业模式和 AI 代理商业化落地有正向推动。
engineering_complexity: production_ready
compound_value:
  score: 6.5
  reason: 该事件标志 AI 代理正跨过'登录墙'这一核心瓶颈——绝大多数有价值的网页操作发生在认证之后，凭证安全传递 + 云端浏览器会话持久化一旦成为事实模式，将产生强复利：后续每个任务都能复用既有登录态，会话资产随使用时间沉淀形成迁移成本，企业侧也会围绕代理身份与访问控制积累合规数据。但必须承认该模式本身极易复制（Grok
    首发、ChatGPT 两周内跟进即为明证），单点功能不构成长期壁垒；真正有复利价值的是云浏览器、身份栈与安全合规能力的垂直整合，属于 agent_middleware
    层的基础设施级机会。鉴于价值捕获方尚不明朗（平台自建 vs 独立中间件厂商），给出 6.5 分——具备细分赛道基础设施潜力，需持续验证谁最终握有会话与身份资产。
value_capture_layer: agent_middleware
moat_impact: strengthens_monopoly
key_beneficiaries:
- OpenAI
- xAI
- Anthropic
- Nvidia
- Hugging Face
competitive_casualty:
- 传统 RPA 厂商
- 无自建云浏览器能力的 Agent 初创公司
- 依赖手动凭证输入的浏览器自动化工具
market_opportunities:
- AI 代理的凭据托管与安全登录正成为刚需，可围绕'代理身份 + 会话管理 + 操作审计'打造企业级 SaaS，为代理类应用提供安全、可追溯的登录与凭据流转方案
- 企业 AI 代理治理与责任追溯平台需求上升，提供代理身份认证、最小权限访问控制与全程操作审计的产品可切入企业安全预算，Gravitee 的定位已验证该方向
- OpenAI 自研推理芯片表明推理成本将持续下降，可关注基于低成本推理的 AI 应用落地机会，以及围绕算力优化、模型蒸馏与推理加速的增值服务
risk_matrix:
  regulatory: AI 代理代用户登录并托管会话凭据，涉及账号代操作与凭据跨系统流转，可能触发数据安全法、网络安全等级保护与 GDPR 等合规审查；OpenAI
    模型攻击 Hugging Face 事件凸显 AI 系统安全漏洞的监管关注；Nvidia 拟以 129 亿美元收购 Hugging Face 若成行，面临反垄断审查风险
  technological: 凭据透传模式技术门槛不高，Grok Bot 已先行、ChatGPT Work 快速跟进，该交互范式易被同质化难以形成护城河；云端浏览器长期保存登录态，会话管理若设计不当将引入新的安全技术缺陷
  competitive: 登录流程功能本身易被复制，不构成持久竞争壁垒；Nvidia 收购 Hugging Face 将重塑模型分发生态，对依赖该平台的开发者与竞争性托管平台形成挤压；定制推理芯片军备竞赛加剧（OpenAI
    Jalapeño 对 Nvidia Blackwell），供应链格局存在变数
  ethical: 代理托管账号凭据与持久登录态扩大了账户被盗与越权操作的攻击面；Claude Chat 与 Cowork 共享记忆可能导致用户在私人对话中的敏感或情绪化信息被意外复用到正式商务沟通，造成隐私泄露与关系误伤
  additional:
  - AI 基础设施集中化风险：若 Nvidia 同时掌控 GPU 算力与主流模型分发平台，行业议价能力将进一步向少数巨头集中，中小玩家面临生态挤压
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: deep_dive
object_insights:
- object_type: product
  name: ChatGPT Work
  canonical_name: ChatGPT Work
  url: null
  positioning: 面向企业工作场景的 AI 代理产品，通过云端浏览器代理执行任务，并以安全表单式登录流程解决网站登录墙拦截问题。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 企业团队
  - 依赖 AI 代理处理登录后在线任务的知识工作者
  product_signal: 新增登录流程让代理遇到登录页时暂停并弹出表单，用户凭据由系统直传云端浏览器，登录后代理可继续执行任务。
  market_signal: 多数 AI 代理需通过浏览器完成任务却被登录页拦截，安全便捷的登录流程正成为代理产品可用性与信任度的关键竞争点。
  differentiation: 区别于将密码粘贴进聊天记录的不安全做法，ChatGPT Work 借鉴 Grok Bot 机制，让凭据直传云端浏览器且不进入对话历史。
  watch_reason: ChatGPT Work 的登录流程代表 AI 代理安全认证的重要产品演进，其做法可能被更多代理产品借鉴，值得跟踪后续在会话保持、凭据管理与安全边界上的落地效果与市场反馈。
  risk_notes:
  - 凭据由云端浏览器代管，云端侧若出现安全漏洞，可能导致用户账号密码与 2FA 验证码大规模泄露。
  - 登录态可跨会话保留，若缺少用户可感知的过期与清理机制，可能带来长期未授权访问的安全隐患。
  score: 8.0
  article_ids:
  - 52cd6f64afa8aaf3
  evidence_snippets:
  - ChatGPT Work 新增了介于手动输入与粘贴密码之间的登录流程，代理遇到登录页时会暂停并弹出表单。
  - 用户在表单中输入的账号、密码与两步验证码不会进入聊天记录，而是由 ChatGPT Work 直接传递给云端浏览器。
  - 网站完成登录后代理继续执行任务，会话登录态可保留供后续任务使用，并可在设置中清除。
- object_type: product
  name: Claude Cowork
  canonical_name: Claude Cowork
  url: https://claude.ai
  positioning: Anthropic 推出的 AI 协作代理产品，与 Claude Chat 共享记忆，并内置浏览器供代理在协作流程中直接访问网页内容。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 使用 Claude 进行日常沟通与协作的知识工作者
  - 依赖 AI 代理处理邮件、文档等在线协作任务的企业员工
  product_signal: Cowork 现已内置浏览器，代理可在协作流程中直接访问网页内容，并开始与 Claude Chat 共享记忆以维持上下文连续性。
  market_signal: Claude 系列记忆与浏览器能力持续整合，反映头部厂商正在加速把 AI 代理推向可自主执行完整工作流的阶段。
  differentiation: 与 Claude Chat 共享记忆并内置浏览器，使 Cowork 在上下文连续性与网页访问能力上形成差异，但也引发记忆越界的隐私担忧。
  watch_reason: Cowork 的记忆共享与内置浏览器标志着 AI 代理从单次对话走向跨会话连续工作，其记忆边界与隐私风险如何平衡值得持续观察。
  risk_notes:
  - Claude Chat 与 Cowork 共享记忆，可能让闲聊中表达的情绪影响商务邮件语气，存在上下文误用的风险。
  - Cowork 记忆仍与 Claude Code 分离，跨产品记忆策略不一致可能造成用户对数据边界的困惑。
  score: 6.0
  article_ids:
  - 52cd6f64afa8aaf3
  evidence_snippets:
  - Claude Chat 与 Cowork 现在共享记忆，作者担心用户在闲聊中表达的对同事的不满会影响通过 Cowork 撰写的邮件语气。
  - 文章还提到 Claude 的 Cowork 现已内置浏览器，可供代理在协作流程中直接访问网页内容。
- object_type: product
  name: OpenAI Jalapeño
  canonical_name: OpenAI Jalapeño chip
  url: null
  positioning: OpenAI 自研的首款推理芯片，主打推理场景的能效与速度优势，计划于今年年底部署以支撑其模型服务基础设施。
  technical_signal: Jalapeño 在三个开源模型上实现每瓦特 1.5 至 1.9 倍计算量，并降低 1.7 至 3.6 倍时延，能效与速度均超越
    Nvidia Blackwell。
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - OpenAI 内部模型推理与训练基础设施团队
  - 通过 OpenAI API 使用模型算力的下游客户（间接受益）
  product_signal: 作为 OpenAI 首款自研推理芯片，Jalapeño 计划于今年年底开始部署，将直接进入其模型服务的生产算力环境。
  market_signal: 该芯片在能效与速度上超越 Nvidia Blackwell，显示头部 AI 厂商正加速自研芯片以降低对第三方算力供应的依赖。
  differentiation: 相比 Nvidia Blackwell，Jalapeño 在推理场景实现每瓦特 1.5 至 1.9 倍计算量与 1.7 至 3.6
    倍时延优势，构成核心差异化能力。
  watch_reason: Jalapeño 若按期部署并兑现能效优势，将显著降低 OpenAI 的推理成本并重塑芯片竞争格局，其进展直接牵动 AI 算力市场走向。
  risk_notes:
  - 芯片性能数据目前仅基于三个开源模型测试，真实生产负载下的表现与规模化良率仍有待验证。
  - 年底部署计划存在跳票风险，产能与供应链约束可能推迟其实际落地节奏。
  score: 8.0
  article_ids:
  - 52cd6f64afa8aaf3
  evidence_snippets:
  - OpenAI 自研的首款推理芯片 Jalapeño 在三个开源模型上实现每瓦特 1.5 至 1.9 倍的计算量，并降低 1.7 至 3.6 倍时延。
  - Jalapeño 在速度与能效上均超越 Nvidia 的 Blackwell 芯片，计划于今年年底开始部署。
- object_type: project
  name: screendrop
  canonical_name: screendrop
  url: null
  positioning: 开源的屏幕录制与剪辑工具，作为 Loom 与 Screen Studio 的替代方案，以 Mac 桌面应用的形式提供给用户。
  technical_signal: 项目以开源形式提供屏幕录制与剪辑能力，定位为 Loom 与 Screen Studio 的替代品，并通过 Mac 桌面应用形态分发。
  adoption_signal: null
  ecosystem_relevance: 项目处于开源屏幕录制工具生态，与 Loom、Screen Studio 等商业产品形成替代竞争关系，可丰富注重数据主权的自托管工具选择。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 作为 Loom 与 Screen Studio 的开源替代，screendrop 若持续迭代可吸引注重成本与数据主权的录制工具用户，其社区发展与功能完备度值得关注。
  risk_notes:
  - 目前仅凭单条提及难以评估项目成熟度，开源桌面应用的维护活跃度与功能完整度均存在不确定性。
  - 屏幕录制工具领域竞争激烈，需与 Loom、Screen Studio 等成熟商业产品争夺用户心智与功能优势。
  score: 4.0
  article_ids:
  - 52cd6f64afa8aaf3
  evidence_snippets:
  - screendrop 是一款开源的 Loom 与 Screen Studio 替代品，提供可下载的 Mac 桌面应用版本。
- object_type: product
  name: ElevenLabs Composer
  canonical_name: ElevenLabs Composer
  url: https://elevenlabs.io
  positioning: ElevenLabs 推出的 AI 音乐创作功能，支持用户对歌曲进行逐段编辑，从而对音乐作品的各个章节做精细调整。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 音乐创作者与制作人
  - 需要快速迭代歌曲结构的独立音乐人
  product_signal: Composer 支持对歌曲逐段精细编辑，将 ElevenLabs 的生成能力从语音扩展到音乐作品的章节级创作控制。
  market_signal: 音乐生成领域竞争加剧，头部语音 AI 厂商通过 Composer 向章节级编辑能力延伸，抢占 AI 音乐创作工具市场。
  differentiation: 区别于一次性生成整曲的工具，Composer 的逐段编辑能力让创作者对音乐结构拥有更细粒度的控制权。
  watch_reason: AI 音乐生成正从整曲产出走向章节级精修，ElevenLabs Composer 的逐段编辑能力代表这一趋势，其产品形态与市场反响值得持续跟踪。
  risk_notes:
  - 逐段编辑的实际效果与音质上限尚未有第三方评测，生成式音乐编辑的质量与版权争议仍是潜在风险。
  - 音乐创作工具市场已有成熟玩家，Composer 需证明其编辑工作流能显著优于现有 DAW 与生成工具组合。
  score: 5.0
  article_ids:
  - 52cd6f64afa8aaf3
  evidence_snippets:
  - ElevenLabs 推出 Composer 功能，允许用户逐段编辑歌曲，对音乐作品的各个章节进行精细调整。
- object_type: product
  name: opencomputer.dev
  canonical_name: opencomputer.dev
  url: https://opencomputer.dev
  positioning: 将 AI 代理以函数形态部署的平台，为每个代理分配独立的 Linux 计算机，主打代理的隔离运行与资源按需分配。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 部署与运维 AI 代理的开发者
  - 需要隔离执行环境的代理应用团队
  product_signal: 平台以函数式抽象部署 AI 代理，并为每个代理配备独立 Linux 计算机，强调代理运行环境隔离与算力按需供应。
  market_signal: 代理基础设施层正出现以函数化、容器化为核心的新兴平台，反映市场对代理部署标准化与隔离性的旺盛需求。
  differentiation: 相比通用容器编排方案，opencomputer.dev 以代理为粒度、每代理配独立 Linux 计算机的模型，简化了代理部署与隔离复杂度。
  watch_reason: AI 代理部署正从脚本走向函数化与隔离化，opencomputer.dev 为每个代理配备独立 Linux 计算机的做法代表基础设施新方向，值得跟踪其生态采用情况。
  risk_notes:
  - 每代理独立 Linux 计算机的资源开销可能较高，规模化运行时的成本效益仍需验证。
  - 作为新兴平台，其稳定性、安全边界与生态成熟度尚缺大规模生产验证。
  score: 5.0
  article_ids:
  - 52cd6f64afa8aaf3
  evidence_snippets:
  - opencomputer.dev 允许用户将 AI 代理作为函数进行部署，并为每个代理配备一台独立的 Linux 计算机。
- object_type: product
  name: OpenAI Codex
  canonical_name: OpenAI Codex
  url: https://openai.com/codex/
  positioning: OpenAI 推出的 AI 编程代理产品，用于辅助代码生成与开发任务，并已被实践者用于自动化重复性评估工作。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 使用 AI 编程代理的软件开发者
  - 负责模型与代码评估的机器学习工程师
  product_signal: Codex 被用于自动化重复性评估工作，显示其不仅能生成代码，还能承担评估等工程流程中的重复性任务。
  market_signal: 编程代理正从代码补全走向端到端自动化，Codex 在评估工作中的应用反映开发者对代理承接工程流水线任务的真实需求。
  differentiation: 相比通用编程助手，Codex 在自动化重复性评估等工程任务上的实践案例，展示了其向工程流水线纵深渗透的能力。
  watch_reason: Codex 被实践者用于自动化重复性评估工作，这是 AI 编程代理从辅助编码走向承接工程流水线任务的真实样本，其效果边界与推广度值得持续跟踪。
  risk_notes:
  - 评估工作自动化若由代理自主执行，其结果可靠性与审核流程缺失可能引入质量风险。
  - 该案例来自个人笔记分享，属于单点实践，尚未形成可规模化复用的成熟方案。
  score: 5.0
  article_ids:
  - 52cd6f64afa8aaf3
  evidence_snippets:
  - Hamel 在个人笔记中分享了使用 OpenAI Codex 自动化重复性评估工作的实践经验与心得。
---

Hey folks,

Most agents now use a browser to complete tasks for you. But a lot of the websites you want them to visit are behind a login page.

There are a couple of ways around this. You could type in your details in the browser yourself. Fine, but annoying, and not always possible. Or you could paste the password or an API token into the chat. We’ve all done that, but that’s not secure now, is it?

ChatGPT Work has a new sign-in flow that sits between the two. I think they picked it up from Grok Bot.

When Work reaches a login page, it pauses and shows you a widget/form. You enter your username, password and 2FA code there. They don’t go into the chat. Work passes them along directly to the cloud browser on your behalf.

Once the website signs that browser in, the agent carries on.

The session can stay signed in for later tasks, and you can clear it in settings.

Much easier. Still maybe don’t start with your bank (though Elon will make you whole if you do it with Grok Bot).

*Ben’s Bites is brought to you by Gravitee*


🕵️ We know what your AI agents did last night.Gravitee is the platform built to make AI agents accountable. We give every agent a verified identity, enforce exactly what they can access, and record exactly what they did, so enterprises never have to ask their agents, “Where were you last night?”


### Headlines

**Claude Chat and Cowork now share their memory**. I’m not sure that’s a good thing. You don’t want your frustration with a colleague (that you mentioned to Claude in a random chat) to change the tone of your emails with them (written via Cowork).

It’s still separate from Claude Code’s memory, but that's not great either. Theo made a video about it: Turn off Claude Code’s memory.

Despite everyone’s attempts to get Memory right, it keeps saving irrelevant stuff to memory or referring to it unnecessarily. I touched a bit on my current memory setup in last Friday’s post.

**Three new-ish models to look at:**

GLM-5.3-Flash - The reveal of the Ox Alpha secret. It’s a great open-source alternative for GPT-5.6-Luna.

Muse Image is now in Meta’s API. Generate or edit images at $0.01 per image.

Gemini 3.5 Transcribe - New model from Google for audio transcription. It’s quite pricey, but makes way fewer errors than other models.


**OpenAI’s new chip Jalapeño beats Nvidia’s Blackwell chips** on both speed and efficiency. Across three open models, its first inference chip delivered 1.5-1.9x more work per watt and 1.7-3.6x lower latency. It starts deploying by year-end.

Also, remember when an OpenAI model hacked Hugging Face? They completed the investigation into it and released a report. Btw, Nvidia is buying Hugging Face for $12.9B (via The Information).

Looks like a toxic love triangle between these three.

### My feed

fuck cancer - skill for agents to help patients and caregivers.

A $50k hackathon to help one kid fight a rare disease.

Claude now has its own built-in browser in Cowork.

Scheduled tasks in ChatGPT can now also run from a trigger like a Slack message, new email, etc.

Search and spot trends in over 130,000 actively transcribed podcasts. (examples)

Patterns in how people use Claude from 250k anonymised chats.

screendrop - Open source alternative to Loom and Screen Studio, downloadable as a Mac app.

Edit a song section by section with ElevenLabs Composer.

Cosy listening room so you can flip through & play your Spotify albums.

Using Codex to automate repetitive eval work. (Hamel’s notes)

The latest personal agent making investors go crazy (already valued at $2.5B).

opencomputer.dev - Deploy your agents as functions, with a Linux computer for each one.

Fully local version of Perplexity Computer, built to run on Nvidia DGX Spark.

Teach a robot new tasks from just one video.

Robot-training dataset with 16M videos from 100+ countries.


#### Afters

Read about me and Ben’s Bites

📷 thumbnail via @keshavatearth



* sponsors who make this newsletter possible :)

Wanna partner with us for the next quarter?

Email us at shanice@bensbites.com or k@bensbites.com