---
title: vitali87/code-graph-rag
source: https://github.com/vitali87/code-graph-rag
author: []
published: ''
created: '2026-08-10'
manifest_dates:
- '2026-08-10'
- '2026-08-11'
- '2026-08-12'
description: 'The ultimate RAG for your monorepo. Query, understand, and edit multi-language
  codebases with the power of AI and knowledge graphs / tags, so we use a single light-mode
  . Restore the theme-aware block below when the GitHub account is reinstated: -->
  --> --> --> Code-Graph-RAG Code-Graph-RAG parses a multi-language codebase with
  Tree-sitter, builds a knowledge graph of its structure in Memgraph, and lets you
  query, edit, and optimise that code in plain English. It works across a monorepo
  of mixed languages under one unified graph schema. Latest News 🔥 Release Automation:
  NEWS.md and the README''s "Latest News" section now refresh automatically on every
  release, keeping the changelog current without hand edits. Ruby Support: Ruby joins
  the graph through a new pluggable ast-grep tier that adds a language from a single
  YAML pattern file, emitting Module, Function, and Class nodes plus import edges
  without a hand-written parser. Structural Search & Replace: Find and rewrite code
  by AST pattern with ast-grep, exposed as agent tools so you can match and transform
  structure across the whole codebase instead of relying on text or regex. See NEWS.md
  for the full history. What It Does Point Code-Graph-RAG at a repository and it reads
  every source file, extracts functions, classes, methods, modules, and the relationships
  between them, and stores the result as an interconnected graph. Once the graph exists
  you can: Ask questions about the codebase in natural language and get answers grounded
  in the real structure. Retrieve the actual source of any function, class, or method
  by name or by intent. Edit code through the agent with AST-based surgical patching
  and a diff preview before anything changes. Optimise code against language best
  practices or your own coding standards. Find dead code by walking call and reference
  edges from entry points. Search and rewrite structurally by AST pattern with ast-grep.
  How It Works The system has two components: Multi-language parser. A Tree-sitter
  based parser reads the codebase and ingests functions, classes, methods, modules,
  and their relationships into Memgraph under a single language-agnostic schema. RAG
  system (codebase_rag/). An interactive CLI that turns natural language into Cypher
  queries, retrieves matching code, and drives AI-powered editing and optimisation.
  Source Code -> Tree-sitter Parser -> AST Analysis -> Memgraph Knowledge Graph |
  User Query -> AI Model (Cypher Gen) -> Cypher Query -> Graph Results -> Response
  See the Architecture Overview and Graph Schema for the full picture. Supported Languages
  Python, TypeScript, TSX, JavaScript, Rust, Go, Java, C, C++, C#, PHP, Lua, and Dart
  are fully supported. Scala is in development, and Ruby has structural support (modules,
  functions, classes, and imports) through the pluggable ast-grep tier. See the Language
  Support matrix for per-language capabilities. Installation cgr is published to PyPI.
  Install it system-wide with the treesitter-full (all languages) and semantic (vector
  search) extras: # with uv (recommended) uv tool install "code-graph-rag[treesitter-full,semantic]"
  # or with pipx pipx install "code-graph-rag[treesitter-full,semantic]" You also
  need Docker (for Memgraph), cmake, and ripgrep. Full prerequisites, source installs,
  and environment setup are in the Installation guide. Quick Start # Start the packaged
  Memgraph + Qdrant stack (no compose file needed) cgr daemon up # Parse a repository
  into the graph, then query it cgr start --repo-path /path/to/repo --update-graph
  cgr start --repo-path /path/to/repo Repeat the first command for each repository
  you want indexed; the graph is shared, and syncing one project leaves the others
  alone. To start over from an empty graph, add --clean — it deletes every project
  in the shared graph, not just this one, and asks for confirmation first when other
  projects would be destroyed. The Quick Start guide walks through parsing, querying,
  and exporting in five minutes. MCP Server Code-Graph-RAG runs as an MCP server so
  Claude Code and other MCP clients can query and edit your codebase directly. See
  the MCP Server guide for setup. Documentation Getting Started Installation Quick
  Start Configuration User Guide CLI Reference Interactive Querying Code Optimisation
  Dead Code Detection Graph Export Real-Time Updates MCP Server Architecture Overview
  Graph Schema Language Support Data-Flow Edges Python SDK Overview Graph Loader Cypher
  Generator Semantic Search Advanced Adding Languages Ignore Patterns Building Binaries
  Troubleshooting Enterprise Services Code-Graph-RAG is open source and free to use.
  For organisations that need more, we offer fully managed cloud-hosted solutions
  and on-premise deployments: Cloud-Hosted Deployment: Managed cloud infrastructure
  for both the graph database and the AI agent connection. Zero infrastructure overhead,
  so we handle scaling, updates, and availability while your team focuses on building.
  On-Premise & Air-Gapped Deployment: Deploy Code-Graph-RAG entirely within your own
  environment, including air-gapped networks. Full data sovereignty for regulated
  industries and security-sensitive organisations. We also offer custom development,
  integration consulting, technical support contracts, and team training. View plans
  & pricing at code-graph-rag.com Contributing Please see CONTRIBUTING.md for contribution
  guidelines. Good first PRs come from the TODO issues. Support For issues or questions,
  check the Troubleshooting guide first, then open an issue. License MIT. See LICENSE.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: ad4fec82cec4fb39
