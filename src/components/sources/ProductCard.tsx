// ============================================================================
// ProductCard.tsx — AI 产品分析卡片
//
// 在 Source Detail 页面中，展示单篇产品的深度分析。
// 作为 ArticleCardSpecialized 的子卡片渲染。
// 使用橙色/琥珀色主题。
// ============================================================================

// ---------------------------------------------------------------------------
// 颜色映射
// ---------------------------------------------------------------------------

/** 发布上下文 Badge 颜色映射 */
const LAUNCH_CONTEXT_COLORS: Record<string, { bg: string; text: string }> = {
  new_launch: { bg: 'bg-orange-100 dark:bg-orange-900/30', text: 'text-orange-700 dark:text-orange-300' },
  major_update: { bg: 'bg-blue-100 dark:bg-blue-900/30', text: 'text-blue-700 dark:text-blue-300' },
  pivot: { bg: 'bg-yellow-100 dark:bg-yellow-900/30', text: 'text-yellow-700 dark:text-yellow-300' },
  funding_announcement: { bg: 'bg-green-100 dark:bg-green-900/30', text: 'text-green-700 dark:text-green-300' },
};

const LAUNCH_CONTEXT_LABELS: Record<string, string> = {
  new_launch: '新产品',
  major_update: '重大更新',
  pivot: '战略转型',
  funding_announcement: '融资发布',
};

/** 定价模式 Badge 颜色映射 */
const PRICING_MODEL_LABELS: Record<string, string> = {
  freemium: 'Freemium',
  subscription: '订阅制',
  usage_based: '按量计费',
  open_source: '开源',
  free: '免费',
  enterprise: '企业版',
  unknown: '未公布',
};

/** 创新程度 Badge 颜色映射 */
const INNOVATION_LEVEL_COLORS: Record<string, { bg: string; text: string }> = {
  breakthrough: { bg: 'bg-orange-100 dark:bg-orange-900/30', text: 'text-orange-700 dark:text-orange-300' },
  incremental: { bg: 'bg-blue-100 dark:bg-blue-900/30', text: 'text-blue-700 dark:text-blue-300' },
  me_too: { bg: 'bg-gray-100 dark:bg-gray-800', text: 'text-gray-600 dark:text-gray-400' },
};

const INNOVATION_LEVEL_LABELS: Record<string, string> = {
  breakthrough: '突破性',
  incremental: '渐进改进',
  me_too: '跟随型',
};

/** 增长信号 Badge 颜色映射 */
const GROWTH_SIGNALS_COLORS: Record<string, { bg: string; text: string }> = {
  strong: { bg: 'bg-green-100 dark:bg-green-900/30', text: 'text-green-700 dark:text-green-300' },
  moderate: { bg: 'bg-blue-100 dark:bg-blue-900/30', text: 'text-blue-700 dark:text-blue-300' },
  early: { bg: 'bg-yellow-100 dark:bg-yellow-900/30', text: 'text-yellow-700 dark:text-yellow-300' },
  unclear: { bg: 'bg-gray-100 dark:bg-gray-800', text: 'text-gray-600 dark:text-gray-400' },
};

const GROWTH_SIGNALS_LABELS: Record<string, string> = {
  strong: '强劲增长',
  moderate: '稳定增长',
  early: '早期阶段',
  unclear: '信号不明',
};

/** 用户情绪 Badge 颜色映射 */
const OVERALL_SENTIMENT_COLORS: Record<string, { bg: string; text: string }> = {
  overwhelmingly_positive: { bg: 'bg-green-100 dark:bg-green-900/30', text: 'text-green-700 dark:text-green-300' },
  mostly_positive: { bg: 'bg-emerald-100 dark:bg-emerald-900/30', text: 'text-emerald-700 dark:text-emerald-300' },
  mixed: { bg: 'bg-yellow-100 dark:bg-yellow-900/30', text: 'text-yellow-700 dark:text-yellow-300' },
  mostly_negative: { bg: 'bg-red-100 dark:bg-red-900/30', text: 'text-red-700 dark:text-red-300' },
};

const OVERALL_SENTIMENT_LABELS: Record<string, string> = {
  overwhelmingly_positive: '极度好评',
  mostly_positive: '多数好评',
  mixed: '褒贬不一',
  mostly_negative: '多数差评',
};

