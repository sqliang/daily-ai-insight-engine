---
title: trycua/cua
source: https://github.com/trycua/cua
author: []
published: ''
created: '2026-06-16'
description: 'Open-source infrastructure for Computer-Use Agents. Sandboxes, SDKs,
  and benchmarks to train and evaluate AI agents that can control full desktops (macOS,
  Linux, Windows). Build, benchmark, and deploy agents that use computers Choose Your
  Path Building your own agent? Start with Cua · Giving a coding agent a computer?
  Cua Drivers · Evaluating or training models? Cua Bench · Need macOS VMs? Lume Cua
  Drivers - Background computer-use on macOS and Windows, with Linux pre-release Drive
  native desktop apps in the background. Agents click, type, and verify without stealing
  the cursor or focus. Use the same CLI and MCP server on macOS and Windows from Claude
  Code, Cursor, Codex, OpenClaw, and custom clients. Linux support is available as
  a pre-release backend while platform testing is still in progress. macOS / Linux
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/trycua/cua/main/libs/cua-driver/scripts/install.sh)"
  Windows (PowerShell) irm https://raw.githubusercontent.com/trycua/cua/main/libs/cua-driver/scripts/install.ps1
  | iex Then wire it into Claude Code as an MCP server and your agent can drive the
  desktop in the background: claude mcp add --transport stdio cua-driver -- cua-driver
  mcp Full tool reference, architecture notes, and the optional agent skill pack live
  here: libs/cua-driver/README.md. Cua - Agent-Ready Sandboxes for Any OS Build agents
  that see screens, click buttons, and complete tasks autonomously. One API for any
  VM or container image — cloud or local. pip install cua # Requires Python 3.11 or
  later from cua import Sandbox, Image # Same API regardless of OS or runtime async
  with Sandbox.ephemeral(Image.linux()) as sb: # or .macos() .windows() .android()
  result = await sb.shell.run("echo hello") screenshot = await sb.screenshot() await
  sb.mouse.click(100, 200) await sb.keyboard.type("Hello from Cua!") await sb.mobile.gesture((100,
  500), (100, 200)) # multi-touch gestures Linux container Linux VM macOS Windows
  Android BYOI (.qcow2, .iso) Cloud (cua.ai) ✅ ✅ ✅ ✅ ✅ 🔜 soon Local (QEMU) ✅ ✅ ✅ ✅
  ✅ ✅ Get Started | Examples | API Reference Cua-Bench - Benchmarks & RL Environments
  Evaluate computer-use agents on OSWorld, ScreenSpot, Windows Arena, and custom tasks.
  Export trajectories for training. # Clone, install, and create base image git clone
  https://github.com/trycua/cua && cd cua/cua-bench uv tool install -e . && cb image
  create linux-docker # Run benchmark with agent cb run dataset datasets/cua-bench-basic
  --agent cua-agent --max-parallel 4 Get Started | Partner With Us | Registry | CLI
  Reference Lume - macOS Virtualization Create and manage macOS/Linux VMs with near-native
  performance on Apple Silicon using Apple''s Virtualization.Framework. # Install
  Lume /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/trycua/cua/main/libs/lume/scripts/install.sh)"
  # Pull & start a macOS VM lume run macos-sequoia-vanilla:latest Get Started | FAQ
  | CLI Reference Packages Package Description cua-driver Background computer-use
  agent for macOS, Windows, and Linux cua-agent AI agent framework for computer-use
  tasks cua-sandbox SDK for creating and controlling sandboxes cua-computer-server
  Driver for UI interactions and code execution in sandboxes cua-bench Benchmarks
  and RL environments for computer-use lume macOS/Linux VM management on Apple Silicon
  lumier Docker-compatible interface for Lume VMs Resources Documentation — Guides,
  examples, and API reference Blog — Tutorials, updates, and research Discord — Community
  support and discussions GitHub Issues — Bug reports and feature requests Contributing
  We welcome contributions! See our Contributing Guidelines for details. License MIT
  License — see LICENSE for details. Third-party components have their own licenses:
  Kasm (MIT) OmniParser (CC-BY-4.0) Optional cua-agent[omni] includes ultralytics
  (AGPL-3.0) Trademarks Apple, macOS, Ubuntu, Canonical, and Microsoft are trademarks
  of their respective owners. This project is not affiliated with or endorsed by these
  companies. Thank you to all our GitHub Sponsors!'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: feacb1c4ff8cc40f
