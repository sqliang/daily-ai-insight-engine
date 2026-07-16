---
title: SQLite should have (Rust-style) editions
source: https://mort.coffee/home/sqlite-editions/
author:
- '[[gnyeki]]'
published: '2026-07-15'
created: '2026-07-16'
manifest_dates:
- '2026-07-16'
description: 'Article URL: https://mort.coffee/home/sqlite-editions/ Comments URL:
  https://news.ycombinator.com/item?id=48928135 Points: 266 # Comments: 106'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: c9f6eb2af9ad4ae5
source_type: community_discussion
tldr: 文章批判 SQLite 的默认配置存在四大问题：外键约束默认关闭、列类型检查不严格、并发写入默认立即返回 SQLITE_BUSY 错误、以及写性能优化选项默认未启用。作者借鉴
  Rust 的 edition 机制，提议 SQLite 引入版本化系统来渐进改进默认行为而不破坏向后兼容性。
objective_summary: Morten Hustveit 在个人博客中指出 SQLite 的默认设置有四大缺陷：外键约束默认不启用（需 PRAGMA foreign_keys
  = ON），结合 ROWID 重用机制可能导致数据被静默关联到错误行；列类型使用"类型亲和性"而非严格检查，允许将文本值存入 INTEGER 列，虽从 3.25
  版本支持 STRICT 表但需逐表手动声明；多进程并发写入时默认立即返回 SQLITE_BUSY 而非等待锁释放（需 PRAGMA busy_timeout =
  5000）；默认使用回滚日志而非 WAL 模式导致写入性能不佳（需 PRAGMA journal_mode = WAL）。作者认为这些违反直觉的默认值持续导致真实项目中的
  Bug，提议 SQLite 借鉴 Rust 的 edition 机制，通过版本化方式渐进改进默认行为。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - SQLite
  - ROWID
  - WAL
  - RDBMS
  - PRAGMA
  - BLOB
  - CREATE DOMAIN
  key_people:
  - Sylvain Kerkour
  - masklinn
  - zie
key_logic_flow:
- SQLite 默认不启用外键约束（需 PRAGMA foreign_keys = ON），结合 ROWID 重用机制，删除用户后其帖子可能被静默关联到新用户的同名
  ID 上，产生数据完整性问题。
- SQLite 使用"类型亲和性"而非严格类型检查，允许将 TEXT 值插入 INTEGER 列，虽从 3.25.0 版本支持 STRICT 表但需逐表手动声明添加
  strict 关键字，没有全局启用选项。
- 多进程并发写入时 SQLite 默认立即返回 SQLITE_BUSY 错误而非等待锁释放，作者建议设置 PRAGMA busy_timeout = 5000 让
  SQLite 尝试最多 5 秒后报错。
- SQLite 默认使用回滚日志模式（rollback journal），作者建议启用 WAL 模式（PRAGMA journal_mode = WAL）并配合
  synchronous = NORMAL 以大幅提升写入性能。
- 作者借鉴 Rust 的 edition 机制，提议 SQLite 引入版本化系统来渐进改进默认行为，每次新 edition 都启用更好的默认值，同时保留旧 edition
  以保持向后兼容性。
object_mentions:
- object_type: project
  name: SQLite
  canonical_name: SQLite
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 文章以 SQLite 为核心分析对象，详细讨论其默认配置的四大缺陷及改进方案。
  - 文章提议 SQLite 借鉴 Rust 的 edition 机制来版本化地改进默认行为。
  - 文章引用 SQLite 官方文档和 SQLite 作者关于灵活类型偏好的论述作为论据。
  article_id: c9f6eb2af9ad4ae5
- object_type: project
  name: lobste.rs
  canonical_name: lobste.rs
  url: https://lobste.rs
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 文章提到 lobste.rs 正在使用 SQLite 作为数据库。
  - 文章引用 lobste.rs 用户 'zie' 和 'masklinn' 对 SQLite 严格表和 CREATE DOMAIN 的评论作为论据。
  article_id: c9f6eb2af9ad4ae5
extract_result: success
impact_score:
  score: 5.5
  reason: 该文章是一篇社区博客，非官方公告。SQLite 作为全球部署最广的数据库引擎，其默认配置问题长期存在且有实际影响（外键忽略、类型亲和性、并发写入失败等）。作者提出的
    Rust-style edition 机制是一个有创见的治理方案，但并非技术范式突破。文章质量扎实、论据充分，但本质是对已知问题的系统性梳理与改进提案，影响力局限于
    SQLite 生态内讨论层面，不足以改变行业格局。
