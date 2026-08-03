---
title: tradesdontlie/tradingview-mcp
source: https://github.com/tradesdontlie/tradingview-mcp
author: []
published: ''
created: '2026-07-22'
manifest_dates:
- '2026-07-22'
description: 'AI-assisted TradingView chart analysis — connect Claude Code to your
  TradingView Desktop for personal workflow automationTradingView MCP Bridge Personal
  AI assistant for your TradingView Desktop charts. Connects Claude Code to your locally
  running TradingView app via Chrome DevTools Protocol for AI-assisted chart analysis,
  Pine Script development, and workflow automation. Warning This tool is not affiliated
  with, endorsed by, or associated with TradingView Inc. It interacts with your locally
  running TradingView Desktop application via Chrome DevTools Protocol. Review the
  Disclaimer before use. Important Requires a valid TradingView subscription. This
  tool does not bypass or circumvent any TradingView paywall or access control. It
  reads from and controls the TradingView Desktop app already running on your machine.
  Note All data processing occurs locally on your machine. No TradingView data is
  transmitted, stored, or redistributed externally by this tool. Caution This tool
  accesses undocumented internal TradingView APIs via the Electron debug interface.
  These can change or break without notice in any TradingView update. Pin your TradingView
  Desktop version if stability matters to you. How It Works (and why it''s safe to
  run) This tool does not connect to TradingView''s servers, modify any TradingView
  files, or intercept any network traffic. It communicates exclusively with your locally
  running TradingView Desktop instance via Chrome DevTools Protocol (CDP) — a standard
  debugging interface built into all Chromium/Electron applications by Google, including
  VS Code, Slack, and Discord. The debug port is disabled by default and must be explicitly
  enabled by you using a standard Chromium flag (--remote-debugging-port=9222). Nothing
  happens without that deliberate step. What This Tool Does Not Do Connect to TradingView''s
  servers or APIs Store, transmit, or redistribute any market data Work without a
  valid TradingView subscription and installed Desktop app Bypass any TradingView
  paywall or access restriction Execute real trades (chart interaction only) Work
  if TradingView changes their internal Electron structure Research Context This project
  explores an open research question: how can LLM-based agents interact with professional
  trading interfaces to support human decision-making? Specifically it investigates:
  How structured tool APIs (MCP) can bridge LLMs and stateful desktop financial applications
  What latency, context, and reliability constraints emerge when an agent operates
  on live chart data How agents handle ambiguous financial UI state (e.g. interpreting
  Pine Script output, reading indicator tables) Whether natural language is an effective
  interface for chart navigation and Pine Script development The failure modes of
  LLM agents operating in real-time data environments This is not a trading bot. It
  is an interface layer that makes a trading application legible to an LLM agent,
  allowing researchers and developers to study human-AI collaboration in financial
  workflows. See RESEARCH.md for open questions, findings, and related work. Prerequisites
  TradingView Desktop app (paid subscription required for real-time data) Node.js
  18+ Claude Code with MCP support (for MCP tools) or any terminal (for CLI) macOS,
  Windows, or Linux What It Does Gives your AI assistant eyes and hands on your own
  chart: Pine Script development — write, inject, compile, debug, and iterate on scripts
  with AI assistance Chart navigation — change symbols, timeframes, zoom to dates,
  add/remove indicators Visual analysis — read your chart''s indicator values, price
  levels, and annotations Draw on charts — trend lines, horizontal lines, rectangles,
  text annotations Manage alerts — create, list, and delete price alerts Replay practice
  — step through historical bars, practice entries/exits Screenshots — capture chart
  state for AI visual analysis Multi-pane layouts — set up 2x2, 3x1, etc. grids with
  different symbols per pane Monitor your chart — stream JSONL from your locally running
  chart for local monitoring scripts CLI access — every MCP tool is also a tv CLI
  command, pipe-friendly with JSON output Launch TradingView — auto-detect and launch
  with debug mode from any platform Install with Claude Code Paste this into Claude
  Code and it will handle the rest: Install the TradingView MCP server. Clone https://github.com/tradesdontlie/tradingview-mcp.git,
  run npm install, add it to my MCP config at ~/.claude/.mcp.json, and launch TradingView
  with the debug port. Then verify the connection with tv_health_check. Or follow
  the manual steps below. Quick Start 1. Install git clone https://github.com/tradesdontlie/tradingview-mcp.git
  cd tradingview-mcp npm install 2. Launch TradingView with CDP TradingView Desktop
  must be running with Chrome DevTools Protocol enabled on port 9222. Mac: ./scripts/launch_tv_debug_mac.sh
  Windows: scripts\launch_tv_debug.bat Linux: ./scripts/launch_tv_debug_linux.sh Or
  launch manually on any platform: /path/to/TradingView --remote-debugging-port=9222
  Or use the MCP tool (auto-detects your install): "Use tv_launch to start TradingView
  in debug mode" 3. Add to Claude Code Add to your Claude Code MCP config (~/.claude/.mcp.json
  or project .mcp.json): { "mcpServers": { "tradingview": { "command": "node", "args":
  ["/path/to/tradingview-mcp/src/server.js"] } } } Replace /path/to/tradingview-mcp
  with your actual path. 4. Verify Ask Claude: "Use tv_health_check to verify TradingView
  is connected" CLI Every MCP tool is also accessible as a tv CLI command. All output
  is JSON for piping with jq. # Install globally (optional) npm link # Or run directly
  node src/cli/index.js <command> Quick Examples tv status # check connection tv quote
  # current price tv symbol AAPL # change symbol tv ohlcv --summary # price summary
  tv screenshot -r chart # capture chart tv pine compile # compile Pine Script tv
  pane layout 2x2 # 4-chart grid tv pane symbol 1 ES1! # set pane symbol tv stream
  quote | jq ''.close'' # monitor price changes All Commands tv status / launch /
  state / symbol / timeframe / type / info / search tv quote / ohlcv / values tv data
  lines/labels/tables/boxes/strategy/trades/equity/depth/indicator tv pine get/set/compile/analyze/check/save/new/open/list/errors/console
  tv draw shape/list/get/remove/clear tv alert list/create/delete tv watchlist get/add
  tv indicator add/remove/toggle/set/get tv layout list/switch tv pane list/layout/focus/symbol
  tv tab list/new/close/switch tv replay start/step/stop/status/autoplay/trade tv
  stream quote/bars/values/lines/labels/tables/all tv ui click/keyboard/hover/scroll/find/eval/type/panel/fullscreen/mouse
  tv screenshot / discover / ui-state / range / scroll Streaming The tv stream commands
  poll your locally running TradingView Desktop instance at regular intervals via
  Chrome DevTools Protocol on localhost. No connection is made to TradingView''s servers.
  All data stays on your machine. Warning Programmatic consumption of TradingView
  data may conflict with their Terms of Use regardless of the data source. You are
  solely responsible for ensuring your usage complies. tv stream quote # price tick
  monitoring tv stream bars # bar-by-bar updates tv stream values # indicator value
  monitoring tv stream lines --filter "NY Levels" # price level monitoring tv stream
  tables --filter Profiler # table data monitoring tv stream all # all panes at once
  (multi-symbol) How Claude Knows Which Tool to Use Claude reads CLAUDE.md automatically
  when working in this project. It contains a complete decision tree: You say... Claude
  uses... "What''s on my chart?" chart_get_state → data_get_study_values → quote_get
  "What levels are showing?" data_get_pine_lines → data_get_pine_labels "Read the
  session table" data_get_pine_tables with study_filter "Give me a full analysis"
  quote_get → data_get_study_values → data_get_pine_lines → data_get_pine_labels →
  data_get_pine_tables → data_get_ohlcv (summary) → capture_screenshot "Switch to
  AAPL daily" chart_set_symbol → chart_set_timeframe "Write a Pine Script for..."
  pine_set_source → pine_smart_compile → pine_get_errors "Start replay at March 1st"
  replay_start → replay_step → replay_trade "Set up a 4-chart grid" pane_set_layout
  → pane_set_symbol for each pane "Draw a level at 24500" draw_shape (horizontal_line)
  "Take a screenshot" capture_screenshot Tool Reference (78 MCP tools) Chart Reading
  Tool When to use Output size chart_get_state First call — get symbol, timeframe,
  all indicator names + IDs ~500B data_get_study_values Read current RSI, MACD, BB,
  EMA values from all indicators ~500B quote_get Get latest price, OHLC, volume ~200B
  data_get_ohlcv Get price bars. Use summary: true for compact stats 500B (summary)
  / 8KB (100 bars) Custom Indicator Data (Pine Drawings) Read line.new(), label.new(),
  table.new(), box.new() output from any visible Pine indicator. Tool When to use
  Output size data_get_pine_lines Read horizontal price levels (support/resistance,
  session levels) ~1-3KB data_get_pine_labels Read text annotations + prices ("PDH
  24550", "Bias Long") ~2-5KB data_get_pine_tables Read data tables (session stats,
  analytics dashboards) ~1-4KB data_get_pine_boxes Read price zones / ranges as {high,
  low} pairs ~1-2KB Always use study_filter to target a specific indicator: study_filter:
  "Profiler". Chart Control Tool What it does chart_set_symbol Change ticker (BTCUSD,
  AAPL, ES1!, NYMEX:CL1!) chart_set_timeframe Change resolution (1, 5, 15, 60, D,
  W, M) chart_set_type Change style (Candles, HeikinAshi, Line, Area, Renko) chart_manage_indicator
  Add/remove indicators. Use full names: "Relative Strength Index" not "RSI" chart_scroll_to_date
  Jump to a date (ISO: "2025-01-15") chart_set_visible_range Zoom to exact range (unix
  timestamps) symbol_info / symbol_search Symbol metadata and search indicator_set_inputs
  / indicator_toggle_visibility Change indicator settings, show/hide Multi-Pane Layouts
  Tool What it does pane_list List all panes with symbols and active state pane_set_layout
  Change grid: s, 2h, 2v, 2x2, 4, 6, 8 pane_focus Focus a specific pane by index pane_set_symbol
  Set symbol on any pane Tab Management Tool What it does tab_list List open chart
  tabs tab_new / tab_close Open/close tabs tab_switch Switch to a tab by index Pine
  Script Development Tool Step pine_set_source 1. Inject code into editor pine_smart_compile
  2. Compile with auto-detection + error check pine_get_errors 3. Read compilation
  errors if any pine_get_console 4. Read log.info() output pine_save 5. Save to TradingView
  cloud pine_get_source Read current script (warning: can be 200KB+ for complex scripts)
  pine_new Create blank indicator/strategy/library pine_open / pine_list_scripts Open
  or list saved scripts pine_analyze Offline static analysis (no chart needed) pine_check
  Server-side compile check (no chart needed) Replay Mode Tool Step replay_start Enter
  replay at a date replay_step Advance one bar replay_autoplay Auto-advance (set speed
  in ms) replay_trade Buy/sell/close positions replay_status Check position, P&L,
  date replay_stop Return to realtime Drawing, Alerts, UI Automation Tool What it
  does draw_shape Draw horizontal_line, trend_line, rectangle, text draw_list / draw_remove_one
  / draw_clear Manage drawings alert_create / alert_list / alert_delete Manage price
  alerts capture_screenshot Screenshot (regions: full, chart, strategy_tester) batch_run
  Run action across multiple symbols/timeframes watchlist_get / watchlist_add Read/modify
  watchlist layout_list / layout_switch Manage saved layouts ui_open_panel / ui_click
  / ui_evaluate UI automation tv_launch / tv_health_check / tv_discover Connection
  management Context Management Tools return compact output by default to minimize
  context usage. For a typical "analyze my chart" workflow, total context is ~5-10KB
  instead of ~80KB. Feature How it saves context Pine lines Returns deduplicated price
  levels only, not every line object Pine labels Capped at 50 per study, text+price
  only Pine tables Pre-formatted row strings, no cell metadata Pine boxes Deduplicated
  {high, low} zones only OHLCV summary mode Stats + last 5 bars instead of all bars
  Indicator inputs Encrypted/encoded blobs auto-filtered verbose: true Pass on any
  pine tool to get raw data with IDs/colors when needed study_filter Target one indicator
  instead of scanning all Finding TradingView on Your System Launch scripts and tv_launch
  auto-detect TradingView. If auto-detection fails: Platform Common Locations Mac
  /Applications/TradingView.app/Contents/MacOS/TradingView Windows %LOCALAPPDATA%\TradingView\TradingView.exe,
  %PROGRAMFILES%\WindowsApps\TradingView*\TradingView.exe Linux /opt/TradingView/tradingview,
  ~/.local/share/TradingView/TradingView, /snap/tradingview/current/tradingview The
  key flag: --remote-debugging-port=9222 Testing # Requires TradingView running with
  --remote-debugging-port=9222 npm test 29 tests covering: Pine Script static analysis,
  server-side compilation, and CLI routing. Architecture Claude Code ←→ MCP Server
  (stdio) ←→ CDP (port 9222) ←→ TradingView Desktop (Electron) Transport: MCP over
  stdio (84 tools) + CLI (tv command, 30 commands with 66 subcommands) Connection:
  Chrome DevTools Protocol on localhost:9222 Streaming: Poll-and-diff loop with deduplication,
  JSONL output to stdout No dependencies beyond @modelcontextprotocol/sdk and chrome-remote-interface
  Attributions This project is not affiliated with, endorsed by, or associated with:
  TradingView Inc. — TradingView is a trademark of TradingView Inc. Anthropic — Claude
  and Claude Code are trademarks of Anthropic, PBC. This tool is an independent MCP
  server that connects to Claude Code via the standard MCP protocol. It does not contain
  or modify any Anthropic software. Disclaimer This project is provided for personal,
  educational, and research purposes only. How this tool works: This tool uses Chrome
  DevTools Protocol (CDP), the standard debugging interface built into Chromium-based
  applications. It does not reverse engineer any proprietary TradingView protocol,
  connect to TradingView''s servers, or bypass any access controls. The debug port
  must be explicitly enabled by the user via a standard Chromium command-line flag
  (--remote-debugging-port=9222). By using this software, you acknowledge and agree
  that: You are solely responsible for ensuring your use of this tool complies with
  TradingView''s Terms of Use and all applicable laws. TradingView''s Terms of Use
  restrict automated data collection, scraping, and non-display usage of their platform
  and data. This tool uses Chrome DevTools Protocol to programmatically interact with
  the TradingView Desktop app, which may conflict with those terms. You assume all
  risk associated with using this tool. The authors are not responsible for any account
  bans, suspensions, legal actions, or other consequences resulting from its use.
  This tool must not be used for, including but not limited to: Redistributing, reselling,
  or commercially exploiting TradingView''s market data Circumventing TradingView''s
  access controls or subscription restrictions Performing automated trading or algorithmic
  decision-making using extracted data Violating the intellectual property rights
  of Pine Script indicator authors Connecting to TradingView''s servers or infrastructure
  (all access is via the locally running Desktop app) The streaming functionality
  monitors your locally running TradingView Desktop instance only. It does not connect
  to TradingView''s servers or extract data from TradingView''s infrastructure. Market
  data accessed through this tool remains subject to exchange and data provider licensing
  terms. Do not redistribute, store, or commercially exploit any data obtained through
  this tool. This tool accesses internal, undocumented TradingView application interfaces
  that may change or break at any time without notice. Use at your own risk. If you
  are unsure whether your intended use complies with TradingView''s terms, do not
  use this tool. License MIT — see LICENSE for details. The MIT license applies to
  the source code of this project only. It does not grant any rights to TradingView''s
  software, data, trademarks, or intellectual property.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: eda52afc2779cedf
