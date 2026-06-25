---
title: JCodesMore/ai-website-cloner-template
source: https://github.com/JCodesMore/ai-website-cloner-template
author: []
published: ''
created: '2026-06-24'
description: 'Clone any website with one command using AI coding agentsAI Website
  Cloner Template A reusable template for reverse-engineering any website into a clean,
  modern Next.js codebase using AI coding agents. Recommended: Claude Code with Opus
  4.7 for best results — but works with a variety of AI coding agents. Point it at
  a URL, run /clone-website, and your AI agent will inspect the site, extract design
  tokens and assets, write component specs, and dispatch parallel builders to reconstruct
  every section. Demo Click the image above to watch the full demo on YouTube. Quick
  Start Important: Start by making your own copy with GitHub''s Use this template
  button. Do not clone this template repository directly for your website project,
  and do not open pull requests here with your generated website. Create your own
  repository from this template On the GitHub page for this project, click Use this
  template, then click Create a new repository. Give your new repository a name, choose
  whether it should be public or private, then click Create repository. If GitHub
  shows an Include all branches option, you can leave it off. This gives you your
  own separate project to work in, so your website changes stay in your account instead
  of coming back to the main template. Open your new repository on your computer After
  GitHub creates your copy, open that new repository. Click Code and open or clone
  your new repository with your preferred coding tool. If you use the terminal, the
  command will look like this: git clone https://github.com/YOUR-USERNAME/YOUR-NEW-REPOSITORY.git
  cd YOUR-NEW-REPOSITORY Install dependencies npm install Start your AI agent — Claude
  Code recommended: claude --chrome Run the skill: /clone-website <target-url1> [<target-url2>
  ...] Customize (optional) — after the base clone is built, modify as needed Using
  a different agent? Open AGENTS.md for project instructions — most agents pick it
  up automatically. Supported Platforms Agent Status Claude Code Recommended — Opus
  4.7 Codex CLI Supported OpenCode Supported GitHub Copilot Supported Cursor Supported
  Windsurf Supported Gemini CLI Supported Cline Supported Roo Code Supported Continue
  Supported Amazon Q Supported Augment Code Supported Aider Supported Prerequisites
  Node.js 24+ An AI coding agent (see Supported Platforms) Tech Stack Next.js 16 —
  App Router, React 19, TypeScript strict shadcn/ui — Radix primitives + Tailwind
  CSS v4 Tailwind CSS v4 — oklch design tokens Lucide React — default icons (replaced
  by extracted SVGs during cloning) How It Works The /clone-website skill runs a multi-phase
  pipeline: Reconnaissance — screenshots, design token extraction, interaction sweep
  (scroll, click, hover, responsive) Foundation — updates fonts, colors, globals,
  downloads all assets Component Specs — writes detailed spec files (docs/research/components/)
  with exact computed CSS values, states, behaviors, and content Parallel Build —
  dispatches builder agents in git worktrees, one per section/component Assembly &
  QA — merges worktrees, wires up the page, runs visual diff against the original
  Each builder agent receives the full component specification inline — exact getComputedStyle()
  values, interaction models, multi-state content, responsive breakpoints, and asset
  paths. No guessing. Use Cases Platform migration — rebuild a site you own from WordPress/Webflow/Squarespace
  into a modern Next.js codebase Lost source code — your site is live but the repo
  is gone, the developer left, or the stack is legacy. Get the code back in a modern
  format Learning — deconstruct how production sites achieve specific layouts, animations,
  and responsive behavior by working with real code Not Intended For Phishing or impersonation
  — this project must not be used for deceptive purposes, impersonation, or any activity
  that breaks the law. Passing off someone''s design as your own — logos, brand assets,
  and original copy belong to their owners. Violating terms of service — some sites
  explicitly prohibit scraping or reproduction. Check first. Project Structure src/
  app/ # Next.js routes components/ # React components ui/ # shadcn/ui primitives
  icons.tsx # Extracted SVG icons lib/utils.ts # cn() utility types/ # TypeScript
  interfaces hooks/ # Custom React hooks public/ images/ # Downloaded images from
  target videos/ # Downloaded videos from target seo/ # Favicons, OG images docs/
  research/ # Extraction output & component specs design-references/ # Screenshots
  scripts/ sync-agent-rules.sh # Regenerate agent instruction files sync-skills.mjs
  # Regenerate /clone-website for all platforms AGENTS.md # Agent instructions (single
  source of truth) CLAUDE.md # Claude Code config (imports AGENTS.md) GEMINI.md #
  Gemini CLI config (imports AGENTS.md) Commands npm run dev # Start dev server npm
  run build # Production build npm run lint # ESLint check npm run typecheck # TypeScript
  check npm run check # Run lint + typecheck + build If using docker docker compose
  up app --build # build and run the app docker compose up dev --build # run the app
  in dev mode on port 3001 Updating for Other Platforms Two source-of-truth files
  power all platform support. Edit the source, then run the sync script: What Source
  of truth Sync command Project instructions AGENTS.md bash scripts/sync-agent-rules.sh
  /clone-website skill .claude/skills/clone-website/SKILL.md node scripts/sync-skills.mjs
  Each script regenerates the platform-specific copies automatically. Agents that
  read the source files natively need no regeneration. Star History License MIT'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 624efc8fafcad404
