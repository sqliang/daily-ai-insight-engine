---
title: agegr/pi-web
source: https://github.com/agegr/pi-web
author: []
published: ''
created: '2026-07-22'
manifest_dates:
- '2026-07-22'
- '2026-07-23'
- '2026-07-24'
description: 'Web UI for the pi coding agentPi Web 中文文档 Local web UI for the pi coding
  agent. Pi Web reads your local pi session files and gives you a browser workspace
  for session browsing, real-time chat, model configuration, skill management, and
  project file preview. The same pi session in CLI and Pi Web: structured tool calls,
  readable Markdown, session browsing, and cleaner results. Quick Start Run without
  installing: npx @agegr/pi-web@latest Or install globally: npm install -g @agegr/pi-web
  pi-web Then open http://localhost:30141. The CLI will try to open the browser automatically
  after the server is ready. Options: pi-web --port 8080 # custom port pi-web --hostname
  127.0.0.1 # local access only pi-web -p 8080 -H 127.0.0.1 # combine options pi-web
  --no-open # do not open the browser automatically PORT=8080 pi-web # environment
  variable is also supported PI_WEB_NO_OPEN=1 pi-web # useful when running as a background
  service Features Pick work back up: browse previous pi conversations by project
  without digging through terminal history or session paths. Try different directions
  safely: continue from an earlier message or fork a session into a separate route.
  Work across branches: switch Git worktrees from the sidebar so new sessions and
  the Explorer follow the checkout you choose. Chat beside the project: browse files
  on the left and preview source, docs, images, audio, and PDFs on the right while
  the agent works. See session state clearly: context usage, cost, compaction state,
  and system prompt details are visible from the top bar. Configure less from the
  terminal: manage models, login/API keys, model tests, and skill switches from the
  web UI. Notes Data directory: Pi Web reads ~/.pi/agent/sessions by default. Set
  PI_CODING_AGENT_DIR to point at another pi agent directory. Session files: files
  are stored as ~/.pi/agent/sessions/<encoded-cwd>/<timestamp>_<uuid>.jsonl. Model
  config: the Models panel reads and writes models.json in the pi agent directory.
  Model lists and defaults come from pi''s config. File access: file browsing and
  preview are scoped to the selected project directory and working directories that
  appear in sessions. Git worktrees: see Worktrees in Pi Web for when the switcher
  appears, how new worktrees are created, and what removal does. Forks vs in-session
  branches: Fork creates a new .jsonl file. "Edit from here" creates another branch
  inside the same session file. Development npm install npm run dev The local dev
  server runs at http://localhost:30141. Common checks: node_modules/.bin/tsc --noEmit
  npm run lint Avoid running next build / npm run build during local development.
  It writes to .next/ and can interfere with the dev server; leave builds for release
  work. Project Structure app/ api/ agent/ # creates/drives AgentSession and exposes
  SSE events auth/ # OAuth and API key management cwd/validate/ # custom working directory
  validation default-cwd/ # pi default working directory lookup files/ # file listing,
  reading, preview, and watching home/ # current user home directory models/ # available
  models, default model, thinking levels models-config/ # read/write models.json and
  test models sessions/ # session reads, rename, delete, context, HTML export skills/
  # skill listing, search, install, enable/disable components/ AppShell.tsx # main
  layout, URL state, top panels, file tabs SessionSidebar.tsx # project selector,
  session tree, Explorer ChatWindow.tsx # messages, SSE, image drag/drop, minimap
  ChatInput.tsx # input bar, model/tools/thinking/compact/slash controls MessageView.tsx
  # message, thinking, tool call/result rendering ModelsConfig.tsx # model and auth
  configuration panel SkillsConfig.tsx # skill management panel FileExplorer.tsx #
  file tree FileViewer.tsx # source, diff, image, audio, PDF, DOCX preview lib/ rpc-manager.ts
  # AgentSessionWrapper lifecycle and global registry session-reader.ts # parses .jsonl
  session files and branch contexts normalize.ts # normalizes toolCall field names
  file-access.ts # file read safety boundary file-paths.ts # path encoding and relative
  path helpers markdown.ts # Markdown/Mermaid/KaTeX plugin configuration pi-types.ts
  # pi-related types hooks/ useAgentSession.ts # session loading, command sending,
  SSE state machine useAudio.ts # completion sound useDragDrop.ts # image drag/drop
  useTheme.ts # theme switching bin/ pi-web.js # npm CLI entrypoint'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 2d5fceaeaafe1429