source_type: community_discussion
tldr: tradesdontlie/tradingview-mcp 是一个开源 MCP 服务器，通过 Chrome DevTools Protocol 将 AI
  助手连接到 TradingView Desktop，实现 AI 辅助图表分析、Pine Script 开发和流程自动化，所有数据均在本地处理。
objective_summary: tradesdontlie 在 GitHub 上发布了 tradingview-mcp 项目，这是一个 MCP 服务器，通过
  Chrome DevTools Protocol 将 LLM 代理连接到用户本地运行的 TradingView Desktop 应用程序。该项目提供 Pine
  Script 开发、图表导航、视觉分析、画图工具、警报管理和回放练习等功能，所有数据处理均在本地完成，不向外部传输任何数据。它同时提供 MCP 工具接口和 CLI
  命令两种交互方式，需要用户手动启用调试端口并拥有有效的 TradingView 订阅。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - TradingView Inc.
  technologies:
  - MCP
  - CDP
  - Pine Script
  - Chrome DevTools Protocol
  key_people: []
key_logic_flow:
- 该项目是一个开源 MCP 服务器，通过 Chrome DevTools Protocol 将 AI 助手连接到本地运行的 TradingView Desktop，实现
  AI 辅助图表分析、Pine Script 开发和流程自动化。
