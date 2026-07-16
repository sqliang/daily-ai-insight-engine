// ============================================================================
// /specialized/github/[date] — GitHub 开源项目专题报告页
//
// 展示指定日期的 GitHub Trending 当日简报。
// Phase 1 改为从日报 JSON 的 specializedBrief.githubHighlights 读取，
// 保持与日报卡片口径一致；不再直接聚合 all_articles.json。
// ============================================================================

import Link from "next/link";
import type { ReactNode } from "react";
import { loadGithubBrief } from "@/lib/data/specialized";
import { PageShell } from "@/components/layout/PageShell";
import { SpecializedReportHero } from "@/components/reports/SpecializedReportHero";
import {
  DOMAIN_LABELS,
  DOMAIN_LIST,
} from "@/components/sources/GitHubProjectCard";

export const dynamic = "force-dynamic";

interface Props {
  params: Promise<{ date: string }>;
}

export default async function GithubSpecializedPage({ params }: Props) {
  const { date } = await params;
  const brief = await loadGithubBrief(date);

  // 当日无 GitHub 简报 → 空状态页
  if (!brief || brief.articleCount === 0) {
    return (
      <PageShell>
        <div className="py-20 text-center">
          <h1 className="text-2xl font-bold text-gray-900 dark:text-gray-100 mb-4">
            {date} GitHub 项目专题报告
          </h1>
          <p className="text-gray-500 dark:text-gray-400">
            当日没有新的 GitHub Trending 项目。
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
        title="GitHub 开源项目"
        eyebrow="GitHub Project Brief"
        summary={brief.summary}
        stats={[
          { label: "个项目", value: `${brief.articleCount}` },
          { label: "个领域", value: `${Object.keys(brief.domainDistribution).length}` },
          { label: "个 AI 类目", value: `${Object.keys(brief.aiCategoryDistribution || {}).length}` },
        ]}
      >
        <div className="space-y-3">
          {Object.keys(brief.domainDistribution).length > 0 && (
            <TagGroup label="领域分布">
              {DOMAIN_LIST.filter((d) => brief.domainDistribution[d]).map(
                (d) => (
                  <DistributionTag
                    key={d}
                    label={DOMAIN_LABELS[d] || d}
                    count={brief.domainDistribution[d]}
                  />
                ),
              )}
            </TagGroup>
          )}

          {brief.aiCategoryDistribution &&
            Object.keys(brief.aiCategoryDistribution).length > 0 && (
              <TagGroup label="AI 子领域">
                {Object.entries(brief.aiCategoryDistribution)
                  .sort((a, b) => b[1] - a[1])
                  .map(([cat, count]) => (
                    <DistributionTag
                      key={cat}
                      label={cat.replace(/_/g, " ")}
                      count={count}
                    />
                  ))}
              </TagGroup>
            )}
        </div>
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
            <h2 className="text-[15px] font-bold text-foreground">重点项目</h2>
            <span
              className="rounded-md px-2 py-0.5 text-[12px] font-semibold"
              style={{
                color: "var(--accent)",
                backgroundColor:
                  "color-mix(in oklch, var(--accent) 10%, transparent)",
              }}
            >
              {brief.topProjects.length} 项
            </span>
          </div>
        </div>

        <div className="space-y-5">
          {brief.topProjects.map((projectName, index) => (
            <ProjectRow
              key={projectName}
              rank={index + 1}
              projectName={projectName}
            />
          ))}
        </div>
      </section>

      {brief.topProjects.length === 0 && (
        <p className="text-center text-gray-500 py-12">当日无重点推荐项目。</p>
      )}
    </PageShell>
  );
}

// ---------------------------------------------------------------------------
// 项目行子组件
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

function ProjectRow({ rank, projectName }: { rank: number; projectName: string }) {
  // 尝试从 "owner/repo" 格式构造 GitHub 仓库 URL
  const githubUrl = /^[\w.-]+\/[\w.-]+$/.test(projectName)
    ? `https://github.com/${projectName}`
    : undefined;

  const content = (
    <article
      className="group relative overflow-hidden rounded-2xl border border-line/60 bg-panel/85 shadow-sm backdrop-blur-sm transition-all duration-300 hover:-translate-y-0.5 hover:border-accent/25 hover:shadow-lg"
      style={{ borderLeft: "4px solid var(--accent)" }}
    >
      <div className="block p-5 outline-none transition-colors md:p-6">
        <div className="flex flex-col gap-5 lg:flex-row lg:items-start">
          <div className="flex min-w-0 flex-1 flex-col gap-3">
            <div className="flex flex-wrap items-center gap-2.5">
              <span className="inline-flex items-center rounded-full bg-accent/8 px-3 py-1 text-[12px] font-semibold text-accent">
                GitHub Trending
              </span>
              <span className="font-mono text-[12px] text-muted/45">
                #{rank}
              </span>
              {githubUrl && (
                <span className="truncate font-mono text-[12px] text-muted/45">
                  github.com/{projectName}
                </span>
              )}
            </div>

            <div>
              <h3 className="text-[18px] font-bold leading-snug text-foreground transition-colors duration-200 group-hover:text-accent md:text-[19px]">
                {projectName}
              </h3>
              <p className="mt-2.5 line-clamp-2 text-[14px] leading-[1.75] text-foreground/55">
                今日 GitHub 专题简报选出的重点项目，可结合仓库主页继续查看功能定位、实现方式与社区信号。
              </p>
            </div>
          </div>

          <div className="flex shrink-0 items-center justify-between gap-4 border-t border-line/50 pt-4 lg:w-44 lg:flex-col lg:items-end lg:border-t-0 lg:pt-0 lg:pr-12">
            <span className="inline-flex min-w-16 items-center justify-center rounded-xl bg-accent/8 px-3 py-2 font-mono text-[17px] font-bold tabular-nums text-accent ring-1 ring-accent/15">
              {rank}
            </span>
            {githubUrl && (
              <span className="inline-flex items-center gap-2 text-[13px] font-bold text-accent transition-transform duration-200 group-hover:translate-x-1">
                打开仓库
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
                  <path d="M6 3H3a1 1 0 0 0-1 1v9a1 1 0 0 0 1 1h9a1 1 0 0 0 1-1v-3" />
                  <path d="M9 2h5v5" />
                  <path d="M8 8l6-6" />
                </svg>
              </span>
            )}
          </div>
        </div>
      </div>
    </article>
  );

  if (githubUrl) {
    return (
      <Link
        href={githubUrl}
        target="_blank"
        rel="noopener noreferrer"
        className="block focus:outline-none focus-visible:ring-2 focus-visible:ring-accent"
      >
        {content}
      </Link>
    );
  }

  return content;
}
