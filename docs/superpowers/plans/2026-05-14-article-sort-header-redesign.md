# Article List Sort & Header Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add client-side impact-score sort toggle button to the article list header, with a refreshed header row design.

**Architecture:** New `ArticleList` client component owns the header row + article loop + sorting state. The server component (`page.tsx`) passes articles as props and delegates all interactive behavior to the client component. No changes to data layer.

**Tech Stack:** Next.js 16 App Router, React 19, TypeScript, Tailwind CSS

---

### Task 1: Create ArticleList client component

**Files:**
- Create: `src/components/sources/ArticleList.tsx`

- [ ] **Step 1: Write the component**

```tsx
"use client";

import { useState, useMemo } from "react";
import type { EnrichedArticle } from "@/lib/data/sources";
import { ArticleCard } from "./ArticleCard";

type SortMode = null | "impact";

type ArticleListProps = {
  articles: EnrichedArticle[];
  hasManifest: boolean;
  manifestFound: boolean;
  articleCount: number;
};

function getImpactScore(article: EnrichedArticle): number {
  return (
    article.enriched?.impact_score?.score ??
    article.enriched?.compound_value?.score ??
    0
  );
}

export function ArticleList({
  articles,
  hasManifest,
  manifestFound,
  articleCount,
}: ArticleListProps) {
  const [sortMode, setSortMode] = useState<SortMode>(null);

  const sortedArticles = useMemo(() => {
    if (sortMode !== "impact") return articles;
    return [...articles].sort((a, b) => getImpactScore(b) - getImpactScore(a));
  }, [articles, sortMode]);

  const isActive = sortMode === "impact";

  return (
    <section className="mt-10 min-w-0">
      {/* Header row */}
      {hasManifest && (
        <div className="flex items-center justify-between pb-3.5 mb-6 border-b border-line">
          <div className="flex items-center gap-2.5">
            <svg
              width="16"
              height="16"
              viewBox="0 0 24 24"
              fill="none"
              stroke="var(--accent)"
              strokeWidth="2"
              strokeLinecap="round"
              strokeLinejoin="round"
            >
              <rect x="3" y="3" width="7" height="7" rx="1" />
              <rect x="14" y="3" width="7" height="7" rx="1" />
              <rect x="3" y="14" width="7" height="7" rx="1" />
              <rect x="14" y="14" width="7" height="7" rx="1" />
            </svg>
            <h2 className="text-[15px] font-bold text-foreground">
              文章列表
            </h2>
            <span
              className="text-[12px] font-semibold px-2 py-0.5 rounded-md"
              style={{
                color: "var(--accent)",
                backgroundColor: "color-mix(in oklch, var(--accent) 10%, transparent)",
              }}
            >
              {articleCount} 篇
            </span>
          </div>

          <button
            type="button"
            onClick={() => setSortMode((prev) => (prev ? null : "impact"))}
            className="inline-flex items-center gap-1.5 rounded-lg px-3 py-1.5 text-[12px] font-semibold
                       transition-all duration-200 shrink-0"
            style={
              isActive
                ? {
                    backgroundColor: "var(--accent)",
                    borderColor: "var(--accent)",
                    color: "white",
                    border: "1px solid var(--accent)",
                  }
                : {
                    backgroundColor: "transparent",
                    borderColor: "var(--line)",
                    color: "var(--muted)",
                    border: "1px solid var(--line)",
                  }
            }
          >
            {isActive ? (
              <svg
                width="12"
                height="12"
                viewBox="0 0 16 16"
                fill="none"
                stroke="currentColor"
                strokeWidth="1.5"
                strokeLinecap="round"
              >
                <path d="M16 3v10h-3M0 13l4-4 4 4" />
              </svg>
            ) : (
              <svg
                width="12"
                height="12"
                viewBox="0 0 16 16"
                fill="none"
                stroke="currentColor"
                strokeWidth="1.5"
                strokeLinecap="round"
              >
                <path d="M8 3v10M4 7l4-4 4 4" />
              </svg>
            )}
            影响力排序
          </button>
        </div>
      )}

      {/* Article cards */}
      {hasManifest ? (
        <div className="space-y-5">
          {sortedArticles.map((article, i) => (
            <ArticleCard key={i} article={article} />
          ))}
        </div>
      ) : (
        <div className="rounded-xl border border-line bg-panel/50 px-5 py-16 text-center">
          <p className="text-sm text-muted/35">
            {manifestFound
              ? "当前流水线运行无文章"
              : "暂无清单数据 — 等待流水线运行"}
          </p>
        </div>
      )}
    </section>
  );
}
```

### Task 2: Wire ArticleList into the source detail page

**Files:**
- Modify: `src/app/sources/[name]/page.tsx`

- [ ] **Step 1: Add import**

Replace the `ArticleCard` import (line 6):
```tsx
import { ArticleCard } from "@/components/sources/ArticleCard";
```
with:
```tsx
import { ArticleList } from "@/components/sources/ArticleList";
```

- [ ] **Step 2: Replace the article list section**

Remove lines 211-239:
```tsx
      {/* ====== Article list ====== */}
      <section className="mt-10 min-w-0">
        <div className="flex items-center justify-between mb-6">
          <h2 className="text-[15px] font-semibold text-foreground/80">
            文章列表
          </h2>
          {hasManifest && (
            <span className="text-[12px] text-muted/40">
              共 {source.articleCount} 篇
            </span>
          )}
        </div>

        {hasManifest ? (
          <div className="space-y-5">
            {source.articles.map((article, i) => (
              <ArticleCard key={i} article={article} />
            ))}
          </div>
        ) : (
          <div className="rounded-xl border border-line bg-panel/50 px-5 py-16 text-center">
            <p className="text-sm text-muted/35">
              {source.manifestFound
                ? "当前流水线运行无文章"
                : "暂无清单数据 — 等待流水线运行"}
            </p>
          </div>
        )}
      </section>
```

Replace with:
```tsx
      <ArticleList
        articles={source.articles}
        hasManifest={hasManifest}
        manifestFound={source.manifestFound}
        articleCount={source.articleCount}
      />
```

### Task 3: Verify build

**Files:** None (verification only)

- [ ] **Step 1: Run type check**

```bash
cd /Users/sqliang/ai-workspace/agent-workspace/daily-ai-insight-engine && pnpm typecheck
```

Expected: no errors.

- [ ] **Step 2: Run lint**

```bash
cd /Users/sqliang/ai-workspace/agent-workspace/daily-ai-insight-engine && pnpm lint
```

Expected: no errors (ignore pre-existing warnings).

- [ ] **Step 3: Start dev server and verify UI**

```bash
cd /Users/sqliang/ai-workspace/agent-workspace/daily-ai-insight-engine && pnpm dev
```

Open a source detail page (e.g., `http://localhost:3000/sources/anthropic`) and verify:
- Header row shows: grid icon + "文章列表" + count badge + sort button (outline, inactive)
- Click sort button → button turns accent-filled, articles reorder by impact score descending
- Click again → button returns to outline, articles return to original order
- Source without manifest shows empty state, no sort button

### Task 4: Commit

- [ ] **Step 1: Commit the changes**

```bash
cd /Users/sqliang/ai-workspace/agent-workspace/daily-ai-insight-engine && \
  git add src/components/sources/ArticleList.tsx src/app/sources/\[name\]/page.tsx && \
  git commit -m "$(cat <<'EOF'
feat(sources): add impact score sort toggle and refresh article list header

Client-side sort by impact_score desc, accent-style header with icon + count badge,
toggle button with active/inactive states. Pure presentation — no data changes.
EOF
)"
```
