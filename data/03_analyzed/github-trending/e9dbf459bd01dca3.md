---
title: firecrawl/firecrawl
source: https://github.com/firecrawl/firecrawl
author: []
published: ''
created: '2026-06-24'
description: 'The API to search, scrape, and interact with the web at scale. 🔥 🔥 Firecrawl
  The API to search, scrape, and interact with the web at scale. 🔥 The web context
  API to find sources, extract content, and turn it into clean Markdown or structured
  data your agents can ship with. Open source and available as a hosted service. Pst.
  Hey, you, join our stargazers 😃 Why Firecrawl? Industry-leading reliability: Covers
  96% of the web, including JS-heavy pages — no proxy headaches, just clean data (see
  benchmarks) Blazingly fast: P95 latency of 3.4s across millions of pages, built
  for real-time agents and dynamic apps LLM-ready output: Clean markdown, structured
  JSON, screenshots, and more — spend fewer tokens, build better AI apps We handle
  the hard stuff: Rotating proxies, orchestration, rate limits, JS-blocked content,
  and more — zero configuration Agent ready: Connect Firecrawl to any AI agent or
  MCP client with a single command Media parsing: Parse and extract content from web-hosted
  PDFs, DOCX, and more Actions: Click, scroll, write, wait, and press before extracting
  content Open source: Developed transparently and collaboratively — join our community
  Feature Overview Core Endpoints Feature Description Search Search the web and get
  full page content from results Scrape Convert any URL to markdown, HTML, screenshots,
  or structured JSON Interact Scrape a page, then interact with it using AI prompts
  or code More Feature Description Agent Automated data gathering, just describe what
  you need Crawl Scrape all URLs of a website with a single request Map Discover all
  URLs on a website instantly Batch Scrape Scrape thousands of URLs asynchronously
  Quick Start Sign up at firecrawl.dev to get your API key. Try the playground to
  test it out. Search Search the web and get full content from results. from firecrawl
  import Firecrawl app = Firecrawl(api_key="fc-YOUR_API_KEY") search_result = app.search("firecrawl",
  limit=5) Node.js / cURL / CLI Node.js import { Firecrawl } from ''firecrawl''; const
  app = new Firecrawl({apiKey: "fc-YOUR_API_KEY"}); app.search("firecrawl", { limit:
  5 }) cURL curl -X POST ''https://api.firecrawl.dev/v2/search'' \ -H ''Authorization:
  Bearer fc-YOUR_API_KEY'' \ -H ''Content-Type: application/json'' \ -d ''{ "query":
  "firecrawl", "limit": 5 }'' CLI firecrawl search "firecrawl" --limit 5 Output: [
  { "url": "https://firecrawl.dev", "title": "Firecrawl", "markdown": "Turn websites
  into..." }, { "url": "https://docs.firecrawl.dev", "title": "Firecrawl Docs", "markdown":
  "# Getting Started..." } ] Scrape Get LLM-ready data from any website — markdown,
  JSON, screenshots, and more. from firecrawl import Firecrawl app = Firecrawl(api_key="fc-YOUR_API_KEY")
  result = app.scrape(''firecrawl.dev'') Node.js / cURL / CLI Node.js import { Firecrawl
  } from ''firecrawl''; const app = new Firecrawl({ apiKey: "fc-YOUR_API_KEY" });
  app.scrape(''firecrawl.dev'') cURL curl -X POST ''https://api.firecrawl.dev/v2/scrape''
  \ -H ''Authorization: Bearer fc-YOUR_API_KEY'' \ -H ''Content-Type: application/json''
  \ -d ''{ "url": "firecrawl.dev" }'' CLI firecrawl scrape https://firecrawl.dev firecrawl
  https://firecrawl.dev --only-main-content Output: # Firecrawl Firecrawl helps AI
  systems search, scrape, and interact with the web. ## Features - Search: Find information
  across the web - Scrape: Clean data from any page - Interact: Click, navigate, and
  operate pages - Agent: Autonomous data gathering Interact Scrape a page, then interact
  with it using AI prompts or code. from firecrawl import Firecrawl app = Firecrawl(api_key="fc-YOUR_API_KEY")
  result = app.scrape("https://amazon.com") scrape_id = result.metadata.scrape_id
  app.interact(scrape_id, prompt="Search for ''mechanical keyboard''") app.interact(scrape_id,
  prompt="Click the first result") Node.js / cURL / CLI Node.js import { Firecrawl
  } from ''firecrawl''; const app = new Firecrawl({apiKey: "fc-YOUR_API_KEY"}); const
  result = await app.scrape("https://amazon.com"); await app.interact(result.metadata.scrapeId,
  { prompt: "Search for ''mechanical keyboard''" }); await app.interact(result.metadata.scrapeId,
  { prompt: "Click the first result" }); cURL # 1. Scrape the page curl -X POST ''https://api.firecrawl.dev/v2/scrape''
  \ -H ''Authorization: Bearer fc-YOUR_API_KEY'' \ -H ''Content-Type: application/json''
  \ -d ''{"url": "https://amazon.com"}'' # 2. Interact with the page (use scrapeId
  from step 1) curl -X POST ''https://api.firecrawl.dev/v2/scrape/SCRAPE_ID/interact''
  \ -H ''Authorization: Bearer fc-YOUR_API_KEY'' \ -H ''Content-Type: application/json''
  \ -d ''{"prompt": "Search for mechanical keyboard"}'' CLI firecrawl scrape https://amazon.com
  firecrawl interact exec --prompt "Search for ''mechanical keyboard''" firecrawl
  interact exec --prompt "Click the first result" Output: { "success": true, "output":
  "Keyboard available at $100", "liveViewUrl": "https://liveview.firecrawl.dev/..."
  } Power Your Agent Connect Firecrawl to any AI agent or MCP client in minutes. Skill
  Give your agent easy access to real-time web data with one command. npx -y firecrawl-cli@latest
  init --all --browser Restart your agent after installing. Works with Claude Code,
  Antigravity, OpenCode, and more. MCP Connect any MCP-compatible client to the web
  in seconds. { "mcpServers": { "firecrawl-mcp": { "command": "npx", "args": ["-y",
  "firecrawl-mcp"], "env": { "FIRECRAWL_API_KEY": "fc-YOUR_API_KEY" } } } } Agent
  Onboarding Are you an AI agent? Fetch this skill to sign up your user, get an API
  key, and start building with Firecrawl. curl -s https://firecrawl.dev/agent-onboarding/SKILL.md
  See the Skill + CLI documentation for all available commands. For MCP, see firecrawl-mcp-server.
  More Endpoints Agent The easiest way to get data from the web. Describe what you
  need, and our AI agent searches, navigates, and retrieves it. No URLs required.
  Agent is the evolution of our /extract endpoint: faster, more reliable, and doesn''t
  require you to know the URLs upfront. curl -X POST ''https://api.firecrawl.dev/v2/agent''
  \ -H ''Authorization: Bearer fc-YOUR_API_KEY'' \ -H ''Content-Type: application/json''
  \ -d ''{ "prompt": "Find the pricing plans for Notion" }'' Response: { "success":
  true, "data": { "result": "Notion offers the following pricing plans:\n\n1. Free
  - $0/month...\n2. Plus - $10/seat/month...\n3. Business - $18/seat/month...", "sources":
  ["https://www.notion.so/pricing"] } } Agent with Structured Output Use a schema
  to get structured data: from firecrawl import Firecrawl from pydantic import BaseModel,
  Field from typing import List, Optional app = Firecrawl(api_key="fc-YOUR_API_KEY")
  class Founder(BaseModel): name: str = Field(description="Full name of the founder")
  role: Optional[str] = Field(None, description="Role or position") class FoundersSchema(BaseModel):
  founders: List[Founder] = Field(description="List of founders") result = app.agent(
  prompt="Find the founders of Firecrawl", schema=FoundersSchema ) print(result.data)
  { "founders": [ {"name": "Eric Ciarla", "role": "Co-founder"}, {"name": "Nicolas
  Camara", "role": "Co-founder"}, {"name": "Caleb Peffer", "role": "Co-founder"} ]
  } Agent with URLs (Optional) Focus the agent on specific pages: result = app.agent(
  urls=["https://docs.firecrawl.dev", "https://firecrawl.dev/pricing"], prompt="Compare
  the features and pricing information" ) Model Selection Choose between two models
  based on your needs: Model Cost Best For spark-1-mini (default) 60% cheaper Most
  tasks spark-1-pro Standard Complex research, critical data gathering result = app.agent(
  prompt="Compare enterprise features across Firecrawl, Apify, and ScrapingBee", model="spark-1-pro"
  ) When to use Pro: Comparing data across multiple websites Extracting from sites
  with complex navigation or auth Research tasks where the agent needs to explore
  multiple paths Critical data where accuracy is paramount Learn more about Spark
  models in our Agent documentation. Crawl Crawl an entire website and get content
  from all pages. curl -X POST ''https://api.firecrawl.dev/v2/crawl'' \ -H ''Authorization:
  Bearer fc-YOUR_API_KEY'' \ -H ''Content-Type: application/json'' \ -d ''{ "url":
  "https://docs.firecrawl.dev", "limit": 100, "scrapeOptions": { "formats": ["markdown"]
  } }'' Returns a job ID: { "success": true, "id": "123-456-789", "url": "https://api.firecrawl.dev/v2/crawl/123-456-789"
  } Check Crawl Status curl -X GET ''https://api.firecrawl.dev/v2/crawl/123-456-789''
  \ -H ''Authorization: Bearer fc-YOUR_API_KEY'' { "status": "completed", "total":
  50, "completed": 50, "creditsUsed": 50, "data": [ { "markdown": "# Page Title\n\nContent...",
  "metadata": {"title": "Page Title", "sourceURL": "https://..."} } ] } Note: The
  SDKs handle polling automatically for a better developer experience. Map Discover
  all URLs on a website instantly. curl -X POST ''https://api.firecrawl.dev/v2/map''
  \ -H ''Authorization: Bearer fc-YOUR_API_KEY'' \ -H ''Content-Type: application/json''
  \ -d ''{"url": "https://firecrawl.dev"}'' Response: { "success": true, "links":
  [ {"url": "https://firecrawl.dev", "title": "Firecrawl", "description": "Turn websites
  into LLM-ready data"}, {"url": "https://firecrawl.dev/pricing", "title": "Pricing",
  "description": "Firecrawl pricing plans"}, {"url": "https://firecrawl.dev/blog",
  "title": "Blog", "description": "Firecrawl blog"} ] } Map with Search Find specific
  URLs within a site: from firecrawl import Firecrawl app = Firecrawl(api_key="fc-YOUR_API_KEY")
  result = app.map("https://firecrawl.dev", search="pricing") # Returns URLs ordered
  by relevance to "pricing" Batch Scrape Scrape multiple URLs at once: from firecrawl
  import Firecrawl app = Firecrawl(api_key="fc-YOUR_API_KEY") job = app.batch_scrape([
  "https://firecrawl.dev", "https://docs.firecrawl.dev", "https://firecrawl.dev/pricing"
  ], formats=["markdown"]) for doc in job.data: print(doc.metadata.source_url) SDKs
  Our SDKs provide a convenient way to use all Firecrawl features and automatically
  handle polling for async operations. Python Install the SDK: pip install firecrawl-py
  from firecrawl import Firecrawl app = Firecrawl(api_key="fc-YOUR_API_KEY") # Scrape
  a single URL doc = app.scrape("https://firecrawl.dev", formats=["markdown"]) print(doc.markdown)
  # Use the Agent for autonomous data gathering result = app.agent(prompt="Find the
  founders of Stripe") print(result.data) # Crawl a website (automatically waits for
  completion) docs = app.crawl("https://docs.firecrawl.dev", limit=50) for doc in
  docs.data: print(doc.metadata.source_url, doc.markdown[:100]) # Search the web results
  = app.search("best AI data tools 2024", limit=10) print(results) Node.js Install
  the SDK: npm install firecrawl import { Firecrawl } from ''firecrawl''; const app
  = new Firecrawl({ apiKey: ''fc-YOUR_API_KEY'' }); // Scrape a single URL const doc
  = await app.scrape(''https://firecrawl.dev'', { formats: [''markdown''] }); console.log(doc.markdown);
  // Use the Agent for autonomous data gathering const result = await app.agent({
  prompt: ''Find the founders of Stripe'' }); console.log(result.data); // Crawl a
  website (automatically waits for completion) const docs = await app.crawl(''https://docs.firecrawl.dev'',
  { limit: 50 }); docs.data.forEach(doc => { console.log(doc.metadata.sourceURL, doc.markdown.substring(0,
  100)); }); // Search the web const results = await app.search(''best AI data tools
  2024'', { limit: 10 }); results.data.web.forEach(result => { console.log(`${result.title}:
  ${result.url}`); }); Java Add the dependency (Gradle/Maven): repositories { mavenCentral()
  maven { url ''https://jitpack.io'' } } dependencies { implementation ''com.github.firecrawl:firecrawl-java-sdk:2.0''
  } import dev.firecrawl.client.FirecrawlClient; import dev.firecrawl.model.*; FirecrawlClient
  client = new FirecrawlClient( System.getenv("FIRECRAWL_API_KEY"), null, null );
  // Scrape a single URL ScrapeParams scrapeParams = new ScrapeParams(); scrapeParams.setFormats(new
  String[]{"markdown"}); FirecrawlDocument doc = client.scrapeURL("https://firecrawl.dev",
  scrapeParams); System.out.println(doc.getMarkdown()); // Use the Agent for autonomous
  data gathering AgentParams agentParams = new AgentParams("Find the founders of Stripe");
  AgentResponse start = client.createAgent(agentParams); AgentStatusResponse result
  = client.getAgentStatus(start.getId()); System.out.println(result.getData()); //
  Crawl a website (polls until completion) CrawlParams crawlParams = new CrawlParams();
  crawlParams.setLimit(50); CrawlStatusResponse job = client.crawlURL("https://docs.firecrawl.dev",
  crawlParams, null, 10); for (FirecrawlDocument page : job.getData()) { System.out.println(page.getMetadata().get("sourceURL"));
  } // Search the web SearchParams searchParams = new SearchParams("best AI data tools
  2024"); searchParams.setLimit(10); SearchResponse results = client.search(searchParams);
  for (SearchResult r : results.getResults()) { System.out.println(r.getTitle() +
  ": " + r.getUrl()); } Elixir Add the dependency: def deps do [ {:firecrawl, "~>
  1.0"} ] end # Scrape a URL {:ok, response} = Firecrawl.scrape_and_extract_from_url(
  url: "https://firecrawl.dev", formats: ["markdown"] ) # Crawl a website {:ok, response}
  = Firecrawl.crawl_urls( url: "https://docs.firecrawl.dev", limit: 50 ) # Search
  the web {:ok, response} = Firecrawl.search_and_scrape( query: "best AI data tools
  2024", limit: 10 ) # Map URLs {:ok, response} = Firecrawl.map_urls(url: "https://example.com")
  Rust Add the dependency: [dependencies] firecrawl = "2" tokio = { version = "1",
  features = ["macros", "rt-multi-thread"] } use firecrawl::{Client, ScrapeOptions,
  Format, CrawlOptions}; #[tokio::main] async fn main() -> Result<(), Box<dyn std::error::Error>>
  { let client = Client::new("fc-YOUR_API_KEY")?; // Scrape a URL let document = client.scrape("https://firecrawl.dev",
  None).await?; println!("{:?}", document.markdown); // Crawl a website let options
  = CrawlOptions { limit: Some(50), ..Default::default() }; let result = client.crawl("https://docs.firecrawl.dev",
  options).await?; println!("Crawled {} pages", result.data.len()); // Search the
  web let response = client.search("best web scraping tools 2024", None).await?; println!("{:?}",
  response.data); Ok(()) } Community SDKs Go SDK Integrations Agents & AI Tools Firecrawl
  Skill Firecrawl CLI Skills Firecrawl Workflows Firecrawl MCP Platforms Lovable Zapier
  n8n View all integrations → Missing your favorite tool? Open an issue and let us
  know! Resources Documentation API Reference Playground Changelog Open Source vs
  Cloud Firecrawl is open source under the AGPL-3.0 license. The cloud version at
  firecrawl.dev includes additional features: To run locally, see the Contributing
  Guide. To self-host, see Self-Hosting Guide. Contributing We love contributions!
  Please read our Contributing Guide before submitting a pull request. Contributors
  License This project is primarily licensed under the GNU Affero General Public License
  v3.0 (AGPL-3.0). The SDKs and some UI components are licensed under the MIT License.
  See the LICENSE files in specific directories for details. It is the sole responsibility
  of end users to respect websites'' policies when scraping. Users are advised to
  adhere to applicable privacy policies and terms of use. By default, Firecrawl respects
  robots.txt directives. By using Firecrawl, you agree to comply with these conditions.
  ↑ Back to Top ↑'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: e9dbf459bd01dca3
source_type: community_discussion
tldr: Firecrawl 是一个开源的网页抓取与交互 API，支持将任意网页转换为 AI 可消费的 Markdown、结构化 JSON 或截图，覆盖 96%
  的网页且 P95 延迟为 3.4 秒。
objective_summary: Firecrawl 是一个开源 Web 数据抓取与交互 API 项目，由 Eric Ciarla、Nicolas Camara
  和 Caleb Peffer 联合创立。它提供 Search、Scrape、Interact、Agent、Crawl 和 Map 等核心功能，可将网页内容转为
  LLM 就绪的 Markdown、JSON 或截图，并内置代理轮换、速率限制等复杂处理。项目在 GitHub 上开源，同时提供托管云服务，支持 MCP 协议集成，覆盖
  96% 的网页且 P95 延迟为 3.4 秒。
event_type: framework_tools
epistemic_status: pr_statement
entities:
  companies:
  - Firecrawl
  - Notion
  - Apify
  - ScrapingBee
  technologies:
  - MCP
  key_people:
  - Eric Ciarla
  - Nicolas Camara
  - Caleb Peffer
key_logic_flow:
- Firecrawl 是开源项目，提供 Search、Scrape、Interact、Agent、Crawl、Map 和 Batch Scrape 七项核心 API
  端点，覆盖网页数据全链路。
- Scrape 端点可将任意 URL 转为 Markdown、HTML、结构化 JSON 或截图，且内置代理轮换和反爬处理，无需用户额外配置。
- Interact 端点允许在抓取页面上执行点击、滚动、输入等操作，适用于 Amazon 等复杂动态页面的数据采集。
- Agent 功能支持用户通过自然语言描述需求，AI 自主搜索、导航和提取数据，无需提前指定目标 URL。
- 项目支持 MCP 协议，通过一条 npx 命令即可将 Firecrawl 集成到 Claude Code、Antigravity、OpenCode 等 AI 代理中。
- 提供 Python、Node.js、Java 多语言 SDK 及 CLI 工具，SDK 自动处理异步任务的轮询等待。
extract_result: success
object_mentions:
- object_type: project
  name: firecrawl/firecrawl
  canonical_name: firecrawl/firecrawl
  url: https://github.com/firecrawl/firecrawl
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Firecrawl 是一个开源 Web 抓取 API，支持 Search、Scrape、Crawl、Map 等核心功能，覆盖 96% 的网页且 P95 延迟为
    3.4 秒。
  - 项目提供 Python、Node.js、Java 多语言 SDK 及 CLI 工具，并作为托管服务在 firecrawl.dev 上运营。
  - Firecrawl 由 Eric Ciarla、Nicolas Camara 和 Caleb Peffer 联合创立，核心创始人均在官网公开列出。
  article_id: e9dbf459bd01dca3
- object_type: project
  name: firecrawl-mcp
  canonical_name: firecrawl-mcp
  url: https://github.com/firecrawl/firecrawl-mcp-server
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - Firecrawl 可通过 MCP 配置将 firecrawl-mcp 作为 mcpServers 接入，兼容 Claude Code、Antigravity、OpenCode
    等 AI 代理。
  - 配置示例为在 mcpServers 中添加 firecrawl-mcp 条目，设置命令为 npx -y firecrawl-mcp，并传入 FIRECRAWL_API_KEY
    环境变量。
  article_id: e9dbf459bd01dca3
- object_type: product
  name: Firecrawl Agent
  canonical_name: Firecrawl Agent
  url: https://firecrawl.dev
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Agent 功能支持用户通过自然语言描述需求，AI 自主搜索、导航和获取数据，无需提前知道目标 URL。
  - Agent 提供 spark-1-mini 和 spark-1-pro 两种模型，前者比后者便宜 60%，后者适用于复杂研究任务。
  - Agent 支持 Pydantic schema 定义输出结构，也支持通过 urls 参数限定搜索范围后进行对比分析。
  article_id: e9dbf459bd01dca3
impact_score:
  score: 6.5
  reason: Firecrawl 定位为 AI Agent 的网页数据基础设施层，其开源策略 + MCP 原生集成是一个关键差异化点，直接降低了 AI agent
    获取实时网页数据的技术门槛。96% 网页覆盖率（含 JS 动态页）和 P95 3.4s 延迟的指标虽带有营销色彩，但在同类工具（Jina AI、Browserbase、ScrapingBee）中确实具有竞争力。更重要的是其对
    MCP 协议的一等支持，使其能无缝嵌入 Claude Code、Antigravity 等 AI 客户端生态。这是一款重要的 Developer Tool
    发布，改变了 AI 数据抓取工具的市场格局，但尚未达到行业范式转移的量级。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 开源 + MCP 原生集成，AI Agent 可一键接入网页数据
hype_assessment:
  level: medium
  reason: README 中存在一定 PR 包装，如 'Industry-leading reliability'、'Blazingly fast' 等主观性措辞，且
    96% 覆盖率、P95 3.4s 等基准测试缺乏第三方独立验证。Scrape/interact 的演示示例（Amazon 交互）也偏理想化。但整体来看产品功能确实存在、代码开源可验证、提供了多语言
    SDK 和具体 API 文档，并非空壳炒作，水分属于可控范围。
information_entropy: medium
domain_disruption:
  technical_innovation: Firecrawl 将传统网页抓取的三大范式（搜索→抓取→交互）统一为单一 API 调用链，尤其独特的 'Interact'
    端点允许 AI Agent 通过自然语言指令控制无头浏览器（点击、滚动、输入表单），叠加 MCP 协议的一等集成，使其实际上成为了 AI Agent 的 'Web
    浏览器驱动层'。这种 'AI原生网页交互接口' 的设计思路比传统的 RESTful 爬虫 API 前进了一步。
  business_model: 开源核心 + 托管云服务的双重模式，类似 GitLab/Supabase 路线。但 MCP 协议的集成创造了一个新的分发渠道——Firecrawl
    可被 Claude Code 等 AI 客户端直接发现和调用，本质上将开发者工具的传统 PLG（产品驱动增长）延伸到了 'Agent 驱动分发'（Agent-Driven
    Distribution），即 AI Agent 本身成为产品的推广渠道。
engineering_complexity: production_ready
compound_value:
  score: 7.5
  reason: Firecrawl 以开源 + 托管双模式切入 AI Agent 网页数据管道这一确定性需求。核心投资逻辑有三：第一，AI Agent 规模化落地必须打通实时网页数据，这是不可绕过的基础设施层，需求确定性极高；第二，开源策略带来社区网络效应（GitHub
    Star 增长 → 更多贡献者 → 覆盖率和质量提升 → 更多用户），数据覆盖面和延迟指标（96% 覆盖、P95 3.4s）构成竞争基准；第三，MCP 集成使其成为
    Agent 生态的标准组件，Claude Code 等客户端的原生接入带来渠道锁定效应。但需警惕：该领域护城河偏浅——网页抓取技术本身可复制，Jina AI、Browserbase、Apify
    等竞品环伺；开源版本可能侵蚀付费转化率；长期价值取决于能否从工具演进为 Agent 数据编排平台（而非纯 API 代理）。当前估值适合早期布局，需持续跟踪企业级付费率和
    MCP 生态份额。
value_capture_layer: agent_middleware
moat_impact: democratizes_access
key_beneficiaries:
- Firecrawl
- Anthropic
- OpenCode
- Antigravity
competitive_casualty:
- Jina AI (Reader API)
- Browserbase
- Apify
- 传统网页抓取服务商
market_opportunities:
- AI Agent 开发者可集成 Firecrawl 的 MCP 协议，为自主智能体提供实时网页数据检索与交互能力，显著提升 RAG 系统的知识新鲜度
- 创业者可基于 Firecrawl 的开源架构搭建垂直行业（如电商比价、新闻监控、学术文献追踪）的结构化数据采集服务，以托管 API 形式变现
- 企业 AI 团队可利用其 Agent 自然语言接口和 Schema 输出能力，构建低代码内部情报系统，减少自研爬虫基础设施的维护成本
risk_matrix:
  regulatory: 网页抓取的合规风险突出：大规模抓取可能违反目标网站的 ToS，在 GDPR/CCPA 管辖下抓取个人数据面临隐私诉讼风险；AI 训练语料的版权争议（如纽约时报诉
    OpenAI）的判例趋势可能波及基于抓取内容的商业化应用
  technological: 头部网站（如 Cloudflare、Google）的 anti-bot 技术持续升级，Firecrawl 声称的 96% 覆盖率存在被突破的风险；OpenAI/Google
    等大模型厂商内置原生网页访问能力可能削弱第三方抓取工具的需求
  competitive: 赛道极为拥挤：Browserbase、Apify、ScrapingBee、Bright Data、Crawl4AI 等开源与商业产品直接竞争，Firecrawl
    需持续差异化才能避免价格战与生态挤压
  ethical: 无差别抓取可能采集到未经同意的个人数据或付费墙内容；AI Agent 自主交互（如模拟点击购物网站）可能被滥用于爬虫攻击或数据滥用场景
  additional:
  - 项目严重依赖 GitHub 开源社区的活跃度和贡献者留存，若核心团队转向商业化闭源可能引发社区分叉
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: deep_dive
object_insights:
- object_type: project
  name: firecrawl/firecrawl
  canonical_name: firecrawl/firecrawl
  url: https://github.com/firecrawl/firecrawl
  positioning: Firecrawl 是一个开源网页抓取与交互 API，支持将任意网页转换为 AI 可消费的 Markdown、结构化 JSON 或截图，覆盖
    96% 的网页且 P95 延迟为 3.4 秒。
  technical_signal: 项目提供 Search、Scrape、Interact、Agent、Crawl、Map 和 Batch Scrape 七项核心
    API，内置代理轮换与反爬处理，P95 延迟仅 3.4 秒。
  adoption_signal: 项目在 GitHub 上开源，提供 Python、Node.js、Java 多语言 SDK 及 CLI 工具，并作为托管服务在
    firecrawl.dev 上运营。
  ecosystem_relevance: 支持 MCP 协议集成，通过一条 npx 命令即可将 Firecrawl 接入 Claude Code、Antigravity、OpenCode
    等主流 AI 代理生态。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: Firecrawl 以开源模式提供企业级的网页数据采集能力，覆盖 96% 的网页且延迟优秀，在 AI 代理需要实时网页数据的场景中价值显著，MCP
    协议集成进一步降低了生态接入门槛，值得持续跟踪其在 AI 基础设施领域的渗透进展。
  risk_notes:
  - 开源项目面临来自 Jina AI、Trafilatura 等竞品的持续竞争压力。
  - 托管服务的 API 定价模式依赖客户增长，收入可持续性需长期验证。
  score: 8.0
  article_ids:
  - e9dbf459bd01dca3
  evidence_snippets:
  - Firecrawl 是一个开源 Web 抓取 API，支持 Search、Scrape、Crawl、Map 等核心功能，覆盖 96% 的网页且 P95 延迟为
    3.4 秒。
  - 项目提供 Python、Node.js、Java 多语言 SDK 及 CLI 工具，并作为托管服务在 firecrawl.dev 上运营。
  - Firecrawl 由 Eric Ciarla、Nicolas Camara 和 Caleb Peffer 联合创立，核心创始人均在官网公开列出。
- object_type: product
  name: Firecrawl Agent
  canonical_name: Firecrawl Agent
  url: https://firecrawl.dev
  positioning: Firecrawl Agent 是 Firecrawl 平台中的 AI 自主数据采集功能，用户只需用自然语言描述需求即可自动搜索、导航和提取网页数据。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 需要网页数据采集但无编程经验的非技术用户
  - 希望用自然语言驱动数据管道的 AI 应用开发者
  product_signal: Agent 支持用户通过自然语言描述需求，AI 自主完成搜索、导航和数据采集，无需提前指定目标 URL。
  market_signal: 提供 spark-1-mini 和 spark-1-pro 两种模型选项，前者比后者便宜 60%，覆盖从轻量查询到复杂研究任务的不同预算需求。
  differentiation: Agent 是 Firecrawl 原有 /extract 端点的进化版本，速度更快且可靠性更高，同时支持 Pydantic
    schema 定义输出结构。
  watch_reason: Firecrawl Agent 将 AI 代理能力与网页数据采集深度结合，降低了获取结构化网页数据的门槛，其定价分层策略表明产品化程度较成熟，值得关注其在网页数据
    SaaS 市场的成长路径。
  risk_notes:
  - Agent 功能依赖底层 AI 模型质量，输出结果的准确性和可控性存在不确定性。
  score: 7.0
  article_ids:
  - e9dbf459bd01dca3
  evidence_snippets:
  - Agent 功能支持用户通过自然语言描述需求，AI 自主搜索、导航和获取数据，无需提前知道目标 URL。
  - Agent 提供 spark-1-mini 和 spark-1-pro 两种模型，前者比后者便宜 60%，后者适用于复杂研究任务。
  - Agent 支持 Pydantic schema 定义输出结构，也支持通过 urls 参数限定搜索范围后进行对比分析。
---

**The API to search, scrape, and interact with the web at scale. 🔥** The web context API to find sources, extract content, and turn it into clean Markdown or structured data your agents can ship with. Open source and available as a hosted service.

*Pst. Hey, you, join our stargazers :)*