- 项目不隶属于 TradingView Inc.，需要用户拥有有效的 TradingView 订阅并手动启用调试端口（--remote-debugging-port=9222）才能使用。
- 所有数据处理均在本地机器完成，不涉及 TradingView 服务器连接，也不执行实际交易操作，仅进行图表交互。
- 该项目探索 LLM 代理如何与专业交易界面交互以支持人类决策的研究问题，包括延迟、上下文和可靠性约束。
- 该工具提供 MCP 工具接口和 CLI 命令两种交互方式，涵盖图表操作、指标读取、Pine Script 开发、回放练习和多窗格布局等功能。
- TradingView Desktop 内部 Electron 结构变化可能导致工具失效，建议用户在需要稳定性时固定 TradingView Desktop 版本。
object_mentions:
- object_type: project
  name: tradesdontlie/tradingview-mcp
  canonical_name: tradesdontlie/tradingview-mcp
  url: https://github.com/tradesdontlie/tradingview-mcp
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 该项目是一个开源 MCP 服务器，通过 Chrome DevTools Protocol 将 AI 助手连接到本地运行的 TradingView Desktop，实现
    AI 辅助图表分析。
  - 项目提供 Pine Script 开发、图表导航、视觉分析、画图工具、警报管理、回放练习和截图等完整功能集。
  - 所有数据处理均在本地完成，不向外部传输任何 TradingView 数据，且不执行实际交易操作。
  article_id: eda52afc2779cedf
