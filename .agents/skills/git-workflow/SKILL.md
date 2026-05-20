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
  version: "1.2.1"
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

## Core Principles

- **Clean Trunk**: Never work directly on the main branch. All changes go through feature branches.
- **Feature Branches**: Each task gets its own branch.
- **Conventional Commits**: All commit messages follow the Conventional Commits specification.
- **Linear History**: Use rebase, never merge commits. `git pull --rebase` is the default sync method.
- **Push Safety**: Run local build and type-check before pushing. Never force-push to main.
- **Specific Staging**: Stage files by name (`git add <file> <file>`), never use `git add .` or `git add -A`. This prevents accidentally staging secrets, large binaries, or unrelated changes.

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

Before committing, verify:
1. Does the type match the actual changes?
2. Is the description in imperative mood ("add" not "added", "fix" not "fixed")?
3. Are only intended files staged? Check with `git diff --cached --stat`.

If the project has commitlint hooks configured, they will auto-validate on commit.

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

### Before Pushing
1. Run the project's build and type-check commands (check CLAUDE.md for the exact commands — e.g., `pnpm typecheck && pnpm build`)
2. Verify all checks pass
3. Do a final `git status` to confirm the right changes are staged

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

### Never Push To
- `main` or `master` directly — always use a PR.

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
gh issue create --title "<type>: <brief description>" --body "..."
```

### 2. Create a Branch
Follow Section 1 (branch from main, stash if needed). Name the branch to match the issue type.

### 3. Make Changes & Commit
Follow Section 2. Reference the issue in the commit footer:
```
Closes #3
```

### 4. Push & Create a PR
```bash
git push --set-upstream origin <branch-name>
gh pr create --title "<type>(<scope>): <description>" --body "<PR body>"
```

Use the PR body template from `references/pr-template.md`. Reference the issue with `Closes #N` — GitHub will auto-link and auto-close the issue when the PR merges.

## 7. Code Review Best Practices

For code review guidelines, read `references/code-review.md`. This covers PR requirements, review process, and what to look for.
