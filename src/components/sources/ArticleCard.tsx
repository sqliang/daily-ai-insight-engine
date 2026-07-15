"use client";

// ============================================================================
// ArticleCard.tsx — 数据源文章索引卡片
//
// 在 SourceDetailPage 的文章列表中渲染精简摘要卡片。
// 主点击进入站内文章详情页，原文链接作为次要操作保留。
// ============================================================================

import Link from "next/link";
import type { EnrichedArticle } from "@/lib/data/sources";
import {
  ACTIONABLE_INSIGHT_LABELS,
  EVENT_TYPE_LABELS,
} from "@/lib/data/status";
import { StatusBadge } from "./StatusBadge";
import { SentimentIndicator } from "./SentimentIndicator";

type ArticleCardProps = {
  article: EnrichedArticle;
  detailHref: string;
};

function getDomain(url: string): string {
  try {
    return new URL(url).hostname.replace(/^www\./, "");
  } catch {
    return url;
  }
}

function getImpactColor(enriched: EnrichedArticle["enriched"]): string {
  const score = enriched?.impact_score?.score ?? enriched?.compound_value?.score;
  if (score === undefined) return "var(--line)";
  if (score >= 7) return "var(--cool)";
  if (score >= 4) return "var(--warm)";
  return "var(--muted)";
}

function MetricPill({ article }: { article: EnrichedArticle }) {
  const { enriched } = article;
  const score = enriched?.impact_score?.score ?? enriched?.compound_value?.score;
  if (score === undefined) {
    return (
      <span className="rounded-lg border border-line/50 px-3 py-1.5 font-mono text-[12px] font-semibold text-muted/35">
        no score
      </span>
    );
  }

  const color = getImpactColor(enriched);
  return (
    <span
      className="inline-flex min-w-16 items-center justify-center rounded-xl px-3 py-2 font-mono text-[17px] font-bold tabular-nums"
      style={{
        backgroundColor: `${color} / 0.08`,
        color,
        boxShadow: `inset 0 0 0 1px ${color} / 0.14`,
      }}
      title="影响力评分"
    >
      {score.toFixed(1)}
    </span>
  );
}

function SecondaryTags({ article }: { article: EnrichedArticle }) {
  const { enriched } = article;
  const eventType = enriched?.event_type;
  const actionableInsight = enriched?.actionable_insight;

  return (
    <div className="flex flex-wrap items-center gap-2">
      {eventType && eventType in EVENT_TYPE_LABELS && (
        <span
          className="inline-flex items-center gap-1.5 rounded-full px-3 py-1 text-[12px] font-semibold"
          style={{
            backgroundColor: `${EVENT_TYPE_LABELS[eventType].color} / 0.08`,
            color: EVENT_TYPE_LABELS[eventType].color,
          }}
        >
          <span
            className="h-1.5 w-1.5 rounded-full"
            style={{ backgroundColor: EVENT_TYPE_LABELS[eventType].color }}
          />
          {EVENT_TYPE_LABELS[eventType].label}
        </span>
      )}
      {actionableInsight && actionableInsight in ACTIONABLE_INSIGHT_LABELS && (
        <span
          className="inline-flex items-center gap-1.5 rounded-full px-3 py-1 text-[12px] font-bold"
          style={{
            backgroundColor: `${ACTIONABLE_INSIGHT_LABELS[actionableInsight].color} / 0.08`,
            color: ACTIONABLE_INSIGHT_LABELS[actionableInsight].color,
          }}
        >
          ◆ {ACTIONABLE_INSIGHT_LABELS[actionableInsight].label}
        </span>
      )}
      {enriched?.sentiment && <SentimentIndicator sentiment={enriched.sentiment} />}
    </div>
  );
}

/**
 * 数据源文章索引卡片。
 *
 * 保持列表扫描效率：仅展示标题、摘要和少量核心指标；完整指标进入详情页查看。
 */