sentiment: mixed
developer_sentiment:
  tone: skeptical
  primary_focus: SQLite 官方是否愿意打破极致向后兼容的惯例来采纳 edition 机制
hype_assessment:
  level: low
  reason: 文章没有任何 PR 话术，不使用'颠覆'、'革命性'等夸张词汇。每个论点都附有完整的 SQL 示例和问题复现场景，论证逻辑严谨。作者承认 SQLite
    的优异特性（嵌入式、自包含、行业标准），同时建设性批评默认配置，内容扎实、态度克制，属于技术社区高质量讨论。
information_entropy: high
domain_disruption:
  technical_innovation: 将 Rust edition 的语义化版本治理模式引入数据库领域，为 SQLite 默认行为的渐进式改进提供了一条不破坏向后兼容的可行路径。核心洞察是：数据库的默认值也是
    API 的一部分，需要版本化治理。
  business_model: 无
engineering_complexity: conceptual
compound_value:
  score: 3.5
  reason: 该提议本身合理且直击 SQLite 长期存在的四项默认行为痛点（外键忽略、类型亲和性宽松、并发写入立即报错、非 WAL 模式），借鉴 Rust
    edition 机制的渐进式改进方案具有工程智慧。若被 SQLite 官方采纳，将系统性改善全球最广泛部署数据库的数据完整性，减少大量生产环境 Bug。但当前仅为一篇个人博客的技术建议文，并非
    SQLite 核心团队路线图或 RFC 提案，实际采纳概率与时间表高度不确定。从 VC 视角看，SQLite 已占据嵌入式数据库霸主地位，该改进是对成熟基础设施的增量优化，不创造新市场或新价值捕获渠道，无法形成可投资的正反馈循环，复利效应微弱。
value_capture_layer: agent_middleware
moat_impact: strengthens_monopoly
key_beneficiaries:
- SQLite 项目社区
- Turso
competitive_casualty:
- DuckDB
- 嵌入式数据库替代方案
market_opportunities:
- 开发者可开发 SQLite 配置审计与自动修复工具（类似 linter），检测并自动补全缺失的 PRAGMA 设置，服务于百万级 SQLite 存量项目
- ORM 和数据库驱动库（如 SQLAlchemy、Prisma、Drizzle）可将文章提到的安全 PRAGMA（foreign_keys=ON、busy_timeout、WAL）纳入默认模板，作为差异化竞争力
- 基于 SQLite 的托管数据库服务或边缘数据库产品可以将"安全默认值"作为核心卖点，对标 Firebase、Turso 等竞品的默认行为
risk_matrix:
  regulatory: 若 SQLite 用于医疗（HIPAA）、金融（SOX）等对数据完整性有严格合规要求的场景，默认关闭外键和宽松类型检查可能导致数据损坏进而引发合规审查
  technological: SQLite 核心团队以保守和兼容性优先著称，edition 提案可能需要多年才能落地或最终被否决；同时 libSQL、DuckDB
    等竞品已在默认安全方面走在前列
  competitive: DuckDB 在嵌入式分析场景快速增长且默认配置更严谨，libSQL（Turso）正在分叉 SQLite 并引入更激进的默认行为改进，可能逐步侵蚀
    SQLite 的传统优势领域
  ethical: 默认配置可导致数据静默关联错误（ROWID 重用+无外键约束）、类型错误数据被悄无声息存入，这些缺陷影响了数亿终端设备上依赖 SQLite 的应用的数据可靠性和用户信任
  additional:
  - SQLite 的极端广泛部署（每个智能手机、浏览器、车载系统）意味着任何默认行为变更的向后兼容性挑战和迁移成本极其巨大，核心团队对此极为审慎
confidence:
  impact: medium
  compound: low
  hype: low
