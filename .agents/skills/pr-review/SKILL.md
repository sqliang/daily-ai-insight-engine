---
name: pr-review
description: >
  Reviews GitHub Pull Requests across five dimensions: correctness, security, architecture,
  performance, and style. Use this skill whenever the user mentions PR review, pull request
  review, "review this PR", or wants structured feedback on a GitHub pull request.
  Posts findings as PR comments with severity ratings and a summary report.
---

# PR Review

## Workflow

1. Fetch the PR diff via `gh pr diff <PR_NUMBER>` (or `gh pr view <PR_NUMBER> --json body,comments` for metadata).
2. Read any files that are new or heavily modified to understand full context.
3. Analyze the diff across five dimensions. Read the relevant reference file for each dimension before reviewing.
4. Compile findings into the report template below.
5. Post each finding as a separate PR review comment via `gh pr review <PR_NUMBER> --comment -F <file>`, or post the full report as a single comment via `gh pr comment <PR_NUMBER> -F <file>`.

## Review Dimensions

Review across these five dimensions, in priority order:

| # | Dimension | Focus | Reference |
|---|-----------|-------|-----------|
| 1 | Correctness | Bugs, logic errors, edge cases, race conditions, error handling gaps | `references/correctness.md` |
| 2 | Security | Injection, auth, data exposure, dependency risks | `references/security.md` |
| 3 | Architecture | Design consistency, coupling, SOLID violations, anti-patterns | `references/architecture.md` |
| 4 | Performance | N+1 queries, blocking calls, memory leaks, inefficient patterns | `references/performance.md` |
| 5 | Style | Naming, comments, code organization, project conventions | `references/style.md` |

For each dimension, first read the reference file, then examine the diff through that lens.

## Severity Classification

Tag every finding with exactly one severity:

| Severity | Meaning | Examples |
|----------|---------|---------|
| `🔴 critical` | Must fix before merge — data loss, security breach, crash | SQL injection, unhandled exception crashing server, credential leak |
| `🟠 high` | Should fix before merge — broken functionality, significant risk | Logic error changing behavior, missing auth check, N+1 on hot path |
| `🟡 medium` | Fix in this PR or soon after — code quality, maintainability | Duplicated logic, misleading variable name, missing error handling |
| `🟢 low` | Nice to have, non-blocking — polish, minor improvements | Comment typo, slightly suboptimal pattern, missing docstring |
| `💡 suggestion` | Optional improvement idea, not a problem | Alternative approach worth considering, future optimization idea |

## Report Template

Generate the following markdown report. Replace `{PLACEHOLDER}` with actual content.

```markdown
## 🔍 PR Review: #{PR_NUMBER}

**Branch**: `{SOURCE_BRANCH}` → `{TARGET_BRANCH}`
**Files Changed**: {N} files
**Reviewed At**: {TIMESTAMP}

---

### 📊 Summary

| Dimension | 🔴 Critical | 🟠 High | 🟡 Medium | 🟢 Low | 💡 Suggestion |
|-----------|:-----------:|:--------:|:---------:|:------:|:-------------:|
| Correctness | {N} | {N} | {N} | {N} | {N} |
| Security | {N} | {N} | {N} | {N} | {N} |
| Architecture | {N} | {N} | {N} | {N} | {N} |
| Performance | {N} | {N} | {N} | {N} | {N} |
| Style | {N} | {N} | {N} | {N} | {N} |
| **Total** | **{N}** | **{N}** | **{N}** | **{N}** | **{N}** |

### 🚨 Must-Fix Before Merge

<!-- Only list 🔴 critical + 🟠 high findings here -->

{CRITICAL_AND_HIGH_FINDINGS}

---

### 📋 All Findings

{ALL_FINDINGS_GROUPED_BY_DIMENSION}

---

### ✅ Positives

<!-- What was done well — good patterns, clean code, smart solutions -->

{POSITIVES}
```

## Finding Format

Each individual finding must use this exact format:

```markdown
### [{SEVERITY_LABEL}] {DIMENSION}: {ONE_LINE_SUMMARY}

**File**: `{FILE_PATH}:{LINE}`
**Why**: {1-2 sentences explaining why this matters}
**Fix**: {Specific fix suggestion}

<!-- optional: code diff showing the fix -->
\`\`\`diff
- old code
+ new code
\`\`\`
```

## Posting Strategy

1. Post findings with `🔴 critical` or `🟠 high` severity as **individual PR review comments** on the relevant line via `gh pr review {NUMBER} --comment -F -` with inline diff suggestions.
2. Post the full report (all findings) as a **single PR comment** via `gh pr comment {NUMBER} --body-file <report.md>`.
3. If there are zero critical + high findings, start the PR review with a ✅ approval.

## Before Starting

- Verify `gh` CLI is authenticated and the repo is correct.
- Confirm the PR number with the user if not explicitly provided.
- If the diff is very large (>50 files), ask the user if they want a focused review on specific paths.
