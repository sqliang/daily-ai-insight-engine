---
title: 百度文心助手任务Agent登顶国际权威榜单，超越Claude、GPT拿下全球智能体冠军
source: https://www.qbitai.com/2026/07/457117.html
author:
- '[[量子位的朋友们]]'
published: '2026-07-22'
created: '2026-07-22'
manifest_dates:
- '2026-07-22'
description: ''
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: ccb0a34dcedd10df
source_type: news_media
tldr: 百度文心助手任务 Agent 在 PinchBench v2 评测中以最高分 94.6%、平均分 94.4% 的成绩登顶全球智能体冠军，超越 Claude
  Opus 4.8、GPT-5.6-luna 等模型，百度已将相关技术应用于百度 App 并开源完整评测流程。
objective_summary: 2026 年 7 月 17 日，百度文心助手任务 Agent 在 Kilo AI 推出的 PinchBench v2 评测中以最高分
  94.6%、平均分 94.4% 的成绩夺得全球智能体冠军，超越 Anthropic Claude Opus 4.8、阿里 Qwen3.7-max、OpenAI
  GPT-5.6-luna 等 59 个参评模型。PinchBench v2 覆盖 23 个真实工作场景共 147 项任务，采用自动化校验与 LLM 评审双轨评分机制，全程零人工干预。百度
  AI 搜索团队已在 GitHub 开源完整评测流程供复现，文心助手任务 Agent 核心技术已全面应用于百度 App。该文章由百度提供并授权量子位转载。
event_type: application_landing
epistemic_status: pr_statement
entities:
  companies:
  - Baidu
  - Kilo AI
  - Anthropic
  - Alibaba
  - OpenAI
  - OpenClaw
  technologies:
  - PinchBench
  - 多智能体框架
  - Agent
  key_people: []
key_logic_flow:
- 百度文心助手任务 Agent 在 PinchBench v2 评测中以最高分 94.6%、平均分 94.4% 的成绩登顶全球智能体冠军，超越 59 个参评模型。
- PinchBench v2 由 Kilo AI 推出、OpenClaw 社区维护，覆盖 23 个真实工作场景和 147 项任务，采用自动化校验与 LLM 评审双轨机制。
- 文心助手任务 Agent 在 GitLab 财报分析、Node.js 安全漏洞分析和合同法律分析等复杂任务中均获得满分评分。
- 百度 AI 搜索团队在 GitHub 上开源了完整评测流程，147 个任务的执行快照和交付物全量公开以供复现。
- 文心助手任务 Agent 依托百度搜索猎户座 AI 引擎的多智能体框架构建，将搜索引擎的意图理解能力升级为 Agent 框架。
- 文心助手任务 Agent 核心技术已全面应用于百度 App 及文心助手，用户可在 chat.baidu.com 选择「任务」模式体验。
object_mentions:
- object_type: product
  name: 文心助手任务Agent
  canonical_name: 文心助手任务Agent
  url: https://chat.baidu.com
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 百度文心助手任务 Agent 以最高分 94.6%、平均分 94.4% 的成绩登顶全球工程向 AI 智能体评测榜单 PinchBench v2。
  - 文心助手任务 Agent 依托百度搜索猎户座 AI 引擎的多智能体框架构建，将搜索引擎的意图理解能力升级为 Agent 框架。
  - 文心助手任务 Agent 核心技术已全面应用于百度 App 及文心助手，可登录 chat.baidu.com 选择「任务」模式体验。
  article_id: ccb0a34dcedd10df
- object_type: project
  name: PinchBench
  canonical_name: PinchBench
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - PinchBench 由 Kilo AI 推出、OpenClaw 社区维护，与 MMLU、GPQA 等传统基准不同，它考核智能体能否完成完整任务并交付可验证结果。
  - 当前版本包含 23 个真实工作场景、147 项任务，覆盖数据分析、研究写作、代码开发等七大类别，共完成 617 次测试运行。
  article_id: ccb0a34dcedd10df
- object_type: project
  name: Baidu-AI-Search/PinchBench-Evaluation
  canonical_name: Baidu-AI-Search/PinchBench-Evaluation
  url: https://github.com/Baidu-AI-Search/PinchBench-Evaluation
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 百度 AI 搜索团队在 GitHub 上开源了完整评测流程，147 个任务的执行快照、交付物、LLM Judge 打分理由全量公开。
  - 任何人都可以逐条复现该评测流程。
  article_id: ccb0a34dcedd10df
