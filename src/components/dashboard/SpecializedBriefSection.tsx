// ============================================================================
// SpecializedBriefSection.tsx — 日报专题简报入口 Section
//
// 从 dailyReport.specializedBrief 读取可选子块，
// 渲染为入口卡片，点击进入专题报告详情页。
// ============================================================================

import Link from 'next/link';
import { DOMAIN_LABELS } from '@/components/sources/GitHubProjectCard';
import { RESEARCH_AREA_LABELS } from '@/components/sources/PaperCard';

// ---------------------------------------------------------------------------
// 类型定义（匹配 Stage 4b 输出的 specializedBrief 字段形状）
// ---------------------------------------------------------------------------

interface GithubHighlights {
  summary: string;
  topProjects: string[];
  domainDistribution: Record<string, number>;
  aiCategoryDistribution?: Record<string, number> | null;
  articleCount: number;
}

interface PaperHighlights {
  summary: string;
  keyPapers: string[];
  researchAreas: string[];
  articleCount: number;
}

interface SpecializedBrief {
  githubHighlights?: GithubHighlights | null;
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  productHighlights?: any;
  paperHighlights?: PaperHighlights | null;
}

interface SpecializedBriefSectionProps {
  data: SpecializedBrief | null | undefined;
  date: string;
}

// ---------------------------------------------------------------------------
// 主组件
// ---------------------------------------------------------------------------

/**
 * 日报专题简报入口 Section。
 *
 * 在 DashboardContent 中渲染，展示 GitHub/Product/Paper 三个专题的摘要卡片。
 * 当 specializedBrief 为空或所有子块均为 null 时，不渲染任何内容。
 * 当前只有 GitHub 专题有完整页面（/specialized/github/[date]），其他为占位卡片。
 */
export function SpecializedBriefSection({ data, date }: SpecializedBriefSectionProps) {
  if (!data) return null;

  const hasContent = data.githubHighlights || data.productHighlights || data.paperHighlights;
  if (!hasContent) return null;

  return (
    <section className="mt-8">
      <h2 className="text-xl font-bold text-gray-900 dark:text-gray-100 mb-4">
        专题洞察
      </h2>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {data.githubHighlights && (
          <GithubBriefCard data={data.githubHighlights} date={date} />
        )}
        {data.productHighlights && (
          <BriefCardPlaceholder
            icon="📦"
            title="产品扫描"
            summary={data.productHighlights.summary}
            count={data.productHighlights.articleCount}
          />
        )}
        {data.paperHighlights && (
          <PaperBriefCard data={data.paperHighlights} date={date} />
        )}
      </div>
    </section>
  );
}

// ---------------------------------------------------------------------------
// GitHub 简报卡片
// ---------------------------------------------------------------------------

function GithubBriefCard({ data, date }: { data: GithubHighlights; date: string }) {
  return (
    <Link
      href={`/specialized/github/${date}`}
      className="block rounded-xl border border-purple-200 dark:border-purple-800 bg-gradient-to-br from-purple-50 to-indigo-50 dark:from-purple-950/20 dark:to-indigo-950/20 p-5 hover:shadow-md hover:border-purple-300 dark:hover:border-purple-700 transition-all group"
    >
      <div className="flex items-center gap-2 mb-2">
        <span className="text-2xl">🐙</span>
        <h3 className="text-lg font-semibold text-gray-900 dark:text-gray-100">
          GitHub 开源项目
        </h3>
        <span className="ml-auto inline-flex items-center rounded-full bg-purple-100 dark:bg-purple-900/30 px-2 py-0.5 text-xs font-medium text-purple-700 dark:text-purple-300">
          {data.articleCount} 个项目
        </span>
      </div>

      <p className="text-sm text-gray-600 dark:text-gray-400 mb-3 line-clamp-2">
        {data.summary}
      </p>

      {/* Top 项目列表 */}
      {data.topProjects?.length > 0 && (
        <div className="space-y-1 mb-3">
          {data.topProjects.slice(0, 3).map((name, i) => (
            <div key={name} className="flex items-center gap-2 text-sm text-gray-700 dark:text-gray-300">
              <span className="text-purple-400 text-xs font-mono">{i + 1}.</span>
              <span className="truncate">{name}</span>
            </div>
          ))}
        </div>
      )}

      {/* 领域分布预览 */}
      {data.domainDistribution && Object.keys(data.domainDistribution).length > 0 && (
        <div className="flex flex-wrap gap-1">
          {Object.entries(data.domainDistribution)
            .sort((a, b) => b[1] - a[1])
            .slice(0, 4)
            .map(([domain, count]) => (
              <span
                key={domain}
                className="inline-flex items-center rounded-full bg-white/60 dark:bg-gray-800/60 px-2 py-0.5 text-xs text-gray-600 dark:text-gray-400"
              >
                {DOMAIN_LABELS[domain] || domain} ×{count}
              </span>
            ))}
          {Object.keys(data.domainDistribution).length > 4 && (
            <span className="text-xs text-gray-400">
              +{Object.keys(data.domainDistribution).length - 4}
            </span>
          )}
        </div>
      )}

      <div className="mt-3 flex items-center text-sm text-purple-600 dark:text-purple-400 group-hover:underline">
        查看完整报告
        <svg className="w-4 h-4 ml-1 group-hover:translate-x-0.5 transition-transform" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
        </svg>
      </div>
    </Link>
  );
}

