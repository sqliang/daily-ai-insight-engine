// ============================================================================
// /specialized/github/[date] — GitHub 开源项目专题报告页
//
// 展示指定日期的 GitHub Trending 项目分析结果。
// 支持按领域和 AI 子领域筛选。
// ============================================================================

import Link from 'next/link';
import {
  loadGithubArticles,
  computeDomainDistribution,
  computeAiCategoryDistribution,
} from '@/lib/data/specialized';
import type { GithubProjectEntry } from '@/lib/data/specialized';
import { PageShell } from '@/components/layout/PageShell';
import { DOMAIN_LABELS, DOMAIN_COLORS, DOMAIN_LIST } from '@/components/sources/GitHubProjectCard';

export const dynamic = 'force-dynamic';

interface Props {
  params: Promise<{ date: string }>;
  searchParams: Promise<{ domain?: string }>;
}

export default async function GithubSpecializedPage({ params, searchParams }: Props) {
  const { date } = await params;
  const { domain: filterDomain } = await searchParams;

  const projects = await loadGithubArticles(date);

  // 当日无数据 → 空状态页
  if (projects.length === 0) {
    return (
      <PageShell>
        <div className="py-20 text-center">
          <h1 className="text-2xl font-bold text-gray-900 dark:text-gray-100 mb-4">
            {date} GitHub 项目专题报告
          </h1>
          <p className="text-gray-500 dark:text-gray-400">
            当日没有 GitHub Trending 数据。
          </p>
          <Link href="/dashboard" className="text-blue-600 hover:underline mt-4 inline-block">
            ← 回到日报列表
          </Link>
        </div>
      </PageShell>
    );
  }

  // 按领域筛选
  const filtered = filterDomain
    ? projects.filter((p) => p.domain === filterDomain)
    : projects;

  const domainDist = computeDomainDistribution(projects);
  const aiCatDist = computeAiCategoryDistribution(projects);

  return (
    <PageShell>
      {/* Hero Banner */}
      <div className="mb-8 p-6 rounded-xl bg-gradient-to-br from-purple-50 to-indigo-50 dark:from-purple-950/30 dark:to-indigo-950/30 border border-purple-200 dark:border-purple-800">
        <Link
          href={`/dashboard/${date}`}
          className="text-sm text-purple-600 dark:text-purple-400 hover:underline mb-2 inline-block"
        >
          ← 回到日报
        </Link>
        <h1 className="text-2xl font-bold text-gray-900 dark:text-gray-100 mt-2">
          {date} GitHub 开源项目专题报告
        </h1>
        <p className="text-gray-600 dark:text-gray-400 mt-1">
          共 {projects.length} 个项目 · {Object.keys(domainDist).length} 个领域
        </p>

        {/* 领域筛选标签 */}
        <div className="mt-4 flex flex-wrap gap-1">
          {DOMAIN_LIST.filter((d) => domainDist[d]).map((d) => {
            const colors = DOMAIN_COLORS[d] || DOMAIN_COLORS.other;
            const label = DOMAIN_LABELS[d] || d;
            const count = domainDist[d];
            const isActive = filterDomain === d;
            return (
              <Link
                key={d}
                href={isActive ? `/specialized/github/${date}` : `?domain=${d}`}
                className={`inline-flex items-center gap-1 rounded-full px-2.5 py-1 text-xs font-medium transition-colors ${
                  isActive
                    ? 'ring-2 ring-purple-400 ' + colors.bg + ' ' + colors.text
                    : colors.bg + ' ' + colors.text + ' hover:opacity-80'
                }`}
              >
                {label} ({count})
              </Link>
            );
          })}
        </div>

        {/* AI 子领域分布（条件显示） */}
        {Object.keys(aiCatDist).length > 0 && (
          <div className="mt-2 flex flex-wrap gap-1">
            <span className="text-xs text-gray-400 mr-1">AI 子领域:</span>
            {Object.entries(aiCatDist).sort((a, b) => b[1] - a[1]).map(([cat, count]) => (
              <span
                key={cat}
                className="inline-flex items-center rounded-full bg-purple-100 dark:bg-purple-900/30 px-2 py-0.5 text-xs text-purple-700 dark:text-purple-300"
              >
                {cat.replace(/_/g, ' ')} ({count})
              </span>
            ))}
          </div>
        )}
      </div>

      {/* 项目列表 */}
      <div className="space-y-4">
        {filtered.map((project) => (
          <ProjectCard key={project.articleId} project={project} date={date} />
        ))}
      </div>

      {/* 筛选后无结果 */}
      {filtered.length === 0 && (
        <p className="text-center text-gray-500 py-12">该领域下暂无项目。</p>
      )}
    </PageShell>
  );
}