/** 差异化质量 Badge 颜色映射 */
const DIFFERENTIATION_COLORS: Record<string, { bg: string; text: string }> = {
  unique: { bg: 'bg-orange-100 dark:bg-orange-900/30', text: 'text-orange-700 dark:text-orange-300' },
  meaningful: { bg: 'bg-blue-100 dark:bg-blue-900/30', text: 'text-blue-700 dark:text-blue-300' },
  marginal: { bg: 'bg-yellow-100 dark:bg-yellow-900/30', text: 'text-yellow-700 dark:text-yellow-300' },
  none: { bg: 'bg-gray-100 dark:bg-gray-800', text: 'text-gray-600 dark:text-gray-400' },
};

const DIFFERENTIATION_LABELS: Record<string, string> = {
  unique: '独一无二',
  meaningful: '有意义的差异',
  marginal: '差异微小',
  none: '无明显差异',
};

/** PMF 信号 Badge 颜色映射 */
const PMF_SIGNAL_COLORS: Record<string, { bg: string; text: string }> = {
  strong_pmf: { bg: 'bg-green-100 dark:bg-green-900/30', text: 'text-green-700 dark:text-green-300' },
  finding_pmf: { bg: 'bg-blue-100 dark:bg-blue-900/30', text: 'text-blue-700 dark:text-blue-300' },
  too_early_to_tell: { bg: 'bg-yellow-100 dark:bg-yellow-900/30', text: 'text-yellow-700 dark:text-yellow-300' },
  no_signal: { bg: 'bg-gray-100 dark:bg-gray-800', text: 'text-gray-600 dark:text-gray-400' },
};

const PMF_SIGNAL_LABELS: Record<string, string> = {
  strong_pmf: '强 PMF',
  finding_pmf: '寻找 PMF',
  too_early_to_tell: '为时过早',
  no_signal: '暂无信号',
};

// ---------------------------------------------------------------------------
// 专题标注数据形状（匹配 Stage 2 管道输出的 snake_case 字段）
// ---------------------------------------------------------------------------

interface ProductTagsData {
  product_name: string;
  product_url: string;
  company_team?: string;
  launch_context: string;
  pricing_model: string;
  product_category: string;
  target_users?: string[];
}

// ---------------------------------------------------------------------------
// Props
// ---------------------------------------------------------------------------

interface ProductCardProps {
  /** Stage 2 specialized_tags.product */
  tags: ProductTagsData;
  /** Stage 3 产品分析结果（可能未运行） */
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  analysis?: Record<string, any>;
}

// ---------------------------------------------------------------------------
// 子组件
// ---------------------------------------------------------------------------

/**
 * 发布上下文 Badge。
 */
function LaunchContextBadge({ context }: { context: string }) {
  const colors = LAUNCH_CONTEXT_COLORS[context] || { bg: 'bg-gray-100 dark:bg-gray-800', text: 'text-gray-600 dark:text-gray-400' };
  const label = LAUNCH_CONTEXT_LABELS[context] || context;
  return (
    <span className={`inline-flex items-center rounded-full px-2 py-0.5 text-xs font-medium ${colors.bg} ${colors.text}`}>
      {label}
    </span>
  );
}

/**
 * 定价模式 Badge。
 */
function PricingModelBadge({ model }: { model: string }) {
  const label = PRICING_MODEL_LABELS[model] || model;
  return (
    <span className="inline-flex items-center rounded-full px-2 py-0.5 text-xs font-medium bg-amber-100 dark:bg-amber-900/30 text-amber-700 dark:text-amber-300">
      {label}
    </span>
  );
}

/**
 * 创新程度 Badge。
 */
function InnovationLevelBadge({ level }: { level: string }) {
  const colors = INNOVATION_LEVEL_COLORS[level] || { bg: 'bg-gray-100 dark:bg-gray-800', text: 'text-gray-600 dark:text-gray-400' };
  const label = INNOVATION_LEVEL_LABELS[level] || level;
  return (
    <span className={`inline-flex items-center rounded-full px-2 py-0.5 text-xs font-medium ${colors.bg} ${colors.text}`}>
      {label}
    </span>
  );
}

/**
 * 增长信号 Badge。
 */
