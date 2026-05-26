---
title: ProgramBench (5 minute read)
source: https://programbench.com/?utm_source=tldrai
author: []
published: ''
created: '2026-05-08'
description: AI 工程与研究
tags:
- clippings
id: 373a2fdebbb0bc0c
source_type: news_media
tldr: ProgramBench 基准测试发布：所有顶级模型在仅凭二进制和文档重写完整程序的任务中，完全解决率均为 0%
objective_summary: 2026年5月，ProgramBench 发布了一项包含 200 个程序重构任务的基准测试，要求 AI 智能体仅凭可执行二进制和文档重写完整代码库。测试覆盖从
  jq、ripgrep 到 SQLite、FFmpeg 的复杂项目，包含超 24.8 万行为测试。所有主流模型（Claude Opus 4.
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - Anthropic
  - OpenAI
  - Google
  technologies:
  - mini-SWE-agent
  - ProgramBench
  - agent-driven fuzzing
  key_people: []
key_logic_flow:
- ProgramBench 包含 200 个程序重构任务，覆盖从小型命令行工具（jq、ripgrep）到大型软件项目（PHP 编译器、FFmpeg、SQLite）的复杂度跨度
- 智能体仅获得可执行二进制文件和文档，无法访问源码、不可反编译、不可联网，必须在沙箱容器中独立完成架构设计、语言选择、代码编写和构建脚本
- 测试套件通过智能体驱动的模糊测试生成，总计超过 248,000 个行为测试用例
- 所有 9 个受测模型在完全解决率（Resolved）上均为 0%，最高几乎解决率（Almost Resolved）仅为 Claude Opus 4.7 的 3.0%
- 基准使用 mini-SWE-agent 作为统一脚手架，避免针对特定任务调优工具链，确保模型能力的公平对比
- 智能体在多项任务上取得了部分进展，但完全通过所有行为测试仍超出当前所有模型的能力边界
pipeline_stage: fact_extracted
impact_score:
  score: 6.0
  reason: ProgramBench 以严谨的实验设计（200 个任务、24.8 万行为测试、沙箱隔离、统一脚手架）揭示了所有顶级模型在从零构建软件这一核心能力上的共同短板——完全解决率均为
    0%。该基准填补了 SWE-bench 等现有基准未覆盖的'无源码参考下自主架构设计'能力评估空白，将影响 AI 编程工具的能力评估框架和行业叙事。但因属于基准测试发布而非产品发布或技术突破，短期行业冲击力上限受限，评分落于
    6 分区间。
sentiment: mixed
developer_sentiment:
  tone: skeptical
  primary_focus: 仅凭二进制和文档重写完整程序是否衡量了有实际意义的软件工程能力——真实开发中几乎不存在此类清洁室场景
hype_assessment:
  level: low
  reason: 文章坦诚披露所有模型完全解决率为 0%，未使用'颠覆''革命性'等 PR 滥用词汇，方法论透明（沙箱容器隔离、禁止反编译和联网、统一 mini-SWE-agent
    脚手架消除工具链调优偏差），数据详实且有完整论文支撑，属于实打实的学术基准发布。
information_entropy: high
domain_disruption:
  technical_innovation: 引入智能体驱动模糊测试（agent-driven fuzzing）自动生成超 24.8 万个行为测试用例；以统一通用脚手架（mini-SWE-agent）替代针对特定任务调优的工具链，消除因脚手架差异导致的模型能力评估偏差；清洁室约束（无源码、无反编译、无网络）构建了严格的'从零架构设计'能力测试范式。
  business_model: 无直接商业模式冲击。但该基准暴露了当前 AI 编程工具在缺乏源码参考时的自主架构设计与完整实现能力短板，可能促使 AI 编程助手厂商（GitHub
    Copilot、Cursor、Claude Code 等）在产品能力边界宣称上趋于审慎，并推动企业采购评估中纳入'从零构建'维度。
engineering_complexity: production_ready
compound_value:
  score: 6.5
  reason: ProgramBench 的「全模型 0% 完全解决率」是一个里程碑式的行业信号，其长期复利价值不在于基准本身，而在于它揭示的核心事实：当前 AI
    距离真正的自主软件工程仍有巨大鸿沟。这一发现将在未来 12-24 个月内持续影响资本流向——从「AI 替代开发者」的叙事转向「AI 增强开发者」，从根本上重塑
    AI 编程工具赛道的投资逻辑。基准使用 mini-SWE-agent 作为统一脚手架且设计上防作弊（无网络、无反编译），使其结果难以被模型厂商的营销话术稀释，具备较高的引用耐久性。但基准终将被超越或替代，其直接复利效应有限。
value_capture_layer: foundation_model
moat_impact: democratizes_access
key_beneficiaries:
- Anthropic
- mini-SWE-agent
- Cursor
- GitHub Copilot
competitive_casualty:
- Cognition AI (Devin)
- OpenAI
- 自主 AI 编程 Agent 初创公司
market_opportunities:
- 基于 ProgramBench 暴露的 AI 架构推理短板，可开发专注于辅助智能体进行高层软件架构设计的中间件层，将复杂程序自动拆解为可被当前模型独立完成的模块粒度，填补'从零构建完整程序'的能力缺口
- 该基准的智能体驱动模糊测试方法论（24.8 万行为测试用例）可产品化为遗留系统迁移的自动化行为等价性验证平台，面向金融、政务、电信等核心系统现代化改造的高容错需求市场
- 个人开发者可将'AI 编码时代的任务分解与架构决策能力'作为核心差异化技能进行刻意训练——在模型擅长实现细节但缺乏全局架构能力的现阶段，具备拆解复杂需求并分派给
  AI 执行的能力将成为高价值的稀缺技能
