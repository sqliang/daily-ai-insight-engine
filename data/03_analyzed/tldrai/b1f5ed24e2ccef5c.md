---
title: Gemini Robotics ER 2 (1 minute read)
source: https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-robotics-er-2/?utm_source=tldrai
author: []
published: ''
created: '2026-08-01'
manifest_dates:
- '2026-08-01'
- '2026-08-02'
description: TLDR AI 每日头条
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: b1f5ed24e2ccef5c
source_type: news_media
tldr: 谷歌 DeepMind 发布具身推理模型 Gemini Robotics ER 2，作为机器人高级大脑，可对话、理解物理世界并规划多步任务，将动作执行交由底层
  VLA 模型完成。该模型已通过 Gemini API 与 Google AI Studio 向开发者公开，较 ER 1.6 在进度追踪、工具编排与多机器人协作上显著提升。
objective_summary: 谷歌 DeepMind 正式推出具身推理模型 Gemini Robotics ER 2，该模型充当机器人高级大脑，负责与人类对话、理解物理世界与规划多步任务，并把电机执行交给底层视觉-语言-动作（VLA）模型。新模型支持原生调用
  Google Search 等工具，通过持续视频流实现进度追踪与自我纠错，并新增多机器人协作能力。模型已通过 Gemini API 与 Google AI Studio
  向开发者公开发布，同时在 Gemini Enterprise Agent Platform 提供私有预览。官方评测显示其在三种控制模式下均优于 ER 1.6，进度分类准确率达
  57.4%，超过前代与竞品前沿模型。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - Google DeepMind
  - Boston Dynamics
  - Google
  technologies:
  - Gemini Robotics ER 2
  - VLA
  - Gemini Live API
  - Gemini Enterprise Agent Platform
  - Google AI Studio
  key_people: []
key_logic_flow:
- 谷歌 DeepMind 正式推出具身推理模型 Gemini Robotics ER 2，它充当机器人的高级大脑，负责与人类对话、理解物理世界并规划多步任务。
- Gemini Robotics ER 2 将电机执行交由底层视觉-语言-动作（VLA）模型完成，并能原生调用 Google Search 等工具，实现边执行边思考的并行推理。
- 相较上一代 ER 1.6，新模型通过连续视频流追踪任务进度、在出错时自我纠错，并新增多机器人协作能力，可共同完成复杂工作流。
- 该模型已通过 Gemini API 与 Google AI Studio 向开发者公开发布，并在 Gemini Enterprise Agent Platform
  上提供私有预览，同时公开了模型配置与提示词示例。
- 官方评测显示，Gemini Robotics ER 2 在真实 VLA、模拟 VLA 与人工远程操控三种控制模式下，工具编排性能均优于 ER 1.6。
- 在进度分类任务上模型取得 57.4% 的准确率，领先前代与竞品前沿模型，并在关键时刻定位任务上取得显著进步。
object_mentions:
- object_type: model
  name: Gemini Robotics ER 2
  canonical_name: Gemini Robotics ER 2
  url: https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-robotics-er-2/
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 谷歌 DeepMind 正式发布 Gemini Robotics ER 2，这是其最强大的具身推理模型，充当机器人的高级大脑，让机器人能与人类对话、理解物理世界并规划多步任务。
  - Gemini Robotics ER 2 已通过 Gemini API 与 Google AI Studio 向开发者公开发布，并在 Gemini Enterprise
    Agent Platform 上以私有预览形式提供。
  - 官方评测显示该模型在进度分类任务上达到 57.4% 准确率，并领先前代与竞品前沿模型。
  article_id: b1f5ed24e2ccef5c
- object_type: model
  name: Gemini Robotics ER 1.6
  canonical_name: Gemini Robotics ER 1.6
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Gemini Robotics ER 2 较上一代 ER 1.6 显著升级，通过连续视频流让机器人追踪自身进度、出错时自适应调整，并新增多机器人协作能力。
  - 官方评测显示 Gemini Robotics ER 2 在真实 VLA、模拟 VLA 与人工远程操控三种控制模式下的工具编排性能均优于 ER 1.6。
  article_id: b1f5ed24e2ccef5c
- object_type: product
  name: Spot
  canonical_name: Boston Dynamics Spot
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - 谷歌与合作伙伴波士顿动力合作，使用 Gemini Robotics ER 2 编排 Spot 的导航与机械臂 API，打造能根据自然语言指令取物的交互式机器人。
  article_id: b1f5ed24e2ccef5c
- object_type: product
  name: Gemini Live API
  canonical_name: Gemini Live API
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - Gemini Robotics ER 2 接入 Gemini Live API，使用面向低延迟任务优化的双向流式端点，实现流畅的动作编排并避免任务间的卡顿停顿。
  article_id: b1f5ed24e2ccef5c
