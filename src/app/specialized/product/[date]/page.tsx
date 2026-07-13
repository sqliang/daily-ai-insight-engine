// ============================================================================
// /specialized/product/[date] — 产品扫描专题报告页
//
// 展示指定日期的 AI 产品分析结果。
// ============================================================================

import Link from 'next/link';
import { loadProductArticles } from '@/lib/data/specialized';
import type { ProductEntry } from '@/lib/data/specialized';
import { PageShell } from '@/components/layout/PageShell';

export const dynamic = 'force-dynamic';

interface Props {
  params: Promise<{ date: string }>;
}

export default async function ProductSpecializedPage({ params }: Props) {
  const { date } = await params;

  const products = await loadProductArticles(date);

  // 当日无数据 → 空状态页
  if (products.length === 0) {
    return (
      <PageShell>
        <div className="py-20 text-center">
          <h1 className="text-2xl font-bold text-gray-900 dark:text-gray-100 mb-4">
            {date} 产品扫描专题报告
          </h1>
          <p className="text-gray-500 dark:text-gray-400">
            当日没有产品数据。
          </p>
          <Link href="/dashboard" className="text-blue-600 hover:underline mt-4 inline-block">
            ← 回到日报列表
          </Link>
        </div>
      </PageShell>
    );
  }

  return (
    <PageShell>
      {/* Hero Banner */}
      <div className="mb-8 p-6 rounded-xl bg-gradient-to-br from-orange-50 to-amber-50 dark:from-orange-950/30 dark:to-amber-950/30 border border-orange-200 dark:border-orange-800">
        <Link
          href={`/dashboard/${date}`}
          className="text-sm text-orange-600 dark:text-orange-400 hover:underline mb-2 inline-block"
        >
          ← 回到日报
        </Link>
        <h1 className="text-2xl font-bold text-gray-900 dark:text-gray-100 mt-2">
          {date} 产品扫描专题报告
        </h1>
        <p className="text-gray-600 dark:text-gray-400 mt-1">
          共 {products.length} 个产品
        </p>
      </div>

      {/* 产品列表 */}
      <div className="space-y-4">
        {products.map((product) => (
          <ProductCardItem key={product.articleId} product={product} date={date} />
        ))}
      </div>
    </PageShell>
  );
}

// ---------------------------------------------------------------------------
// 产品卡片子组件（列表项渲染）
// ---------------------------------------------------------------------------

