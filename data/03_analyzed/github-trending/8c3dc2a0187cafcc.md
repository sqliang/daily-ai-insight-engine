---
title: openai/codex
source: https://github.com/openai/codex
author: []
published: ''
created: '2026-08-23'
manifest_dates:
- '2026-08-23'
- '2026-08-24'
- '2026-08-25'
- '2026-08-26'
- '2026-08-27'
description: 'Lightweight coding agent that runs in your terminalCodex CLI is a coding
  agent from OpenAI that runs locally on your computer. If you want Codex in your
  code editor (VS Code, Cursor, Windsurf), install in your IDE. If you want the desktop
  app experience, run codex app or visit the Codex App page. If you are looking for
  the cloud-based agent from OpenAI, Codex Web, go to chatgpt.com/codex. Quickstart
  Installing and running Codex CLI Run the following on Mac or Linux to install Codex
  CLI: curl -fsSL https://chatgpt.com/codex/install.sh | sh Run the following on Windows
  to install Codex CLI: powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1
  | iex" The standalone installers download from https://releases.openai.com/codex
  by default and fall back to GitHub Releases if a metadata or asset download is unavailable.
  To force GitHub Releases, set CODEX_INSTALLER_USE_RELEASES_OPENAI_COM to false (0
  and no are also accepted): curl -fsSL https://chatgpt.com/codex/install.sh | CODEX_INSTALLER_USE_RELEASES_OPENAI_COM=false
  sh $env:CODEX_INSTALLER_USE_RELEASES_OPENAI_COM=''false''; irm https://chatgpt.com/codex/install.ps1
  | iex Codex CLI can also be installed via the following package managers: # Install
  using npm npm install -g @openai/codex # Install using Homebrew brew install --cask
  codex Then simply run codex to get started. You can also go to the latest GitHub
  Release and download the appropriate binary for your platform. Each GitHub Release
  contains many executables, but in practice, you likely want one of these: macOS
  Apple Silicon/arm64: codex-aarch64-apple-darwin.tar.gz x86_64 (older Mac hardware):
  codex-x86_64-apple-darwin.tar.gz Linux x86_64: codex-x86_64-unknown-linux-musl.tar.gz
  arm64: codex-aarch64-unknown-linux-musl.tar.gz Each archive contains a single entry
  with the platform baked into the name (e.g., codex-x86_64-unknown-linux-musl), so
  you likely want to rename it to codex after extracting it. Using Codex with your
  ChatGPT plan Run codex and select Sign in with ChatGPT. We recommend signing into
  your ChatGPT account to use Codex as part of your Plus, Pro, Business, Edu, or Enterprise
  plan. Learn more about what''s included in your ChatGPT plan. You can also use Codex
  with an API key, but this requires additional setup. Docs Codex Documentation Contributing
  Installing & building Open source fund This repository is licensed under the Apache-2.0
  License.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 8c3dc2a0187cafcc
source_type: community_discussion
tldr: OpenAI 在 GitHub 发布 Codex CLI，这是一个在本地运行的编程代理，支持 Mac、Linux 与 Windows，可通过安装脚本、npm、Homebrew
  或 GitHub Release 二进制安装，并支持 VS Code 等 IDE 集成。
objective_summary: OpenAI 在 GitHub 上发布 openai/codex 仓库，介绍其本地运行的编程代理 Codex CLI。该工具支持
  Mac、Linux 与 Windows 系统，用户可通过安装脚本、npm、Homebrew 或 GitHub Release 二进制文件安装，并可集成到 VS
  Code、Cursor、Windsurf 等编辑器。文章同时区分了云端代理 Codex Web（位于 chatgpt.com/codex）与桌面应用 Codex
  App，并建议使用 ChatGPT 账号登录以纳入 Plus、Pro、Business、Edu 或 Enterprise 订阅套餐。该仓库采用 Apache-2.0
  许可证。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - OpenAI
  technologies:
  - Codex CLI
  - Codex Web
  key_people: []
key_logic_flow:
- OpenAI 发布 Codex CLI，它是一个在本地计算机上运行的编程代理。
- 用户可通过 Mac/Linux 安装脚本、Windows PowerShell 命令、npm、Homebrew 或 GitHub Release 二进制文件安装
  Codex CLI。
