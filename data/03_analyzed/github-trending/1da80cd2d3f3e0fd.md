---
title: NVIDIA-NeMo/Switchyard
source: https://github.com/NVIDIA-NeMo/Switchyard
author: []
published: ''
created: '2026-08-13'
manifest_dates:
- '2026-08-13'
- '2026-08-14'
description: 'Switchyard Switchyard is a Rust proxy and library for LLM traffic. It
  routes requests across providers, translates between OpenAI and Anthropic APIs,
  records operational metrics, and provides typed, composable routing algorithms.
  Why Switchyard? Point a coding agent such as Claude Code or Codex at an open-source
  model. Switchyard translates between the OpenAI Chat, Anthropic Messages, and OpenAI
  Responses formats, so the agent keeps speaking its native API while the request
  is served by vLLM, NVIDIA NIM, Ollama, or any OpenAI-compatible endpoint. The same
  proxy can spread traffic across several models for A/B benchmarking, apply signal-driven
  stage routing, or run a custom algorithm you write yourself. Features Protocol Translation:
  convert between OpenAI Chat, Anthropic Messages, and OpenAI Responses formats Multi-Backend
  Routing: random routing, LLM-as-classifier routing, signal-driven stage-router,
  or your own algorithm Operational Metrics: Prometheus metrics cover requests, errors,
  latency, tokens, and routing overhead Maturity Switchyard is pre-alpha software
  that is evolving rapidly. The API and algorithms are expected to change significantly
  before we reach v1.0. Warning Experimental software. Not for production use. Quick
  Start Choose the launcher path to run Claude Code, Codex CLI, or OpenClaw through
  Switchyard. Choose the server path to run Switchyard as a standalone proxy. Choose
  the library path to embed routing in your own Rust application. Launcher Path Install
  uv if it is not already available, then install the published Switchyard tool: curl
  -LsSf https://astral.sh/uv/install.sh | sh source "$HOME/.local/bin/env" uv tool
  install --python 3.10 "nemo-switchyard[cli]" The coding agent you launch must also
  be installed and on your PATH. This does not install the standalone switchyard-server
  binary; use the Server Path for that. Set an OpenRouter key and launch against the
  packaged deployment: export OPENROUTER_API_KEY="your-openrouter-key" # pragma: allowlist
  secret switchyard launch claude --model switchyard switchyard launch codex --model
  switchyard switchyard launch openclaw --model switchyard To use your own native
  TOML deployment, pass its route ID and configuration: switchyard launch claude --model
  my-route --config routes.toml Server Path Use this path to install and run the standalone
  Rust proxy. Install Rust with Cargo, then install the published binary: cargo install
  --locked switchyard-server switchyard-server --help Cargo builds the release binary
  and installs it into ~/.cargo/bin by default. Create routes.toml using the Getting
  Started guide, then validate it and start the server: export OPENROUTER_API_KEY="your-openrouter-key"
  # pragma: allowlist secret switchyard-server --config routes.toml --dry-run switchyard-server
  --config routes.toml --host 127.0.0.1 --port 4000 Verify the proxy in another terminal:
  curl http://localhost:4000/health For a complete configuration and a test request,
  follow Getting Started. Library Path switchyard-libsy embeds the routing algorithms
  in your own Rust application. It never calls a model itself: an algorithm decides
  which target to use and hands every model call back to you, so it drops into an
  existing proxy, gateway, or agent runtime without owning an HTTP stack. Pair it
  with switchyard-llm-client when you want the calls made for you. [dependencies]
  switchyard-libsy = { git = "https://github.com/NVIDIA-NeMo/Switchyard.git" } switchyard-protocol
  = { git = "https://github.com/NVIDIA-NeMo/Switchyard.git" } See Getting Started
  for setup and the algorithm list, or the switchyard-libsy crate docs. Routing Strategies
  Strategy Use it when Route type LLM Classifier Request content should decide whether
  a turn needs the weak or strong tier. llm_classifier Stage Router Signals already
  in the conversation, such as tool results and errors, should route most turns without
  an extra model call. stage_router Escalation Router Every turn runs on the weak
  tier first, and a judge reads that answer to decide whether to send the same request
  to the strong tier. llm_classifier with mode = "escalation" Random You need a fixed
  traffic split for A/B tests, baselines, or cost experiments. random A passthrough
  route registers one target under one model ID with no routing decision. See the
  Routing Overview for the common route shape and self-hosted targets. Architecture
  flowchart LR clients["Clients"] switchyard["Switchyard<br/>routing · translation
  · fallback"] backends["Model backends"] clients -->|"OpenAI / Anthropic API"| switchyard
  switchyard -->|"provider-native format"| backends Clients keep their native OpenAI
  or Anthropic API format. Switchyard picks a configured backend, forwards the request
  in that backend''s own format, and translates the response back into the shape the
  client expects. The server accepts OpenAI Chat Completions, OpenAI Responses, and
  Anthropic Messages. Each configured LLM client selects one upstream format. Documentation
  Getting Started: complete launcher and standalone server walkthroughs Core Concepts:
  LLM clients, targets, routes, model IDs, and routing algorithms Routing Overview:
  choose and configure a routing algorithm switchyard-server: server configuration,
  routing algorithms, and metrics switchyard-libsy: embed routing algorithms in a
  Rust application switchyard-protocol: provider-neutral request, response, and streaming
  types switchyard-translation: request, response, and stream translation Community
  Issues: GitHub Issues Code of Conduct: Code of Conduct License Apache 2.0 License.
  Copyright NVIDIA Corporation.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 1da80cd2d3f3e0fd
source_type: community_discussion
tldr: NVIDIA NeMo 开源了 Switchyard：一个用 Rust 编写的 LLM 流量代理与库，可在 OpenAI/Anthropic API 与
  vLLM、NVIDIA NIM、Ollama 等后端之间做协议转换与多后端路由，目前为 pre-alpha 实验软件。
objective_summary: NVIDIA 的 NeMo 团队在 GitHub 上发布了名为 Switchyard 的 Rust 项目，这是一个面向大语言模型流量的代理与库。它通过转换
  OpenAI Chat、Anthropic Messages 和 OpenAI Responses 协议，把来自 Claude Code、Codex CLI 等编码代理的请求路由到
  vLLM、NVIDIA NIM、Ollama 等后端，并支持随机、LLM 分类器、信号驱动阶段路由等算法以及 Prometheus 运维指标。项目目前处于 pre-alpha
  阶段，API 与算法在 v1.0 前预计会有较大变化，不建议用于生产环境。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - NVIDIA
  technologies:
  - Rust
  - LLM proxy
  - OpenAI API
  - Anthropic Messages API
  - OpenAI Responses API
  - vLLM
  - NVIDIA NIM
  - Ollama
  - Prometheus
  - TOML
  key_people: []
key_logic_flow:
- Switchyard 是用 Rust 编写的 LLM 流量代理与库，核心能力包括协议转换、多后端路由和运维指标采集。
- 在 Launcher 路径中，用户安装 nemo-switchyard CLI 后，可将 Claude Code、Codex CLI、OpenClaw 等编码代理的
  OpenAI/Anthropic 格式请求转接至 OpenRouter 或本地 TOML 配置的后端。
- 在 Server 路径中，用户通过 cargo 安装 switchyard-server，用 routes.toml 配置并启动独立代理服务，对外暴露 /health
  等端点。
- 在 Library 路径中，switchyard-libsy 把路由算法嵌入用户自己的 Rust 应用，switchyard-protocol 提供供应商中立的请求/响应/流类型，可与
  switchyard-llm-client 配对使用。
- 项目支持随机路由、LLM 分类器、阶段路由、升级路由等策略，也支持 passthrough 直连单个目标。
- Switchyard 当前为 pre-alpha 软件，API 与算法在达到 v1.0 前预计会大幅变化，不适用于生产环境。
object_mentions:
- object_type: project
  name: NVIDIA-NeMo/Switchyard
  canonical_name: Switchyard
  url: https://github.com/NVIDIA-NeMo/Switchyard
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 文章指出，Switchyard 是一个面向大模型流量的 Rust 代理与库，可在不同供应商之间转发请求并完成 OpenAI 与 Anthropic API
    的协议转换。
  - 它记录 Prometheus 运维指标，并提供类型化、可组合的路由算法。
  - 项目采用 Apache 2.0 许可证，版权归 NVIDIA Corporation 所有。
  article_id: 1da80cd2d3f3e0fd
- object_type: product
  name: nemo-switchyard
  canonical_name: nemo-switchyard
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 文章介绍 Launcher 路径时指出，可通过 uv tool install --python 3.10 'nemo-switchyard[cli]' 安装已发布的
    Switchyard 命令行工具。
  - 安装后可用 switchyard launch claude --model switchyard 等命令把编码代理的流量导入 Switchyard。
  article_id: 1da80cd2d3f3e0fd
- object_type: product
  name: switchyard-server
  canonical_name: switchyard-server
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Server 路径使用 cargo install --locked switchyard-server 安装独立 Rust 代理，并用 switchyard-server
    --config routes.toml 启动服务。
  - 启动后可通过 curl http://localhost:4000/health 验证代理是否正常运行。
  article_id: 1da80cd2d3f3e0fd
- object_type: project
  name: switchyard-libsy
  canonical_name: switchyard-libsy
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - Library 路径中，switchyard-libsy 把路由算法嵌入用户自己的 Rust 应用，本身不调用模型，只决定目标并把模型调用交回调用方。
  - 用户可在 Cargo 依赖中通过 GitHub 仓库地址引入 switchyard-libsy。
  article_id: 1da80cd2d3f3e0fd
- object_type: project
  name: switchyard-protocol
  canonical_name: switchyard-protocol
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - switchyard-protocol 提供与供应商无关的请求、响应和流式类型，支撑在不同后端之间完成格式转换。
  - 它可以与 switchyard-libsy 一起通过 GitHub 仓库地址引入到 Rust 项目中。
  article_id: 1da80cd2d3f3e0fd
- object_type: project
  name: switchyard-llm-client
  canonical_name: switchyard-llm-client
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - 当需要由库自动发起模型调用时，用户可以将 switchyard-libsy 与 switchyard-llm-client 配对使用。
  - 这样既能复用 Switchyard 的路由算法，又不必自己实现上游模型的 HTTP 调用。
  article_id: 1da80cd2d3f3e0fd
extract_result: success
impact_score:
  score: 6.5
  reason: NVIDIA NeMo 在 LLM 网关/代理赛道开源了一个 Rust 实现的协议转换与路由工具，直接连接 Claude Code、Codex
    CLI 等主流 coding agent 与 vLLM、NIM、Ollama 等后端。考虑到 NVIDIA 的硬件-软件生态号召力、NeMo 品牌以及当前
    LLM 路由市场的热度，这是一个重要产品发布，可能改变局部竞争格局。但它仍处于 pre-alpha，明确不建议生产使用，因此尚未达到 ChatGPT 或 Transformer
    级别的范式转移。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: Rust 高性能实现与 OpenAI/Anthropic/vLLM 多后端互操作性，以及 pre-alpha 阶段的稳定性和 API
    演进风险
hype_assessment:
  level: low
  reason: 文章没有使用“颠覆”“革命性”等 PR 滥用词汇，反而反复强调 pre-alpha、experimental、not for production，并给出了具体的功能清单、安装命令和路由算法对比。虽然
    NVIDIA 品牌本身会带来关注，但信息披露较为克制，干货多于包装。
information_entropy: high
domain_disruption:
  technical_innovation: 以 Rust 提供 LLM 流量的协议转换（OpenAI Chat、Anthropic Messages、OpenAI
    Responses）与多后端路由，封装为 CLI 启动器、独立 server 和可嵌入库三种形态；内置随机、LLM-as-classifier、信号驱动阶段路由、升级路由等算法，并提供
    Prometheus 运维指标。
  business_model: 巩固 NVIDIA NeMo/NIM 在开源推理后端和 AI agent 工具链中的入口地位，可能对 LiteLLM 等 LLM
    网关/代理产品形成竞争压力；通过 Rust 高性能定位吸引需要自建网关的企业用户，但 pre-alpha 阶段短期内难以形成直接商业变现。
engineering_complexity: prototype
compound_value:
  score: 5.5
  reason: Switchyard 切中 LLM 应用落地的真实痛点：OpenAI / Anthropic / OpenAI Responses 协议并存，企业需要在自托管（vLLM/NIM/Ollama）与商业
    API 之间灵活切换。协议转换 + 多后端路由 + 可嵌入 Rust 库的组合，使其具备成为 Agent 与模型 serving 之间基础设施的潜力，长期复利来自生态位卡位。但当前为
    pre-alpha，API 与算法在 v1.0 前会大幅变动，商业化路径也不清晰（Apache 2.0 开源，大概率不直接收费，而是为 NVIDIA NIM
    / GPU 销售导流）。同类竞品已有 LiteLLM、OpenRouter、Kong 等，且协议层转换本身壁垒不高，用户迁移成本低。因此不能给高分；5.5
    分反映‘赛道方向正确、巨头背书加分、但尚处早期且护城河未验证’的投资判断。
value_capture_layer: agent_middleware
moat_impact: democratizes_access
key_beneficiaries:
- NVIDIA
- NVIDIA NIM
- vLLM
- Ollama
- OpenRouter
competitive_casualty:
- LiteLLM 商业版
- 闭源 LLM 网关 / API 代理初创公司
- 依赖 API 锁定生态的单一模型供应商
market_opportunities:
- 企业级 LLM 网关厂商可基于 Switchyard 封装私有化多模型路由产品，面向金融、医疗等对数据主权和成本敏感的客户提供统一接入、协议转换与可观测能力。
- AI Agent 与编码工具团队可借鉴其阶段路由与协议翻译设计，将 Claude Code、Codex CLI 等客户端请求转接到 vLLM、NVIDIA NIM
  或 Ollama 后端，显著降低 Token 成本并增强数据可控性。
- 基础设施开发者应关注 Rust 在 LLM 代理与高性能路由中的工程实践，把多后端调度、A/B 评测和 Prometheus 指标作为云原生 AI 架构的技能补充点。
risk_matrix:
  regulatory: 无
  technological: 项目处于 pre-alpha 阶段，API 与路由算法在 v1.0 前可能大幅调整，早期集成存在迁移成本；协议转换层需持续跟进 OpenAI/Anthropic
    API 的更新与兼容。
  competitive: LLM 路由/代理赛道已有 LiteLLM、Kong、Envoy Gateway、Cloudflare AI Gateway 等成熟方案，Switchyard
    虽有 NVIDIA 生态与 Rust 性能优势，但市场教育和生态份额面临挤压。
  ethical: 代理层会转发用户请求与模型响应，若部署不当可能导致敏感数据经过不可控组件；路由策略设计不当时也可能放大模型偏见、错误输出或被用于规避内容安全过滤。
  additional:
  - pre-alpha 软件不建议用于生产环境，存在稳定性、文档完善度与社区支持不足的风险。
  - NVIDIA 品牌背书虽带来关注度，但也可能使项目过度依赖 NVIDIA 生态（如 NIM、Triton），削弱其中立性与跨厂商兼容性。
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: monitor
object_insights:
- object_type: project
  name: NVIDIA-NeMo/Switchyard
  canonical_name: Switchyard
  url: https://github.com/NVIDIA-NeMo/Switchyard
  positioning: NVIDIA NeMo 团队开源的 Rust LLM 流量代理与库，专注于多供应商协议转换、智能路由与运维指标采集。
  technical_signal: 项目用 Rust 实现 OpenAI Chat、Anthropic Messages 与 OpenAI Responses
    三种协议互转，并内置随机、LLM 分类器、信号驱动阶段路由等算法。
  adoption_signal: 当前处于 pre-alpha 阶段，API 与算法在 v1.0 前预计大幅变化，官方明确不建议用于生产环境。
  ecosystem_relevance: 可桥接 Claude Code、Codex CLI 等编码代理与 vLLM、NVIDIA NIM、Ollama 等后端，补全开源模型
    serving 生态中的协议兼容层。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: NVIDIA 背书加上 Rust 高性能实现与多协议翻译能力，使其在 AI 代理基础设施赛道具备长期跟踪价值，但需关注 v1.0 前的稳定性演进。
  risk_notes:
  - 项目为 pre-alpha 软件，API 与路由算法在 v1.0 前可能发生大幅变化。
  - 官方文档已标注实验性质，不建议将 Switchyard 用于生产环境。
  score: 8.0
  article_ids:
  - 1da80cd2d3f3e0fd
  evidence_snippets:
  - 文章指出，Switchyard 是一个面向大模型流量的 Rust 代理与库，可在不同供应商之间转发请求并完成 OpenAI 与 Anthropic API
    的协议转换。
  - 它记录 Prometheus 运维指标，并提供类型化、可组合的路由算法，支持随机、LLM 分类器、信号驱动阶段路由等多种策略。
  - 项目采用 Apache 2.0 许可证，版权归 NVIDIA Corporation 所有，目前为 pre-alpha 实验软件，不建议用于生产环境。
- object_type: product
  name: nemo-switchyard
  canonical_name: nemo-switchyard
  url: null
  positioning: Switchyard 的 Python CLI 启动器，用于将 Claude Code、Codex CLI、OpenClaw 等编码代理的流量导入
    Switchyard 路由层。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - Claude Code 用户
  - Codex CLI 用户
  - OpenClaw 用户
  - 希望用开源模型替代商业 API 的开发者
  product_signal: 通过 uv tool install 一键安装，支持 launch claude/codex/openclaw 等子命令，并可用
    --config routes.toml 指向自定义路由配置。
  market_signal: 作为已发布的 PyPI 工具降低上手门槛，瞄准希望用开源或第三方模型替代商业 API 的编码代理用户。
  differentiation: 以命令行封装方式让现有编码代理无需改造即可使用 Switchyard 的多后端路由与协议转换能力。
  watch_reason: CLI 形态是 Switchyard 生态触达终端用户的关键入口，其安装体验、命令覆盖度与路由配置灵活性将决定项目早期采用曲线。
  risk_notes:
  - 依赖 uv 与 Python 3.10 环境，且未随工具安装 switchyard-server 二进制。
  - 作为 pre-alpha 项目的一部分，CLI 稳定性与后端兼容性存在不确定性。
  score: 7.0
  article_ids:
  - 1da80cd2d3f3e0fd
  evidence_snippets:
  - 文章介绍 Launcher 路径时指出，可通过 uv tool install --python 3.10 'nemo-switchyard[cli]' 安装已发布的
    Switchyard 命令行工具，用于启动编码代理。
  - 安装后可用 switchyard launch claude --model switchyard 等命令，把 Claude Code、Codex CLI、OpenClaw
    等编码代理的流量导入 Switchyard，实现多后端路由与协议转换。
- object_type: product
  name: switchyard-server
  canonical_name: switchyard-server
  url: null
  positioning: Switchyard 的独立 Rust 代理服务，对外暴露 HTTP 端点并承担协议转换与多后端路由的核心职责。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 需要自托管 LLM 网关的团队
  - 使用 vLLM/NIM/Ollama 后端的运维人员
  - Rust 生态开发者
  product_signal: 通过 cargo install --locked 安装，使用 routes.toml 配置路由，提供 --dry-run 校验与
    /health 健康检查端点。
  market_signal: 面向需要自托管 LLM 代理网关的团队，可与 OpenRouter 或本地 vLLM、NVIDIA NIM、Ollama 等后端集成。
  differentiation: 以纯 Rust 二进制提供高性能独立代理，适合嵌入现有 serving 架构作为网关层，且不会强制接管 HTTP 栈。
  watch_reason: 作为 Switchyard 的服务端核心，其路由策略丰富度、运维指标能力与部署灵活性将决定项目在 enterprise serving
    场景中的落地潜力。
  risk_notes:
  - 需要 Rust/Cargo 环境，构建与部署门槛高于 Python CLI 工具，对非 Rust 团队不够友好。
  - pre-alpha 阶段，routes.toml 配置格式与服务端 API 可能发生变化。
  score: 7.0
  article_ids:
  - 1da80cd2d3f3e0fd
  evidence_snippets:
  - Server 路径使用 cargo install --locked switchyard-server 安装独立 Rust 代理，并用 switchyard-server
    --config routes.toml 启动服务，对外提供 LLM 流量路由与协议转换能力。
  - 启动后可通过 curl http://localhost:4000/health 验证代理是否正常运行，服务对外暴露 OpenAI/Anthropic 兼容接口并完成协议转换。
---

Switchyard is a Rust proxy and library for LLM traffic. It routes requests across providers, translates between OpenAI and Anthropic APIs, records operational metrics, and provides typed, composable routing algorithms.

**Why Switchyard?** Point a coding agent such as Claude Code or Codex at an
open-source model. Switchyard translates between the OpenAI Chat, Anthropic
Messages, and OpenAI Responses formats, so the agent keeps speaking its native
API while the request is served by vLLM, NVIDIA NIM, Ollama, or any
OpenAI-compatible endpoint. The same proxy can spread traffic across several
models for A/B benchmarking, apply signal-driven stage routing, or run a custom
algorithm you write yourself.

**Protocol Translation**: convert between OpenAI Chat, Anthropic Messages, and OpenAI Responses formats**Multi-Backend Routing**: random routing, LLM-as-classifier routing, signal-driven stage-router, or your own algorithm**Operational Metrics**: Prometheus metrics cover requests, errors, latency, tokens, and routing overhead

Switchyard is pre-alpha software that is evolving rapidly. The API and algorithms are expected to change significantly before we reach v1.0.

Warning

Experimental software. Not for production use.

Choose the launcher path to run Claude Code, Codex CLI, or OpenClaw through Switchyard. Choose the server path to run Switchyard as a standalone proxy. Choose the library path to embed routing in your own Rust application.

Install `uv`

if it is
not already available, then install the published Switchyard tool:

```
curl -LsSf https://astral.sh/uv/install.sh | sh
source "$HOME/.local/bin/env"
uv tool install --python 3.10 "nemo-switchyard[cli]"
```

The coding agent you launch must also be installed and on your `PATH`

. This does
not install the standalone `switchyard-server`

binary; use the Server Path for
that.

Set an OpenRouter key and launch against the packaged deployment:

```
export OPENROUTER_API_KEY="your-openrouter-key" # pragma: allowlist secret
switchyard launch claude --model switchyard
switchyard launch codex --model switchyard
switchyard launch openclaw --model switchyard
```

To use your own native TOML deployment, pass its route ID and configuration:

`switchyard launch claude --model my-route --config routes.toml`

Use this path to install and run the standalone Rust proxy. Install Rust with Cargo, then install the published binary:

```
cargo install --locked switchyard-server
switchyard-server --help
```

Cargo builds the release binary and installs it into `~/.cargo/bin`

by default.

Create `routes.toml`

using the
Getting Started guide, then validate it
and start the server:

```
export OPENROUTER_API_KEY="your-openrouter-key" # pragma: allowlist secret
switchyard-server --config routes.toml --dry-run
switchyard-server --config routes.toml --host 127.0.0.1 --port 4000
```

Verify the proxy in another terminal:

`curl http://localhost:4000/health`

For a complete configuration and a test request, follow Getting Started.

`switchyard-libsy`

embeds the routing algorithms in your own Rust application.
It never calls a model itself: an algorithm decides which target to use and
hands every model call back to you, so it drops into an existing proxy, gateway,
or agent runtime without owning an HTTP stack. Pair it with
`switchyard-llm-client`

when you want the calls made for you.

```
[dependencies]
switchyard-libsy = { git = "https://github.com/NVIDIA-NeMo/Switchyard.git" }
switchyard-protocol = { git = "https://github.com/NVIDIA-NeMo/Switchyard.git" }
```

See Getting Started for setup and the
algorithm list, or the `switchyard-libsy`

crate docs.

| Strategy | Use it when | Route `type` |
|---|---|---|
| LLM Classifier | Request content should decide whether a turn needs the weak or strong tier. | `llm_classifier` |
| Stage Router | Signals already in the conversation, such as tool results and errors, should route most turns without an extra model call. | `stage_router` |
| Escalation Router | Every turn runs on the weak tier first, and a judge reads that answer to decide whether to send the same request to the strong tier. | `llm_classifier` with `mode = "escalation"` |
| Random | You need a fixed traffic split for A/B tests, baselines, or cost experiments. | `random` |

A `passthrough`

route registers one target under one model ID with no routing
decision. See the Routing Overview for
the common route shape and self-hosted targets.

```
flowchart LR
clients["Clients"]
switchyard["Switchyard<br/>routing · translation · fallback"]
backends["Model backends"]
clients -->|"OpenAI / Anthropic API"| switchyard
switchyard -->|"provider-native format"| backends
```

Clients keep their native OpenAI or Anthropic API format. Switchyard picks a configured backend, forwards the request in that backend's own format, and translates the response back into the shape the client expects. The server accepts OpenAI Chat Completions, OpenAI Responses, and Anthropic Messages. Each configured LLM client selects one upstream format.

**Getting Started**: complete launcher and standalone server walkthroughs**Core Concepts**: LLM clients, targets, routes, model IDs, and routing algorithms**Routing Overview**: choose and configure a routing algorithm: server configuration, routing algorithms, and metrics`switchyard-server`

: embed routing algorithms in a Rust application`switchyard-libsy`

: provider-neutral request, response, and streaming types`switchyard-protocol`

: request, response, and stream translation`switchyard-translation`


**Issues**: GitHub Issues**Code of Conduct**: Code of Conduct

Apache 2.0 License. Copyright NVIDIA Corporation.