extract_result: success
impact_score:
  score: 7.0
  reason: 该发布将具身智能领域'大脑-身体'解耦的架构范式推向产品化：高层次具身推理（对话、物理理解、多步规划）与低层 VLA 执行分离，通过原生工具编排连接，这对机器人
    AI 技术栈是一次清晰的定型，且模型已通过 Gemini API 公开开放并与 Gemini Live API 双向流式集成，开发者可立即使用，短期内会在具身智能开发者社区产生显著影响并改变局部竞争格局。但机器人
    AI 仍属相对细分赛道，57.4% 的进度分类准确率在绝对值上并不惊艳，且是对 ER 1.6 的渐进式升级而非范式转移，故给 7.0 分。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 脑体分离编排架构——如何用 ER 2 作为统一大脑编排任意 VLA 模型与机器人 API，实现边执行边思考的流畅物理任务
hype_assessment:
  level: low
  reason: 文章给出了可验证的具体证据：三控制模式（真实 VLA、模拟 VLA、人工远程操控）下的工具编排评测数据、57.4% 的进度分类准确率、公开的 GitHub
    代码示例与可直接调用的 API 入口，并展示了与 Boston Dynamics Spot 的真实演示。虽使用了 'most capable' 等营销措辞，但整体属于有实底的产品发布，未出现'颠覆''革命性'等空泛概念炒作，水分较低。
information_entropy: high
domain_disruption:
  technical_innovation: 核心突破在于将具身推理模型（负责对话、物理世界理解与多步任务规划）与底层 VLA 模型彻底解耦，通过原生工具编排实现'边执行边思考'的并行推理架构；并引入基于连续视频流的进度分类与关键时刻定位能力，使机器人具备实时态势感知、自我纠错与精确任务切换，同时新增多机器人协作共享空间的协同能力。
  business_model: 谷歌借此将自身定位为机器人技术栈的'大脑层'平台，通过 Gemini API 按用量计费，机器人厂商可订阅式获得智能推理能力而无需自研大脑模型；Gemini
    Enterprise Agent Platform 的私有预览指向企业级部署市场，可能推动具身智能商业模式从硬件销售转向 AI 服务订阅与平台抽成。
engineering_complexity: production_ready
compound_value:
  score: 7.5
  reason: 具身推理层是物理 AI 产业链中具备平台属性的环节——它把'思考'与'执行'解耦，理论上可挂接任意 VLA 模型与机器人硬件，一旦成为事实标准将获得类似
    LLM 时代的认知层复利。谷歌 DeepMind 拥有三重杠杆：Gemini 前沿模型底座、Google Search 原生工具调用、Gemini Live
    API 低延迟流式端点，并通过 Gemini API 与 Gemini Enterprise Agent Platform 构建了从开发者到企业侧的完整分发通道，具备成为机器人'高级大脑'基础设施的禀赋。但需清醒看到风险：当前技术成熟度仍低（进度分类准确率仅
    57.4%），机器人本体与 VLA 层碎片化严重，OpenAI/Figure、NVIDIA GR00T、Physical Intelligence 等强敌环伺，'脑层'存在被
    API 商品化稀释单点议价权的可能。综合判断 7.5 分：有潜力成为物理智能细分赛道的基础设施，但 3-5 年后能否仍是行业基石，取决于谷歌能否把搜索集成、多机器人协作与低延迟推理构筑成可持续护城河。
value_capture_layer: foundation_model
moat_impact: creates_new_moat
key_beneficiaries:
- Google DeepMind
- Boston Dynamics
- Google Cloud
- VLA 模型厂商
- 具身智能初创公司
competitive_casualty:
- 闭源机器人规划/控制软件厂商
- 自研高级推理层的机器人厂商
- 传统工业机器人软件栈
market_opportunities:
- 开发者可基于 Gemini Robotics ER 2 构建机器人'高级大脑'编排层，将 VLA 模型、导航 API 与工具调用封装为可配置的 agentic
  工作流，降低具身智能应用的门槛，主打'无需自研推理模型'的差异化方案
- 多机器人协作能力催生群组任务编排与调度软件的机会，可面向仓储、物流、制造等场景开发多机协同工作流管理平台，弥补单体机器人无法完成的复杂任务缺口
- 进度分类与关键时刻定位能力可用于开发机器人在线任务验收与自纠错中间件，面向工业质检、复杂装配等场景提供'边执行边验证'的实时监控与异常重试产品
risk_matrix:
  regulatory: 机器人进入真实物理环境执行任务将面临日益严格的机器人安全标准与产品责任法规（如欧盟 AI Act 对高风险机器人系统的合规要求），同时该模型通过
    Google API 分发，存在地缘政治导致的跨境访问限制与出口管制风险
  technological: Gemini Robotics ER 2 为闭源 API 形态，过度依赖将带来供应商锁定与模型被弃用或改版的风险；底层 VLA 模型与开源替代方案演进迅速，推理层与动作层解耦的设计也可能被更轻量的端到端方案取代
  competitive: OpenAI、NVIDIA、Figure、Tesla 等玩家在具身智能领域密集布局，谷歌以闭源 API 形态切入，面临开源生态（如开源
    VLA 模型）的挤压和巨头间价格战，多机器人编排能力也快速被竞争对手复刻
  ethical: 机器人在共享物理空间运行涉及人身安全与责任归属问题；持续视频流采集环境数据带来隐私泄露与数据伦理风险；物流、制造等场景的多机器人协作可能加速低技能岗位的替代与就业冲击
  additional:
  - 当前进度分类准确率仅 57.4%，距工业级可靠仍有关键差距，实际落地可能存在过度承诺后的预期回落；模型配置、提示词与工具接口的碎片化增加开发者学习与集成成本
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: deep_dive
---