source_type: community_discussion
tldr: trycua/cua 是一个开源计算机操作代理框架，支持通过单一 API 在 macOS、Windows、Linux 和 Android 上控制桌面应用，提供
  CLI、MCP 服务器、Python SDK 和沙箱环境。
objective_summary: trycua/cua 发布了计算机操作代理框架，包含 cua-driver、cua-agent、cua-sandbox、cua-bench
  和 lume 等多个子项目。该项目支持在后台驱动桌面应用（点击、输入、验证），不抢占光标焦点，可通过 CLI 和 MCP 服务器从 Claude Code、Cursor、Codex
  等客户端调用。Cua 提供 Python SDK（pip install cua），支持 Linux 容器、Linux VM、macOS、Windows 和 Android
  环境，同时包含计算机使用基准测试和 macOS/Linux VM 管理工具。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - trycua
  technologies:
  - MCP
  - QEMU
  - Apple Virtualization.Framework
  key_people: []
key_logic_flow:
- Cua 是一个开源计算机操作代理框架，提供统一 API 用于在多种操作系统上控制桌面应用。
- cua-driver 允许代理在后台执行点击、输入和验证操作，不抢占用户光标焦点，支持 macOS、Windows 和 Linux。
- cua-sandbox 提供 Python SDK（通过 pip install cua 安装），支持 Linux 容器、Linux VM、macOS、Windows
  和 Android 环境。
- cua-bench 提供计算机使用代理的基准测试和强化学习环境，支持 OSWorld、ScreenSpot、Windows Arena 等数据集。
- lume 是基于 Apple Virtualization.Framework 的 macOS/Linux VM 管理工具，在 Apple Silicon 上提供接近原生性能。
- 该项目使用 MIT 许可证，依赖的 OmniParser 使用 CC-BY-4.0 许可证，可选组件 cua-agent[omni] 包含 AGPL-3.0 的
  ultralytics。
extract_result: success
object_mentions:
- object_type: project
  name: trycua/cua
  canonical_name: trycua/cua
  url: https://github.com/trycua/cua
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Cua 是一个开源计算机操作代理框架，提供 Python SDK 和统一 API 用于控制桌面应用。
  - 该项目包含 cua-driver、cua-agent、cua-sandbox、cua-bench 和 lume 等多个子项目。
  - Cua 支持通过 MCP 服务器从 Claude Code、Cursor 和 Codex 等客户端调用。
  article_id: feacb1c4ff8cc40f
- object_type: project
  name: cua-driver
  canonical_name: trycua/cua/cua-driver
  url: https://github.com/trycua/cua
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - cua-driver 是 Cua 的桌面驱动组件，允许代理在后台驱动 macOS、Windows 和 Linux 桌面应用。
  - cua-driver 支持通过 MCP 服务器集成到 Claude Code、Cursor 和 Codex 等客户端中。
  article_id: feacb1c4ff8cc40f
- object_type: project
  name: cua-agent
  canonical_name: trycua/cua/cua-agent
  url: https://github.com/trycua/cua
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - cua-agent 是 Cua 中用于计算机操作任务的 AI 代理框架。
  - 可选组件 cua-agent[omni] 包含 ultralytics，使用 AGPL-3.0 许可证。
  article_id: feacb1c4ff8cc40f
