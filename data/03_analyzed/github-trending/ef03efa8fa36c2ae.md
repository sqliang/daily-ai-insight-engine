---
title: KnockOutEZ/wigolo
source: https://github.com/KnockOutEZ/wigolo
author: []
published: ''
created: '2026-07-19'
manifest_dates:
- '2026-07-19'
- '2026-07-20'
description: 'The go-to web for your AI coding agent — local-first search, fetch,
  crawl & research over MCP. No API keys, no cloud, $0/query. Public beta. Local-first
  web intelligence for AI agents — no keys, no cloud, no metered bill. works with&nbsp;&nbsp;Claude
  Code · Cursor · Codex · Gemini CLI · VS Code · Windsurf · Zed · Antigravity and
  beyond&nbsp;&nbsp;LangChain · CrewAI · LlamaIndex · Vercel AI SDK · n8n & self-hosted
  agents · any MCP client · plain REST Quickstart · Tools · Why wigolo · Benchmark
  · Docs · Examples · Feedback · FAQ wigolo gives an AI agent one durable surface
  for everything web-related — search, fetch, crawl, extract, cache, find-similar,
  research, and autonomous gather loops. It runs wherever your agent runs: as an MCP
  server next to your coding agent, as a REST/MCP endpoint on the box where your self-hosted
  agents live, or embedded through an SDK inside your own app. The core tools need
  no API keys, nothing it touches leaves ~/.wigolo/, and there''s no bill that grows
  with how much your agent thinks. Quickstart Requires Node ≥ 20 and ~1.5 GB of free
  disk. macOS, Linux, and Windows. One command wires the local engine into your agent.
  init is unattended by default — no prompts, safe in scripts and CI — and does the
  complete setup: it downloads the browser engine and on-device models, runs a health
  check, and prints a per-component summary, so any setup problem surfaces right here,
  not silently on your agent''s first call: npx wigolo init --agents=<your-agent>
  <your-agent> — one or more of claude-code · cursor · codex · gemini-cli · vscode
  · windsurf · zed · antigravity (comma-separated). wigolo writes the MCP config and
  instructions for you. Any other MCP client? Omit --agents and register npx -y wigolo
  yourself — the installation guide has the exact config block for every client, plus
  Docker, Homebrew, and single-file-binary channels. Prefer prompts? --interactive
  is a plain-text flow; --wizard is the full terminal TUI. Skip the downloads? --no-warmup
  defers everything to first use. A failed component download never fails setup —
  init reports what''s not ready with the exact fix and still wires your agent. That''s
  the whole setup — search, fetch, crawl, extract, cache, and find-similar work with
  no API key. Check it''s healthy anytime: npx wigolo doctor Not for you? npx wigolo
  config --uninstall --yes removes everything, cleanly. You can also paste the installation
  guide at any AI assistant and let it do the setup — it''s written to be self-contained.
  Recommended — a free key makes research & agent shine Search, fetch, crawl, extract,
  cache, and find-similar are fully keyless. But research, agent, and search format=answer
  use an LLM to write the synthesized, cited answer — without one they hand back a
  raw brief and evidence for your agent to assemble, which is a much thinner experience.
  A free Gemini key is all it takes, and it''s the single biggest quality upgrade
  you can make: export WIGOLO_LLM_PROVIDER=gemini export GEMINI_API_KEY=<free-key>
  # grab one at aistudio.google.com/apikey — the free tier is plenty Any provider
  works (anthropic · openai · groq), or stay fully local and keyless with WIGOLO_LLM_PROVIDER=ollama
  (or any OpenAI-compatible URL). Set it in your shell or your agent''s MCP env block.
  Providers, models, and the keyless local-model ladder: configuration guide. What
  your agent gets back Not snippets — evidence. Every search result carries a verbatim
  excerpt pinned to its exact position in the source, a citation ID the agent can
  quote, and a score it can inspect (abridged real shape): { "results": [{ "title":
  "Logical replication - PostgreSQL docs", "url": "https://www.postgresql.org/docs/current/logical-replication.html",
  "excerpt": "Logical replication is a method of replicating data objects…", "citation_id":
  "src-1", "source_span": { "start": 1042, "end": 1305 }, // byte-exact provenance
  "evidence_score": { "final": 0.86, "semantic": 0.91, "lexical": 0.78, "engine_consensus":
  3 } }], "citations": [{ "id": "src-1", "url": "…" }], "freshness_signal": { "published":
  "2026-05-12", "confidence": "high" } } Weak results get flagged as junk by wigolo''s
  own scorer, failed engines are reported, stale cache is labeled — the agent always
  knows what it''s standing on. Full response contracts per tool: tools reference.
  Tools Tool What it does 🔎 search Multi-engine web search (18 direct adapters) with
  rank fusion, ML reranking, and an explainable per-result score. Pass a query array
  for parallel breadth. 📄 fetch Load one URL through a tiered router that auto-escalates
  from plain HTTP to a headless browser engine on anti-bot challenges or SPA shells.
  Clean markdown + metadata + links. 🕸️ crawl Multi-page crawl — BFS, DFS, sitemap,
  or map-only. Per-domain rate limits, robots.txt respect, boilerplate dedup. 🧩 extract
  Structured data from a page: tables, metadata, JSON-LD, brand identity, named schemas
  (Article / Recipe / Product / …), or any custom JSON Schema. 💾 cache Query everything
  already seen — keyword or hybrid semantic. Plus stats, clear, and change detection.
  🧲 find_similar Pages similar to a URL or a concept, via 3-way fusion of keyword
  + semantic + live web. 🧠 research Decompose a question → fan out sub-queries → fetch
  sources → synthesize a cited report (or a structured brief the host LLM writes from).
  🤖 agent Autonomous gather loop: plan → search → fetch → extract → synthesize, with
  a step log, time budget, and optional output schema. 🔁 diff + ⏱️ watch See exactly
  what changed on a page since last visit; re-check on demand and deliver changes
  to a webhook. Every tool also runs from the terminal (wigolo search "…" --json),
  from an interactive shell with NDJSON piping (wigolo shell), over REST, and through
  the SDKs — CLI reference. What that actually lets you do Each tool goes well past
  its one-liner. A sampler — every line links to the guide and, where there''s one,
  a runnable example: Search that fans out — pass a query array for parallel breadth,
  scope to include_domains, bound by time_range/recency, exact-phrase match, choose
  a depth tier, even image results. → guide · example Fetch almost anything — JS-rendered
  SPAs, PDFs, a single heading section, authenticated pages (via a browser profile
  or remote browser), or drive the page with actions (click / type / scroll / screenshot).
  → guide Crawl a whole site — sitemap, BFS, DFS, or map-only; robots.txt-respecting,
  per-domain rate-limited, boilerplate-deduped. → guide Extract structure — tables,
  JSON-LD, metadata, brand assets, named schemas (Article / Recipe / Product / …),
  or your own JSON Schema. → guide A memory that compounds — every page is cached;
  re-query by keyword or meaning, instantly and offline; detect what changed since
  last visit. → guide · example Research & autonomous gather — decompose a question
  into a cited brief, or turn agent loose to plan → fetch → extract → synthesize against
  a JSON Schema and a time budget. → guide · example Watch & diff — monitor a URL,
  get a change report, deliver it to a webhook. → guide · example Drive it your way
  — one-shot CLI, an NDJSON shell for pipelines, REST, SDKs, or as skills your agent
  installs. → CLI & shell · example Extend it — add a search engine or a site extractor
  as a plugin in ~100 lines. → plugins · example Tune & inspect — wigolo tune shows
  what it learned per domain (which fetch tier, challenge clearances, backoff); doctor
  / verify health-check every component. → CLI · troubleshooting Why it''s different
  wigolo isn''t the free stand-in you settle for until the budget clears — it''s built
  to hold the same line as the paid services in this lane, and it brings receipts.
  What actually separates it: Built for agents, not humans. One MCP call fans out
  many queries across many engines in parallel — something a serial host tool-loop
  can''t replicate — with transparent per-result scoring and budget-aware output.
  Honest output. Stale cache, failed fetches, degraded backends, and truncation are
  surfaced in the result, never disguised as empty-but-successful data. When a bot-protected
  page can''t be read, you get a labeled blocked_by_challenge failure — never a challenge
  shell dressed up as content. $0 per query, free to re-query. Default search talks
  to public engines through direct adapters; the reranker and embeddings run on-device.
  Every response is cached, so asking again is instant and costs nothing. Private
  by default. Cache, embeddings, models, and config live under ~/.wigolo/. Nothing
  reaches a third party unless you explicitly opt into an LLM for synthesis. wigolo
  is a focused web layer for your agents — not a hosted SaaS, a vector database other
  apps query, or a scale-scraping platform. Within that lane it goes toe-to-toe with
  the paid services on result quality — and the meter, the key, and the data-egress
  simply aren''t there. Here''s what one real result looks like, dissected — including
  the failed engine and the weak result, because those are part of the answer too:
  Benchmark All four tools converged on the same core answer — and only one of them
  handed back verbatim, byte-pinned evidence while doing it. One cold query, run live
  inside a single Claude Fable 5 session and fanned out to four web tools on equal
  footing — built-in WebSearch, wigolo, Tavily, and Exa — then reported by the agent
  itself under one rule: judge on the evidence alone, no favoritism. All four converged
  on the same answer and the same top source — parity demonstrated, not asserted.
  wigolo alone returned verbatim excerpts pinned to byte-offset source spans, an explainable
  score decomposition, and live per-engine telemetry — and when two of its results
  were weak, its own scorer flagged them as junk on-screen. The cloud tools earn their
  line too: Exa rendered the official docs'' comparison matrix in full. One honest
  query, not a leaderboard — run your own and you''ll see the same shape. Same fight,
  different physics wigolo Firecrawl Exa Tavily Multi-engine web search ✅ ✅ ✅ ✅ Fetch
  & structured extraction ✅ ✅ ✅ ✅ Whole-site crawl & map ✅ ✅ — ✅ Verbatim excerpts
  pinned to byte-offset source spans ✅ — — — Explainable per-result score decomposition
  ✅ — — — Persistent local memory — re-query instantly, offline ✅ — — — Query data
  stays on your machine ✅ — — — API key / account none required required required
  Cost per query $0 metered metered metered Feature standing as of July 2026 — check
  each vendor''s docs for current state. That last row is the one that compounds —
  agents don''t ask once, they ask in bursts: Beyond your editor The same ten tools
  serve every kind of agent, over whichever surface fits — MCP for coding agents,
  REST for everything else, SDKs to embed, framework wrappers to drop in. REST API
  — wigolo serve One process exposes a plain-JSON REST API next to the MCP transport.
  No MCP client needed — just curl: wigolo serve # 127.0.0.1:3333 — loopback is open;
  off-loopback requires a token curl -sX POST http://127.0.0.1:3333/v1/search \ -H
  ''Content-Type: application/json'' \ -d ''{"query":"local-first software","max_results":5}''
  POST /v1/{tool} covers all ten tools, GET /openapi.json is the OpenAPI 3.1 contract,
  and /mcp + /sse serve remote MCP clients from the same port. Bind past loopback
  and a bearer token is required — the server fails closed rather than opening wide
  by accident. Point n8n, a Hermes-style assistant, or any self-hosted agent at it.
  → REST API SDKs — TypeScript & Python Thin, typed clients with an embedded local
  mode that finds or starts the daemon for you — no separate serve step. TypeScript
  — npm install wigolo-sdk (zero-dep; Node / Bun / Deno / edge): import { createLocalClient
  } from ''wigolo-sdk/local''; const { client, close } = await createLocalClient();
  // reuse a running daemon, or spawn one const res = await client.search({ query:
  ''local-first web search'', max_results: 5 }); console.log(res.results.map((r) =>
  r.title)); await close(); // stops the daemon only if this call spawned it Python
  — pip install wigolo (standard library only; sync + async): from wigolo import local_client
  with local_client() as client: # reuse a healthy daemon, or spawn one res = client.search(query="local-first
  web search", max_results=5) for r in res["results"]: print(r["title"], r["url"])
  → SDKs & embedded mode Framework integrations Drop wigolo''s tools into the framework
  you already use — the full ten-tool surface, including the cache / find_similar
  / research / agent that most framework web-tools don''t ship: Framework Package
  What you get LangChain wigolo-langchain each tool as a BaseTool, plus a BaseRetriever
  over search / find_similar for RAG CrewAI wigolo-crewai wigolo_tools() → hand the
  set to any crew LlamaIndex wigolo-llamaindex a BaseReader that loads fetched / crawled
  / searched pages as documents Vercel AI SDK wigolo-vercel-ai-sdk tool factories
  for generateText / streamText, edge-friendly → Framework integrations Docker # stdio
  MCP — wire it into any MCP client as command: docker docker run -i --rm -v wigolo-data:/data
  ghcr.io/knockoutez/wigolo # HTTP server for remote / multi-client use docker run
  -p 3333:3333 -v wigolo-data:/data \ -e WIGOLO_API_TOKEN=a-long-random-secret \ ghcr.io/knockoutez/wigolo
  serve --host 0.0.0.0 The slim image lazy-loads models into the volume; :full preinstalls
  the browser engine. Also on Docker Hub as towhid69420/wigolo. → installation & all
  channels Agent skills An 11-pack skill catalog teaches your coding agent to drive
  each tool well — installed by init, managed with wigolo skills add|list|remove.
  → skills One honest note for self-hosters: some challenge-protected sites score
  IP reputation, so a datacenter IP won''t clear walls a home connection would. wigolo
  labels those failures instead of faking them, and the self-hosting guide covers
  the opt-in proxy answer. Star history Live chart — it updates itself. If it''s still
  climbing when you read this, add a ⭐. Architecture A single Node process speaking
  MCP (JSON-RPC over stdio). Everything heavy is local and lazy-loaded, so a zero-key
  install pays nothing for the parts it isn''t using. flowchart TD A["🤖 AI agent<br/>any
  MCP client · REST · SDK"] A -->|MCP over stdio| B["<b>wigolo</b><br/>10 tools ·
  dynamic instructions<br/>in-process browser pool + cache + models"] B --> C{"Tool
  layer"} C --> T1["search · fetch · crawl · extract"] C --> T2["cache · find_similar
  · research · agent"] T1 --> F["⚙️ Fetch router<br/>tiered escalation, learned per
  domain"] T1 --> S["⚙️ Search<br/>18 engines → rank fusion → ML rerank<br/><i>explainable
  evidence score</i>"] T2 --> DB[("🗄️ Local cache<br/>keyword + vector index")] T2
  --> ML["🧠 On-device ML<br/>embeddings + reranker"] F -.->|optional| LLM["☁️ LLM<br/>synthesis
  only · opt-in"] S -.->|optional| SX["🔀 Aggregator backend<br/>opt-in legacy / hybrid"]
  F --> WEB["🌍 Public web"] S --> WEB style B fill:#7c3aed,stroke:#5b21b6,color:#fff
  style WEB fill:#0ea5e9,stroke:#0369a1,color:#fff style DB fill:#1e293b,stroke:#334155,color:#fff
  style LLM stroke-dasharray: 5 5 style SX stroke-dasharray: 5 5 Code beats model.
  Deterministic work — canonicalization, rank fusion, dedup, schema matching — never
  touches an LLM. The model is reserved for judgment, opt-in, and capped per request;
  LLM-filled fields are checked against the source and nulled if absent. Routing on
  observable signals. The fetch ladder escalates to a real browser on what it sees
  — SPA markers, challenge bodies, thin content — not domain guesses. It learns per
  domain, unlearns when a site stops needing it, and wigolo tune list shows you exactly
  what it learned. Reads pages the way a browser does — and says so when it can''t.
  Tiered fetching waits out interstitial challenges and reuses clearances per domain,
  politely: robots.txt respected, per-domain rate limits, research-grade volumes.
  When a wall stays up, the failure is labeled, never disguised. Configuration A clean
  install works out of the box. Three settings meaningfully raise output quality:
  # 1. Synthesis — the biggest lever (research / agent / search-answer write real
  prose) export WIGOLO_LLM_PROVIDER=gemini # or anthropic / openai / groq / ollama
  (keyless) export GEMINI_API_KEY=<your-key> # 2. Wider retrieval funnel export WIGOLO_SEARCH=hybrid
  # core engines + aggregator fallback export WIGOLO_GITHUB_TOKEN=... # GitHub code
  search 10 → 30 req/min # 3. Land more fetches, stay warm export WIGOLO_TLS_TIER=auto
  # per-domain learned fetch hardening export WIGOLO_EAGER_WARMUP=1 # pay the ~1s
  model load up front Per-call habits that pay off: query arrays (["a","b","c"]) for
  parallel breadth · search_depth: "deep" for queries that matter · include_domains
  as a hard filter for docs lookups. The full reference — every environment variable,
  config-file key, search backend, cache TTL, and serve limit — lives in the configuration
  guide. Docs & examples docs/ — the complete manual: getting started · installation
  & channels · configuration · tools reference · CLI & shell · REST API · SDKs & integrations
  · self-hosting · agent skills · plugins · troubleshooting & FAQ · privacy & security
  examples/ — runnable, each with a README (and most with a terminal recording): one-shot
  CLI, NDJSON shell pipelines, REST via curl, TypeScript & Python SDKs, Vercel AI
  SDK tools, pointing self-hosted n8n at a remote wigolo, watch-with-webhook, and
  writing your own search-engine plugin. Docs are also rendered on the site: knockoutez.github.io/wigolo/docs.
  Beta & feedback wigolo is in public beta. Everything documented here works and is
  held to a 7,600-test suite — beta is about the polish bar, not stability. It stays
  beta until enough people have used it, kicked it, and starred it that calling it
  v1 means something. That makes your feedback the whole game right now. Every report
  is read, usually the same day: 🐛 Report a bug — broke, misbehaved, surprised you
  💡 Request a feature — something it should do 💬 Ask anything — questions, setups,
  show & tell And if wigolo earns a place in your setup, the ways to keep it alive:
  a ⭐ star (it''s how open source gets found), a ☕ coffee (there''s no paid tier and
  never will be), or just an email — it goes straight to the one developer who wrote
  the code. FAQ Free? What''s the catch? No catch by design. The expensive parts —
  ranking, embeddings, the browser engine — run on your hardware, so there''s no per-query
  cost to recover and no reason for a meter. Sustained by donations; the AGPL license
  legally prevents a bait-and-switch into a closed hosted product. Is the quality
  really on par with the paid services? Run one query and judge — the benchmark section
  above is a live 4-way run, not a chart. Everyday agent queries land at parity; the
  paid tools still win some deep-extraction edge cases, and crawling is where wigolo
  is strongest. Every result shows its scoring, so you don''t have to take anyone''s
  word for it. Won''t public search engines block or rot? It''s engineered for exactly
  that: 18 engines fused with rank fusion (any one failing barely moves results),
  a tiered fetch ladder with per-domain learning, and an optional aggregator fallback.
  Degraded backends are reported in the output, never hidden — and the local cache
  means everything already seen keeps working regardless. Is this kind of scraping
  OK? wigolo reads the public web the way a browser does — robots.txt respected by
  default, per-domain rate limits, research-grade volumes for one agent on one machine.
  It''s deliberately the polite end of the spectrum, not a harvesting platform. AGPL
  — can I use this at work? Yes, freely, company-wide. The license only bites if you
  modify wigolo and run it as a network service — then you must publish those modifications.
  Using it as a local dev tool carries zero obligation. Commercial-licensing questions:
  reach out. Why 1.5 GB of disk? That''s the on-device brain: a full browser engine
  plus the ranking and embedding models the cloud services run on their side and bill
  you for. Disk is cheap; meters aren''t. Available on npm — wigolo (primary channel
  — the Quickstart above) PyPI — wigolo (Python SDK) Docker — ghcr.io/knockoutez/wigolo
  · towhid69420/wigolo Official MCP Registry — io.github.KnockOutEZ/wigolo Directories
  — Glama · Smithery · mcp.so · LobeHub Homebrew, curl | sh, and the single-file binary
  are covered in the installation guide — one channel per machine; they all share
  ~/.wigolo. Contributing Bug reports, feature requests, and PRs are all welcome —
  see CONTRIBUTING.md. Keep tool handlers thin, add tests, run the suite before opening
  a PR. The friendliest entry point: wigolo has a plugin system for custom search
  engines and extractors — add a search engine in ~100 lines, template in examples/plugin-search-engine.
  License GNU AGPL-3.0-only. Free to use, modify, and self-host — including inside
  a company. The one obligation: if you run a modified version as a network service,
  you must publish your modified source under the same license. That keeps wigolo
  open while preventing a closed, hosted fork. See SECURITY.md to report a vulnerability
  and TRADEMARK.md for use of the name. For commercial-licensing questions, reach
  out. wigolo is free and meant to stay that way — maintained, not paywalled. If it
  saves you a metered search bill, a ⭐, a sharp issue, or a ☕ coffee helps keep it
  sustainable. Built and maintained by @KnockOutEZ · ktowhid20@gmail.com'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: ef03efa8fa36c2ae
source_type: community_discussion
tldr: KnockOutEZ 发布了 wigolo，一个本地优先、无需 API 密钥的 AI 代理网络智能工具，提供搜索、抓取、提取、缓存等十种工具，通过 MCP、REST
  和 SDK 三种方式与各类 AI 编码代理集成，所有数据默认存储在本地 ~/.wigolo/ 目录下。
objective_summary: KnockOutEZ 在 GitHub 上发布了 wigolo，一个面向 AI 代理的本地优先网络智能工具。它提供搜索、抓取、提取、缓存、研究等十种工具，核心功能无需
  API 密钥即可使用。用户通过一条命令 npx wigolo init 即可完成安装配置，支持 Claude Code、Cursor、Codex 等主流 AI
  编码代理的 MCP 集成。所有缓存、嵌入向量、模型和配置默认存储在本地 ~/.wigolo/ 目录下，不向第三方发送数据。文章通过与 Firecrawl、Exa、Tavily
  的对比测试，展示了 wigolo 在逐字节引证摘录、可解释评分分解和本地持久化记忆方面的差异化优势。
event_type: framework_tools
epistemic_status: pr_statement
entities:
  companies:
  - KnockOutEZ
  - LangChain
  - CrewAI
  - LlamaIndex
  - Vercel
  - n8n
  - Firecrawl
  - Exa
  - Tavily
  technologies:
  - MCP
  - REST
  - SDK
  - BFS
  - DFS
  - TUI
  - OpenAPI
  key_people: []
key_logic_flow:
- KnockOutEZ 发布了 wigolo，一个面向 AI 代理的本地优先网络智能工具，核心功能无需 API 密钥。
- wigolo 提供搜索、抓取、提取、缓存、找相似、研究、自主代理、差异对比和页面监控等十种工具。
- 用户通过 npx wigolo init 命令一键安装，自动下载浏览器引擎和本地模型，并完成与指定 AI 代理的 MCP 配置。
- wigolo 支持 MCP 服务器、REST 端点和 SDK 三种集成方式，可接入 Claude Code、Cursor、Codex 等编码代理以及 LangChain、CrewAI、Vercel
  AI SDK 等框架。
- 所有缓存、嵌入向量、模型和配置存储在本地 ~/.wigolo/ 目录下，默认不向第三方发送任何数据。
- 与 Firecrawl、Exa、Tavily 的对比测试显示，wigolo 在提供逐字节引证摘录、可解释评分分解和本地持久化记忆方面具有独特优势。
object_mentions:
- object_type: project
  name: KnockOutEZ/wigolo
  canonical_name: wigolo
  url: https://github.com/KnockOutEZ/wigolo
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - wigolo 是一个本地优先的 AI 代理网络智能工具，核心功能无需 API 密钥，支持搜索、抓取、提取和缓存等操作。
  - 它通过 MCP 服务器、REST 端点和 SDK 三种方式集成到 Claude Code、Cursor、Codex 等主流 AI 编码代理中。
  - wigolo 的全部缓存、嵌入向量和配置均存储在本地 ~/.wigolo/ 目录下，默认不向任何第三方发送用户数据。
  article_id: ef03efa8fa36c2ae
- object_type: product
  name: Firecrawl
  canonical_name: Firecrawl
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - 文章将 wigolo 与 Firecrawl 进行对比，指出 Firecrawl 同样支持多引擎搜索、页面抓取和结构化提取功能。
  - 与 wigolo 不同，Firecrawl 需要 API 密钥并按查询计费，且不提供本地持久化记忆和离线查询能力。
  article_id: ef03efa8fa36c2ae
- object_type: product
  name: Exa
  canonical_name: Exa
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - 文章在对比表中指出 Exa 需要 API 密钥并按查询计费，但能完整呈现官方文档的比较矩阵。
  - Exa 与 wigolo 一样支持多引擎搜索和结构化提取，但不提供字节级引证摘录和本地离线查询能力。
  article_id: ef03efa8fa36c2ae
- object_type: product
  name: Tavily
  canonical_name: Tavily
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - 文章将 Tavily 列为对比对象之一，指出其需要 API 密钥且按使用量计费。
  - Tavily 支持多引擎搜索、页面抓取和结构化提取，但缺少逐字节引证摘录和本地持久化缓存功能。
  article_id: ef03efa8fa36c2ae
extract_result: success
impact_score:
  score: 7.0
  reason: wigolo 的定位是 AI 代理生态中一个被忽视但关键的痛点——网络智能工具的 API 密钥依赖和隐私成本。它并非学术突破，而是一个工程化程度很高的基础设施级工具，通过
    MCP 协议无缝嵌入 Claude Code、Cursor、Codex 等主流编码代理，核心功能零密钥即可使用。在 AI 编码代理快速普及的当下，这一工具可能显著改变开发者获取网络情报的行为模式——从
    SaaS API 按量计费转向本地离线运行。但需要注意的是，它是对 Firecrawl、Exa 等现有工具的补充而非颠覆，且在 LLM 合成能力上仍需可选的外部密钥，因此不构成范式转移。综合评定为
    7.0 分：对 AI 代理工具链生态有实质影响，但属渐进式改进。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 无需 API 密钥即可获得搜索、抓取、提取等核心网络智能能力，本地存储保障数据隐私，且通过 MCP 一键集成主流 AI 编码代理
hype_assessment:
  level: low
  reason: 文章提供了充分的技术细节（10 种工具的具体能力、响应 JSON schema、安装过程、隐私策略），与 Firecrawl/Exa/Tavily
    的对比测试有具体基准数据，诚实标注了 research/agent 工具需要 LLM 密钥的局限性。没有使用 '颠覆'、'革命性' 等 PR 高频词汇，整体语气偏工程化、技术化。
information_entropy: high
domain_disruption:
  technical_innovation: 本地优先的 AI 代理网络智能工具，集成 18 个搜索引擎适配器、多源排名融合、ML 重排序、可解释的逐项评分分解，以及逐字节精确引证溯源——所有核心功能无需
    API 密钥、数据默认存储在本地 ~/.wigolo/ 下。支持 MCP 服务器、REST 端点和 SDK 三种集成模式，覆盖从编码代理到 LangChain/CrewAI
    等框架的全场景。
  business_model: 以本地优先模式直接挑战 Firecrawl、Exa、Tavily 等 SaaS API 按量计费模式。通过 MCP 协议嵌入现有
    AI 代理生态，将网络智能的成本结构从 '每次调用付费' 转变为 '本地资源占用'，大幅降低 AI 代理获取网络信息的门槛和隐私风险。这可能推动 AI 代理工具链从云中心化向边缘化、隐私化方向演进。
engineering_complexity: production_ready
compound_value:
  score: 6.5
  reason: wigolo 的长期复利价值取决于其能否成为 AI 代理获取 Web 信息的默认基础设施层。正面因素：1) 零 API Key、本地优先模式消除了开发者的接入摩擦，一旦被
    Claude Code、Cursor、Codex 等主流编码代理广泛采用，MCP 配置将形成替代成本，产生生态锁定效应；2) 本地缓存随使用时间持续积累单机数据资产，虽非全局网络效应（相比
    Exa/Firecrawl 的共享缓存池），但足以提升用户留存；3) 支持 MCP/REST/SDK 三种集成方式，兼容 LangChain、CrewAI、Vercel
    AI SDK 等框架，覆盖了 AI Agent 工具链的绝大部分入口，传播面广。限制因素：1) 开源且明确标榜 'no metered bill' 的定位，意味着无法走传统
    API 计量变现路径，商业模式不清晰，VC 退出路径狭窄；2) 本地优先架构限制了跨用户的网络效应和数据飞轮，而 Firecrawl、Exa 等云服务可通过共享缓存池持续提升搜索质量，形成竞争差异；3)
    护城河浅——核心功能无需 API Key 也意味着用户迁移成本低，竞争对手也可以开源免费策略跟进。结论：wigolo 是一个优秀的基础设施项目，对 AI Agent
    生态有正向价值，但作为 VC 投资标的，其长期复利受到变现路径不明和网络效应缺失的制约，需要观测是否推出托管版/企业版或数据共享层来构建真正的护城河。
