// ============================================================================
// src/app/specialized/github/[date]/page.tsx — 项目洞察页
//
// 展示指定日期的项目洞察简报，是”专题洞察”三页面之一。
// 数据基于 Stage 2 specialized_tags.github 与 Stage 3 github_assessment 识别出的
// 开源项目与技术方案，经 Stage 4b 主编 Agent 跨天去重后写入日报 JSON。
// 优先使用 specializedBrief.projectInsights（新版完整洞察结构），
// 不存在时回退到 githubHighlights（旧版轻量列表），保持与 /dashboard/{date}
// 卡片口径一致。
//
// 设计理由：
//   专题洞察在 Stage 4b 由主编 Agent 统一生成并做过跨天去重，前端不再重复聚合
//   all_articles.json。这样既能保证 /dashboard 入口与专题详情页数据一致，又能让
//   专题页专注于渲染决策辅助信息（keyJudgment、watchSignals、项目条目、来源引用）。
// ============================================================================

import Link from "next/link";
import type { ReactNode } from "react";
import {
  loadGithubBrief,
  type SpecializedInsightItem,
} from "@/lib/data/specialized";
import { PageShell } from "@/components/layout/PageShell";
import { SpecializedReportHero } from "@/components/reports/SpecializedReportHero";
import {
  DOMAIN_LABELS,
} from "@/components/sources/GitHubProjectCard";
import {
  ensureSentencePunctuation,
  ensureSentencePunctuationList,
} from "@/lib/utils/text";

export const dynamic = "force-dynamic";

interface Props {
  params: Promise<{ date: string }>;
}

const INSIGHT_DISTRIBUTION_LABELS: Record<string, string> = {
  framework_tools: "框架与工具",
  application_landing: "应用落地",
  infrastructure_update: "基础设施",
  capital_movement: "资本与商业",
  research_breakthrough: "研究突破",
  governance_risk: "治理与风险",
  other: "其他",
  其他: "其他",
};

function formatDistributionLabel(key: string): string {
  return INSIGHT_DISTRIBUTION_LABELS[key] || DOMAIN_LABELS[key] || key.replace(/_/g, " ");
}

