---
title: How to tell if your AI platforms’ accounts have been hacked
source: https://techcrunch.com/2026/08/15/how-to-tell-if-your-ai-platforms-accounts-have-been-hacked/
author:
- '[[Lorenzo Franceschi-Bicchierai]]'
published: '2026-08-15'
created: '2026-08-16'
manifest_dates:
- '2026-08-16'
- '2026-08-17'
description: A guide on how to check if hackers have broken into your accounts on
  the most popular AI platforms.
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 23cd5e9aacbd902c
source_type: news_media
tldr: TechCrunch 发布安全指南，教用户如何检查 ChatGPT、Claude、Perplexity 三个 AI 平台账户是否被黑客入侵，包括查看活动会话、单独或全部登出设备、重置密码等具体操作步骤。
objective_summary: TechCrunch 于 2026 年 8 月发布指南文章，介绍如何判断 AI 平台账户是否被黑客入侵，并建议使用密码管理器与开启多因素认证。ChatGPT
  和 Perplexity 支持多因素认证，而 Claude 使用邮件登录链接代替密码。文章分别给出三个平台检查可疑登录设备的方法：ChatGPT 可在 Security
  and Login 中查看活动会话并重置密码，Claude 可在账户设置中终止可疑会话且无密码可修改，Perplexity 因不显示登录位置只能通过退出所有会话应对风险。
event_type: policy_and_safety
epistemic_status: verified_fact
entities:
  companies:
  - TechCrunch
  - OpenAI
  - Anthropic
  - Perplexity
  technologies:
  - MFA
  key_people: []
key_logic_flow:
- TechCrunch 发布指南，指出黑客可像攻击其他在线服务一样入侵 ChatGPT、Claude 和 Perplexity 等 AI 平台账户，并建议使用唯一密码与开启多因素认证（MFA）。
- ChatGPT 和 Perplexity 支持多因素认证，而 Claude 不使用密码，而是通过向用户邮箱发送登录链接来验证身份。
- ChatGPT 用户可通过 Settings 中的 Security and Login 查看 Active Sessions 登录设备，对不认识的设备可单独登出或点击
  Log out all，并可通过邮箱验证码重置密码。
- Claude 用户可在 Settings 的 Account 中查看 Active sessions，对可疑会话选择 Log out 或 Terminate，也可登出所有设备，但因无密码机制无法修改密码。
- Perplexity 不显示用户的登录位置，用户只能进入 All settings 点击 Sign out of all sessions 并确认，强制登出所有会话以应对潜在的账户入侵。
object_mentions:
- object_type: product
  name: ChatGPT
  canonical_name: ChatGPT
  url: https://chatgpt.com
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - ChatGPT 用户可在账户设置的 Security and Login 页面查看 Active Sessions 登录设备列表，对不认识的设备可单独登出或一键退出全部会话。
  - ChatGPT 支持多因素认证，用户可在忘记密码时通过邮箱接收六位验证码并设置新密码。
  article_id: 23cd5e9aacbd902c
- object_type: product
  name: Claude
  canonical_name: Claude
  url: https://claude.ai
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Claude 不使用密码，而是通过向用户邮箱发送登录链接完成身份验证，用户可在账户设置的 Active sessions 中终止可疑会话或登出所有设备。
  - Claude 因完全采用邮件链接登录机制，没有可修改的密码。
  article_id: 23cd5e9aacbd902c
- object_type: product
  name: Perplexity
  canonical_name: Perplexity
  url: https://www.perplexity.ai
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Perplexity 不显示用户的当前登录位置，若怀疑账户被入侵，用户只能进入 All settings 点击 Sign out of all sessions
    并确认，强制退出所有会话。
  - Perplexity 作为 AI 驱动的搜索引擎支持多因素认证以保护账户安全。
  article_id: 23cd5e9aacbd902c
extract_result: success
impact_score:
  score: 2.5
  reason: 这是一篇面向消费者的安全操作指南，不涉及新产品发布、融资或技术范式变化，不会改变局部竞争格局。评分依据：它反映 AI 平台账户安全日益受关注这一行业趋势，对普通用户有实用价值，但本质是教程性质的内容，对从业者与行业结构的影响有限，属于日常更新级别的事件。