// ---------------------------------------------------------------------------
// 论文简报卡片
// ---------------------------------------------------------------------------

function PaperBriefCard({ data, date }: { data: PaperHighlights; date: string }) {
  return (
    <Link
      href={`/specialized/paper/${date}`}
      className="block rounded-xl border border-purple-200 dark:border-purple-800 bg-gradient-to-br from-purple-50 to-indigo-50 dark:from-purple-950/20 dark:to-indigo-950/20 p-5 hover:shadow-md hover:border-purple-300 dark:hover:border-purple-700 transition-all group"
    >
      <div className="flex items-center gap-2 mb-2">
        <span className="text-2xl">📄</span>
        <h3 className="text-lg font-semibold text-gray-900 dark:text-gray-100">
          论文速递
        </h3>
        <span className="ml-auto inline-flex items-center rounded-full bg-purple-100 dark:bg-purple-900/30 px-2 py-0.5 text-xs font-medium text-purple-700 dark:text-purple-300">
          {data.articleCount} 篇论文
        </span>
      </div>

      <p className="text-sm text-gray-600 dark:text-gray-400 mb-3 line-clamp-2">
        {data.summary}
      </p>

      {/* 重点论文列表 */}
      {data.keyPapers?.length > 0 && (
        <div className="space-y-1 mb-3">
          {data.keyPapers.slice(0, 3).map((name, i) => (
            <div key={name} className="flex items-center gap-2 text-sm text-gray-700 dark:text-gray-300">
              <span className="text-purple-400 text-xs font-mono">{i + 1}.</span>
              <span className="truncate">{name}</span>
            </div>
          ))}
        </div>
      )}

      {/* 研究领域分布预览 */}
      {data.researchAreas?.length > 0 && (
        <div className="flex flex-wrap gap-1">
          {data.researchAreas.slice(0, 4).map((area) => (
            <span
              key={area}
              className="inline-flex items-center rounded-full bg-white/60 dark:bg-gray-800/60 px-2 py-0.5 text-xs text-gray-600 dark:text-gray-400"
            >
              {RESEARCH_AREA_LABELS[area] || area}
            </span>
          ))}
          {data.researchAreas.length > 4 && (
            <span className="text-xs text-gray-400">
              +{data.researchAreas.length - 4}
            </span>
          )}
        </div>
      )}

      <div className="mt-3 flex items-center text-sm text-purple-600 dark:text-purple-400 group-hover:underline">
        查看完整报告
        <svg className="w-4 h-4 ml-1 group-hover:translate-x-0.5 transition-transform" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
        </svg>
      </div>
    </Link>
  );
}

// ---------------------------------------------------------------------------
// 占位卡片（产品扫描 — 专题页尚未上线）
// ---------------------------------------------------------------------------

function BriefCardPlaceholder({
  icon, title, summary, count,
}: {
  icon: string; title: string; summary: string; count: number;
}) {
  return (
    <div className="block rounded-xl border border-gray-200 dark:border-gray-700 bg-gray-50 dark:bg-gray-800/20 p-5 opacity-60">
      <div className="flex items-center gap-2 mb-2">
        <span className="text-2xl">{icon}</span>
        <h3 className="text-lg font-semibold text-gray-900 dark:text-gray-100">{title}</h3>
        <span className="ml-auto text-xs text-gray-500">{count} 项</span>
      </div>
      <p className="text-sm text-gray-600 dark:text-gray-400 line-clamp-2">{summary}</p>
      <p className="text-xs text-gray-400 mt-3">专题报告即将上线</p>
    </div>
  );
}