function GrowthSignalsBadge({ signal }: { signal: string }) {
  const colors = GROWTH_SIGNALS_COLORS[signal] || { bg: 'bg-gray-100 dark:bg-gray-800', text: 'text-gray-600 dark:text-gray-400' };
  const label = GROWTH_SIGNALS_LABELS[signal] || signal;
  return (
    <span className={`inline-flex items-center rounded-full px-2 py-0.5 text-xs font-medium ${colors.bg} ${colors.text}`}>
      {label}
    </span>
  );
}

/**
 * 用户情绪 Badge。
 */
function SentimentBadge({ sentiment }: { sentiment: string }) {
  const colors = OVERALL_SENTIMENT_COLORS[sentiment] || { bg: 'bg-gray-100 dark:bg-gray-800', text: 'text-gray-600 dark:text-gray-400' };
  const label = OVERALL_SENTIMENT_LABELS[sentiment] || sentiment;
  return (
    <span className={`inline-flex items-center rounded-full px-2 py-0.5 text-xs font-medium ${colors.bg} ${colors.text}`}>
      {label}
    </span>
  );
}

/**
 * 差异化质量 Badge。
 */
function DifferentiationBadge({ quality }: { quality: string }) {
  const colors = DIFFERENTIATION_COLORS[quality] || { bg: 'bg-gray-100 dark:bg-gray-800', text: 'text-gray-600 dark:text-gray-400' };
  const label = DIFFERENTIATION_LABELS[quality] || quality;
  return (
    <span className={`inline-flex items-center rounded-full px-2 py-0.5 text-xs font-medium ${colors.bg} ${colors.text}`}>
      {label}
    </span>
  );
}

/**
 * PMF 信号 Badge。
 */
function PmfSignalBadge({ signal }: { signal: string }) {
  const colors = PMF_SIGNAL_COLORS[signal] || { bg: 'bg-gray-100 dark:bg-gray-800', text: 'text-gray-600 dark:text-gray-400' };
  const label = PMF_SIGNAL_LABELS[signal] || signal;
  return (
    <span className={`inline-flex items-center rounded-full px-2 py-0.5 text-xs font-medium ${colors.bg} ${colors.text}`}>
      {label}
    </span>
  );
}

// ---------------------------------------------------------------------------
// 主组件
// ---------------------------------------------------------------------------

/**
 * AI 产品分析卡片。
 *
 * 在 Source Detail 页面中，展示单款 AI 产品的深度分析，
 * 包括产品画像、定位、功能拆解、商业模式、用户反馈和市场评估。
 */