**Industry-leading reliability**: Covers 96% of the web, including JS-heavy pages — no proxy headaches, just clean data (see benchmarks)**Blazingly fast**: P95 latency of 3.4s across millions of pages, built for real-time agents and dynamic apps**LLM-ready output**: Clean markdown, structured JSON, screenshots, and more — spend fewer tokens, build better AI apps**We handle the hard stuff**: Rotating proxies, orchestration, rate limits, JS-blocked content, and more — zero configuration**Agent ready**: Connect Firecrawl to any AI agent or MCP client with a single command**Media parsing**: Parse and extract content from web-hosted PDFs, DOCX, and more**Actions**: Click, scroll, write, wait, and press before extracting content**Open source**: Developed transparently and collaboratively — join our community

**Core Endpoints**

| Feature | Description |
|---|---|
Search |
Search the web and get full page content from results |
Scrape |
Convert any URL to markdown, HTML, screenshots, or structured JSON |
Interact |
Scrape a page, then interact with it using AI prompts or code |

**More**

| Feature | Description |
|---|---|
Agent |
Automated data gathering, just describe what you need |
Crawl |
Scrape all URLs of a website with a single request |
Map |
Discover all URLs on a website instantly |
Batch Scrape |
Scrape thousands of URLs asynchronously |

Sign up at firecrawl.dev to get your API key. Try the playground to test it out.

