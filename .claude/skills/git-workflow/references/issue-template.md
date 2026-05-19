# Issue Body Template

Use this template when creating a GitHub issue via `gh issue create`.

```markdown
## Problem
<What's broken or missing? What triggered this task?>

## Scope
- <Bullet list of what needs to change>
- <Include specific files/components if known>

## Acceptance
- [ ] <Verifiable condition 1>
- [ ] <Verifiable condition 2>
```

**Example:**

```markdown
## Problem
Loading skeletons are placed at wrong route segments — root loading.tsx
shows Dashboard skeleton but root page is Sources. Dashboard skeleton is
missing 5 of 9 sections causing large layout shift.

## Scope
- Move Dashboard skeleton to src/app/dashboard/loading.tsx
- Replace root loading.tsx with Sources skeleton
- Add missing Dashboard skeleton sections (KPISection, DistributionSection, etc.)
- Fix width mismatches in skeleton placeholders

## Acceptance
- [ ] Root page shows Sources skeleton during loading
- [ ] /dashboard shows Dashboard skeleton with all 9 sections
- [ ] Skeleton widths match actual UI within 5%
```

```bash
gh issue create --title "<type>: <brief description>" --body "..."
```