export function ProductCard({ tags, analysis }: ProductCardProps) {
  return (
    <div className="rounded-lg border border-gray-200 dark:border-gray-700 overflow-hidden">
      {/* 卡片标题栏 */}
      <div className="px-4 py-3 bg-orange-50/50 dark:bg-orange-950/20 border-b border-gray-200 dark:border-gray-700">
        <div className="flex items-center gap-2">
          <svg className="w-5 h-5 text-orange-600 dark:text-orange-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <path strokeLinecap="round" strokeLinejoin="round" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4" />
          </svg>
          <span className="text-sm font-semibold text-gray-800 dark:text-gray-200">
            产品分析
          </span>
          {/* 发布上下文 + 定价标签 */}
          {tags.launch_context && (
            <LaunchContextBadge context={tags.launch_context} />
          )}
          {tags.pricing_model && (
            <PricingModelBadge model={tags.pricing_model} />
          )}
        </div>
      </div>

      {/* 卡片正文 */}
      <div className="p-4 space-y-3">
        {/* 产品画像 */}
        <div>
          <div className="flex items-center gap-2 flex-wrap">
            <span className="text-base font-semibold text-gray-900 dark:text-gray-100">
              {tags.product_name}
            </span>
          </div>

          {/* 公司/团队 */}
          {tags.company_team && (
            <p className="text-xs text-gray-500 dark:text-gray-400 mt-1">
              {tags.company_team}
            </p>
          )}

          {/* 品类信息 */}
          <div className="flex items-center gap-3 mt-1 text-xs text-gray-400 dark:text-gray-500">
            {tags.product_category && (
              <span className="text-orange-600 dark:text-orange-400 font-medium">
                {tags.product_category}
              </span>
            )}
          </div>

          {/* 产品链接 */}
          {tags.product_url && (
            <a
              href={tags.product_url}
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center gap-1 mt-1 text-xs text-orange-600 dark:text-orange-400 hover:underline"
            >
              <svg className="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="2">
                <path strokeLinecap="round" strokeLinejoin="round" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
              </svg>
              访问产品
            </a>
          )}
        </div>

        {/* 产品定位（Stage 3 分析） */}
        {analysis?.positioning && (
          <div className="rounded-md bg-orange-50/50 dark:bg-orange-950/10 p-3 border border-orange-100 dark:border-orange-900/30">
            <div className="flex items-center gap-2 mb-1">
              <span className="text-xs font-medium text-orange-600 dark:text-orange-400">
                产品定位
              </span>
            </div>
            {analysis.positioning.value_proposition && (
              <p className="text-sm text-gray-700 dark:text-gray-300">
                {analysis.positioning.value_proposition}
              </p>
            )}
            {analysis.positioning.target_users?.length > 0 && (
              <div className="flex flex-wrap gap-1 mt-1">
                {analysis.positioning.target_users.map((user: string) => (
                  <span
                    key={user}
                    className="inline-flex items-center rounded bg-orange-100 dark:bg-orange-900/20 px-2 py-0.5 text-xs text-orange-700 dark:text-orange-300"
                  >
                    {user}
                  </span>
                ))}
              </div>
            )}
            {analysis.positioning.core_jobs_to_be_done?.length > 0 && (
              <div className="mt-1">
                <span className="text-xs text-gray-400">JTBD: </span>
                <span className="text-xs text-gray-600 dark:text-gray-400">
                  {analysis.positioning.core_jobs_to_be_done.join('; ')}
                </span>
              </div>
            )}
            {analysis.positioning.competitive_positioning && (
              <p className="text-xs text-gray-500 dark:text-gray-400 mt-1">
                {analysis.positioning.competitive_positioning}
              </p>
            )}
          </div>
        )}

        {/* 功能拆解（Stage 3 分析） */}
        {analysis?.feature_breakdown && (
          <div className="rounded-md bg-amber-50/50 dark:bg-amber-950/10 p-3 border border-amber-100 dark:border-amber-900/30">
            <div className="flex items-center gap-2 mb-1">
              <span className="text-xs font-medium text-amber-600 dark:text-amber-400">
                功能拆解
              </span>
            </div>
            {/* 核心功能 */}
            {analysis.feature_breakdown.core_features?.length > 0 && (
              <ul className="space-y-1.5">
                {analysis.feature_breakdown.core_features.map((feat: { name: string; description: string; innovation_level: string }, i: number) => (
                  <li key={i} className="flex items-start gap-2">
                    <span className="text-amber-400 mt-0.5 text-xs">+</span>
                    <div>
                      <div className="flex items-center gap-1.5">
                        <span className="text-sm font-medium text-gray-700 dark:text-gray-300">
                          {feat.name}
                        </span>
                        {feat.innovation_level && (
                          <InnovationLevelBadge level={feat.innovation_level} />
                        )}
                      </div>
                      {feat.description && (
                        <p className="text-xs text-gray-500 dark:text-gray-400 mt-0.5">
                          {feat.description}
                        </p>
                      )}
                    </div>
                  </li>
                ))}
              </ul>
            )}
            {/* UX 亮点 */}
            {analysis.feature_breakdown.ux_highlights?.length > 0 && (
              <div className="mt-2">
                <span className="text-xs text-gray-400">体验亮点: </span>
                <span className="text-xs text-gray-600 dark:text-gray-400">
                  {analysis.feature_breakdown.ux_highlights.join('; ')}
                </span>
              </div>
            )}
            {/* UX 痛点 */}
            {analysis.feature_breakdown.ux_pain_points?.length > 0 && (
              <div className="mt-1">
                <span className="text-xs text-gray-400">体验痛点: </span>
                <span className="text-xs text-red-600 dark:text-red-400">
                  {analysis.feature_breakdown.ux_pain_points.join('; ')}
                </span>
              </div>
            )}
          </div>
        )}

        {/* 商业模式分析（Stage 3 分析） */}
        {analysis?.business_model_analysis && (
          <div className="rounded-md bg-green-50/50 dark:bg-green-950/10 p-3 border border-green-100 dark:border-green-900/30">
            <div className="flex items-center gap-2 mb-1">
              <span className="text-xs font-medium text-green-600 dark:text-green-400">
                商业模式
              </span>
              {analysis.business_model_analysis.growth_signals && (
                <GrowthSignalsBadge signal={analysis.business_model_analysis.growth_signals} />
              )}
            </div>
            {analysis.business_model_analysis.revenue_model && (
              <p className="text-sm text-gray-700 dark:text-gray-300">
                <span className="text-gray-400 text-xs">收入模式: </span>
                {analysis.business_model_analysis.revenue_model}
              </p>
            )}
            {analysis.business_model_analysis.unit_economics_indicators && (
              <p className="text-xs text-gray-500 dark:text-gray-400 mt-1">
                <span className="text-gray-400">单位经济学: </span>
                {analysis.business_model_analysis.unit_economics_indicators}
              </p>
            )}
            {analysis.business_model_analysis.defensibility && (
              <p className="text-xs text-gray-500 dark:text-gray-400 mt-1">
                <span className="text-gray-400">壁垒: </span>
                {analysis.business_model_analysis.defensibility}
              </p>
            )}
          </div>
        )}

        {/* 用户反馈 + 市场评估（双列布局） */}
        {(analysis?.user_sentiment_synthesis || analysis?.market_assessment) && (
          <div className="grid grid-cols-2 gap-3">
            {/* 用户反馈 */}
            {analysis?.user_sentiment_synthesis && (
              <div className="rounded-md bg-gray-50 dark:bg-gray-800/30 p-3">
                <div className="flex items-center gap-2 mb-1">
                  <span className="text-xs font-medium text-gray-500 dark:text-gray-400">
                    用户反馈
                  </span>
                  {analysis.user_sentiment_synthesis.overall_sentiment && (
                    <SentimentBadge sentiment={analysis.user_sentiment_synthesis.overall_sentiment} />
                  )}
                </div>
                <div className="text-xs text-gray-600 dark:text-gray-400 space-y-1">
                  {analysis.user_sentiment_synthesis.praise_themes?.length > 0 && (
                    <div>
                      <span className="text-green-500">好评: </span>
                      {analysis.user_sentiment_synthesis.praise_themes.slice(0, 3).join('; ')}
                    </div>
                  )}
                  {analysis.user_sentiment_synthesis.complaint_themes?.length > 0 && (
                    <div>
                      <span className="text-red-500">差评: </span>
                      {analysis.user_sentiment_synthesis.complaint_themes.slice(0, 3).join('; ')}
                    </div>
                  )}
                </div>
                {/* 代表性评论 */}
                {analysis.user_sentiment_synthesis.key_user_quotes?.length > 0 && (
                  <div className="mt-2 space-y-1">
                    {analysis.user_sentiment_synthesis.key_user_quotes.slice(0, 2).map((quote: string, i: number) => (
                      <p key={i} className="text-xs text-gray-400 italic">
                        &ldquo;{quote}&rdquo;
                      </p>
                    ))}
                  </div>
                )}
              </div>
            )}

            {/* 市场评估 */}
            {analysis?.market_assessment && (
              <div className="rounded-md bg-gray-50 dark:bg-gray-800/30 p-3">
                <div className="flex items-center gap-2 mb-1">
                  <span className="text-xs font-medium text-gray-500 dark:text-gray-400">
                    市场评估
                  </span>
                </div>
                <div className="text-xs text-gray-600 dark:text-gray-400 space-y-1">
                  {analysis.market_assessment.category && (
                    <div>品类: {analysis.market_assessment.category}</div>
                  )}
                  {analysis.market_assessment.key_competitors?.length > 0 && (
                    <div>
                      竞品: {analysis.market_assessment.key_competitors.slice(0, 3).join(', ')}
                    </div>
                  )}
                </div>
                {/* 差异化 + PMF 标签 */}
                <div className="mt-2 flex flex-wrap gap-1">
                  {analysis.market_assessment.differentiation_quality && (
                    <DifferentiationBadge quality={analysis.market_assessment.differentiation_quality} />
                  )}
                  {analysis.market_assessment.pmf_signal && (
                    <PmfSignalBadge signal={analysis.market_assessment.pmf_signal} />
                  )}
                </div>
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
}
