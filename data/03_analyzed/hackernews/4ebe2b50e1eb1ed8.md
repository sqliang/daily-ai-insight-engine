---
title: 'Show HN: Ante, a coding agent in a single binary that runs offline'
source: https://github.com/AntigmaLabs/ante
author:
- '[[ubermon]]'
published: '2026-08-10'
created: '2026-08-11'
manifest_dates:
- '2026-08-11'
description: 'Article URL: https://github.com/AntigmaLabs/ante Comments URL: https://news.ycombinator.com/item?id=49245437
  Points: 131 # Comments: 79'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 4ebe2b50e1eb1ed8
source_type: community_discussion
tldr: Antigma Labs 发布 Ante，一款约 15MB 的单二进制离线编码智能体，用 Rust 手写、内置 llama.cpp 本地推理，在 Terminal-Bench
  2.1 上取得 82.7% 分数，并开源文档、协议与 SDK。
objective_summary: 2026 年，Antigma Labs 在 Hacker News 通过 Show HN 发布编码智能体 Ante。它是一个用
  Rust 手写的约 15MB 单二进制程序，核心 harness 以预编译二进制形式发布，仓库内开源了文档、协议、SDK 与评测管线。Ante 在 Terminal-Bench
  2.1 上搭配 DeepSeek V4 Flash 0731 取得 82.7% 准确率，并宣称在 Docker 并行任务下比 Claude Code 节省约 7
  倍峰值内存与 9 倍平均 CPU。
event_type: framework_tools
epistemic_status: pr_statement
entities:
  companies:
  - Antigma Labs
  - DeepSeek
  - Anthropic
  - OpenAI
  - Google
  - xAI
  - Open Router
  technologies:
  - Rust
  - llama.cpp
  - GGUF
  - MCP
  - Terminal-Bench
  - TUI
  - JSONL
  key_people: []
key_logic_flow:
- Ante 是 Antigma Labs 开发的单二进制编码智能体，约 15MB 的 Rust 程序，零运行时依赖，可在终端内自组织运行。
- 核心 harness 在 alpha 阶段以预编译二进制发布，仓库开源了 docs-site 文档、protocol-shape 协议、agent-sdk SDK、ante-harbor
  评测管线与 exec 库。
- Ante 在 Terminal-Bench 2.1 上以 DeepSeek V4 Flash 0731 取得 82.7% 准确率，共 368/445 trials，推理成本约
  68 美元。
- Ante 内置固定版本的 llama.cpp 推理引擎，可直接加载本地 GGUF 模型完全离线运行，无需 API key 与网络连接。
- 相比 Claude Code，Ante 在 Docker 中 20 个并行任务下使用约 7 倍更少的峰值内存、9 倍更少的平均 CPU 与 5 倍更少的磁盘 I/O。
- Ante 支持交互式 TUI、headless、serve 服务器与 gateway 网关四种模式，兼容 12 家以上模型提供商并支持 MCP 与多智能体编排。
object_mentions:
- object_type: product
  name: Ante
  canonical_name: Ante
  url: https://github.com/AntigmaLabs/ante
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Ante 是 Antigma Labs 开发的单二进制编码智能体，约 15MB 的 Rust 程序，零运行时依赖，可在终端内自组织运行。
  - Ante 在 Terminal-Bench 2.1 上搭配 DeepSeek V4 Flash 0731 取得 82.7% 准确率，并支持本地 GGUF 模型完全离线推理。
  article_id: 4ebe2b50e1eb1ed8
- object_type: project
  name: ante-harbor
  canonical_name: ante-harbor
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - ante-harbor 是 Ante 的 Harbor 智能体适配器，负责产出 Terminal-Bench 结果，可用于复现 antigma.ai/eval
    上的任何评测运行。
  article_id: 4ebe2b50e1eb1ed8
- object_type: project
  name: crates/agent-sdk
  canonical_name: Ante agent-sdk
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - crates/agent-sdk 是 Antigma Labs 开源的 Rust SDK 与客户端，用于基于 agent 运行时构建应用，遵循 Apache
    2.0 许可。
  article_id: 4ebe2b50e1eb1ed8
- object_type: project
  name: crates/protocol-shape
  canonical_name: Ante protocol-shape
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - crates/protocol-shape 定义了 ante serve 模式所遵循的 schema 与线缆消息协议，是 Ante 核心协议的开源实现。
  article_id: 4ebe2b50e1eb1ed8
