---
title: Chachamaru127/claude-code-harness
source: https://github.com/Chachamaru127/claude-code-harness
author: []
published: ''
created: '2026-05-28'
description: 'Claude Code Dedicated Development Harness - Achieving High-Quality Development
  Through an Autonomous Plan→Work→Review CycleClaude Code Harness Plan. Work. Review.
  Ship. A disciplined delivery loop for Claude Code, with bounded paths for Codex
  and OpenCode. English | 日本語 Claude Code is powerful, but raw agent work drifts:
  plans live in chat, tests become optional, review happens too late, and release
  evidence gets rebuilt by memory. Harness turns that into one repeatable operating
  path. After install, the default changes from "ask the agent to code" to: write
  the spec and plan, implement only the approved slice, verify the result, review
  independently, package evidence for PR or release. Quickstart New users should start
  from the tool they already use. Existing users should run the migration report before
  cleanup or reinstall. Path Start New user Tool-first onboarding Existing user Migration
  check Claude Code fast path Install in 30 seconds Trigger proof Skill trigger gate
  Install in 30 Seconds claude /plugin marketplace add Chachamaru127/claude-code-harness
  /plugin install claude-code-harness@claude-code-harness-marketplace /harness-setup
  Next command: run /harness-plan with one small request. /harness-plan Improve the
  README onboarding flow First 15 Minutes Install through your tool route. Run /harness-setup
  or the equivalent setup script. Run /harness-plan with a small request; Harness
  writes the spec.md and Plans.md drafts for you to check. Small typo, docs, and status
  updates stay lightweight. Approve the generated contract or reply with the correction
  you want. Run the smallest approved task, for example /harness-work 1.1.1. Run /harness-review
  and keep the verification output. Your job is not to hand-write the plan. It is
  to approve or correct the generated contract before execution continues. How It
  Works Harness adds a source-of-truth loop around agent work. The 5 verb skills keep
  that surface small: plan, work, review, sync, release. You describe the outcome
  in normal language. /harness-plan drafts or updates spec.md and Plans.md with scope,
  acceptance criteria, unknowns, and stop conditions. Non-trivial planning records
  team_validation_mode and validates the plan through team/sub-agent or manual-pass
  perspectives for spec/Plans alignment, memory reuse, product fit, security fit,
  and works-in-practice. Harness treats those files as the source of truth. Data the
  agent has not seen stays unknown instead of being silently invented. /harness-work
  implements the approved slice with TDD and verification. /harness-review separates
  review from implementation. /harness-release packages only verified evidence. Commands
  Command What happens inside /harness-setup Installs project guidance, command surfaces,
  hooks, and checks so the workflow starts from one known baseline. /harness-plan
  Turns intent into spec.md and Plans.md, including scope, acceptance criteria, dependencies,
  unknowns, stop conditions, and non-trivial planning validation. /harness-work Executes
  one approved task or range, adds tests when required, runs verification, and keeps
  work inside the plan. /harness-work all Runs the approved plan through implementation
  and review paths; use after the plan is clear and the repo baseline is known. /harness-review
  Reviews the result separately from implementation and treats major findings as blockers.
  /harness-release Checks release readiness, CHANGELOG/tag boundaries, and evidence
  packaging after implementation and review are complete. bin/harness doctor --migration-report
  Inventories old plugin caches, Codex skills, OpenCode files, symlinks, and memory
  state without deleting data. Basic Workflow Stage Output Gate Investigate Evidence
  and unknowns Do not promote unobserved data into claims. Plan spec.md + Plans.md
  User approves or corrects the generated contract. Work Code and tests TDD required
  when the task says so. Review Independent verdict Major findings block completion.
  PR Evidence pack PR ready is not release ready. Release Tag/release artifacts Release
  preflight must pass on the release path. Install By Tool Tool Tier Route Claude
  Code supported Claude plugin marketplace, then /harness-setup. Codex CLI internal-compatible
  scripts/setup-codex.sh --user; direct plugin smoke is tracked separately. Codex
  app candidate Candidate smoke only; do not reuse Codex CLI proof. OpenCode internal-compatible
  scripts/setup-opencode.sh; runtime parity is not claimed. Cursor candidate PM handoff
  or adapter research only. GitHub Copilot CLI candidate Manual profile research only.
  Antigravity CLI future/unsupported No end-user install route in this phase. Existing
  User Migration Run bin/harness doctor --migration-report before changing an existing
  setup. The report inventories stale Claude plugin caches, duplicate Codex skills,
  old symlinks, OpenCode backup paths, and harness-mem state without deleting anything.
  Support Boundary Harness can describe candidate paths, but it does not inherit support
  claims from Superpowers, Hermes Agent, or any other project. A host only moves up
  when Harness has its own bootstrap, trigger, runtime, and release evidence. not_observed
  != absent: missing local proof means "not proven here", not "impossible" and not
  "supported". Requirements Claude Code v2.1+ for the supported Claude path. A project
  repository with write access for local setup. No Node.js is required for the Go-native
  guardrail engine. Optional harness-mem for cross-session memory when configured
  and healthy. Advanced Use these after the basic trigger path is visible. Capability
  What it adds Boundary Breezing Planner/Critic/Worker style team execution for larger
  task lists. Still gated by plan quality and review. Codex companion review Schema-backed
  Codex second opinion through scripts/codex-companion.sh. Raw codex exec is not the
  Harness companion path. OpenCode bootstrap Mirrors Harness guidance into OpenCode-compatible
  surfaces. Real runtime parity is not claimed. harness-mem Project-scoped memory
  and recall across sessions. Optional companion; purge remains explicit. Documentation
  Resource Description Tool-first onboarding Where to start by host tool. Install
  routes Per-tool setup and support-tier boundaries. Migration check Existing-user
  impact, compatibility, and rollback path. Skill trigger gate How install success
  is verified. Capability matrix Supported, internal-compatible, candidate, and unsupported
  host claims. Claude Code Compatibility Current Claude Code requirements and compatibility
  notes. Cursor Integration Cursor handoff boundary and candidate-route notes. Distribution
  Scope Included vs compatibility vs development-only paths. Hardening parity Runtime
  safety differences between Claude hooks and Codex gates. Work All Evidence Pack
  Success/failure verification contract for full-plan execution. Changelog User-facing
  version history. Contributing Issues and PRs welcome. See CONTRIBUTING.md. Acknowledgments
  AI Masao - Hierarchical skill design Beagle - Test tampering prevention patterns
  License MIT License. See LICENSE.md.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: cea129f9b669edcc
