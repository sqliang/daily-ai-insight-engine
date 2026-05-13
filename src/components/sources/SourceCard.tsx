"use client";

import Link from "next/link";
import type { SourceStatus } from "@/lib/data/sources";
import {
  TIER_COLORS,
  TIER_SHORT_LABELS,
  SOURCE_TYPE_LABELS,
  LANGUAGE_LABELS,
} from "@/lib/data/tiers";

type SourceCardProps = {
  source: SourceStatus;
};

export function SourceCard({ source }: SourceCardProps) {
  const color = TIER_COLORS[source.tier] ?? "var(--line)";
  const hasArticles = source.manifestFound && source.articleCount > 0;
  const displayKeywords = source.keywords.slice(0, 5);
  const overflowCount = source.keywords.length - 5;

  const cardContent = (
    <article
      className="relative rounded-xl border border-line bg-panel/90 backdrop-blur-sm shadow-sm
                 transition-all duration-300 ease-out
                 group-hover/card:shadow-lg group-hover/card:-translate-y-1
                 group-hover/card:border-accent/20"
      style={{ borderTopColor: color, borderTopWidth: 3 }}
    >
      {/* Gradient overlay on hover — only when clickable */}
      {hasArticles && (
        <div
          className="absolute inset-0 rounded-xl opacity-0 group-hover/card:opacity-100 transition-opacity duration-300 pointer-events-none"
          style={{
            background: `linear-gradient(180deg, ${color}08 0%, transparent 60%)`,
          }}
        />
      )}

      <div className="relative p-5">
        {/* Title row */}
        <div className="flex items-start justify-between gap-3">
          <h3
            className={[
              "text-lg font-bold text-foreground tracking-tight leading-snug",
              hasArticles && "group-hover/card:text-accent transition-colors duration-200",
            ].join(" ")}
          >
            {source.display_name}
          </h3>
          <button
            onClick={(e) => {
              e.stopPropagation();
              e.preventDefault();
              window.open(source.url, "_blank", "noopener,noreferrer");
            }}
            className="shrink-0 text-muted/20 hover:text-accent transition-colors duration-200 mt-0.5 cursor-pointer"
            title="访问源站"
            type="button"
          >
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8">
              <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6" strokeLinecap="round" strokeLinejoin="round" />
              <polyline points="15 3 21 3 21 9" strokeLinecap="round" strokeLinejoin="round" />
              <line x1="10" y1="14" x2="21" y2="3" strokeLinecap="round" strokeLinejoin="round" />
            </svg>
          </button>
        </div>

        {/* Tag row */}
        <div className="mt-3 flex flex-wrap items-center gap-2">
          <span
            className="inline-flex items-center rounded-full px-2.5 py-0.5 text-xs font-semibold"
            style={{ backgroundColor: `${color}18`, color }}
          >
            {TIER_SHORT_LABELS[source.tier] ?? source.tier}
          </span>
          <span className="inline-flex items-center rounded-full border border-line px-2.5 py-0.5 text-xs font-medium text-muted/80">
            {SOURCE_TYPE_LABELS[source.type] ?? source.type}
          </span>
          <span className="inline-flex items-center rounded-full border border-line px-2.5 py-0.5 text-xs font-medium text-muted/80">
            {LANGUAGE_LABELS[source.language] ?? source.language}
          </span>
          {hasArticles && (
            <span
              className="inline-flex shrink-0 items-center rounded-full px-2.5 py-0.5 text-xs font-semibold ml-auto"
              style={{ backgroundColor: `${color}14`, color }}
            >
              {source.articleCount} 篇
            </span>
          )}
        </div>

        {/* Description */}
        <p className="mt-3 text-sm leading-relaxed text-muted/80 line-clamp-3">
          {source.display_description}
        </p>

        {/* Keyword chips */}
        {displayKeywords.length > 0 && (
          <div className="mt-2.5 flex flex-wrap gap-1">
            {displayKeywords.map((kw) => (
              <span
                key={kw}
                className="rounded bg-surface px-1.5 py-0.5 text-[10px] font-mono text-muted/35"
              >
                {kw}
              </span>
            ))}
            {overflowCount > 0 && (
              <span className="rounded bg-surface px-1.5 py-0.5 text-[10px] font-mono text-muted/25">
                +{overflowCount}
              </span>
            )}
          </div>
        )}

        {/* Footer */}
        <div className="mt-4 flex items-center justify-between border-t border-line/40 pt-3">
          <span className="text-[11px] text-muted/45">
            {hasArticles
              ? `${source.articleCount} 篇文章`
              : source.manifestFound
                ? "暂无文章"
                : "等待运行"}
          </span>
          <span className="text-[10px] font-mono text-muted/30">
            {source.fetch_strategy}
          </span>
        </div>
      </div>
    </article>
  );

  if (!hasArticles) {
    return <div className="block opacity-70">{cardContent}</div>;
  }

  return (
    <Link href={`/sources/${source.name}`} className="block group/card">
      {cardContent}
    </Link>
  );
}