- object_type: project
  name: nanochat-rs
  canonical_name: nanochat-rs
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - nanochat-rs 是 Ante 团队开源的教学版玩具引擎，用于研究内置 llama.cpp 本地推理引擎的工作原理。
  article_id: 4ebe2b50e1eb1ed8
- object_type: project
  name: crates/exec
  canonical_name: Ante exec crate
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - crates/exec 是 Ante 核心库中第一个被渐进开源到仓库的独立进程执行库，作为稳定化的核心组件随 alpha 发布。
  article_id: 4ebe2b50e1eb1ed8
extract_result: success
impact_score:
  score: 6.0
  reason: 评分依据：其一，Terminal-Bench 2.1 的 82.7% 成绩若经 Harbor 管线可审计属实，意味着本地/离线编码智能体首次在公开基准上与云端主流产品（Claude
    Code/Codex 生态）站上同一水平线，对开发者工具局部竞争格局构成实质冲击；其二，单二进制 + 零依赖 + 内置 llama.cpp 的架构在资源效率上确有真实差异化，且与'开源协议与
    SDK、二进制交付核心'的折中模式形成话题性；其三，扣分因素包括核心 harness 闭源、成绩为厂商自报、公司无知名度、产品仅 alpha 预览且明确预期
    breaking changes，距离范式转移（如 ChatGPT 级）尚有量级差距，短期影响主要限定在编码智能体工具赛道内部。综合评定为 6.0 分。
sentiment: mixed
developer_sentiment:
  tone: skeptical
  primary_focus: 核心 harness 仅以预编译二进制分发、闭源模式与默认开启的遥测，以及自报基准成绩（82.7%、7×/9× 资源节省）未经第三方复现的可信度
hype_assessment:
  level: medium
  reason: 判定依据：文中的 'A ghost in your shell'、'substrate for self-organizing intelligence'、'light
    enough to run by the thousands' 等表述带有明显的营销包装成分；7× 峰值内存、9× CPU、5× 磁盘 I/O 的对比为厂商自报、缺乏独立第三方复现；但另一方面
    82.7% 成绩绑定了精确 build 版本并开放 Harbor 评测管线供独立审计，协议/SDK/文档以 Apache 2.0 真实开源，存在可验证的实证支撑，并非空口概念炒作，故定性为中等水分。
information_entropy: high
domain_disruption:
  technical_innovation: 将 grep/git 等重工具与固定版本 llama.cpp 推理引擎全部内嵌进单一 Rust 进程，实现零运行时依赖的约
    15MB 编码智能体；本地 GGUF 离线推理 + 多提供商 BYO 切换的架构设计，在资源受限、容器化与大规模并行场景下具备真实工程优势，是编码智能体向轻量化/可验证方向的一次实质性探索。
  business_model: 提出'开源协议/SDK/文档、以预编译二进制交付核心 harness'的 agent 时代开源折中方案，并采用'自带密钥、零账号锁定、可自由切换
    12+ 提供商'的 BYO 商业模式，直接冲击 Claude Code/Codex 的订阅制与闭源生态，推动编码智能体从厂商锁定服务向可自托管基础设施演进。
engineering_complexity: prototype
compound_value:
  score: 6.0
  reason: 投资逻辑推演：(1) 差异化定位成立——'单二进制 + 内嵌 llama.cpp + 零运行时依赖'本质上是编码智能体的'SQLite 化'叙事，离线可验、低资源、可大规模并发的特性使其具备嵌入
    CI/CD、容器与私有化环境的复利场景，若被企业/开发者采纳为默认轻量 agent runtime，会形成持续沉淀的数据与评测飞轮。(2) 开源 protocol-shape
    协议、agent-sdk 与 ante-harbor 评测管线（Apache 2.0）是正确的基础设施打法——协议一旦被社区采纳即为事实标准，具备长期复利；但正面撞上
    MCP 已占据的智能体互操作标准生态，协议采纳率是最大不确定性。(3) 风险项：核心 harness 在 alpha 阶段仍以预编译二进制闭源发布，团队自身承认'agentic
    时代如何做开源'尚未想清，商业模式未验证；82.7% 的 Terminal-Bench 成绩依赖外购的 DeepSeek V4 Flash 模型，模型层能力不构成自有壁垒，自身在数据飞轮上的积累尚待观察。(4)
    赛道极其拥挤，Claude Code、Codex 与开源框架均在前沿模型绑定上占优，Ante 必须靠'轻量/离线/免锁定'的差异化切走边缘长尾。综合判定：有潜力成为细分（本地/离线/嵌入式编码智能体）基础设施，但需持续验证协议采纳与商业化，故落在
    6.0。