- object_type: product
  name: 猎户座AI引擎
  canonical_name: 猎户座AI引擎
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - 文心助手任务 Agent 依托百度搜索猎户座 AI 引擎的多智能体框架构建，将搜索引擎的意图理解能力升级为 Agent 框架。
  article_id: ccb0a34dcedd10df
extract_result: success
impact_score:
  score: 5.5
  reason: 评分依据：这是一项有实质内容的工程成果，百度文心助手任务Agent在PinchBench v2上取得了有竞争力的分数，且评测流程已开源、结果可复现。但本文本质是百度授权发布的PR文章（文中明确标注'本文由百度提供，量子位获授权转载'），客观性需打折扣。PinchBench
    v2虽设计合理（23场景147任务，自动化+LLM双轨评分），但其作为新晋评测榜单的行业影响力仍远不及MMLU、GPQA或SWE-bench等成熟基准。文心助手94.4%平均分对第二名的领先幅度（Claude
    Opus 4.8-fast为93.5%）仅约1个百分点，并非碾压式差距。整体属于重要产品里程碑（国内首个以产品身份登顶国际Agent榜的系统），但远未达到行业范式转移级别。给予5.5分。
sentiment: mixed
developer_sentiment:
  tone: skeptical
  primary_focus: PR供稿的评测榜首宣称，以及评测结果在非百度场景下的可复现性
hype_assessment:
  level: medium
  reason: 判定依据：文章使用了'登顶全球智能体冠军'、'最难作假的能力'等情绪化修辞，且明确标注为百度授权转载的PR稿件，存在明显的商业包装。但另一方面，评测流程确实已在GitHub开源（147个任务的执行快照和交付物全量公开），给出的具体评测案例（GitLab财报分析、Node.js漏洞分析、合同分析）有细节支撑且评分合理。这些真实性信号部分对冲了PR包装的影响。综合评估为中等炒作水平，有干货但包装过度。
information_entropy: medium
domain_disruption:
  technical_innovation: 将搜索引擎二十余年积累的意图理解与任务拆解能力升级为多智能体框架，本质上是用系统工程能力（工具调用编排、上下文管理、任务规划）弥补或释放底层模型的潜力。其核心贡献在于证明了Agent框架工程对任务完成率的提升作用可以超越单纯模型参数竞赛，但并未提出新的算法或架构突破。
  business_model: 百度App已全线接入该Agent能力，标志着中国搜索引擎从'信息检索→蓝链列表'向'意图理解→任务执行→交付成果'的商业模式转型。同时开源评测流程意在建立开发者生态信任，吸引第三方开发者验证和采用其Agent框架，这是一种通过开放评测降低采用门槛的生态策略。
engineering_complexity: production_ready
compound_value:
  score: 6.5
  reason: 该事件核心投资逻辑在于验证了'Agent框架工程能力超越模型参数比拼'这一重要行业判断——搭载不同框架的同一底座模型得分差距显著，这意味着价值正在从模型层向中间件层迁移。百度基于20年搜索意图理解积累构建的多智能体框架，具备真实产品集成度（已落地百度App），形成了可复用的系统工程壁垒，这确实具有长期复利潜力。但需审慎折扣：1)
    文章为百度授权PR稿，存在选择性披露偏差和夸大倾向（认识论状态为pr_statement）；2) 94.6% vs 93.5%（Claude Opus 4.8-fast）的领先幅度边际，榜单格局随版本迭代可能快速变化；3)
    PinchBench v2由Kilo AI推出不足半年，作为新兴Agent评测的长期权威性和行业采纳度有待验证；4) 优势高度绑定中文市场和百度搜索生态，全球化复利效应有限；5)
    百度在消费级AI产品领域的商业化能力和开发者生态建设历史上表现平平，能否将技术优势转化为持续产品壁垒存疑。综合评分6.5分：Agent框架作为竞争壁垒的 thesis
    成立且有产品验证支撑，但领先幅度和可持续性需至少2-3个季度跨版本数据才能确认。