value_capture_layer: agent_middleware
moat_impact: democratizes_access
key_beneficiaries:
- KnockOutEZ
- Anthropic
- MCP ecosystem
- Open-source AI agent community
competitive_casualty:
- Firecrawl
- Exa
- Tavily
- Metered web scraping API services
market_opportunities:
- 企业级 AI 代理团队可采用 wigolo 作为本地化网络情报工具，在无需 API 密钥、无计量计费的前提下为编码代理提供搜索、抓取与研究能力，尤其适用于数据合规要求严格的金融、医疗和政务场景
- 自建 AI 代理平台的开发团队可通过 wigolo 的 REST/SDK 集成方式，将本地优先的网页智能能力嵌入 LangChain、CrewAI、Vercel
  AI SDK 等框架，显著降低第三方 API 调用成本和数据外泄风险
- 隐私敏感型产品创业者可以 wigolo 的开源代码为基础，构建面向垂直行业（如法律调研、竞品监控、学术文献追踪）的本地化 AI 研究助手，核心功能无需任何外部
  API 即可运行
risk_matrix:
  regulatory: 网页抓取与爬取功能可能触犯目标网站的 robots.txt 规则或服务条款，在欧盟《AI Act》和各国数据保护法下，若用于系统性数据采集仍需评估合规风险；但本地优先架构本身不向第三方传输数据，降低了数据处理层面的监管暴露
  technological: 依赖本地浏览器引擎和端侧模型（~1.5GB 磁盘），在搜索结果质量和语义理解深度上可能不及云端方案（Firecrawl、Exa、Tavily）；TUI
    和 CLI 为主的交互方式限制了非技术用户的采用；开源项目存在维护停滞或社区分叉的风险
  competitive: Firecrawl、Exa、Tavily 等竞品已建立起品牌知名度和开发者生态，且部分获得资本支持；wigolo 虽以本地优先和开源免费形成差异化，但在功能成熟度、文档完善度和社区规模上仍有明显差距，较难在短期内获得大规模采用
  ethical: 本地存储所有缓存、嵌入和配置的设计在隐私保护上是正面信号，降低了数据滥用风险；但爬取/监控工具（watch/diff）可能被用于未经授权的网页变更追踪或数据采集，需引导用户遵守目标网站的使用条款
  additional:
  - Node ≥20 和 1.5GB 磁盘的前置要求排除了资源受限环境（如低配 CI 或边缘设备）的使用场景