- object_type: product
  name: Claude Code
  canonical_name: Claude Code
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - README 提供了粘贴到 Claude Code 即可自动完成安装和 MCP 配置的一键集成指令。
  - 该项目专门为 Claude Code 的 MCP 支持设计了集成方案，Claude Code 可自动读取项目中的 CLAUDE.md 决策树。
  article_id: eda52afc2779cedf
- object_type: product
  name: TradingView Desktop
  canonical_name: TradingView Desktop
  url: null
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - TradingView Desktop 是一个基于 Electron 的桌面应用程序，需要有效的 TradingView 订阅才能使用实时数据。
  - 该工具通过 Chrome DevTools Protocol 与 TradingView Desktop 通信，后者必须手动使用调试端口标志启动。
  article_id: eda52afc2779cedf
extract_result: success
impact_score:
  score: 5.0
  reason: 该项目是 MCP 生态中首个将 LLM Agent 与专业交易桌面端（TradingView Desktop）对接的开源实现，填补了 AI 辅助金融技术分析的工程空白。但考虑到其依赖
    Chrome DevTools Protocol 操作 Electron 内部 DOM 结构、明确声明不隶属于 TradingView、且存在版本兼容性风险，短期内更多是工具链层面的补充而非行业颠覆。评分
    5.0：对量化交易和 Pine Script 开发者社区有实际价值，但离主流采用和商业闭环还有较大距离。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: MCP 协议与本地桌面金融工具的集成模式，以及 AI 辅助 Pine Script 开发的可行性
hype_assessment:
  level: low
  reason: 项目 README 措辞克制，明确标注了 'not affiliated with TradingView Inc.'、'uses undocumented
    internal APIs'、'can break without notice' 等风险声明，并使用 'explores an open research
    question' 等实事求是的表述，未出现 '颠覆'、'革命性' 等 PR 滥用词汇。
information_entropy: high
domain_disruption:
  technical_innovation: 通过 Chrome DevTools Protocol 桥接 LLM Agent 与 Electron 桌面金融应用的工程模式，将
    MCP 协议实战落地到交易场景，为 AI 与专业桌面工具交互提供了可复用的参考架构。
  business_model: 无直接影响。该项目是开源社区作品，不涉及商业模式重塑，但可能催生付费的 AI 交易助手插件或定制化 MCP 服务器服务。
engineering_complexity: prototype
compound_value:
  score: 6.0
  reason: 该项目本身是一个脆弱的开源适配器，依赖 TradingView 未文档化的 Electron 内部 API，随时可能因 TradingView
    更新而失效，不具备独立商业价值。但其代表的核心模式——通过 MCP 协议将 AI Agent 与专业桌面金融应用深度耦合——具有显著的长期复利潜力。金融交易是
    AI Agent 最有付费意愿的高价值场景之一，且 TradingView 拥有庞大的零售与半专业交易者用户基础。一旦 MCP 生态成熟，这类桥接层将成为金融
    AI 工作流的事实基础设施。但 6 分的上限源于：(1) 项目没有商业模式且难以私有化变现；(2) 技术路径依赖 CDP 这一非官方接口，TradingView
    官方若推出原生 AI 功能将直接封死空间；(3) 开源替代品极易复制，网络效应极弱。长期看，价值不在这个具体项目，而在它所验证的「MCP + 专业桌面应用」范式。