actionable_insight: monitor
object_insights:
- object_type: project
  name: SQLite
  canonical_name: SQLite
  url: https://www.sqlite.org
  positioning: 全球部署最广泛的嵌入式 SQL 数据库引擎，以库的形式嵌入应用程序而非独立的客户端-服务器进程，在嵌入式系统、移动应用、浏览器及服务器软件中作为本地数据存储的事实标准。
  technical_signal: 文章系统性地指出 SQLite 默认配置存在四大技术债务：(1) 外键约束默认关闭，结合 ROWID 重用机制可能导致数据静默关联到错误行，构成数据完整性问题；(2)
    类型亲和性（type affinity）而非严格类型检查，允许 TEXT 值存入 INTEGER 列，3.25 版本后虽支持 STRICT 表但需逐表手动声明；(3)
    多进程并发写入时默认立即返回 SQLITE_BUSY 而非等待锁释放；(4) 默认使用回滚日志模式（rollback journal）而非 WAL 模式，写入性能不佳。作者借鉴
    Rust 的 edition 机制提议引入版本化系统来渐进改善默认行为，每次新 edition 启用更好的默认值，同时保留旧 edition 保证向后兼容。从
    3.25 版本支持的 STRICT 表已证明 SQLite 有改进方向但缺乏全局切换机制。
  adoption_signal: SQLite 是嵌入式数据存储的行业标准，被无数嵌入式项目、移动应用、浏览器及桌面软件采用。文章还提到 lobste.rs 等服务器端软件也开始使用
    SQLite，印证了其在服务端场景的扩展趋势。
  ecosystem_relevance: 作为基础设施级项目，SQLite 的默认行为直接影响数万个下游应用的数据完整性和正确性。edition 机制如果被采纳，将根本性地改变
    SQLite 的演进模式与向后兼容策略，影响整个嵌入式数据库生态系统的开发实践。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 文章提出的 edition 机制是 SQLite 演进思路的重要信号——如果 SQLite 社区或 D. Richard Hipp
    对此持开放态度，将开启 SQLite 的一项重大治理变革，从根本上解决长期存在的默认值陷阱问题，影响所有 SQLite 用户的最佳实践。
  risk_notes:
  - SQLite 项目以保守设计著称（创始人 D. Richard Hipp 对灵活类型有明确偏好），edition 机制需要核心团队认同和社区广泛支持
  - 多个 edition 并存可能增加维护复杂度和测试负担
  - edition 迁移路径的设计本身需要严谨的兼容性考量
  score: 8.0
  article_ids:
  - c9f6eb2af9ad4ae5
  evidence_snippets:
  - 文章以 SQLite 为核心分析对象，详细讨论其默认配置的四大缺陷及改进方案。
  - 文章提议 SQLite 借鉴 Rust 的 edition 机制来版本化地改进默认行为。
  - 文章引用 SQLite 官方文档和 SQLite 作者关于灵活类型偏好的论述作为论据。
  - Foreign key constraints are ignored by default — 结合 ROWID 重用导致数据被静默关联到错误行。
  - Columns can store the wrong data type — 类型亲和性允许 TEXT 存入 INTEGER 列。
  - No busy timeout — 多进程并发时默认立即返回 SQLITE_BUSY。
  - No WAL mode — 默认回滚日志模式写入性能差，需手动启用 WAL + synchronous = NORMAL。
- object_type: project
  name: lobste.rs
  canonical_name: lobste.rs
  url: https://lobste.rs
  positioning: 面向程序员的社交新闻聚合与讨论平台，类似于 Hacker News 但采用更细粒度的标签分类和邀请制注册，社区规模较小但用户参与质量较高。
  technical_signal: lobste.rs 在生产环境中使用 SQLite 作为数据库，这在传统上以 PostgreSQL/MySQL 为主的 Web
    服务端点中较为少见，体现了 SQLite 在中等规模服务端场景的应用可行性。
  adoption_signal: 在技术社区中具有良好口碑，但用户规模有限，属于小众高质社区。其 SQLite 采用的实践经验可能影响其他中小型 Web 项目的数据库选型决策。
  ecosystem_relevance: 作为 SQLite 服务端部署的实际案例，lobste.rs 的经验直接关联到 SQLite 在服务器场景的适用性讨论。文章引用其用户评论（关于
    STRICT 表和 CREATE DOMAIN）作为论据，说明社区对 SQLite 默认行为的关注。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 作为生产环境使用 SQLite 的服务端案例，lobste.rs 的实际运行经验可为 SQLite 服务端部署提供参考，其社区讨论也对
    SQLite 改进有反馈价值。
  risk_notes:
  - 社区规模较小，技术信号的普适性有限
  - 作为参考引用对象，文章未提供其 SQLite 使用的性能或可靠性数据
  score: 3.0
  article_ids:
  - c9f6eb2af9ad4ae5
  evidence_snippets:
  - 文章提到 lobste.rs 正在使用 SQLite 作为数据库。
  - 文章引用 lobste.rs 用户 'zie' 和 'masklinn' 对 SQLite 严格表和 CREATE DOMAIN 的评论作为论据。
  - Some server software even uses it; for example, lobste.rs is now running on SQLite.
