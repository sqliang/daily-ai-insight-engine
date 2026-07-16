// ============================================================================
// src/app/specialized/paper/[date]/page.tsx — 论文洞察页
//
// 展示基于 Stage 2 specialized_tags.paper 与 Stage 3 paper_assessment 识别的
// AI 论文分析结果，是”专题洞察”三页面之一。
// 目前直接从 all_articles.json 加载论文文章并做领域分布统计；待 Stage 4b 论文简报
//（specializedBrief.paperHighlights 或 paperInsights）稳定后，可迁移到与
// 项目 / 产品页面一致的日报 JSON 读取模式。
//
// 设计理由：
//   论文洞察需要展示每篇论文的元数据、研究问题、方法创新、实验严谨度等细粒度信息，
//   当前由 Stage 2/3 直接写入文章 frontmatter，因此页面直接读取 all_articles.json。
//   未来演进为 paperInsights 后，可复用 SpecializedReportHero 等组件做更聚合的展示。
// ============================================================================

import Link from 'next/link';
import {
  loadPaperArticles,
  computeResearchAreaDistribution,
  RESEARCH_AREA_LIST,
} from '@/lib/data/specialized';
import type { PaperEntry } from '@/lib/data/specialized';
import { RESEARCH_AREA_LABELS, RESEARCH_AREA_COLORS } from '@/components/sources/PaperCard';
import { PageShell } from '@/components/layout/PageShell';

export const dynamic = 'force-dynamic';

interface Props {
  params: Promise<{ date: string }>;
  searchParams: Promise<{ area?: string }>;
}