value_capture_layer: agent_middleware
moat_impact: democratizes_access
key_beneficiaries:
- TradingView
- Anthropic
- MCP 生态系统
- 零售交易者
competitive_casualty:
- 传统图表形态识别 SaaS
- Pine Script 自由职业开发者
- 闭源交易自动化中间件
market_opportunities:
- 开发者可基于 MCP + Chrome DevTools Protocol 模式，将 AI 助手连接到其他 Electron 桌面应用（如 Slack、Discord、VS
  Code），开辟桌面自动化工具赛道
- 面向量化交易者和技术分析师，提供 AI 辅助 Pine Script 开发和策略回测的 SaaS 或插件产品，降低策略开发门槛
- 该项目的 CDP 桥接模式可复制到 Bloomberg Terminal、MetaTrader 等金融终端，孵化金融行业的 AI Agent 中间件创业机会
risk_matrix:
  regulatory: TradingView 可能通过用户协议或技术手段禁止使用非官方调试接口访问其桌面应用，存在合规摩擦；若工具被用于自动化高频查询或市场数据批量提取，可能触发服务条款违约风险
  technological: 该工具依赖 TradingView Desktop 的 Electron 内部结构（通过 CDP 访问未文档化 API），TradingView
    任何版本更新都可能导致工具失效，强烈依赖用户固定版本；Chrome DevTools Protocol 作为标准调试接口本身稳定，但上层应用的内部 DOM/CSS
    结构变更会破坏工具功能
  competitive: TradingView 自身可能推出官方 AI 助手功能，直接挤压第三方工具的生存空间；其他 MCP 金融工具（如 Bloomberg
    MCP、雪球 MCP）可能形成生态竞争，细分市场较小难以支撑多个竞品
  ethical: 该工具明确声明不上传外部数据、不执行实际交易，数据完全本地处理，伦理风险较低；但若被第三方改造为自动化交易执行层，可能带来金融公平性和算法交易监管问题
  additional:
  - 项目为个人维护的开源项目，长期维护和兼容性保障不确定；依赖用户具备 TradingView 付费订阅和手动配置调试端口的能力，限制了用户规模
confidence:
  impact: medium
  compound: low
  hype: medium
actionable_insight: speculative_watch
object_insights:
- object_type: project
  name: tradesdontlie/tradingview-mcp
  canonical_name: tradesdontlie/tradingview-mcp
  url: https://github.com/tradesdontlie/tradingview-mcp
  positioning: 开源 MCP 服务器，通过 Chrome DevTools Protocol 将 AI 助手连接到本地运行的 TradingView
    Desktop，为交易者提供 AI 辅助的图表分析、Pine Script 开发和流程自动化能力。
  technical_signal: 通过 Chrome DevTools Protocol 与 TradingView Desktop 的 Electron 调试接口通信，不依赖
    TradingView 官方 API 或网络拦截，所有数据处理均在本地完成。
  adoption_signal: README 提供一键集成指令，用户粘贴到 Claude Code 即可自动完成安装和 MCP 配置，降低了将 AI 引入交易工作流的技术门槛。
  ecosystem_relevance: 作为 MCP 生态中连接金融交易桌面应用的代表性项目，探索了结构化工具接口如何桥接大语言模型与有状态桌面金融应用。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 该项目探索了 LLM 代理通过 MCP 协议与专业金融桌面交互的可行性和边界，涉及 Pine Script 辅助开发、实时图表分析、人机协作决策等研究问题，对
    AI 在量化金融领域的应用具有参考价值。
  risk_notes:
  - TradingView Desktop 的 Electron 内部结构可能随更新变化，导致工具失效，建议用户在需要稳定性时固定版本。
  - 该工具访问的是 TradingView 未公开的内部调试接口，并非官方 API，长期兼容性存在不确定性。
  - 项目明确声明不执行实际交易操作，仅进行图表交互，金融决策仍需人类用户最终确认。
  score: 6.0
  article_ids:
  - eda52afc2779cedf
  evidence_snippets:
  - 该项目是一个开源 MCP 服务器，通过 Chrome DevTools Protocol 将 AI 助手连接到本地运行的 TradingView Desktop，实现
    AI 辅助图表分析。
  - 项目提供 Pine Script 开发、图表导航、视觉分析、画图工具、警报管理、回放练习和截图等完整功能集。
  - 所有数据处理均在本地完成，不向外部传输任何 TradingView 数据，且不执行实际交易操作。
- object_type: product
  name: Claude Code
  canonical_name: Claude Code
  url: null
  positioning: Anthropic 推出的 AI 编程助手，具备 MCP 协议集成能力，可通过 CLAUDE.md 自动读取项目上下文并调用外部工具，扩展
    AI 辅助开发的应用边界。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - AI 开发者
  - 金融技术开发者
  - 量化交易研究者
  product_signal: 支持 MCP 服务器集成，用户可通过粘贴指令让 Claude Code 自动完成外部工具的安装和 MCP 配置，大幅简化了开发环境的搭建流程。
  market_signal: null
  differentiation: 通过 MCP 协议连接外部工具和桌面应用的能力，使其从代码补全工具扩展为可操作交易软件等复杂界面的 AI 代理，超越了传统编程助手的定位。
  watch_reason: Claude Code 通过 MCP 协议将 AI 编程助手的能力延伸到专业桌面应用操作层面，tradingview-mcp 项目展示了其在金融交易场景中的实际应用潜力，值得关注其开发者工具生态的持续演进。
  risk_notes:
  - MCP 生态仍处于早期发展阶段，外部工具集成的稳定性和质量高度依赖第三方项目的持续维护。
  - Claude Code 作为闭源产品，其 MCP 集成能力的演进方向和更新节奏由 Anthropic 单方控制。
  score: 7.0
  article_ids:
  - eda52afc2779cedf
  evidence_snippets:
  - README 提供了粘贴到 Claude Code 即可自动完成安装和 MCP 配置的一键集成指令。
  - 该项目专门为 Claude Code 的 MCP 支持设计了集成方案，Claude Code 可自动读取项目中的 CLAUDE.md 决策树。