source_type: community_discussion
tldr: Chachamaru127/claude-code-harness 是一个为 Claude Code 提供结构化交付循环的开源插件，通过 Plan、Work、Review、Sync、Release
  五个核心命令将原始代理工作转化为可重复的操作路径，并生成 spec.md 和 Plans.md 作为事实来源。
objective_summary: Chachamaru127 在 GitHub 上发布了 claude-code-harness 项目，这是一个针对 Claude
  Code 的插件，提供从需求描述到发布证据打包的完整工作流。该插件通过 /harness-setup、/harness-plan、/harness-work、/harness-review、/harness-release
  五个命令来约束开发流程，要求用户先审批生成的 spec.md 和 Plans.md 合同文件，再执行具体任务，最后封装验证后的证据用于 PR 或发布。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies: []
  technologies:
  - Claude Code
  - Codex CLI
  - OpenCode
  - Cursor
  - GitHub Copilot CLI
  key_people: []
key_logic_flow:
- claude-code-harness 将默认的"让代理直接编码"模式转变为先编写规范和计划、再实现已审批切片、然后验证结果、独立审查、最后打包证据用于 PR
  或发布的五步流程。
- 用户通过 /harness-plan 命令将需求转化为 spec.md 和 Plans.md，包含范围、验收标准、依赖关系、未知因素和停止条件，非平凡计划还需通过团队验证模式。
- /harness-work 执行已批准的单个任务或范围，要求 TDD 测试驱动开发和验证步骤；/harness-review 将审查与实现分离，主要发现将作为阻塞项处理。
- /harness-release 在实现和审查完成后检查发布就绪状态、CHANGELOG 和标签边界，并封装验证后的证据。
- 不同 AI 编码工具对 Harness 的支持分为 supported、internal-compatible、candidate 和 future/unsupported
  四个等级，Claude Code v2.1+ 是官方支持路径。