value_capture_layer: agent_middleware
moat_impact: democratizes_access
key_beneficiaries:
- Antigma Labs
- DeepSeek
- llama.cpp / ggml-org
- Qwen (Alibaba)
- OpenRouter
competitive_casualty:
- Anthropic (Claude Code)
- OpenAI (Codex)
- 云依赖型编码智能体平台
market_opportunities:
- 企业级离线编码智能体存在真实需求——单二进制、零运行时依赖、可离线运行的 Agent 适合金融、政务、军工等数据敏感与隔离网络环境，建议关注该细分赛道的产品化与私有化部署机会
- Ante 以 Apache 2.0 开源了 protocol-shape 协议与 agent-sdk，开发者可基于这些协议层构建自定义编码助手或垂直领域 Agent
  harness，降低自研 Agent 底座的成本
- 本地 GGUF 模型（如 Qwen3.5-9B）+ 轻量级 Agent 的组合大幅降低推理成本并规避 API 依赖，提示了'低成本本地化编码助手'产品与个人技能深化方向，值得早期跟进研究
risk_matrix:
  regulatory: 核心 harness 以预编译二进制闭源发布、遥测默认开启（opt-out），在 GDPR、数据出境与供应链合规场景可能面临审查；'agentic
    时代的开源'边界模糊，协议与许可证界定不清，存在知识产权与合规争议风险
  technological: 项目处于 alpha 阶段，明确预告破坏性变更且功能不完整；82.7% 为厂商自报成绩（pr_statement），依赖 DeepSeek
    V4 Flash 特定模型与固定版本 llama.cpp，可复现性存疑；核心闭源若项目弃坑将导致技术不可持续
  competitive: 直接对标 Claude Code、Codex 等背靠 Anthropic/OpenAI/Google 资源的产品，同时面临 Aider、OpenHands、Cline
    等成熟开源 Agent 的生态挤压；'开源但不含核心 harness'的折中策略可能引发 OSS 社区信任反噬
  ethical: 遥测机制（即便匿名、可关闭）与 'curl | bash' 分发模式引发隐私与供应链安全顾虑；宣称'可运行数千实例的自组织智能'规模化后可能加速编码岗位替代；自组织
    Agent 权限控制不当存在被提示注入或恶意利用的风险
  additional:
  - curl -fsSL ... | bash 的安装方式存在供应链投毒与中间人攻击风险
  - 单一闭源二进制缺乏第三方代码审计，安全性与可验证性不足，企业采纳前需沙箱隔离验证
confidence:
  impact: medium
  compound: low
  hype: high
actionable_insight: monitor
object_insights:
- object_type: product
  name: Ante
  canonical_name: Ante
  url: https://github.com/AntigmaLabs/ante
  positioning: Ante 是 Antigma Labs 推出的单二进制编码智能体，约 15MB 的 Rust 程序，内置 llama.cpp 本地推理，可在终端内自组织运行并兼容多模型提供商。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 需要离线或低资源环境运行编码智能体的开发者
  - 在容器或远程机器上部署编码代理的工程团队
  - 希望摆脱单一模型提供商锁定、自由切换模型的 AI 工具用户
  product_signal: Ante 在 Terminal-Bench 2.1 上搭配 DeepSeek V4 Flash 0731 取得 82.7% 准确率，支持交互式
    TUI、headless、serve 与 gateway 四种运行模式。
  market_signal: 相比 Claude Code，Ante 在 Docker 中 20 个并行任务下使用约 7 倍更少的峰值内存与 9 倍更少的平均
    CPU，具备资源效率优势。
  differentiation: Ante 以约 15MB 单二进制实现零运行时依赖与完全离线推理，支持 12 家以上模型提供商并兼容 MCP，强调可验证、可负担、可随处运行。
  watch_reason: Ante 以单二进制、离线推理与显著资源效率优势切入编码智能体市场，其 82.7% 的 Terminal-Bench 2.1 成绩可公开审计，开源文档、协议与
    SDK 的策略也值得观察其社区与生态发展。
  risk_notes:
  - 核心 harness 目前以预编译二进制发布，源码尚未公开，存在安全与隐私方面的信任不确定性。
  - 项目仍处 alpha 预览阶段，官方明确提示会有破坏性变更与功能不完整。
  - 基准成绩由厂商自测发布，需第三方独立复现验证其真实水平。
  score: 8.0
  article_ids:
  - 4ebe2b50e1eb1ed8
  evidence_snippets:
  - Ante 是 Antigma Labs 开发的单二进制编码智能体，约 15MB 的 Rust 程序，零运行时依赖，可在终端内自组织运行。
  - Ante 在 Terminal-Bench 2.1 上搭配 DeepSeek V4 Flash 0731 取得 82.7% 准确率，并支持本地 GGUF 模型完全离线推理。