- object_type: project
  name: cua-sandbox
  canonical_name: trycua/cua/cua-sandbox
  url: https://github.com/trycua/cua
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - cua-sandbox 是 Cua 的沙箱 SDK，用于创建和控制虚拟机或容器环境。
  - 开发者可通过 pip install cua 安装后使用 Sandbox.ephemeral() 创建临时沙箱实例。
  article_id: feacb1c4ff8cc40f
- object_type: project
  name: cua-bench
  canonical_name: trycua/cua/cua-bench
  url: https://github.com/trycua/cua
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - cua-bench 用于在 OSWorld、ScreenSpot 和 Windows Arena 等数据集上评估计算机操作代理。
  - cua-bench 支持导出轨迹数据用于训练，并通过 uv tool install 安装后使用 cb 命令运行。
  article_id: feacb1c4ff8cc40f
- object_type: project
  name: lume
  canonical_name: trycua/cua/lume
  url: https://github.com/trycua/cua
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - lume 是基于 Apple Virtualization.Framework 的 VM 管理工具，在 Apple Silicon 上提供接近原生性能。
  - lume 支持创建和管理 macOS 和 Linux 虚拟机，可通过 lume run 命令启动。
  article_id: feacb1c4ff8cc40f
- object_type: product
  name: cua.ai
  canonical_name: cua.ai
  url: https://cua.ai
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - cua.ai 是 Cua 的云服务，支持 Linux 容器、Linux VM、macOS、Windows 和 Android 环境。
  - Cua 提供本地（QEMU）和云（cua.ai）两种运行方式，本地支持 BYOI 自定义镜像。
  article_id: feacb1c4ff8cc40f
- object_type: project
  name: cua-computer-server
  canonical_name: trycua/cua/cua-computer-server
  url: https://github.com/trycua/cua
  confidence: medium
  article_role: primary_subject
  evidence_snippets:
  - cua-computer-server 是 Cua 中负责 UI 交互和沙箱内代码执行的驱动组件。
  article_id: feacb1c4ff8cc40f
- object_type: project
  name: lumier
  canonical_name: trycua/cua/lumier
  url: https://github.com/trycua/cua
  confidence: low
  article_role: ecosystem_context
  evidence_snippets:
  - lumier 是 Cua 生态中的项目，为 Lume VM 提供 Docker 兼容接口。
  article_id: feacb1c4ff8cc40f
impact_score:
  score: 6.8
  reason: 该项目的评分依据如下：这是一个开源计算机使用代理全栈工具链的发布，整合了沙箱、驱动、代理框架和基准测试四大模块，并通过MCP协议与主流AI编码工具（Claude
    Code、Cursor等）打通。其价值在于将此前分散在各AI实验室的计算机使用代理能力标准化、开源化，降低了开发者的准入门槛。但该领域仍处于早期阶段，项目本身是现有技术（QEMU、Apple
    Virtualization.Framework）的工程化整合而非全新的理论突破，且社区尚未形成大规模采用。综合评估：改变局部竞争格局，但尚未达到行业范式转移级别。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: MCP协议集成与不抢占焦点的后台桌面操作能力，可直接接入Claude Code和Cursor等AI编码工具
hype_assessment:
  level: low
  reason: 项目README采用技术驱动的客观描述方式，详细列出了各模块功能、API示例、支持平台和限制条件（如Linux标注为pre-release、第三方组件许可证声明），没有使用'颠覆''革命性'等PR滥用词汇，宣传水分较低。
information_entropy: high
domain_disruption:
  technical_innovation: 提供了统一的多平台沙箱API抽象层（Linux/Windows/macOS/Android），后台桌面驱动支持不抢占光标焦点运行计算机使用代理，并通过MCP协议将这种能力暴露为AI编码工具的标准工具接口，打通了智能体与桌面应用的桥梁。
  business_model: 开源核心（MIT许可证）+云端执行服务（cua.ai）的双轨商业模式，通过MCP协议生态绑定开发者，将开源社区转化为付费云端沙箱客户，类似GitHub
    Codespaces模式在计算机使用代理领域的迁移。