Search the web and get full content from results.

```
from firecrawl import Firecrawl
app = Firecrawl(api_key="fc-YOUR_API_KEY")
search_result = app.search("firecrawl", limit=5)
```

**Node.js / cURL / CLI**

**Node.js**

```
import { Firecrawl } from 'firecrawl';
const app = new Firecrawl({apiKey: "fc-YOUR_API_KEY"});
app.search("firecrawl", { limit: 5 })
```

**cURL**

```
curl -X POST 'https://api.firecrawl.dev/v2/search' \
-H 'Authorization: Bearer fc-YOUR_API_KEY' \
-H 'Content-Type: application/json' \
-d '{
"query": "firecrawl",
"limit": 5
}'
```

**CLI**

`firecrawl search "firecrawl" --limit 5`

Output:

```
[
{
"url": "https://firecrawl.dev",
"title": "Firecrawl",
"markdown": "Turn websites into..."
},
{
"url": "https://docs.firecrawl.dev",
"title": "Firecrawl Docs",
"markdown": "# Getting Started..."
}
]
```

Get LLM-ready data from any website — markdown, JSON, screenshots, and more.

```
from firecrawl import Firecrawl
app = Firecrawl(api_key="fc-YOUR_API_KEY")
result = app.scrape('firecrawl.dev')
```