export default async function GithubSpecializedPage({ params }: Props) {
  const { date } = await params;
  const brief = await loadGithubBrief(date);
  const domainEntries = Object.entries(brief?.domainDistribution || {})
    .filter(([, count]) => count > 0)
    .sort((a, b) => b[1] - a[1]);

  // 当日无项目简报 → 空状态页
  if (!brief || brief.articleCount === 0) {
    return (
      <PageShell>
        <div className="py-20 text-center">
          <h1 className="text-2xl font-bold text-gray-900 dark:text-gray-100 mb-4">
            {date} 项目洞察报告
          </h1>
          <p className="text-gray-500 dark:text-gray-400">
            当日没有新的项目洞察对象。
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
        title="项目洞察"
        eyebrow="Project Insights"
        summary={brief.summary}
        stats={[
          { label: "个项目", value: `${brief.items.length || brief.articleCount}` },
          { label: "个领域", value: `${Object.keys(brief.domainDistribution).length}` },
          { label: "个来源", value: `${brief.sourceCoverage?.length || 0}` },
        ]}
      >
        <div className="space-y-3">
          {domainEntries.length > 0 && (
            <TagGroup label="领域分布">
              {domainEntries.map(([domain, count]) => (
                <DistributionTag
                  key={domain}
                  label={formatDistributionLabel(domain)}
                  count={count}
                />
              ))}
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

      {(brief.keyJudgment || (brief.watchSignals && brief.watchSignals.length > 0)) && (
        <section className="mt-8 grid gap-4 lg:grid-cols-[minmax(0,1.15fr)_minmax(360px,0.85fr)]">
          {brief.keyJudgment && (
            <InsightPanel
              eyebrow="Judgment"
              title="关键判断"
              body={brief.keyJudgment}
              accent="var(--accent)"
            />
          )}
          {brief.watchSignals && brief.watchSignals.length > 0 && (
            <SignalPanel
              title="后续关注"
              signals={brief.watchSignals}
              accent="var(--accent)"
            />
          )}
        </section>
      )}

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
            <h2 className="text-[15px] font-bold text-foreground">项目洞察对象</h2>
            <span
              className="rounded-md px-2 py-0.5 text-[12px] font-semibold"
              style={{
                color: "var(--accent)",
                backgroundColor:
                  "color-mix(in oklch, var(--accent) 10%, transparent)",
              }}
            >
              {brief.items.length} 项
            </span>
          </div>
        </div>

        <div className="space-y-5">
          {brief.items.map((item, index) => (
            <InsightRow
              key={`${item.canonicalName}-${index}`}
              rank={index + 1}
              item={item}
              tone="accent"
            />
          ))}
        </div>
      </section>

      {brief.items.length === 0 && (
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

function InsightPanel({
  eyebrow,
  title,
  body,
  accent,
}: {
  eyebrow: string;
  title: string;
  body: string;
  accent: string;
}) {
  return (
    <section
      className="relative overflow-hidden rounded-lg bg-panel/95 p-6 shadow-md shadow-black/5 ring-1 ring-black/5"
      style={{
        background: `linear-gradient(135deg, color-mix(in oklch, ${accent} 14%, transparent), var(--panel) 58%)`,
      }}
    >
      <div className="flex items-center gap-3">
        <span
          className="inline-flex h-9 w-9 items-center justify-center rounded-md text-[15px] font-black text-white shadow-sm"
          style={{ backgroundColor: accent }}
        >
          !
        </span>
        <div>
          <p className="text-[11px] font-black uppercase tracking-wider text-foreground/45">
            {eyebrow}
          </p>
          <h2 className="text-[17px] font-black text-foreground">{title}</h2>
        </div>
      </div>
      <p className="mt-5 max-w-4xl text-[16px] font-medium leading-8 text-foreground/78">
        {ensureSentencePunctuation(body)}
      </p>
    </section>
  );
}

function SignalPanel({
  title,
  signals,
  accent,
}: {
  title: string;
  signals: string[];
  accent: string;
}) {
  return (
    <section
      className="rounded-lg bg-panel/95 p-6 shadow-md shadow-black/5 ring-1 ring-black/5"
      style={{
        background: `linear-gradient(135deg, color-mix(in oklch, ${accent} 10%, transparent), var(--panel) 64%)`,
      }}
    >
      <div className="flex items-center justify-between gap-3">
        <h2 className="text-[17px] font-black text-foreground">{title}</h2>
        <span
          className="rounded-md px-2.5 py-1 font-mono text-[12px] font-black"
          style={{
            color: accent,
            backgroundColor: `color-mix(in oklch, ${accent} 10%, transparent)`,
          }}
        >
          {signals.length} signals
        </span>
      </div>
      <div className="mt-4 space-y-2.5">
        {ensureSentencePunctuationList(signals).slice(0, 5).map((signal, index) => (
          <div
            key={signal}
            className="flex items-start gap-3 rounded-md bg-white/60 p-3 shadow-sm shadow-black/4 dark:bg-white/[0.04]"
          >
            <span
              className="mt-0.5 inline-flex h-6 w-6 shrink-0 items-center justify-center rounded-md font-mono text-[11px] font-black text-white"
              style={{ backgroundColor: accent }}
            >
              {index + 1}
            </span>
            <p className="text-[14px] font-bold leading-6 text-foreground/78">
              {signal}
            </p>
          </div>
        ))}
      </div>
    </section>
  );
}

function InsightRow({
  rank,
  item,
  tone,
}: {
  rank: number;
  item: SpecializedInsightItem;
  tone: "accent" | "warm";
}) {
  const accent = tone === "warm" ? "var(--warm)" : "var(--accent)";
  const href = item.url || undefined;
  const displayName = item.canonicalName || item.name;
  const host = href ? href.replace(/^https?:\/\//, "").replace(/\/$/, "") : "";

  const content = (
    <article
      className="group relative overflow-hidden rounded-lg bg-panel/95 shadow-md shadow-black/6 ring-1 ring-black/5 backdrop-blur-sm transition-all duration-300 hover:-translate-y-0.5 hover:shadow-xl hover:shadow-black/8 motion-reduce:transition-none"
      style={{
        background: `linear-gradient(180deg, color-mix(in oklch, ${accent} 9%, transparent), var(--panel) 32%)`,
      }}
    >
      <div
        className="h-1.5 w-full"
        style={{ backgroundColor: accent }}
        aria-hidden="true"
      />
      <div className="p-5 md:p-6">
        <div className="grid gap-5 lg:grid-cols-[1fr_160px]">
          <div className="min-w-0">
            <div className="flex flex-wrap items-center gap-2">
              <span
                className="inline-flex h-9 min-w-9 items-center justify-center rounded-md px-2 font-mono text-[12px] font-black tabular-nums text-white shadow-sm"
                style={{ backgroundColor: accent }}
              >
                {String(rank).padStart(2, "0")}
              </span>
              <span className="inline-flex items-center rounded-md border border-accent/20 bg-accent/10 px-2.5 py-1 text-[12px] font-black text-accent">
                项目洞察
              </span>
              {host && (
                <span className="max-w-full truncate font-mono text-[12px] font-semibold text-foreground/50">
                  {host}
                </span>
              )}
            </div>

            <div className="mt-4">
              <h3 className="text-[20px] font-black leading-tight text-foreground transition-colors duration-200 group-hover:text-accent md:text-[22px]">
                {displayName}
              </h3>
              <p className="mt-3 max-w-5xl text-[15px] font-medium leading-7 text-foreground/72">
                {ensureSentencePunctuation(item.oneLine || item.whyItMatters)}
              </p>
            </div>
          </div>

          <div className="flex items-center justify-between gap-4 rounded-lg bg-white/55 p-4 shadow-sm shadow-black/4 dark:bg-white/[0.04] lg:flex-col lg:items-end lg:justify-start">
            <div className="text-left lg:text-right">
              <p className="text-[11px] font-black uppercase tracking-wider text-foreground/55">
                关注评分
              </p>
              <p className="mt-1 font-mono text-[34px] font-black leading-none tabular-nums text-accent">
                {item.score.toFixed(1)}
              </p>
            </div>
            {href && (
              <Link
                href={href}
                target="_blank"
                rel="noopener noreferrer"
                className="inline-flex min-h-10 items-center gap-2 rounded-md bg-accent px-3 text-[13px] font-black text-white shadow-sm transition-transform hover:-translate-y-0.5 focus:outline-none focus-visible:ring-2 focus-visible:ring-accent/40 motion-reduce:transition-none"
              >
                打开对象
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
              </Link>
            )}
          </div>
        </div>

        <div className="mt-5 grid gap-3 lg:grid-cols-2">
          <MiniBlock
            title="关注理由"
            items={ensureSentencePunctuationList([item.whyItMatters])}
            accent={accent}
          />
          <MiniBlock
            title="机会信号"
            items={ensureSentencePunctuationList(item.signals)}
            accent={accent}
          />
          {item.risks.length > 0 && (
            <MiniBlock
              title="风险提示"
              items={ensureSentencePunctuationList(item.risks)}
              accent={accent}
            />
          )}
          {item.sources.length > 0 && (
            <SourceBlock sources={item.sources} accent={accent} />
          )}
        </div>

        {item.evidenceSnippets.length > 0 && (
          <div className="mt-5">
            <p className="text-[11px] font-black uppercase tracking-wider text-foreground/55">
              证据片段
            </p>
            <p className="mt-2 line-clamp-2 rounded-md bg-white/55 px-3 py-2 text-[13px] font-semibold leading-6 text-foreground/74 shadow-sm shadow-black/4 dark:bg-white/[0.04]">
              {ensureSentencePunctuation(item.evidenceSnippets[0])}
            </p>
          </div>
        )}
      </div>
    </article>
  );

  return content;
}

function MiniBlock({
  title,
  items,
  accent,
}: {
  title: string;
  items: string[];
  accent: string;
}) {
  if (items.length === 0) return null;
  return (
    <div
      className="min-w-0 rounded-md p-4 shadow-sm shadow-black/4"
      style={{
        backgroundColor: `color-mix(in oklch, ${accent} 7%, var(--surface))`,
      }}
    >
      <p className="flex items-center gap-2 text-[12px] font-black text-foreground/82">
        <span
          className="h-1.5 w-1.5 rounded-full"
          style={{ backgroundColor: accent }}
          aria-hidden="true"
        />
        {title}
      </p>
      <ul className="mt-3 space-y-2.5 text-[13px] font-medium leading-6 text-foreground/76">
        {items.slice(0, 3).map((item) => (
          <li key={item} className="relative pl-3 before:absolute before:left-0 before:top-2.5 before:h-1.5 before:w-1.5 before:rounded-full before:bg-current before:text-foreground/35">
            {item}
          </li>
        ))}
      </ul>
    </div>
  );
}

function SourceBlock({
  sources,
  accent,
}: {
  sources: SpecializedInsightItem["sources"];
  accent: string;
}) {
  return (
    <div
      className="min-w-0 rounded-md p-4 shadow-sm shadow-black/4"
      style={{
        backgroundColor: `color-mix(in oklch, ${accent} 7%, var(--surface))`,
      }}
    >
      <p className="flex items-center gap-2 text-[12px] font-black text-foreground/82">
        <span
          className="h-1.5 w-1.5 rounded-full"
          style={{ backgroundColor: accent }}
          aria-hidden="true"
        />
        文章来源
      </p>
      <div className="mt-2.5 flex flex-wrap gap-1.5">
        {sources.slice(0, 4).map((source) => (
          <Link
            key={`${source.articleId}-${source.url}`}
            href={source.url || "#"}
            target="_blank"
            rel="noopener noreferrer"
            className="max-w-full rounded-md bg-panel/90 px-2.5 py-1 text-[12px] font-bold text-foreground/76 shadow-sm shadow-black/4 transition-colors hover:text-accent focus:outline-none focus-visible:ring-2 focus-visible:ring-accent/35"
          >
            <span className="font-mono">{source.sourceDir || "source"}</span>
            {source.title && (
              <span className="ml-1 text-foreground/52">
                · {source.title.slice(0, 28)}
              </span>
            )}
          </Link>
        ))}
      </div>
    </div>
  );
}
