"use client";

// ============================================================================
// SourceCard.tsx — 数据源卡片
//
// 聚焦展示数据源的属性特征（类型、层级、语言、抓取策略、关键词），
// 不再展示文章篇数。始终可点击跳转到详情页。
// ============================================================================

import Link from "next/link";
import type { SourceStatus } from "@/lib/data/sources";
import {
  TIER_COLORS,
  TIER_SHORT_LABELS,
  SOURCE_TYPE_LABELS,
  LANGUAGE_LABELS,
} from "@/lib/data/tiers";

// ---------------------------------------------------------------------------
// Source type icon mapping
// ---------------------------------------------------------------------------

const TYPE_ICONS: Record<string, React.ReactNode> = {
  academic_paper: (
    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor"
      strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round">
      <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20" />
      <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z" />
    </svg>
  ),
  tech_blog: (
    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor"
      strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round">
      <polyline points="16 18 22 12 16 6" />
      <polyline points="8 6 2 12 8 18" />
    </svg>
  ),
  news_media: (
    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor"
      strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round">
      <path d="M4 11a9 9 0 0 1 9 9" />
      <path d="M4 4a16 16 0 0 1 16 16" />
      <circle cx="5" cy="19" r="1" />
    </svg>
  ),
  community_discussion: (
    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor"
      strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round">
      <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z" />
    </svg>
  ),
  newsletter_rss: (
    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor"
      strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round">
      <path d="M22 2L11 13" />
      <path d="M22 2l-7 20-4-9-9-4 20-7z" />
    </svg>
  ),
};

// ---------------------------------------------------------------------------
// Helpers
// ---------------------------------------------------------------------------

function extractDomain(url: string): string {
  try {
    return new URL(url).hostname.replace(/^www\./, "");
  } catch {
    return url;
  }
}

// ---------------------------------------------------------------------------
// SourceCard
// ---------------------------------------------------------------------------

type SourceCardProps = {
  source: SourceStatus;
};

export function SourceCard({ source }: SourceCardProps) {
  const color = TIER_COLORS[source.tier] ?? "var(--line)";
  const typeLabel = SOURCE_TYPE_LABELS[source.type] ?? source.type;
  const typeIcon = TYPE_ICONS[source.type] ?? null;
  const domain = extractDomain(source.url);
  const displayKeywords = source.keywords.slice(0, 6);
  const overflowCount = source.keywords.length - 6;

  return (
    <Link href={`/sources/${source.name}`} className="block group/card h-full">
      <article
        className="relative flex h-full rounded-xl border border-line/70 bg-panel
                   shadow-sm transition-all duration-300 ease-out overflow-hidden
                   group-hover/card:shadow-md group-hover/card:-translate-y-0.5
                   group-hover/card:border-foreground/20"
      >
        {/* Tier color accent bar (left side) */}
        <div
          className="shrink-0 w-1 rounded-l-xl transition-colors duration-300"
          style={{ backgroundColor: color }}
        />

        <div className="flex flex-col flex-1 p-5 min-w-0">
          {/* ---- Top: type icon + label ---- */}
          <div className="flex items-center gap-2 mb-3">
            {typeIcon && (
              <span className="text-foreground/50">{typeIcon}</span>
            )}
            <span className="text-[12px] font-semibold uppercase tracking-wider text-foreground/55">
              {typeLabel}
            </span>
          </div>

          {/* ---- Title ---- */}
          <div className="flex items-start justify-between gap-2">
            <h3 className="text-[17px] font-bold text-foreground tracking-tight leading-snug
                           group-hover/card:text-accent transition-colors duration-200">
              {source.display_name}
            </h3>
            <button
              onClick={(e) => {
                e.stopPropagation();
                e.preventDefault();
                window.open(source.url, "_blank", "noopener,noreferrer");
              }}
              className="shrink-0 text-foreground/25 hover:text-accent transition-colors
                         duration-200 mt-0.5 cursor-pointer"
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

          {/* ---- Meta tags: tier + language + strategy ---- */}
          <div className="mt-3 flex flex-wrap items-center gap-2">
            <span
              className="inline-flex items-center rounded-md px-2.5 py-0.5 text-[11px] font-semibold"
              style={{ backgroundColor: `${color}1a`, color }}
            >
              {TIER_SHORT_LABELS[source.tier] ?? source.tier}
            </span>
            <span className="inline-flex items-center rounded-md border border-line px-2.5 py-0.5 text-[11px] font-medium text-foreground/65">
              {LANGUAGE_LABELS[source.language] ?? source.language}
            </span>
            <span className="inline-flex items-center rounded-md border border-line/60 px-2.5 py-0.5 text-[11px] font-mono text-foreground/55">
              {source.fetch_strategy}
            </span>
          </div>

          {/* ---- Description ---- */}
          <p className="mt-3.5 text-[14px] leading-[1.7] text-foreground/78 line-clamp-3 flex-1">
            {source.display_description}
          </p>

          {/* ---- Keyword chips ---- */}
          {displayKeywords.length > 0 && (
            <div className="mt-3 flex flex-wrap gap-1.5">
              {displayKeywords.map((kw) => (
                <span
                  key={kw}
                  className="rounded-md border border-line bg-background px-2 py-0.5 text-[11px] font-mono font-medium text-foreground/65"
                >
                  {kw}
                </span>
              ))}
              {overflowCount > 0 && (
                <span className="rounded-md px-2 py-0.5 text-[11px] font-mono text-foreground/40">
                  +{overflowCount}
                </span>
              )}
            </div>
          )}

          {/* ---- Footer: domain ---- */}
          <div className="mt-3.5 flex items-center gap-1.5 text-[11px] text-foreground/45 font-mono">
            <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
              <circle cx="12" cy="12" r="10" />
              <line x1="2" y1="12" x2="22" y2="12" />
              <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z" />
            </svg>
            {domain}
          </div>
        </div>
      </article>
    </Link>
  );
}