**Node.js / cURL / CLI**

**Node.js**

```
import { Firecrawl } from 'firecrawl';
const app = new Firecrawl({ apiKey: "fc-YOUR_API_KEY" });
app.scrape('firecrawl.dev')
```

**cURL**

```
curl -X POST 'https://api.firecrawl.dev/v2/scrape' \
-H 'Authorization: Bearer fc-YOUR_API_KEY' \
-H 'Content-Type: application/json' \
-d '{
"url": "firecrawl.dev"
}'
```

**CLI**

```
firecrawl scrape https://firecrawl.dev
firecrawl https://firecrawl.dev --only-main-content
```

Output:

```
# Firecrawl
Firecrawl helps AI systems search, scrape, and interact with the web.
## Features
- Search: Find information across the web
- Scrape: Clean data from any page
- Interact: Click, navigate, and operate pages
- Agent: Autonomous data gathering
```


Scrape a page, then interact with it using AI prompts or code.

```
from firecrawl import Firecrawl
app = Firecrawl(api_key="fc-YOUR_API_KEY")
result = app.scrape("https://amazon.com")
scrape_id = result.metadata.scrape_id
app.interact(scrape_id, prompt="Search for 'mechanical keyboard'")
app.interact(scrape_id, prompt="Click the first result")
```

