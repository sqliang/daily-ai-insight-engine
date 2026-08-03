---
title: 100%开源！吴恩达做了个个人桌面Agent
source: https://www.qbitai.com/2026/07/460892.html
author:
- '[[文婷]]'
published: '2026-07-25'
created: '2026-07-26'
manifest_dates:
- '2026-07-26'
- '2026-07-27'
description: 开源、隐私、本地优先、模型无关
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: cf2f8df7da9c057a
source_type: news_media
tldr: 吴恩达发布开源桌面Agent项目OpenWorker（MIT许可证），主打本地优先、隐私保护和模型无关，支持自带API Key接入GPT 5.6 Sol、Claude
  Fable、Gemini 3.6等多种模型，可连接超过25种办公工具并自主完成跨应用交付工作，执行关键操作前需经用户批准。
objective_summary: 2026年7月，DeepLearning.AI创始人吴恩达在GitHub上开源了桌面Agent项目OpenWorker，采用MIT许可证。OpenWorker是一个本地优先、隐私保护和模型无关的AI
  Agent，用户可携带自有API Key接入GPT 5.6 Sol、Claude Fable、Gemini 3.6等模型，或通过Ollama运行DeepSeek、Kimi、GLM等开放权重模型。它能连接超过25种工具（包括GitHub、Slack、Jira、Notion、Outlook、Google
  Calendar等），自主拆解任务并交付成品文件，在执行发消息、改日历、写外部工具或执行终端命令等关键操作前会暂停并请示用户批准。目前处于公开测试阶段，已支持Mac，Windows版本即将上线。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - DeepLearning.AI
  - Coursera
  - Stanford University
  - Google Brain
  - Baidu
  technologies:
  - MCP
  - Ollama
  - MIT License
  - GPT 5.6 Sol
  - Claude Fable
  - Gemini 3.6
  - Kimi
  - GLM
  - DeepSeek
  - Inkling
  key_people:
  - Andrew Ng
key_logic_flow:
- 吴恩达在GitHub上开源了桌面Agent项目OpenWorker，采用MIT许可证，目前处于公开测试阶段，已支持Mac，Windows版本即将上线。
- OpenWorker主打开放、本地优先、隐私保护和模型无关四大特性，用户数据默认只保留在本地设备上，不强制绑定任何特定模型厂商。
- 用户可携带自有API Key接入GPT 5.6 Sol、Claude Fable、Gemini 3.6等模型，或通过Ollama运行DeepSeek、Kimi、GLM、Inkling等开放权重模型。
- OpenWorker能够连接超过25种工具，包括GitHub、Slack、Jira、Notion、Linear、HubSpot、Outlook、Gmail、Google
  Calendar等，并支持通过MCP扩展更多工具。
- 在执行发送消息、修改日历、写入外部工具或执行终端命令等关键操作前，OpenWorker会暂停并请示用户，只有获得批准后才继续执行，未批准的请求会进入待确认列表。
object_mentions:
- object_type: project
  name: OpenWorker
  canonical_name: OpenWorker
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 吴恩达在GitHub上开源了桌面Agent项目OpenWorker，采用MIT许可证，目前处于公开测试阶段。
  - OpenWorker可以连接超过25种工具，包括GitHub、Slack、Jira、Notion、Outlook、Gmail、Google Calendar等办公和项目协作工具。
  - 用户只需携带自己的API Key，即可接入GPT 5.6 Sol、Claude Fable、Gemini 3.6等模型，或通过Ollama运行Kimi、GLM、DeepSeek等开放权重模型。
  - 在执行发送消息、修改日历、写入外部工具或执行终端命令等关键操作前，OpenWorker会暂停并请示用户，获得批准后才继续执行。
  article_id: cf2f8df7da9c057a
extract_result: success
impact_score:
  score: 7.0
  reason: 吴恩达作为AI教育领域最具号召力的人物之一，其亲自下场发布开源桌面Agent对行业有显著示范效应。OpenWorker以MIT许可证开源，主推本地优先、模型无关、自带API
    Key四大特性，直接挑战当前主流AI Agent的封闭生态和厂商锁定模式。短期内将引发大量开发者和企业试用、fork和二次开发，推动桌面Agent从浏览器/编辑器限定场景走向全桌面自动化。但项目仍处于公开测试阶段（仅Mac可用，Windows即将上线），功能成熟度和工具生态完备性尚需验证，距ChatGPT级别的范式转移尚有距离。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: MIT开源+模型无关+本地优先的桌面Agent框架，支持自带API Key接入GPT/Claude/Gemini/DeepSeek等多种模型