- 现有用户在执行清理或重装前应先运行 bin/harness doctor --migration-report 命令，该命令会清查旧的插件缓存和状态而不删除任何数据。
extract_result: success
object_mentions:
- object_type: project
  name: Chachamaru127/claude-code-harness
  canonical_name: claude-code-harness
  url: https://github.com/Chachamaru127/claude-code-harness
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - claude-code-harness 是一个为 Claude Code 提供结构化交付循环的开源项目，通过 plan、work、review、sync、release
    五个核心命令将原始代理工作转化为可重复的操作路径。
  - 该项目通过 /plugin marketplace add Chachamaru127/claude-code-harness 等命令安装，安装后默认行为从"让代理编码"变为编写规范、实现切片、验证结果、独立审查、打包证据的流程。
  - 不同 AI 编码工具对 Harness 的支持等级不同，Claude Code 为官方支持级，Codex CLI 和 OpenCode 为内部兼容级。
  article_id: cea129f9b669edcc
impact_score:
  score: 4.5
  reason: 该工具针对 AI 编程智能体「工作漂移」这一真实痛点提出了结构化的 Plan-Work-Review-Ship 四阶段纪律循环方案，通过 MCP
    插件市场分发降低了安装门槛。但本质上是在 Claude Code 现有能力之上叠加流程约束层，而非底层能力突破；其影响力受限于 Claude Code 用户群，且开源
    MIT 协议意味着无直接商业杠杆。属于「解决真问题但圈子不大」的工具型发布，评分 4.5 反映其务实价值与有限辐射范围的平衡。
sentiment: positive
developer_sentiment:
  tone: skeptical
  primary_focus: 流程仪式感是否真正减少 agent 漂移还是增加了不必要的开发摩擦
hype_assessment:
  level: medium
  reason: README 使用了 'source-of-truth loop'、'disciplined delivery loop' 等包装性表述，但整体保持诚实——明确区分了
    supported/internal-compatible/candidate 三级支持状态，承认 'not_observed != absent'，且没有使用
    '颠覆'、'革命性' 等严重 PR 词汇。存在一定包装但核心功能描述具体可验证，属于中等水分。
information_entropy: high
domain_disruption:
  technical_innovation: 将软件工程中经典的 Plan-Do-Check-Act 循环固化为 Claude Code 的 MCP 插件命令集（/harness-plan
    → /harness-work → /harness-review → /harness-release），以 spec.md + Plans.md 作为合约文件实现意图与实施的分离，用
    Go 原生引擎做守卫而不依赖 Node.js 运行时，且将 TDD 和独立评审作为强制性门禁条件嵌入智能体工作流。
  business_model: 无直接商业模式——MIT 开源协议、通过 Claude 插件市场免费分发。其生态价值在于可能成为 AI 辅助开发的流程标准参考实现，间接推动
    Claude Code 企业级采纳。
engineering_complexity: prototype
compound_value:
  score: 5.0
  reason: 该工具解决了 AI 编码智能体"无纪律漂移"的真实痛点，Plan-Work-Review-Ship 四阶段门禁模型将软件工程纪律注入 Agent
    工作流，概念正确且实用。但长期复利效应受限：(1) 核心价值是流程模式而非专有技术，MIT 开源协议下任何人都可复制；(2) 严重依赖 Claude Code
    插件生态，平台风险集中——若 Anthropic 原生内置类似能力，Harness 的独立价值将大幅缩水；(3) 个人开发者维护的开源项目，缺乏商业化路径和持续投入保障；(4)
    MCP 插件分发降低了安装门槛但未构建数据网络效应或用户迁移成本。3-5 年后更可能被平台吸收为原生功能或被更成熟的竞品替代，难以独立成为行业基石。