source_type: community_discussion
tldr: Code-Graph-RAG 是一个开源代码库智能工具，用 Tree-sitter 解析多语言代码并存入 Memgraph 知识图谱，支持用自然语言查询、编辑和优化代码，还可作为
  MCP 服务器供 Claude Code 调用。
objective_summary: GitHub 用户 vitali87 开发了 Code-Graph-RAG，这是一款基于 Tree-sitter 的多语言代码库解析与
  RAG 工具。它把函数、类、方法、模块及其关系以统一图模式存入 Memgraph，用户通过 cgr 命令行用自然语言生成 Cypher 查询，实现代码检索、AST
  级结构化编辑、优化和死代码检测。工具完整支持 Python、TypeScript、JavaScript、Rust、Go、Java 等 13 种语言，以 MIT
  协议开源并发布到 PyPI，同时提供云托管与本地私有化部署方案。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - Memgraph
  - Qdrant
  technologies:
  - Tree-sitter
  - RAG
  - MCP
  - Cypher
  - ast-grep
  - Memgraph
  - Qdrant
  key_people:
  - vitali87
key_logic_flow:
- Code-Graph-RAG 用 Tree-sitter 解析多语言代码库，将函数、类、方法、模块及其关系以统一语言无关的图模式存入 Memgraph 知识图谱。
- 系统由多语言解析器和 RAG 系统两部分组成，RAG 系统提供交互式 CLI，把自然语言转换为 Cypher 查询并返回图匹配的代码结果。
- 工具完整支持 Python、TypeScript、TSX、JavaScript、Rust、Go、Java、C、C++、C#、PHP、Lua、Dart 等语言，Scala
  开发中，Ruby 通过可插拔 ast-grep 层提供结构支持。
- 本次更新新增 Ruby 语言支持、基于 ast-grep 的结构化搜索与替换能力，以及 NEWS.md 与 README 最新动态区块的发布自动化。
- cgr 已发布到 PyPI，可通过 uv 或 pipx 安装，运行需要 Docker（Memgraph）、cmake 和 ripgrep 环境。
- Code-Graph-RAG 可作为 MCP 服务器运行，让 Claude Code 等 MCP 客户端直接查询和编辑代码库，并提供云托管与本地私有化部署方案。
object_mentions:
- object_type: project
  name: code-graph-rag
  canonical_name: vitali87/code-graph-rag
  url: https://github.com/vitali87/code-graph-rag
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Code-Graph-RAG 用 Tree-sitter 解析多语言代码库，将函数、类、方法、模块及其关系以统一图模式存入 Memgraph 知识图谱。
  - 该工具以 MIT 协议开源，并可作为 MCP 服务器运行，让 Claude Code 等 MCP 客户端直接查询和编辑代码库。
  article_id: ad4fec82cec4fb39
