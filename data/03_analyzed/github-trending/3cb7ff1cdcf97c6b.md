---
title: alirezarezvani/claude-skills
source: https://github.com/alirezarezvani/claude-skills
author: []
published: ''
created: '2026-07-05'
description: '337 Claude Code skills & agent skills & plugins (30+ Agents, 70+ custom
  commands, 330+ skills, customizable references, scripts)for Claude Code, Codex,
  Gemini CLI, Cursor, and 8 more coding agents — engineering, marketing, product,
  compliance, C-level advisory, research, business operations, commercial & finance,
  and your daily productivity skills.Claude Code Skills & Plugins — Agent Skills for
  Every Coding Tool 354 production-ready Claude Code skills, plugins, and agent skills
  for 13 AI coding tools. The most comprehensive open-source library of Claude Code
  skills and agent plugins — also works with OpenAI Codex, Gemini CLI, Cursor, and
  9 more coding agents. Reusable expertise packages covering engineering, DevOps,
  marketing (incl. AEO — Answer Engine Optimization for LLM citation), security (PreToolUse
  hooks), compliance, C-level advisory (incl. founder-mode CFO/CMO/CRO/CPO/COO/CHRO/CISO/GC/CDO/CAIO/CCO/VPE
  personas + 21 /cs:* slash commands), productivity (capture/email/reflect), an academic
  research stack (litreview/grants/dossier/patent/syllabus/pulse/notebooklm/deep-research
  + hybrid router), and enterprise Research Operations (clinical-research/research-finance/market-research/product-research,
  v2.9.0). Works with: Claude Code · OpenAI Codex · Gemini CLI · OpenClaw · Hermes
  Agent[1] · Mistral Vibe[2] · Cursor · Aider · Windsurf · Kilo Code · OpenCode ·
  Augment · Antigravity 5,200+ GitHub stars — the most comprehensive open-source Claude
  Code skills & agent plugins library. What Are Claude Code Skills & Agent Plugins?
  Claude Code skills (also called agent skills or coding agent plugins) are modular
  instruction packages that give AI coding agents domain expertise they don''t have
  out of the box. Each skill includes: SKILL.md — structured instructions, workflows,
  and decision frameworks Python tools — 593 CLI scripts (all stdlib-only, zero pip
  installs) Reference docs — 711 templates, checklists, and domain-specific knowledge
  files One repo, thirteen platforms. Works natively as Claude Code plugins, Codex
  agent skills, Gemini CLI skills, Hermes Agent skills, Mistral Vibe skills, and converts
  to more tools via scripts/convert.sh. All 593 Python tools run anywhere Python runs.
  Skills vs Agents vs Personas Skills Agents Personas Purpose How to execute a task
  What task to do Who is thinking Scope Single domain Single domain Cross-domain Voice
  Neutral Professional Personality-driven Example "Follow these steps for SEO" "Run
  a security audit" "Think like a startup CTO" All three work together. See Orchestration
  for how to combine them. Quick Install Gemini CLI (New) # Clone the repository git
  clone https://github.com/alirezarezvani/claude-skills.git cd claude-skills # Run
  the setup script ./scripts/gemini-install.sh # Start using skills > activate_skill(name="senior-architect")
  Claude Code (Recommended) # Add the marketplace /plugin marketplace add alirezarezvani/claude-skills
  # Install by domain /plugin install engineering-skills@claude-code-skills # 24 core
  engineering /plugin install engineering-advanced-skills@claude-code-skills # 25
  POWERFUL-tier /plugin install product-skills@claude-code-skills # 12 product skills
  /plugin install marketing-skills@claude-code-skills # 43 marketing skills /plugin
  install ra-qm-skills@claude-code-skills # 12 regulatory/quality /plugin install
  pm-skills@claude-code-skills # 6 project management /plugin install c-level-skills@claude-code-skills
  # 28 C-level advisory (full C-suite) /plugin install business-growth-skills@claude-code-skills
  # 4 business & growth /plugin install finance-skills@claude-code-skills # 2 finance
  (analyst + SaaS metrics) # Or install individual skills /plugin install skill-security-auditor@claude-code-skills
  # Security scanner /plugin install playwright-pro@claude-code-skills # Playwright
  testing toolkit /plugin install self-improving-agent@claude-code-skills # Auto-memory
  curation /plugin install content-creator@claude-code-skills # Single skill OpenAI
  Codex npx agent-skills-cli add alirezarezvani/claude-skills --agent codex # Or:
  git clone + ./scripts/codex-install.sh OpenClaw bash <(curl -s https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/scripts/openclaw-install.sh)
  Manual Installation git clone https://github.com/alirezarezvani/claude-skills.git
  # Copy any skill folder to ~/.claude/skills/ (Claude Code) or ~/.codex/skills/ (Codex)
  Multi-Tool Support (New) Convert all 345 skills to 9 AI coding tools with a single
  script: Tool Format Install Cursor .mdc rules ./scripts/install.sh --tool cursor
  --target . Aider CONVENTIONS.md ./scripts/install.sh --tool aider --target . Kilo
  Code .kilocode/rules/ ./scripts/install.sh --tool kilocode --target . Windsurf .windsurf/skills/
  ./scripts/install.sh --tool windsurf --target . OpenCode .opencode/skills/ ./scripts/install.sh
  --tool opencode --target . Augment .augment/rules/ ./scripts/install.sh --tool augment
  --target . Antigravity ~/.gemini/antigravity/skills/ ./scripts/install.sh --tool
  antigravity Hermes Agent ~/.hermes/skills/ python scripts/sync-hermes-skills.py
  --verbose Mistral Vibe ~/.vibe/skills/ ./scripts/vibe-install.sh How it works: #
  1. Convert all skills to all tools (takes ~15 seconds) ./scripts/convert.sh --tool
  all # 2. Install into your project (with confirmation) ./scripts/install.sh --tool
  cursor --target /path/to/project # Or use --force to skip confirmation: ./scripts/install.sh
  --tool aider --target . --force # 3. Verify find .cursor/rules -name "*.mdc" | wc
  -l # Should show 346 Each tool gets: ✅ All 345 skills converted to native format
  ✅ Per-tool README with install/verify/update steps ✅ Support for scripts, references,
  templates where applicable ✅ Zero manual conversion work Run ./scripts/convert.sh
  --tool all to generate tool-specific outputs locally. Skills Overview 354 skills
  across 18 domains: Domain Skills Highlights Details 🔧 Engineering — Core 52 Architecture,
  frontend, backend, fullstack, QA, DevOps, SecOps, AI/ML, data, Playwright Pro (test
  gen, flaky fix, migrations), self-improving agent (auto-memory curation), security
  suite, a11y audit, named-persona-adversarial-review (review via named engineering
  philosophies) engineering-team/ ⚡ Engineering — POWERFUL 80 Agent designer, RAG
  architect, database designer, CI/CD builder, security auditor, MCP builder, AgentHub,
  Helm charts, Terraform, self-eval, llm-wiki, tc-tracker, autoresearch-agent, reliability
  portfolio (feature-flags-architect, kubernetes-operator, chaos-engineering, slo-architect),
  ship-gate, security-guidance PreToolUse hook, Matt Pocock skills (write-a-skill,
  caveman, grill-me, handoff, grill-with-docs), zero-hallucination-coder (Discuss→Map→Decompose→Execute→Verify)
  engineering/ 🎯 Product 17 Product manager, agile PO, strategist, UX researcher,
  UI design, landing pages, SaaS scaffolder, analytics, experiment designer, discovery,
  roadmap communicator, code-to-prd, apple-hig-expert product-team/ 📣 Marketing 48
  8 pods: Content, SEO + AEO (aeo — E-E-A-T audit, citation tracking across 5 LLMs)
  + local (local-seo-manager — GBP/NAP/Map-Pack), CRO, Channels, Growth, Intelligence,
  Sales + context foundation + orchestration router marketing-skill/ 🚀 Productivity
  7 capture (brain-dump-to-action), email pair (inbox-setup + inbox-triage), reflect
  (journal), handoff (Matt Pocock-inspired), andreessen (market-first decision mode),
  roast (5-angle idea panel → GO/RESHAPE/KILL) productivity/ 🎨 Marketing (top-level)
  1 landing — single-file HTML landing-page generator (4 design styles, GSAP patterns,
  brand palette validator) marketing/ 🔬 Research (academic) 9 research orchestrator
  (hybrid router + fallback) + 8 specialists: pulse, litreview, grants (NIH), dossier,
  patent, syllabus, notebooklm, deep-research (rigor-first meta-research) research/
  🧪 Research Operations ✨v2.9.0 5 Enterprise/cross-functional research: orchestrator
  + clinical-research (study design), research-finance (R&D program finance), market-research
  (sizing/survey/segmentation), product-research (user research) — each with onboarding
  + customization + opt-in autoresearch bridge research-ops/ 📋 Project Management
  9 Senior PM, scrum master, Jira, Confluence, Atlassian admin, templates + bundled
  Atlassian Remote MCP project-management/ 🏥 Regulatory & QM 19 ISO 13505, MDR 2017/745,
  FDA, ISO 27001, GDPR, SOC 2, CAPA, risk management, agent-decision-receipts (PQ-signed
  action receipts) ra-qm-team/ 🛡️ Compliance OS 9 Compliance operating system — controls,
  evidence, audit-readiness workflows compliance-os/ 💼 C-Level Advisory 68 Full C-suite
  (CEO/CTO/CFO/CMO/CRO/CPO/COO/CHRO/CISO/GC/CDO/CAIO/CCO/VPE) + founder-mode agents
  + orchestration + board meetings + culture & collaboration c-level-advisor/ 📈 Business
  & Growth 5 Customer success, sales engineer, revenue ops, contracts & proposals,
  BizDev toolkit business-growth/ 🏭 Business Operations 7 Orchestrator + process-mapper,
  vendor-management, capacity-planner, internal-comms, knowledge-ops, procurement-optimizer
  business-operations/ 🤝 Commercial 8 Orchestrator + pricing-strategist, deal-desk,
  partnerships-architect, channel-economics, commercial-policy, rfp-responder, commercial-forecaster
  commercial/ 💰 Finance 4 Financial analyst (DCF, budgeting, forecasting), SaaS metrics
  coach, business investment advisor finance/ 🔄 Loop Library 1 loop-library — discover,
  find, audit/repair, adapt, and design bounded AI-agent loops; reads the live catalog
  from signals.forwardfuture.ai at runtime (vendored verbatim from Forward-Future/loop-library)
  loop-library/ 📄 Markdown → HTML 5 markdown-html-orchestrator (doctype router) +
  design-system (WCAG-AA brand tokens) + md-document (long-form) + md-review (2-col
  code review) + md-slides (single-file deck) — markdown-to-interactive-HTML converter
  markdown-html/ Personas Pre-configured agent identities with curated skill loadouts,
  workflows, and distinct communication styles. Personas go beyond "use these skills"
  — they define how an agent thinks, prioritizes, and communicates. Persona Domain
  Best For Startup CTO Engineering + Strategy Architecture decisions, tech stack selection,
  team building, technical due diligence Growth Marketer Marketing + Growth Content-led
  growth, launch strategy, channel optimization, bootstrapped marketing Solo Founder
  Cross-domain One-person startups, side projects, MVP building, wearing all hats
  Usage: # Claude Code cp agents/personas/startup-cto.md ~/.claude/agents/ # Any tool
  ./scripts/convert.sh --tool cursor # Converts personas too See agents/personas/
  for details. Create your own with TEMPLATE.md. Orchestration A lightweight protocol
  for coordinating personas, skills, and agents on work that crosses domain boundaries.
  No framework required. Four patterns: Pattern What When Solo Sprint Switch personas
  across project phases Side projects, MVPs, solo founders Domain Deep-Dive One persona
  + multiple stacked skills Architecture reviews, compliance audits Multi-Agent Handoff
  Personas review each other''s output High-stakes decisions, launch readiness Skill
  Chain Sequential skills, no persona needed Content pipelines, repeatable checklists
  Example: 6-week product launch Week 1-2: startup-cto + aws-solution-architect +
  senior-frontend → Build Week 3-4: growth-marketer + launch-strategy + copywriting
  + seo-audit → Prepare Week 5-6: solo-founder + email-sequence + analytics-tracking
  → Ship and iterate See orchestration/ORCHESTRATION.md for the full protocol and
  examples. POWERFUL Tier 25 advanced skills with deep, production-grade capabilities:
  Skill What It Does agent-designer Multi-agent orchestration, tool schemas, performance
  evaluation agent-workflow-designer Sequential, parallel, router, orchestrator, and
  evaluator patterns rag-architect RAG pipeline builder, chunking optimizer, retrieval
  evaluator database-designer Schema analyzer, ERD generation, index optimizer, migration
  generator database-schema-designer Requirements → migrations, types, seed data,
  RLS policies migration-architect Migration planner, compatibility checker, rollback
  generator skill-security-auditor 🔒 Security gate — scan skills for malicious code
  before installation ci-cd-pipeline-builder Analyze stack → generate GitHub Actions
  / GitLab CI configs mcp-server-builder Build MCP servers from OpenAPI specs pr-review-expert
  Blast radius analysis, security scan, coverage delta api-design-reviewer REST API
  linter, breaking change detector, design scorecard api-test-suite-builder Scan API
  routes → generate complete test suites dependency-auditor Multi-language scanner,
  license compliance, upgrade planner observability-designer SLO designer, alert optimizer,
  dashboard generator performance-profiler Node/Python/Go profiling, bundle analysis,
  load testing monorepo-navigator Turborepo/Nx/pnpm workspace management & impact
  analysis changelog-generator Conventional commits → structured changelogs codebase-onboarding
  Auto-generate onboarding docs from codebase analysis runbook-generator Codebase
  → operational runbooks with commands git-worktree-manager Parallel dev with port
  isolation, env sync env-secrets-manager .env management, leak detection, rotation
  workflows incident-commander Incident response playbook, severity classifier, PIR
  generator tech-debt-tracker Codebase debt scanner, prioritizer, trend dashboard
  interview-system-designer Interview loop designer, question bank, calibrator 🔒 Skill
  Security Auditor New in v2.0.0 — audit any skill for security risks before installation:
  python3 engineering/skill-security-auditor/scripts/skill_security_auditor.py /path/to/skill/
  Scans for: command injection, code execution, data exfiltration, prompt injection,
  dependency supply chain risks, privilege escalation. Returns PASS / WARN / FAIL
  with remediation guidance. Zero dependencies. Works anywhere Python runs. Recently
  Enhanced Skills Production-quality upgrades added for: engineering/git-worktree-manager
  — worktree lifecycle + cleanup automation scripts engineering/mcp-server-builder
  — OpenAPI -> MCP scaffold + manifest validator engineering/changelog-generator —
  release note generator + conventional commit linter engineering/ci-cd-pipeline-builder
  — stack detector + pipeline generator marketing-skill/prompt-engineer-toolkit —
  prompt A/B tester + prompt version/diff manager Each now ships with scripts/, extracted
  references/, and a usage-focused README.md. Usage Examples Architecture Review Using
  the senior-architect skill, review our microservices architecture and identify the
  top 3 scalability risks. Content Creation Using the content-creator skill, write
  a blog post about AI-augmented development. Optimize for SEO targeting "Claude Code
  tutorial". Compliance Audit Using the mdr-745-specialist skill, review our technical
  documentation for MDR Annex II compliance gaps. Python Analysis Tools 580 CLI tools
  ship with the skills (all verified, stdlib-only): # SaaS health check python3 finance/saas-metrics-coach/scripts/metrics_calculator.py
  --mrr 80000 --customers 200 --churned 3 --json # Brand voice analysis python3 marketing-skill/content-production/scripts/brand_voice_analyzer.py
  article.txt # Tech debt scoring python3 c-level-advisor/cto-advisor/scripts/tech_debt_analyzer.py
  /path/to/codebase # RICE prioritization python3 product-team/product-manager-toolkit/scripts/rice_prioritizer.py
  features.csv # Security audit python3 engineering/skill-security-auditor/scripts/skill_security_auditor.py
  /path/to/skill/ # Landing page (TSX + Tailwind) python3 product-team/landing-page-generator/scripts/landing_page_scaffolder.py
  config.json --format tsx Related Projects Project Description Claude Code Skills
  & Agents Factory Methodology for building skills at scale Claude Code Tresor Productivity
  toolkit with 60+ prompt templates Product Manager Skills Senior PM agent with 6
  knowledge domains, 12 templates, 30+ frameworks — discovery, strategy, delivery,
  SaaS metrics, career coaching, AI product craft toprank 9 SEO and Google Ads skills
  for Claude Code — connects Google Search Console, PageSpeed Insights, and Google
  Ads API; ships meta tag, schema markup, and keyword bid fixes to source or CMS.
  MIT, 107 stars FAQ How do I install Claude Code plugins? Add the marketplace with
  /plugin marketplace add alirezarezvani/claude-skills, then install any skill bundle
  with /plugin install <name>@claude-code-skills. Do these skills work with OpenAI
  Codex / Cursor / Windsurf / Aider / Mistral Vibe? Yes. Skills work natively with
  13 tools: Claude Code, OpenAI Codex, Gemini CLI, OpenClaw, Hermes Agent, Mistral
  Vibe, Cursor, Aider, Windsurf, Kilo Code, OpenCode, Augment, and Antigravity. Hermes
  Agent and Mistral Vibe both use the same agentskills.io SKILL.md standard — run
  python scripts/sync-hermes-skills.py or ./scripts/vibe-install.sh to install. For
  other tools run ./scripts/convert.sh --tool all then ./scripts/install.sh --tool
  <name>. See Multi-Tool Integrations for details. Will updating break my installation?
  No. We follow semantic versioning and maintain backward compatibility within patch
  releases. Existing script arguments, plugin source paths, and SKILL.md structures
  are never changed in patch versions. See the CHANGELOG for details on each release.
  Are the Python tools dependency-free? Yes. All 593 Python CLI tools use the standard
  library only — zero pip installs required. Every script is verified to run with
  --help. How do I create my own Claude Code skill? Each skill is a folder with a
  SKILL.md (frontmatter + instructions), optional scripts/, references/, and assets/.
  See the Skills & Agents Factory for a step-by-step guide. Contributing We welcome
  contributions! See CONTRIBUTING.md for guidelines. Quick ideas: Add new skills in
  underserved domains Improve existing Python tools Add test coverage for scripts
  Translate skills for non-English markets License MIT — see LICENSE for details.
  Star History Built by Alireza Rezvani · Medium · Twitter Hermes Agent is BYO-sync
  tier: the repo ships a pre-generated .hermes/skills/claude-skills/ tree, but you
  run python scripts/sync-hermes-skills.py once locally to install into ~/.hermes/skills/.
  Uses the same agentskills.io SKILL.md standard — no format conversion. ↩︎ Mistral
  Vibe is also BYO-sync tier: the repo ships a pre-generated .vibe/skills/claude-skills/
  tree, run ./scripts/vibe-install.sh once locally to install into ~/.vibe/skills/.
  Same agentskills.io SKILL.md standard — no format conversion. Docs: https://docs.mistral.ai/mistral-vibe/agents-skills.
  ↩︎'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 3cb7ff1cdcf97c6b