- Codex CLI 支持 VS Code、Cursor、Windsurf 等代码编辑器的 IDE 集成，并可通过 codex app 获得桌面应用体验。
- OpenAI 还提供云端代理 Codex Web，位于 chatgpt.com/codex，与本地运行的版本相区别。
- 文章推荐使用 ChatGPT 账号登录以纳入 Plus、Pro、Business、Edu 或 Enterprise 订阅套餐，也可通过 API 密钥使用但需要额外配置。
- 该仓库采用 Apache-2.0 许可证发布。
object_mentions:
- object_type: project
  name: openai/codex
  canonical_name: openai/codex
  url: https://github.com/openai/codex
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Codex CLI 是 OpenAI 推出的本地运行的编程代理，可通过 curl 脚本、npm、Homebrew 或 GitHub Release 二进制文件安装。
  - Codex CLI 可在 Mac、Linux 与 Windows 上安装，并支持 VS Code、Cursor、Windsurf 等编辑器的 IDE 集成。
  article_id: 8c3dc2a0187cafcc
- object_type: product
  name: Codex Web
  canonical_name: Codex Web
  url: https://chatgpt.com/codex
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 文章提到 OpenAI 的云端代理 Codex Web 位于 chatgpt.com/codex，与本地运行的 Codex CLI 相区别。
  article_id: 8c3dc2a0187cafcc
- object_type: product
  name: Codex App
  canonical_name: Codex App
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 文章说明如需桌面应用体验，可运行 codex app 命令或访问 Codex App 页面获取。
  article_id: 8c3dc2a0187cafcc
extract_result: success
impact_score:
  score: 7.5
  reason: 评分依据：OpenAI 以 Apache-2.0 协议开源 Codex CLI 并主打本地运行，直接杀入 Claude Code 长期主导的本地编程代理细分市场，打破了此前编程代理以云端为主的产品形态；配合
    ChatGPT 订阅套餐捆绑而非纯 API 计量，对竞品的商业化模式构成实质性冲击。但 Codex 作为产品此前已以云端形态存在并多次公开曝光，本次属于正式开源与本地化发行，是重要产品发布而非范式转移，故给
    7.5 分。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: Apache-2.0 开源许可与本地运行带来的代码隐私可控性，以及能否在 IDE 生态上正面挑战 Claude Code
hype_assessment:
  level: low
  reason: 全文为客观的安装与使用文档（安装脚本、各平台二进制、包管理器、许可证、订阅方式），无任何“颠覆”“革命”类 PR 用语，也未对性能或能力做夸大承诺，判定为实打实的产品发布信息。
information_entropy: medium
domain_disruption:
  technical_innovation: 将编程代理从云端形态推向本地执行——代码与仓库上下文保留在开发者本机，仅通过 ChatGPT 订阅或 API Key
    调用后端模型；同时以 Apache-2.0 全面开源 CLI 层，使社区可审计、可二次分发并自由扩展 VS Code/Cursor/Windsurf 集成。本质创新在于把代理能力产品化为跨平台（Mac/Linux/Windows）的本地二进制工具链，并配套安装脚本、npm/Homebrew
    多分发渠道。
  business_model: 将编程代理的使用量捆绑进 ChatGPT Plus/Pro/Business/Edu/Enterprise 订阅套餐而非按 API
    令牌计量，重构了编程助手类产品的定价范式，降低了开发者的边际使用门槛；同时借 Apache-2.0 开源策略抢占开发者生态入口，对 Claude Code、GitHub
    Copilot 等订阅/按量竞品形成直接的价格与生态双重竞争。
engineering_complexity: production_ready
compound_value:
  score: 7.5
  reason: 投资逻辑链：(1) 编程代理正从'代码补全插件'向'自主编码智能体'演进，是开发者工具链中价值最集中的新入口，长期将承载大量软件生产流程，赛道本身具备明确长期复利属性；(2)
    OpenAI 以 Apache-2.0 开源 CLI 的姿态切入，表面让利、实则是把编程代理作为 ChatGPT 订阅（Plus/Pro/Business/Edu/Enterprise）的增值分发渠道，形成'模型能力+订阅粘性+IDE
    集成+本地/云端双形态'的组合打法，构建流量与数据飞轮——使用越频繁，模型迭代越快，订阅转化与留存越高；(3) 复利效应体现在开发者习惯与生态锁定：Codex
    一旦成为团队默认编码代理，迁移成本随时间递增，订阅收入呈累积性增长。风险变量：赛道竞争白热化（Claude Code、GitHub Copilot、Cursor、Devin
    均已重兵布局），CLI 本身开源意味着工具层无独占壁垒，差异化主要押注于模型层；若未来闭源与开源模型能力趋同，其护城河将被稀释。综合判断其具备成为开发者基础设施的强潜力，但需持续验证，故给予
    7.5 分而非更高。