value_capture_layer: agent_middleware
moat_impact: democratizes_access
key_beneficiaries:
- Anthropic
- 开源 AI 编码社区
- Go 生态工具链开发者
competitive_casualty:
- 依赖人力 Code Review 的传统研发流程工具
- 以"AI 结对编程"为卖点但缺乏结构化流程的轻量 AI 编码工具
market_opportunities:
- 开发者可基于 Harness 的 Plan-Work-Review-Ship 四阶段纪律循环模式，为企业内部 AI 编程助手定制合规工作流插件，满足金融、医疗等强监管行业的代码审计追溯需求
- MCP 插件市场中"AI Agent 流程治理"品类尚属蓝海，创业者可参考 Harness 的 spec.md/Plans.md 合约文件机制，打造覆盖更多 AI
  编程工具（Cursor、Copilot、Windsurf）的跨平台工作流治理产品
- 个人开发者应尽早掌握 /harness-plan → /harness-work → /harness-review 的结构化 AI 协作范式，这将是从"对话式编程"升级到"工程化
  AI 协作"的核心竞争力分水岭
risk_matrix:
  regulatory: 无
  technological: Claude Code 或 Anthropic 官方可能在未来版本中原生集成类似的结构化工作流能力，导致 Harness 作为第三方插件的存在价值被大幅削弱；此外，项目重度依赖
    Claude Code 的插件架构和 MCP 协议，若平台接口发生破坏性变更，工具将面临适配滞后风险
  competitive: AI 编程工作流治理赛道正快速拥挤——Codex CLI 自带类似规划能力、OpenCode 已实现内部兼容、Cursor 拥有 Rules
    体系、GitHub Copilot 也在扩展 Agent 模式，Harness 作为单人开源项目在生态位上面临巨头和已有工具的挤压
  ethical: 过度依赖 AI 编程工作流的"门禁式"约束可能导致开发者丧失独立判断能力，尤其是初级工程师可能将 spec.md 和 review 环节完全托管给
    AI，形成"流程合规但实质空洞"的虚假安全感；此外，TDD 强制要求若被机械执行，可能催生为满足门禁而编写的低质量测试
  additional:
  - 项目当前处于单人维护阶段，若作者精力不足或兴趣转移，工具将面临停更风险，已集成该工作流的团队需承担迁移成本
  - 跨工具兼容性声明（Codex、OpenCode）标记为 internal-compatible 或 candidate，实际体验可能与 Claude Code
    正式路径存在显著差距，多工具团队引入时需评估一致性风险
  - harness-mem 跨会话记忆功能若配置不当，可能在不经意间将项目敏感信息（设计决策、架构讨论）持久化到非预期的存储位置
confidence:
  impact: medium
  compound: low
  hype: medium