---

Date: 2026-07-15

Git: https://gitlab.com/mort96/blog/blob/published/content/00000-home/00017-sqlite-editions.md

SQLite is an amazing database engine. I use it as a database for plenty of embedded projects, and I don't think it's an exaggeration to call it the industry standard for local data storage. Some server software even uses it; for example, lobste.rs is now running on SQLite.

Unlike traditional RDBMSes (Relational DataBase Management Systems), SQLite is not a separate process; it's an RDBMS as a library, meaning your software remains self contained. Unlike traditional file formats, you don't need to write custom serializers and parsers. In some ways, it's the best of both worlds.

There's just one huge problem though. Its defaults are all wrong.

## Bad default #1: Foreign key constraints are ignored by default

You read that right. Foreign key constraints are arguably the primary tool we have to ensure that a database remains consistent and don't have dangling references.

As a quick primer, this is how an SQL foreign key constraint looks:

```
CREATE TABLE users (
id INTEGER PRIMARY KEY,
display_name TEXT
);
CREATE TABLE posts (
id INTEGER PRIMARY KEY,
user_id INTEGER NOT NULL,
content TEXT NOT NULL,
FOREIGN KEY(user_id) REFERENCES users(id)
);
```


The typical behavior for all other RDBMSes would be that the `user_id`

column
of a post must *always* reference the ID of a valid user.
You can't create a new post without providing a valid user ID,
you can't delete a user without also deleting its posts,
lest you get a foreign key constraint violation error.

The only RDBMS I'm aware of which doesn't enforce this by default is SQLite.

This is made even worse by SQLite's tendency to re-use `ROWID`

.
You see, in this example, those `INTEGER PRIMARY KEY`

rows become aliases
for the table's `ROWID`

, which is a unique integer ID assigned to every row
of a table in SQLite.
The algorithm for assigning `ROWID`

is a bit complicated
(more details in the SQLite documentation),
but it results in ID re-use in some cases.
This means that a dangling reference easily results in a reference to
the *wrong row*, which is even worse than a dangling reference because
everything will seem fine.
You don't even get an error during lookup.

Just look at this hypothetical sequence of operations in our toy database schema:

```
-- Bob creates a user account
INSERT INTO users (display_name) VALUES ('Bob');
SELECT * FROM users;
-- id | display_name
-- 1 | Bob
-- Bob posts an introduction post
INSERT INTO posts (user_id, content) VALUES (1, 'Hello, I am Bob');
SELECT u.display_name, p.content FROM users as u, posts as p WHERE u.id = p.user_id;
-- display_name | content
-- Bob | Hello, I am Bob
-- Bob deletes his account,
-- but we forgot to delete the posts.
-- SQLite doesn't produce an error because it ignores our foreign key.
DELETE FROM users WHERE id = 1;
-- Alice creates an account.
-- Alice gets the same ID that Bob had due to the ROWID algorithm.
INSERT INTO users (display_name) VALUES ('Alice');
SELECT * FROM users;
-- id | display_name
-- 1 | Alice
-- Alice has now inherited Bob's old post!
SELECT u.display_name, p.content FROM users as u, posts as p WHERE u.id = p.user_id;
-- display_name | content
-- Alice | Hello, I am Bob
```


The fix is to enable `foreign_keys`

with a pragma:

```
PRAGMA foreign_keys = ON;
```


If we had done this in the beginning,
the buggy `DELETE`

would have produced an error:

```
DELETE FROM users WHERE id = 1;
-- Runtime error: FOREIGN KEY constraint failed (19)
```


## Bad default #2: Columns can store the wrong data type

SQLite has a simple type system: a value can be `NULL`

, an `INTEGER`

,
a `REAL`

(aka a double precision float), `TEXT`

, or a `BLOB`

(aka binary data).
Consequently, a column can be defined to hold values of any of those types.

However, a column defined as an `INTEGER`