export default async function PaperSpecializedPage({ params, searchParams }: Props) {
  const { date } = await params;
  const { area: filterArea } = await searchParams;

  const papers = await loadPaperArticles(date);

  // 当日无数据 → 空状态页
  if (papers.length === 0) {
    return (
      <PageShell>
        <div className="rounded-xl border border-line bg-panel p-8 text-center shadow-sm">
          <Link
            href={`/dashboard/${date}`}
            className="mb-5 inline-flex items-center gap-1.5 text-xs font-medium text-muted transition-colors hover:text-accent focus:outline-none focus-visible:ring-2 focus-visible:ring-accent"
          >
            <svg
              className="h-3.5 w-3.5"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              strokeWidth="2"
              strokeLinecap="round"
              strokeLinejoin="round"
              aria-hidden="true"
            >
              <path d="m15 18-6-6 6-6" />
            </svg>
            回到日报
          </Link>
          <p className="text-[11px] font-medium uppercase tracking-[0.22em] text-accent">
            Specialized Brief
          </p>
          <h1 className="mt-2 text-2xl font-bold text-foreground">
            论文速递
          </h1>
          <p className="mx-auto mt-3 max-w-xl text-sm leading-7 text-muted/75">
            {date} 暂无可展示的论文洞察简报。Paper 洞察入口当前保持关闭，后续恢复后会在这里展示当日研究摘要。
          </p>
        </div>
      </PageShell>
    );
  }

  // 按研究领域筛选
  const filtered = filterArea
    ? papers.filter((p) => p.researchArea === filterArea)
    : papers;

  const areaDist = computeResearchAreaDistribution(papers);

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
          {date} 论文速递洞察报告
        </h1>
        <p className="text-gray-600 dark:text-gray-400 mt-1">
          共 {papers.length} 篇论文 · {Object.keys(areaDist).length} 个研究领域
        </p>

        {/* 研究领域筛选标签 */}
        <div className="mt-4 flex flex-wrap gap-1">
          {RESEARCH_AREA_LIST.filter((d) => areaDist[d]).map((d) => {
            const colors = RESEARCH_AREA_COLORS[d] || RESEARCH_AREA_COLORS.unknown;
            const label = RESEARCH_AREA_LABELS[d] || d;
            const count = areaDist[d];
            const isActive = filterArea === d;
            return (
              <Link
                key={d}
                href={isActive ? `/specialized/paper/${date}` : `?area=${d}`}
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
      </div>

      {/* 论文列表 */}
      <div className="space-y-4">
        {filtered.map((paper) => (
          <PaperCardItem key={paper.articleId} paper={paper} date={date} />
        ))}
      </div>

      {/* 筛选后无结果 */}
      {filtered.length === 0 && (
        <p className="text-center text-gray-500 py-12">该领域下暂无论文。</p>
      )}
    </PageShell>
  );
}

// ---------------------------------------------------------------------------
// 论文卡片子组件（列表项渲染）
// ---------------------------------------------------------------------------

function PaperCardItem({ paper, date: _date }: { paper: PaperEntry; date: string }) {
  const areaColors = RESEARCH_AREA_COLORS[paper.researchArea] || RESEARCH_AREA_COLORS.unknown;
  const areaLabel = RESEARCH_AREA_LABELS[paper.researchArea] || paper.researchArea;

  // 检查是否有 Stage 3 论文分析数据
  const hasAnalysis = !!paper.researchProblem;

  return (
    <Link
      href={`/sources/arxiv-cs-ai`}
      className="block rounded-lg border border-gray-200 dark:border-gray-700 p-4 hover:border-purple-300 dark:hover:border-purple-700 transition-colors"
    >
      <div className="flex items-start justify-between gap-4">
        <div className="min-w-0 flex-1">
          {/* 论文标题 + 研究领域标签 */}
          <div className="flex items-center gap-2 flex-wrap mb-1">
            <h3 className="text-base font-semibold text-gray-900 dark:text-gray-100 truncate">
              {paper.paperTitle || paper.title}
            </h3>
            <span
              className={`inline-flex items-center rounded-full px-2 py-0.5 text-xs font-medium ${areaColors.bg} ${areaColors.text}`}
            >
              {areaLabel}
            </span>
          </div>

          {/* 作者信息 */}
          {paper.authors.length > 0 && (
            <p className="text-xs text-gray-500 dark:text-gray-400 mt-0.5 truncate">
              {paper.authors.slice(0, 4).join(', ')}
              {paper.authors.length > 4 && ` 等 ${paper.authors.length} 位`}
            </p>
          )}

          {/* 元信息 */}
          <div className="flex items-center gap-3 mt-1 text-xs text-gray-400 dark:text-gray-500">
            {paper.venue && <span>{paper.venue}</span>}
            {paper.methodType && (
              <span className="font-mono text-purple-600 dark:text-purple-400">
                {paper.methodType}
              </span>
            )}
            {(paper.codeUrl || paper.datasetUrl) && (
              <span className="text-purple-500 dark:text-purple-400">
                {[
                  paper.codeUrl ? '附带代码' : '',
                  paper.datasetUrl ? '附带数据集' : '',
                ].filter(Boolean).join(' · ')}
              </span>
            )}
          </div>

          {/* 研究方法分析摘要 */}
          {hasAnalysis && (
            <div className="mt-2 space-y-1">
              {/* 核心问题 */}
              {paper.researchProblem?.coreQuestion && (
                <p className="text-sm text-gray-700 dark:text-gray-300">
                  <span className="text-purple-500 dark:text-purple-400 font-medium">核心问题: </span>
                  {paper.researchProblem.coreQuestion}
                </p>
              )}
              {/* 方法概述 */}
              {paper.methodology?.approachSummary && (
                <p className="text-xs text-gray-500 dark:text-gray-400 line-clamp-2">
                  {paper.methodology.approachSummary}
                </p>
              )}
            </div>
          )}

          {/* 实验与工业落地摘要 */}
          {hasAnalysis && (
            <div className="mt-2 flex flex-wrap items-center gap-2 text-xs">
              {paper.experimentalRigor?.baselineComparison && (
                <span className="text-gray-500 dark:text-gray-400">
                  基线: {paper.experimentalRigor.baselineComparison.replace(/_/g, ' ')}
                </span>
              )}
              {paper.industrialRelevance?.computeRequirements && (
                <span className="text-gray-500 dark:text-gray-400">
                  算力: {paper.industrialRelevance.computeRequirements.replace(/_/g, ' ')}
                </span>
              )}
              {paper.industrialRelevance?.integrationReadiness && (
                <span className="text-gray-500 dark:text-gray-400">
                  集成就绪: {paper.industrialRelevance.integrationReadiness.replace(/_/g, ' ')}
                </span>
              )}
            </div>
          )}

          {/* TLDR 回退（无 Stage 3 分析时显示） */}
          {!hasAnalysis && paper.tldr && (
            <p className="mt-2 text-xs text-gray-500 dark:text-gray-400 line-clamp-2">
              {paper.tldr}
            </p>
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