source_type: community_discussion
tldr: JCodesMore 发布 AI 网站克隆模板，用 AI 编码代理将任意网站逆向工程为 Next.js 代码库
objective_summary: JCodesMore 在 GitHub 发布 ai-website-cloner-template，一个基于 AI 编码代理的网页逆向工程模板。用户提供目标
  URL 后，AI 代理自动执行侦察、设计令牌提取、组件规格编写和并行构建，最终生成 Next.js 16 代码库。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - GitHub
  - Anthropic
  technologies:
  - Next.js 16
  - React 19
  - TypeScript
  - shadcn/ui
  - Tailwind CSS v4
  - Lucide React
  - Claude Code
  - AI coding agents
  key_people: []
key_logic_flow:
- JCodesMore 创建了一个 GitHub 模板仓库 ai-website-cloner-template，用于逆向工程任意网站并生成现代化 Next.js
  代码库。
- 用户使用 `Use this template` 按钮创建自己的仓库副本，安装依赖后运行 `/clone-website <目标URL>` 命令启动克隆流程。
- 克隆流程分为五个阶段：侦察（截图、设计令牌提取、交互扫描）、基础设置（字体、颜色、全局样式、资源下载）、组件规格编写、并行构建（使用 git worktree
  每个组件独立构建）、组装与质量检查（合并、页面拼接、视觉差异对比）。
- 模板技术栈为 Next.js 16 + shadcn/ui + Tailwind CSS v4 + Lucide React，推荐使用 Claude Code
  (Opus 4.7)，同时支持 Codex CLI、Cursor、Windsurf 等十余种 AI 编码代理。
- 项目声明伦理限制：禁止用于钓鱼/冒充、冒用他人设计、违反服务条款等行为。
- 项目通过 AGENTS.md 和 .claude/skills/clone-website/SKILL.md 两个源文件驱动所有平台支持，使用同步脚本自动生成各平台专属配置。
extract_result: success
---

A reusable template for reverse-engineering any website into a clean, modern Next.js codebase using AI coding agents.

**Recommended: Claude Code with Opus 4.7 for best results** — but works with a variety of AI coding agents.

Point it at a URL, run `/clone-website`

, and your AI agent will inspect the site, extract design tokens and assets, write component specs, and dispatch parallel builders to reconstruct every section.

Click the image above to watch the full demo on YouTube.



Important:Start by making your own copy with GitHub'sUse this templatebutton. Do not clone this template repository directly for your website project, and do not open pull requests here with your generated website.

-
**Create your own repository from this template**On the GitHub page for this project, click

**Use this template**, then click**Create a new repository**.Give your new repository a name, choose whether it should be public or private, then click

**Create repository**. If GitHub shows an**Include all branches**option, you can leave it off.This gives you your own separate project to work in, so your website changes stay in your account instead of coming back to the main template.

-
**Open your new repository on your computer**After GitHub creates your copy, open that new repository. Click

