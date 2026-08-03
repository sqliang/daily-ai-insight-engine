---
title: 首个鸿蒙PC开源AI统一工作台JiuwenSwarm，办公编程一站式搞定
source: https://www.qbitai.com/2026/07/462065.html
author:
- '[[思邈]]'
published: '2026-07-29'
created: '2026-07-29'
manifest_dates:
- '2026-07-29'
description: 让多智能体团队随时随地为你干活
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: bcadbce107fae84b
source_type: news_media
tldr: 华为2012实验室、华为云、终端小艺等团队构建的开源AI Agent平台openJiuwen，推出首个面向鸿蒙PC的开源AI统一工作台JiuwenSwarm，支持办公、编程与娱乐场景的多智能体协同，并发布人机协同新范式HITS。
objective_summary: 华为2012实验室、华为云、终端小艺等团队联合构建的开源AI Agent平台openJiuwen，于2026年7月推出JiuwenSwarm蜂群智能体的鸿蒙PC版本，定位为首个面向鸿蒙PC的开源AI统一工作台。openJiuwen社区同时发布人机协同新范式HITS（Human
  in the Swarm），支持人与智能体共同组队、多人多机协同。该工作台覆盖办公（集群模式约20分钟生成200页PPT）、编程（多智能体并行开发并生成可安装的ArkTS应用）与娱乐（智能体组织五子棋与狼人杀）三类场景，全套开源并支持Windows、Mac、HarmonyOS、Ubuntu多平台部署。
event_type: framework_tools
epistemic_status: pr_statement
entities:
  companies:
  - Huawei 2012 Lab
  - Huawei Cloud
  - openJiuwen
  - Feishu
  technologies:
  - HarmonyOS
  - HITS
  - ArkTS
  - Coordination Engineering
  key_people: []
key_logic_flow:
- 开源AI Agent平台openJiuwen由华为2012实验室、华为云、终端小艺等团队联合构建，其联合华为终端平板与PC产品线等团队推出JiuwenSwarm鸿蒙PC版本，这是首个面向鸿蒙PC的开源AI统一工作台。
- openJiuwen社区发布人机协同新范式HITS（Human in the Swarm），人在智能体团队内部与智能体共同组队，支持多人多机协同，将协同工程从智能体之间扩展到人与智能体之间。
- 办公场景下，用户可在鸿蒙PC上通过集群模式让系统自动组建多智能体团队，约20分钟内生成200页高质量PPT，也能用手机飞书远程唤起鸿蒙PC上的汇报材料团队开工。
- 编程场景下，用户可在Code模式集群中组建小型开发团队，前端与后端开发在不同分支独立并行开发后统一合入主干，系统也能自主规划任务并完成ArkTS代码开发，生成可安装运行的应用。
- 娱乐场景下，智能体可担任主持人组织五子棋对局并推荐落子位置，也可在狼人杀中与人类玩家共同组队、讨论、投票、推理与伪装身份。
- JiuwenSwarm全套开源，支持Windows、Mac、HarmonyOS、Ubuntu等多平台安装部署，体验入口在openjiuwen.com官网，代码托管于AtomGit与GitHub。
object_mentions:
- object_type: project
  name: JiuwenSwarm
  canonical_name: JiuwenSwarm
  url: https://github.com/openJiuwen-ai/jiuwenswarm
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - JiuwenSwarm是首个面向鸿蒙PC的开源AI统一工作台，由openJiuwen社区联合华为终端平板与PC产品线、软件部等团队推出，可在桌面办公、编程与娱乐场景中派活、推进和交付任务。
  - JiuwenSwarm全套开源，支持在Windows、Mac、HarmonyOS、Ubuntu等多平台安装部署，鸿蒙PC版本的安装教程和开源代码已发布于openjiuwen.com官网、AtomGit与GitHub。
  article_id: bcadbce107fae84b
