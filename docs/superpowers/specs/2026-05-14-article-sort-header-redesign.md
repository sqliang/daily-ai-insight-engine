# Article List Sort & Header Redesign

**Date:** 2026-05-14
**Status:** approved

## Summary

Add client-side impact-score sorting to the source detail page article list, and redesign the article list header area with improved visual hierarchy. Sorting is pure presentation logic — it does not touch the `data/` directory or any data-fetching code.

## Scope

- `src/app/sources/[name]/page.tsx` — replace inline `<section>` (L212-L239) with `<ArticleList>` component
- `src/components/sources/ArticleList.tsx` — new client component (header row + article cards)
- No changes to `ArticleCard`, data layer, or manifest files

## Component Design

### ArticleList (`src/components/sources/ArticleList.tsx`)

New client component (`"use client"`) that owns the article list section.

**Props:**

| Prop | Type | Description |
|------|------|-------------|
| `articles` | `EnrichedArticle[]` | All articles for the current source |
| `hasManifest` | `boolean` | Whether a manifest was found |
| `articleCount` | `number` | Total article count |

**State:**

```
sortMode: null | 'impact'   // null = default order, 'impact' = sorted by impact score desc
```

**Renders:**

1. Header row — grid icon + "文章列表" title + count badge + sort toggle button
2. Article cards — `space-y-5` loop of `<ArticleCard>` with the (possibly sorted) articles
3. Empty state — when `hasManifest` is false, show existing empty-state UI

### Header row details

**Layout:** single flex row, `justify-between`, with a thin bottom border (`border-b border-line`)

**Left side:**
- Grid icon (`var(--accent)` color, 16×16 SVG)
- "文章列表" text (15px, bold)
- Count badge: accent-tinted chip showing `N 篇` (12px, accent color on accent/0.1 background, rounded-lg)

**Right side:**
- Sort toggle button

**Sort button states:**

| State | Background | Border | Text color | Icon |
|-------|-----------|--------|------------|------|
| Inactive (sortMode = null) | transparent | `1px solid var(--line)` | `var(--muted)` | up-arrow |
| Active (sortMode = 'impact') | `var(--accent)` solid | `1px solid var(--accent)` | white | down-arrow |

Text: "影响力排序" (both states). Width: fixed with transition.

### Sorting logic

```ts
function getImpactScore(article: EnrichedArticle): number {
  return article.enriched?.impact_score?.score
    ?? article.enriched?.compound_value?.score
    ?? 0;
}
```

- `sortMode === null`: render articles in original manifest order
- `sortMode === 'impact'`: sort descending by `getImpactScore()`, articles with score 0 sort to bottom
- Sort is a derived value from state — no state mutation of `articles` prop
- Clicking the button toggles between `null` and `'impact'`

### Modified: source detail page

Change in `src/app/sources/[name]/page.tsx`:

**Remove:** the `<section>` block at L212-L239 containing the inline header and article loop.

**Replace with:**
```tsx
<ArticleList
  articles={source.articles}
  hasManifest={hasManifest}
  articleCount={source.articleCount}
/>
```

Import added: `import { ArticleList } from "@/components/sources/ArticleList";`

The hero banner (`<header>`) and all metadata above the article list remain unchanged.

## What does NOT change

- `ArticleCard` — zero modifications
- `src/lib/data/sources.ts` — zero modifications
- `src/lib/data/status.ts` — zero modifications
- `src/lib/data/files.ts` — zero modifications
- `data/` directory — zero impact
- No URL search params, no server-side sorting

## Edge cases

- **All articles are "scout" status** (no enriched data): all get score 0, sorted order remains same as original
- **No manifest found**: `hasManifest=false`, empty-state message shown, sort button not rendered
- **Single article**: sort toggle still works but has no visible reordering effect
- **Toggle off**: returns to exact original manifest order (stable identity, no data mutation)
