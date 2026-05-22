import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { Suspense } from "react";
import { getSourceDetailEnriched, type DateRange } from "@/lib/data/sources";
import { PageShell } from "@/components/layout/PageShell";
import { ArticleList } from "@/components/sources/ArticleList";
import { DateFilterBar } from "@/components/sources/DateFilterBar";
import {
  TIER_SHORT_LABELS,
  SOURCE_TYPE_LABELS,
  LANGUAGE_LABELS,
} from "@/lib/data/tiers";

export const dynamic = "force-dynamic";

export async function generateMetadata({
  params,
}: {
  params: Promise<{ name: string }>;
}): Promise<Metadata> {
  const { name } = await params;
  return { title: `${name} - 数据源详情` };
}

function formatGeneratedAt(iso: string): string {
  const d = new Date(iso);
  const pad = (n: number) => String(n).padStart(2, "0");
  return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())} ${pad(d.getHours())}:${pad(d.getMinutes())}`;
}

export default async function SourceDetailPage({
  params,
  searchParams,
}: {
  params: Promise<{ name: string }>;
  searchParams: Promise<{ from?: string; to?: string }>;
}) {
  const { name } = await params;
  const sp = await searchParams;

  const dateRange: DateRange | undefined =
    sp.from || sp.to ? { from: sp.from, to: sp.to } : undefined;

  const source = await getSourceDetailEnriched(name, dateRange);
  if (!source) notFound();

  const hasManifest = source.manifestFound && source.articleCount > 0;

  return (
    <PageShell>
      {/* ====== Banner — tier-colored gradient hero ====== */}
      <header className="relative overflow-hidden rounded-2xl bg-gradient-to-br from-foreground via-foreground to-accent-dark p-6 shadow-lg md:p-10"
        style={{ backgroundImage: source.tier === "B"
          ? "linear-gradient(135deg, var(--foreground), oklch(0.18 0.02 260), oklch(0.38 0.12 85))"
          : source.tier === "C"
          ? "linear-gradient(135deg, var(--foreground), oklch(0.18 0.02 260), oklch(0.33 0.12 340))"
          : undefined
        }}
      >
        {/* Decorative SVG shapes */}
        <svg
          className="pointer-events-none absolute inset-0 h-full w-full"
          aria-hidden="true"
          viewBox="0 0 1200 360"
          preserveAspectRatio="none"
        >
          <circle cx="1050" cy="50" r="160" fill="oklch(0.55 0.13 200 / 0.10)" />
          <circle cx="1080" cy="30" r="90" fill="oklch(0.55 0.13 200 / 0.08)" />
          <circle cx="80" cy="310" r="120" fill="oklch(0.45 0.16 340 / 0.08)" />
          <circle cx="50" cy="330" r="70" fill="oklch(0.45 0.16 340 / 0.06)" />
          {Array.from({ length: 5 }).flatMap((_, row) =>
            Array.from({ length: 5 }).map((_, col) => (
              <circle
                key={`${row}-${col}`}
                cx={30 + col * 22}
                cy={20 + row * 22}
                r="1"
                fill="oklch(1 0 0 / 0.15)"
              />
            )),
          )}
          <line
            x1="30" y1="340" x2="380" y2="340"
            stroke="oklch(0.55 0.13 200 / 0.20)"
            strokeWidth="0.5"
            strokeDasharray="4 6"
          />
        </svg>

        <div className="relative">
          {/* Breadcrumb */}
          <Link
            href="/sources"
            className="inline-flex items-center gap-1.5 text-[12px] font-medium text-white/50
                       hover:text-accent-light transition-colors duration-200"
          >
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor"
              strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <polyline points="15 18 9 12 15 6" />
            </svg>
            数据源列表
          </Link>

          {/* Title row */}
          <div className="mt-4 flex flex-wrap items-center gap-3">
            <h1 className="text-2xl font-bold tracking-tight text-white md:text-3xl break-words min-w-0">
              {source.display_name}
            </h1>
            {/* Live indicator */}
            {hasManifest && (
              <span className="relative flex h-2.5 w-2.5">
                <span className="absolute inline-flex h-full w-full animate-ping rounded-full bg-accent opacity-60" />
                <span className="relative inline-flex h-2.5 w-2.5 rounded-full bg-accent" />
              </span>
            )}
          </div>

          {/* Metadata pills — glass */}
          <div className="mt-4 flex flex-wrap items-center gap-2">
            <span className="inline-flex items-center gap-1.5 rounded-full border border-white/10 bg-white/5 px-3 py-1 text-[11px] font-medium text-white/70 backdrop-blur">
              <span className="h-1.5 w-1.5 rounded-full bg-accent" />
              {TIER_SHORT_LABELS[source.tier] ?? source.tier}
            </span>
            <span className="inline-flex items-center gap-1.5 rounded-full border border-white/10 bg-white/5 px-3 py-1 text-[11px] font-medium text-white/70 backdrop-blur">
              {SOURCE_TYPE_LABELS[source.type] ?? source.type}
            </span>
            <span className="inline-flex items-center gap-1.5 rounded-full border border-white/10 bg-white/5 px-3 py-1 text-[11px] font-medium text-white/70 backdrop-blur">
              {LANGUAGE_LABELS[source.language] ?? source.language}
            </span>
            <span className="inline-flex items-center gap-1.5 rounded-full border border-white/10 bg-white/5 px-3 py-1 text-[11px] font-medium text-white/50 backdrop-blur font-mono">
              {source.fetch_strategy}
            </span>
            {source.manifestDate && (
              <span className="inline-flex items-center gap-1.5 rounded-full border border-white/10 bg-white/5 px-3 py-1 text-[11px] font-medium text-white/50 backdrop-blur">
                <svg width="11" height="11" viewBox="0 0 16 16" fill="none" stroke="currentColor" strokeWidth="1.5">
                  <circle cx="8" cy="8" r="6.5" />
                  <path d="M8 4.5V8l3 2" strokeLinecap="round" strokeLinejoin="round" />
                </svg>
                {source.manifestDate}
              </span>
            )}
          </div>

          {/* Description + Keywords — glass panel */}
          {source.display_description && (
            <div className="mt-5 rounded-xl border border-white/8 bg-white/[0.04] p-4 backdrop-blur md:p-5">
              <p className="text-sm leading-7 text-white/75 md:text-[15px] md:leading-8">
                {source.display_description}
              </p>
              {source.keywords.length > 0 && (
                <div className="mt-3 flex flex-wrap gap-1">
                  {source.keywords.slice(0, 5).map((kw) => (
                    <span
                      key={kw}
                      className="rounded bg-white/8 px-1.5 py-0.5 text-[10px] font-mono text-white/40"
                    >
                      {kw}
                    </span>
                  ))}
                  {source.keywords.length > 5 && (
                    <span className="rounded bg-white/8 px-1.5 py-0.5 text-[10px] font-mono text-white/30">
                      +{source.keywords.length - 5}
                    </span>
                  )}
                </div>
              )}
            </div>
          )}

          {/* Source URL */}
          <a
            href={source.url}
            target="_blank"
            rel="noopener noreferrer"
            className="mt-4 flex items-start gap-1.5 max-w-full text-[12px] text-white/35
                       hover:text-accent-light transition-colors duration-200 leading-relaxed"
          >
            <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"
              strokeLinecap="round" strokeLinejoin="round" className="shrink-0 mt-0.5">
              <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6" />
              <polyline points="15 3 21 3 21 9" />
              <line x1="10" y1="14" x2="21" y2="3" />
            </svg>
            <span className="break-all min-w-0">{source.url}</span>
          </a>

          {/* Stats bar */}
          <div className="mt-5 flex flex-wrap items-center gap-x-4 gap-y-2">
            <span className="inline-flex items-center gap-1.5 rounded-full bg-white/10 px-3 py-1 text-[12px] font-semibold text-white/80 backdrop-blur">
              {source.articleCount} 篇文章
            </span>
            {source.stageCounts.analyzed > 0 && (
              <span className="inline-flex items-center gap-1.5 text-[11px] text-white/50">
                <span className="h-1.5 w-1.5 rounded-full" style={{ backgroundColor: "var(--accent)" }} />
                {source.stageCounts.analyzed} 篇深度分析
              </span>
            )}
            {source.stageCounts.extracted > 0 && (
              <span className="inline-flex items-center gap-1.5 text-[11px] text-white/50">
                <span className="h-1.5 w-1.5 rounded-full" style={{ backgroundColor: "var(--warm)" }} />
                {source.stageCounts.extracted} 篇已提取
              </span>
            )}
            {source.stageCounts.scout > 0 && (
              <span className="inline-flex items-center gap-1.5 text-[11px] text-white/50">
                <span className="h-1.5 w-1.5 rounded-full" style={{ backgroundColor: "var(--muted)" }} />
                {source.stageCounts.scout} 篇待处理
              </span>
            )}
            {source.manifestGeneratedAt && (
              <span className="text-[11px] text-white/35">
                生成于 {formatGeneratedAt(source.manifestGeneratedAt)}
              </span>
            )}
          </div>
        </div>
      </header>

      <div className="mt-10">
        <Suspense fallback={null}>
          <DateFilterBar />
        </Suspense>
        <ArticleList
          articles={source.articles}
          hasManifest={hasManifest}
          manifestFound={source.manifestFound}
          articleCount={source.articleCount}
          dateRange={source.dateRange}
        />
      </div>
    </PageShell>
  );
}