---

Personal AI assistant for your TradingView Desktop charts. Connects Claude Code to your locally running TradingView app via Chrome DevTools Protocol for AI-assisted chart analysis, Pine Script development, and workflow automation.

Warning

**This tool is not affiliated with, endorsed by, or associated with TradingView Inc.** It interacts with your locally running TradingView Desktop application via Chrome DevTools Protocol. Review the Disclaimer before use.

Important

**Requires a valid TradingView subscription.** This tool does not bypass or circumvent any TradingView paywall or access control. It reads from and controls the TradingView Desktop app already running on your machine.

Note

**All data processing occurs locally on your machine.** No TradingView data is transmitted, stored, or redistributed externally by this tool.

Caution

This tool accesses undocumented internal TradingView APIs via the Electron debug interface. These can change or break without notice in any TradingView update. Pin your TradingView Desktop version if stability matters to you.

This tool does not connect to TradingView's servers, modify any TradingView files, or intercept any network traffic. It communicates exclusively with your locally running TradingView Desktop instance via Chrome DevTools Protocol (CDP) — a standard debugging interface built into all Chromium/Electron applications by Google, including VS Code, Slack, and Discord.

The debug port is disabled by default and must be explicitly enabled by you using a standard Chromium flag (`--remote-debugging-port=9222`

). Nothing happens without that deliberate step.

- Connect to TradingView's servers or APIs
- Store, transmit, or redistribute any market data
- Work without a valid TradingView subscription and installed Desktop app
- Bypass any TradingView paywall or access restriction
- Execute real trades (chart interaction only)
- Work if TradingView changes their internal Electron structure

This project explores an open research question: **how can LLM-based agents interact with professional trading interfaces to support human decision-making?**

Specifically it investigates:

- How structured tool APIs (MCP) can bridge LLMs and stateful desktop financial applications
- What latency, context, and reliability constraints emerge when an agent operates on live chart data
- How agents handle ambiguous financial UI state (e.g. interpreting Pine Script output, reading indicator tables)
- Whether natural language is an effective interface for chart navigation and Pine Script development
- The failure modes of LLM agents operating in real-time data environments

This is not a trading bot. It is an interface layer that makes a trading application legible to an LLM agent, allowing researchers and developers to study human-AI collaboration in financial workflows.

See RESEARCH.md for open questions, findings, and related work.

**TradingView Desktop app**(paid subscription required for real-time data)**Node.js 18+****Claude Code**with MCP support (for MCP tools) or any terminal (for CLI)**macOS, Windows, or Linux**

Gives your AI assistant eyes and hands on your own chart:

**Pine Script development**— write, inject, compile, debug, and iterate on scripts with AI assistance**Chart navigation**— change symbols, timeframes, zoom to dates, add/remove indicators**Visual analysis**— read your chart's indicator values, price levels, and annotations**Draw on charts**— trend lines, horizontal lines, rectangles, text annotations**Manage alerts**— create, list, and delete price alerts**Replay practice**— step through historical bars, practice entries/exits**Screenshots**— capture chart state for AI visual analysis**Multi-pane layouts**— set up 2x2, 3x1, etc. grids with different symbols per pane**Monitor your chart**— stream JSONL from your locally running chart for local monitoring scripts**CLI access**— every MCP tool is also a`tv`

CLI command, pipe-friendly with JSON output**Launch TradingView**— auto-detect and launch with debug mode from any platform

Paste this into Claude Code and it will handle the rest:

Install the TradingView MCP server. Clone https://github.com/tradesdontlie/tradingview-mcp.git, run npm install, add it to my MCP config at ~/.claude/.mcp.json, and launch TradingView with the debug port. Then verify the connection with tv_health_check.


Or follow the manual steps below.

```
git clone https://github.com/tradesdontlie/tradingview-mcp.git
cd tradingview-mcp
npm install
```

TradingView Desktop must be running with Chrome DevTools Protocol enabled on port 9222.

**Mac:**

`./scripts/launch_tv_debug_mac.sh`

**Windows:**

`scripts\launch_tv_debug.bat`

**Linux:**

`./scripts/launch_tv_debug_linux.sh`

**Or launch manually on any platform:**

`/path/to/TradingView --remote-debugging-port=9222`

**Or use the MCP tool** (auto-detects your install):

"Use tv_launch to start TradingView in debug mode"


Add to your Claude Code MCP config (`~/.claude/.mcp.json`

or project `.mcp.json`

):

```
{
"mcpServers": {
"tradingview": {
"command": "node",
"args": ["/path/to/tradingview-mcp/src/server.js"]
}
}
}
```

Replace `/path/to/tradingview-mcp`

with your actual path.

Ask Claude: *"Use tv_health_check to verify TradingView is connected"*

Every MCP tool is also accessible as a `tv`

CLI command. All output is JSON for piping with `jq`

.

```
# Install globally (optional)
npm link
# Or run directly
node src/cli/index.js <command>
```

```
tv status # check connection
tv quote # current price
tv symbol AAPL # change symbol
tv ohlcv --summary # price summary
tv screenshot -r chart # capture chart
tv pine compile # compile Pine Script
tv pane layout 2x2 # 4-chart grid
tv pane symbol 1 ES1! # set pane symbol
tv stream quote | jq '.close' # monitor price changes
```

