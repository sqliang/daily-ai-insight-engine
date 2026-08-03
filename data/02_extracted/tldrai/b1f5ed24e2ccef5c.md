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