# PR Body Template

Use this template when creating a pull request via `gh pr create`.

```markdown
## Summary
<1-2 sentences on what this does and why>

## Changes
- <bullet list of key changes>

## Verification
- ✅ <check 1>
- ✅ <check 2>
```

**Example:**

```markdown
## Summary
Fix loading skeleton placement and structure mismatches. Dashboard skeleton
moved to correct route segment with all 9 sections, skeleton widths now
match actual UI.

## Changes
- Move Dashboard skeleton to src/app/dashboard/loading.tsx
- Replace root loading.tsx with Sources skeleton (Hero + Tier + SourceCard)
- Add 5 missing Dashboard skeleton sections
- Fix 12 width/spacing mismatches across hero, KPI, and card skeletons
- Sync CLAUDE.md, README, and 3 design docs with route refactor

## Verification
- ✅ Root page shows Sources skeleton during loading
- ✅ /dashboard shows Dashboard skeleton with all 9 sections
- ✅ Skeleton widths match actual UI within 5%
- ✅ Documents synced with route changes
```

Always reference the issue with `Closes #N` so GitHub auto-links and auto-closes it when the PR merges.