source_type: community_discussion
tldr: agegr/pi-web 是为 pi 编程智能体提供本地 Web 界面的开源工具，支持会话浏览、实时聊天、模型配置和项目管理，可通过 npx 直接运行无需安装。
objective_summary: agegr 发布了 pi-web，一个为 pi 编程智能体设计的本地 Web UI 开源项目。该工具通过读取本地 pi 会话文件，在浏览器中提供会话浏览与分叉、实时聊天、模型配置管理、技能管理以及项目文件预览等功能。用户可通过
  npx @agegr/pi-web@latest 直接运行，或通过 npm 全局安装后使用 pi-web 命令启动，默认访问 http://localhost:30141。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - agegr
  technologies:
  - pi
  - pi-web
  key_people: []
key_logic_flow:
- pi-web 是专为 pi 编程智能体设计的本地 Web 用户界面，通过读取本地会话文件提供浏览器工作区。
- 用户可通过 npx @agegr/pi-web@latest 直接运行 pi-web，无需安装即可使用全部功能。
- pi-web 支持会话浏览与分叉、实时聊天、模型配置管理、技能管理以及项目文件预览等核心功能。
- 工具支持 Git 工作区切换，可从侧边栏切换分支并使新会话和文件浏览器跟随所选工作区。
- 会话状态可视化包括上下文用量、成本、压缩状态和系统提示详情，在顶部栏中实时显示。
- 数据目录默认为 ~/.pi/agent/sessions，可通过 PI_CODING_AGENT_DIR 环境变量自定义指向其他目录。
object_mentions:
- object_type: project
  name: agegr/pi-web
  canonical_name: agegr/pi-web
  url: https://github.com/agegr/pi-web
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - agegr/pi-web 是为 pi 编程智能体提供本地 Web 用户界面的开源项目，可读取本地 pi 会话文件并提供完整的浏览器工作区。
  - 用户可通过 npx @agegr/pi-web@latest 命令直接运行 pi-web，无需任何安装步骤即可在浏览器中使用全部功能。
  - pi-web 支持会话浏览与分叉、实时聊天交互、模型配置管理、技能启用与禁用以及项目文件预览等核心功能。
  article_id: 2d5fceaeaafe1429
- object_type: project
  name: pi
  canonical_name: pi
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - pi-web 是专为 pi 编程智能体设计的本地 Web 用户界面，pi 的会话文件以 JSONL 格式存储在 ~/.pi/agent/sessions 目录下。
  - pi-web 的 Models 面板会读取和写入 pi 智能体目录中的 models.json 文件，模型列表和默认值来自 pi 的配置。
  article_id: 2d5fceaeaafe1429
extract_result: success
impact_score:
  score: 4.8
  reason: pi-web 是为 pi 编程智能体提供本地 Web 界面的工具，本质上是 CLI 已有能力的图形化封装，并未引入新的 AI 能力或训练范式突破。它对
    pi 生态内的用户体验有明显提升（会话浏览、分叉、工作区切换等），但 pi 本身属于新兴但非主流的编程智能体，用户基数有限，短期内难以撼动 Cursor、Claude
    Code、GitHub Copilot 等已建立稳固地位的竞品格局。评分 4.8 分：这是一个值得关注的开发者工具补充，属于局部体验优化，不具备行业范式转移潜力。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 通过本地 Web UI 实现 pi 会话可视化管理与交互，无需记忆命令行路径即可浏览/分叉会话
hype_assessment:
  level: low
  reason: 文章为 GitHub README 式技术文档，语言客观、功能描述准确，没有使用 '颠覆'、'革命性' 等 PR 夸大词汇。核心价值主张清晰（为
    pi agent 提供本地 Web UI），且附带完整安装命令、架构说明和开发指南，属于实打实的技术发布。
information_entropy: high
domain_disruption:
  technical_innovation: 无底层模型或算法突破。技术亮点在于围绕 pi 的 JSONL 会话文件格式做了完整的 Web 封装：基于文件系统的会话读取/分叉/分支管理、SSE
    实时通信、Git worktree 集成、文件预览沙箱等，工程实现扎实但属于成熟的 Web UI 套壳模式。
  business_model: 开源 MIT 风格项目，通过 npm 分发，无商业化迹象。对 agegr 而言，pi-web 降低了 pi 智能体的使用门槛，有助于扩大用户基础，间接推动
    pi 生态的采用。商业模式影响有限。
engineering_complexity: production_ready
compound_value:
  score: 5.5
  reason: pi-web 的价值完全依附于 pi 编程智能体的生态采用曲线，本身不具备独立的复利效应。它为 CLI 原生的 pi 提供了一个本地 Web GUI，显著降低了使用门槛（npx
    一键启动，无需安装），并通过会话管理、模型配置、技能管理等功能提升了用户体验的完整度。从 VC 视角看，这是一个 '生态增强型' 产品而非独立平台：其长期价值取决于
    pi 能否成为编程智能体的主流选择。如果 pi 生态持续增长，pi-web 会沉淀为事实上的标准 UI，具备一定的用户粘性和社区贡献积累效应；但若 pi 被其他方案取代，pi-web
    的价值将随之下沉。当前阶段属于 '赌生态配套' 的逻辑，值得跟踪但不宜赋予过高独立估值。
