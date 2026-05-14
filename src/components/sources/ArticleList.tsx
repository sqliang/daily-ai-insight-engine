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
              aria-hidden="true"
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
                aria-hidden="true"
              >
                <path d="M14 3v10h-3M0 13l4-4 4 4" />
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
                aria-hidden="true"
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
          {sortedArticles.map((article) => (
            <ArticleCard key={article.id ?? article.url} article={article} />
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