engineering_complexity: production_ready
compound_value:
  score: 7.5
  reason: 计算机使用代理是AI Agent能力的关键基础设施层，trycua/cua是业界首个提供从沙箱(Sandbox)、后台桌面驱动(Driver)、Agent框架到基准测试(Bench)完整开源工具链的项目。核心投资逻辑：1)
    MIT许可证+ MCP协议深度绑定，有望形成'计算机使用代理的默认开源基建'定位，驱动开发者生态网络效应——越多项目基于其构建，切换成本越高，复利效应越强；2)
    后台非抢占式桌面驱动技术（不抢光标/焦点）在技术上构成差异化壁垒，解决了Agent自动化中用户痛点；3) 跨平台一站式API（Linux/macOS/Windows/Android）极大降低集成成本，单一接口即可对接多种运行环境。长期风险在于：项目尚处早期，面临OpenAI
    CUA等闭源方案的生态和品牌竞争，纯开源模式的可商业变现路径（如云服务cua.ai）尚待验证。综合评定7.5分，位于细分赛道基础设施潜力段的上沿，3-5年后若开发者生态形成临界规模则大概率成为行业基石。
value_capture_layer: agent_middleware
moat_impact: creates_new_moat
key_beneficiaries:
- Anthropic
- trycua
- Cursor
competitive_casualty:
- OpenAI
- 传统RPA厂商
- 闭源Agent基础设施提供商
market_opportunities:
- 企业级RPA厂商可将cua-driver的背景桌面操控能力集成到现有自动化流程中，实现不抢占光标的无感自动化，显著提升用户体验和部署接受度
- AI编码工具（如Cursor、Claude Code）可通过MCP接入cua-driver，赋予代理操作本地桌面应用的能力，开辟'代码编辑+桌面自动化'的融合产品形态
- cua-bench与沙箱SDK可用于构建计算机使用代理的训练数据生产线，为模型微调和强化学习提供标准化的轨迹数据采集与评估平台
risk_matrix:
  regulatory: 计算机使用代理可操控桌面应用执行任意操作，可能触发各国对自动化软件的安全审查与合规要求（如欧盟AI Act对高风险自动化系统的分类），且涉及屏幕截图传输可能违反数据保护法规
  technological: 依赖QEMU和Apple Virtualization.Framework等虚拟化技术，在Windows/Linux非容器场景下的稳定性和性能有待验证；Lume仅支持Apple
    Silicon，限制了x86 macOS用户的可用性
  competitive: Anthropic Computer Use、OpenAI Operator、Google Mariner等巨头产品在原生能力和生态整合上更具优势；开源替代项目（如Open-Interpreter、CogAgent）可能形成碎片化竞争
  ethical: 屏幕抓取与桌面操控能力可被滥用于自动化攻击、数据窃取或监控；背景操作特性降低了用户感知度，增加了无授权操控的风险；benchmark导出的执行轨迹若包含敏感数据可能引发隐私问题
  additional:
  - 项目采用MIT许可证但部分依赖组件（如Ultralytics使用AGPL-3.0），AGPL的传染性可能对商业集成构成许可合规风险
  - 云服务(cua.ai)与本地运行的混合架构可能导致用户对数据流向和隐私边界产生混淆
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: deep_dive
object_insights:
- object_type: project
  name: trycua/cua
  canonical_name: trycua/cua
  url: https://github.com/trycua/cua
  positioning: 开源计算机操作代理框架，提供统一 API 和 Python SDK 用于在后台控制 macOS、Windows、Linux 和 Android
    桌面应用，不抢占用户光标焦点。
  technical_signal: 采用模块化架构，包含 cua-driver、cua-agent、cua-sandbox、cua-bench 和 lume 等子项目，支持通过
    MCP 服务器协议与主流 AI 客户端集成。
  adoption_signal: 已支持从 Claude Code、Cursor 和 Codex 等主流 AI 编码工具调用，提供 MIT 开源许可降低企业和社区采用门槛。
  ecosystem_relevance: 填补了 AI 代理框架与真实桌面操作系统之间的交互层空白，与 MCP 协议生态高度互补，有望成为 AI 代理操作桌面的标准基础设施。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 作为开源计算机操作代理框架，统一了跨平台桌面自动化 API 和后台驱动能力，有望成为 AI 代理与现实桌面应用交互的标准中间层基础设施，值得持续跟踪其社区生态发展和企业采用进度。
  risk_notes:
  - Linux 支持目前为预发布状态，跨平台兼容性和稳定性仍在完善中。
  - 可选组件 cua-agent[omni] 依赖 AGPL-3.0 许可证的 ultralytics，可能带来合规风险。
  score: 8.0
  article_ids:
  - feacb1c4ff8cc40f
  evidence_snippets:
  - Cua 是一个开源计算机操作代理框架，提供 Python SDK 和统一 API 用于控制桌面应用。
  - 该项目包含 cua-driver、cua-agent、cua-sandbox、cua-bench 和 lume 等多个子项目。
  - Cua 支持通过 MCP 服务器从 Claude Code、Cursor 和 Codex 等客户端调用。