- object_type: product
  name: cgr
  canonical_name: code-graph-rag CLI
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - cgr 命令行工具已发布到 PyPI，可通过 uv 或 pipx 安装，并附带 treesitter-full 和 semantic 两个扩展选项。
  - 用户运行 cgr start --repo-path 即可把仓库解析进共享图，配合 --update-graph 参数可增量同步单个项目而不影响其他项目。
  article_id: ad4fec82cec4fb39
- object_type: product
  name: Memgraph
  canonical_name: Memgraph
  url: null
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - Code-Graph-RAG 使用 Memgraph 作为图数据库，将 Tree-sitter 解析出的代码结构以统一语言无关的图模式存储。
  - cgr daemon up 命令会启动打包好的 Memgraph 与 Qdrant 技术栈，无需额外编写 compose 文件。
  article_id: ad4fec82cec4fb39
- object_type: product
  name: Qdrant
  canonical_name: Qdrant
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - Code-Graph-RAG 的打包技术栈中包含 Qdrant，通过 semantic 扩展为代码检索提供向量搜索能力。
  article_id: ad4fec82cec4fb39
- object_type: project
  name: ast-grep
  canonical_name: ast-grep
  url: null
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - Ruby 通过可插拔的 ast-grep 层加入图谱，只需一个 YAML 模式文件即可新增一种语言支持，无需手写解析器。
  - 工具借助 ast-grep 暴露为智能体工具，可依据 AST 模式在整库范围内完成结构化搜索与重写，替代文本或正则匹配。
  article_id: ad4fec82cec4fb39
- object_type: project
  name: Tree-sitter
  canonical_name: Tree-sitter
  url: null
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - 多语言解析器基于 Tree-sitter 读取代码库，将函数、类、方法、模块及其关系摄入 Memgraph 知识图谱。
  article_id: ad4fec82cec4fb39
extract_result: success
impact_score:
  score: 4.5
  reason: 这是个人开发者发布的社区开源项目，事件类型为 community_discussion。它把 Tree-sitter 多语言解析、Memgraph
    知识图谱与自然语言生成 Cypher 查询结合起来，并可作为 MCP 服务器接入 Claude Code，属于当前热门的代码智能/MCP 工具赛道，功能完整、文档清晰且已发布到
    PyPI，对个人开发者和小团队有实用价值，能在 MCP 开源圈形成一定声量；但同类能力已有 Sourcegraph、Copilot 等成熟产品覆盖，且无大厂背书或资本事件，属于局部生态补充而非格局重塑，故评分落在中低区间。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: MCP 服务器让 Claude Code 能以 AST 级精度直接查询、编辑和优化代码库
hype_assessment:
  level: low
  reason: README 通篇未出现"颠覆""革命性"等 PR 滥用词汇，功能声明均可验证：给出明确的架构流水线、安装命令、13 种语言支持矩阵以及发布到
    PyPI 的事实；即便带有云托管/私有化部署的商业推广，也属于开源核心 + 企业服务的常规 open-core 模式，不构成概念炒作。
information_entropy: medium
domain_disruption:
  technical_innovation: 以 Tree-sitter 将多语言代码库解析为统一语言无关的知识图谱（函数/类/方法/模块及其调用、引用关系）存入
    Memgraph，再用自然语言生成 Cypher 完成结构化检索；差异化亮点在于通过可插拔 ast-grep 层以单个 YAML 模式文件快速扩展新语言（如
    Ruby），并提供基于 AST 模式的结构化搜索与替换，替代纯文本/正则匹配，实现精确的代码级编辑。
  business_model: 采用开源核心（MIT + PyPI）+ 商业托管（云托管/私有化/气隙部署）的经典 open-core 模式，并借 MCP 服务器切入
    Claude Code 等代理生态，开辟了"代码知识图谱 + 智能体工具"的落地分发路径，为代码智能工具的商业化提供了一种低门槛参考。