# Introducing Gemini Robotics ER 2

For robots to assist humans in everyday environments, accurate spatial reasoning is not enough. Robots must also think fast, timing their decisions and reasoning with the real-time speed of the physical world.

That’s why today we’re launching Gemini Robotics ER 2, our most capable “embodied reasoning” model for robotics. Think of Gemini Robotics ER 2 as a high-level brain for robots. It allows robots to chat with humans, understand the physical world, and plan multi-step tasks. It then hands off motor execution to any given lower level vision-language-action (VLA) model. Gemini Robotics ER 2 can also natively call tools like Google Search to find information, or any other user-defined function. The design of Gemini Robotics ER 2 allows the robot to “think” about what comes next while simultaneously performing its actions.

Gemini Robotics ER 2 represents a significant upgrade over Gemini Robotics ER 1.6. By watching continuous video feeds, robots can now track their own progress, adapt if something goes wrong, and know exactly when to move on to the next step. We are also introducing multi-robot collaboration, enabling robots to work together in shared spaces and complete complex workflows a single robot could not do alone.

Gemini Robotics ER 2 is now publicly available to developers via the Gemini API, Google AI Studio, and in private preview on Gemini Enterprise Agent Platform. To help you get started, we’re sharing examples of how to configure the model and prompt it to power more useful physical AI tasks.

## Advancing physical agentic capabilities

Most tasks in the physical world are complex and require multiple steps to complete. Gemini Robotics ER 2 is a physical agent, orchestrating steps for the robot and enabling it to self-correct, and generalize to more novel situations. To build an agentic setup, developers can declare low-level control interfaces — like Vision-Language-Action (VLA) models or navigation APIs — as tools, and stream multimodal video, audio, or text directly into the model.

Gemini Robotics ER 2 improves this tool orchestration workflow. We can evaluate its performance with robots in simulation, using real-world robot control, and even pair it with a human controlling the robot remotely.

Gemini Robotics ER 2 consistently outperforms ER 1.6 for tool orchestration across three control modes: real VLA, sim VLA, and human tele-op.

In robotics, high-level reasoning depends on execution speed. Gemini Robotics ER 2 integrates into the Gemini Live API, using a bidirectional streaming endpoint optimized for latency-sensitive tasks. The result is fluid orchestration: Gemini Robotics ER 2 commands action models and robotics APIs to complete multi-step tasks without the jarring “stop-and-think” pauses.

To illustrate this, we’ve built a demo with Spot from our partners at Boston Dynamics. We use Gemini Robotics ER 2 to orchestrate Spot APIs, such as navigation and manipulator movement, creating an interactive robot that fetches objects for you.

Gemini Robotics ER 2 powered Boston Dynamic Spot fetches a popcorn snack up on a natural language command.

The code is available on Github with other examples.

## Unlocking temporal intelligence for robust task completion

One of robotics’ hardest challenges is knowing when a task is done. Gemini Robotics ER 2 brings a step-change in video understanding and progress tracking to verify that complex tasks — such as tightening a light bulb or tying a trash bag — are complete to specification before switching to the next task.

In this update, we’ve made progress on two foundational capabilities for task progress understanding: progress classification and moment finding.

### Continuous progress classification

Progress classification refers to a robot’s ability to track progress towards task completion. In our evaluations, we assign each frame in a video feed into five levels of progress (0-20%, 20-40%, 40-60%, 60-80%, 80-100%). By quantifying task progress, Gemini Robotics ER 2 provides robots with real-time situational awareness, and allows them to adjust actions on the fly or retry failed steps without restarting an entire workflow.

Gemini Robotics ER 2 achieves 57.4% accuracy on progress classification tasks, outperforming previous generation models and competing frontier models.

### Precision moment-finding

Moment-finding measures a model's ability to identify the exact video frame where a critical event takes place (i.e. when to stop pouring coffee into a cup). Gemini Robotics ER 2 achieves significant gains in performance on moment finding, enabling robots to precisely switch between tasks, verify success and suggest corrections.