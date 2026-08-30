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