// ---------------------------------------------------------------------------
// 项目卡片子组件
// ---------------------------------------------------------------------------

function ProjectCard({ project, date }: { project: GithubProjectEntry; date: string }) {
  const colors = DOMAIN_COLORS[project.domain] || DOMAIN_COLORS.other;
  const domainLabel = DOMAIN_LABELS[project.domain] || project.domain;

  // 检查是否有 Stage 3 分析数据
  const hasAnalysis = !!project.techAssessment?.techStackQuality;

  return (
    <Link
      href={`/sources/github-trending`}
      className="block rounded-lg border border-gray-200 dark:border-gray-700 p-4 hover:border-purple-300 dark:hover:border-purple-700 transition-colors"
    >
      <div className="flex items-start justify-between gap-4">
        <div className="min-w-0 flex-1">
          {/* 项目名 + 领域标签 */}
          <div className="flex items-center gap-2 flex-wrap mb-1">
            <h3 className="text-base font-semibold text-gray-900 dark:text-gray-100 truncate">
              {project.projectName || project.title}
            </h3>
            <span
              className={`inline-flex items-center rounded-full px-2 py-0.5 text-xs font-medium ${colors.bg} ${colors.text}`}
            >
              {domainLabel}
            </span>
          </div>

          {/* 元信息 */}
          <div className="flex items-center gap-3 text-xs text-gray-500 dark:text-gray-400">
            {project.primaryLanguage && (
              <span className="font-mono">{project.primaryLanguage}</span>
            )}
            {project.licenseType && <span>{project.licenseType}</span>}
          </div>

          {/* 技术评价摘要 */}
          {hasAnalysis && (
            <div className="mt-2 flex items-center gap-3 text-sm">
              {project.techAssessment?.techStackQuality && (
                <span className="text-gray-700 dark:text-gray-300">
                  技术栈: {project.techAssessment.techStackQuality}
                </span>
              )}
              {project.communityHealth?.contributorActivity && (
                <span className="text-gray-500 dark:text-gray-400">
                  社区: {project.communityHealth.contributorActivity}
                </span>
              )}
              {project.adoptionGuidance?.timeToProduction && (
                <span className="text-gray-500 dark:text-gray-400">
                  投产: {project.adoptionGuidance.timeToProduction}
                </span>
              )}
            </div>
          )}

          {/* 采用建议 */}
          {(project.adoptionGuidance?.recommendedFor?.length ?? 0) > 0 && (
            <div className="mt-2 flex flex-wrap gap-1">
              {project.adoptionGuidance?.recommendedFor?.slice(0, 3).map((rec) => (
                <span
                  key={rec}
                  className="inline-flex items-center rounded bg-green-50 dark:bg-green-900/20 px-2 py-0.5 text-xs text-green-700 dark:text-green-400"
                >
                  ✓ {rec}
                </span>
              ))}
            </div>
          )}
        </div>

        {/* 箭头指示 */}
        <svg className="w-5 h-5 text-gray-400 flex-shrink-0 mt-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
        </svg>
      </div>
    </Link>
  );
}