sentiment: neutral
developer_sentiment:
  tone: neutral
  primary_focus: 三大 AI 平台账户安全机制差异：ChatGPT/Perplexity 支持 MFA，而 Claude 采用无密码邮箱登录链接的安全模型
hype_assessment:
  level: low
  reason: 全文为具体可验证的操作步骤，未出现'颠覆'、'革命性'等 PR 滥用词汇，也没有夸大 AI 平台安全风险的恐慌式表述，属于实用干货，无炒作成分。
information_entropy: medium
domain_disruption:
  technical_innovation: 无重大技术突破。值得注意的架构观察是 Claude 采用无密码的邮箱登录链接方案，与 ChatGPT/Perplexity
    的'密码+MFA'体系形成两种不同的身份认证安全模型，前者天然规避密码泄露风险但依赖邮箱安全性。
  business_model: 无
engineering_complexity: production_ready
compound_value:
  score: 4.5
  reason: 推理链：(1) 事件性质——这是一篇消费级安全操作指南，非技术突破、非产品发布、非融资事件，本身不产生直接商业价值；(2) 信号价值——该文被
    TechCrunch 作为规模化选题报道，说明 ChatGPT/Claude/Perplexity 账户已成为黑客系统性攻击目标，侧面印证 AI 应用层已沉淀出高价值用户资产（付费订阅、会话历史、工作流数据），这是
    AI 从尝鲜工具走向生产级平台的关键验证信号；(3) 复利判断——账户安全/身份管理（MFA、会话治理、无密码认证）正从可选项变成应用层的必备基础设施，具备一定的长期沉淀效应，但本文作为一次性新闻报道不构成资产积累，且安全能力更多是平台信任的'及格线'而非差异化壁垒。综合判定为中等偏下，需后续观察
    AI 平台安全支出与用户资产规模的增长趋势再上调。
value_capture_layer: end_application
moat_impact: democratizes_access
key_beneficiaries:
- 1Password
- Bitwarden
- OpenAI
competitive_casualty:
- Perplexity
- Anthropic (Claude)
- 小型 AI 初创公司
market_opportunities:
- 可针对企业员工 AI 平台账户推出统一的安全审计与会话监控 SaaS，聚合 ChatGPT/Claude/Perplexity 的多平台登录状态检查、异常会话告警与集中登出能力，填补各平台原生安全功能分散、缺乏统一管理视图的空白
- 密码管理与身份安全厂商可增设'AI 账户安全中心'模块，将 MFA 配置引导、活跃会话体检与疑似入侵检测整合进现有密码管理器产品，形成面向 C 端用户的差异化增值功能
- 安全咨询与托管检测响应（MDR）服务商可将 AI 平台账户入侵排查纳入企业安全基线清单，提供覆盖三大主流 AI 平台的标准化检查手册与自动化巡检工具，向采用 AI
  办公工具的企业客户交叉销售
risk_matrix:
  regulatory: 主流 AI 平台安全能力不统一（Claude 无密码、仅靠邮件登录链接，不提供传统 MFA），在欧盟《AI 法案》与 GDPR 对账户与数据安全要求趋严的背景下可能形成合规短板；账户遭入侵引发的用户私密对话与个人数据泄露将触发
    GDPR 数据泄露报告义务
  technological: 邮件登录链接作为无密码方案虽降低密码窃取风险，但将攻击面转移到邮箱账户接管与钓鱼链接分发，安全模型存在单点依赖；AI 平台安全功能迭代快、操作路径频繁调整，此类指南式内容时效性衰减快
  competitive: 账户安全能力正成为 AI 平台差异化竞争点，Anthropic 因 Claude 不支持传统 MFA 在争夺企业和机构客户时可能处于劣势，或倒逼其补齐安全功能并引发平台间的安全军备竞赛
  ethical: AI 账户遭入侵将直接导致用户与 AI 的私密对话、工作文档和个人偏好数据泄露，放大隐私侵犯与身份冒充风险；被劫持的账户还可能被用于生成误导性内容、实施钓鱼攻击或清洗恶意用途
  additional: []
