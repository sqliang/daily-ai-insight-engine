---
title: 5 Fun Agentic AI Papers to Read
source: https://www.kdnuggets.com/5-fun-agentic-ai-papers-to-read
author:
- '[[Kanwal Mehreen]]'
published: '2026-08-14'
created: '2026-08-15'
manifest_dates:
- '2026-08-15'
- '2026-08-16'
- '2026-08-17'
description: If you read only five papers on AI agents, make them these.
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: cc30dd8dc6a3ac8e
source_type: news_media
tldr: KDnuggets 发布'5 Fun 系列'第二篇文章，推荐五篇入门 agentic AI 的论文。文章逐一讲解 ReAct、Toolformer、Generative
  Agents 与 Voyager，分别阐释推理与行动结合、自监督工具调用、记忆反思与规划等现代 AI agent 的核心思想。
objective_summary: KDnuggets 发表了一篇面向初学者的推荐类文章，属于其'5 Fun 系列'，目的是帮助读者通过阅读少量关键论文来理解现代
  AI agent，而非直接阅读长篇综述。文章逐一介绍了 ReAct（推理与行动交替的提示框架）、Toolformer（语言模型自监督学会调用外部工具）、Generative
  Agents（在模拟人生风格环境中模拟可信人类行为的智能体）以及 Voyager（开放式的具身智能体）。每篇论文被用来解释 agentic AI 的一个核心思想，包括推理、工具使用、记忆与规划。文章指出
  ReAct 奠定了现代 agent 的'思考、行动、观察、更新'基本循环，Toolformer 使模型能自主决定何时借助外部帮助，Generative Agents
  则强调记忆与反思对行为连续性的价值。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - Stanford University
  - Google
  - Meta AI
  - NVIDIA
  - Princeton University
  technologies:
  - ReAct
  - Toolformer
  - Generative Agents
  - Voyager
  - LLM
  - agentic AI
  - self-supervised learning
  key_people:
  - Shunyu Yao
  - Timo Schick
  - Joon Sung Park
  - Guanzhi Wang
  - Percy Liang
  - Michael S. Bernstein
  - Karthik Narasimhan
  - Luke Zettlemoyer
  - Linxi Jim Fan
  - Anima Anandkumar
key_logic_flow:
- 本文是 KDnuggets '5 Fun 系列'的第二篇，主张从讲解 LLM 的论文进阶到讲解 AI agent 的论文，通过阅读每篇阐明一个核心思想的论文来学习
  agentic AI，而非直接阅读长篇综述。
- ReAct 提出一个提示框架，让语言模型在推理步骤与动作之间交替，推理用于规划、跟踪进度并从错误中恢复，动作用于与搜索引擎、知识库等外部环境交互。
- Toolformer 探索语言模型以自监督方式学习使用外部工具，模型需要学会何时调用、调用哪个工具、传入什么参数以及如何把返回结果融入最终答案，涵盖计算器、搜索引擎、翻译、日历和问答系统。
- Generative Agents 在受《模拟人生》启发的交互环境中模拟可信的人类行为，智能体会制定计划、记忆和反思过往经历、相互交谈并协调未来行动，核心架构结合记忆、反思与规划。
- Voyager 作为一篇开放式具身智能体的论文被列入推荐，文章正文在列出其作者后截断，未展开对该方法的详细描述。
object_mentions:
- object_type: paper
  name: 'ReAct: Synergizing Reasoning and Acting in Language Models'
  canonical_name: ReAct
  url: https://arxiv.org/abs/2210.03629
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - ReAct 提出一个提示框架，让语言模型在推理步骤与动作之间交替，推理帮助模型规划、跟踪进度并从错误中恢复，动作则使其能与外部环境交互。
  - 论文指出许多现代 AI agent 都遵循同样的基本循环：思考、行动、观察、更新，然后继续，因此它是理解 LLM agent 基础的首选论文。
  article_id: cc30dd8dc6a3ac8e
- object_type: paper
  name: 'Toolformer: Language Models Can Teach Themselves to Use Tools'
  canonical_name: Toolformer
  url: https://arxiv.org/abs/2302.04761
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Toolformer 探索语言模型如何以自监督方式学习使用外部 API，模型要学会何时调用工具、调用哪个工具、传入什么参数以及如何利用返回结果。
  - 论文涵盖计算器、搜索引擎、翻译系统、日历和问答系统等工具，推动 LLM 从文本生成器转向能自主判断何时需要外部帮助的系统。
  article_id: cc30dd8dc6a3ac8e