value_capture_layer: agent_middleware
moat_impact: democratizes_access
key_beneficiaries:
- agegr
- pi 开源生态
competitive_casualty:
- CLI-only 编程智能体
- 缺少 Web UI 的开源 Agent 框架
market_opportunities:
- 基于 pi-web 的模式，开发者可构建通用化的 AI 编程智能体本地管理界面，将会话管理、模型配置和项目文件预览整合为一站式工作台
- 企业团队可将此类工具内部化，构建自主可控的 AI 编程助手管理平台，实现会话审计、成本追踪、技能管理与企业级安全管控
- pi-web 的会话分叉与 Git 工作区切换能力启发了 AI Agent 协作场景的产品思路——分支实验和多方案并行对比可作为差异化功能集成到现有开发工具中
risk_matrix:
  regulatory: 无
  technological: pi-web 与 pi 编程智能体的会话格式和配置文件深度绑定，若 pi 更新内部数据格式或停止维护，该工具的兼容性和可用性将面临断裂风险
  competitive: 面临 Cursor、VS Code AI 插件、GitHub Copilot Chat、Windsurf 等成熟产品的竞争，这些工具已内建聊天界面和项目管理功能，pi
    生态目前仍属小众，市场挤压风险显著
  ethical: 无
  additional:
  - pi 智能体本身在编程 Agent 市场中的采用率存在不确定性——若社区活跃度下降或竞品大幅领先，pi-web 的生态价值将随之衰减
confidence:
  impact: medium
  compound: low
  hype: low
actionable_insight: monitor
object_insights:
- object_type: project
  name: agegr/pi-web
  canonical_name: agegr/pi-web
  url: https://github.com/agegr/pi-web
  positioning: 为 pi 编程智能体打造的本地 Web 用户界面，通过读取本地会话文件提供会话浏览、实时聊天和项目管理等浏览器工作区功能。
  technical_signal: 基于 Next.js 架构，通过解析 JSONL 会话文件实现会话浏览与分叉，并支持 SSE 实时流式聊天、模型配置读写和
    Git 工作区切换。
  adoption_signal: 支持 npx 零安装运行和 npm 全局安装两种方式，默认端口 30141 开箱即用，降低了 pi 用户从 CLI 切换到 Web
    界面的门槛。
  ecosystem_relevance: 直接复用 pi 的会话文件格式与模型配置体系，是 pi 编程智能体生态中面向 Web 交互体验的关键配套组件。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: pi-web 为 pi 编程智能体提供了从纯 CLI 到完整浏览器工作区的体验升级，覆盖会话管理、模型配置和文件预览等高频场景，是评估
    pi 生态向开发者工具平台演进的重要观察对象。
  risk_notes:
  - 项目处于早期阶段，功能完整性和生产环境稳定性尚需更多实际使用验证。
  - pi-web 的用户规模受限于 pi 编程智能体自身的社区采用率和用户基础。
  score: 6.0
  article_ids:
  - 2d5fceaeaafe1429
  evidence_snippets:
  - agegr/pi-web 是为 pi 编程智能体提供本地 Web 用户界面的开源项目，可读取本地 pi 会话文件并提供完整的浏览器工作区。
  - 用户可通过 npx @agegr/pi-web@latest 命令直接运行 pi-web，无需任何安装步骤即可在浏览器中使用全部功能。
  - pi-web 支持会话浏览与分叉、实时聊天交互、模型配置管理、技能启用与禁用以及项目文件预览等核心功能。
- object_type: project
  name: pi
  canonical_name: pi
  url: null
  positioning: pi 是一个面向代码开发的编程智能体，以 CLI 为主要交互方式，其会话文件格式和模型配置体系支持第三方工具集成与扩展。
  technical_signal: pi 使用 JSONL 格式存储会话文件并通过 models.json 管理模型配置，数据目录结构开放可供第三方工具读取和写入。
  adoption_signal: null
  ecosystem_relevance: pi 的开放会话格式和配置体系构成 pi-web 等生态工具的集成基础，体现了构建可扩展生态的技术策略。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: pi 作为编程智能体，其开放的会话文件格式和配置机制为生态工具提供了集成接口，是观察 AI 编程工具从单体工具向开放平台演进的重要参考案例。
  risk_notes:
  - 本文主要聚焦 pi-web，对 pi 智能体自身功能、性能和用户规模的描述有限，难以进行全面评估。
  - 在 Cursor、Copilot 等成熟编程智能体主导的市场中，pi 的差异化优势和竞争定位尚需更多信息披露。
  score: 4.0
  article_ids:
  - 2d5fceaeaafe1429
  evidence_snippets:
  - pi-web 是专为 pi 编程智能体设计的本地 Web 用户界面，pi 的会话文件以 JSONL 格式存储在 ~/.pi/agent/sessions 目录下。
  - pi-web 的 Models 面板会读取和写入 pi 智能体目录中的 models.json 文件，模型列表和默认值来自 pi 的配置。