confidence:
  impact: high
  compound: medium
  hype: low
actionable_insight: deep_dive
object_insights:
- object_type: project
  name: KnockOutEZ/wigolo
  canonical_name: wigolo
  url: https://github.com/KnockOutEZ/wigolo
  positioning: wigolo 是一个本地优先、无需 API 密钥的 AI 代理网络智能工具，提供搜索、抓取、提取和缓存等十种工具，通过 MCP、REST
    和 SDK 三种方式与 AI 编码代理集成。
  technical_signal: wigolo 提供搜索、抓取、提取、缓存等十种工具，核心功能无需 API 密钥即可使用，所有缓存、嵌入向量和配置默认存储在本地
    ~/.wigolo/ 目录下。
  adoption_signal: 用户通过 npx wigolo init 一条命令即可完成安装配置，支持 Claude Code、Cursor、Codex 等主流
    AI 编码代理的 MCP 集成，安装过程全自动无需交互。
  ecosystem_relevance: wigolo 支持 MCP 服务器、REST 端点和 SDK 三种集成方式，可接入 LangChain、CrewAI、LlamaIndex、Vercel
    AI SDK 等主流 AI 框架生态。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: wigolo 以本地优先、零 API 密钥的设计为 AI 代理提供网络智能能力，在隐私保护和离线可用性上具有独特价值，随着 AI 编码代理生态快速发展，其轻量级集成方案有潜力成为
    MCP 生态中的关键基础设施。
  risk_notes:
  - 需要 Node ≥ 20 和约 1.5 GB 磁盘空间，本地浏览器引擎可能在某些环境下存在兼容性问题。
  - research 和 agent 等高级工具依赖外部 LLM 提供者，纯本地模式下无密钥则体验受限。
  - 与 Firecrawl、Exa 等成熟方案相比，作为新生项目在社区规模和生态覆盖上尚有明显差距。
  score: 7.0
  article_ids:
  - ef03efa8fa36c2ae
  evidence_snippets:
  - wigolo 是一个本地优先的 AI 代理网络智能工具，核心功能无需 API 密钥，支持搜索、抓取、提取和缓存等操作。
  - 它通过 MCP 服务器、REST 端点和 SDK 三种方式集成到 Claude Code、Cursor、Codex 等主流 AI 编码代理中。
  - wigolo 的全部缓存、嵌入向量和配置均存储在本地 ~/.wigolo/ 目录下，默认不向任何第三方发送用户数据。