actionable_insight: monitor
object_insights:
- object_type: project
  name: Chachamaru127/claude-code-harness
  canonical_name: claude-code-harness
  url: https://github.com/Chachamaru127/claude-code-harness
  positioning: claude-code-harness 是一个为 Claude Code 提供结构化交付循环的开源插件，通过 Plan、Work、Review、Sync、Release
    五个核心命令将原始代理工作转化为可重复的操作路径。
  technical_signal: 项目通过五个核心命令将 Claude Code 的原始代理工作转化为可重复的操作路径，并生成 spec.md 和 Plans.md
    作为契约式事实来源。
  adoption_signal: Claude Code v2.1+ 是官方支持路径，Codex CLI 和 OpenCode 被列为内部兼容级，需通过独立安装脚本启用。
  ecosystem_relevance: 该项目填补了 Claude Code 缺乏结构化交付流程的空白，与多款 AI 编码工具生态形成互补关系，Codex CLI
    和 OpenCode 也提供兼容支持。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: claude-code-harness 解决了 AI 编码代理在真实交付中缺乏规范、审查滞后、证据缺失的核心痛点，其五步契约式工作流为
    AI 辅助开发提供了可审计、可重复的工程范式，值得跟踪其在更多编码工具生态中的落地进展。
  risk_notes:
  - 项目仍处于早期阶段，主流编码工具的兼容性尚不统一，Cursor 和 GitHub Copilot CLI 仅停留在 candidate 等级。
  - 用户需主动审批 spec.md 和 Plans.md 合同文件，额外的工作流认知负担可能影响开发者采用意愿。
  score: 7.0
  article_ids:
  - cea129f9b669edcc
  evidence_snippets:
  - claude-code-harness 是一个为 Claude Code 提供结构化交付循环的开源项目，通过 plan、work、review、sync、release
    五个核心命令将原始代理工作转化为可重复的操作路径。
  - 该项目通过 /plugin marketplace add Chachamaru127/claude-code-harness 等命令安装，安装后默认行为从"让代理编码"变为编写规范、实现切片、验证结果、独立审查、打包证据的流程。
  - 不同 AI 编码工具对 Harness 的支持等级不同，Claude Code 为官方支持级，Codex CLI 和 OpenCode 为内部兼容级。
---

**Plan. Work. Review. Ship.**

*A disciplined delivery loop for Claude Code, with bounded paths for Codex and OpenCode.*

English | 日本語

Claude Code is powerful, but raw agent work drifts: plans live in chat, tests become optional, review happens too late, and release evidence gets rebuilt by memory. Harness turns that into one repeatable operating path.

After install, the default changes from "ask the agent to code" to:

- write the spec and plan,
- implement only the approved slice,
- verify the result,
- review independently,
- package evidence for PR or release.

New users should start from the tool they already use. Existing users should run the migration report before cleanup or reinstall.

| Path | Start |
|---|---|
| New user | Tool-first onboarding |
| Existing user | Migration check |
| Claude Code fast path | Install in 30 seconds |
| Trigger proof | Skill trigger gate |

```
claude
/plugin marketplace add Chachamaru127/claude-code-harness
/plugin install claude-code-harness@claude-code-harness-marketplace
/harness-setup
```

Next command: run `/harness-plan`

with one small request.

`/harness-plan Improve the README onboarding flow`

- Install through your tool route.
- Run
`/harness-setup`

or the equivalent setup script. - Run
`/harness-plan`

with a small request; Harness writes the`spec.md`

and`Plans.md`

drafts for you to check. Small typo, docs, and status updates stay lightweight. - Approve the generated contract or reply with the correction you want.
- Run the smallest approved task, for example
`/harness-work 1.1.1`

. - Run
`/harness-review`

and keep the verification output.

Your job is not to hand-write the plan. It is to approve or correct the generated contract before execution continues.

Harness adds a source-of-truth loop around agent work. The 5 verb skills keep that surface small: plan, work, review, sync, release.

- You describe the outcome in normal language.
`/harness-plan`

drafts or updates`spec.md`

and`Plans.md`

with scope, acceptance criteria, unknowns, and stop conditions.- Non-trivial planning records
`team_validation_mode`

and validates the plan through team/sub-agent or manual-pass perspectives for spec/Plans alignment, memory reuse, product fit, security fit, and works-in-practice. - Harness treats those files as the source of truth. Data the agent has not
seen stays
`unknown`

instead of being silently invented. `/harness-work`

implements the approved slice with TDD and verification.`/harness-review`

separates review from implementation.`/harness-release`

packages only verified evidence.