value_capture_layer: agent_middleware
moat_impact: creates_new_moat
key_beneficiaries:
- Baidu
- Kilo AI
competitive_casualty:
- 纯模型能力型AI公司
- 传统RPA厂商
- 无搜索生态支撑的Agent初创公司
market_opportunities:
- Agent框架工程能力正在超越模型参数成为核心竞争力，创业团队可聚焦垂直行业Agent框架优化与适配，如金融合规审查、安全漏洞分析等高复杂度场景
- 百度开源了PinchBench完整评测流程，开发者可基于该开源工具构建自身Agent系统的对标测试体系，定位能力短板并迭代优化
- 搜索+Agent融合路径得到验证，企业级知识管理场景（内部文档检索+自动执行任务）存在明确的产品化机会
risk_matrix:
  regulatory: 百度作为中国AI企业，其自主决策Agent在跨境应用场景可能面临数据出境审查；中国AI监管框架对Agent的自主行为边界尚无明确定义，存在合规演进的不确定性
  technological: PinchBench v2成绩可能受益于评测框架特定优化，通用Agent能力未经充分验证；开源评测流程可能被竞品快速针对性优化，榜首地位难以持续保持
  competitive: 头部模型成绩差距极小（最高分94.6% vs 93.5%），竞争白热化且格局快速变动；Anthropic、OpenAI、阿里等竞品将快速迭代Agent框架，领先窗口短暂
  ethical: 自主Agent可执行合同审查、安全漏洞分析等高风险决策任务，如出现判断失误可能导致法律追责或安全事件；无人值守定时任务模式增加了自动化错误被放大的风险
  additional:
  - 该文为百度提供的品牌宣传稿，排行榜成绩可能存在宣传放大效应，需等待第三方独立复现验证
confidence:
  impact: medium
  compound: medium
  hype: high
actionable_insight: monitor
object_insights:
- object_type: product
  name: 文心助手任务Agent
  canonical_name: 文心助手任务Agent
  url: https://chat.baidu.com
  positioning: 百度推出的任务型AI智能体产品，基于猎户座AI引擎多智能体框架构建，将搜索引擎意图理解能力升级为Agent框架。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 百度App用户
  - 文心助手用户
  - 需要自动化完成复杂任务的办公人群
  product_signal: 在PinchBench v2评测中以最高分94.6%、平均分94.4%的成绩超越Claude Opus 4.8、GPT-5.6-luna等59个参评模型，夺得全球智能体冠军。
  market_signal: 产品已全面应用于百度App及文心助手，用户可在chat.baidu.com直接体验任务模式，百度同时开源了完整评测流程供社区验证。
  differentiation: 不同于传统知识记忆型基准，PinchBench考核智能体完成完整任务并交付可验证结果的能力；文心助手任务Agent在GitLab财报分析、Node.js安全漏洞修复等复杂场景均获满分。
  watch_reason: 文心助手任务Agent以正式产品身份而非实验模型登顶国际评测榜单，证明百度在Agent框架工程能力上的积累已转化为实际产品力，且核心技术已全面落地百度App，值得持续跟踪其用户增长与场景拓展。
  risk_notes:
  - 文章由百度提供并授权转载，存在品牌宣传倾向，评测结果的独立客观性需第三方验证。
  - 领先地位可能被后续模型版本或竞品Agent框架快速超越，评测榜单具有时效性。
  score: 8.0
  article_ids:
  - ccb0a34dcedd10df
  evidence_snippets:
  - 百度文心助手任务 Agent 以最高分 94.6%、平均分 94.4% 的成绩登顶全球工程向 AI 智能体评测榜单 PinchBench v2。
  - 文心助手任务 Agent 依托百度搜索猎户座 AI 引擎的多智能体框架构建，将搜索引擎的意图理解能力升级为 Agent 框架。
  - 文心助手任务 Agent 核心技术已全面应用于百度 App 及文心助手，可登录 chat.baidu.com 选择「任务」模式体验。