---

Local-first web intelligence for AI agents — **no keys, no cloud, no metered bill.**

works with Claude Code · Cursor · Codex · Gemini CLI · VS Code · Windsurf · Zed · Antigravity

and beyond

**LangChain · CrewAI · LlamaIndex · Vercel AI SDK · n8n & self-hosted agents · any MCP client · plain REST**Quickstart · Tools · Why wigolo · Benchmark · Docs · Examples · Feedback · FAQ

wigolo gives an AI agent one durable surface for everything web-related — **search, fetch, crawl, extract, cache, find-similar, research,** and autonomous gather loops. It runs wherever your agent runs: as an MCP server next to your coding agent, as a REST/MCP endpoint on the box where your self-hosted agents live, or embedded through an SDK inside your own app. The core tools need no API keys, nothing it touches leaves `~/.wigolo/`

, and there's no bill that grows with how much your agent thinks.

Requires **Node ≥ 20** and ~1.5 GB of free disk. macOS, Linux, and Windows.

One command wires the local engine into your agent. `init`

is **unattended by default** — no prompts, safe in scripts and CI — and does the **complete setup**: it downloads the browser engine and on-device models, runs a health check, and prints a per-component summary, so any setup problem surfaces right here, not silently on your agent's first call:

`npx wigolo init --agents=<your-agent>`