hype_assessment:
  level: medium
  reason: 标题'100%开源！'和'AI同事'等表述带有明显的营销包装色彩，但项目本身是真实可用的开源产品，MIT许可证、25+工具集成、MCP扩展、审批机制等特性均为实质内容，并非空壳概念。'模型无关'和'本地优先'的定位虽有差异化价值，但并非革命性技术突破，存在适度包装。
information_entropy: high
domain_disruption:
  technical_innovation: 本地优先的桌面Agent运行时架构，通过MCP协议实现工具生态可插拔扩展，设计了一套关键操作需用户批准的审批机制（暂停执行→说明意图→等待批准→继续执行），以及插件式LLM后端抽象层支持云端模型和本地Ollama模型无缝切换
  business_model: 自带API Key（BYOK）模式颠覆了传统Agent SaaS按订阅收费的商业模式，用户自行选择模型和基础设施，有望推动开源Agent成为企业级桌面自动化的新范式，可能形成社区版免费+企业版增值服务的分层商业路径
engineering_complexity: prototype
compound_value:
  score: 8.0
  reason: 吴恩达的个人品牌与DeepLearning.AI的社区影响力（700万+学员）为OpenWorker提供了极强的冷启动势能。MIT许可证+模型无关+本地优先三大特性对齐了企业级用户对数据主权和供应商锁定的核心焦虑，有望成为'桌面Agent的Linux'。关键复利在于：1)
    25+工具连接器+MCP扩展协议构成平台网络效应——每多一个工具连接器，生态价值非线性增长；2) 跨模型兼容（GPT 5.6 Sol/Claude Fable/Gemini
    3.6/Ollama开放模型）使其天然成为模型厂商的'分销渠道'，不会被单一模型绑定；3) '交付成品'的范式（而非聊天式建议）显著提升了用户粘性和转化漏斗。风险在于目前仅Mac版本且处于公测阶段，Agent可靠性、Windows适配速度以及社区治理模式仍需验证。如果OpenWorker能成为桌面Agent的默认运行时，其复利效应可达8分以上级别。
value_capture_layer: agent_middleware
moat_impact: democratizes_access
key_beneficiaries:
- Ollama
- Anthropic
- DeepLearning.AI
- MCP 生态系统
competitive_casualty:
- UiPath
- Automation Anywhere
- 闭源桌面 Agent 初创公司
- 单一模型绑定的 Agent 平台
market_opportunities:
- 企业可将OpenWorker作为基础框架，针对法务、财务、HR等垂直业务场景开发定制化工作流Agent，提升跨工具办公自动化效率
- 围绕MCP协议生态，开发者可构建OpenWorker专属工具连接器和插件市场，通过付费插件或企业级集成服务实现商业化
- 面向个人知识工作者，可利用OpenWorker的模型无关特性打造本地优先的AI秘书服务，以隐私保护为差异化卖点切入高端用户市场
risk_matrix:
  regulatory: 桌面Agent可访问本地文件与终端命令，在跨境企业场景中可能触及数据本地化法规（如GDPR、中国数据安全法），使用云API时数据出境需额外合规审查
  technological: 操作系统厂商（Apple Intelligence、Windows Copilot）正将类似桌面Agent能力原生集成进系统，可能对OpenWorker形成底层替代；开源Agent框架竞争加剧（如AutoGPT、CrewAI等），架构差异化窗口有限
  competitive: 科技巨头有OS层权限优势和用户基数优势，一旦深度集成桌面Agent能力，将对OpenWorker等第三方开源方案形成生态挤压；且主流AI模型厂商可能推出自有Agent产品加剧竞争
  ethical: Agent拥有文件读写、消息发送、终端执行等高权限操作能力，尽管设计了用户审批机制，但误用或被恶意利用仍可能导致数据泄露、信息误发或系统破坏；非专业用户可能难以审慎判断Agent的每项操作请求
  additional: []
confidence:
  impact: high
  compound: medium
  hype: high