manifest_dates:
- '2026-07-05'
- '2026-07-06'
- '2026-07-07'
source_type: community_discussion
tldr: alirezarezvani/claude-skills 是一个包含 354 个生产就绪技能的开源仓库，支持 Claude Code、OpenAI Codex、Gemini
  CLI、Cursor 等 13 种 AI 编码工具，覆盖工程、营销、产品、合规、C 级顾问、学术研究和商业运营等 18 个领域，已获得 5200+ GitHub
  Star。
objective_summary: Alireza Rezvani 在 GitHub 上发布了 claude-skills 开源项目，提供 354 个模块化的 AI
  编码代理技能包。每个技能包含 SKILL.md 结构化指令、593 个纯标准库 Python 脚本和 711 个参考模板。该项目通过 convert.sh 脚本支持一键转换为
  13 种 AI 编码工具的本地格式，并提供了预配置的代理人设（Personas）和跨域编排协议（Orchestration），适用于从个人开发者到企业级的多场景
  AI 辅助编程。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - Anthropic
  - OpenAI
  - Google
  - Forward Future
  technologies:
  - Claude Code
  - MCP
  - RAG
  key_people:
  - Alireza Rezvani
  - Matt Pocock
key_logic_flow:
- alirezarezvani/claude-skills 是一个开源仓库，提供 354 个生产就绪的 AI 编码代理技能，覆盖 18 个领域。
- 该项目支持 Claude Code、OpenAI Codex、Gemini CLI、Cursor、Aider、Windsurf 等 13 种 AI 编码工具，通过
  convert.sh 脚本实现一键格式转换。