- object_type: project
  name: ante-harbor
  canonical_name: ante-harbor
  url: null
  positioning: ante-harbor 是 Antigma Labs 开源的 Harbor 智能体评测适配器，负责产出 Ante 的 Terminal-Bench
    结果，支持复现 antigma.ai/eval 上的评测运行。
  technical_signal: 作为 Ante 的评测管线，ante-harbor 在官方排行榜约束下运行 Terminal-Bench 2.1，每次结果固定精确构建版本并链接原始运行可供审计。
  adoption_signal: Ante 的官方 Terminal-Bench 结果即由 ante-harbor 产出，其 82.7% 成绩以 Harbor
    运行链接公开，可供社区复现验证。
  ecosystem_relevance: ante-harbor 依托 Harbor 智能体评测生态，使 Ante 的评测方法与结果可被社区审计与复现，有助于推动编码智能体评测透明化。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 评测管线是编码智能体可信度的关键基础设施，ante-harbor 将 Terminal-Bench 结果与具体构建版本和原始运行绑定，其可复现设计值得持续跟踪，以观察评测透明化能否成为行业实践。
  risk_notes:
  - 评测基准成绩为厂商自测发布，独立第三方复现尚未出现，实际水平有待验证。
  - Harbor 适配器与基准版本的兼容性可能随排行榜规则更新而需要持续维护。
  score: 6.0
  article_ids:
  - 4ebe2b50e1eb1ed8
  evidence_snippets:
  - ante-harbor 是 Ante 的 Harbor 智能体适配器，负责产出 Terminal-Bench 结果，可用于复现 antigma.ai/eval
    上的任何评测运行。
- object_type: project
  name: crates/agent-sdk
  canonical_name: Ante agent-sdk
  url: null
  positioning: crates/agent-sdk 是 Antigma Labs 开源的 Rust 版智能体 SDK 与客户端，用于基于 Ante agent
    运行时构建应用，遵循 Apache 2.0 许可。
  technical_signal: 作为 Rust 实现的 SDK 与客户端，agent-sdk 让开发者可以直接对接 agent 运行时构建自己的 harness
    与高性能助手，是 Ante 可扩展性的关键组件。
  adoption_signal: null
  ecosystem_relevance: 它是 Ante 开源策略的一部分，与文档、协议、评测管线一起构成围绕单二进制核心的开放生态，Apache 2.0 许可利于社区复用。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: agent-sdk 是 Ante 从单一产品走向平台化生态的关键棋子，观察开发者基于它构建的自定义智能体数量与质量，可判断其开源协议与
    SDK 策略能否形成真正的第三方生态。
  risk_notes:
  - SDK 与尚以预编译二进制发布的 core harness 深度耦合，核心源码未公开可能限制基于 SDK 的二次开发与调试能力。
  - 项目处于 alpha 阶段，SDK API 可能随破坏性变更频繁调整，增加集成方的维护成本。
  score: 5.0
  article_ids:
  - 4ebe2b50e1eb1ed8
  evidence_snippets:
  - crates/agent-sdk 是 Antigma Labs 开源的 Rust SDK 与客户端，用于基于 agent 运行时构建应用，遵循 Apache
    2.0 许可。