actionable_insight: deep_dive
object_insights:
- object_type: project
  name: OpenWorker
  canonical_name: OpenWorker
  url: null
  positioning: 吴恩达开源的桌面Agent项目，采用MIT许可证，主打开放、本地优先、隐私保护和模型无关，能连接25+工具并自主交付成品文件。
  technical_signal: 采用MIT许可证完全开源，支持自带API Key接入GPT、Claude、Gemini等多种模型，也可通过Ollama运行本地开放权重模型，并通过MCP扩展工具生态。
  adoption_signal: 由AI教育领袖吴恩达主导开源，已支持Mac平台运行，Windows版本即将上线，目前处于公开测试阶段。
  ecosystem_relevance: 可连接超过25种办公及协作工具（GitHub、Slack、Jira、Notion等），不绑定任何特定模型厂商，能与主流闭源及开源模型协同工作。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 吴恩达的品牌效应与AI教育影响力为OpenWorker带来天然关注度，其本地优先、模型无关的设计理念直击当前AI Agent隐私和锁定痛点，可能重塑桌面Agent竞争格局。
  risk_notes:
  - 项目目前仍处于公开测试阶段，仅支持Mac平台，功能稳定性和跨平台兼容性有待验证。
  - 跨应用自主操作涉及复杂的权限管理和安全边界问题，用户批准机制在真实复杂场景中的有效性仍需观察。
  score: 8.0
  article_ids:
  - cf2f8df7da9c057a
  evidence_snippets:
  - 吴恩达在GitHub上开源了桌面Agent项目OpenWorker，采用MIT许可证，目前处于公开测试阶段。
  - OpenWorker可以连接超过25种工具，包括GitHub、Slack、Jira、Notion、Outlook、Gmail、Google Calendar等办公和项目协作工具。
  - 用户只需携带自己的API Key，即可接入GPT 5.6 Sol、Claude Fable、Gemini 3.6等模型，或通过Ollama运行Kimi、GLM、DeepSeek等开放权重模型。
  - 在执行发送消息、修改日历、写入外部工具或执行终端命令等关键操作前，OpenWorker会暂停并请示用户，获得批准后才继续执行。
---

# 100%开源！吴恩达做了个个人桌面Agent

开源、隐私、本地优先、模型无关

##### 文婷 发自 凹非寺

量子位 | 公众号 QbitAI

**AI教育大佬吴恩达也下场做AI同事了。**

不只是陪你聊天，也不只是给你列一个待办清单。

而是你说一句“帮我准备客户brief”，它就能跨文件、日历、Slack这些日常工具自己干活，最后把整理好的文档、写好的消息、更新后的日程交到你手上。

项目名为**OpenWorker**，现已在GitHub开源，采用MIT License。

OpenWorker主打四件事：**开放**、**本地优先、隐私保护**以及**模型无关**。

吴恩达在推上表示，OpenWorker已经可以在Mac上运行，Windows版本也即将上线。

**它不绑定任何特定模型。**你只需带上自己的 API Key，即可接入 GPT 5.6 Sol、Claude Fable、Gemini 3.6，或是通过 Ollama 运行 Kimi、GLM、DeepSeek、Inkling 等开放权重模型。

同时，**你的数据只会保留在你自己的设备上**，除非你主动选择使用特定的 LLM 服务商或第三方集成功能。

吴恩达在X上对它的定位很直接：**这是一个open-source agent**，不只是和你聊天，而是deliver finished work。

直抒胸臆就是：**别光陪我聊天，帮我把活干了。**

这很吴恩达。

过去几年，他一直在强调AI Agent和工作流的重要性。

这次OpenWorker开源，某种意义上也把这个判断又往前推了一步：Agent的下一站，不只在浏览器里，也不只在代码编辑器里，而是在我们的桌面上。

那么，这个OpenWorker到底能干什么？为什么它值得关注？真正的看点在哪？

一起来看：

## 吴恩达，开始造AI同事了

OpenWorker的一大看点，在于其开源者是**吴恩达**。

他是**DeepLearning.AI创始人**、**Coursera联合创始人**，也是**斯坦福大学计算机科学系兼职教授**。

此前，他曾牵头创立**Google Brain项目**，并担任**百度首席科学家**。

除了学术和产业履历，**吴恩达在AI教育领域的影响力同样突出。**

2011年，吴恩达在斯坦福开设了一门在线机器学习课程，吸引逾10万名学生参与。

次年，他与Daphne Koller联合创办了全球知名慕课平台（MOOC）**Coursera**。