- 每个技能包含 SKILL.md 结构化指令、593 个纯标准库 Python 脚本和 711 个参考文档模板，所有脚本无需 pip 安装即可运行。
- 项目提供 Skills（如何执行）、Agents（执行什么任务）和 Personas（谁在思考）三层架构，以及 Solo Sprint、Domain Deep-Dive
  等四种跨域编排模式。
- 预置了 Startup CTO、Growth Marketer、Solo Founder 等代理人设，以及完整 C 级高管（CEO/CTO/CFO/CMO 等）顾问技能包和
  21 个斜杠命令。
- 项目还包含学术研究栈（文献综述、基金申请、专利分析等）、企业研究运营（临床研究、市场研究等）和合规操作系统等专业领域技能。
specialized_tags:
  github:
    projectName: alirezarezvani/claude-skills
    projectUrl: https://github.com/alirezarezvani/claude-skills
    primaryLanguage: Python
    licenseType: null
    domain: ai_ml
    crossTags:
    - agent-skills
    - multi-platform
    - cli-tool
    aiDetail:
      primaryCategories:
      - agent_framework
      agentSubcategory:
      - orchestration
      - tool_use
      techTags:
      - RAG
      - MCP
      - function-calling
extract_result: success
object_mentions:
- object_type: project
  name: alirezarezvani/claude-skills
  canonical_name: alirezarezvani/claude-skills
  url: https://github.com/alirezarezvani/claude-skills
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 该仓库包含 354 个生产就绪的 Claude Code 技能，覆盖工程、营销、产品、合规和 C 级顾问等 18 个领域，已获得 5200+ GitHub
    Star。
  - 支持 Claude Code、OpenAI Codex、Gemini CLI、Cursor 等 13 种 AI 编码工具，通过单个 convert.sh 脚本即可完成所有格式转换。
  - 项目包含 593 个纯标准库 Python 脚本和 711 个参考文档模板，所有脚本无需任何 pip 安装即可直接运行。
  article_id: 3cb7ff1cdcf97c6b