- object_type: project
  name: openJiuwen
  canonical_name: openJiuwen
  url: https://www.openjiuwen.com
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - 开源AI Agent平台openjiuwen由华为2012实验室、华为云、终端小艺等团队联合构建，JiuwenSwarm鸿蒙PC版本正是该平台联合华为终端产品线等团队推出的新成果。
  - openJiuwen社区同时发布了人机协同新范式HITS（Human in the Swarm），支持人站在智能体团队内部与智能体共同组队，并支持多人、多机协同。
  article_id: bcadbce107fae84b
- object_type: project
  name: HITS (Human in the Swarm)
  canonical_name: HITS (Human in the Swarm)
  url: null
  confidence: low
  article_role: ecosystem_context
  evidence_snippets:
  - HITS是openJiuwen社区发布的人机协同新范式，人不仅可以站在智能体团队外部，还能与智能体共同组队，支持多人多机协同，把协同工程推进到人与智能体协同的层面。
  article_id: bcadbce107fae84b
extract_result: success
---

# 首个鸿蒙PC开源AI统一工作台JiuwenSwarm，办公编程一站式搞定

让多智能体团队随时随地为你干活

允中 发自 凹非寺

量子位 | 公众号 QbitAI


鸿蒙PC用户终于不用再等。

就在上周，由华为2012实验室、华为云、终端小艺等团队联合构建的**开源Al Agent平台openjiuwen**又有新动向，其联合华为终端平板与PC产品线、软件部等团队，推出了**JiuwenSwarm蜂群智能体的鸿蒙PC版本，这也是首个面向鸿蒙PC的开源AI统一工作台**。

桌面办公、编程，不必再在多个应用间来回切换，一个工作台里就能派活、推进、交付。

同时openJiuwen社区还发布了人机协同的新范式**HITS（Human in the Swarm）**。

人不仅能站在团队外智慧（HOTS，Human on the Swarm），还可以和智能体共同组队，支持多人、多机协同。

这也意味着，JiuwenSwarm把Coordination Engineering（协同工程）又往前推了一步：多智能体之间的协同卷完一轮，现在开始卷人和智能体的协同。

以鸿蒙PC为主场，它还能和飞书、小艺等场景联动，让用户在不同设备和协作环境里持续推进任务。

不管是办公、编程、还是生活娱乐，JiuwenSwarm都能帮你搞定。

# 办公场景：Agent团队帮你高效产出

**人还在高铁上，鸿蒙PC上的AI团队已经开工**

先看一个最能体现HITS的场景：紧急任务来了，人却不在工位。

高铁上突然接到紧急汇报任务。不用等回公司——打开手机飞书，几句话唤起鸿蒙PC上的JiuwenSwarm汇报材料团队，任务立刻开始跑。

真正的变化不是“手机上也能用”，而是人还在路上，活已经在电脑上干着了。

整个过程**人和智能体协同推进**：大纲不满意就打回，碰到技术细节随时拉一个专家智能体进来会诊，页面不好看就中途再加一个美化智能体，最终稿一轮轮验收到能用为止。

人作为团队一员，与多个智能体协同高效办公！

**在鸿蒙PC上，一句话生成200页PPT**

紧急汇报之外，办公里更高频的痛点是批量出材料。

做PPT最难的不是写，是动笔之前：主题怎么拆、材料上哪找、结构怎么搭。

汇报材料一多、时间一紧，一个人很难快速搞定。

在鸿蒙PC上输入主题、受众和风格要求，JiuwenSwarm选择**集群模式**，由系统自动组建一支多智能体团队，几个成员随即分头开工：有的去调研，有的梳理结构，有的补内容，有的负责整合最终结果。

原本串行的“查资料—搭大纲—补页面”，被拆成一条可以多智能体同步推进的任务链。

整个过程，20分钟内就能搞定200页高质量PPT！

# 编程场景：灵感来了，随时帮你实现

前两个案例是高效办公，这个场景展示的是创作与编程：一个临时冒出的念头，能不能变成能跑的应用？

**想玩的游戏商店里没有？那就自己造一个**

第一个案例是有用户想重温小时候的街机坦克大战，翻遍软件商店没找到合适版本，于是在鸿蒙PC上打开JiuwenSwarm，使用**Code下的集群模式**，让系统组一支小型开发团队——