```
tv status / launch / state / symbol / timeframe / type / info / search
tv quote / ohlcv / values
tv data lines/labels/tables/boxes/strategy/trades/equity/depth/indicator
tv pine get/set/compile/analyze/check/save/new/open/list/errors/console
tv draw shape/list/get/remove/clear
tv alert list/create/delete
tv watchlist get/add
tv indicator add/remove/toggle/set/get
tv layout list/switch
tv pane list/layout/focus/symbol
tv tab list/new/close/switch
tv replay start/step/stop/status/autoplay/trade
tv stream quote/bars/values/lines/labels/tables/all
tv ui click/keyboard/hover/scroll/find/eval/type/panel/fullscreen/mouse
tv screenshot / discover / ui-state / range / scroll
```


The `tv stream`

commands poll your locally running TradingView Desktop instance at regular intervals via Chrome DevTools Protocol on localhost.

No connection is made to TradingView's servers. All data stays on your machine.

Warning

Programmatic consumption of TradingView data may conflict with their Terms of Use regardless of the data source. You are solely responsible for ensuring your usage complies.

```
tv stream quote # price tick monitoring
tv stream bars # bar-by-bar updates
tv stream values # indicator value monitoring
tv stream lines --filter "NY Levels" # price level monitoring
tv stream tables --filter Profiler # table data monitoring
tv stream all # all panes at once (multi-symbol)
```

Claude reads `CLAUDE.md`

automatically when working in this project. It contains a complete decision tree:

| You say... | Claude uses... |
|---|---|
| "What's on my chart?" | `chart_get_state` → `data_get_study_values` → `quote_get` |
| "What levels are showing?" | `data_get_pine_lines` → `data_get_pine_labels` |
| "Read the session table" | `data_get_pine_tables` with `study_filter` |
| "Give me a full analysis" | `quote_get` → `data_get_study_values` → `data_get_pine_lines` → `data_get_pine_labels` → `data_get_pine_tables` → `data_get_ohlcv` (summary) → `capture_screenshot` |
| "Switch to AAPL daily" | `chart_set_symbol` → `chart_set_timeframe` |
| "Write a Pine Script for..." | `pine_set_source` → `pine_smart_compile` → `pine_get_errors` |
| "Start replay at March 1st" | `replay_start` → `replay_step` → `replay_trade` |
| "Set up a 4-chart grid" | `pane_set_layout` → `pane_set_symbol` for each pane |
| "Draw a level at 24500" | `draw_shape` (horizontal_line) |
| "Take a screenshot" | `capture_screenshot` |

| Tool | When to use | Output size |
|---|---|---|
`chart_get_state` |
First call — get symbol, timeframe, all indicator names + IDs | ~500B |
`data_get_study_values` |
Read current RSI, MACD, BB, EMA values from all indicators | ~500B |
`quote_get` |
Get latest price, OHLC, volume | ~200B |
`data_get_ohlcv` |
Get price bars. Use for compact stats`summary: true` |
500B (summary) / 8KB (100 bars) |

Read `line.new()`

, `label.new()`

, `table.new()`

, `box.new()`

output from any visible Pine indicator.

| Tool | When to use | Output size |
|---|---|---|
`data_get_pine_lines` |
Read horizontal price levels (support/resistance, session levels) | ~1-3KB |
`data_get_pine_labels` |
Read text annotations + prices ("PDH 24550", "Bias Long") | ~2-5KB |
`data_get_pine_tables` |
Read data tables (session stats, analytics dashboards) | ~1-4KB |
`data_get_pine_boxes` |
Read price zones / ranges as {high, low} pairs | ~1-2KB |

**Always use study_filter** to target a specific indicator:

`study_filter: "Profiler"`

.| Tool | What it does |
|---|---|
`chart_set_symbol` |
Change ticker (BTCUSD, AAPL, ES1!, NYMEX:CL1!) |
`chart_set_timeframe` |
Change resolution (1, 5, 15, 60, D, W, M) |
`chart_set_type` |
Change style (Candles, HeikinAshi, Line, Area, Renko) |
`chart_manage_indicator` |
Add/remove indicators. Use full names: "Relative Strength Index" not "RSI" |
`chart_scroll_to_date` |
Jump to a date (ISO: "2025-01-15") |
`chart_set_visible_range` |
Zoom to exact range (unix timestamps) |
`symbol_info` / `symbol_search` |
Symbol metadata and search |
`indicator_set_inputs` / `indicator_toggle_visibility` |
Change indicator settings, show/hide |

| Tool | What it does |
|---|---|
`pane_list` |
List all panes with symbols and active state |
`pane_set_layout` |
Change grid: `s` , `2h` , `2v` , `2x2` , `4` , `6` , `8` |
`pane_focus` |
Focus a specific pane by index |
`pane_set_symbol` |
Set symbol on any pane |

| Tool | What it does |
|---|---|
`tab_list` |
List open chart tabs |
`tab_new` / `tab_close` |
Open/close tabs |
`tab_switch` |
Switch to a tab by index |

| Tool | Step |
|---|---|
`pine_set_source` |
1. Inject code into editor |
`pine_smart_compile` |
2. Compile with auto-detection + error check |
`pine_get_errors` |
3. Read compilation errors if any |
`pine_get_console` |
4. Read log.info() output |
`pine_save` |
5. Save to TradingView cloud |
`pine_get_source` |
Read current script (warning: can be 200KB+ for complex scripts) |
`pine_new` |
Create blank indicator/strategy/library |
`pine_open` / `pine_list_scripts` |
Open or list saved scripts |
`pine_analyze` |
Offline static analysis (no chart needed) |
`pine_check` |
Server-side compile check (no chart needed) |