**Node.js / cURL / CLI**

**Node.js**

```
import { Firecrawl } from 'firecrawl';
const app = new Firecrawl({apiKey: "fc-YOUR_API_KEY"});
const result = await app.scrape("https://amazon.com");
await app.interact(result.metadata.scrapeId, {
prompt: "Search for 'mechanical keyboard'"
});
await app.interact(result.metadata.scrapeId, {
prompt: "Click the first result"
});
```

**cURL**

```
# 1. Scrape the page
curl -X POST 'https://api.firecrawl.dev/v2/scrape' \
-H 'Authorization: Bearer fc-YOUR_API_KEY' \
-H 'Content-Type: application/json' \
-d '{"url": "https://amazon.com"}'
# 2. Interact with the page (use scrapeId from step 1)
curl -X POST 'https://api.firecrawl.dev/v2/scrape/SCRAPE_ID/interact' \
-H 'Authorization: Bearer fc-YOUR_API_KEY' \
-H 'Content-Type: application/json' \
-d '{"prompt": "Search for mechanical keyboard"}'
```

**CLI**

```
firecrawl scrape https://amazon.com
firecrawl interact exec --prompt "Search for 'mechanical keyboard'"
firecrawl interact exec --prompt "Click the first result"
```

Output:

```
{
"success": true,
"output": "Keyboard available at $100",
"liveViewUrl": "https://liveview.firecrawl.dev/..."
}
```