engineering_complexity: production_ready
compound_value:
  score: 5.0
  reason: 这个事件代表了一个真实且有长期价值的架构方向：用知识图谱（而非纯向量）作为 AI 编码智能体的代码上下文底座，叠加 AST 级结构化编辑与 MCP
    服务器协议，恰好踩中 agentic coding 与 MCP 生态两条主线，方向上具备复利效应。但就本项目而言，护城河偏薄——Tree-sitter 解析
    + 图数据库 + LLM 生成 Cypher 的技术栈已被充分理解，竞争对手（闭源代码智能平台、各大模型厂商的 agentic 编码工具、以及 Sourcegraph
    等）资金与生态都远强于单一维护者的 MIT 项目；其差异化主要靠统一的 language-agnostic 图模式和 ast-grep 可插拔语言层，这属于工程执行力而非不可复制的壁垒。项目有潜力成为细分赛道的开源基础设施（尤其
    MCP 服务器形态让 Claude Code 等客户端可即插即用），但需持续验证社区采纳、云托管商业化转化率与多语言覆盖的广深度，3-5 年后仍是行业基石的概率不高，因此给到中位区间偏上的评分。
value_capture_layer: agent_middleware
moat_impact: democratizes_access
key_beneficiaries:
- Memgraph
- Qdrant
- Anthropic
competitive_casualty:
- 闭源代码智能/索引平台
- 纯向量检索的代码 RAG 工具
market_opportunities:
- 开发者可基于该项目验证的 Tree-sitter 多语言解析 + 知识图谱 + MCP 服务三层架构，面向大型遗留系统现代化、技术债评估、代码安全审计等垂直场景构建差异化代码智能工具
- 对数据主权要求高的行业（金融、政企、能源等）可评估将其 on-premise/air-gapped 部署作为内部代码问答与重构辅助平台的选型，这一私有化定位与大厂云产品形成错位竞争
- 该项目的 ast-grep 可插拔语言层设计为开源生态贡献者创造了低门槛扩展新语言、提供企业定制集成与训练服务的机会
risk_matrix:
  regulatory: MIT 开源协议本身合规风险低；但云托管方案将代码发送至第三方 AI 服务时，涉及代码出境的出口管制与行业数据合规（如金融、政务敏感代码），需在选型时重点评估
  technological: 基于解析+图结构+LLM 生成 Cypher 的技术路线面临大上下文模型与 Agentic 编码工具（Claude Code、Cursor、Copilot
    等）的替代压力；且依赖 Docker 运行 Memgraph，部署链路较重，存在环境兼容风险
  competitive: 代码智能赛道巨头云集（GitHub、Sourcegraph、Cursor、OpenAI/Anthropic 生态），个人/小团队开源项目面临强烈的生态挤压，云托管商业模式难以与背靠大厂资源的竞品打价格战
  ethical: 代码库全量解析可能索引并泄露密钥、内部算法逻辑等敏感信息；图结构本身也可能被投毒（恶意依赖或代码结构注入）从而污染 RAG 检索结果，造成错误建议
  additional:
  - 项目由单一维护者 vitali87 驱动，存在维护不可持续性、社区治理缺失与长期演进路径不确定的风险
  - 图谱索引实时同步与多项目共享图的清理机制（--clean 会删除所有项目）在多人协作环境存在误操作数据丢失隐患
confidence:
  impact: medium
  compound: low
  hype: low