- object_type: project
  name: Forward-Future/loop-library
  canonical_name: Forward-Future/loop-library
  url: https://github.com/Forward-Future/loop-library
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 该项目的 loop-library 技能直接从 signals.forwardfuture.ai 实时读取目录，并逐字转述自 Forward-Future/loop-library
    仓库。
  - loop-library 技能可发现、审计、修复和设计有边界的 AI 代理循环，运行时从 signals.forwardfuture.ai 读取最新目录。
  article_id: 3cb7ff1cdcf97c6b
impact_score:
  score: 6.0
  reason: 该项目是当前最全面的 AI 编程智能体技能开源库，354 个技能覆盖 18 个领域，支持 13 种编码工具，并附带 593 个零依赖 Python
    CLI 脚本和 711 份参考文档。其价值在于系统化组织与跨平台兼容性，显著降低了开发者使用 AI 编码工具的门槛。但本质上这是对现有 AI 编程工具能力的工程化整合与增强，并未改变底层模型能力或引入全新推理范式。属于重要的生态基础设施型项目，短期行业冲击力中等偏上——对
    AI 编码工具的用户体验提升明显，但不足以构成行业范式转移。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 354 个技能覆盖 18 个领域，且支持 13 种 AI 编程工具的一键跨平台转换
hype_assessment:
  level: low
  reason: 项目描述采用了具体可验证的量化指标（354 个技能、593 个 Python 脚本、711 份参考文档、18 个领域），而非空洞的 PR 话术。'最全面的开源技能库'这一主张有充分数据支撑。全文以技术细节和安装说明为主，未出现
    '颠覆式'、'革命性' 等过度宣传用语。该项目确实交付了实质性的工程化成果，包装程度低。
information_entropy: high
domain_disruption:
  technical_innovation: 无底层算法或架构层面的本质突破。创新点在于工程化整合：将 AI 编码智能体的技能/指令模式系统化组织为 18 个领域模块，并通过
    `convert.sh` 脚本实现跨 13 种工具的格式自动转换。593 个纯 Python CLI 脚本全部依赖标准库（零 pip 安装），体现了良好的工程实践，但属于现有技术的组合应用。
  business_model: 开源社区驱动的生态赋能模式。该项目降低了 AI 编程工具的上手门槛和 prompt 工程成本，有助于加速 AI 编码工具的行业渗透率。对企业用户而言可显著减少内部
    prompt 编写和维护投入，但对现有商业模式未构成冲击或重塑。
