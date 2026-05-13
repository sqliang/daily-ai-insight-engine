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
tldr: ProgramBench测试AI代理仅凭编译后二进制文件重建完整程序的能力，当前所有模型完全解决率为0%。
objective_summary: ProgramBench是一个包含200个任务的基准测试，要求AI代理仅根据编译后二进制文件和文档从头重建完整程序，不允许反编译或访问互联网。测试覆盖从jq等小工具到PHP编译器、FFmpeg和SQLite等大型项目。所有9个模型组合的完全解决率均为0%，Claude
  Opus 4.
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - Anthropic
  - OpenAI
  - Google
  technologies:
  - mini-SWE-agent
  key_people: []
key_logic_flow:
- ProgramBench要求AI代理仅凭编译后二进制文件和文档，从零开始设计架构、编写全部源码并生成构建脚本，不允许反编译或访问互联网。
- 基准测试包含200个任务，覆盖从jq、ripgrep等小型终端工具到PHP编译器、FFmpeg和SQLite等大型项目。
- 测试套件通过自动化模糊测试生成，总计超过248,000个行为测试，用于对比候选程序与原始程序的行为一致性。
- 在全部9个模型×agent组合中，完全解决率均为0%；Claude Opus 4.7的接近解决率最高（3.0%），其次为Claude Opus 4.6（2.5%）和Claude
  Sonnet 4.6（1.0%）。
- 项目使用mini-SWE-agent作为统一评估脚手架，避免针对特定任务进行调优，以确保不同模型间的公平对比。
impact_score:
  score: 7.0
  reason: ProgramBench 以严格的实验设计（200个任务、248,000+ 行为测试、无反编译、无互联网接入）证明当前最强 AI 模型在从头重建程序任务上的完全解决率均为
    0%，Claude Opus 4.7 的接近解决率也仅 3.0%。这是一个强有力的现实检验，直接冲击了行业对 AI 编码代理能力的过度自信。该基准很可能成为评估
    LLM 编程能力的标准参考，对 Coding Agent 产品的市场叙事产生显著影响。评分理由：虽然未达到范式转移级别（如 ChatGPT 发布），但对局部竞争格局和行业预期有实质性修正作用。
sentiment: negative
developer_sentiment:
  tone: skeptical
  primary_focus: 所有9个模型组合完全解决率均为0%，对AI自主编程的商业承诺产生严重质疑
hype_assessment:
  level: low
  reason: 该基准测试方法论极其严谨：200个覆盖从小工具到大型项目的任务、自动化模糊测试生成248,000+行为测试、沙箱容器防止作弊、明确禁止反编译和联网。论文坦诚讨论了实验限制、成本（最高达$5k）和mini-SWE-agent选择的理由，结果呈现完全透明，未使用任何'颠覆性''革命性'等PR用语。这是实打实的干货。
information_entropy: high
domain_disruption:
  technical_innovation: 提出了一种全新的AI编程能力评估范式——仅凭编译后二进制文件和文档重建完整程序，要求代理自主选择语言、设计架构、编写全部源码并生成构建脚本。通过大规模模糊测试自动生成行为测试集（248,000+）验证行为一致性，排除了反编译和互联网搜索等捷径，比SWE-bench等现有基准更能反映真实的端到端软件架构能力。
  business_model: 可能显著影响AI编码工具行业的市场叙事和估值逻辑。当前最强模型完全解决率为0%，意味着'AI替代程序员'的商业叙事需要大幅降调。市场可能从追求完全自动化转向更务实的辅助性工具定位，促使投资者和客户重新评估Coding
    Agent类产品的真实ROI和落地边界。
engineering_complexity: production_ready
compound_value:
  score: 7.0
  reason: ProgramBench 的核心价值在于它系统性地验证了当前所有 AI 模型在自主软件架构与实现上的根本性短板——完全解决率 0%。这一结论对
    AI 产业的投资逻辑具有长期纠偏意义：它迫使资本重新校准对 'autonomous coding' 赛道的预期，从 '替代程序员' 转向 '增强程序员'。该基准采用
    248,000+ 行为测试和统一评估脚手架 mini-SWE-agent，具备成为行业标准测试的潜力（类似 SWE-bench 的路径依赖效应），持续影响模型研发资源分配。但需持续验证其能否被学术界和产业界广泛采纳作为权威标杆，目前仍处于早期验证阶段。
value_capture_layer: agent_middleware
moat_impact: creates_new_moat
key_beneficiaries:
- Anthropic
- mini-SWE-agent
competitive_casualty:
- 过度吹捧'自主编程'能力的 AI 初创公司
- 纯模型能力的 Agent 平台（非 Claude 系）
market_opportunities:
- AI辅助逆向工程与程序理解工具存在商业机会，可帮助开发者在无源码场景下重建程序逻辑
- 针对复杂软件架构设计的AI-human协作工具值得探索，当前AI完全无法自主完成整体架构设计，人机协作是更现实的落地路径
- 自动化行为测试与模糊测试服务有落地空间，ProgramBench的测试生成方法论可迁移至软件质量保障与回归测试领域
risk_matrix:
  regulatory: 无
  technological: 该基准测试揭示当前所有AI模型在完整程序重建任务上的完全解决率均为0%，表明AI自主软件工程能力存在根本性局限，过度依赖AI进行复杂软件开发决策存在显著技术风险
  competitive: 各模型表现存在差异（Claude Opus 4.7接近解决率3.0% vs 多数模型0%），在AI编程助手赛道上，架构级编程能力将成为差异化竞争的关键维度，领先模型可能获得开发者信任优势
  ethical: 无
  additional:
  - 该基准测试单次运行成本高达$5,000，可能加剧AI能力评估的资源鸿沟，小型团队难以进行同等水平的对标评估，导致行业透明度不足
confidence:
  impact: high
  compound: medium
  hype: high
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