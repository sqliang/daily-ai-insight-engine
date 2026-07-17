"use client";

import { useMemo } from "react";
import { useRouter, useSearchParams } from "next/navigation";
import type { EnrichedArticle, DateRange } from "@/lib/data/sources";
import { buildArticleDetailHref } from "@/lib/data/sources/article-route";
import { ArticleCard } from "./ArticleCard";

type SortMode = null | "impact";

type ArticleListProps = {
  articles: EnrichedArticle[];
  hasManifest: boolean;
  manifestFound: boolean;
  articleCount: number;
  sourceName: string;
  dateRange?: DateRange | null;
};

export function ArticleList({
  articles,
  hasManifest,
  manifestFound,
  articleCount,
  sourceName,
  dateRange,
}: ArticleListProps) {
  const router = useRouter();
  const searchParams = useSearchParams();
  const sortMode: SortMode = searchParams.get("sort") === "impact" ? "impact" : null;

  // 排序与分页均在服务端完成，articles 即为当前页的最终顺序，
  // 客户端不再二次排序（否则跨页的全局排序会被页内重排打乱）
  const isActive = sortMode === "impact";
  const detailSearchParams = useMemo(() => {
    const params = new URLSearchParams(searchParams.toString());
    if (sortMode === "impact") {
      params.set("sort", "impact");
    } else {
      params.delete("sort");
    }
    return params;
  }, [searchParams, sortMode]);

  function toggleSortMode() {
    const nextMode: SortMode = sortMode === "impact" ? null : "impact";
    const params = new URLSearchParams(searchParams.toString());
    if (nextMode === "impact") {
      params.set("sort", "impact");
    } else {
      params.delete("sort");
    }
    // 排序语义变化后原页码失去意义，重置回第 1 页
    params.delete("page");
    const qs = params.toString();
    router.push(qs ? `?${qs}` : window.location.pathname, { scroll: false });
  }

  return (
    <section id="article-list" className="mt-10 min-w-0 scroll-mt-20">
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
            {dateRange && (
              <span className="text-[11px] text-muted/50 font-mono">
                {dateRange.from === dateRange.to
                  ? dateRange.from
                  : `${dateRange.from ?? "..."} ~ ${dateRange.to ?? "..."}`}
              </span>
            )}
          </div>

          <button
            type="button"
            onClick={toggleSortMode}
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
          {articles.map((article) => (
            <ArticleCard
              key={article.id ?? article.url}
              article={article}
              detailHref={buildArticleDetailHref(sourceName, article, detailSearchParams)}
            />
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