engineering_complexity: production_ready
compound_value:
  score: 6.5
  reason: 该项目代表了 AI 编程智能体技能层的标准化与生态化趋势，核心价值在于三个方面：一是 354 个跨 18 领域技能库形成了可复用的知识资产池，具有网络效应潜力（贡献者越多价值越大）；二是跨
    13 个工具的格式转换能力打破了平台锁定，降低了用户的迁移成本，这在生态早期具有战略卡位价值；三是 4 种编排模式试图定义 Agent 协作的工作流范式。但作为个人维护的开源项目（非公司实体），缺乏商业变现机制和长期维护承诺，项目可持续性存疑。真正的复利价值不在项目本身，而在于它加速了
    Agent 技能标准化这一趋势——一旦行业形成对这类技能库的依赖，类似于 npm 之于 JavaScript 生态，其基础设施价值会被释放。然而当前阶段仍属早期探索，标准化尚未形成行业共识，给
    6.5 分反映其潜力与不确定性并存。
value_capture_layer: agent_middleware
moat_impact: democratizes_access
key_beneficiaries:
- Cursor
- Aider
- Windsurf
- Kilo Code
- OpenCode
- Augment
- Anthropic
competitive_casualty:
- 专有封闭式编码助手（如无自定义技能机制的竞品）
- 传统 IDE 付费插件市场
- 靠平台锁定盈利的闭源 Agent 生态
market_opportunities:
- 企业可基于该技能库构建标准化的 AI 编程助手工作流，将 18 个领域的专家知识一次性注入团队开发环境，显著降低 prompt engineering 的重复成本
- 创业团队可利用其多工具兼容（13 种）特性开发垂直行业的技能包插件（如医疗合规、金融审计），以开源底座 + 付费增值模式获取企业客户
- 个人开发者可通过深入学习 POWERFUL 级别技能（RAG 架构、Agent 设计、安全审计）快速补齐全栈架构能力，缩短从初级到高级工程师的成长路径
risk_matrix:
  regulatory: 技能库涵盖合规与监管质量（Regulatory/Quality）领域，若用户基于这些技能做出的决策产生合规失误，可能导致间接法律责任；AEO（Answer
    Engine Optimization）技能可能涉及搜索引擎操纵风险
  technological: 354 个技能依赖特定 AI 工具的指令格式和模型行为，随着 Claude Code、Codex 等工具的版本迭代，部分技能可能失效或需要持续适配，维护负担较重
  competitive: 技能库完全开源且免费，缺乏直接商业模式，可能被大厂（Anthropic、OpenAI）原生内置替代，或面临更优质竞品（如更专业的细分领域技能库）的生态挤压
  ethical: 安全审计技能存在双重用途风险（可用于白帽也可用于黑帽）；C 级顾问角色给出的商业建议缺乏问责机制，可能误导创业者做出错误决策；营销类技能可能加剧信息操纵和偏见传播
  additional:
  - 354 个技能质量参差不齐，部分技能可能仅含浅层提示词，用户需要花费甄别成本
  - 该项目依赖单一维护者（alirezarezvani），存在维护者倦怠或项目停摆的 bus factor 风险
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: deep_dive
object_insights:
- object_type: project
  name: alirezarezvani/claude-skills
  canonical_name: alirezarezvani/claude-skills
  url: https://github.com/alirezarezvani/claude-skills
  positioning: 开源 AI 编码代理技能库，提供 354 个覆盖 18 领域的模块化技能包，支持 13 种主流 AI 编码工具的一键格式转换。
  technical_signal: 基于 SKILL.md 结构化指令、593 个纯标准库 Python 脚本和 711 个参考模板的三层架构，所有脚本无需 pip
    安装即可直接运行。
  adoption_signal: GitHub 已获得 5200+ Star，支持 Claude Code、OpenAI Codex、Gemini CLI、Cursor
    等 13 种主流 AI 编码工具的一键格式转换。
  ecosystem_relevance: 填补了 AI 编码代理缺乏跨工具、跨领域标准化技能包的空白，大幅降低了专业领域知识注入 AI 编码助手的门槛。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 作为目前最全面的开源 AI 编码代理技能库，其跨 13 种工具的兼容性和 18 个领域的覆盖范围使其可能成为 AI 辅助编程领域的标准化基础组件，值得长期关注其社区增长和生态渗透情况。
  risk_notes:
  - 354 个技能的维护负担较大，随 AI 编码工具 API 变更可能导致兼容性问题。
  - 技能质量依赖社区贡献，不同领域的技能深度和实用性可能存在较大差异。
  score: 7.0
  article_ids:
  - 3cb7ff1cdcf97c6b
  evidence_snippets:
  - 该仓库包含 354 个生产就绪的 Claude Code 技能，覆盖工程、营销、产品、合规和 C 级顾问等 18 个领域，已获得 5200+ GitHub
    Star。
  - 支持 Claude Code、OpenAI Codex、Gemini CLI、Cursor 等 13 种 AI 编码工具，通过单个 convert.sh 脚本即可完成所有格式转换。
  - 项目包含 593 个纯标准库 Python 脚本和 711 个参考文档模板，所有脚本无需任何 pip 安装即可直接运行。
- object_type: project
  name: Forward-Future/loop-library
  canonical_name: Forward-Future/loop-library
  url: https://github.com/Forward-Future/loop-library
  positioning: 专为 AI 代理循环生命周期管理设计的开源工具库，提供可发现、审计、修复和设计有边界循环的核心能力。
  technical_signal: 通过 signals.forwardfuture.ai 实时目录服务驱动代理循环管理，可实现动态发现与审计的自动化工作流。
  adoption_signal: null
  ecosystem_relevance: 作为 claude-skills 生态中的专业代理循环管理组件，为 AI 代理行为边界控制提供了可复用的工程化工具。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 作为 AI 代理循环边界管理的专业化工具，其与 claude-skills 的集成表明在代理行为治理领域有独特定位，值得关注其独立发展和生态合作进展。
  risk_notes:
  - 当前仅通过 claude-skills 的间接引用获知，缺乏独立的社区活跃度和用户数据支撑。
  - 依赖外部 signals.forwardfuture.ai 实时服务运行，存在服务可用性和数据源持续性的单点风险。
  score: 3.0
  article_ids:
  - 3cb7ff1cdcf97c6b
  evidence_snippets:
  - 该项目的 loop-library 技能直接从 signals.forwardfuture.ai 实时读取目录，并逐字转述自 Forward-Future/loop-library
    仓库。
  - loop-library 技能可发现、审计、修复和设计有边界的 AI 代理循环，运行时从 signals.forwardfuture.ai 读取最新目录。
