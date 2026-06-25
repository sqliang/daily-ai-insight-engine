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
tldr: 一个为 Claude Code 提供规范化 Plan-Work-Review-Ship 开发工作流的开源工具，通过 MCP 插件市场安装。
objective_summary: 开发者 Chachamaru127 发布了 claude-code-harness 开源项目（MIT 协议），为 Claude
  Code 等 AI 编程智能体引入结构化的五阶段交付循环：规划、实施、独立评审、同步与发布。用户通过 Claude 插件市场安装后，以 /harness-plan
event_type: framework_tools
epistemic_status: pr_statement
entities:
  companies: []
  technologies:
  - Claude Code
  - MCP
  - Go
  - Codex CLI
  - OpenCode
  key_people:
  - Chachamaru127
key_logic_flow:
- Harness 将 Claude Code 的原始智能体工作流升级为 Plan → Work → Review → Ship 的四阶段纪律循环，每个阶段有明确的输出物和门禁条件
- /harness-plan 命令将用户意图转化为 spec.md 和 Plans.md 两份合约文件，包含范围、验收标准、依赖项、未知因素和停止条件，用户只需批准或纠正即可
- /harness-work 执行已批准的任务切片，强制要求 TDD 和验证，确保实施不偏离计划边界
- /harness-review 将评审从实施中分离，重大发现被视作阻塞项而非可忽略建议
- 工具通过 Claude 插件市场分发（/plugin marketplace add），支持 Claude Code（正式支持）、Codex CLI 和 OpenCode（内部兼容）三条路径
- 提供 bin/harness doctor --migration-report 迁移检查命令，可盘点旧插件缓存和配置状态而不删除任何数据
extract_result: success
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