confidence:
  impact: medium
  compound: medium
  hype: low
actionable_insight: monitor
object_insights:
- object_type: product
  name: ChatGPT
  canonical_name: ChatGPT
  url: https://chatgpt.com
  positioning: OpenAI 旗下面向大众的 AI 对话助手，提供生成式问答、内容创作与办公辅助等能力，是全球用户规模最大的 AI 平台之一。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - AI 对话助手用户
  - ChatGPT 个人与企业订阅用户
  product_signal: ChatGPT 在账户设置中提供 Security and Login 页面，可查看活动会话设备列表、单独登出或一键退出全部会话，并支持多因素认证与邮箱验证码重置密码。
  market_signal: 作为全球用户量领先的 AI 平台，ChatGPT 账户已成为黑客重点攻击目标，TechCrunch 专门发文指导用户检查其账户是否被入侵。
  differentiation: ChatGPT 采用传统密码加多因素认证机制，支持查看具体登录设备并单独登出可疑设备，账户安全审计能力显著强于无密码的 Claude
    与不显示登录位置的 Perplexity。
  watch_reason: ChatGPT 作为用户规模最大的 AI 平台之一，账户安全事件直接影响海量用户隐私；文章展示其活动会话审计、多因素认证与密码重置能力，值得持续跟踪其账户安全与隐私保护的产品演进。
  risk_notes:
  - 文章仅为第三方操作指南，未披露 ChatGPT 实际安全漏洞或真实入侵案例，产品安全能力结论依据有限。
  - 作为高价值攻击目标，ChatGPT 账户面临持续的盗号与滥用压力，安全对抗成本可能随用户规模上升。
  score: 5.0
  article_ids:
  - 23cd5e9aacbd902c
  evidence_snippets:
  - ChatGPT 用户可在账户设置的 Security and Login 页面查看 Active Sessions 登录设备列表，对不认识的设备可单独登出或一键退出全部会话。
  - ChatGPT 支持多因素认证，用户可在忘记密码时通过邮箱接收六位验证码并设置新密码。
- object_type: product
  name: Claude
  canonical_name: Claude
  url: https://claude.ai
  positioning: Anthropic 旗下 AI 对话助手，面向个人与企业用户提供生成式问答、编程辅助与长文本理解等能力，以安全与可靠性为差异化定位。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - AI 对话助手用户
  - Anthropic Claude 个人与企业用户
  product_signal: Claude 采用邮件登录链接替代密码，账户设置中提供 Active sessions 会话管理，可对可疑会话单独 Log out
    或 Terminate，也可登出所有设备。
  market_signal: Claude 被 TechCrunch 列为与 ChatGPT、Perplexity 并列的主流 AI 平台，表明其用户规模已进入黑客重点攻击的主流服务行列。
  differentiation: Claude 是三者中唯一完全无密码的平台，通过邮件链接登录降低密码盗用风险，但也因此不支持多因素认证且没有可重置的密码。
  watch_reason: Claude 的无密码邮件链接登录在主流 AI 平台中独树一帜，其账户安全模型与恢复机制的设计取舍值得持续跟踪；作为头部 AI 产品，其安全事件也会影响行业对
    AI 平台的信任。
  risk_notes:
  - Claude 无密码机制依赖邮箱安全性，若邮箱被入侵则账户恢复手段有限，且不支持多因素认证少了一层防护。
  - 文章仅描述界面操作流程，未验证邮件链接登录在实际攻击场景下的抗钓鱼与抗劫持效果。
  score: 5.0
  article_ids:
  - 23cd5e9aacbd902c
  evidence_snippets:
  - Claude 不使用密码，而是通过向用户邮箱发送登录链接完成身份验证，用户可在账户设置的 Active sessions 中终止可疑会话或登出所有设备。
  - Claude 因完全采用邮件链接登录机制，没有可修改的密码，账户恢复仅能依赖邮箱登录链接。