— one or more of`<your-agent>`

`claude-code`

·`cursor`

·`codex`

·`gemini-cli`

·`vscode`

·`windsurf`

·`zed`

·`antigravity`

(comma-separated). wigolo writes the MCP config and instructions for you.**Any other MCP client?**Omit`--agents`

and register`npx -y wigolo`

yourself — the installation guide has the exact config block for every client, plus Docker, Homebrew, and single-file-binary channels.**Prefer prompts?**`--interactive`

is a plain-text flow;`--wizard`

is the full terminal TUI.**Skip the downloads?**`--no-warmup`

defers everything to first use. A failed component download never fails setup — init reports what's not ready with the exact fix and still wires your agent.

That's the whole setup — **search, fetch, crawl, extract, cache, and find-similar work with no API key.** Check it's healthy anytime:

`npx wigolo doctor`

Not for you? `npx wigolo config --uninstall --yes`

removes everything, cleanly. You can also paste the installation guide at any AI assistant and let it do the setup — it's written to be self-contained.

Search, fetch, crawl, extract, cache, and find-similar are **fully keyless**. But `research`

, `agent`

, and `search format=answer`

use an LLM to *write* the synthesized, cited answer — without one they hand back a raw brief and evidence for your agent to assemble, which is a much thinner experience. **A free Gemini key is all it takes**, and it's the single biggest quality upgrade you can make:

```
export WIGOLO_LLM_PROVIDER=gemini
export GEMINI_API_KEY=<free-key> # grab one at aistudio.google.com/apikey — the free tier is plenty
```

Any provider works (`anthropic`

· `openai`

· `groq`

), or stay fully local and keyless with `WIGOLO_LLM_PROVIDER=ollama`

(or any OpenAI-compatible URL). Set it in your shell or your agent's MCP `env`

block. Providers, models, and the keyless local-model ladder: configuration guide.

Not snippets — evidence. Every search result carries a verbatim excerpt pinned to its exact position in the source, a citation ID the agent can quote, and a score it can inspect (abridged real shape):

```
{
"results": [{
"title": "Logical replication - PostgreSQL docs",
"url": "https://www.postgresql.org/docs/current/logical-replication.html",
"excerpt": "Logical replication is a method of replicating data objects…",
"citation_id": "src-1",
"source_span": { "start": 1042, "end": 1305 }, // byte-exact provenance
"evidence_score": { "final": 0.86, "semantic": 0.91, "lexical": 0.78, "engine_consensus": 3 }
}],
"citations": [{ "id": "src-1", "url": "…" }],
"freshness_signal": { "published": "2026-05-12", "confidence": "high" }
}
```

Weak results get flagged as junk by wigolo's own scorer, failed engines are reported, stale cache is labeled — the agent always knows what it's standing on. Full response contracts per tool: tools reference.

| Tool | What it does |
|---|---|
🔎 `search` |
Multi-engine web search (18 direct adapters) with rank fusion, ML reranking, and an explainable per-result score. Pass a query array for parallel breadth. |
📄 `fetch` |
Load one URL through a tiered router that auto-escalates from plain HTTP to a headless browser engine on anti-bot challenges or SPA shells. Clean markdown + metadata + links. |
🕸️ `crawl` |
Multi-page crawl — BFS, DFS, sitemap, or map-only. Per-domain rate limits, robots.txt respect, boilerplate dedup. |
🧩 `extract` |
Structured data from a page: tables, metadata, JSON-LD, brand identity, named schemas (Article / Recipe / Product / …), or any custom JSON Schema. |
💾 `cache` |
Query everything already seen — keyword or hybrid semantic. Plus stats, clear, and change detection. |
🧲 `find_similar` |
Pages similar to a URL or a concept, via 3-way fusion of keyword + semantic + live web. |
🧠 `research` |
Decompose a question → fan out sub-queries → fetch sources → synthesize a cited report (or a structured brief the host LLM writes from). |
🤖 `agent` |
Autonomous gather loop: plan → search → fetch → extract → synthesize, with a step log, time budget, and optional output schema. |
🔁 `diff` + ⏱️ `watch` |
See exactly what changed on a page since last visit; re-check on demand and deliver changes to a webhook. |

Every tool also runs from the terminal (`wigolo search "…" --json`

), from an interactive shell with NDJSON piping (`wigolo shell`

), over REST, and through the SDKs — CLI reference.

Each tool goes well past its one-liner. A sampler — every line links to the guide and, where there's one, a runnable example:

**Search that fans out**— pass a query**array**for parallel breadth, scope to`include_domains`

, bound by`time_range`

/recency, exact-phrase match, choose a depth tier, even image results. → guide · example**Fetch almost anything**— JS-rendered SPAs, PDFs, a single heading`section`

, authenticated pages (via a browser profile or remote browser), or drive the page with`actions`

(click / type / scroll / screenshot). → guide**Crawl a whole site**— sitemap, BFS, DFS, or map-only; robots.txt-respecting, per-domain rate-limited, boilerplate-deduped. → guide**Extract structure**— tables, JSON-LD, metadata, brand assets, named schemas (Article / Recipe / Product / …), or your own JSON Schema. → guide**A memory that compounds**— every page is cached; re-query by keyword or meaning, instantly and offline; detect what changed since last visit. → guide · example**Research & autonomous gather**— decompose a question into a cited brief, or turn`agent`

loose to plan → fetch → extract → synthesize against a JSON Schema and a time budget. → guide · example**Watch & diff**— monitor a URL, get a change report, deliver it to a webhook. → guide · example**Drive it your way**— one-shot CLI, an NDJSON shell for pipelines, REST, SDKs, or as skills your agent installs. → CLI & shell · example**Extend it**— add a search engine or a site extractor as a plugin in ~100 lines. → plugins · example**Tune & inspect**—`wigolo tune`

shows what it learned per domain (which fetch tier, challenge clearances, backoff);`doctor`

/`verify`

health-check every component. → CLI · troubleshooting

wigolo isn't the free stand-in you settle for until the budget clears — it's built to hold the same line as the paid services in this lane, and it brings receipts. What actually separates it:

**Built for agents, not humans.**One MCP call fans out many queries across many engines in parallel — something a serial host tool-loop can't replicate — with transparent per-result scoring and budget-aware output.**Honest output.**Stale cache, failed fetches, degraded backends, and truncation are surfaced in the result, never disguised as empty-but-successful data. When a bot-protected page can't be read, you get a labeled`blocked_by_challenge`