- object_type: project
  name: PinchBench
  canonical_name: PinchBench
  url: null
  positioning: 由Kilo AI推出、OpenClaw社区维护的工程向AI智能体评测基准，考核智能体完成完整任务并交付可验证结果的能力。
  technical_signal: 采用自动化校验与LLM评审双轨评分机制，全程零人工干预；当前版本覆盖23个真实工作场景、147项任务，涵盖七大类别共完成617次测试运行。
  adoption_signal: 已吸引59个参测模型参与评测，包括Claude Opus 4.8、GPT-5.6-luna等国际前沿模型；百度已基于此基准开源完整复现流程。
  ecosystem_relevance: 与传统知识记忆型基准（MMLU、GPQA）形成差异化，填补了Agent工程能力标准化评测的空白，有望推动Agent框架能力的透明对比。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: PinchBench v2首次引入大规模真实工作场景评测Agent的完整任务交付能力，且百度已开源全量评测流程供复现，有望成为Agent领域的标杆评测基准，值得关注其后续版本迭代和行业采纳度。
  risk_notes:
  - 评测场景和任务数量（23个场景147项任务）仍有限，可能无法全面覆盖真实世界Agent应用。
  - LLM评审本身可能存在偏差，评测方法的持续改进和第三方验证仍需关注。
  score: 6.0
  article_ids:
  - ccb0a34dcedd10df
  evidence_snippets:
  - PinchBench 由 Kilo AI 推出、OpenClaw 社区维护，与 MMLU、GPQA 等传统基准不同，它考核智能体能否完成完整任务并交付可验证结果。
  - 当前版本包含 23 个真实工作场景、147 项任务，覆盖数据分析、研究写作、代码开发等七大类别，共完成 617 次测试运行。
- object_type: project
  name: Baidu-AI-Search/PinchBench-Evaluation
  canonical_name: Baidu-AI-Search/PinchBench-Evaluation
  url: https://github.com/Baidu-AI-Search/PinchBench-Evaluation
  positioning: 百度AI搜索团队在GitHub上开源的PinchBench v2评测复现项目，公开了147项任务的执行快照、交付物和LLM评分，确保评测可验证。
  technical_signal: 完整开源评测复现流程，包括147个任务的执行快照、交付物和LLM Judge打分理由，使评测过程完全透明且可由第三方审验。
  adoption_signal: 作为百度文心助手任务Agent登顶PinchBench的配套开源项目，已吸引社区关注，任何人都可基于此复现评测结果。
  ecosystem_relevance: 降低了Agent工程能力评测的复现门槛，使研究者和开发者可基于同一标准对比不同Agent框架，推动行业评估透明化。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 该开源项目将PinchBench评测全流程透明化，有助于建立Agent工程能力的可复现评估标准，值得关注其在开源社区的采纳度和后续维护更新。
  risk_notes:
  - 项目依赖百度自家评测流程和数据集配置，可能存在对百度Agent框架的隐性优化偏向。
  - 开源项目缺乏明确的长期维护承诺，后续版本更新和社区贡献活跃度有待观察。
  score: 5.0
  article_ids:
  - ccb0a34dcedd10df
  evidence_snippets:
  - 百度 AI 搜索团队在 GitHub 上开源了完整评测流程，147 个任务的执行快照、交付物、LLM Judge 打分理由全量公开。
  - 任何人都可以逐条复现该评测流程，执行快照和LLM打分理由均已公开，确保过程完全透明。
---

# 百度文心助手任务Agent登顶国际权威榜单，超越Claude、GPT拿下全球智能体冠军

2026 年 7 月 17 日，百度文心助手任务 Agent，以最高分 94.6%、平均分 94.4% 的成绩，登顶全球工程向 AI 智能体评测榜单 PinchBench v2。成为首个以正式产品身份获得 PinchBench 总榜第一的国产智能体系统。

在 59 个参评模型中，文心助手任务 Agent 排名第一，领先 Anthropic Claude Opus 4.8-fast（93.5%）、阿里通义千问 Qwen3.7-max（92.5%）、Anthropic Claude Opus 4.8（90.5%）、OpenAI GPT-5.6-luna（88.7%）。

**这个榜单，测的是最难作假的能力**

PinchBench 由 Kilo AI 推出，OpenClaw 社区维护。它和 MMLU、GPQA 这类传统大模型基准的区别很直接：传统基准考「模型知不知道」，PinchBench 考「智能体能不能把整件事做完并交付可验证的结果」。

当前版本包含 23 个真实工作场景、147 项任务，覆盖数据分析、研究写作、代码开发、办公自动化、文档处理、网页操作、多媒体处理七大类别，共完成 617 次测试运行。评分采用「自动化校验 + LLM 评审」双轨机制，全程零人工干预。