- object_type: product
  name: Perplexity
  canonical_name: Perplexity
  url: https://www.perplexity.ai
  positioning: Perplexity 是 AI 驱动的搜索引擎，基于大模型提供实时问答与信息检索服务，以答案溯源和对话式搜索体验为特色。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - AI 搜索引擎用户
  - 实时信息检索与问答用户
  product_signal: Perplexity 支持多因素认证，但账户设置中不显示登录设备或位置信息，用户只能通过 Sign out of all sessions
    强制退出全部会话来应对入侵风险。
  market_signal: Perplexity 作为 AI 搜索引擎已被 TechCrunch 纳入主流 AI 平台账户安全指南，反映其用户规模与账户价值正受到黑客关注。
  differentiation: 与 ChatGPT、Claude 提供活动会话可视化不同，Perplexity 不展示登录位置，用户无法判断具体入侵来源，只能全量登出，安全审计能力明显偏弱。
  watch_reason: Perplexity 在账户安全审计上存在明显短板，不显示登录位置让用户难以及时发现可疑访问，其安全能力改进动态值得持续关注；作为快速成长的
    AI 搜索产品也具有跟踪价值。
  risk_notes:
  - Perplexity 不显示登录设备或位置信息，用户难以及时识别可疑登录，账户安全透明度不足。
  - 用户只能通过登出全部会话应对入侵，缺少细粒度的会话管理能力，误登出成本较高。
  score: 5.0
  article_ids:
  - 23cd5e9aacbd902c
  evidence_snippets:
  - Perplexity 不显示用户的当前登录位置，若怀疑账户被入侵，用户只能进入 All settings 点击 Sign out of all sessions
    并确认，强制退出所有会话。
  - Perplexity 作为 AI 驱动的搜索引擎支持多因素认证，以降低密码被盗后账户被入侵的风险。
---

Just like any other online service, hackers can target and break into your accounts on popular AI platforms such as ChatGPT, Claude, and Perplexity.

TechCrunch has created a comprehensive guide to help you protect yourself if you suspect someone has broken into your account on one of the internet’s most popular platforms, social networks, or messaging apps. Now, we’re here to show you how to check whether your accounts on AI platforms have been hacked.

As usual, we recommend using unique passwords stored in a password manager, and turning on multi-factor authentication (MFA), so that even if someone steals your password, they won’t be able to log in without that second piece of information.

ChatGPT and Perplexity offer MFA. Claude doesn’t, because instead of asking for a password, Anthropic’s AI chatbot sends a login link to your email address.

All three of these AI platforms offer similar ways to check if there’s a suspicious device logged into your account. Here’s exactly how each platform works.

**ChatGPT**

To find out if someone has broken into your ChatGPT account, open it on your computer’s browser, click on your username in the bottom left corner, go to “Settings,” then “Security and Login,” and finally click on “Active Sessions.”

You will see where you are logged into your ChatGPT account. If you see any device you don’t recognize, you can log out of that single device. You can also click on “Log out all.”

At this point, if you want to change your password, you need to log out of your account.

Then, on ChatGPT’s website, click “Log in” located in the bottom-left corner, enter your email address, click on “Forgot password,” and then “Continue.”

ChatGPT will then send you an email containing a six-digit code. Enter the code on the ChatGPT login page, click “Continue,” and then enter a new password.

You can also click “reset your password” in the email you received to see the official instructions on how to do that.

**Claude**

For Claude, open it in your computer’s browser, click on your username in the bottom-left corner, then “Settings,” and click on “Account.” That’s where you will see your “Active sessions.”

If you don’t recognize one of them, hover over it, click on the three vertical dots that appear on the right, and click “Log out” or “Terminate.”

If you want, you can click on “Log out of all devices.”

At that point, you’ll be able to log back into your account using your email address. You will receive an email with a link to log in. Claude does not allow you to use passwords at all, so there’s no password to change.

**Perplexity**

In the case of Perplexity, the AI-powered search engine does not show you where you are logged in.

So if you’re worried someone may have broken into your account, go to Perplexity in your browser and click your username in the bottom-left corner, then “All settings.” Finally, click on “Sign out of all sessions,” and then “Confirm.”