failure — never a challenge shell dressed up as content.**$0 per query, free to re-query.**Default search talks to public engines through direct adapters; the reranker and embeddings run on-device. Every response is cached, so asking again is instant and costs nothing.**Private by default.**Cache, embeddings, models, and config live under`~/.wigolo/`

. Nothing reaches a third party unless you explicitly opt into an LLM for synthesis.

wigolo is a focused web layer for your agents — not a hosted SaaS, a vector database other apps query, or a scale-scraping platform. Within that lane it goes toe-to-toe with the paid services on result quality — and the meter, the key, and the data-egress simply aren't there.

Here's what one real result looks like, dissected — including the failed engine and the weak result, because those are part of the answer too:


All four tools converged on the same core answer — and only one of them handed back verbatim, byte-pinned evidence while doing it.

One cold query, run live inside a single **Claude Fable 5** session and fanned out to four web tools on equal footing — built-in **WebSearch**, **wigolo**, **Tavily**, and **Exa** — then reported by the agent itself under one rule: judge on the evidence alone, no favoritism. All four converged on the same answer and the same top source — parity demonstrated, not asserted. wigolo alone returned verbatim excerpts pinned to byte-offset source spans, an explainable score decomposition, and live per-engine telemetry — and when two of its results were weak, its own scorer flagged them as junk on-screen. The cloud tools earn their line too: Exa rendered the official docs' comparison matrix in full. One honest query, not a leaderboard — run your own and you'll see the same shape.

| wigolo | Firecrawl | Exa | Tavily | |
|---|---|---|---|---|
| Multi-engine web search | ✅ | ✅ | ✅ | ✅ |
| Fetch & structured extraction | ✅ | ✅ | ✅ | ✅ |
| Whole-site crawl & map | ✅ | ✅ | — | ✅ |
| Verbatim excerpts pinned to byte-offset source spans | ✅ | — | — | — |
| Explainable per-result score decomposition | ✅ | — | — | — |
| Persistent local memory — re-query instantly, offline | ✅ | — | — | — |
| Query data stays on your machine | ✅ | — | — | — |
| API key / account | none | required | required | required |
| Cost per query | $0 | metered | metered | metered |

Feature standing as of July 2026 — check each vendor's docs for current state.

That last row is the one that compounds — agents don't ask once, they ask in bursts:

The same ten tools serve every kind of agent, over whichever surface fits — MCP for coding agents, REST for everything else, SDKs to embed, framework wrappers to drop in.

One process exposes a plain-JSON REST API next to the MCP transport. No MCP client needed — just curl:

```
wigolo serve # 127.0.0.1:3333 — loopback is open; off-loopback requires a token
curl -sX POST http://127.0.0.1:3333/v1/search \
-H 'Content-Type: application/json' \
-d '{"query":"local-first software","max_results":5}'
```

`POST /v1/{tool}`

covers all ten tools, `GET /openapi.json`

is the OpenAPI 3.1 contract, and `/mcp`

+ `/sse`

serve remote MCP clients from the same port. Bind past loopback and a bearer token is required — the server fails closed rather than opening wide by accident. Point n8n, a Hermes-style assistant, or any self-hosted agent at it. → REST API

Thin, typed clients with an embedded local mode that finds or starts the daemon for you — no separate `serve`

step.

**TypeScript** — `npm install wigolo-sdk`

(zero-dep; Node / Bun / Deno / edge):

```
import { createLocalClient } from 'wigolo-sdk/local';
const { client, close } = await createLocalClient(); // reuse a running daemon, or spawn one
const res = await client.search({ query: 'local-first web search', max_results: 5 });
console.log(res.results.map((r) => r.title));
await close(); // stops the daemon only if this call spawned it
```

**Python** — `pip install wigolo`

(standard library only; sync + async):

```
from wigolo import local_client
with local_client() as client: # reuse a healthy daemon, or spawn one
res = client.search(query="local-first web search", max_results=5)
for r in res["results"]:
print(r["title"], r["url"])
```

Drop wigolo's tools into the framework you already use — the full ten-tool surface, including the cache / find_similar / research / agent that most framework web-tools don't ship:

| Framework | Package | What you get |
|---|---|---|
LangChain |
`wigolo-langchain` |
each tool as a `BaseTool` , plus a `BaseRetriever` over search / find_similar for RAG |
CrewAI |
`wigolo-crewai` |
`wigolo_tools()` → hand the set to any crew |
LlamaIndex |
`wigolo-llamaindex` |
a `BaseReader` that loads fetched / crawled / searched pages as documents |
Vercel AI SDK |
`wigolo-vercel-ai-sdk` |
tool factories for `generateText` / `streamText` , edge-friendly |

```
# stdio MCP — wire it into any MCP client as command: docker
docker run -i --rm -v wigolo-data:/data ghcr.io/knockoutez/wigolo
# HTTP server for remote / multi-client use
docker run -p 3333:3333 -v wigolo-data:/data \
-e WIGOLO_API_TOKEN=a-long-random-secret \
ghcr.io/knockoutez/wigolo serve --host 0.0.0.0
```

The slim image lazy-loads models into the volume; `:full`

preinstalls the browser engine. Also on Docker Hub as `towhid69420/wigolo`

. → installation & all channels

An 11-pack skill catalog teaches your coding agent to drive each tool well — installed by `init`

, managed with `wigolo skills add|list|remove`

. → skills

One honest note for self-hosters: some challenge-protected sites score IP reputation, so a datacenter IP won't clear walls a home connection would. wigolo labels those failures instead of faking them, and the self-hosting guide covers the opt-in proxy answer.

A single Node process speaking MCP (JSON-RPC over stdio). Everything heavy is local and lazy-loaded, so a zero-key install pays nothing for the parts it isn't using.

```
flowchart TD
A["🤖 AI agent<br/>any MCP client · REST · SDK"]
A -->|MCP over stdio| B["<b>wigolo</b><br/>10 tools · dynamic instructions<br/>in-process browser pool + cache + models"]
B --> C{"Tool layer"}
C --> T1["search · fetch · crawl · extract"]
C --> T2["cache · find_similar · research · agent"]
T1 --> F["⚙️ Fetch router<br/>tiered escalation, learned per domain"]
T1 --> S["⚙️ Search<br/>18 engines → rank fusion → ML rerank<br/><i>explainable evidence score</i>"]
T2 --> DB[("🗄️ Local cache<br/>keyword + vector index")]
T2 --> ML["🧠 On-device ML<br/>embeddings + reranker"]
F -.->|optional| LLM["☁️ LLM<br/>synthesis only · opt-in"]
S -.->|optional| SX["🔀 Aggregator backend<br/>opt-in legacy / hybrid"]
F --> WEB["🌍 Public web"]
S --> WEB
style B fill:#7c3aed,stroke:#5b21b6,color:#fff
style WEB fill:#0ea5e9,stroke:#0369a1,color:#fff
style DB fill:#1e293b,stroke:#334155,color:#fff
style LLM stroke-dasharray: 5 5
style SX stroke-dasharray: 5 5
```