- object_type: paper
  name: 'Generative Agents: Interactive Simulacra of Human Behavior'
  canonical_name: Generative Agents
  url: https://arxiv.org/abs/2304.03442
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 该论文引入生成式智能体，在受《模拟人生》启发的交互环境中模拟可信的人类行为，智能体会醒来、制定计划、记忆并反思过往经历。
  - 其关键架构结合记忆、反思与规划，表明 agent 行为关乎连续性，包括记住什么、如何更新信念以及过往事件如何影响未来决策。
  article_id: cc30dd8dc6a3ac8e
- object_type: paper
  name: 'Voyager: An Open-Ended Embodied Agent with Large Language Models'
  canonical_name: Voyager
  url: https://arxiv.org/abs/2305.16291
  confidence: medium
  article_role: primary_subject
  evidence_snippets:
  - '文章将 Voyager 列为第五篇推荐论文，标题为 Voyager: An Open-Ended Embodied Agent with Large Language
    Models。'
  - Voyager 的作者包括 Guanzhi Wang、Yuqi Xie、Yunfan Jiang、Ajay Mandlekar、Chaowei Xiao、Yuke
    Zhu、Linxi Jim Fan 与 Anima Anandkumar。
  article_id: cc30dd8dc6a3ac8e
extract_result: success
---

I know there's a lot happening in the agentic AI space. You'll hear about agents that use tools, agents with memory, agents that plan, agents that collaborate with other agents, and agents that explore environments on their own. It can get confusing, and if you start with long survey papers, you'll probably end up even more confused. In my opinion, a much better way to learn is to read a few important papers that each explain one key idea behind modern AI agents.

This article is part of our **5 Fun series**. In a previous article, we looked at **5 Fun Papers That Explain LLMs Clearly**. This time, we are moving one step further, from models that generate text to AI agents that can reason, use tools, remember, and collaborate. So, let's get started.


## # 1. ReAct: Synergizing Reasoning and Acting in Language Models


**Authors:** Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao

This is one of the best papers to start with if you want to understand agentic AI. The main idea is that an agent should not only think, and it should not only act — it should do both together. **ReAct** introduces a prompting framework where the model alternates between reasoning steps and actions. The reasoning helps the model plan, track progress, and recover from mistakes, while the actions allow it to interact with external environments such as search APIs, knowledge bases, or decision-making tasks. This paper is important because many modern AI agents follow this same basic loop: think, act, observe, update, and continue. If you want to understand the foundation of large language model (LLM) agents, this is the paper to read first.


## # 2. Toolformer: Language Models Can Teach Themselves to Use Tools


**Authors:** Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, Roberta Raileanu, Maria Lomeli, Luke Zettlemoyer, Nicola Cancedda, Thomas Scialom

Tool use is one of the most important parts of agentic AI. A language model may be good at writing and reasoning, but it can still struggle with arithmetic, factual lookup, translation, or current information. **Toolformer** explores how a language model can learn to use external APIs in a self-supervised way. The model learns when to call a tool, which tool to call, what arguments to pass, and how to use the returned result in its final answer. The paper includes tools such as a calculator, search engine, translation system, calendar, and question-answering system. This paper is important because it moves us from "LLMs as text generators" toward "LLMs as systems that can decide when outside help is useful."


## # 3. Generative Agents: Interactive Simulacra of Human Behavior


**Authors:** Joon Sung Park, Joseph C. O'Brien, Carrie J. Cai, Meredith Ringel Morris, Percy Liang, Michael S. Bernstein

This is one of the most fun agent papers to read because it feels like watching a small AI society come alive. The **paper** introduces generative agents that simulate believable human behavior in an interactive environment inspired by The Sims. These agents wake up, make plans, remember past experiences, reflect on them, talk to other agents, and coordinate future actions. The key architecture combines memory, reflection, and planning. This paper is important because it shows that agentic behavior is not only about solving one task. It is also about continuity: what the agent remembers, how it updates its beliefs, and how past events influence future decisions. If you want to understand why memory and reflection matter in agent design, this paper is a great place to start.


## # 4. Voyager: An Open-Ended Embodied Agent with Large Language Models


**Authors:** Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi Jim Fan, Anima Anandkumar