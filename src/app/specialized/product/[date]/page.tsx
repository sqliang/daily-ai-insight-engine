// ============================================================================
// /specialized/product/[date] — 产品扫描专题报告页
//
// 展示指定日期的 AI 产品当日简报。
// Phase 2 改为从日报 JSON 的 specializedBrief.productHighlights 读取，
// 保持与日报卡片口径一致；不再直接聚合 all_articles.json。
// ============================================================================

import Link from "next/link";
import type { ReactNode } from "react";
import { loadProductBrief } from "@/lib/data/specialized";
import { PageShell } from "@/components/layout/PageShell";
import { SpecializedReportHero } from "@/components/reports/SpecializedReportHero";

export const dynamic = "force-dynamic";

interface Props {
  params: Promise<{ date: string }>;
}

const LAUNCH_CONTEXT_LABELS: Record<string, string> = {
  new_launch: "新产品",
  major_update: "重大更新",
  pivot: "战略转型",
  funding_announcement: "融资发布",
};

export default async function ProductSpecializedPage({ params }: Props) {
  const { date } = await params;
  const brief = await loadProductBrief(date);

  // 当日无产品简报 → 空状态页
  if (!brief || brief.articleCount === 0) {
    return (
      <PageShell>
        <div className="py-20 text-center">
          <h1 className="text-2xl font-bold text-gray-900 dark:text-gray-100 mb-4">
            {date} 产品扫描专题报告
          </h1>
          <p className="text-gray-500 dark:text-gray-400">
            当日没有新的 AI 产品动态。
          </p>
          <Link
            href="/dashboard"
            className="text-blue-600 hover:underline mt-4 inline-block"
          >
            ← 回到日报列表
          </Link>
        </div>
      </PageShell>
    );
  }

  return (
    <PageShell>
      <SpecializedReportHero
        date={date}
        title="产品扫描"
        eyebrow="Product Brief"
        summary={brief.summary}
        stats={[
          { label: "个产品", value: `${brief.articleCount}` },
          {
            label: "种发布类型",
            value: `${Object.keys(brief.launchContextDistribution).length}`,
          },
          { label: "项推荐", value: `${brief.notableProducts.length}` },
        ]}
      >
        {Object.keys(brief.launchContextDistribution).length > 0 && (
          <TagGroup label="发布上下文">
            {Object.entries(brief.launchContextDistribution)
              .sort((a, b) => b[1] - a[1])
              .map(([context, count]) => (
                <DistributionTag
                  key={context}
                  label={LAUNCH_CONTEXT_LABELS[context] || context}
                  count={count}
                />
              ))}
          </TagGroup>
        )}
      </SpecializedReportHero>

      <section className="mt-10 min-w-0">
        <div className="mb-6 flex items-center justify-between border-b border-line pb-3.5">
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
            <h2 className="text-[15px] font-bold text-foreground">重点产品</h2>
            <span
              className="rounded-md px-2 py-0.5 text-[12px] font-semibold"
              style={{
                color: "var(--accent)",
                backgroundColor:
                  "color-mix(in oklch, var(--accent) 10%, transparent)",
              }}
            >
              {brief.notableProducts.length} 项
            </span>
          </div>
        </div>

        <div className="space-y-5">
          {brief.notableProducts.map((productName, index) => (
            <ProductRow
              key={productName}
              rank={index + 1}
              productName={productName}
            />
          ))}
        </div>
      </section>

      {brief.notableProducts.length === 0 && (
        <p className="text-center text-gray-500 py-12">当日无重点推荐产品。</p>
      )}
    </PageShell>
  );
}

// ---------------------------------------------------------------------------
// 产品行子组件
// ---------------------------------------------------------------------------

function TagGroup({
  label,
  children,
}: {
  label: string;
  children: ReactNode;
}) {
  return (
    <div className="flex flex-col gap-2 sm:flex-row sm:items-start">
      <span className="w-20 shrink-0 text-[11px] font-semibold uppercase tracking-wider text-white/40">
        {label}
      </span>
      <div className="flex flex-wrap gap-1.5">{children}</div>
    </div>
  );
}

function DistributionTag({ label, count }: { label: string; count: number }) {
  return (
    <span className="inline-flex items-center rounded-full border border-white/10 bg-white/[0.04] px-2.5 py-1 text-xs font-medium text-white/65">
      {label}
      <span className="ml-1 text-accent-light">×{count}</span>
    </span>
  );
}

function ProductRow({ rank, productName }: { rank: number; productName: string }) {
  return (
    <article
      className="group relative overflow-hidden rounded-2xl border border-line/60 bg-panel/85 shadow-sm backdrop-blur-sm transition-all duration-300 hover:-translate-y-0.5 hover:border-accent/25 hover:shadow-lg"
      style={{ borderLeft: "4px solid var(--warm)" }}
    >
      <div className="block p-5 outline-none transition-colors md:p-6">
        <div className="flex flex-col gap-5 lg:flex-row lg:items-start">
          <div className="flex min-w-0 flex-1 flex-col gap-3">
            <div className="flex flex-wrap items-center gap-2.5">
              <span className="inline-flex items-center rounded-full bg-accent/8 px-3 py-1 text-[12px] font-semibold text-accent">
                Product Brief
              </span>
              <span className="font-mono text-[12px] text-muted/45">
                #{rank}
              </span>
            </div>

            <div>
              <h3 className="text-[18px] font-bold leading-snug text-foreground transition-colors duration-200 group-hover:text-accent md:text-[19px]">
                {productName}
              </h3>
              <p className="mt-2.5 line-clamp-2 text-[14px] leading-[1.75] text-foreground/55">
                今日产品专题简报选出的重点产品，可用于快速观察新品方向、用户场景与产品化信号。
              </p>
            </div>
          </div>

          <div className="flex shrink-0 items-center justify-between gap-4 border-t border-line/50 pt-4 lg:w-44 lg:flex-col lg:items-end lg:border-t-0 lg:pt-0 lg:pr-12">
            <span className="inline-flex min-w-16 items-center justify-center rounded-xl bg-accent/8 px-3 py-2 font-mono text-[17px] font-bold tabular-nums text-accent ring-1 ring-accent/15">
              {rank}
            </span>
            <span className="inline-flex items-center gap-2 text-[13px] font-bold text-accent transition-transform duration-200 group-hover:translate-x-1">
              查看摘要
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
                <path d="m9 4 4 4-4 4" />
              </svg>
            </span>
          </div>
        </div>
      </div>
    </article>
  );
}