function ProductCardItem({ product }: { product: ProductEntry; date: string }) {
  // 检查是否有 Stage 3 产品分析数据
  const hasAnalysis = !!product.productAssessment;

  return (
    <Link
      href={product.productUrl || `/sources/producthunt`}
      className="block rounded-lg border border-gray-200 dark:border-gray-700 p-4 hover:border-orange-300 dark:hover:border-orange-700 transition-colors"
    >
      <div className="flex items-start justify-between gap-4">
        <div className="min-w-0 flex-1">
          {/* 产品名称 + 分类标签 */}
          <div className="flex items-center gap-2 flex-wrap mb-1">
            <h3 className="text-base font-semibold text-gray-900 dark:text-gray-100 truncate">
              {product.productName || product.title}
            </h3>
            {product.launchContext && (
              <LaunchContextPill context={product.launchContext} />
            )}
            {product.pricingModel && (
              <PricingPill model={product.pricingModel} />
            )}
          </div>

          {/* 公司信息 */}
          {product.companyTeam && (
            <p className="text-xs text-gray-500 dark:text-gray-400 mt-0.5">
              {product.companyTeam}
              {product.productCategory && (
                <span className="ml-2 text-orange-600 dark:text-orange-400">
                  {product.productCategory}
                </span>
              )}
            </p>
          )}

          {/* 价值主张摘要 */}
          {hasAnalysis && product.productAssessment?.positioning?.valueProposition && (
            <p className="mt-2 text-sm text-gray-700 dark:text-gray-300">
              <span className="text-orange-500 dark:text-orange-400 font-medium">价值主张: </span>
              {product.productAssessment.positioning.valueProposition}
            </p>
          )}

          {/* 核心功能预览 */}
          {hasAnalysis && (product.productAssessment?.featureBreakdown?.coreFeatures?.length > 0) && (
            <div className="mt-2 flex flex-wrap gap-1">
              {product.productAssessment?.featureBreakdown?.coreFeatures
                .slice(0, 3)
                .map((f: { name: string; innovationLevel: string }) => (
                  <span
                    key={f.name}
                    className="inline-flex items-center rounded bg-amber-50 dark:bg-amber-900/20 px-2 py-0.5 text-xs text-amber-700 dark:text-amber-400"
                  >
                    {f.name}
                    {f.innovationLevel === 'breakthrough' && ' ★'}
                  </span>
                ))}
            </div>
          )}

          {/* 用户情绪 + PMF 信号 */}
          {hasAnalysis && (
            <div className="mt-2 flex flex-wrap items-center gap-2 text-xs">
              {product.productAssessment?.userSentimentSynthesis?.overallSentiment && (
                <SentimentLabel sentiment={product.productAssessment.userSentimentSynthesis.overallSentiment} />
              )}
              {product.productAssessment?.marketAssessment?.pmfSignal && (
                <PmfLabel signal={product.productAssessment.marketAssessment.pmfSignal} />
              )}
              {product.productAssessment?.businessModelAnalysis?.growthSignals && (
                <GrowthLabel signal={product.productAssessment.businessModelAnalysis.growthSignals} />
              )}
            </div>
          )}

          {/* TLDR 回退（无 Stage 3 分析时显示） */}
          {!hasAnalysis && product.tldr && (
            <p className="mt-2 text-xs text-gray-500 dark:text-gray-400 line-clamp-2">
              {product.tldr}
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

// ---------------------------------------------------------------------------
// 子组件 Inline Badges
// ---------------------------------------------------------------------------

const LAUNCH_CONTEXT_LABELS: Record<string, string> = {
  new_launch: '新产品',
  major_update: '重大更新',
  pivot: '战略转型',
  funding_announcement: '融资发布',
};

const PRICING_LABELS: Record<string, string> = {
  freemium: 'Freemium',
  subscription: '订阅制',
  usage_based: '按量计费',
  open_source: '开源',
  free: '免费',
  enterprise: '企业版',
  unknown: '未公布',
};

const SENTIMENT_LABELS: Record<string, string> = {
  overwhelmingly_positive: '极度好评',
  mostly_positive: '多数好评',
  mixed: '褒贬不一',
  mostly_negative: '多数差评',
};

const PMF_LABELS: Record<string, string> = {
  strong_pmf: '强 PMF',
  finding_pmf: '寻找 PMF',
  too_early_to_tell: '为时过早',
  no_signal: '暂无信号',
};

const GROWTH_LABELS: Record<string, string> = {
  strong: '强劲增长',
  moderate: '稳定增长',
  early: '早期阶段',
  unclear: '信号不明',
};

function LaunchContextPill({ context }: { context: string }) {
  const label = LAUNCH_CONTEXT_LABELS[context] || context;
  return (
    <span className="inline-flex items-center rounded-full bg-orange-100 dark:bg-orange-900/30 px-2 py-0.5 text-xs font-medium text-orange-700 dark:text-orange-300">
      {label}
    </span>
  );
}

function PricingPill({ model }: { model: string }) {
  const label = PRICING_LABELS[model] || model;
  return (
    <span className="inline-flex items-center rounded-full bg-amber-100 dark:bg-amber-900/30 px-2 py-0.5 text-xs font-medium text-amber-700 dark:text-amber-300">
      {label}
    </span>
  );
}

function SentimentLabel({ sentiment }: { sentiment: string }) {
  const label = SENTIMENT_LABELS[sentiment] || sentiment;
  const color =
    sentiment === 'overwhelmingly_positive' || sentiment === 'mostly_positive'
      ? 'text-green-600 dark:text-green-400'
      : sentiment === 'mixed'
        ? 'text-yellow-600 dark:text-yellow-400'
        : 'text-red-600 dark:text-red-400';
  return <span className={`text-xs ${color}`}>{label}</span>;
}

function PmfLabel({ signal }: { signal: string }) {
  const label = PMF_LABELS[signal] || signal;
  const color =
    signal === 'strong_pmf'
      ? 'text-green-600 dark:text-green-400'
      : signal === 'finding_pmf'
        ? 'text-blue-600 dark:text-blue-400'
        : 'text-gray-400';
  return <span className={`text-xs ${color}`}>{label}</span>;
}

function GrowthLabel({ signal }: { signal: string }) {
  const label = GROWTH_LABELS[signal] || signal;
  const color =
    signal === 'strong'
      ? 'text-green-600 dark:text-green-400'
      : signal === 'moderate'
        ? 'text-blue-600 dark:text-blue-400'
        : 'text-gray-400';
  return <span className={`text-xs ${color}`}>{label}</span>;
}
