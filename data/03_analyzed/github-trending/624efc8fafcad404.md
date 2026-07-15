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
tldr: JCodesMore 发布 AI 网站克隆模板，可用 AI 编码代理将任意网站逆向工程为 Next.js 代码库
objective_summary: JCodesMore 在 GitHub 发布 ai-website-cloner-template 开源模板，使用 Claude
  Code 等 AI 编码代理对任意网站进行逆向工程，经过侦察、设计提取、组件规格编写、并行构建和组装质检五个阶段，生成基于 Next.
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - JCodesMore
  technologies:
  - Next.js
  - shadcn/ui
  - Tailwind CSS
  - Lucide React
  - React
  - TypeScript
  key_people: []
key_logic_flow:
- JCodesMore 发布 ai-website-cloner-template 模板，用于将任意网站逆向工程转换为 Next.js 代码库
- 该模板使用 AI 编码代理（推荐 Claude Code + Opus 4.8）执行五阶段流水线：侦察（截图、设计令牌提取、交互扫描）、基础设置（字体/颜色/全局样式/资源下载）、组件规格编写（精确
  CSS 计算值说明）、并行构建（使用 git worktree 分派多个构建代理）、组装与质量检测（合并 worktree 并运行视觉差异对比）
- 项目支持多种 AI 编码代理，包括 Claude Code、Codex CLI、Cursor、Windsurf、GitHub Copilot、Cline 等 13
  种平台
- 使用方式为点击 GitHub 'Use this template' 创建独立仓库，安装依赖后运行 /clone-website <target-url> 命令
- 项目明确禁止用于钓鱼、仿冒、盗用他人设计或违反服务条款等恶意用途
- 采用 MIT 开源协议，包含自动同步脚本（sync-agent-rules.sh 和 sync-skills.mjs）以维护跨平台代理指令文件
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
impact_score:
  score: 5.0
  reason: 这是一个实用但非突破性的开发者工具。其核心价值在于将AI编码代理应用到网站逆向工程这一具体场景，并通过五阶段流水线（侦察→基础设置→组件规格→并行构建→质检）和git
    worktree并行构建模式，展现了较好的工程组织能力。但本质上，AI克隆网站的概念已有大量实践（如v0、Bolt.new等），该模板更多是工作流模式的最佳实践总结，而非技术范式突破。影响范围局限在开发者工具生态圈，对AI行业整体格局影响有限，因此评分5.0。
sentiment: mixed
developer_sentiment:
  tone: excited
  primary_focus: 多AI代理并行构建网站逆向工程的流水线模式是否真的可靠且可用
hype_assessment:
  level: medium
  reason: 项目本身的技术文档和架构描述较为务实，给出了具体的技术栈（Next.js 16、shadcn/ui、Tailwind CSS v4）和五阶段流水线细节，并非空泛的概念炒作。但'将任意网站逆向工程为干净的现代Next.js代码库'这一表述存在一定包装成分——实际克隆质量高度依赖底层AI代理（推荐Opus
    4.8），且对复杂交互网站的效果未经充分验证。'任意网站'和'clean, modern'属于软性承诺，存在水分。
information_entropy: high
domain_disruption:
  technical_innovation: 并非底层AI技术突破，而是工程模式创新：1) 多代理并行构建架构——利用git worktree隔离多个构建代理，实现组件级并发重建，最后合并质检，这是比串行调用AI更高效的协作模式；2)
    精确CSS计算值提取流水线——通过getComputedStyle()获取像素级精确值写入规格文档，减少AI'猜测'带来的还原偏差；3) 跨13种AI代理平台的一次编写/多平台同步机制，通过AGENTS.md单源真值自动生成各平台指令文件。
  business_model: 模板本身采用MIT开源协议，无直接商业模式。但其潜在影响在于：降低了网站迁移（WordPress/Webflow/Squarespace
    → Next.js）的技术门槛，可能催生出'AI驱动的网站迁移即服务'微服务生态。对于数字代理商和自由开发者，可作为高杠杆效率工具使用。同时也引发关于设计知识产权和爬取合规性的商业法律灰色地带讨论。
engineering_complexity: production_ready
compound_value:
  score: 4.0
  reason: 该模板本身是 MIT 开源项目，无直接商业模式、网络效应或数据护城河，长期复利能力有限。但其核心价值在于演示了一种可复用的 AI 代理编排流水线（侦察→设计提取→组件规格→并行构建→质检），这一模式随
    AI 编码代理能力提升而持续增值。不过由于模板可被轻易复刻、无锁定效应，且价值主要外溢到 AI 代理平台方，独立复利能力仅处于中等偏下水平。
value_capture_layer: agent_middleware
moat_impact: democratizes_access
key_beneficiaries:
- Anthropic
- OpenAI
- Vercel
- Codex CLI
- Cursor
competitive_casualty:
- 传统网站重建/迁移服务商
- Webflow
- Wix
- Squarespace
- 低端网页开发外包团队
market_opportunities:
- 提供企业级 Legacy 网站现代化迁移服务：利用该模板将 WordPress/Wix/Webflow/Squarespace 等旧平台网站自动迁移至 Next.js
  技术栈，可大幅降低人工迁移成本并缩短交付周期
- 数字资产恢复与代码审计服务：为企业找回丢失的源代码或重建已离职开发者遗留的项目资产，形成数字化应急恢复的垂直解决方案
- 前端设计教育与竞品技术拆解工具：系统化拆解生产级网站的布局实现、动画模式和响应式策略，用于前端团队的逆向学习与设计系统分析
risk_matrix:
  regulatory: 网站克隆涉及版权法侵权风险、DMCA 下架诉讼以及被克隆网站服务条款（ToS）违反问题；欧盟 AI Act 可能将此类网站逆向工程工具列为高风险应用；跨境法律适用性问题使合规成本显著增加
  technological: AI 生成的克隆代码可能存在质量不一致问题，包括组件状态处理不完整（加载/空/错误状态缺失）、计算样式与实际渲染偏差、复杂交互（拖拽/动画/WebSocket）无法精确还原，以及依赖注入后的兼容性风险
  competitive: 头部 AI 编码工具（Cursor、Copilot、Codex CLI、Windsurf）正将网站逆向工程能力直接内置到开发环境中，存在平台原生化挤压独立模板项目的风险
  ethical: 该工具可被滥用于钓鱼网站制作、品牌仿冒、设计盗窃和身份冒充欺诈；尽管项目已通过 README 声明禁止恶意用途，但缺乏技术层面的约束机制（无水印、无来源声明强制要求），使用者仅靠自觉遵守
  additional: []
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: strategic_invest
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