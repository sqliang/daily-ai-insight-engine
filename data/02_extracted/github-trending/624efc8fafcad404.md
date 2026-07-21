---
title: JCodesMore/ai-website-cloner-template
source: https://github.com/JCodesMore/ai-website-cloner-template
author: []
published: ''
created: '2026-06-26'
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
tldr: JCodesMore 在 GitHub 上发布了一个 AI 网站克隆模板项目，可通过 AI 编码代理将任意网站逆向工程为 Next.js 16 现代化代码库。推荐使用
  Claude Code 与 Opus 4.8，用户只需执行 /clone-website 命令即可触发多阶段自动化流水线。
objective_summary: JCodesMore 在 GitHub 上发布了 ai-website-cloner-template 模板仓库，用于通过 AI
  编码代理将任意网站逆向工程为基于 Next.js 16 的代码库。该项目推荐使用 Claude Code 搭配 Opus 4.8 模型，用户需先通过 GitHub
  的 Use this template 按钮创建自己的仓库，安装依赖后启动 AI 代理并执行 /clone-website 命令。代理自动执行侦察、组件规范编写、并行构建和组装
  QA 五个阶段，最终输出包含完整组件、图标、图片和设计令牌的 Next.js 项目。项目采用 MIT 许可证，并明确禁止用于钓鱼、冒充或违反服务条款等用途。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - GitHub
  technologies:
  - Next.js 16
  - shadcn/ui
  - Tailwind CSS v4
  - Lucide React
  - React 19
  key_people: []
key_logic_flow:
- JCodesMore 在 GitHub 上发布了 ai-website-cloner-template 模板项目，用于通过 AI 编码代理将任意网站逆向工程为基于
  Next.js 16 的现代化代码库。
- 项目推荐使用 Claude Code 搭配 Opus 4.8 模型以获得最佳效果，同时也兼容 Codex CLI、Cursor、Windsurf 等十余种主流
  AI 编码代理工具。
- 用户需先通过 GitHub 的 Use this template 按钮创建自己的仓库副本，然后执行 npm install 安装依赖并启动 AI 代理。
- /clone-website 命令包含侦察、基础构建、组件规范编写、并行构建和组装 QA 五个阶段的完整流水线，每个构建代理接收完整的组件规格说明。
- 项目技术栈基于 Next.js 16 App Router、shadcn/ui、Tailwind CSS v4 和 Lucide React，输出目录包含 app
  路由、组件、图标、图片和设计参考文档。
- 项目明确声明禁止用于钓鱼、冒充他人身份或违反目标网站服务条款等用途，原始设计和品牌资产归其所有者所有。
specialized_tags:
  github:
    projectName: JCodesMore/ai-website-cloner-template
    projectUrl: https://github.com/JCodesMore/ai-website-cloner-template
    primaryLanguage: TypeScript
    licenseType: MIT
    domain: ai_ml
    crossTags:
    - reverse-engineering
    - website-cloning
    - template
    aiDetail:
      primaryCategories:
      - code_gen
      agentSubcategory:
      - orchestration
      - tool_use
      - coding_agent
      techTags:
      - Next.js
      - TypeScript
      - Tailwind-CSS
      - shadcn-ui
      - React
extract_result: success
object_mentions:
- object_type: project
  name: JCodesMore/ai-website-cloner-template
  canonical_name: JCodesMore/ai-website-cloner-template
  url: https://github.com/JCodesMore/ai-website-cloner-template
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 该模板项目支持通过 AI 编码代理将任意网站逆向工程为基于 Next.js 16 的现代化代码库，用户只需指定目标 URL 即可自动完成重构。
  - 推荐使用 Claude Code 搭配 Opus 4.8 模型，同时也兼容 Codex CLI、Cursor、Windsurf 等十余种主流 AI 编码代理工具。
  - /clone-website 命令包含侦察、基础构建、组件规范编写、并行构建和组装 QA 五个阶段的多阶段流水线。
  article_id: 624efc8fafcad404
---

A reusable template for reverse-engineering any website into a clean, modern Next.js codebase using AI coding agents.

**Recommended: Claude Code with Opus 4.8 for best results** — but works with a variety of AI coding agents.

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
| Claude Code | Recommended — Opus 4.8 |
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