- object_type: project
  name: cua-driver
  canonical_name: trycua/cua/cua-driver
  url: https://github.com/trycua/cua
  positioning: Cua 框架的桌面驱动组件，支持 AI 代理在后台驱动 macOS、Windows 和 Linux 桌面应用，执行点击、输入和验证操作且不抢占用户光标焦点。
  technical_signal: 通过 MCP 服务器协议与 AI 客户端集成，支持在后台执行点击、输入和屏幕验证等操作，不干扰用户当前操作焦点。
  adoption_signal: 可通过 MCP 服务器集成到 Claude Code、Cursor 和 Codex 等主流 AI 编码工具中，提供安装脚本简化部署流程。
  ecosystem_relevance: 作为 Cua 框架的核心驱动层，与 MCP 协议生态深度耦合，为 AI 代理操作桌面应用提供了可复用的参考实现。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 桌面后台驱动能力是 Cua 框架的差异化核心，其不抢占光标的实现方式和 MCP 集成方案值得持续跟踪其在真实工作流中的稳定性和用户反馈。
  risk_notes:
  - 跨平台稳定性和兼容性仍在测试中，Windows 与 Linux 环境可能面临不同的权限和安全限制。
  score: 7.0
  article_ids:
  - feacb1c4ff8cc40f
  evidence_snippets:
  - cua-driver 是 Cua 的桌面驱动组件，允许代理在后台驱动 macOS、Windows 和 Linux 桌面应用。
  - cua-driver 支持通过 MCP 服务器集成到 Claude Code、Cursor 和 Codex 等客户端中。
- object_type: project
  name: cua-agent
  canonical_name: trycua/cua/cua-agent
  url: https://github.com/trycua/cua
  positioning: Cua 框架中用于计算机操作任务的 AI 代理框架，负责视觉理解和操作规划，可选集成视觉组件增强屏幕分析能力。
  technical_signal: 可选集成 OmniParser 和 ultralytics 等视觉组件，支持屏幕理解和元素定位等高级功能，提升代理桌面操作自主性。
  adoption_signal: 作为 Cua 框架的默认代理实现，已对接 cua-bench 基准测试评估体系，可量化衡量代理性能表现。
  ecosystem_relevance: 与 cua-sandbox 和 cua-driver 等组件紧密协作，构成完整的计算机操作代理技术栈，承担 AI 决策核心职责。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 作为 Cua 框架的 AI 决策核心，其视觉理解和操作规划能力直接决定了框架整体自动化水平，值得跟踪其模型选型和性能演进。
  risk_notes:
  - 可选组件 cua-agent[omni] 的 AGPL-3.0 许可证可能限制商业使用场景。
  - 集成第三方视觉组件的稳定性和准确性在复杂桌面环境中仍有待验证。
  score: 6.0
  article_ids:
  - feacb1c4ff8cc40f
  evidence_snippets:
  - cua-agent 是 Cua 中用于计算机操作任务的 AI 代理框架。
  - 可选组件 cua-agent[omni] 包含 ultralytics，使用 AGPL-3.0 许可证。