- object_type: project
  name: crates/protocol-shape
  canonical_name: Ante protocol-shape
  url: null
  positioning: crates/protocol-shape 是 Antigma Labs 开源的 Ante 核心协议实现，定义 ante serve
    模式所遵循的 schema 与线缆消息协议，支撑编辑器插件与集成。
  technical_signal: protocol-shape 以开源方式公开 Ante 的服务端线缆协议与 schema，使第三方编辑器插件与集成可以基于标准协议对接
    ante serve 模式。
  adoption_signal: null
  ecosystem_relevance: 开放协议是构建生态的基石，protocol-shape 让 ante serve 成为可编程的智能体后端，有助于编辑器、插件与自定义客户端围绕它形成集成生态。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 协议是否开放直接决定第三方能否深度集成与替换核心组件，protocol-shape 的开源让 Ante 具备成为可编程智能体协议标准的潜力，值得跟踪其被社区采用与扩展的情况。
  risk_notes:
  - 协议仍在 alpha 阶段演进，线缆格式可能发生破坏性变更，依赖该协议的集成方案需要紧跟版本。
  - 核心 harness 未开源，协议实现与二进制实际行为的完全一致性难以被外部验证。
  score: 5.0
  article_ids:
  - 4ebe2b50e1eb1ed8
  evidence_snippets:
  - crates/protocol-shape 定义了 ante serve 模式所遵循的 schema 与线缆消息协议，是 Ante 核心协议的开源实现。
- object_type: project
  name: nanochat-rs
  canonical_name: nanochat-rs
  url: null
  positioning: nanochat-rs 是 Ante 团队开源的教学版玩具引擎，用于研究内置 llama.cpp 本地推理引擎的工作原理，面向学习与实验场景。
  technical_signal: 作为教学用途的轻量引擎实现，nanochat-rs 展示了 llama.cpp 本地推理引擎的核心机制，帮助开发者理解 Ante
    离线推理能力的实现原理。
  adoption_signal: null
  ecosystem_relevance: nanochat-rs 承担技术布道与教育角色，通过公开 toy 引擎降低理解本地推理的门槛，间接吸引开发者关注 Ante
    的离线能力。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: nanochat-rs 虽为教学项目，但反映了 Ante 团队对离线推理引擎的技术取舍与实现细节，可作为观察 Ante 底层推理能力演进和开源教育策略的窗口。
  risk_notes:
  - 教学版 toy 引擎与 Ante 实际使用的固定版本 llama.cpp 存在差距，不能作为生产级离线推理性能的直接参考。
  - 作为教学项目，其维护活跃度与更新频率可能较低，技术内容存在过时风险。
  score: 4.0
  article_ids:
  - 4ebe2b50e1eb1ed8
  evidence_snippets:
  - nanochat-rs 是 Ante 团队开源的教学版玩具引擎，用于研究内置 llama.cpp 本地推理引擎的工作原理。
---

Alpha preview: expect breaking changes and incomplete functionality. macOS and Linux only; on Windows we suggest WSL.

Two things many people ask about:

**Where is the source?** The core harness currently ships as a prebuilt binary; this repo holds the docs, protocol, SDK, and eval pipeline (details). We are working out a way to ship the source code along with the binary, to address security and privacy concerns first, while taking the time to figure out how open source should work in the agentic era. If you have concerns today, run Ante in a sandbox: it is a single binary with minimal runtime dependencies, built to be easy to deploy in a container or on a remote machine.

**Is there telemetry?** Yes, and it is opt-out: set `ANTE_TELEMETRY=off`

to disable export entirely. What it sends is anonymous — a random installation label you can delete and re-mint, never your username, hostname, or machine id. The `RUST_LOG`

filter also applies to exported logs, a convenience carried over from the Rust ecosystem. A better UX is in the works. Details →

**A ghost in your shell.** Ante is a self-contained coding agent that lives in your terminal and self-organizes. One ~15MB Rust binary from Antigma Labs, zero runtime dependencies, built to get the most out of any model.

It works like Claude Code or Codex, with none of their dependencies or model constraints. It can also be the optimized core for building your own harness and high-performing assistants.

```
curl -fsSL https://ante.run/install.sh | bash
ante
```

Every agent claims to be good. Here are numbers you can check:

Ante runs Terminal-Bench 2.1 continuously under official leaderboard constraints: 89 tasks, 5 trials each. Each result pins the exact build you can download and links the raw Harbor run for independent audit. Latest full run: **82.7%** with open-weight **DeepSeek V4 Flash 0731** (368/445 trials, Ante 0.preview.71, about $68 of inference). DeepSeek reports the same 82.7 for this model, measured with its unreleased DeepSeek Harness in minimal mode.