---

**354 production-ready Claude Code skills, plugins, and agent skills for 13 AI coding tools.**

The most comprehensive open-source library of Claude Code skills and agent plugins — also works with OpenAI Codex, Gemini CLI, Cursor, and 9 more coding agents. Reusable expertise packages covering engineering, DevOps, marketing (incl. AEO — Answer Engine Optimization for LLM citation), security (PreToolUse hooks), compliance, C-level advisory (incl. founder-mode CFO/CMO/CRO/CPO/COO/CHRO/CISO/GC/CDO/CAIO/CCO/VPE personas + 21 /cs:* slash commands), productivity (capture/email/reflect), an academic research stack (litreview/grants/dossier/patent/syllabus/pulse/notebooklm/deep-research + hybrid router), and enterprise Research Operations (clinical-research/research-finance/market-research/product-research, v2.9.0).

**Works with:** Claude Code · OpenAI Codex · Gemini CLI · OpenClaw · Hermes Agent1 · Mistral Vibe2 · Cursor · Aider · Windsurf · Kilo Code · OpenCode · Augment · Antigravity


5,200+ GitHub stars— the most comprehensive open-source Claude Code skills & agent plugins library.

Claude Code skills (also called agent skills or coding agent plugins) are modular instruction packages that give AI coding agents domain expertise they don't have out of the box. Each skill includes:

**SKILL.md**— structured instructions, workflows, and decision frameworks**Python tools**— 593 CLI scripts (all stdlib-only, zero pip installs)**Reference docs**— 711 templates, checklists, and domain-specific knowledge files

**One repo, thirteen platforms.** Works natively as Claude Code plugins, Codex agent skills, Gemini CLI skills, Hermes Agent skills, Mistral Vibe skills, and converts to more tools via `scripts/convert.sh`

. All 593 Python tools run anywhere Python runs.

| Skills | Agents | Personas | |
|---|---|---|---|
Purpose |
How to execute a task | What task to do | Who is thinking |
Scope |
Single domain | Single domain | Cross-domain |
Voice |
Neutral | Professional | Personality-driven |
Example |
"Follow these steps for SEO" | "Run a security audit" | "Think like a startup CTO" |

All three work together. See Orchestration for how to combine them.

```
# Clone the repository
git clone https://github.com/alirezarezvani/claude-skills.git
cd claude-skills
# Run the setup script
./scripts/gemini-install.sh
# Start using skills
> activate_skill(name="senior-architect")
```

```
# Add the marketplace
/plugin marketplace add alirezarezvani/claude-skills
# Install by domain
/plugin install engineering-skills@claude-code-skills # 24 core engineering
/plugin install engineering-advanced-skills@claude-code-skills # 25 POWERFUL-tier
/plugin install product-skills@claude-code-skills # 12 product skills
/plugin install marketing-skills@claude-code-skills # 43 marketing skills
/plugin install ra-qm-skills@claude-code-skills # 12 regulatory/quality
/plugin install pm-skills@claude-code-skills # 6 project management
/plugin install c-level-skills@claude-code-skills # 28 C-level advisory (full C-suite)
/plugin install business-growth-skills@claude-code-skills # 4 business & growth
/plugin install finance-skills@claude-code-skills # 2 finance (analyst + SaaS metrics)
# Or install individual skills
/plugin install skill-security-auditor@claude-code-skills # Security scanner
/plugin install playwright-pro@claude-code-skills # Playwright testing toolkit
/plugin install self-improving-agent@claude-code-skills # Auto-memory curation
/plugin install content-creator@claude-code-skills # Single skill
```

```
npx agent-skills-cli add alirezarezvani/claude-skills --agent codex
# Or: git clone + ./scripts/codex-install.sh
```

`bash <(curl -s https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/scripts/openclaw-install.sh)`

```
git clone https://github.com/alirezarezvani/claude-skills.git
# Copy any skill folder to ~/.claude/skills/ (Claude Code) or ~/.codex/skills/ (Codex)
```

**Convert all 345 skills to 9 AI coding tools** with a single script:

| Tool | Format | Install |
|---|---|---|
Cursor |
`.mdc` rules |
`./scripts/install.sh --tool cursor --target .` |
Aider |
`CONVENTIONS.md` |
`./scripts/install.sh --tool aider --target .` |
Kilo Code |
`.kilocode/rules/` |
`./scripts/install.sh --tool kilocode --target .` |
Windsurf |
`.windsurf/skills/` |
`./scripts/install.sh --tool windsurf --target .` |
OpenCode |
`.opencode/skills/` |
`./scripts/install.sh --tool opencode --target .` |
Augment |
`.augment/rules/` |
`./scripts/install.sh --tool augment --target .` |
Antigravity |
`~/.gemini/antigravity/skills/` |
`./scripts/install.sh --tool antigravity` |
Hermes Agent |
`~/.hermes/skills/` |
`python scripts/sync-hermes-skills.py --verbose` |
Mistral Vibe |
`~/.vibe/skills/` |
`./scripts/vibe-install.sh` |

**How it works:**

```
# 1. Convert all skills to all tools (takes ~15 seconds)
./scripts/convert.sh --tool all
# 2. Install into your project (with confirmation)
./scripts/install.sh --tool cursor --target /path/to/project
# Or use --force to skip confirmation:
./scripts/install.sh --tool aider --target . --force
# 3. Verify
find .cursor/rules -name "*.mdc" | wc -l # Should show 346
```

**Each tool gets:**

- ✅ All 345 skills converted to native format
- ✅ Per-tool README with install/verify/update steps
- ✅ Support for scripts, references, templates where applicable
- ✅ Zero manual conversion work

Run `./scripts/convert.sh --tool all`

to generate tool-specific outputs locally.

**354 skills across 18 domains:**

