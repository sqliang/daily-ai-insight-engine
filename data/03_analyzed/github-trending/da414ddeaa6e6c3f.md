---
title: tursodatabase/turso
source: https://github.com/tursodatabase/turso
author: []
published: ''
created: '2026-06-21'
description: 'Turso is an in-process SQL database, compatible with SQLite. Turso Database
  An in-process SQL database, compatible with SQLite. About Turso Database is an in-process
  SQL database written in Rust, compatible with SQLite. ⚠️ Warning: This software
  is in BETA. It may still contain bugs and unexpected behavior. Use caution with
  production data and ensure you have backups. Features and Roadmap SQLite compatibility
  for SQL dialect, file formats, and the C API [see document for details] BEGIN CONCURRENT
  for improved write throughput using multi-version concurrency control (MVCC). Change
  data capture (CDC) for real-time tracking of database changes. Multi-language support
  for Go JavaScript Java .NET Python Rust WebAssembly Asynchronous I/O support on
  Linux with io_uring Cross-platform support for Linux, macOS, Windows and browsers
  (through WebAssembly) Vector support support including exact search and vector manipulation
  Improved schema management including extended ALTER support and faster schema changes.
  The database has the following experimental features: Encryption at rest for protecting
  the data locally. Incremental computation using DBSP for incremental view maintenance
  and query subscriptions. Full-Text-Search powered by the awesome tantivy library
  Multi-process WAL coordination via the .tshm sidecar for cross-process WAL readers
  and writers. The following features are on our current roadmap: Vector indexing
  for fast approximate vector search, similar to libSQL vector search. Getting Started
  Please see the Turso Database Manual for more information. 💻 Command Line You can
  install the latest `turso` release with: curl --proto ''=https'' --tlsv1.2 -LsSf
  \ https://github.com/tursodatabase/turso/releases/latest/download/turso_cli-installer.sh
  | sh Then launch the interactive shell: $ tursodb This will start the Turso interactive
  shell where you can execute SQL statements: Turso Enter ".help" for usage hints.
  Connected to a transient in-memory database. Use ".open FILENAME" to reopen on a
  persistent database turso> CREATE TABLE users (id INT, username TEXT); turso> INSERT
  INTO users VALUES (1, ''alice''); turso> INSERT INTO users VALUES (2, ''bob'');
  turso> SELECT * FROM users; 1|alice 2|bob You can also build and run the latest
  development version with: cargo run If you like docker, we got you covered. Simply
  run this in the root folder: make docker-cli-build && \ make docker-cli-run 🦀 Rust
  cargo add turso Example usage: let db = Builder::new_local("sqlite.db").build().await?;
  let conn = db.connect()?; let res = conn.query("SELECT * FROM users", ()).await?;
  ✨ JavaScript npm i @tursodatabase/database Example usage: import { connect } from
  ''@tursodatabase/database''; const db = await connect(''sqlite.db''); const stmt
  = db.prepare(''SELECT * FROM users''); const users = stmt.all(); console.log(users);
  🐍 Python uv pip install pyturso Example usage: import turso con = turso.connect("sqlite.db")
  cur = con.cursor() res = cur.execute("SELECT * FROM users") print(res.fetchone())
  🦫 Go go get turso.tech/database/tursogo go install turso.tech/database/tursogo Example
  usage: import ( "database/sql" _ "turso.tech/database/tursogo" ) conn, _ = sql.Open("turso",
  "sqlite.db") defer conn.Close() stmt, _ := conn.Prepare("select * from users") defer
  stmt.Close() rows, _ = stmt.Query() for rows.Next() { var id int var username string
  _ := rows.Scan(&id, &username) fmt.Printf("User: ID: %d, Username: %s\n", id, username)
  } ️#️⃣ .NET Example usage: using Turso; using var connection = new TursoConnection("Data
  Source=:memory:"); connection.Open(); connection.ExecuteNonQuery("CREATE TABLE t(a,
  b)"); var rowsAffected = connection.ExecuteNonQuery("INSERT INTO t(a, b) VALUES
  (1, 2), (3, 4)"); Console.WriteLine($"RowsAffected: {rowsAffected}"); using var
  command = connection.CreateCommand(); command.CommandText = "SELECT * FROM t"; using
  var reader = command.ExecuteReader(); while (reader.Read()) { var a = reader.GetInt32(0);
  var b = reader.GetInt32(1); Console.WriteLine($"Value1: {a}, Value2: {b}"); } ☕️
  Java We integrated Turso Database into JDBC. For detailed instructions on how to
  use Turso Database with java, please refer to the README.md under bindings/java.
  🤖 MCP Server Mode The Turso CLI includes a built-in Model Context Protocol (MCP)
  server that allows AI assistants to interact with your databases. Start the MCP
  server with: tursodb your_database.db --mcp Configuration Add Turso to your MCP
  client configuration: { "mcpServers": { "turso": { "command": "/path/to/.turso/tursodb",
  "args": ["/path/to/your/database.db", "--mcp"] } } } Available Tools The MCP server
  provides nine tools for database interaction: open_database - Open a new database
  current_database - Describe the current database list_tables - List all tables in
  the database describe_table - Describe the structure of a specific table execute_query
  - Execute read-only SELECT queries insert_data - Insert new data into tables update_data
  - Update existing data in tables delete_data - Delete data from tables schema_change
  - Execute schema modification statements (CREATE TABLE, ALTER TABLE, DROP TABLE)
  Once connected, you can ask your AI assistant: "Show me all tables in the database"
  "What''s the schema for the users table?" "Find all posts with more than 100 upvotes"
  "Insert a new user with name ''Alice'' and email ''alice@example.com''" MCP Clients
  Claude Code If you''re using Claude Code, you can easily connect to your Turso MCP
  server using the built-in MCP management commands: Quick Setup Add the MCP server
  to Claude Code: claude mcp add my-database -- tursodb ./path/to/your/database.db
  --mcp Restart Claude Code to activate the connection Start querying your database
  through natural language! Command Breakdown claude mcp add my-database -- tursodb
  ./path/to/your/database.db --mcp # ↑ ↑ ↑ ↑ # | | | | # Name | Database path MCP
  flag # Separator my-database - Choose any name for your MCP server -- - Required
  separator between Claude options and your command tursodb - The Turso database CLI
  ./path/to/your/database.db - Path to your SQLite database file --mcp - Enables MCP
  server mode Example Usage # For a local project database cd /your/project claude
  mcp add my-project-db -- tursodb ./data/app.db --mcp # For an absolute path claude
  mcp add analytics-db -- tursodb /Users/you/databases/analytics.db --mcp # For a
  specific project (local scope) claude mcp add project-db --local -- tursodb ./database.db
  --mcp Managing MCP Servers # List all configured MCP servers claude mcp list # Get
  details about a specific server claude mcp get my-database # Remove an MCP server
  claude mcp remove my-database Claude Desktop For Claude Desktop, add the configuration
  to your claude_desktop_config.json file: { "mcpServers": { "turso": { "command":
  "/path/to/.turso/tursodb", "args": ["./path/to/your/database.db.db", "--mcp"] }
  } } Cursor For Cursor, configure MCP in your settings: Open Cursor settings Navigate
  to Extensions → MCP Add a new server with: Name: turso Command: /path/to/.turso/tursodb
  Args: ["./path/to/your/database.db.db", "--mcp"] Alternatively, you can add it to
  your Cursor configuration file directly. Direct JSON-RPC Usage The MCP server runs
  as a single process that handles multiple JSON-RPC requests over stdin/stdout. Here''s
  how to interact with it directly: Example with In-Memory Database cat << ''EOF''
  | tursodb --mcp {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion":
  "2024-11-05", "capabilities": {}, "clientInfo": {"name": "client", "version": "1.0"}}}
  {"jsonrpc": "2.0", "id": 2, "method": "tools/call", "params": {"name": "schema_change",
  "arguments": {"query": "CREATE TABLE users (id INTEGER, name TEXT, email TEXT)"}}}
  {"jsonrpc": "2.0", "id": 3, "method": "tools/call", "params": {"name": "list_tables",
  "arguments": {}}} {"jsonrpc": "2.0", "id": 4, "method": "tools/call", "params":
  {"name": "insert_data", "arguments": {"query": "INSERT INTO users VALUES (1, ''Alice'',
  ''alice@example.com'')"}}} {"jsonrpc": "2.0", "id": 5, "method": "tools/call", "params":
  {"name": "execute_query", "arguments": {"query": "SELECT * FROM users"}}} EOF Example
  with Existing Database # Working with an existing database file cat << ''EOF'' |
  tursodb mydb.db --mcp {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params":
  {"protocolVersion": "2024-11-05", "capabilities": {}, "clientInfo": {"name": "client",
  "version": "1.0"}}} {"jsonrpc": "2.0", "id": 2, "method": "tools/call", "params":
  {"name": "list_tables", "arguments": {}}} EOF Contributing We''d love to have you
  contribute to Turso Database! Please check out the contribution guide to get started.
  FAQ Is Turso Database ready for production use? Turso powers production apps today.
  That includes Turso Cloud, the Kin AI assistant, and Spice.ai. However, it is still
  under active development and for mission-critical applications, caution is advised.
  Independent backups are encouraged. Turso is extensively tested by a collection
  of tools including a native Deterministic Simulation Testing suite and Antithesis,
  so we are generally confident in the end result. But our bar is SQLite-level reliability,
  and we will still recommend caution until we are confident it meets that bar. How
  is Turso Database different from Turso''s libSQL? Turso Database is a project to
  build the next evolution of SQLite in Rust, with a strong open contribution focus
  and features like native async support, vector search, and more. The libSQL project
  is also an attempt to evolve SQLite in a similar direction, but through a fork rather
  than a rewrite. Rewriting SQLite in Rust started as an unassuming experiment, and
  due to its incredible success, replaces libSQL as our intended direction. At this
  point, libSQL is production ready, Turso Database is not - although it is evolving
  rapidly. More details here. Publications Pekka Enberg, Sasu Tarkoma, Jon Crowcroft
  Ashwin Rao (2024). Serverless Runtime / Database Co-Design With Asynchronous I/O.
  In EdgeSys ‘24. [PDF] Pekka Enberg, Sasu Tarkoma, and Ashwin Rao (2023). Towards
  Database and Serverless Runtime Co-Design. In CoNEXT-SW ’23. [PDF] [Slides] Alperen
  Keles, Ethan Chou, Harrison Goldstein, Leonidas Lampropoulos (2026). DIRT: Database-Integrated
  Random Testing. In DBTest ''26. [PDF] License This project is licensed under the
  MIT license. Contribution Unless you explicitly state otherwise, any contribution
  intentionally submitted for inclusion in Turso Database by you, shall be licensed
  as MIT, without any additional terms or conditions. Partners Thanks to all the partners
  of Turso! Contributors Thanks to all the contributors to Turso Database!'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: da414ddeaa6e6c3f
source_type: community_discussion
tldr: Turso Database 是一个用 Rust 重写的 SQLite 兼容数据库，处于 Beta 阶段，支持 MVCC、CDC、向量搜索和异步 I/O。其
  CLI 内置 MCP 服务器，可为 AI 助手提供九种数据库交互工具，并支持 Rust、JavaScript、Python、Go、.NET 和 Java 等多种语言绑定。
objective_summary: Turso 团队在 GitHub 上发布了 tursodatabase/turso 项目，这是一个用 Rust 从零重写的 SQLite
  兼容数据库引擎。该数据库支持多版本并发控制（MVCC）提升写入吞吐量、变更数据捕获（CDC）、向量搜索与操作、异步 I/O（io_uring）、以及扩展的 ALTER
  TABLE 等特性。项目提供跨平台支持（Linux、macOS、Windows 和浏览器 WebAssembly），并为 Rust、JavaScript、Python、Go、.NET
  和 Java 提供了官方 SDK 绑定。Turso CLI 工具内置 MCP 服务器模式，可让 AI 助手直接通过自然语言查询和修改数据库。该项目源于 libSQL
  的演进，目前处于 Beta 阶段，团队建议在生产数据中保持谨慎并做好备份。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - Turso
  - Spice.ai
  technologies:
  - SQLite
  - MVCC
  - CDC
  - WebAssembly
  - MCP
  - DBSP
  - tantivy
  - libSQL
  - io_uring
  key_people:
  - Pekka Enberg
  - Sasu Tarkoma
  - Jon Crowcroft
  - Ashwin Rao
  - Alperen Keles
  - Ethan Chou
  - Harrison Goldstein
  - Leonidas Lampropoulos
key_logic_flow:
- Turso Database 是一个用 Rust 重写的 SQLite 兼容数据库引擎，目前处于 Beta 阶段，提供跨 Linux、macOS、Windows
  和浏览器的多平台支持。
- 该数据库支持多版本并发控制（MVCC）提升写入吞吐量、变更数据捕获（CDC）、向量搜索与操作，以及基于 io_uring 的异步 I/O。
- 项目提供加密、增量计算（DBSP）、全文搜索（tantivy）等实验性功能，并将向量索引列为未来路线图。
- Turso 拥有 Rust、JavaScript、Python、Go、.NET 和 Java 六种语言的官方 SDK 绑定，方便不同技术栈的开发者集成。
- Turso CLI 内置 MCP 服务器模式，提供九种数据库交互工具，可集成到 Claude Code、Claude Desktop 和 Cursor 等 AI
  客户端中。
- 该项目由 libSQL 演进而来，团队选择 Rust 重写方案替代了原先的 libSQL 分支方案，Turso Cloud 等生产应用已在运行中。
extract_result: success
object_mentions:
- object_type: project
  name: tursodatabase/turso
  canonical_name: tursodatabase/turso
  url: https://github.com/tursodatabase/turso
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Turso Database 是一个用 Rust 编写的 SQLite 兼容数据库，支持多版本并发控制（MVCC）以提高写入吞吐量。
  - 该项目处于 Beta 阶段，提供跨平台支持和 Rust、JavaScript、Python、Go、.NET、Java 等多语言绑定。
  - 项目由 libSQL 演进而来，团队以 Rust 重写方案替代了原先的 libSQL 分支方案。
  article_id: da414ddeaa6e6c3f
- object_type: project
  name: libSQL
  canonical_name: libSQL
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - libSQL 项目也试图向类似方向演进 SQLite，但采用 fork 分支方式而非 Rust 重写。
  - Turso Database 最初是作为一个实验开始的，现已替代 libSQL 成为团队的预期发展方向。
  article_id: da414ddeaa6e6c3f
- object_type: product
  name: Turso MCP Server
  canonical_name: Turso MCP Server
  url: null
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - Turso CLI 内置 MCP 服务器模式，可为 AI 助手提供九种数据库交互工具，包括查询、插入、更新和删除操作。
  - 该 MCP 服务器支持与 Claude Code、Claude Desktop 和 Cursor 等 AI 工具集成。
  - 用户可以通过自然语言向 AI 助手询问数据库内容，例如查询表结构或查找特定数据。
  article_id: da414ddeaa6e6c3f
impact_score:
  score: 6.5
  reason: Turso Database 是 SQLite 生态近年来最重大的基础设施级更新之一。SQLite 全球部署量极大，但其单写入器架构一直是写入密集场景的瓶颈。Turso
    用 Rust 重写并引入 MVCC、CDC、io_uring 异步 I/O，在保持文件格式和 C API 完全兼容的前提下突破原版架构限制，同时内置 MCP
    服务器模式直接对接 AI 客户端，技术路线清晰且实用。然而该项目仍处于 Beta 阶段，需要时间验证稳定性和生态迁移成本，达不到范式转移级别（8+），但显著改变了
    SQLite 嵌入式数据库的竞争格局。评分：6.5
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: Rust 重写 SQLite 兼容数据库的 MVCC 写入性能提升和 MCP 原生集成带来的 AI 交互新范式
hype_assessment:
  level: low
  reason: 该项目以技术文档风格呈现，明确标注 Beta 阶段及潜在风险，列出实验性功能与路线图边界，未使用 '颠覆'、'革命性' 等 PR 夸饰语言。各项技术主张（MVCC、CDC、io_uring、向量搜索）均有明确的技术实现路径，信息透明度高。
information_entropy: high
domain_disruption:
  technical_innovation: 用 Rust 重写 SQLite 兼容层，引入 MVCC（通过 BEGIN CONCURRENT 提升写入吞吐）、CDC
    实时变更捕获、io_uring 异步 I/O、向量搜索及基于 DBSP 的增量计算，在保持 SQLite 文件格式和 C API 完全兼容的前提下突破原版单写入器架构瓶颈。
  business_model: 内置 MCP 服务器模式，将数据库操作封装为 9 种 AI 客户端可直接调用的工具，开创了数据库即 AI 数据源的新交互范式，可能重塑
    AI 应用访问本地数据的方式，降低 AI 集成门槛。
engineering_complexity: production_ready
compound_value:
  score: 7.5
  reason: Turso Database 通过完全兼容 SQLite 的 SQL 方言、文件格式和 C API，实现了零成本的存量生态迁移。其最大的复利杠杆来自两个差异化引擎：一是
    MVCC + io_uring + CDC 等现代特性解决了 SQLite 长期以来的写入瓶颈和实时数据需求，二是内置 MCP 服务器模式（9 种数据库工具），使
    AI Agent 能原生操作数据库。一旦 MCP 成为 AI-工具交互的标准协议，Turso 作为首个在核心产品中深度集成 MCP 的数据库，将享受显著的先发优势和网络效应——更多
    AI 客户端（Claude Code、Cursor 等）支持 MCP → 更多开发者选择 Turso → 数据和 schema 层面的锁定效应加深。向量搜索、DBSP
    增量计算、WASM 浏览器运行等特性进一步拓展了在 AI 工作流和边缘计算中的适用场景。目前已被 Turso Cloud、Kin AI、Spice.ai 等生产环境验证，证明了
    PMF 的初步成立。风险在于：Beta 阶段的不确定性、SQLite 生态极其稳固（SQLite 本身也持续迭代）、DuckDB 在分析场景的强势竞争，以及
    MCP 协议标准化进程的不确定性。综合来看，若能抓住 AI Agent 数据层的生态位，具备较强的复利积累潜力，评分 7.5，值得持续跟踪 adoption
    曲线和开发者生态增长。
value_capture_layer: agent_middleware
moat_impact: creates_new_moat
key_beneficiaries:
- Turso
- Anthropic
- Claude Code
- Cursor
- Spice.ai
competitive_casualty:
- SQLite
- DuckDB
- libSQL
- 传统嵌入式数据库方案
market_opportunities:
- 开发者可基于 Turso 内置的 MCP 服务器快速构建 AI Agent 数据处理工具，极大降低自然语言操作数据库的集成成本
- 边缘计算与浏览器端场景可借助其 WebAssembly 支持和轻量级进程内架构，打造本地优先的 AI 应用数据层
- 将 CDC 实时变更捕获与向量搜索结合，适合构建需要实时数据同步+语义检索的 RAG 应用
risk_matrix:
  regulatory: 无
  technological: Turso Database 仍处于 Beta 阶段，存在未发现的 Bug 和破坏性变更风险；且该项目已替代 libSQL 成为未来方向，现有
    libSQL 用户面临技术栈迁移的不确定性
  competitive: SQLite 生态已有 libSQL、DuckDB、Better-SQLite3 等竞品，Turso 需在稳定性和 MCP 差异化之间取得平衡；同时云数据库厂商（如
    Neon、PlanetScale）也在强化 AI 集成能力
  ethical: MCP 服务器模式赋予 AI 助手直接读写数据库的能力，若权限控制不当或缺乏审计，可能导致数据泄露或未经授权的数据修改
  additional:
  - Turso 同时维护 libSQL 和 Turso Database 两个项目，社区资源分配和长期路线图可能存在分裂风险
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: deep_dive
object_insights:
- object_type: project
  name: tursodatabase/turso
  canonical_name: tursodatabase/turso
  url: https://github.com/tursodatabase/turso
  positioning: 基于 Rust 从零重写的 SQLite 兼容嵌入式数据库引擎，通过 MVCC 并发控制提升写入吞吐量，并原生内置 MCP 服务器以支持
    AI 助手直接操作数据库。
  technical_signal: 采用 Rust 语言完整重写 SQLite 兼容层，实现 MVCC、io_uring 异步 I/O、向量搜索与 CDC 变更捕获等高级特性，技术架构激进且完整。
  adoption_signal: 已提供 Rust、JavaScript、Python、Go、.NET 和 Java 六种官方 SDK 绑定，覆盖主流操作系统与浏览器
    WebAssembly 平台。
  ecosystem_relevance: 源自 libSQL 生态的技术演进，CLI 内置 MCP 服务器可直接对接 Claude Code 和 Cursor
    等 AI 客户端，推动 AI 与数据库交互范式融合。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: Turso Database 以 Rust 重写 SQLite 的方式在兼容性与创新性之间找到独特平衡，其内置 MCP 服务器预示
    AI 时代数据库交互范式变革，值得持续跟踪其从 Beta 到正式版的演进路径及社区生态发展。
  risk_notes:
  - 项目仍处于 Beta 阶段，可能存在未发现的 Bug 和逻辑缺陷，生产环境部署需谨慎评估稳定性风险。
  - Rust 重写方案需持续维护与上游 SQLite 文件格式和 C API 的兼容性，长期维护成本较高。
  score: 7.0
  article_ids:
  - da414ddeaa6e6c3f
  evidence_snippets:
  - Turso Database 是一个用 Rust 编写的 SQLite 兼容数据库，支持多版本并发控制（MVCC）以提高写入吞吐量。
  - 该项目处于 Beta 阶段，提供跨平台支持和 Rust、JavaScript、Python、Go、.NET、Java 等多语言绑定。
  - 项目由 libSQL 演进而来，团队以 Rust 重写方案替代了原先的 libSQL 分支方案。
  - Turso CLI 内置 MCP 服务器模式，提供九种数据库交互工具，可集成到 Claude Code、Claude Desktop 和 Cursor 等
    AI 客户端中。
- object_type: project
  name: libSQL
  canonical_name: libSQL
  url: null
  positioning: SQLite 的开放分支项目，旨在通过 fork 方式扩展 SQLite 功能边界，是 Turso Database 的技术前身与路线对照。
  technical_signal: 采用 fork 分支方式扩展 SQLite 能力，技术路线相对保守但保持了与上游的高度兼容，与 Turso 的 Rust 重写方案形成路线对比。
  adoption_signal: 作为 Turso 团队原先主力项目已有一定社区基础，但团队现已转向 Rust 重写方案，libSQL 分支路线的发展重心正在转移。
  ecosystem_relevance: 与 Turso Database 构成直接演进关系，代表 SQLite 生态中分支扩展与重写重构两种增强路线的分化与对照。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: libSQL 作为 SQLite 生态的重要分支项目，其与 Turso Rust 重写方案的路线分化反映了数据库底层技术演进的关键决策，值得跟踪两种方案在社区采纳率和功能完备性上的长期对比。
  risk_notes:
  - Turso 团队已全面转向 Rust 重写方案，libSQL 分支路线的未来维护资源和社区活跃度存在不确定性。
  score: 4.0
  article_ids:
  - da414ddeaa6e6c3f
  evidence_snippets:
  - libSQL 项目也试图向类似方向演进 SQLite，但采用 fork 分支方式而非 Rust 重写。
  - Turso Database 最初是作为一个实验开始的，现已替代 libSQL 成为团队的预期发展方向。
---

An in-process SQL database, compatible with SQLite.

Turso Database is an in-process SQL database written in Rust, compatible with SQLite.


This software is in BETA. It may still contain bugs and unexpected behavior. Use caution with production data and ensure you have backups.⚠️ Warning:

**SQLite compatibility**for SQL dialect, file formats, and the C API [see document for details]for improved write throughput using multi-version concurrency control (MVCC).`BEGIN CONCURRENT`

**Change data capture (CDC)**for real-time tracking of database changes.**Multi-language support**for**Asynchronous I/O**support on Linux with`io_uring`

**Cross-platform**support for Linux, macOS, Windows and browsers (through WebAssembly)**Vector support**support including exact search and vector manipulation**Improved schema management**including extended`ALTER`

support and faster schema changes.

The database has the following experimental features:

**Encryption at rest**for protecting the data locally.**Incremental computation**using DBSP for incremental view maintenance and query subscriptions.**Full-Text-Search**powered by the awesome tantivy library**Multi-process WAL coordination**via the`.tshm`

sidecar for cross-process WAL readers and writers.

The following features are on our current roadmap:

**Vector indexing**for fast approximate vector search, similar to libSQL vector search.

Please see the Turso Database Manual for more information.

## 💻 Command Line

You can install the latest `turso` release with:

```
curl --proto '=https' --tlsv1.2 -LsSf \
https://github.com/tursodatabase/turso/releases/latest/download/turso_cli-installer.sh | sh
```

Then launch the interactive shell:

`$ tursodb`

This will start the Turso interactive shell where you can execute SQL statements:

```
Turso
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database
turso> CREATE TABLE users (id INT, username TEXT);
turso> INSERT INTO users VALUES (1, 'alice');
turso> INSERT INTO users VALUES (2, 'bob');
turso> SELECT * FROM users;
1|alice
2|bob
```

You can also build and run the latest development version with:

`cargo run`

If you like docker, we got you covered. Simply run this in the root folder:

```
make docker-cli-build && \
make docker-cli-run
```

## 🦀 Rust

`cargo add turso`

Example usage:

```
let db = Builder::new_local("sqlite.db").build().await?;
let conn = db.connect()?;
let res = conn.query("SELECT * FROM users", ()).await?;
```

## ✨ JavaScript

`npm i @tursodatabase/database`

Example usage:

```
import { connect } from '@tursodatabase/database';
const db = await connect('sqlite.db');
const stmt = db.prepare('SELECT * FROM users');
const users = stmt.all();
console.log(users);
```

## 🐍 Python

`uv pip install pyturso`

Example usage:

```
import turso
con = turso.connect("sqlite.db")
cur = con.cursor()
res = cur.execute("SELECT * FROM users")
print(res.fetchone())
```

## 🦫 Go

```
go get turso.tech/database/tursogo
go install turso.tech/database/tursogo
```

Example usage:

```
import (
"database/sql"
_ "turso.tech/database/tursogo"
)
conn, _ = sql.Open("turso", "sqlite.db")
defer conn.Close()
stmt, _ := conn.Prepare("select * from users")
defer stmt.Close()
rows, _ = stmt.Query()
for rows.Next() {
var id int
var username string
_ := rows.Scan(&id, &username)
fmt.Printf("User: ID: %d, Username: %s\n", id, username)
}
```

## ️#️⃣ .NET

Example usage:

```
using Turso;
using var connection = new TursoConnection("Data Source=:memory:");
connection.Open();
connection.ExecuteNonQuery("CREATE TABLE t(a, b)");
var rowsAffected = connection.ExecuteNonQuery("INSERT INTO t(a, b) VALUES (1, 2), (3, 4)");
Console.WriteLine($"RowsAffected: {rowsAffected}");
using var command = connection.CreateCommand();
command.CommandText = "SELECT * FROM t";
using var reader = command.ExecuteReader();
while (reader.Read())
{
var a = reader.GetInt32(0);
var b = reader.GetInt32(1);
Console.WriteLine($"Value1: {a}, Value2: {b}");
}
```

## ☕️ Java

We integrated Turso Database into JDBC. For detailed instructions on how to use Turso Database with java, please refer to the README.md under bindings/java.

## 🤖 MCP Server Mode

The Turso CLI includes a built-in Model Context Protocol (MCP) server that allows AI assistants to interact with your databases.

Start the MCP server with:

`tursodb your_database.db --mcp`

Add Turso to your MCP client configuration:

```
{
"mcpServers": {
"turso": {
"command": "/path/to/.turso/tursodb",
"args": ["/path/to/your/database.db", "--mcp"]
}
}
}
```

The MCP server provides nine tools for database interaction:

- Open a new database`open_database`

- Describe the current database`current_database`

- List all tables in the database`list_tables`

- Describe the structure of a specific table`describe_table`

- Execute read-only SELECT queries`execute_query`

- Insert new data into tables`insert_data`

- Update existing data in tables`update_data`

- Delete data from tables`delete_data`

- Execute schema modification statements (CREATE TABLE, ALTER TABLE, DROP TABLE)`schema_change`


Once connected, you can ask your AI assistant:

- "Show me all tables in the database"
- "What's the schema for the users table?"
- "Find all posts with more than 100 upvotes"
- "Insert a new user with name 'Alice' and email 'alice@example.com'"

## Claude Code

If you're using Claude Code, you can easily connect to your Turso MCP server using the built-in MCP management commands:

-
**Add the MCP server**to Claude Code:claude mcp add my-database -- tursodb ./path/to/your/database.db --mcp

-
**Restart Claude Code**to activate the connection -
**Start querying**your database through natural language!

```
claude mcp add my-database -- tursodb ./path/to/your/database.db --mcp
# ↑ ↑ ↑ ↑
# | | | |
# Name | Database path MCP flag
# Separator
```

- Choose any name for your MCP server`my-database`

- Required separator between Claude options and your command`--`

- The Turso database CLI`tursodb`

- Path to your SQLite database file`./path/to/your/database.db`

- Enables MCP server mode`--mcp`


```
# For a local project database
cd /your/project
claude mcp add my-project-db -- tursodb ./data/app.db --mcp
# For an absolute path
claude mcp add analytics-db -- tursodb /Users/you/databases/analytics.db --mcp
# For a specific project (local scope)
claude mcp add project-db --local -- tursodb ./database.db --mcp
```

```
# List all configured MCP servers
claude mcp list
# Get details about a specific server
claude mcp get my-database
# Remove an MCP server
claude mcp remove my-database
```

## Claude Desktop

For Claude Desktop, add the configuration to your `claude_desktop_config.json`

file:

```
{
"mcpServers": {
"turso": {
"command": "/path/to/.turso/tursodb",
"args": ["./path/to/your/database.db.db", "--mcp"]
}
}
}
```

## Cursor

For Cursor, configure MCP in your settings:

- Open Cursor settings
- Navigate to Extensions → MCP
- Add a new server with:
**Name**:`turso`

**Command**:`/path/to/.turso/tursodb`

**Args**:`["./path/to/your/database.db.db", "--mcp"]`



Alternatively, you can add it to your Cursor configuration file directly.

The MCP server runs as a single process that handles multiple JSON-RPC requests over stdin/stdout. Here's how to interact with it directly:

```
cat << 'EOF' | tursodb --mcp
{"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2024-11-05", "capabilities": {}, "clientInfo": {"name": "client", "version": "1.0"}}}
{"jsonrpc": "2.0", "id": 2, "method": "tools/call", "params": {"name": "schema_change", "arguments": {"query": "CREATE TABLE users (id INTEGER, name TEXT, email TEXT)"}}}
{"jsonrpc": "2.0", "id": 3, "method": "tools/call", "params": {"name": "list_tables", "arguments": {}}}
{"jsonrpc": "2.0", "id": 4, "method": "tools/call", "params": {"name": "insert_data", "arguments": {"query": "INSERT INTO users VALUES (1, 'Alice', 'alice@example.com')"}}}
{"jsonrpc": "2.0", "id": 5, "method": "tools/call", "params": {"name": "execute_query", "arguments": {"query": "SELECT * FROM users"}}}
EOF
```

```
# Working with an existing database file
cat << 'EOF' | tursodb mydb.db --mcp
{"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2024-11-05", "capabilities": {}, "clientInfo": {"name": "client", "version": "1.0"}}}
{"jsonrpc": "2.0", "id": 2, "method": "tools/call", "params": {"name": "list_tables", "arguments": {}}}
EOF
```

We'd love to have you contribute to Turso Database! Please check out the contribution guide to get started.

Turso powers production apps today. That includes Turso Cloud, the Kin AI assistant, and Spice.ai. However, it is still under active development and for mission-critical applications, caution is advised. Independent backups are encouraged. Turso is extensively tested by a collection of tools including a native Deterministic Simulation Testing suite and Antithesis, so we are generally confident in the end result. But our bar is SQLite-level reliability, and we will still recommend caution until we are confident it meets that bar.

Turso Database is a project to build the next evolution of SQLite in Rust, with a strong open contribution focus and features like native async support, vector search, and more. The libSQL project is also an attempt to evolve SQLite in a similar direction, but through a fork rather than a rewrite.

Rewriting SQLite in Rust started as an unassuming experiment, and due to its incredible success, replaces libSQL as our intended direction. At this point, libSQL is production ready, Turso Database is not - although it is evolving rapidly. More details here.

- Pekka Enberg, Sasu Tarkoma, Jon Crowcroft Ashwin Rao (2024). Serverless Runtime / Database Co-Design With Asynchronous I/O. In
*EdgeSys ‘24*. [PDF] - Pekka Enberg, Sasu Tarkoma, and Ashwin Rao (2023). Towards Database and Serverless Runtime Co-Design. In
*CoNEXT-SW ’23*. [PDF] [Slides] - Alperen Keles, Ethan Chou, Harrison Goldstein, Leonidas Lampropoulos (2026). DIRT: Database-Integrated Random Testing. In
*DBTest '26*. [PDF]

This project is licensed under the MIT license.

Unless you explicitly state otherwise, any contribution intentionally submitted for inclusion in Turso Database by you, shall be licensed as MIT, without any additional terms or conditions.

Thanks to all the partners of Turso!

Thanks to all the contributors to Turso Database!