Connect Firecrawl to any AI agent or MCP client in minutes.

Give your agent easy access to real-time web data with one command.

`npx -y firecrawl-cli@latest init --all --browser`

Restart your agent after installing. Works with Claude Code, Antigravity, OpenCode, and more.

Connect any MCP-compatible client to the web in seconds.

```
{
"mcpServers": {
"firecrawl-mcp": {
"command": "npx",
"args": ["-y", "firecrawl-mcp"],
"env": {
"FIRECRAWL_API_KEY": "fc-YOUR_API_KEY"
}
}
}
}
```

Are you an AI agent? Fetch this skill to sign up your user, get an API key, and start building with Firecrawl.

`curl -s https://firecrawl.dev/agent-onboarding/SKILL.md`

See the Skill + CLI documentation for all available commands. For MCP, see firecrawl-mcp-server.

**The easiest way to get data from the web.** Describe what you need, and our AI agent searches, navigates, and retrieves it. No URLs required.

Agent is the evolution of our `/extract`

endpoint: faster, more reliable, and doesn't require you to know the URLs upfront.

```
curl -X POST 'https://api.firecrawl.dev/v2/agent' \
-H 'Authorization: Bearer fc-YOUR_API_KEY' \
-H 'Content-Type: application/json' \
-d '{
"prompt": "Find the pricing plans for Notion"
}'
```