column isn't restricted to only integers;
instead, SQLite considers it to "use INTEGER affinity".
What this means is essentially:

- If you try to insert a
`TEXT`

value, and it is a valid string representation of an integer, it is converted to an integer and stored as such. - If you try to insert a
`TEXT`

value, and it is a valid string representation of a real number, it is converted to a real (aka double precision float) and stored as such. - Otherwise, the value is stored as-is.

Other affinities have different but simpler rules:

- Columns with
`BLOB`

affinity store values as-is. - Columns with
`TEXT`

affinity store`BLOB`

,`TEXT`

and`NULL`

values as-is, but convert numeric values to`TEXT`

. - Columns with
`REAL`

affinity work like columns with`INTEGER`

affinity except that integer values are converted to`REAL`

.

Here's how this looks in practice:

```
CREATE TABLE music (
id INTEGER PRIMARY KEY,
name TEXT,
duration_sec INTEGER
);
INSERT INTO music (name, duration_sec) VALUES ('Lost In Hollywood', 321);
INSERT INTO music (name, duration_sec) VALUES ('Comfortably Numb', 382);
INSERT INTO music (name, duration_sec) VALUES ('The Way of All Flesh', 'Way too long, I mean come on');
SELECT * FROM music;
-- id | name | duration_sec
-- 1 | Lost In Hollywood | 321
-- 2 | Comfortably Numb | 382
-- 3 | The Way of All Flesh | Way too long, I mean come on
```


I don't think I need to explain why it's a bad idea for a *database*
to be so careless about *data validation*.
It would be one thing if SQLite was an explicitly dynamically typed
document database, but it's not.
SQLite asks me through its syntax rules, "What type do you want to go into this column".

I once had to clean up a project where some code had accidentally been writing the
strings `'1'`

and `'0'`

to a column which was intended to store booleans (`1`

and `0`

).
That was not a fun debugging story.

Luckily, SQLite has the concept of strict tables, which makes SQLite produce a type error when the wrong type is inserted into a column:

```
CREATE TABLE music (
id INTEGER PRIMARY KEY,
name TEXT,
duration_sec INTEGER
) strict;
INSERT INTO music (name, duration_sec) VALUES ('The Way of All Flesh', 'Way too long, I mean come on');
-- Runtime error: cannot store TEXT value in INTEGER column music.duration_sec (19)
```


Unfortunately, there is no pragma to globally make all tables strict.
So you have to remember to add the `strict`

tag to every table manually.

There's a couple of arguments against strict tables which I want to cover here.

The authors of SQLite have written
about their preference for "flexible typing".
Personally, I find this a really strange piece of writing.
It doesn't provide any examples for why it could ever be useful to insert
a `BLOB`

into an `INTEGER`

column.
All it does is illustrate why it's sometimes useful to have a column
which can store values of any type.
Strict tables have a solution for that; it's called the `ANY`

data type.
You can still create columns which accept any value,
you just have to be explicit about it.

A much better argument
is provided by user 'zie' on lobste.rs.
You see, strict tables in SQLite don't just *enforce* types.
They also change the rules for how type specifiers are parsed.