更关键的是，PinchBench 用于衡量模型与 Agent 框架的综合能力。即便是同一底座模型，搭载不同 Agent 框架，最终评测得分也会存在较大差距。这也说明，文心助手任务 Agent 取得榜首成绩，代表的是模型能力与系统工程协同打造的综合实力第一。

百度 AI 搜索团队在 GitHub 上开源了完整评测流程（github.com/Baidu-AI-Search/PinchBench-Evaluation），147 个任务的执行快照、交付物、LLM Judge 打分理由全量公开，任何人都可以逐条复现。

**让AI从「动动嘴」，到「迈开腿」**

比如其中一个任务是：「GitLab Q3 2025 财季的实际利润率与指引之间差了多少个基点？」没有给任何数据文件，Agent 需要自主检索 GitLab 财报原文或电话会议记录，定位相关指引，计算出非 GAAP 运营利润率约 18%、超出指引约 500 个基点，并将结论写入指定文件。

五个自动化评分维度——文件创建、指标定位、实际值与指引值提取、基点计算结论——全部满分 1.0。

另一个任务考的是安全工程：分析一个 Node.js 应用的多个 CVE 漏洞，按优先级分级并制定修复计划。评测要求 Agent 识别 express RCE 和 JWT bypass 两个 CRITICAL 级漏洞为 P0，其中 JWT bypass 因存在活跃利用记录需要特别标注；将 PostgreSQL SQL 注入定为 P1 并结合 PCI DSS 支付路径给出上下文；将仅影响构建阶段的依赖漏洞降级为 P2/P3；制定五批次修复计划，附具体部署窗口（4 月 12 日紧急热修、4 月 14 日 P1 批次）。

LLM 评审的评审结论是「所有维度表现卓越」，得分满分 1.0。

还有一个合同法律分析的 case，任务是读取一份软件服务协议，提取关键日期、梳理双方义务、识别风险点、生成财务摘要。这种任务过去需要律师助理花几个小时。文心助手任务 Agent 的输出结果，识别了客户方 12 项风险、供应商 10 项风险、5 项共享风险，付款结构六期分期的现金流前置问题、IP 转让条件的产权间隙，全部做到了——最终评分四个维度都是满分 1.0。

上面这些复杂的任务文心助手任务 Agent 都不在话下，更不用说普通用户的日常办公需求。

比如，你扔给文心助手一份职业数据表，然后说「统一表头格式，新建汇总 sheet，按职业大类做汇总表和 Top10/Bottom10 榜单，生成图表对比各职业大类就业人数。」

这是一条有内部依赖关系的任务链，任何一步出错后面就没法接。文心助手任务 Agent 自主拆解，一次性跑完。

或者你给不了这么详细的指令，想摇个盲盒：「我这周末想从北京去青岛玩两天 solo trip。」没有给任何别的信息。Agent 自主检索了交通、住宿、景点实时数据，排出完整行程、预算清单和避坑指南，交付一份可以直接截图出发的攻略。

或者你不想每次都要问 AI，让它帮你完成重复性又高脑力的劳动，可以设置定时任务，如「每周一晚上十点，帮我汇总近一周的高质量 AI 领域论文，用投研报告风格的 HTML 给我」。

7×24 小时，用户无需时刻在场。

**为什么是百度做出来了？**

答案其实很简单：百度是一家在意图理解上花了 20 多年的公司。

文心助手任务 Agent 依托百度搜索猎户座 AI 引擎的多智能体框架构建。

从架构逻辑来看，搜索引擎本身就是最早的 Agent 雏形——接收意图、拆解任务、调用工具、验证结果，这条链路百度已经跑了二十余年。

工具集从索引爬虫升级成了代码执行环境、文件处理器和实时 API 接口，输出从蓝链列表变成了结构化报告和可运行代码，但底层逻辑一脉相承。

文心助手任务 Agent 将模型任务评估得分提升至 94% 以上，证明优秀的系统架构与工程实现能够显著释放模型潜力。

也就是说，同一个底层模型，换上文心助手任务 Agent 的框架，任务完成率会更高。Agent 时代，框架工程能力的重要性正在超过单纯的模型参数比拼。

目前，文心助手任务 Agent 核心技术已全面应用于百度 App 及文心助手，可登录 chat.baidu.com ，点选「任务」，即可体验。

*本文由百度提供，量子位获授权转载，观点归原作者所有。*

*版权所有，未经授权不得以任何形式转载及使用，违者必究。*