risk_matrix:
  regulatory: 无
  technological: 所有主流模型在 ProgramBench 上的完全解决率均为 0%，揭示当前基于 next-token prediction 的
    LLM 范式在需要长期规划与深度架构推理的复杂程序合成任务上存在根本性瓶颈，对重仓 AI 全自动代码生成的企业构成技术路线风险
  competitive: Anthropic Claude Opus 4.7 以 3.0% 几乎解决率领先，但绝对分差极小（与第二名仅差 0.5 个百分点），竞争格局远未固化；需警惕各厂商后续针对该基准进行专项调优（harness
    tuning）导致基准公信力稀释，重演 SWE-bench 的'分数通胀'问题
  ethical: 智能体在仅获得二进制和文档的前提下重写完整程序，在方法论层面触及软件逆向工程的灰色地带——虽当前设置禁止反编译和联网，但该能力的逐步提升可能引发关于软件版权、专利保护和商业机密的技术伦理争议
  additional:
  - 基准分数的选择性引用风险：0% 完全解决率与 3% 几乎解决率之间的巨大落差，可能被利益相关方断章取义用于夸大危机或贬低竞品，分析师需关注伴随该基准的舆论叙事操纵
  - 沙箱化干净室实现的商业化歧路：若该能力持续提升，可能出现以'行为等价重实现'为名义绕过软件许可证限制的灰色商业实践，对开源生态构成间接威胁
confidence:
  impact: medium
  compound: low
  hype: medium
actionable_insight: deep_dive
---

# ./ProgramBench

Can language models rebuild programs from scratch?

Given only a compiled binary and its documentation, agents must architect and implement a complete codebase that reproduces the original program's behavior.

| # | Model | Agent | Resolved The number of fully solved instances as measured by the hidden behavioral tests. Note that behavioral tests can never cover all possible inputs. The behavioral tests of ProgramBench can be easily extended should any false positives arise. | Almost resolvedAlmost Instances where the agent's solution solves ≥ 95% of all behavioral tests. See extended results. | |
|---|---|---|---|---|---|
| 1 | Claude Opus 4.7 Anthropic | mini-SWE-agent | 0% | 3.0% | |
| 2 | Claude Opus 4.6 Anthropic | mini-SWE-agent | 0% | 2.5% | |
| 3 | Claude Sonnet 4.6 Anthropic | mini-SWE-agent | 0% | 1.0% | |
| 4 | GPT 5.4 OpenAI | mini-SWE-agent | 0% | 0.0% | |
| 5 | Gemini 3.1 Pro Google | mini-SWE-agent | 0% | 0.0% | |
| 6 | Gemini 3 Flash Google | mini-SWE-agent | 0% | 0.0% | |
| 7 | Claude Haiku 4.5 Anthropic | mini-SWE-agent | 0% | 0.0% | |
| 8 | GPT 5.4 mini OpenAI | mini-SWE-agent | 0% | 0.0% | |
| 9 | GPT 5 mini OpenAI | mini-SWE-agent | 0% | 0.0% |

## About ProgramBench

In each task, the agent receives an executable and its documentation, and it must re-implement the given executable. It does not get access to *any* of the executable's source code, it cannot de-compile the executable, and cannot use the internet. There are 200 tasks in total covering different program complexities, ranging from small terminal utilities like jq and ripgrep to massive software projects like the PHP compiler, FFmpeg, and SQLite.

The agent must choose a language, design the architecture, write all source code, and produce a build script. Every design decision is the model's to make.

Once the agent submits a program, our test suite compares the candidate program's behavior against the original program. A candidate program passes only if all tests for that task pass.

Our test suite is generated via agent-driven fuzzing, and it comprises more than 248,000 total behavioral tests for our 200 tasks.

## Can tasks in ProgramBench be fully solved at all?

Yes. The agent can run the given program with any input and observe exactly what it does, so there's nothing hidden that can't be discovered through experimentation. The benchmark is hard, but it's solvable by design: all the reference executables pass our test suites. Read more in our blog post.

## Why are ProgramBench scores so low?

Building a program from scratch is a fundamentally challenging task. Agents do currently make partial progress on many tasks (see the extended results for details), but fully passing every test is still out of reach.

**Agents truly have to architect.** This is in part because unlike other whole-repo generation projects, we give no hints or structure to the agent, meaning that the agent truly has to architect its own solutions (see "How is ProgramBench different?").

**No harness tuning.** Other recent and concurrent work also performed substantial harness tuning for a single or a handful number of tasks. We deliberately avoid this, since headline scores from a tuned harness on a curated handful of tasks can substantially overstate how capable agents really are at building software from scratch. Instead, ProgramBench is evaluated with a single generic harness across the entire task set.

**Cleanroom implementation.** We take substantial precautions to prevent cheating. Agents run in sandboxed containers without internet access, so they cannot retrieve the original source code or obtain any other form of help.

**No decompilation.** See "Can tasks be solved with decompilation?"

We review related work in section 6 of the paper. We also discuss cheating in the FAQ below and in section 4.1.

## Is your agent scaffold sufficient to solve all tasks?

**Widely adopted baseline.** We use mini-SWE-agent because it is both widely adopted as a baseline by other benchmarks (SWE-bench Verified, SWE-bench Multilingual, Terminal-bench) and deliberately minimal in its scaffolding, reducing confounds between model capability and harness design. Most other agents (like Claude Code with apparently several 100k lines of code) are also constantly changing in non-transparent ways, while mini-SWE-agent will allow for apples-to-apples performance comparison of models for the foreseeable future.

**Almost no runtime limitations.** With very few exceptions, models submit their solutions deliberately rather than exceeding our generous time or step limits, and they never exhaust their context window. Because we do not limit total cost, our runs have cost up to $5k (for Sonnet 4.5).