| Domain | Skills | Highlights | Details |
|---|---|---|---|
🔧 Engineering — Core |
52 | Architecture, frontend, backend, fullstack, QA, DevOps, SecOps, AI/ML, data, Playwright Pro (test gen, flaky fix, migrations), self-improving agent (auto-memory curation), security suite, a11y audit, named-persona-adversarial-review (review via named engineering philosophies) |
engineering-team/ |
⚡ Engineering — POWERFUL |
80 | Agent designer, RAG architect, database designer, CI/CD builder, security auditor, MCP builder, AgentHub, Helm charts, Terraform, self-eval, llm-wiki, tc-tracker, autoresearch-agent, reliability portfolio (feature-flags-architect, kubernetes-operator, chaos-engineering, slo-architect), ship-gate, security-guidance PreToolUse hook, Matt Pocock skills (write-a-skill, caveman, grill-me, handoff, grill-with-docs), zero-hallucination-coder (Discuss→Map→Decompose→Execute→Verify) |
engineering/ |
🎯 Product |
17 | Product manager, agile PO, strategist, UX researcher, UI design, landing pages, SaaS scaffolder, analytics, experiment designer, discovery, roadmap communicator, code-to-prd, apple-hig-expert | product-team/ |
📣 Marketing |
48 | 8 pods: Content, SEO + AEO (`aeo` — E-E-A-T audit, citation tracking across 5 LLMs) + local (`local-seo-manager` — GBP/NAP/Map-Pack), CRO, Channels, Growth, Intelligence, Sales + context foundation + orchestration router |
marketing-skill/ |
🚀 Productivity |
7 | `capture` (brain-dump-to-action), `email` pair (inbox-setup + inbox-triage), `reflect` (journal), `handoff` (Matt Pocock-inspired), `andreessen` (market-first decision mode), `roast` (5-angle idea panel → GO/RESHAPE/KILL) |
productivity/ |
🎨 Marketing (top-level) |
1 | `landing` — single-file HTML landing-page generator (4 design styles, GSAP patterns, brand palette validator) |
marketing/ |
🔬 Research (academic) |
9 | `research` orchestrator (hybrid router + fallback) + 8 specialists: `pulse` , `litreview` , `grants` (NIH), `dossier` , `patent` , `syllabus` , `notebooklm` , `deep-research` (rigor-first meta-research) |
research/ |
🧪 Research Operations ✨v2.9.0 |
5 | Enterprise/cross-functional research: orchestrator + `clinical-research` (study design), `research-finance` (R&D program finance), `market-research` (sizing/survey/segmentation), `product-research` (user research) — each with onboarding + customization + opt-in autoresearch bridge |
research-ops/ |
📋 Project Management |
9 | Senior PM, scrum master, Jira, Confluence, Atlassian admin, templates + bundled Atlassian Remote MCP | project-management/ |
🏥 Regulatory & QM |
19 | ISO 13505, MDR 2017/745, FDA, ISO 27001, GDPR, SOC 2, CAPA, risk management, agent-decision-receipts (PQ-signed action receipts) | ra-qm-team/ |
🛡️ Compliance OS |
9 | Compliance operating system — controls, evidence, audit-readiness workflows | compliance-os/ |
💼 C-Level Advisory |
68 | Full C-suite (CEO/CTO/CFO/CMO/CRO/CPO/COO/CHRO/CISO/GC/CDO/CAIO/CCO/VPE) + founder-mode agents + orchestration + board meetings + culture & collaboration | c-level-advisor/ |
📈 Business & Growth |
5 | Customer success, sales engineer, revenue ops, contracts & proposals, BizDev toolkit | business-growth/ |
🏭 Business Operations |
7 | Orchestrator + process-mapper, vendor-management, capacity-planner, internal-comms, knowledge-ops, procurement-optimizer | business-operations/ |
🤝 Commercial |
8 | Orchestrator + pricing-strategist, deal-desk, partnerships-architect, channel-economics, commercial-policy, rfp-responder, commercial-forecaster | commercial/ |
💰 Finance |
4 | Financial analyst (DCF, budgeting, forecasting), SaaS metrics coach, business investment advisor | finance/ |
🔄 Loop Library |
1 | `loop-library` — discover, find, audit/repair, adapt, and design bounded AI-agent loops; reads the live catalog from signals.forwardfuture.ai at runtime (vendored verbatim from Forward-Future/loop-library) |
loop-library/ |
📄 Markdown → HTML |
5 | `markdown-html-orchestrator` (doctype router) + `design-system` (WCAG-AA brand tokens) + `md-document` (long-form) + `md-review` (2-col code review) + `md-slides` (single-file deck) — markdown-to-interactive-HTML converter |
markdown-html/ |

Pre-configured agent identities with curated skill loadouts, workflows, and distinct communication styles. Personas go beyond "use these skills" — they define how an agent thinks, prioritizes, and communicates.

| Persona | Domain | Best For |
|---|---|---|
Startup CTO |
Engineering + Strategy | Architecture decisions, tech stack selection, team building, technical due diligence |
Growth Marketer |
Marketing + Growth | Content-led growth, launch strategy, channel optimization, bootstrapped marketing |
Solo Founder |
Cross-domain | One-person startups, side projects, MVP building, wearing all hats |

**Usage:**

```
# Claude Code
cp agents/personas/startup-cto.md ~/.claude/agents/
# Any tool
./scripts/convert.sh --tool cursor # Converts personas too
```

See agents/personas/ for details. Create your own with TEMPLATE.md.

A lightweight protocol for coordinating personas, skills, and agents on work that crosses domain boundaries. No framework required.

**Four patterns:**

| Pattern | What | When |
|---|---|---|
Solo Sprint |
Switch personas across project phases | Side projects, MVPs, solo founders |
Domain Deep-Dive |
One persona + multiple stacked skills | Architecture reviews, compliance audits |
Multi-Agent Handoff |
Personas review each other's output | High-stakes decisions, launch readiness |
Skill Chain |
Sequential skills, no persona needed | Content pipelines, repeatable checklists |

**Example: 6-week product launch**

```
Week 1-2: startup-cto + aws-solution-architect + senior-frontend → Build
Week 3-4: growth-marketer + launch-strategy + copywriting + seo-audit → Prepare
Week 5-6: solo-founder + email-sequence + analytics-tracking → Ship and iterate
```


See orchestration/ORCHESTRATION.md for the full protocol and examples.

25 advanced skills with deep, production-grade capabilities:

| Skill | What It Does |
|---|---|
agent-designer |
Multi-agent orchestration, tool schemas, performance evaluation |
agent-workflow-designer |
Sequential, parallel, router, orchestrator, and evaluator patterns |
rag-architect |
RAG pipeline builder, chunking optimizer, retrieval evaluator |
database-designer |
Schema analyzer, ERD generation, index optimizer, migration generator |
database-schema-designer |
Requirements → migrations, types, seed data, RLS policies |
migration-architect |
Migration planner, compatibility checker, rollback generator |
skill-security-auditor |
🔒 Security gate — scan skills for malicious code before installation |
ci-cd-pipeline-builder |
Analyze stack → generate GitHub Actions / GitLab CI configs |
mcp-server-builder |
Build MCP servers from OpenAPI specs |
pr-review-expert |
Blast radius analysis, security scan, coverage delta |
api-design-reviewer |
REST API linter, breaking change detector, design scorecard |
api-test-suite-builder |
Scan API routes → generate complete test suites |
dependency-auditor |
Multi-language scanner, license compliance, upgrade planner |
observability-designer |
SLO designer, alert optimizer, dashboard generator |
performance-profiler |
Node/Python/Go profiling, bundle analysis, load testing |
monorepo-navigator |
Turborepo/Nx/pnpm workspace management & impact analysis |
changelog-generator |
Conventional commits → structured changelogs |
codebase-onboarding |
Auto-generate onboarding docs from codebase analysis |
runbook-generator |
Codebase → operational runbooks with commands |
git-worktree-manager |
Parallel dev with port isolation, env sync |
env-secrets-manager |
.env management, leak detection, rotation workflows |
incident-commander |
Incident response playbook, severity classifier, PIR generator |
tech-debt-tracker |
Codebase debt scanner, prioritizer, trend dashboard |
interview-system-designer |
Interview loop designer, question bank, calibrator |

New in v2.0.0 — audit any skill for security risks before installation:

`python3 engineering/skill-security-auditor/scripts/skill_security_auditor.py /path/to/skill/`

Scans for: command injection, code execution, data exfiltration, prompt injection, dependency supply chain risks, privilege escalation. Returns **PASS / WARN / FAIL** with remediation guidance.

**Zero dependencies.** Works anywhere Python runs.

Production-quality upgrades added for:

`engineering/git-worktree-manager`

— worktree lifecycle + cleanup automation scripts`engineering/mcp-server-builder`

— OpenAPI -> MCP scaffold + manifest validator`engineering/changelog-generator`

— release note generator + conventional commit linter`engineering/ci-cd-pipeline-builder`

— stack detector + pipeline generator`marketing-skill/prompt-engineer-toolkit`

— prompt A/B tester + prompt version/diff manager

Each now ships with `scripts/`

, extracted `references/`

, and a usage-focused `README.md`

.

```
Using the senior-architect skill, review our microservices architecture
and identify the top 3 scalability risks.
```


```
Using the content-creator skill, write a blog post about AI-augmented
development. Optimize for SEO targeting "Claude Code tutorial".
```


```
Using the mdr-745-specialist skill, review our technical documentation
for MDR Annex II compliance gaps.
```


580 CLI tools ship with the skills (all verified, stdlib-only):

```
# SaaS health check
python3 finance/saas-metrics-coach/scripts/metrics_calculator.py --mrr 80000 --customers 200 --churned 3 --json
# Brand voice analysis
python3 marketing-skill/content-production/scripts/brand_voice_analyzer.py article.txt
# Tech debt scoring
python3 c-level-advisor/cto-advisor/scripts/tech_debt_analyzer.py /path/to/codebase
# RICE prioritization
python3 product-team/product-manager-toolkit/scripts/rice_prioritizer.py features.csv
# Security audit
python3 engineering/skill-security-auditor/scripts/skill_security_auditor.py /path/to/skill/
# Landing page (TSX + Tailwind)
python3 product-team/landing-page-generator/scripts/landing_page_scaffolder.py config.json --format tsx
```

| Project | Description |
|---|---|
Claude Code Skills & Agents Factory |
Methodology for building skills at scale |
Claude Code Tresor |
Productivity toolkit with 60+ prompt templates |
Product Manager Skills |
Senior PM agent with 6 knowledge domains, 12 templates, 30+ frameworks — discovery, strategy, delivery, SaaS metrics, career coaching, AI product craft |
toprank |
9 SEO and Google Ads skills for Claude Code — connects Google Search Console, PageSpeed Insights, and Google Ads API; ships meta tag, schema markup, and keyword bid fixes to source or CMS. MIT, 107 stars |

**How do I install Claude Code plugins?**
Add the marketplace with `/plugin marketplace add alirezarezvani/claude-skills`

, then install any skill bundle with `/plugin install <name>@claude-code-skills`

.

**Do these skills work with OpenAI Codex / Cursor / Windsurf / Aider / Mistral Vibe?**
Yes. Skills work natively with 13 tools: Claude Code, OpenAI Codex, Gemini CLI, OpenClaw, Hermes Agent, Mistral Vibe, Cursor, Aider, Windsurf, Kilo Code, OpenCode, Augment, and Antigravity. Hermes Agent and Mistral Vibe both use the same agentskills.io SKILL.md standard — run `python scripts/sync-hermes-skills.py`

or `./scripts/vibe-install.sh`

to install. For other tools run `./scripts/convert.sh --tool all`

then `./scripts/install.sh --tool <name>`

. See Multi-Tool Integrations for details.

**Will updating break my installation?**
No. We follow semantic versioning and maintain backward compatibility within patch releases. Existing script arguments, plugin source paths, and SKILL.md structures are never changed in patch versions. See the CHANGELOG for details on each release.

**Are the Python tools dependency-free?**
Yes. All 593 Python CLI tools use the standard library only — zero pip installs required. Every script is verified to run with `--help`

.

**How do I create my own Claude Code skill?**
Each skill is a folder with a `SKILL.md`

(frontmatter + instructions), optional `scripts/`

, `references/`

, and `assets/`

. See the Skills & Agents Factory for a step-by-step guide.

We welcome contributions! See CONTRIBUTING.md for guidelines.

**Quick ideas:**

- Add new skills in underserved domains
- Improve existing Python tools
- Add test coverage for scripts
- Translate skills for non-English markets

MIT — see LICENSE for details.

**Built by Alireza Rezvani** · Medium · Twitter

## Footnotes

-
Hermes Agent is

**BYO-sync tier**: the repo ships a pre-generated`.hermes/skills/claude-skills/`

tree, but you run`python scripts/sync-hermes-skills.py`

once locally to install into`~/.hermes/skills/`

. Uses the same agentskills.io SKILL.md standard — no format conversion. ↩ -
Mistral Vibe is also

**BYO-sync tier**: the repo ships a pre-generated`.vibe/skills/claude-skills/`

tree, run`./scripts/vibe-install.sh`

once locally to install into`~/.vibe/skills/`

. Same agentskills.io SKILL.md standard — no format conversion. Docs: https://docs.mistral.ai/mistral-vibe/agents-skills. ↩