据其个人官网数据，**目前已有超过700万人通过他的课程学习人工智能。**

因此，OpenWorker不是某个开发者随手放到GitHub上的实验项目。

吴恩达这一次瞄准的，仍然是**降低AI的使用门槛。**

只不过，**过去交付的是课程；**

**这一次，交付的是一个AI同事。**

## 不给建议，直接给成品

OpenWorker与普通聊天机器人最直接的区别，可以用**“交付”**一词概括。

之前使用大模型，通常需要经历一条漫长的任务链，即先让AI分析需求，再让它生成文本，然后自己查找文件、核对数据、调整格式，最后打开Slack、邮箱或者日历，把结果发出去。

在这个过程中，AI虽然参与了工作，但我们仍然需要在不同软件之间来回倒腾、收拾残局。

现在，**OpenWorker想把这条链路接起来。**

我们只需要告诉它希望得到什么结果，它便会自行拆解任务，调用电脑中的文件、终端和已连接的应用，完成具体操作，最后交付一份能够打开、修改和分享的文件。

比如让它准备一份客户简报，它不只会列出简报应该包含哪些内容，而是会寻找相关资料、整理客户信息，再生成完整文档。

让它检查项目进度，它也可以前往Jira和GitHub搜集信息，而不是等着用户把所有背景材料一段段喂给它。

OpenWorker项目主页显示，它可以**连接超过25种工具**，包括GitHub、Slack、Jira、Notion、Linear、HubSpot、Outlook、Gmail、Google Calendar等，能调用本地文件与终端。

并且，如果你觉得这25种工具不够用，**还可以通过MCP继续为它接入更多的工具。**



此外，OpenWorker还能与大模型相互配合、共同执行**定时任务**。

比如每天早上定时整理一份信息简报，每周自动生成工作报告，或者持续关注某个Slack频道等，都可以交给它处理。

这么看下来，OpenWorker更像是给大模型配上了办公桌、电脑和一串工具账号。

**大模型负责思考，OpenWorker负责让它真正动手。**

听起来真像一对配合默契的工作伙伴！

## 能干活，也能主动请示、不自作主张

不过，当AI从回答问题走向操作电脑，风险也跟着变了。

一段回答写错了，可以重新生成。

但如果AI把你准备发给朋友的吐槽发给领导、删错没有备份的重要文件、改错日程，事情就没有那么简单了。

对此，OpenWorker给出的解决方式是**“在执行重要操作前，先回来请示。”**

当任务涉及发送消息、修改日历、写入外部工具或者执行终端命令时，它会先暂停操作，向我们说明自己准备做什么。只有获得批准后，它才会继续执行。

如果我们不在电脑前，但OpenWorker又刚好执行到了发消息、改文件、运行命令这类关键步骤，**它也不会为了赶着完成任务就跳过确认，而是会先把请求放进待确认列表，等我们回来同意了后再继续做。**

这条设计看起来不起眼，却决定了AI Agent能不能真正进入办公场景。

毕竟，一个合格的AI同事可以勤快，但不能擅作主张。

**它既要有能力把工作推进下去，也要知道哪些事情必须由人拍板。**

## 模型随便换，数据可以留在本地

除了直接交活，OpenWorker还强调四个特点：**开源、本地优先、隐私保护以及模型无关。**

OpenWorker整个项目**已采用MIT许可证开源**，开发者可以查看代码、修改功能，也可以按照自己的工作流程进行部署。

它也**不把用户绑定在某一家模型厂商上**。

**只要你带上自己的API key**，就可以接入OpenAI、DeepSeek、Kimi等模型，也可以通过Ollama运行本地模型。

**这样可自由多了！**因为假如说今天GPT涨价了或者不好用，我随时都可以切换成Kimi或其他模型。

此外，OpenWorker的Agent循环、对话记录、连接器令牌和模型密钥都默认保存在我们自己的设备上。

只有当我们主动选择使用特定的LLM服务商或第三方集成功能时，相应的数据才会离开本机。

不过这也**并不意味着数据绝对不会上传云端。**

但至少我们将更多的选择权保留在了自己的手中，比如“使用哪个模型、连接哪些工具、把数据交给谁”等。

另外，我看了一眼OpenWorker项目主页，它**目前仍处于公开测试阶段**，GitHub上也已经放出了两个Windows安装包，分别适配Windows 10和Windows 11。