Non-strict SQLite tables use the following rules to determine the type of a column (from SQLite's documentation):


- If the declared type contains the string "INT" then it is assigned INTEGER affinity.
- If the declared type of the column contains any of the strings "CHAR", "CLOB", or "TEXT" then that column has TEXT affinity. Notice that the type VARCHAR contains the string "CHAR" and is thus assigned TEXT affinity.
- If the declared type for a column contains the string "BLOB" or if no type is specified then the column has affinity BLOB.
- If the declared type for a column contains any of the strings "REAL", "FLOA", or "DOUB" then the column has REAL affinity.
- Otherwise, the affinity is NUMERIC.

A consequence of this rule, combined with SQLite's loose typing,
is that you can give your columns type names such as `DATETIME`

or `KEY_VALUE_SET`

or `COLOR`

,
and have a database connector/wrapper which automatically knows to
serialize and deserialize columns with custom types.
And if nothing else, those custom type names serve as useful documentation.

I have to acknowledge that just changing the default from non-strict tables to strict tables, with no further changes, would give up on this somewhat nifty quirk. However, I think we would be much better served by custom type aliases.

If we could write something like:

```
CREATE TYPE KEY_VALUE_SET = TEXT;
```


and then use `KEY_VALUE_SET`

as a type name in a strict table,
I think everyone would be happy.
I would probably start using such a feature liberally to document
the expected pattern of data in my columns.
In a real world schema,
you inevitably end up with `TEXT`

columns which have to be parsed
by application code.

As an aside to this aside, it would be neat if we could associate CHECK constraints with a custom type.


Update:'masklinn' on lobste.rs points out that the SQL 99 standard already specifies type aliases, called CREATE DOMAIN. This already supports constraints as well. So really, SQLite just needs to add support for the standard`CREATE DOMAIN`

statement.

## Bad default #3: SQLITE_BUSY errors with concurrent writers

SQLite allows multiple concurrent readers, but only one writer at a time.
By default, if you have two processes trying to acquire a write lock
at the same time, one of them will immediately receive an `SQLITE_BUSY`

error.

This is not the behavior I expect. I expect SQLite to wait for the lock to get unlocked, up to some timeout. It's doing disk IO after all, so I already structure my code with the assumption that a write could potentially be slow.

The default behavior has lead me to writing real-world bugs, where systems would sometimes just crash. I've manually written retry loops to fix it.

The fix is to set `busy_timeout`

with a pragma:

```
PRAGMA busy_timeout = 5000;
```


This makes SQLite try to acquire the lock for up to 5 seconds before erroring
with a `SQLITE_BUSY`

error.

I didn't learn about this setting until recently. It seems like such an obvious default that I'm astonished that it's not.


Update:I should add a note here about why support for concurrent writers is desirable.During normal operation, you're usually best served by structuring your software such that all writes are done by a single process, ideally a single thread. Concurrent writers will never be

fast. But there are non-typical situations. Maybe you need to manually clean up a database interactively using the`sqlite3`

tool interactively on the command line. Maybe you have scripts for uncommon administrative tasks which you haven't had the need to write a front-end for. These are perfectly legitimate and, I believe, fairly common use cases. I think it's bad that with SQLite's defaults, this kind use has a chance to just crash the software by making it throw an unexpected`SQLITE_BUSY`

error.

## Bad default 4: Performance

There's a lot to say about performance tuning in SQLite. When correctly configured, it can be a truly fast RDBMS, with the ability to fill roles we typically reserve for the big servers like PostgreSQL or MySQL.

But by default, its performance isn't great. Smarter people than me have written much more on this, and I recommend Sylvain Kerkour's Optimizing SQLite for servers if you're interested in this topic.

But the most significant bad default is that SQLite's Write-Ahead Log (WAL) is disabled by default. It can be enabled with:

```
PRAGMA journal_mode = WAL;
```


The WAL provides a dramatic write speed-up in most circumstances. Additionally, it lets us drastically reduce the amount of disk syncs without risking data corruption by changing another setting:

```
PRAGMA synchronous = NORMAL;
```


See the SQLite documentation on what exactly synchronous does.

## The solution: editions?

The oft-cited reason for why these defaults remain, well, default,
is of course backwards compatibility.
Changing defaults *now* would likely break lots of old software
and make people afraid to upgrade SQLite in the future in case it breaks everything again,
just like how I'm afraid to upgrade Python because every "upgrade"
breaks a bunch of software I use.
It's a laudbile and rare goal to try to not break your dependents.

However, I think the solution is simple: add one "super pragma" which changes all the bad defaults. I propose that the following:

```
PRAGMA edition = 2026;
```


should be an alias for at least the following set of pragmas:

```
PRAGMA foreign_keys = ON;
PRAGMA busy_timeout = 5000;
PRAGMA journal_mode = WAL;
PRAGMA synchronous = NORMAL;
```


And also make `strict`

mode the default for tables.

This should be a nice middle ground which avoids breaking backwards compatibility, but lets the database engine move forwards and not be bogged down by its own history.

The `edition`

idea is stolen straight from
Rust editions.
The advantage of a year-based edition rather than something like
JavaScript's `"use strict";`

is that as the years go by, the sensible defaults may change.
Maybe something like Hctree's WAL2
makes its way into the main branch, say, in the year 2034,
so maybe `PRAGMA edition = 2034`

will some day set `PRAGMA journal_mode = WAL2`

.

Anyway, that's all. I think SQLite should have an edition system with updated sets of defaults. Are there any things I've missed which makes this a bad idea? Or more pragmas which should be added to my imaginary "2026 edition"?