---

Local web UI for the pi coding agent. Pi Web reads your local pi session files and gives you a browser workspace for session browsing, real-time chat, model configuration, skill management, and project file preview.

The same pi session in CLI and Pi Web: structured tool calls, readable Markdown, session browsing, and cleaner results.

**Run without installing:**

`npx @agegr/pi-web@latest`

**Or install globally:**

```
npm install -g @agegr/pi-web
pi-web
```

Then open http://localhost:30141. The CLI will try to open the browser automatically after the server is ready.

**Options:**

```
pi-web --port 8080 # custom port
pi-web --hostname 127.0.0.1 # local access only
pi-web -p 8080 -H 127.0.0.1 # combine options
pi-web --no-open # do not open the browser automatically
PORT=8080 pi-web # environment variable is also supported
PI_WEB_NO_OPEN=1 pi-web # useful when running as a background service
```

**Pick work back up**: browse previous pi conversations by project without digging through terminal history or session paths.**Try different directions safely**: continue from an earlier message or fork a session into a separate route.**Work across branches**: switch Git worktrees from the sidebar so new sessions and the Explorer follow the checkout you choose.**Chat beside the project**: browse files on the left and preview source, docs, images, audio, and PDFs on the right while the agent works.**See session state clearly**: context usage, cost, compaction state, and system prompt details are visible from the top bar.**Configure less from the terminal**: manage models, login/API keys, model tests, and skill switches from the web UI.

**Data directory**: Pi Web reads`~/.pi/agent/sessions`

by default. Set`PI_CODING_AGENT_DIR`

to point at another pi agent directory.**Session files**: files are stored as`~/.pi/agent/sessions/<encoded-cwd>/<timestamp>_<uuid>.jsonl`

.**Model config**: the Models panel reads and writes`models.json`

in the pi agent directory. Model lists and defaults come from pi's config.**File access**: file browsing and preview are scoped to the selected project directory and working directories that appear in sessions.**Git worktrees**: see Worktrees in Pi Web for when the switcher appears, how new worktrees are created, and what removal does.**Forks vs in-session branches**: Fork creates a new`.jsonl`

file. "Edit from here" creates another branch inside the same session file.

```
npm install
npm run dev
```

The local dev server runs at http://localhost:30141.

Common checks:

```
node_modules/.bin/tsc --noEmit
npm run lint
```

Avoid running `next build`

/ `npm run build`

during local development. It writes to `.next/`

and can interfere with the dev server; leave builds for release work.

```
app/
api/
agent/ # creates/drives AgentSession and exposes SSE events
auth/ # OAuth and API key management
cwd/validate/ # custom working directory validation
default-cwd/ # pi default working directory lookup
files/ # file listing, reading, preview, and watching
home/ # current user home directory
models/ # available models, default model, thinking levels
models-config/ # read/write models.json and test models
sessions/ # session reads, rename, delete, context, HTML export
skills/ # skill listing, search, install, enable/disable
components/
AppShell.tsx # main layout, URL state, top panels, file tabs
SessionSidebar.tsx # project selector, session tree, Explorer
ChatWindow.tsx # messages, SSE, image drag/drop, minimap
ChatInput.tsx # input bar, model/tools/thinking/compact/slash controls
MessageView.tsx # message, thinking, tool call/result rendering
ModelsConfig.tsx # model and auth configuration panel
SkillsConfig.tsx # skill management panel
FileExplorer.tsx # file tree
FileViewer.tsx # source, diff, image, audio, PDF, DOCX preview
lib/
rpc-manager.ts # AgentSessionWrapper lifecycle and global registry
session-reader.ts # parses .jsonl session files and branch contexts
normalize.ts # normalizes toolCall field names
file-access.ts # file read safety boundary
file-paths.ts # path encoding and relative path helpers
markdown.ts # Markdown/Mermaid/KaTeX plugin configuration
pi-types.ts # pi-related types
hooks/
useAgentSession.ts # session loading, command sending, SSE state machine
useAudio.ts # completion sound
useDragDrop.ts # image drag/drop
useTheme.ts # theme switching
bin/
pi-web.js # npm CLI entrypoint
```