Response:

```
{
"success": true,
"data": {
"result": "Notion offers the following pricing plans:\n\n1. Free - $0/month...\n2. Plus - $10/seat/month...\n3. Business - $18/seat/month...",
"sources": ["https://www.notion.so/pricing"]
}
}
```

Use a schema to get structured data:

```
from firecrawl import Firecrawl
from pydantic import BaseModel, Field
from typing import List, Optional
app = Firecrawl(api_key="fc-YOUR_API_KEY")
class Founder(BaseModel):
name: str = Field(description="Full name of the founder")
role: Optional[str] = Field(None, description="Role or position")
class FoundersSchema(BaseModel):
founders: List[Founder] = Field(description="List of founders")
result = app.agent(
prompt="Find the founders of Firecrawl",
schema=FoundersSchema
)
print(result.data)
```

```
{
"founders": [
{"name": "Eric Ciarla", "role": "Co-founder"},
{"name": "Nicolas Camara", "role": "Co-founder"},
{"name": "Caleb Peffer", "role": "Co-founder"}
]
}
```

Focus the agent on specific pages:

```
result = app.agent(
urls=["https://docs.firecrawl.dev", "https://firecrawl.dev/pricing"],
prompt="Compare the features and pricing information"
)
```

Choose between two models based on your needs:

| Model | Cost | Best For |
|---|---|---|
`spark-1-mini` (default) |
60% cheaper | Most tasks |
`spark-1-pro` |
Standard | Complex research, critical data gathering |

```
result = app.agent(
prompt="Compare enterprise features across Firecrawl, Apify, and ScrapingBee",
model="spark-1-pro"
)
```

**When to use Pro:**

- Comparing data across multiple websites
- Extracting from sites with complex navigation or auth
- Research tasks where the agent needs to explore multiple paths
- Critical data where accuracy is paramount

Learn more about Spark models in our Agent documentation.

Crawl an entire website and get content from all pages.

```
curl -X POST 'https://api.firecrawl.dev/v2/crawl' \
-H 'Authorization: Bearer fc-YOUR_API_KEY' \
-H 'Content-Type: application/json' \
-d '{
"url": "https://docs.firecrawl.dev",
"limit": 100,
"scrapeOptions": {
"formats": ["markdown"]
}
}'
```

Returns a job ID:

```
{
"success": true,
"id": "123-456-789",
"url": "https://api.firecrawl.dev/v2/crawl/123-456-789"
}
```

```
curl -X GET 'https://api.firecrawl.dev/v2/crawl/123-456-789' \
-H 'Authorization: Bearer fc-YOUR_API_KEY'
```

```
{
"status": "completed",
"total": 50,
"completed": 50,
"creditsUsed": 50,
"data": [
{
"markdown": "# Page Title\n\nContent...",
"metadata": {"title": "Page Title", "sourceURL": "https://..."}
}
]
}
```

**Note:** The SDKs handle polling automatically for a better developer experience.

Discover all URLs on a website instantly.

```
curl -X POST 'https://api.firecrawl.dev/v2/map' \
-H 'Authorization: Bearer fc-YOUR_API_KEY' \
-H 'Content-Type: application/json' \
-d '{"url": "https://firecrawl.dev"}'
```

Response:

```
{
"success": true,
"links": [
{"url": "https://firecrawl.dev", "title": "Firecrawl", "description": "Turn websites into LLM-ready data"},
{"url": "https://firecrawl.dev/pricing", "title": "Pricing", "description": "Firecrawl pricing plans"},
{"url": "https://firecrawl.dev/blog", "title": "Blog", "description": "Firecrawl blog"}
]
}
```

Find specific URLs within a site:

```
from firecrawl import Firecrawl
app = Firecrawl(api_key="fc-YOUR_API_KEY")
result = app.map("https://firecrawl.dev", search="pricing")
# Returns URLs ordered by relevance to "pricing"
```

