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