value_capture_layer: agent_middleware
moat_impact: creates_new_moat
key_beneficiaries:
- OpenAI
- Microsoft (VS Code)
- NVIDIA
competitive_casualty:
- Claude Code (Anthropic)
- Devin (Cognition)
- Cursor / Windsurf
- GitHub Copilot
market_opportunities:
- 开发者可基于 Apache-2.0 开源的 Codex CLI 代码，研究其本地代理架构，衍生面向垂直场景（如测试生成、安全审计、文档维护）的编程代理插件与工作流
- 企业可将本地运行、云端推理的编程代理接入 CI/CD 与代码评审流程，降低审查人力成本，同时催生配套的代码合规、安全评估与数据出境咨询服务
- 关注本地编程代理生态的工具链机会，如 MCP 服务器、跨 IDE 协作插件、代理行为审计与沙箱执行产品
risk_matrix:
  regulatory: OpenAI 持续面临版权诉讼与欧盟 AI Act 等监管压力，Codex 生成代码可能卷入许可与归属争议；企业用于受监管行业时需评估专有代码上传云端的数据出境合规风险
  technological: Codex CLI 虽在本地运行，但模型推理仍依赖 OpenAI 云服务，断网或订阅受限时功能大幅退化；该领域迭代极快，可能被支持本地开源模型（Qwen
    Coder、DeepSeek 等）或新型代理架构替代
  competitive: 终端编程代理赛道竞争激烈，Anthropic Claude Code、GitHub Copilot、Cursor、Gemini CLI
    等对手林立，OpenAI 借助 ChatGPT 订阅捆绑建立壁垒，可能引发价格战与生态挤压
  ethical: 本地代理可自主执行代码，存在提示注入与供应链投毒放大风险；代码发送至云端推理引发企业专有代码隐私顾虑；AI 生成代码可能扩散低质量或带漏洞的代码
  additional:
  - 一键脚本安装（curl | sh / PowerShell 管道）存在供应链劫持风险，需校验来源与哈希
  - 代理被授予本机执行权限，误操作可能导致本地环境损坏或敏感数据泄露
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: deep_dive
object_insights:
- object_type: project
  name: openai/codex
  canonical_name: openai/codex
  url: https://github.com/openai/codex
  positioning: OpenAI 官方开源的本地运行编程代理 CLI，支持 Mac、Linux 与 Windows 多平台安装，并可集成主流代码编辑器。
  technical_signal: 采用 Apache-2.0 开源许可证，支持 curl 脚本、npm、Homebrew 及 GitHub Release 多通道安装，并原生支持
    VS Code、Cursor、Windsurf 等 IDE 集成。
  adoption_signal: 作为 OpenAI 官方发布的编程代理，可通过 npm、Homebrew 与安装脚本快速部署，降低开发者本地使用门槛。
  ecosystem_relevance: 与 ChatGPT Plus、Pro、Business、Edu 及 Enterprise 订阅体系打通，并纳入 OpenAI
    编程工具产品矩阵。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 作为 OpenAI 官方发布的本地编程代理，以 Apache-2.0 开源并覆盖 CLI、Web、桌面三种形态，其安装生态、IDE
    集成与订阅绑定策略将显著影响开发者采用格局。
  risk_notes:
  - 本地运行依赖用户机器算力与配置，实际编码效率与云端版本存在差异。
  - 项目仍处于快速迭代期，API 与 CLI 接口可能频繁变动，影响集成稳定性。
  score: 8.0
  article_ids:
  - 8c3dc2a0187cafcc
  evidence_snippets:
  - Codex CLI 是 OpenAI 推出的本地运行的编程代理，可通过 curl 脚本、npm、Homebrew 或 GitHub Release 二进制文件安装。
  - Codex CLI 可在 Mac、Linux 与 Windows 上安装，并支持 VS Code、Cursor、Windsurf 等编辑器的 IDE 集成。