- object_type: project
  name: cua-sandbox
  canonical_name: trycua/cua/cua-sandbox
  url: https://github.com/trycua/cua
  positioning: Cua 框架的沙箱 SDK，用于创建和控制虚拟机或容器环境，支持 Linux、macOS、Windows 和 Android 等多种操作系统镜像。
  technical_signal: 提供 Python SDK 和统一 API，通过 pip install cua 安装后可一键创建临时沙箱实例，屏蔽底层虚拟化差异。
  adoption_signal: 支持云（cua.ai）和本地（QEMU）两种运行方式，本地支持 BYOI 自定义镜像，降低用户部署和测试成本。
  ecosystem_relevance: 为 AI 代理提供隔离的运行环境抽象，统一了 Linux 容器、Linux VM、macOS、Windows 和 Android
    等多种平台的操作接口。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 沙箱 SDK 提供了统一的跨平台运行环境抽象，大幅降低了 AI 代理在真实操作系统上执行任务的准入门槛，值得跟踪其环境兼容性和性能表现。
  risk_notes:
  - 云服务 cua.ai 的可用性、稳定性和收费模式尚未明确公开。
  - 本地运行依赖 QEMU 等虚拟化技术，性能开销可能影响复杂任务的执行效率。
  score: 7.0
  article_ids:
  - feacb1c4ff8cc40f
  evidence_snippets:
  - cua-sandbox 是 Cua 的沙箱 SDK，用于创建和控制虚拟机或容器环境。
  - 开发者可通过 pip install cua 安装后使用 Sandbox.ephemeral() 创建临时沙箱实例。
- object_type: project
  name: cua-bench
  canonical_name: trycua/cua/cua-bench
  url: https://github.com/trycua/cua
  positioning: Cua 框架的基准测试和强化学习环境，用于在 OSWorld、ScreenSpot 和 Windows Arena 等数据集上评估计算机操作代理性能。
  technical_signal: 支持导出代理运行轨迹数据用于训练，提供 cb 命令行工具，支持多任务并行评估和自定义代理接入。
  adoption_signal: 可通过 uv tool install 安装，支持 cua-agent 等自定义代理接入基准测试流程，降低评估门槛。
  ecosystem_relevance: 填补了计算机操作代理标准化评估工具的空白，与 OSWorld 等公开数据集互补，有望推动该领域形成可比较的基准体系。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 作为计算机操作代理的标准化评估工具，其数据集覆盖范围和评估方法论可能影响该领域的技术发展和横向对比标准。
  risk_notes:
  - 当前覆盖的数据集范围有限，可能无法全面反映真实复杂场景下的代理性能表现。
  score: 6.0
  article_ids:
  - feacb1c4ff8cc40f
  evidence_snippets:
  - cua-bench 用于在 OSWorld、ScreenSpot 和 Windows Arena 等数据集上评估计算机操作代理。
  - cua-bench 支持导出轨迹数据用于训练，并通过 uv tool install 安装后使用 cb 命令运行。