actionable_insight: monitor
object_insights:
- object_type: project
  name: code-graph-rag
  canonical_name: vitali87/code-graph-rag
  url: https://github.com/vitali87/code-graph-rag
  positioning: Code-Graph-RAG 是一个基于 Tree-sitter 与 Memgraph 的开源代码库智能工具，将多语言代码结构转为统一知识图谱，支持用自然语言查询、编辑与优化代码。
  technical_signal: 采用 Tree-sitter 解析多语言代码，将函数、类、方法、模块及关系以统一语言无关图模式存入 Memgraph，并支持
    AST 级结构化编辑与死代码检测。
  adoption_signal: 项目以 MIT 协议开源并发布到 PyPI，可通过 uv 或 pipx 安装，并可作为 MCP 服务器被 Claude Code
    等客户端直接调用。
  ecosystem_relevance: 作为 MCP 服务器可让 Claude Code 等客户端直接查询编辑代码库，与 AI 编程工具生态深度协同。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 该项目用知识图谱替代纯向量检索来理解代码库，代表代码 Agent 上下文基础设施的新方向；其 MCP 服务器能力直接对接 Claude
    Code 生态，值得持续跟踪语言覆盖扩展与社区采用情况。
  risk_notes:
  - 项目依赖 Docker、cmake 与 ripgrep 等复杂运行环境，本地部署门槛较高。
  - Ruby 仅通过可插拔 ast-grep 层提供结构支持，Scala 仍在开发中，语言覆盖尚未完全成熟。
  - 项目由个人开发者主导，社区规模与长期维护活力有待观察。
  score: 7.0
  article_ids:
  - ad4fec82cec4fb39
  evidence_snippets:
  - Code-Graph-RAG 用 Tree-sitter 解析多语言代码库，将函数、类、方法、模块及其关系以统一图模式存入 Memgraph 知识图谱。
  - 该工具以 MIT 协议开源，并可作为 MCP 服务器运行，让 Claude Code 等 MCP 客户端直接查询和编辑代码库。
- object_type: product
  name: cgr
  canonical_name: code-graph-rag CLI
  url: null
  positioning: cgr 是 Code-Graph-RAG 的交互式命令行工具，将自然语言转为 Cypher 查询以检索代码，并驱动 AI 编辑与优化，支持本地私有化与云托管部署。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 使用 Claude Code 等 MCP 客户端的开发者
  - 需要数据主权的受监管行业与安全敏感机构
  product_signal: cgr 已发布到 PyPI，提供 treesitter-full 与 semantic 扩展，用户运行 cgr start --repo-path
    即可将仓库解析进共享图并增量同步。
  market_signal: 项目提供全托管云服务与本地及气隙网络私有化部署方案，面向需要数据主权的受监管行业与安全敏感机构。
  differentiation: 区别于纯向量检索工具，cgr 基于 Memgraph 图结构与 Cypher 查询，支持 AST 级结构化搜索替换与死代码检测。
  watch_reason: cgr 以共享图加增量同步的方式管理多仓库代码索引，并借 PyPI 分发降低安装门槛，同时提供云托管与私有化两条商业化路径，值得跟踪其企业采用与
    MCP 生态扩散。
  risk_notes:
  - 命令行依赖 Docker（Memgraph）等基础设施，环境准备成本可能阻碍轻量用户上手。
  - 云托管与私有化部署为商业能力，开源免费与付费版本的边界尚需观察。
  score: 6.0
  article_ids:
  - ad4fec82cec4fb39
  evidence_snippets:
  - cgr 命令行工具已发布到 PyPI，可通过 uv 或 pipx 安装，并附带 treesitter-full 和 semantic 两个扩展选项。
  - 用户运行 cgr start --repo-path 即可把仓库解析进共享图，配合 --update-graph 参数可增量同步单个项目而不影响其他项目。
---

Code-Graph-RAG parses a multi-language codebase with Tree-sitter, builds a knowledge graph of its structure in Memgraph, and lets you query, edit, and optimise that code in plain English. It works across a monorepo of mixed languages under one unified graph schema.

**Release Automation**:`NEWS.md`

and the README's "Latest News" section now refresh automatically on every release, keeping the changelog current without hand edits.**Ruby Support**: Ruby joins the graph through a new pluggable ast-grep tier that adds a language from a single YAML pattern file, emitting`Module`

,`Function`