| Command | What happens inside |
|---|---|
`/harness-setup` |
Installs project guidance, command surfaces, hooks, and checks so the workflow starts from one known baseline. |
`/harness-plan` |
Turns intent into `spec.md` and `Plans.md` , including scope, acceptance criteria, dependencies, unknowns, stop conditions, and non-trivial planning validation. |
`/harness-work` |
Executes one approved task or range, adds tests when required, runs verification, and keeps work inside the plan. |
`/harness-work all` |
Runs the approved plan through implementation and review paths; use after the plan is clear and the repo baseline is known. |
`/harness-review` |
Reviews the result separately from implementation and treats major findings as blockers. |
`/harness-release` |
Checks release readiness, CHANGELOG/tag boundaries, and evidence packaging after implementation and review are complete. |
`bin/harness doctor --migration-report` |
Inventories old plugin caches, Codex skills, OpenCode files, symlinks, and memory state without deleting data. |

| Stage | Output | Gate |
|---|---|---|
| Investigate | Evidence and unknowns | Do not promote unobserved data into claims. |
| Plan | `spec.md` + `Plans.md` |
User approves or corrects the generated contract. |
| Work | Code and tests | TDD required when the task says so. |
| Review | Independent verdict | Major findings block completion. |
| PR | Evidence pack | PR ready is not release ready. |
| Release | Tag/release artifacts | Release preflight must pass on the release path. |

| Tool | Tier | Route |
|---|---|---|
| Claude Code | `supported` |
Claude plugin marketplace, then `/harness-setup` . |
| Codex CLI | `internal-compatible` |
`scripts/setup-codex.sh --user` ; direct plugin smoke is tracked separately. |
| Codex app | `candidate` |
Candidate smoke only; do not reuse Codex CLI proof. |
| OpenCode | `internal-compatible` |
`scripts/setup-opencode.sh` ; runtime parity is not claimed. |
| Cursor | `candidate` |
PM handoff or adapter research only. |
| GitHub Copilot CLI | `candidate` |
Manual profile research only. |
| Antigravity CLI | `future/unsupported` |
No end-user install route in this phase. |

Run `bin/harness doctor --migration-report`

before changing an existing setup.
The report inventories stale Claude plugin caches, duplicate Codex skills, old
symlinks, OpenCode backup paths, and harness-mem state without deleting
anything.

Harness can describe candidate paths, but it does not inherit support claims from Superpowers, Hermes Agent, or any other project. A host only moves up when Harness has its own bootstrap, trigger, runtime, and release evidence.

`not_observed != absent`

: missing local proof means "not proven here", not
"impossible" and not "supported".

- Claude Code v2.1+ for the supported Claude path.
- A project repository with write access for local setup.
- No Node.js is required for the Go-native guardrail engine.
- Optional harness-mem for cross-session memory when configured and healthy.

Use these after the basic trigger path is visible.

| Capability | What it adds | Boundary |
|---|---|---|
| Breezing | Planner/Critic/Worker style team execution for larger task lists. | Still gated by plan quality and review. |
| Codex companion review | Schema-backed Codex second opinion through `scripts/codex-companion.sh` . |
Raw `codex exec` is not the Harness companion path. |
| OpenCode bootstrap | Mirrors Harness guidance into OpenCode-compatible surfaces. | Real runtime parity is not claimed. |
| harness-mem | Project-scoped memory and recall across sessions. | Optional companion; purge remains explicit. |

| Resource | Description |
|---|---|
| Tool-first onboarding | Where to start by host tool. |
| Install routes | Per-tool setup and support-tier boundaries. |
| Migration check | Existing-user impact, compatibility, and rollback path. |
| Skill trigger gate | How install success is verified. |
| Capability matrix | Supported, internal-compatible, candidate, and unsupported host claims. |
| Claude Code Compatibility | Current Claude Code requirements and compatibility notes. |
| Cursor Integration | Cursor handoff boundary and candidate-route notes. |
| Distribution Scope | Included vs compatibility vs development-only paths. |
| Hardening parity | Runtime safety differences between Claude hooks and Codex gates. |
| Work All Evidence Pack | Success/failure verification contract for full-plan execution. |
| Changelog | User-facing version history. |

Issues and PRs welcome. See CONTRIBUTING.md.

MIT License. See LICENSE.md.