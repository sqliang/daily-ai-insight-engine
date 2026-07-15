---
title: Claude Science, an AI Workbench for Scientists (4 minute read)
source: https://www.anthropic.com/news/claude-science-ai-workbench?utm_source=tldrai
author: []
published: ''
created: '2026-07-02'
description: TLDR AI 每日头条
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: e2cc0f4a4ecdec76
manifest_dates:
- '2026-07-02'
source_type: news_media
tldr: Anthropic推出Claude Science，面向科学家的AI工作台
objective_summary: Anthropic于2026年7月15日发布Claude Science测试版，这是一个整合了60多种科学工具和连接器的AI工作台应用。它帮助科学家在单一环境中完成文献分析、多步骤研究设计、生成可重现的图文工件，并支持本地或远程HPC/SSH基础设施运行。
event_type: application_landing
epistemic_status: pr_statement
entities:
  companies:
  - Anthropic
  - Modal
  technologies:
  - MCP
  - HPC
  key_people: []
key_logic_flow:
- Anthropic 发布 Claude Science 测试版，这是一款面向科学家的 AI 工作台应用，旨在将分散的科学工具整合到单一研究环境中。
- 该应用内置 60 多种预配置的技能和连接器，覆盖基因组学、单细胞分析、蛋白质组学、结构生物学和化学信息学等领域。
- 用户通过通用协调代理与系统交互，该代理可调用专家代理和用户创建的自定义代理，并配备审核代理自动检查引用和计算错误。
- Claude Science 支持生成丰富的科学工件（3D 蛋白质结构、基因组浏览器轨迹、化学结构图等），每项输出附带完整的可追溯生成记录。
- 该应用可在 macOS/Linux 本地运行，也可通过 SSH 或 HPC 登录节点在远程基础设施上执行，敏感数据无需离开实验室自有系统。
- 计算任务可自动扩展（从单 GPU 到数百 GPU），审核代理在流水线运行中持续检查输出并自我修正错误。
extract_result: success
impact_score:
  score: 7.5
  reason: 评分依据：这是 Anthropic 在科学计算领域迄今为止最大胆的产品发布。Claude Science 不是简单的模型微调或 API 更新，而是一个完整的
    AI 工作台，内置 60+ 科学工具连接器、多智能体协调架构（通用协调代理 + 专家代理 + 审核代理），并直接对接 HPC/SSH 基础设施。这意味着 AI
    辅助科研从'对话式助手'升级为'可执行复杂多步骤流水线的科研操作系统'。对于 AI 行业竞争格局影响明显——它直接挑战了现有科学计算平台（如 Jupyter、Galaxy、DNAnexus）并建立了新的
    AI-for-Science 范式。但尚未达到'范式转移'级别（如 ChatGPT 发布），因为其核心能力仍依赖底层模型进展，且目前仅限 beta 阶段。评分：7.5
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: AI 工作台能否真正替代现有的 Jupyter + HPC 组合工作流，以及本地化部署对敏感数据安全的承诺是否可靠
hype_assessment:
  level: medium
  reason: 判定依据：文章整体提供了相当详细的产品架构描述（协调代理、审核代理、60+ 技能、可追溯工件、HPC/SSH 集成），并非空洞的 PR 话术。但仍存在一定包装成分：'革命性'、'显著加速科学发现'等措辞属于标准产品发布语言；60+
    连接器的实际覆盖质量和深度尚未验证；'审核代理自我修正'的能力边界未明确说明。整体而言，产品概念扎实但有'画饼'成分，需要用户实测验证。
information_entropy: high
domain_disruption:
  technical_innovation: 多智能体架构在科学计算场景的系统级创新：通用协调代理可动态调度专家代理和用户自定义代理，审核代理在流水线执行过程中持续检查输出并自我修正。会话级持久上下文使得大数据集仅需加载一次，避免了传统
    Jupyter 内核重启的重复开销。支持原生渲染 3D 蛋白质结构、基因组浏览器轨迹等科学工件，且每个输出附带完整的代码+环境+对话历史追溯链。
  business_model: Anthropic 从 API 提供商向垂直领域平台提供商迈进。Claude Science 面向 Pro/Max/Team/Enterprise
    用户，意味着 Anthropic 开始收取平台使用费而非单纯的 token 消耗费。同时通过集成 Modal 等第三方计算资源，构建生态闭环：计算层由合作伙伴提供，AI
    层由 Anthropic 把控，科学家被锁定在 Claude 工作台内。这对现有科学计算 SaaS（如 DNAnexus、Benchling、Galaxy）构成直接威胁。
engineering_complexity: prototype
compound_value:
  score: 8.0
  reason: Claude Science 构建在科学家工作流之上的深度集成平台，一旦被实验室采纳将形成极高切换成本。其核心复利效应来自三方面：(1) 审计追踪和可重现性机制创造数据和流程锁定——论文图表、代码、环境全部在平台内生成，形成长期依赖；(2)
    60+ MCP 连接器构成生态护城河，社区贡献的科学技能越多，平台网络效应越强；(3) 支持本地/HPC/SSH 部署、数据不出实验室，这一合规特性对于生物医药和受监管学术机构是刚需壁垒，竞争对手难以短期复制。科学研发全球年投入超
    2 万亿美元，即便仅捕获 1-2% 的 AI 渗透率，市场空间也极其可观。扣分项：当前仍处 beta 阶段，科学家群体的实际采纳率、留存率、以及对手（如 OpenAI
    的类 Codex for Science）的跟进速度尚需验证。
