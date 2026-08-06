---
title: Pi's Minimalism Is Its Advantage
source: https://earendil.com/posts/pi-autoresearch-and-databricks/
author:
- '[[luispa]]'
published: '2026-08-04'
created: '2026-08-05'
manifest_dates:
- '2026-08-05'
description: 'Article URL: https://earendil.com/posts/pi-autoresearch-and-databricks/
  Comments URL: https://news.ycombinator.com/item?id=49176038 Points: 350 # Comments:
  137'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: ffbe90d5ea594eb1
source_type: community_discussion
tldr: Earendil 发布的极简编码框架 Pi 默认仅含 4 个工具、提示词不足 1000 token。Databricks 测评显示其搭配 Opus 4.8
  通过率最高且成本更低，Shopify 也基于它构建了 pi-autoresearch 扩展并大幅提速。
objective_summary: Earendil 撰文介绍其极简编码框架 Pi，称其默认仅含 4 个工具，系统提示词与工具定义合计低于 1000 token。Databricks
  在百万行代码库上自建基准测评编码智能体，发现同一模型经不同框架调用时单任务成本差异可超 2 倍，Pi 搭配 Opus 4.8 与 xhigh 思考强度取得最高通过率，成本低于
  Claude Code 与 Codex。Shopify 工程师 David Cortés 以 Pi 扩展方式构建了 pi-autoresearch 自主优化循环，报告称单元测试提速约
  300 倍、React 组件挂载提速约 20%。作者认为 Pi 的上下文纪律与可扩展性使其在本地模型场景下同样具有优势。
event_type: framework_tools
epistemic_status: pr_statement
entities:
  companies:
  - Earendil
  - Databricks
  - Shopify
  - Anthropic
  technologies:
  - Pi
  - pi-autoresearch
  - Claude Code
  - Codex
  - Opus 4.8
  - Haiku 4.5
  - Sonnet 4.6
  key_people:
  - David Cortés
key_logic_flow:
- Earendil 认为 AI 降低编码成本后许多公司趋向复杂化，而 Pi 反其道而行，默认仅提供 4 个工具，系统提示词与工具定义合计低于 1000 个 token。
- Databricks 在百万行代码库上自建基准测评编码智能体，发现简单框架 Pi 在多数工作负载上表现最佳，并指出模型经不同框架调用时单任务成本差异可超过 2
  倍而质量保持不变。
- Pi 搭配 Opus 4.8 与 xhigh 思考强度时整体通过率最高，成本显著低于 Claude Code 与 Codex，作者将这一优势归因于 Pi 每轮发送上下文约少
  3 倍的上下文纪律。
- Shopify 工程师 David Cortés 以 Pi 扩展方式构建了 pi-autoresearch，该自主循环通过实验寻找有效改动并排除引发回归的变更，报告称单元测试提速约
  300 倍。
- Anthropic 将 Claude Code 系统提示词缩减 80%，表明原生框架的结构优势正在减弱，框架如何管理上下文以避免冗余成为更关键的变量。
- Pi 的上下文纪律与极简默认配置使其尤其适合上下文窗口较小、prefill 耗时的本地模型场景，能避免长时间重复预填充。
object_mentions:
- object_type: product
  name: Pi
  canonical_name: Pi
  url: https://earendil.com
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Pi 是 Earendil 推出的极简编码框架，开箱默认仅提供 4 个工具，系统提示词与工具定义合计不足 1000 个 token。
  - Databricks 的测评显示，Pi 搭配 Opus 4.8 与 xhigh 思考强度时整体通过率最高，且成本显著低于 Claude Code 和 Codex。
  - Pi 的核心哲学是极简但可扩展，作者称其为首个为可扩展性与自我编辑而设计的广泛使用的智能体基础设施。
  article_id: ffbe90d5ea594eb1
- object_type: project
  name: pi-autoresearch
  canonical_name: pi-autoresearch
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Shopify 工程师 David Cortés 直接以 Pi 扩展形式构建 pi-autoresearch，只需向 Pi 提出创建扩展的请求即可启动开发流程。
  - Autoresearch 是一个面向编码智能体的自主优化循环，通过运行实验确定有效改动并识别引发回归的变更。
  - Shopify 报告相关成果包括单元测试运行提速约 300 倍、React 组件挂载提速约 20%，以及构建时间和 pnpm 性能的改善。
  article_id: ffbe90d5ea594eb1
- object_type: product
  name: Claude Code
  canonical_name: Claude Code
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Anthropic 近期将 Claude Code 的系统提示词削减了 80%，这被视为前沿模型已能胜任终端式编码环境的明确信号。
  - 在 Databricks 的测评中，Claude Code 与 Pi 搭配 Opus 4.8 相比，在同等质量下表现出更高的单任务成本。
  article_id: ffbe90d5ea594eb1
- object_type: product
  name: Codex
  canonical_name: Codex
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 在 Databricks 的测评中，Pi 搭配 Opus 4.8 时在成本显著更低的前提下达到最高通过率，表现优于 Claude Code 与 Codex。
  article_id: ffbe90d5ea594eb1
- object_type: model
  name: Opus 4.8
  canonical_name: Opus 4.8
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Databricks 的研究将模型与框架分离，发现 Pi 搭配 Opus 4.8 与 xhigh 思考强度时在自建工作负载上通过率最高。
  article_id: ffbe90d5ea594eb1