一个成员设计玩法和界面，一个前端开发，一个后端开发，一个做测试验证，Leader统筹节奏。

前端和后端开发分别在**不同分支独立并行开发**，完成后再统一合入主干。

几轮协作之后，坦克大战真的在鸿蒙PC上跑了起来，开发过程中，想到新点子，**还能@某个成员，给他加需求**。

第二个案例更日常，用户正在健身，想给自己做一个简单、干净、够用的热量记录工具。

打开鸿蒙PC上的JiuwenSwarm，切换Code模式，描述需求后，系统**自主规划任务、完成ArkTS代码开发**，经过编译后，生成一个可在鸿蒙PC上安装运行的热量记录应用。

灵感稍纵即逝，难的是做出来——搭架构、写代码、测试验证….JiuwenSwarm直接都帮你搞定。

# 生活娱乐：工作之外，与AI组队游戏

HITS的作用不止于协同办公：下了班，人还能和智能体组队打游戏。

**工作之外，它也能拉你开一局小游戏**

先看一局五子棋小游戏：使用JiuwenSwarm在鸿蒙PC上组建一支五子棋游戏团队，由智能体担任主持人，邀请两位人类玩家入场。

两人都准备好，输入“开始游戏”，对局正式启动。

过程中主持人同步棋盘、维护规则、提醒玩家落子，就像是有人在现场带着玩，不知道下一步棋落在哪儿？智能体还能给你推荐位置。

场景很轻松，但也说明了一件事：智能体不只会埋头干活，还能站出来当组织者，把一件需要多人配合的事从头到尾张罗明白。

**这一次，你亲自入局，与AI同桌博弈**

五子棋里，人还是玩家，智能体是组织者。

狼人杀则是**人和Agent共同组队，沉浸式互动游戏**。

你可以是狼人，可以是预言家，也可以就是个普通村民。

几位AI玩家会和你一起讨论、发言、投票、伪装、带节奏。

它们会读你的发言，推理你的身份，判断你是在认真分析还是在悄悄搅浑水，也可能选择带飞你，或者在关键轮次把票投给你。

在游戏过程中还可以单独@某个成员和他说悄悄话，其他人看不见，比如和狼人玩家对暗号。

到这里，人和AI的关系变了：不再是人盯着AI干活，而是双方坐在同一张桌上“以身入局”，共同推理、博弈、交付。

# 快速上手

办公、编程、娱乐等场景看下来，不如自己跑一遍。

JiuwenSwarm全套开源，支持在**Windows、Mac、HarmonyOS、Ubuntu**等多平台安装部署。访问官网，即可立即体验鸿蒙PC版本，再配置好模型服务，就能快速开启你的多智能体任务。

JiuwenSwarm鸿蒙PC版本安装教程和开源代码链接如下:

**立即体验：**https://www.openjiuwen.com/download

**AtomGit: **https://atomgit.com/openJiuwen/jiuwenswarm/tree/openharmony

**GitHub: **https://github.com/openJiuwen-ai/jiuwenswarm/tree/openharmony

# 写在最后

三个场景六个案例，从协同办公、开发应用、再到沉浸式游戏，落点是同一个：任务不再交给单个智能体，而是交给一支队伍；人也不再站在队伍外面，而是和智能体共同组队。

对鸿蒙PC用户来说，这一次终于不用再等：JiuwenSwarm蜂群智能体支持鸿蒙PC，把统一工作台连同多智能体团队一起交到你手里——灵感来了即刻开工，人在高铁上一句话也能唤醒它，让多智能体团队随时随地为你干活。

更值得关注的是HITS（Human in the Swarm），它回答的是**多智能体时代人站在哪**的问题：不只是在流程外面点同意，而是带着身份走进蜂群，和智能体一起推理、博弈、交付。

智能体会协同，人也在协同之中，这才是完整的人机协同。

最后说一句：JiuwenSwarm是**全套开源**的。

如果看完这几个案例你也有点心动，不妨访问源码或去官网立即体验鸿蒙PC版本，亲手组一支自己的智能体团队试试。