value_capture_layer: end_application
moat_impact: creates_new_moat
key_beneficiaries:
- Anthropic
- Modal
competitive_casualty:
- 传统生物信息学独立工具厂商
- 通用 AI 编码助手
- 缺乏科学专业能力的通用 Agent 平台
market_opportunities:
- 科研机构可通过Claude Science将文献分析、实验设计和论文绘图整合到单一工作流中，显著降低多工具切换带来的效率损耗，适合实验室管理者评估部署方案
- MCP生态开发者可围绕Claude Science的60余个预置技能和自定义代理接口，开发针对基因组学、结构生物学等细分领域的专用插件和专家代理
- 面向生物制药和CRO企业，提供Claude Science与现有HPC/SSH基础设施集成的咨询与部署服务，帮助其在保障数据不出实验室的前提下利用AI加速研发
risk_matrix:
  regulatory: 科研数据可能涉及患者隐私（HIPAA）、人类遗传资源（中国科技部法规）或出口管制基因序列数据，使用云端AI处理此类敏感数据前需进行合规性评估
  technological: 对Anthropic API和Claude模型存在强绑定依赖，若API定价调整、服务中断或模型能力升级方向发生变化，嵌入工作流的科研管线将面临重构风险
  competitive: Google DeepMind（AlphaFold生态）、微软（Azure AI for Science）和OpenAI（Codex/科研应用）可能推出竞品工作台，且学术开源社区（如Jupyter+本地LLM组合）构成低成本替代方案
  ethical: AI生成的科研图表和稿件可能存在幻觉性错误（虚构引用、不可复现数值），若审核代理未能完全拦截，将污染科学记录并加剧可重复性危机；过度依赖AI工作台可能导致研究人员基础技能退化
  additional: []
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: deep_dive
---

AI has the potential to dramatically accelerate the pace of scientific discovery and the development of healthcare interventions. Since launching our efforts in the life sciences last fall, we’ve worked to improve our model capabilities, make connections to the scientific ecosystem via MCPs and skills, and launch partnerships in an effort to realize this potential.

Today, we’re introducing our most significant expansion of these efforts: Claude Science, an AI workbench for scientists. Claude Science is an app that integrates the tools and packages that researchers most commonly use, produces auditable artifacts, and provides flexible access to computing resources.

## Introducing Claude Science

Scientific research is often tedious. Researchers must work across dozens of databases, each with their own schema, contend with file formats that require bespoke data pipelines and viewers, and transition between a roster of tools: PubMed, Jupyter, R, a cluster terminal, and more.

Claude Science brings these fragmented tools into a single research environment where scientists can conduct all stages of their work. It helps you analyze literature and execute multi-step research, produces detailed artifacts, and lets you iteratively refine figures and manuscripts until they’re ready for publication. Every output carries an auditable history of how it was made, so you can validate and reproduce the results. Like a Jupyter Notebook, you can access Claude Science wherever you already work—locally on macOS or Linux, or on a remote machine over SSH or with an HPC login node.

Users interact with a generalist coordinating agent with access to over 60 curated skills and connectors pre-configured for genomics, single-cell, proteomics, structural biology, cheminformatics, and more. These agents can spin up others and engage with specialist agents created by users. And a reviewer agent checks citations and calculations, flagging and correcting errors.

We are releasing Claude Science today in beta for Claude Pro, Max, Team, and Enterprise users, and will continue to refine the platform as we collect feedback from users.

**How it works**

**Rich scientific artifacts, fully reproducible. **Scientific research is inherently visual, so Claude Science generates figures and manuscripts alongside the code that created them. It natively renders rich scientific artifacts, including 3D protein structures, genome browser tracks, chemical structures, and more. You can chat with the agent about any detail, annotating figures and manuscripts in-line so the agent knows what to address to make them publication-ready.

When it generates a figure, Claude Science includes the exact code and environment that produced it, a plain-language description of how it was created, and the full message history. This allows you to understand the inputs, making the work easier to validate and reproduce even months later. You can ask Claude Science to make edits to figures in plain language—removing gridlines, for example, or changing an axis to log scale—and the agent will edit its own code.

**Manages your compute and scales on demand. **Large analyses—folding a protein, for example, or running a genomics pipeline over a massive dataset—often require researchers to shift their focus to setting up a computing job, waiting while it’s sent to a cluster, checking whether it succeeded or failed, and pulling the results back. Claude Science handles this process for you. It drafts a plan, asks before reaching new resources, and lets you review or revoke any decision before writing and submitting the job to the computing resources your lab already uses (your own HPC cluster over SSH, or your Modal account for compute on demand), scaling the analysis from a single GPU to hundreds as needed.

Because its agents work inside a running session that holds context in memory, even massive datasets only need to be loaded once. It runs on your lab’s own infrastructure—your laptop, Linux box, or HPC login node—so large or sensitive datasets never have to leave the systems they’re already on, and only the context needed for each step of the analysis is sent to Claude. As the pipeline runs, a reviewer agent inspects the outputs, flagging incorrect citations, untraceable numbers, and figures that don’t match their underlying code, and self-correcting as it goes. You can fork the session at any point to compare two approaches without losing the original thread.