- object_type: product
  name: Codex Web
  canonical_name: Codex Web
  url: https://chatgpt.com/codex
  positioning: OpenAI 提供的云端编程代理，位于 chatgpt.com/codex，与本地运行的 Codex CLI 形成互补交付形态。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 需要云端托管、免本地安装的开发者
  - 已订阅 ChatGPT Plus、Pro 等套餐的用户
  product_signal: 云端代理形态，用户可通过 ChatGPT 账号登录使用，并纳入 Plus、Pro、Business、Edu、Enterprise
    订阅体系。
  market_signal: 与本地 CLI 分层交付，覆盖不同开发者使用场景，反映 OpenAI 对编程代理的云端与本地双线布局。
  differentiation: 与本地运行、需自行安装的 Codex CLI 相区别，Codex Web 提供免配置的云端访问方式，交付形态完全不同。
  watch_reason: 作为 OpenAI 云端编程代理的官方入口，其与本地 CLI 的协同演进、能力边界及订阅套餐绑定策略，将直接反映 OpenAI 编程代理产品矩阵的走向。
  risk_notes:
  - 文章仅提及 Codex Web 的存在，未披露其功能细节、性能表现与可用区域等关键信息。
  score: 5.0
  article_ids:
  - 8c3dc2a0187cafcc
  evidence_snippets:
  - 文章提到 OpenAI 的云端代理 Codex Web 位于 chatgpt.com/codex，与本地运行的 Codex CLI 相区别。
- object_type: product
  name: Codex App
  canonical_name: Codex App
  url: null
  positioning: OpenAI 提供的桌面应用形态编程代理，可通过 codex app 命令或专属页面获得桌面端使用体验。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 偏好桌面原生应用体验的开发者
  product_signal: 提供桌面应用体验，与 CLI 及 Web 版本共同构成 Codex 的多端交付形态。
  market_signal: null
  differentiation: 区别于命令行与云端形态，Codex App 以桌面应用形式交付，面向偏好图形界面操作的开发者。
  watch_reason: Codex App 作为 OpenAI 编程代理的桌面形态，其功能完整度、发布节奏以及与 CLI、Web 版本的差异定位，反映了产品矩阵的多端布局策略，值得持续跟踪。
  risk_notes:
  - 文章仅简要提及桌面应用，未说明其支持平台、功能范围与正式发布时间。
  score: 4.0
  article_ids:
  - 8c3dc2a0187cafcc
  evidence_snippets:
  - 文章说明如需桌面应用体验，可运行 codex app 命令或访问 Codex App 页面获取。
---

**Codex CLI** is a coding agent from OpenAI that runs locally on your computer.

If you want Codex in your code editor (VS Code, Cursor, Windsurf), install in your IDE.

If you want the desktop app experience, run

`codex app`

or visit the Codex App page.
If you are looking for the

*cloud-based agent*from OpenAI,

**Codex Web**, go to chatgpt.com/codex.

Run the following on Mac or Linux to install Codex CLI:

`curl -fsSL https://chatgpt.com/codex/install.sh | sh`

Run the following on Windows to install Codex CLI:

`powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"`

The standalone installers download from `https://releases.openai.com/codex`

by default and fall back to GitHub Releases if a metadata or asset download is unavailable. To force GitHub Releases, set `CODEX_INSTALLER_USE_RELEASES_OPENAI_COM`

to `false`

(`0`

and `no`

are also accepted):

`curl -fsSL https://chatgpt.com/codex/install.sh | CODEX_INSTALLER_USE_RELEASES_OPENAI_COM=false sh`

`$env:CODEX_INSTALLER_USE_RELEASES_OPENAI_COM='false'; irm https://chatgpt.com/codex/install.ps1 | iex`

Codex CLI can also be installed via the following package managers:

```
# Install using npm
npm install -g @openai/codex
```

```
# Install using Homebrew
brew install --cask codex
```

Then simply run `codex`

to get started.

## You can also go to the latest GitHub Release and download the appropriate binary for your platform.

Each GitHub Release contains many executables, but in practice, you likely want one of these:

- macOS
- Apple Silicon/arm64:
`codex-aarch64-apple-darwin.tar.gz`

- x86_64 (older Mac hardware):
`codex-x86_64-apple-darwin.tar.gz`


- Apple Silicon/arm64:
- Linux
- x86_64:
`codex-x86_64-unknown-linux-musl.tar.gz`

- arm64:
`codex-aarch64-unknown-linux-musl.tar.gz`


- x86_64:

Each archive contains a single entry with the platform baked into the name (e.g., `codex-x86_64-unknown-linux-musl`

), so you likely want to rename it to `codex`

after extracting it.

Run `codex`

and select **Sign in with ChatGPT**. We recommend signing into your ChatGPT account to use Codex as part of your Plus, Pro, Business, Edu, or Enterprise plan. Learn more about what's included in your ChatGPT plan.

You can also use Codex with an API key, but this requires additional setup.

This repository is licensed under the Apache-2.0 License.