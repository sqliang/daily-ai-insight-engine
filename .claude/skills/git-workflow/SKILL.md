---
name: git-workflow
description: >
  Full-cycle Git workflow for feature branches, conventional commits, rebase sync, and PR creation.
  Use when the user asks you to execute git actions — commit code, push, create/update pull requests,
  start a new branch, rebase, or amend commits. Trigger on phrases like "commit this", "push my changes",
  "create a PR", "提交代码", "推送", "amend commit", "更新PR". Do NOT use for code review, explaining
  git concepts, viewing git history, deploying applications, security audits, or non-git operations
  like database transactions.
allowed-tools:
  - Bash(git:*)
  - Bash(gh:*)
license: MIT
metadata:
  author: sqliang
  version: "1.4.1"
---

# Git Workflow

An expert workflow guide for Git operations that maintains a clean, linear project history. Covers branch management, stash handling, commit conventions, synchronization, conflict resolution, push safety, and PR workflows.

## When to Apply

Invoke this skill whenever the user wants to:
- Create a new feature/fix/chore branch
- Stage and commit changes (any phrasing: "commit this", "提交代码", "make a commit")
- Push changes to remote or create a pull request
- Sync or rebase their branch
- Resolve conflicts during rebase
- Update code after a code review
- Any git-related task not covered by another skill

## 0. Pre-Action Safety Gate — READ THIS FIRST

**Before ANY commit, push, or destructive operation, you MUST check the current branch:**

```bash
git branch --show-current
```

### If current branch is `main` or `master` and the user asks to commit:

**STOP. Do NOT commit on main.** The user may not realize they're on main, or may be new to git. Committing on main pollutes the trunk and makes it impossible to create a clean PR later. Explain clearly:

> "We're currently on `main`. Changes should go through a feature branch and PR to keep the trunk clean. Let me move everything to a new branch first."

Then immediately follow the **Full Branch Creation Flow** (Section 1) to stash changes, create a branch, and pop the stash. Only after the branch is ready, proceed with the commit (Section 2).

**User insists on committing to main after warning:** warn once more that this bypasses review, then follow their instruction. User intent overrides skill rules.

### If current branch is `main` or `master` and the user asks to push:

**REFUSE.** This is non-negotiable. Pushing directly to main skips code review, CI checks, and branch protection — it can break production for the entire team. Respond:

> "I won't push directly to `main`. That branch is protected — all changes must go through pull requests. If you need to get changes onto main, let me create a PR from a feature branch."

There is no exception. If commits were already made on main by mistake, follow the recovery flow (Section 8).

### If already on a feature branch:

Proceed normally. The safety gate is satisfied.

## Core Principles

- **Clean Trunk**: Never work directly on the main branch. Changes always go through feature branches and PRs.
- **Feature Branches**: Each task gets its own branch. No exceptions — even "small fixes" deserve a branch.
- **Conventional Commits**: All commit messages follow the Conventional Commits specification.
- **Linear History**: Use rebase, never merge commits. `git pull --rebase` is the default sync method.
- **Push Safety**: Run local build, type-check, and tests before pushing. Never force-push to main.
- **Specific Staging**: Stage files by name (`git add <file> <file>`), never use `git add .` or `git add -A`. This prevents accidentally staging secrets, large binaries, or unrelated changes.
- **Local Checks First**: GitHub CI is the safety net, not the primary validation. Pre-commit hooks and explicit local verification must pass before any push or PR creation.

## 1. Branch Management & Stash Workflow

### Branch Naming

| Prefix | Use for |
|--------|---------|
| `feature/` | New features |
| `fix/` | Bug fixes |
| `chore/` | Maintenance tasks (cleanup, dependency updates, skill changes) |
| `docs/` | Documentation-only changes |
| `hotfix/` | Urgent production fixes |
| `release/` | Release branches |

Keep names descriptive and kebab-case: `fix/loading-skeleton-mismatch`, `chore/remove-unused-skill`.

### Full Branch Creation Flow

When the user has uncommitted changes on main (or any branch) and wants to start a new task:

**Step 1: Stash current changes**
```bash
git stash push -u -m "<brief description of what's being stashed>"
```
The `-u` flag includes untracked files (new files that haven't been staged yet). Without it, new files stay in the working tree and can cause confusion.

**Step 2: Sync the base branch**
```bash
git checkout main
git fetch origin main
git pull --rebase origin main
```

**Step 3: Create the new branch**
```bash
git checkout -b <prefix>/<descriptive-name>
```

**Step 4: Restore stashed changes**
```bash
git stash pop
```
If `git stash pop` results in conflicts (because the same file was modified both in the stash and on the new branch), resolve the conflicts manually, then:
```bash
git add <resolved-files>
git stash drop   # clean up the stash after successful pop with conflicts
```

**Step 5: Verify working tree**
```bash
git status
```
Carefully review the output. `git stash pop` can surface changes from linters or pre-existing modifications unrelated to the current task. If you see unexpected modified files, restore them with:
```bash
git restore <unwanted-file-1> <unwanted-file-2>
```
Only the files relevant to the current task should remain modified. If untracked files from a previous session appear (like `.claude/skills/` directories), leave them alone — they're not part of the commit.

If the working tree is already clean (no uncommitted changes), skip steps 1, 4, and 5.

## 2. Commit Generation Rules

### Staging Files

**Always stage files by name** — never use `git add .` or `git add -A`. This is a project-level requirement (per CLAUDE.md) because bulk-staging can accidentally include secrets (`.env`), large binaries, or unrelated changes.

```bash
# Correct: list every file explicitly
git add src/app/loading.tsx src/components/sources/SourceCardSkeleton.tsx ...

# Wrong:
git add .
git add -A
```

Use `git status --short` to see what needs staging, then add files selectively.

### Commit Message Format

Follow the Conventional Commits specification:

```
<type>(<scope>): <imperative-description>

[body explaining why and what changed]

[footer: Closes #N or Refs #N]
```

**Types:**
| Type | Use for |
|------|---------|
| `feat` | New feature |
| `fix` | Bug fix |
| `docs` | Documentation only |
| `style` | Formatting (no code change) |
| `refactor` | Code change that neither fixes a bug nor adds a feature |
| `test` | Adding or updating tests |
| `chore` | Maintenance tasks (dependency updates, cleanup, skill changes) |

**Body**: Describe the "why" and summarize the "what". Use bullet points for multi-part changes. Keep it concise — the diff shows the details.

**Footer**: Reference related issues with `Closes #N` or `Refs #N`.

**Example:**
```
fix(loading): correct skeleton placement, add missing sections, sync docs with route refactor

Move Dashboard skeleton to dashboard/loading.tsx, replace root loading.tsx
with Sources skeleton, delete dead sources/loading.tsx. Add 5 missing
Dashboard skeleton sections. Fix width mismatches in hero, KPI, and card
skeletons. Sync CLAUDE.md, README, and design docs with route refactor.

Closes #1
```

### Pre-commit Validation

Before committing, verify these in order. If any check fails, stop and fix before proceeding:

1. **Branch check**: Run `git branch --show-current`. If the result is `main` or `master`, STOP — return to Section 0 and follow the branch creation flow. Never skip this check, even if the user says "just commit it quickly."
2. **Staging check**: Are only intended files staged? Run `git diff --cached --stat` to verify. Never commit secrets (`.env`, credentials), large binaries, or unrelated changes.
3. **Type check**: Does the commit type match the actual changes? (`feat` for features, `fix` for bugs, `chore` for maintenance, etc.)
4. **Message check**: Is the description in imperative mood ("add" not "added", "fix" not "fixed")?

If the project has pre-commit hooks (e.g., husky), they will run automatically. Do not bypass them with `--no-verify` unless the failure is unrelated to your changes and you have explicitly informed the user.

## 3. Synchronization & Conflict Resolution

**Rule**: Always use rebase, never merge.

### Sync with remote (same branch)
```bash
git fetch origin
git pull --rebase origin <current-branch>
```

### Rebase onto latest main
When main has moved ahead and you need to bring your feature branch up to date:
```bash
git fetch origin
git rebase origin/main
```

### Conflict Resolution
If conflicts occur:
1. Resolve conflicts in the listed files, then run `git add <file> && git rebase --continue`
2. If conflicts are too complex and you want to back out:
   ```bash
   git rebase --abort
   ```
   This returns your branch to its pre-rebase state — nothing is lost.
3. After a successful rebase: run the project's build and type-check to ensure nothing broke
4. Notify the user about any surprising changes

## 4. Push Safety Protocol

### Mandatory Pre-Push Gate

**Before any push, check the target branch:**

1. Run `git branch --show-current` to see your current branch.
2. If the result is `main` or `master`: **REFUSE TO PUSH.** The response is always:

   > "I won't push directly to `main`. Pushing to main bypasses code review and can break production. Changes on main must go through a PR from a feature branch."

   If commits were already made on main by mistake, follow Section 8 (Recovery) to migrate them to a feature branch, then push that branch instead.

3. If on a feature branch: proceed with the checks below.

### Before Pushing
1. Run the project's full local check commands (check CLAUDE.md for the exact commands — typically `pnpm typecheck && pnpm build && uv run python -m pytest tests/`)
2. Verify all checks pass
3. Do a final `git status --short` to confirm:
   - The right changes are committed
   - No intended new files are left untracked (`??`)
   - No unexpected modified files remain unstaged
4. If pre-push hooks are configured, they will run automatically. Do not bypass them.

### First Push (new branch)
```bash
git push --set-upstream origin <current-branch-name>
```
The `--set-upstream` flag links the local branch to the remote tracking branch.

### Subsequent Pushes
```bash
git push origin <current-branch-name>
```

### If Push Is Rejected (non-force)
Someone else pushed to the same branch. Recover by rebasing your changes on top:
```bash
git fetch origin
git pull --rebase origin <current-branch-name>
git push origin <current-branch-name>
```

### After Rebase (history rewritten)
```bash
git push --force-with-lease origin <current-branch-name>
```
`--force-with-lease` is the safe force-push: it will refuse if someone else pushed to the same branch. **Never use raw `--force`.**

## 4.5 Local Verification & CI Gate

Local verification is the first line of defense; CI is the second. The project should have:

- **Pre-commit hook** (e.g., husky): runs `pnpm typecheck` against staged files, catching missing imports and type errors before the commit is even created.
- **Pre-push hook** (e.g., husky): runs the full local check suite (`pnpm typecheck && pnpm build && uv run python -m pytest tests/`) before allowing a push.
- **GitHub Actions CI**: runs the same checks in a clean environment on every PR and push to `main`.

When using this skill, assume these hooks exist. If a hook fails:
1. Fix the underlying issue — do not bypass with `--no-verify` or `--force`.
2. Re-stage affected files and re-commit.
3. Re-run the failing check locally to confirm it passes before pushing again.

If the project does not yet have hooks configured and you are creating a PR, manually run the full check suite before `gh pr create`.

## 5. Post-Review Commit Hygiene

When updating code after a code review, avoid creating "fix review" or "address comments" commits. Amend the existing commit instead:

```bash
git add <specific-file-1> <specific-file-2>
git commit --amend --no-edit
git push --force-with-lease origin <current-branch>
```

If the commit message also needs updating, use `git commit --amend` (without `--no-edit`).

## 6. Issue-Driven Workflow

The full end-to-end flow for a task:

### 1. Create an Issue
Label it appropriately. The issue captures the problem and context before any code is written.

Use the issue body template from `references/issue-template.md`.

```bash
# 同样使用 body-file 避免 \\n 转义问题
cat > /tmp/issue-body.md << 'EOF'
## Problem
<清晰描述问题或需求>

## Acceptance Criteria
- [ ] <验收标准 1>
- [ ] <验收标准 2>
EOF

gh issue create --title "<type>: <brief description>" --body-file /tmp/issue-body.md
```

### 2. Create a Branch
Follow Section 1 (branch from main, stash if needed). Name the branch to match the issue type.

### 3. Make Changes & Commit
Follow Section 2. Reference the issue in the commit footer:
```
Closes #3
```

### 4. Push & Create a PR

Before creating the PR, ensure all local checks have passed:

```bash
pnpm typecheck
pnpm build
uv run python -m pytest tests/
```

Then push and create the PR. **Always use `--body-file` instead of inline `--body`** — inline shell strings preserve literal `\n` characters, which render as broken newlines on GitHub.

```bash
git push --set-upstream origin <branch-name>

# 1. 按 references/pr-template.md 填充 PR 正文，保存为文件
cat > /tmp/pr-body.md << 'EOF'
## Summary
<1-2 sentences on what this does and why>

## Changes
- <bullet list of key changes>

## Verification
- ✅ <check 1>
- ✅ <check 2>
EOF

# 2. 创建 PR
gh pr create --title "<type>(<scope>): <description>" --body-file /tmp/pr-body.md
```

Use the PR body template from `references/pr-template.md` exactly — do not use a different format even if the repository has a `.github/PULL_REQUEST_TEMPLATE.md`. Reference the issue with `Closes #N` — GitHub will auto-link and auto-close the issue when the PR merges.

After creating the PR, verify two things:

1. **Rendered body**: run `gh pr view <number> --json body` and confirm the JSON contains real newlines (`\n`) rather than escaped `\\n`. If you see `\\n`, the body was passed incorrectly — edit it with `gh pr edit <number> --body-file /tmp/pr-body.md`.
2. **CI checks**: confirm GitHub Actions + Vercel all pass. If any fail, fix locally and push again.

## 7. Code Review Best Practices

For code review guidelines, read `references/code-review.md`. This covers PR requirements, review process, and what to look for.

## 8. Recovery: Fixing Main-Branch Mistakes

If commits were accidentally made on `main` (either in this session or a previous one), do NOT push them. Recover with one of the following flows.

### Case A: Commits on main, NOT pushed to remote

Move the commits to a feature branch and rewind main:

```bash
# 1. Create a feature branch at the current position (captures the commits)
git branch feature/recover-<description>

# 2. Rewind main to match the remote (removes commits from main)
git reset --hard origin/main

# 3. Switch to the feature branch
git checkout feature/recover-<description>

# 4. Verify the commits are now on the feature branch
git log --oneline -5

# 5. Continue with normal workflow — commit more, push, create PR
```

### Case B: Commits on main, ALREADY pushed to remote

This is more serious — the commits are visible to the team. Options in order of preference:

**Option 1: Revert (safest for shared branches)**
```bash
git revert HEAD~<N>..HEAD --no-edit  # revert the last N commits
git push origin main
```
Then create a feature branch and re-apply the changes properly.

**Option 2: Force push (only if you're SURE no one else has pulled)**
```bash
git reset --hard HEAD~<N>             # remove the last N commits locally
git push --force-with-lease origin main
```
**Warn the user about the risks before force-pushing to main.**

### Prevention

The safety gates in Section 0, Section 2, and Section 4 exist to prevent this situation entirely. If you're reading Section 8 because those gates failed, the gates need to be stronger — consider updating this skill.