, and`Class`

nodes plus import edges without a hand-written parser.**Structural Search & Replace**: Find and rewrite code by AST pattern with ast-grep, exposed as agent tools so you can match and transform structure across the whole codebase instead of relying on text or regex.

See NEWS.md for the full history.

Point Code-Graph-RAG at a repository and it reads every source file, extracts functions, classes, methods, modules, and the relationships between them, and stores the result as an interconnected graph. Once the graph exists you can:

- Ask questions about the codebase in natural language and get answers grounded in the real structure.
- Retrieve the actual source of any function, class, or method by name or by intent.
- Edit code through the agent with AST-based surgical patching and a diff preview before anything changes.
- Optimise code against language best practices or your own coding standards.
- Find dead code by walking call and reference edges from entry points.
- Search and rewrite structurally by AST pattern with ast-grep.

The system has two components:

**Multi-language parser.**A Tree-sitter based parser reads the codebase and ingests functions, classes, methods, modules, and their relationships into Memgraph under a single language-agnostic schema.**RAG system**(`codebase_rag/`

). An interactive CLI that turns natural language into Cypher queries, retrieves matching code, and drives AI-powered editing and optimisation.

```
Source Code -> Tree-sitter Parser -> AST Analysis -> Memgraph Knowledge Graph
|
User Query -> AI Model (Cypher Gen) -> Cypher Query -> Graph Results -> Response
```


See the Architecture Overview and Graph Schema for the full picture.

Python, TypeScript, TSX, JavaScript, Rust, Go, Java, C, C++, C#, PHP, Lua, and Dart are fully supported. Scala is in development, and Ruby has structural support (modules, functions, classes, and imports) through the pluggable ast-grep tier. See the Language Support matrix for per-language capabilities.

`cgr`

is published to PyPI. Install it system-wide with the `treesitter-full`

(all languages) and `semantic`

(vector search) extras:

```
# with uv (recommended)
uv tool install "code-graph-rag[treesitter-full,semantic]"
# or with pipx
pipx install "code-graph-rag[treesitter-full,semantic]"
```

You also need Docker (for Memgraph), `cmake`

, and `ripgrep`

. Full prerequisites, source installs, and environment setup are in the Installation guide.

```
# Start the packaged Memgraph + Qdrant stack (no compose file needed)
cgr daemon up
# Parse a repository into the graph, then query it
cgr start --repo-path /path/to/repo --update-graph
cgr start --repo-path /path/to/repo
```

Repeat the first command for each repository you want indexed; the graph is
shared, and syncing one project leaves the others alone. To start over from an
empty graph, add `--clean`

— it deletes **every** project in the shared graph,
not just this one, and asks for confirmation first when other
projects would be destroyed.

The Quick Start guide walks through parsing, querying, and exporting in five minutes.

Code-Graph-RAG runs as an MCP server so Claude Code and other MCP clients can query and edit your codebase directly. See the MCP Server guide for setup.

**Getting Started**

**User Guide**

- CLI Reference
- Interactive Querying
- Code Optimisation
- Dead Code Detection
- Graph Export
- Real-Time Updates
- MCP Server

**Architecture**

**Python SDK**

**Advanced**

Code-Graph-RAG is open source and free to use. For organisations that need more, we offer **fully managed cloud-hosted solutions** and **on-premise deployments**:

**Cloud-Hosted Deployment**: Managed cloud infrastructure for both the graph database and the AI agent connection. Zero infrastructure overhead, so we handle scaling, updates, and availability while your team focuses on building.**On-Premise & Air-Gapped Deployment**: Deploy Code-Graph-RAG entirely within your own environment, including air-gapped networks. Full data sovereignty for regulated industries and security-sensitive organisations.

We also offer custom development, integration consulting, technical support contracts, and team training.

Please see CONTRIBUTING.md for contribution guidelines. Good first PRs come from the TODO issues.

For issues or questions, check the Troubleshooting guide first, then open an issue.

MIT. See LICENSE.