**Live results →** · Methodology →

Ante is hand-written Rust with the heavy parts (`Grep`

, `git`

) embedded in one binary, one process, and local inference handled by a pinned, managed llama.cpp. Across the same 20 parallel tasks in Docker, Ante uses **~7× less peak memory**, **~9× less average CPU**, and **~5× less disk I/O** than Claude Code.

**Raw numbers →** · Benchmark details →

Ante's inference engine is a pinned, managed version of llama.cpp. Point it at a GGUF file and the whole loop runs on your machine: no API key, no account, no internet.

```
ante --offline-model ~/.ante/models/Qwen3.5-9B-Q4_K_M.gguf \
-p "add error handling to src/main.rs"
```

**Offline mode →** · nanochat-rs, a toy engine for study →

The three are one design decision. An agent you can **verify**, **afford**, and **run anywhere** is light enough to run by the *thousands*: the substrate for self-organizing intelligence.

Ante is a single, self-contained binary with no external dependencies: download and run.

```
curl -fsSL https://ante.run/install.sh | bash
# Install a specific release channel
curl -fsSL https://ante.run/install.sh | bash -s -- nightly
# Install into a directory already on PATH
curl -fsSL https://ante.run/install.sh | ANTE_INSTALL_DIR=/usr/local/bin bash
```

| Mode | Command | Use it for |
|---|---|---|
| Interactive TUI | `ante` |
day-to-day work in the terminal |
| Headless | `ante -p "..."` |
one-shot tasks, scripts, CI |
| Server | `ante serve` |
editor plugins and integrations, over a JSONL protocol |
| Gateway | `ante gateway` |
running Ante as a Slack or Discord bot |

```
# Fix a bug
ante -p "find and fix the failing test in src/auth"
# Review a diff
git diff | ante -p "review this for security issues"
# Use a different provider
ante --provider openai --model gpt-5.5 -p "refactor the database module"
# Resume a saved session
ante --resume ses_01ARZ3NDEKTSV4RRFFQ69G5FAV -p "now add tests"
# Run fully offline with a local GGUF model
ante --offline-model ~/.ante/models/Qwen3.5-9B-Q4_K_M.gguf \
-p "add error handling to src/main.rs"
```

```
ante update
# One-off update from a different channel
ante update --channel nightly
# Roll back or pin to an exact release
ante update --version v0.preview.71
```

**Zero vendor lock-in**: bring your own API key, subscription, or local model. Switch between 12+ providers freely. No account required, not even with us.**Multi-agent orchestration**: spawn sub-agents and coordinate complex tasks across independent, decentralized, and centralized architectures. See the patterns →**Channel integrations**: run Ante as a Slack or Discord bot with`ante gateway`

.**Extensible**: custom skills, sub-agents, MCP, and persistent memory across sessions.

Ante works with 12+ providers out of the box:

| Provider | Example Models |
|---|---|
| Anthropic | Claude Sonnet 4.5, Opus 4.6 |
| OpenAI | GPT-5 family |
| Google Gemini | Gemini 3 family |
| Grok (xAI) | Grok 4 |
| Open Router | Multiple providers |
| Local (GGUF) | Any GGUF model via built-in llama.cpp |
| ...and more | Vertex AI, Zai, Antix, OpenAI-compatible |

Configure providers via environment variables (`ANTHROPIC_API_KEY`

, `OPENAI_API_KEY`

, etc.) or OAuth. Add custom providers in `~/.ante/catalog.json`

.

We open sourced what really matters in the age of agentic coding, all under Apache 2.0:

**Detailed documentation, the descriptive truth.**`docs-site/`

is the source for docs.antigma.ai: a precise description of what the harness does and how to drive it.**The protocol, the algorithm of the core.**`crates/protocol-shape`

defines the schema and wire messages spoken by`ante serve`

;`crates/agent-sdk`

is the Rust SDK and client for building against agent runtimes.**The eval pipeline, constraint and continuous improvement.**`ante-harbor/`

is the Harbor agent adapter behind our Terminal-Bench results: use it to reproduce any run at antigma.ai/eval.`CHANGELOG.md`

records the improvement, release by release.

The core harness itself is developed in a private repository during the alpha and ships as a prebuilt binary via releases. Core libraries from it are included here progressively as they stabilize; `crates/exec`

, standalone process execution, is the first.

The protocol surface maps to Ante's client-daemon architecture:

```
┌─────────────────────────────────────────────────────────────┐
│ Clients │
│ │
│ ┌───────────┐ ┌───────────┐ ┌────────────────────┐ │
│ │ TUI │ │ Headless │ │ ante serve │ │
│ │ (ante) │ │ (ante -p) │ │ (stdio / ws) │ │
│ └─────┬─────┘ └─────┬─────┘ └─────────┬──────────┘ │
└─────────┼────────────────┼─────────────────────┼────────────┘
│ │ │
▼ ▼ ▼
┌─────────────────────────────────────────────────────────────┐
│ Daemon │
│ │
│ Session ──▶ Turn ──▶ Step │
│ │
│ ┌──────────┐ ┌──────────────┐ ┌───────────────────┐ │
│ │ Tools │ │ Permission │ │ Skills / Agents │ │
│ └──────────┘ └──────────────┘ └───────────────────┘ │
└────────────────────────┬────────────────────────────────────┘
│
▼
┌─────────────────────────────────────────────────────────────┐
│ LLM Providers │
│ │
│ Anthropic · OpenAI · Gemini · Grok · Open Router · Local │
└─────────────────────────────────────────────────────────────┘
```



We care about the harness, not the model or the prompts.

Documentation is the new source code.

Ante is designed for **cellular-native** agents: like cells in an organism, tiny, expendable, massively replicated. That thesis is why the three headline claims exist. A cell-scale agent must be *verified* (reliability compounds at scale), *tiny* (every byte is multiplied by thousands), and *self-contained* (no runtime to install, no service to phone home to). Read more in our philosophy and agent organization patterns.

The name is the answer: **An**other **Te**rminal agent, and *ante*, the stake you put on the table to play. Ante is fast, lightweight, and the only terminal agent with native local inference built in. We believe a self-contained agent core that self-organizes is the foundation of the coming agent economy.

**How is Ante different from other agents?**

Ante has most of the features you expect from agents like Claude Code or Codex: multi-agents, skills, MCP, persistent memory. The difference is the build philosophy.

- Built from scratch in Rust. Core components like
`Grep`

(fully rebuilt and customized) and`git`

are embedded in the same ~15MB binary and run in the same process at runtime, so nothing is shelled out and no resources leak. Most similar projects ship on Node.js or CPython and carry an order-of-magnitude larger footprint. - Local inference is built in: the engine is a pinned, managed version of llama.cpp, so a local GGUF model is all Ante needs to run without any provider. To study how such an engine works, see nanochat-rs, our toy version.
- No vendor lock-in, not even to ourselves: no account needed, reuse your existing API credentials. An opt-in, fully integrated server-side experience lives at antix.antigma.ai.
- Every claim is backed by public, reproducible benchmarks of the exact builds we ship: antigma.ai/eval.

Beyond the footprint it comes down to agent architecture, and ultimately to *who* is building it and with what philosophy. Anyone can fork a binary; taste and engineering rigor don't copy. Those differences leak into every detail of the product.

**Why care about runtime optimization like memory and I/O if model inference is usually the biggest bottleneck?**

For one-on-one agent interactions, runtime overhead like memory usage and I/O is often less important than model inference.

But our vision is much bigger: millions of agents self-organizing and communicating at massive scale. At that point, even small inefficiencies get multiplied millions or billions of times, so runtime optimization becomes economically significant.

**Can I run Ante completely offline?**

Yes. Ante has a built-in llama.cpp engine that runs GGUF models locally. It handles engine installation, model discovery, and memory management automatically. No API keys or internet connection required.

**Can I use my own custom models or providers?**

Yes. Create a `~/.ante/catalog.json`

file to add or override providers and models with custom endpoints, API keys, and configurations. Any OpenAI-compatible API works.

**What is the **`ante serve`

mode for?

`ante serve`

mode for?Server mode runs Ante as a long-lived daemon that communicates over a structured JSONL protocol. It's ideal for building editor plugins, web UIs, and custom integrations on top of Ante.

Full documentation is available at docs.antigma.ai.

Source code in this repository (including the SDK and protocol crates) is licensed under the Apache License 2.0.

The prebuilt `ante`

binary is free to use — including commercially — during
the alpha preview under the Binary Preview Terms. The core
harness is currently developed in a private repository and shipped as a
binary; the SDK and protocol surface you build against here will remain
permissively licensed.