- object_type: project
  name: lume
  canonical_name: trycua/cua/lume
  url: https://github.com/trycua/cua
  positioning: 基于 Apple Virtualization.Framework 的 macOS 和 Linux 虚拟机管理工具，在 Apple Silicon
    上提供接近原生性能的虚拟化方案。
  technical_signal: 利用 Apple 官方虚拟化框架实现高性能 VM 管理，支持通过 lume run 命令一键启动 macOS 和 Linux
    虚拟机。
  adoption_signal: 提供 curl 一键安装脚本和简洁 CLI 工具，与 Cua 沙箱生态紧密集成，降低 VM 管理操作复杂度。
  ecosystem_relevance: 为 Cua 沙箱在 Apple Silicon 上提供底层虚拟化基础设施，是 Cua 框架在 macOS 环境中运行的关键依赖组件。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 基于 Apple 原生虚拟化框架打造的 VM 管理方案在 Apple Silicon 上具有显著的性能优势，值得跟踪其在 Cua 生态中的采用深度。
  risk_notes:
  - 仅支持 Apple Silicon 硬件，无法在 Intel Mac 和其他非 Apple 平台上使用，场景受限。
  score: 5.0
  article_ids:
  - feacb1c4ff8cc40f
  evidence_snippets:
  - lume 是基于 Apple Virtualization.Framework 的 VM 管理工具，在 Apple Silicon 上提供接近原生性能。
  - lume 支持创建和管理 macOS 和 Linux 虚拟机，可通过 lume run 命令启动。
- object_type: project
  name: cua-computer-server
  canonical_name: trycua/cua/cua-computer-server
  url: https://github.com/trycua/cua
  positioning: Cua 框架中负责 UI 交互和沙箱内代码执行的驱动组件，连接 AI 代理决策层与桌面操作执行层的关键中间件。
  technical_signal: 专注于在沙箱环境中执行 UI 交互操作和代码运行，承担将代理意图转换为实际桌面操作的关键执行职责。
  adoption_signal: 作为 Cua 框架内部组件，主要通过 Cua 整体框架被间接采用，不面向最终用户独立发布。
  ecosystem_relevance: 在 Cua 架构中承担 UI 操作执行和代码运行的双重职责，是框架从决策到执行链路中的核心保障组件。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 作为连接 AI 决策与桌面操作的关键执行中间件，其执行效率和操作可靠性直接影响 Cua 框架的整体用户体验和可用性。
  risk_notes:
  - 技术边界与 cua-driver 存在潜在功能重叠，组件职责划分有待进一步明确。
  score: 5.0
  article_ids:
  - feacb1c4ff8cc40f
  evidence_snippets:
  - cua-computer-server 是 Cua 中负责 UI 交互和沙箱内代码执行的驱动组件。
- object_type: product
  name: cua.ai
  canonical_name: cua.ai
  url: https://cua.ai
  positioning: Cua 开源框架的配套云服务平台，提供 Linux 容器、Linux VM、macOS、Windows 和 Android 环境的托管运行服务，与本地
    SDK API 一致。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - AI 代理开发者
  - 需要跨平台测试环境的团队
  - 不愿自己配置虚拟化基础设施的企业用户
  product_signal: 支持多种操作系统环境的云托管，提供与本地 QEMU 完全一致的 API 接口，实现本地开发与云端部署的无缝切换体验。
  market_signal: 作为 Cua 开源框架的商业化云服务，填补了开源项目在托管执行环境方面的需求缺口，有助于吸引企业级用户。
  differentiation: 与开源框架深度集成，提供与本地 SDK 一致的 API 接口和工作流，实现本地开发与云端执行的无缝切换。
  watch_reason: 作为 Cua 生态的核心商业化产品，其定价策略、服务可靠性和功能边界将直接影响 Cua 框架的可持续发展和企业用户采用决策。
  risk_notes:
  - 服务定价和商业条款尚未公开，商业化落地路径有待观察。
  - 云服务与开源项目本地运行之间的功能差异可能影响用户体验一致性。
  score: 6.0
  article_ids:
  - feacb1c4ff8cc40f
  evidence_snippets:
  - cua.ai 是 Cua 的云服务，支持 Linux 容器、Linux VM、macOS、Windows 和 Android 环境。
  - Cua 提供本地（QEMU）和云（cua.ai）两种运行方式，本地支持 BYOI 自定义镜像。
