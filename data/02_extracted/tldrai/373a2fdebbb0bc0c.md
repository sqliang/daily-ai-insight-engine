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
tldr: ProgramBench基准测试：主流AI模型从二进制文件重建完整程序的解决率均为0%。
objective_summary: ProgramBench发布一项评估AI智能体从编译后二进制和文档重建程序能力的基准测试，包含200个任务和24.8万项行为测试。Claude
  Opus 4.7、GPT 5.4、Gemini 3.1 Pro等模型完全解决率均为0%。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - Anthropic
  - OpenAI
  - Google
  technologies:
  - ProgramBench
  key_people: []
key_logic_flow:
- ProgramBench 是一个评估 AI 智能体从编译后二进制文件及其文档重建完整程序能力的基准测试。
- 该基准包含200个任务，覆盖从小型终端工具（jq、ripgrep）到大型项目（PHP编译器、FFmpeg、SQLite）的多种复杂度。
- 测试套件通过智能体驱动的模糊测试生成，共计超过24.8万项行为测试。
- 在多款主流模型使用 mini-SWE-agent 评估中，完全解决率均为 0%，最高部分解决率仅 3.0%（Claude Opus 4.7）。
- ProgramBench 采用沙箱隔离、无网络访问、禁止反编译等严格防作弊措施，且不使用任务特调脚手架。
- 智能体需自行选择编程语言、设计架构、编写全部源代码并生成构建脚本，不获得任何提示或结构指导。
pipeline_stage: fact_extracted
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