Scrape multiple URLs at once:

```
from firecrawl import Firecrawl
app = Firecrawl(api_key="fc-YOUR_API_KEY")
job = app.batch_scrape([
"https://firecrawl.dev",
"https://docs.firecrawl.dev",
"https://firecrawl.dev/pricing"
], formats=["markdown"])
for doc in job.data:
print(doc.metadata.source_url)
```

Our SDKs provide a convenient way to use all Firecrawl features and automatically handle polling for async operations.

Install the SDK:

`pip install firecrawl-py`

```
from firecrawl import Firecrawl
app = Firecrawl(api_key="fc-YOUR_API_KEY")
# Scrape a single URL
doc = app.scrape("https://firecrawl.dev", formats=["markdown"])
print(doc.markdown)
# Use the Agent for autonomous data gathering
result = app.agent(prompt="Find the founders of Stripe")
print(result.data)
# Crawl a website (automatically waits for completion)
docs = app.crawl("https://docs.firecrawl.dev", limit=50)
for doc in docs.data:
print(doc.metadata.source_url, doc.markdown[:100])
# Search the web
results = app.search("best AI data tools 2024", limit=10)
print(results)
```

Install the SDK:

`npm install firecrawl`

```
import { Firecrawl } from 'firecrawl';
const app = new Firecrawl({ apiKey: 'fc-YOUR_API_KEY' });
// Scrape a single URL
const doc = await app.scrape('https://firecrawl.dev', { formats: ['markdown'] });
console.log(doc.markdown);
// Use the Agent for autonomous data gathering
const result = await app.agent({ prompt: 'Find the founders of Stripe' });
console.log(result.data);
// Crawl a website (automatically waits for completion)
const docs = await app.crawl('https://docs.firecrawl.dev', { limit: 50 });
docs.data.forEach(doc => {
console.log(doc.metadata.sourceURL, doc.markdown.substring(0, 100));
});
// Search the web
const results = await app.search('best AI data tools 2024', { limit: 10 });
results.data.web.forEach(result => {
console.log(`${result.title}: ${result.url}`);
});
```

Add the dependency (Gradle/Maven):

```
repositories {
mavenCentral()
maven { url 'https://jitpack.io' }
}
dependencies {
implementation 'com.github.firecrawl:firecrawl-java-sdk:2.0'
}
```

```
import dev.firecrawl.client.FirecrawlClient;
import dev.firecrawl.model.*;
FirecrawlClient client = new FirecrawlClient(
System.getenv("FIRECRAWL_API_KEY"), null, null
);
// Scrape a single URL
ScrapeParams scrapeParams = new ScrapeParams();
scrapeParams.setFormats(new String[]{"markdown"});
FirecrawlDocument doc = client.scrapeURL("https://firecrawl.dev", scrapeParams);
System.out.println(doc.getMarkdown());
// Use the Agent for autonomous data gathering
AgentParams agentParams = new AgentParams("Find the founders of Stripe");
AgentResponse start = client.createAgent(agentParams);
AgentStatusResponse result = client.getAgentStatus(start.getId());
System.out.println(result.getData());
// Crawl a website (polls until completion)
CrawlParams crawlParams = new CrawlParams();
crawlParams.setLimit(50);
CrawlStatusResponse job = client.crawlURL("https://docs.firecrawl.dev", crawlParams, null, 10);
for (FirecrawlDocument page : job.getData()) {
System.out.println(page.getMetadata().get("sourceURL"));
}
// Search the web
SearchParams searchParams = new SearchParams("best AI data tools 2024");
searchParams.setLimit(10);
SearchResponse results = client.search(searchParams);
for (SearchResult r : results.getResults()) {
System.out.println(r.getTitle() + ": " + r.getUrl());
}
```

Add the dependency:

```
def deps do
[
{:firecrawl, "~> 1.0"}
]
end
```

```
# Scrape a URL
{:ok, response} = Firecrawl.scrape_and_extract_from_url(
url: "https://firecrawl.dev",
formats: ["markdown"]
)
# Crawl a website
{:ok, response} = Firecrawl.crawl_urls(
url: "https://docs.firecrawl.dev",
limit: 50
)
# Search the web
{:ok, response} = Firecrawl.search_and_scrape(
query: "best AI data tools 2024",
limit: 10
)
# Map URLs
{:ok, response} = Firecrawl.map_urls(url: "https://example.com")
```

Add the dependency:

```
[dependencies]
firecrawl = "2"
tokio = { version = "1", features = ["macros", "rt-multi-thread"] }
```

```
use firecrawl::{Client, ScrapeOptions, Format, CrawlOptions};
#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
let client = Client::new("fc-YOUR_API_KEY")?;
// Scrape a URL
let document = client.scrape("https://firecrawl.dev", None).await?;
println!("{:?}", document.markdown);
// Crawl a website
let options = CrawlOptions {
limit: Some(50),
..Default::default()
};
let result = client.crawl("https://docs.firecrawl.dev", options).await?;
println!("Crawled {} pages", result.data.len());
// Search the web
let response = client.search("best web scraping tools 2024", None).await?;
println!("{:?}", response.data);
Ok(())
}
```

**Agents & AI Tools**

**Platforms**

**Missing your favorite tool?** Open an issue and let us know!

Firecrawl is open source under the AGPL-3.0 license. The cloud version at firecrawl.dev includes additional features:

To run locally, see the Contributing Guide. To self-host, see Self-Hosting Guide.

We love contributions! Please read our Contributing Guide before submitting a pull request.

This project is primarily licensed under the GNU Affero General Public License v3.0 (AGPL-3.0). The SDKs and some UI components are licensed under the MIT License. See the LICENSE files in specific directories for details.

**It is the sole responsibility of end users to respect websites' policies when scraping.** Users are advised to adhere to applicable privacy policies and terms of use. By default, Firecrawl respects robots.txt directives. By using Firecrawl, you agree to comply with these conditions.