---

**Building your own agent?** Start with Cua ·
**Giving a coding agent a computer?** Cua Drivers ·
**Evaluating or training models?** Cua Bench ·
**Need macOS VMs?** Lume

Drive native desktop apps **in the background**. Agents click, type, and verify without stealing the cursor or focus. Use the same CLI and MCP server on macOS and Windows from Claude Code, Cursor, Codex, OpenClaw, and custom clients. Linux support is available as a pre-release backend while platform testing is still in progress.

**macOS / Linux**

`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/trycua/cua/main/libs/cua-driver/scripts/install.sh)"`

**Windows (PowerShell)**

`irm https://raw.githubusercontent.com/trycua/cua/main/libs/cua-driver/scripts/install.ps1 | iex`

Then wire it into Claude Code as an MCP server and your agent can drive the desktop in the background:

`claude mcp add --transport stdio cua-driver -- cua-driver mcp`

Full tool reference, architecture notes, and the optional agent skill pack live here: `libs/cua-driver/README.md`

.

Build agents that see screens, click buttons, and complete tasks autonomously. One API for any VM or container image — cloud or local.

`pip install cua`

```
# Requires Python 3.11 or later
from cua import Sandbox, Image
# Same API regardless of OS or runtime
async with Sandbox.ephemeral(Image.linux()) as sb: # or .macos() .windows() .android()
result = await sb.shell.run("echo hello")
screenshot = await sb.screenshot()
await sb.mouse.click(100, 200)
await sb.keyboard.type("Hello from Cua!")
await sb.mobile.gesture((100, 500), (100, 200)) # multi-touch gestures
```

| Linux container | Linux VM | macOS | Windows | Android | BYOI (.qcow2, .iso) | |
|---|---|---|---|---|---|---|
Cloud (cua.ai) |
✅ | ✅ | ✅ | ✅ | ✅ | 🔜 soon |
Local (QEMU) |
✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Get Started** | **Examples** | **API Reference**

Evaluate computer-use agents on OSWorld, ScreenSpot, Windows Arena, and custom tasks. Export trajectories for training.

```
# Clone, install, and create base image
git clone https://github.com/trycua/cua && cd cua/cua-bench
uv tool install -e . && cb image create linux-docker
# Run benchmark with agent
cb run dataset datasets/cua-bench-basic --agent cua-agent --max-parallel 4
```

**Get Started** | **Partner With Us** | **Registry** | **CLI Reference**

Create and manage macOS/Linux VMs with near-native performance on Apple Silicon using Apple's Virtualization.Framework.

```
# Install Lume
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/trycua/cua/main/libs/lume/scripts/install.sh)"
# Pull & start a macOS VM
lume run macos-sequoia-vanilla:latest
```

**Get Started** | **FAQ** | **CLI Reference**

| Package | Description |
|---|---|
| cua-driver | Background computer-use agent for macOS, Windows, and Linux |
| cua-agent | AI agent framework for computer-use tasks |
| cua-sandbox | SDK for creating and controlling sandboxes |
| cua-computer-server | Driver for UI interactions and code execution in sandboxes |
| cua-bench | Benchmarks and RL environments for computer-use |
| lume | macOS/Linux VM management on Apple Silicon |
| lumier | Docker-compatible interface for Lume VMs |

- Documentation — Guides, examples, and API reference
- Blog — Tutorials, updates, and research
- Discord — Community support and discussions
- GitHub Issues — Bug reports and feature requests

We welcome contributions! See our Contributing Guidelines for details.

MIT License — see LICENSE for details.

Third-party components have their own licenses:

- Kasm (MIT)
- OmniParser (CC-BY-4.0)
- Optional
`cua-agent[omni]`

includes ultralytics (AGPL-3.0)

Apple, macOS, Ubuntu, Canonical, and Microsoft are trademarks of their respective owners. This project is not affiliated with or endorsed by these companies.