| Tool | Step |
|---|---|
`replay_start` |
Enter replay at a date |
`replay_step` |
Advance one bar |
`replay_autoplay` |
Auto-advance (set speed in ms) |
`replay_trade` |
Buy/sell/close positions |
`replay_status` |
Check position, P&L, date |
`replay_stop` |
Return to realtime |

| Tool | What it does |
|---|---|
`draw_shape` |
Draw horizontal_line, trend_line, rectangle, text |
`draw_list` / `draw_remove_one` / `draw_clear` |
Manage drawings |
`alert_create` / `alert_list` / `alert_delete` |
Manage price alerts |
`capture_screenshot` |
Screenshot (regions: full, chart, strategy_tester) |
`batch_run` |
Run action across multiple symbols/timeframes |
`watchlist_get` / `watchlist_add` |
Read/modify watchlist |
`layout_list` / `layout_switch` |
Manage saved layouts |
`ui_open_panel` / `ui_click` / `ui_evaluate` |
UI automation |
`tv_launch` / `tv_health_check` / `tv_discover` |
Connection management |

Tools return compact output by default to minimize context usage. For a typical "analyze my chart" workflow, total context is ~5-10KB instead of ~80KB.

| Feature | How it saves context |
|---|---|
| Pine lines | Returns deduplicated price levels only, not every line object |
| Pine labels | Capped at 50 per study, text+price only |
| Pine tables | Pre-formatted row strings, no cell metadata |
| Pine boxes | Deduplicated {high, low} zones only |
| OHLCV summary mode | Stats + last 5 bars instead of all bars |
| Indicator inputs | Encrypted/encoded blobs auto-filtered |
`verbose: true` |
Pass on any pine tool to get raw data with IDs/colors when needed |
`study_filter` |
Target one indicator instead of scanning all |

Launch scripts and `tv_launch`

auto-detect TradingView. If auto-detection fails:

| Platform | Common Locations |
|---|---|
Mac |
`/Applications/TradingView.app/Contents/MacOS/TradingView` |
Windows |
`%LOCALAPPDATA%\TradingView\TradingView.exe` , `%PROGRAMFILES%\WindowsApps\TradingView*\TradingView.exe` |
Linux |
`/opt/TradingView/tradingview` , `~/.local/share/TradingView/TradingView` , `/snap/tradingview/current/tradingview` |

The key flag: `--remote-debugging-port=9222`


```
# Requires TradingView running with --remote-debugging-port=9222
npm test
```

29 tests covering: Pine Script static analysis, server-side compilation, and CLI routing.

```
Claude Code ←→ MCP Server (stdio) ←→ CDP (port 9222) ←→ TradingView Desktop (Electron)
```


**Transport**: MCP over stdio (84 tools) + CLI (`tv`

command, 30 commands with 66 subcommands)**Connection**: Chrome DevTools Protocol on localhost:9222**Streaming**: Poll-and-diff loop with deduplication, JSONL output to stdout**No dependencies**beyond`@modelcontextprotocol/sdk`

and`chrome-remote-interface`


This project is not affiliated with, endorsed by, or associated with:

**TradingView Inc.**— TradingView is a trademark of TradingView Inc.**Anthropic**— Claude and Claude Code are trademarks of Anthropic, PBC.

This tool is an independent MCP server that connects to Claude Code via the standard MCP protocol. It does not contain or modify any Anthropic software.

This project is provided **for personal, educational, and research purposes only**.

**How this tool works:** This tool uses Chrome DevTools Protocol (CDP), the standard debugging interface built into Chromium-based applications. It does not reverse engineer any proprietary TradingView protocol, connect to TradingView's servers, or bypass any access controls. The debug port must be explicitly enabled by the user via a standard Chromium command-line flag (`--remote-debugging-port=9222`

).

By using this software, you acknowledge and agree that:

**You are solely responsible**for ensuring your use of this tool complies with TradingView's Terms of Use and all applicable laws.- TradingView's Terms of Use
**restrict automated data collection, scraping, and non-display usage**of their platform and data. This tool uses Chrome DevTools Protocol to programmatically interact with the TradingView Desktop app, which may conflict with those terms. **You assume all risk**associated with using this tool. The authors are not responsible for any account bans, suspensions, legal actions, or other consequences resulting from its use.- This tool
**must not be used**for, including but not limited to:- Redistributing, reselling, or commercially exploiting TradingView's market data
- Circumventing TradingView's access controls or subscription restrictions
- Performing automated trading or algorithmic decision-making using extracted data
- Violating the intellectual property rights of Pine Script indicator authors
- Connecting to TradingView's servers or infrastructure (all access is via the locally running Desktop app)

- The streaming functionality monitors your locally running TradingView Desktop instance only. It does not connect to TradingView's servers or extract data from TradingView's infrastructure.
- Market data accessed through this tool remains subject to exchange and data provider licensing terms.
**Do not redistribute, store, or commercially exploit any data obtained through this tool.** - This tool accesses internal, undocumented TradingView application interfaces that may change or break at any time without notice.

**Use at your own risk.** If you are unsure whether your intended use complies with TradingView's terms, do not use this tool.

MIT — see LICENSE for details.

The MIT license applies to the source code of this project only. It does not grant any rights to TradingView's software, data, trademarks, or intellectual property.