**Code**and open or clone your new repository with your preferred coding tool.If you use the terminal, the command will look like this:

`git clone https://github.com/YOUR-USERNAME/YOUR-NEW-REPOSITORY.git cd YOUR-NEW-REPOSITORY`

-
**Install dependencies**npm install

-
**Start your AI agent**— Claude Code recommended:claude --chrome

-
**Run the skill**:`/clone-website <target-url1> [<target-url2> ...]`

-
**Customize**(optional) — after the base clone is built, modify as needed

Using a different agent? Open

`AGENTS.md`

for project instructions — most agents pick it up automatically.

| Agent | Status |
|---|---|
| Claude Code | Recommended — Opus 4.7 |
| Codex CLI | Supported |
| OpenCode | Supported |
| GitHub Copilot | Supported |
| Cursor | Supported |
| Windsurf | Supported |
| Gemini CLI | Supported |
| Cline | Supported |
| Roo Code | Supported |
| Continue | Supported |
| Amazon Q | Supported |
| Augment Code | Supported |
| Aider | Supported |

- Node.js 24+
- An AI coding agent (see Supported Platforms)

**Next.js 16**— App Router, React 19, TypeScript strict**shadcn/ui**— Radix primitives + Tailwind CSS v4**Tailwind CSS v4**— oklch design tokens**Lucide React**— default icons (replaced by extracted SVGs during cloning)

The `/clone-website`

skill runs a multi-phase pipeline:

**Reconnaissance**— screenshots, design token extraction, interaction sweep (scroll, click, hover, responsive)**Foundation**— updates fonts, colors, globals, downloads all assets**Component Specs**— writes detailed spec files (`docs/research/components/`

) with exact computed CSS values, states, behaviors, and content**Parallel Build**— dispatches builder agents in git worktrees, one per section/component**Assembly & QA**— merges worktrees, wires up the page, runs visual diff against the original

Each builder agent receives the full component specification inline — exact `getComputedStyle()`

values, interaction models, multi-state content, responsive breakpoints, and asset paths. No guessing.

**Platform migration**— rebuild a site you own from WordPress/Webflow/Squarespace into a modern Next.js codebase**Lost source code**— your site is live but the repo is gone, the developer left, or the stack is legacy. Get the code back in a modern format**Learning**— deconstruct how production sites achieve specific layouts, animations, and responsive behavior by working with real code

**Phishing or impersonation**— this project must not be used for deceptive purposes, impersonation, or any activity that breaks the law.**Passing off someone's design as your own**— logos, brand assets, and original copy belong to their owners.**Violating terms of service**— some sites explicitly prohibit scraping or reproduction. Check first.

```
src/
app/ # Next.js routes
components/ # React components
ui/ # shadcn/ui primitives
icons.tsx # Extracted SVG icons
lib/utils.ts # cn() utility
types/ # TypeScript interfaces
hooks/ # Custom React hooks
public/
images/ # Downloaded images from target
videos/ # Downloaded videos from target
seo/ # Favicons, OG images
docs/
research/ # Extraction output & component specs
design-references/ # Screenshots
scripts/
sync-agent-rules.sh # Regenerate agent instruction files
sync-skills.mjs # Regenerate /clone-website for all platforms
AGENTS.md # Agent instructions (single source of truth)
CLAUDE.md # Claude Code config (imports AGENTS.md)
GEMINI.md # Gemini CLI config (imports AGENTS.md)
```


```
npm run dev # Start dev server
npm run build # Production build
npm run lint # ESLint check
npm run typecheck # TypeScript check
npm run check # Run lint + typecheck + build
```

```
docker compose up app --build # build and run the app
docker compose up dev --build # run the app in dev mode on port 3001
```

Two source-of-truth files power all platform support. Edit the source, then run the sync script:

| What | Source of truth | Sync command |
|---|---|---|
| Project instructions | `AGENTS.md` |
`bash scripts/sync-agent-rules.sh` |
`/clone-website` skill |
`.claude/skills/clone-website/SKILL.md` |
`node scripts/sync-skills.mjs` |

Each script regenerates the platform-specific copies automatically. Agents that read the source files natively need no regeneration.

MIT