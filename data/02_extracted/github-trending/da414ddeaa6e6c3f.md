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
tldr: Turso 发布用 Rust 重写的 SQLite 兼容数据库，内置 MCP 服务器模式
objective_summary: Turso 团队正式发布 Turso Database（Beta 阶段），这是一款用 Rust 编写的进程内 SQL 数据库，兼容
  SQLite 的文件格式、SQL 方言和 C API。该数据库支持 MVCC 提升写入吞吐、CDC 实时变更捕获、io_uring 异步
event_type: infrastructure_update
epistemic_status: verified_fact
entities:
  companies:
  - Turso
  technologies:
  - SQLite
  - Rust
  - MVCC
  - CDC
  - MCP
  - io_uring
  - WebAssembly
  - DBSP
  - tantivy
  - libSQL
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
- Turso Database 是一款用 Rust 编写的进程内 SQL 数据库，兼容 SQLite 的 SQL 方言、文件格式和 C API，目前处于 Beta
  阶段。
- 核心功能包括：MVCC（多版本并发控制）提升写入性能、CDC（变更数据捕获）实现实时数据库变更追踪、io_uring 异步 I/O（Linux）、向量搜索以及跨平台支持（含浏览器
  WebAssembly）。
- 实验性功能包括：静态加密、基于 DBSP 的增量计算、基于 tantivy 的全文搜索、以及通过 .tshm 侧车进程实现的多进程 WAL 协调。
- CLI 内置 MCP 服务器模式，提供 9 种数据库交互工具（打开数据库、列出表、描述表结构、执行查询、插入/更新/删除数据、模式变更），可与 Claude Code、Claude
  Desktop、Cursor 等 AI 客户端集成。
- 该项目替代了 libSQL 成为 Turso 的发展方向——libSQL 已生产就绪，Turso Database 尚在快速演进中，已用于 Turso Cloud、Kin
  AI 助手和 Spice.ai 等生产环境。
- 支持 Rust、JavaScript、Python、Go、.NET、Java 六种语言绑定，CLI 可通过 curl 一键安装或通过 Docker 运行。
extract_result: success
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