- object_type: paper
  name: Benchmarking Coding Agents on Databricks' Multi-Million Line Codebase
  canonical_name: Benchmarking Coding Agents on Databricks' Multi-Million Line Codebase
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Databricks 发布了名为 Benchmarking Coding Agents on Databricks' Multi-Million Line
    Codebase 的测评研究，基于工程师日常任务自建基准以避免外部基准的过拟合。
  - 研究指出同一模型经不同框架调用时单任务成本差异可超过 2 倍而质量保持不变，Pi 每轮发送的上下文约为其他框架的三分之一。
  article_id: ffbe90d5ea594eb1
extract_result: success
---

# Pi, Minimal and Performant

# Pi’s Minimalism Is Its Advantage

AI has made code cheap, and as a result many companies are building bigger tools in pursuit of better performance. Larger prompts, more orchestration, more layers, more complexity. This also makes these tools intrinsically more expensive to use. Pi takes the opposite approach.

Pi is the coding harness that chooses minimalism on purpose. It comes out of the box with only 4 tools, and its system prompt and tool definitions come in below 1,000 tokens. The idea being that most work can be done with the basics, and if you want more, build it.

Evidence increasingly suggests that Pi’s design is not just cleaner; it’s cheaper and more performant. Users are finding that vanilla Pi produces industry leading results, even before adding on extensions to match user specific workflows and needs. As we'll see in case studies of Databricks and Shopify, Pi produced ideal outcomes for both.

## Case Studies

**Databricks Study: Cost Per Task**

Databricks recently shared their findings “*Benchmarking Coding Agents on Databricks’ Multi-Million Line Codebase*.” The goal of their research was to understand which coding agents offer the best performance on real-world coding tasks, and how task-performance varies with price.

To avoid bias from external benchmarks that have become oversaturated, they created their own based on tasks their team of engineers regularly performs. The results match what we would expect, but what many in the industry may have been surprised to learn. In their words, “...the harness a model is called from dramatically impacts cost and quality,” and, “in many cases, simple harnesses like Pi performed best on our workloads.”

When combined with Opus 4.8, xhigh, Pi had the highest overall pass-rate, at a significantly lower cost than both Claude Code and Codex.

#### Minimal harness, measurable effect

Pi shines because it doesn’t try to wrap the model in a bunch of defaults and instructions that get lost in the instruction hierarchy. Instead, Pi stays out of the model’s way, and the team is able to add what they actually need for their workflow.

Databricks’ study is insightful because it separates model from harness.

They reported that when they ran the same model with the same thinking effort through different harnesses, “the cost per task differed significantly (more than 2x in some cases), while quality remained the same”. We call this Pi’s “context discipline”. “Pi sent about 3x less context per turn. It managed context better, keeping a tighter working set and finishing the tasks in fewer runs.”

We agree that one must take into account end-to-end engineering economics, and not just price per token. And this is also true at the model level; we have observed, for instance, that running complex workflows on Haiku 4.5 was often more expensive than Sonnet 4.6, especially when code execution was involved, simply because the agent required more turns to complete the task successfully.

Now we see this at the harness level too; stronger, more expensive models with a performant harness can be cheaper than the converse.

**Shopify builds Pi Autoresearch: Extensible beats bloat**

Minimalism is part of Pi’s core philosophy. What makes this work is that minimal does not mean inflexible. In fact, it is the first widely used agentic infrastructure created for extensibility and self-editability.

Another insightful external validation of Pi’s design comes from Shopify. In this post from Shopify Engineering, David Cortés describes building `pi-autoresearch`

directly as a Pi extension, by simply asking “Pi, [to] create an extension for Autoresearch...”. Pi reads its own extension documentation and starts building a new workflow from there.

Autoresearch is an autonomous loop for optimization with coding agents. When you ask for a change, it runs experiments to find out what works and what causes regressions. For as long as the target is measurable, it can throw out these regressions and keep self-improving.

For Shopify and others, the Autoresearch extension quickly became a serious internal productivity tool. Shopify reported cases including unit tests running “300 times faster,” React component mounting “20% faster,” reduced build times across multiple projects, and even improvements to pnpm performance.

The important point here is that Pi doesn’t ship any of these tools out of the box. Instead, it makes it ridiculously simple for you to build them. Instead of assuming the vendor knows your workflow and trying to ship every tool under the sun, Pi assumes you know best, and gifts you extensibility to wield and craft your own workflow.

## Why minimal wins now

About a year ago, an argument could be made for native harnesses having a structural advantage over all others, because models were built around them. However, this argument has gotten weaker.

Frontier models are now generally very competent at understanding a terminal (or terminal-style) coding environment, and acting within it. Anthropic recently cutting down Claude Code’s system prompt by 80% is a clear sign of this. So the question is becoming less about how native the harness is, and more about how it handles context to avoid redundancy and act with clean primitives. Models need a clean interface to the environment, and a harness that does not waste context.

Pi provides this: less prompt overhead and repeated context, cheaper runs, fewer unnecessary abstractions. Because it is extensible, you do not lose power, but gain selectivity. You add complexity only when it “earns its keep”.

We are also seeing local models developing fast, and at Earendil we find them very promising. Pi’s context discipline is especially an asset here. Local models usually have lower context windows, and prefill can take a long time, so preserving a stable prompt prefix matters. Context discipline means we do not change the context without the user explicitly asking for it, avoiding minute-long re-prefilling. Combined with the minimal default system prompt and tool set, this makes pi an ideal harness for local models.

Pi is proving that it can manage it all. To be cheaper, minimal, and more performant.