**Code beats model.**Deterministic work — canonicalization, rank fusion, dedup, schema matching — never touches an LLM. The model is reserved for judgment, opt-in, and capped per request; LLM-filled fields are checked against the source and nulled if absent.**Routing on observable signals.**The fetch ladder escalates to a real browser on what it*sees*— SPA markers, challenge bodies, thin content — not domain guesses. It learns per domain, unlearns when a site stops needing it, and`wigolo tune list`

shows you exactly what it learned.**Reads pages the way a browser does — and says so when it can't.**Tiered fetching waits out interstitial challenges and reuses clearances per domain, politely: robots.txt respected, per-domain rate limits, research-grade volumes. When a wall stays up, the failure is labeled, never disguised.

A clean install works out of the box. Three settings meaningfully raise output quality:

```
# 1. Synthesis — the biggest lever (research / agent / search-answer write real prose)
export WIGOLO_LLM_PROVIDER=gemini # or anthropic / openai / groq / ollama (keyless)
export GEMINI_API_KEY=<your-key>
# 2. Wider retrieval funnel
export WIGOLO_SEARCH=hybrid # core engines + aggregator fallback
export WIGOLO_GITHUB_TOKEN=... # GitHub code search 10 → 30 req/min
# 3. Land more fetches, stay warm
export WIGOLO_TLS_TIER=auto # per-domain learned fetch hardening
export WIGOLO_EAGER_WARMUP=1 # pay the ~1s model load up front
```

**Per-call habits that pay off:** query **arrays** (`["a","b","c"]`

) for parallel breadth · `search_depth: "deep"`

for queries that matter · `include_domains`

as a hard filter for docs lookups.

The full reference — every environment variable, config-file key, search backend, cache TTL, and serve limit — lives in the configuration guide.

**docs/** — the complete manual:
getting started · installation & channels · configuration · tools reference · CLI & shell · REST API · SDKs & integrations · self-hosting · agent skills · plugins · troubleshooting & FAQ · privacy & security

**examples/** — runnable, each with a README (and most with a terminal recording): one-shot CLI, NDJSON shell pipelines, REST via curl, TypeScript & Python SDKs, Vercel AI SDK tools, pointing self-hosted n8n at a remote wigolo, watch-with-webhook, and writing your own search-engine plugin.

Docs are also rendered on the site: **knockoutez.github.io/wigolo/docs**.

wigolo is in **public beta**. Everything documented here works and is held to a 7,600-test suite — beta is about the polish bar, not stability. It stays beta until enough people have used it, kicked it, and starred it that calling it v1 means something.

That makes your feedback the whole game right now. Every report is read, usually the same day:

- 🐛
**Report a bug**— broke, misbehaved, surprised you - 💡
**Request a feature**— something it should do - 💬
**Ask anything**— questions, setups, show & tell

And if wigolo earns a place in your setup, the ways to keep it alive: a ⭐ **star** (it's how open source gets found), a **☕ coffee** (there's no paid tier and never will be), or just **an email** — it goes straight to the one developer who wrote the code.

`wigolo doctor`

names any broken component and the exact env var or command that fixes it; `wigolo doctor --fix`

repairs the common cases. A component failing during `init`

**doesn't** break wigolo — `init`

still exits 0, and core search / fetch / crawl / extract / cache work with no models and no browser.

Quick hits:

**Slow or failed downloads**— re-run`wigolo warmup --all`

(or`--browser`

/`--embeddings`

/`--reranker`

); they resume and retry.**Browser won't launch on Linux**—`wigolo warmup --browser`

installs the OS libraries (or prints the exact command).**Native build error / unusual Node**— use an LTS:**Node 20, 22, or 24**.**Behind a proxy**—`USE_PROXY=true`

+`PROXY_URL`

; add`NODE_EXTRA_CA_CERTS`

for TLS-inspecting proxies.

Full guide — per-symptom fixes, a "what still works when X fails" map, platform notes (incl. linux-arm64), and offline installs: **docs/troubleshooting.md**.

**Free? What's the catch?**

No catch by design. The expensive parts — ranking, embeddings, the browser engine — run on *your* hardware, so there's no per-query cost to recover and no reason for a meter. Sustained by donations; the AGPL license legally prevents a bait-and-switch into a closed hosted product.

**Is the quality really on par with the paid services?**

Run one query and judge — the benchmark section above is a live 4-way run, not a chart. Everyday agent queries land at parity; the paid tools still win some deep-extraction edge cases, and crawling is where wigolo is strongest. Every result shows its scoring, so you don't have to take anyone's word for it.

**Won't public search engines block or rot?**

It's engineered for exactly that: 18 engines fused with rank fusion (any one failing barely moves results), a tiered fetch ladder with per-domain learning, and an optional aggregator fallback. Degraded backends are *reported in the output*, never hidden — and the local cache means everything already seen keeps working regardless.

**Is this kind of scraping OK?**

wigolo reads the public web the way a browser does — robots.txt respected by default, per-domain rate limits, research-grade volumes for one agent on one machine. It's deliberately the polite end of the spectrum, not a harvesting platform.

**AGPL — can I use this at work?**

Yes, freely, company-wide. The license only bites if you *modify wigolo and run it as a network service* — then you must publish those modifications. Using it as a local dev tool carries zero obligation. Commercial-licensing questions: reach out.

**Why 1.5 GB of disk?**

That's the on-device brain: a full browser engine plus the ranking and embedding models the cloud services run on their side and bill you for. Disk is cheap; meters aren't.

**npm**—`wigolo`

*(primary channel — the Quickstart above)***PyPI**—`wigolo`

*(Python SDK)***Docker**—`ghcr.io/knockoutez/wigolo`

·`towhid69420/wigolo`

**Official MCP Registry**—`io.github.KnockOutEZ/wigolo`

**Directories**— Glama · Smithery · mcp.so · LobeHub

Homebrew, `curl | sh`

, and the single-file binary are covered in the installation guide — one channel per machine; they all share `~/.wigolo`

.

Bug reports, feature requests, and PRs are all welcome — see **CONTRIBUTING.md**. Keep tool handlers thin, add tests, run the suite before opening a PR. The friendliest entry point: wigolo has a plugin system for custom search engines and extractors — add a search engine in ~100 lines, template in `examples/plugin-search-engine`

.

**GNU AGPL-3.0-only.** Free to use, modify, and self-host — including inside a company. The one obligation: if you run a **modified** version as a network service, you must publish your modified source under the same license. That keeps wigolo open while preventing a closed, hosted fork. See **SECURITY.md** to report a vulnerability and **TRADEMARK.md** for use of the name. For commercial-licensing questions, reach out.

wigolo is free and meant to stay that way — maintained, not paywalled.
If it saves you a metered search bill, a ⭐, a sharp issue, or a **☕ coffee** helps keep it sustainable.

Built and maintained by @KnockOutEZ · ktowhid20@gmail.com