export function ArticleCard({ article, detailHref }: ArticleCardProps) {
  const { enriched, title, url, status } = article;
  const displayTldr = status !== "scout" ? enriched?.tldr : undefined;
  const displaySummary =
    status !== "scout" ? enriched?.objective_summary : article.summary;
  const borderColor = getImpactColor(enriched);

  return (
    <article
      className="group relative overflow-hidden rounded-2xl border border-line/60 bg-panel/85 shadow-sm backdrop-blur-sm transition-all duration-300 hover:-translate-y-0.5 hover:border-accent/25 hover:shadow-lg"
      style={{ borderLeft: `4px solid ${borderColor}` }}
    >
      <Link
        href={detailHref}
        className="block p-5 outline-none transition-colors focus-visible:ring-2 focus-visible:ring-accent focus-visible:ring-offset-2 focus-visible:ring-offset-background md:p-6"
        aria-label={`查看文章详情：${title || "无标题"}`}
      >
        <div className="flex flex-col gap-5 lg:flex-row lg:items-start">
          <div className="flex min-w-0 flex-1 flex-col gap-3">
            <div className="flex flex-wrap items-center gap-2.5">
              <StatusBadge status={status} />
              <span className="inline-flex items-center gap-1.5 text-[12px] font-mono text-muted/45">
                {getDomain(url)}
              </span>
              {article.published && (
                <span className="text-[12px] text-muted/35">
                  {article.published}
                </span>
              )}
            </div>

            <div>
              <h3 className="text-[18px] font-bold leading-snug text-foreground transition-colors duration-200 group-hover:text-accent md:text-[19px]">
                {title || "无标题"}
              </h3>
              {displayTldr && (
                <p className="mt-2.5 line-clamp-2 text-[15px] font-semibold leading-[1.65] text-foreground/78">
                  {displayTldr}
                </p>
              )}
              {displaySummary && (
                <p className={`line-clamp-2 text-[14px] leading-[1.75] text-foreground/55 ${displayTldr ? "mt-1.5" : "mt-2.5"}`}>
                  {displaySummary}
                </p>
              )}
            </div>

            <SecondaryTags article={article} />
          </div>

          <div className="flex shrink-0 items-center justify-between gap-4 border-t border-line/50 pt-4 lg:w-44 lg:flex-col lg:items-end lg:border-t-0 lg:pt-0 lg:pr-12">
            <MetricPill article={article} />
            <span className="inline-flex items-center gap-2 text-[13px] font-bold text-accent transition-transform duration-200 group-hover:translate-x-1">
              查看详情
              <svg
                width="15"
                height="15"
                viewBox="0 0 16 16"
                fill="none"
                stroke="currentColor"
                strokeWidth="1.8"
                strokeLinecap="round"
                strokeLinejoin="round"
                aria-hidden="true"
              >
                <path d="M3 8h10" />
                <path d="M9 4l4 4-4 4" />
              </svg>
            </span>
          </div>
        </div>
      </Link>

      <a
        href={url}
        target="_blank"
        rel="noopener noreferrer"
        className="absolute right-4 top-4 inline-flex h-9 w-9 items-center justify-center rounded-full border border-line/60 bg-panel/90 text-muted/45 shadow-sm backdrop-blur transition-colors hover:border-accent/30 hover:text-accent focus:outline-none focus-visible:ring-2 focus-visible:ring-accent focus-visible:ring-offset-2 focus-visible:ring-offset-background lg:right-6 lg:top-6"
        aria-label="打开原文"
        title="打开原文"
      >
        <svg
          width="15"
          height="15"
          viewBox="0 0 16 16"
          fill="none"
          stroke="currentColor"
          strokeWidth="1.6"
          strokeLinecap="round"
          strokeLinejoin="round"
          aria-hidden="true"
        >
          <path d="M6 3H3a1 1 0 0 0-1 1v9a1 1 0 0 0 1 1h9a1 1 0 0 0 1-1v-3" />
          <path d="M9 2h5v5" />
          <path d="M8 8l6-6" />
        </svg>
      </a>
    </article>
  );
}
