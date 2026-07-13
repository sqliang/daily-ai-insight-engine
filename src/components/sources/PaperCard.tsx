// ============================================================================
// PaperCard.tsx — 学术论文分析卡片
//
// 在 Source Detail 页面中，展示单篇论文的深度分析。
// 作为 ArticleCardSpecialized 的子卡片渲染。
// ============================================================================

import type { AiDetail } from '@/lib/data/status';

// ---------------------------------------------------------------------------
// 研究领域颜色映射
// ---------------------------------------------------------------------------

export const RESEARCH_AREA_COLORS: Record<string, { bg: string; text: string }> = {
  nlp: { bg: 'bg-indigo-100 dark:bg-indigo-900/30', text: 'text-indigo-700 dark:text-indigo-300' },
  cv: { bg: 'bg-rose-100 dark:bg-rose-900/30', text: 'text-rose-700 dark:text-rose-300' },
  rl: { bg: 'bg-amber-100 dark:bg-amber-900/30', text: 'text-amber-700 dark:text-amber-300' },
  multimodal: { bg: 'bg-violet-100 dark:bg-violet-900/30', text: 'text-violet-700 dark:text-violet-300' },
  generative: { bg: 'bg-fuchsia-100 dark:bg-fuchsia-900/30', text: 'text-fuchsia-700 dark:text-fuchsia-300' },
  agent: { bg: 'bg-blue-100 dark:bg-blue-900/30', text: 'text-blue-700 dark:text-blue-300' },
  reasoning: { bg: 'bg-cyan-100 dark:bg-cyan-900/30', text: 'text-cyan-700 dark:text-cyan-300' },
  efficiency: { bg: 'bg-emerald-100 dark:bg-emerald-900/30', text: 'text-emerald-700 dark:text-emerald-300' },
  security: { bg: 'bg-red-100 dark:bg-red-900/30', text: 'text-red-700 dark:text-red-300' },
  robotics: { bg: 'bg-orange-100 dark:bg-orange-900/30', text: 'text-orange-700 dark:text-orange-300' },
  systems: { bg: 'bg-teal-100 dark:bg-teal-900/30', text: 'text-teal-700 dark:text-teal-300' },
  theory: { bg: 'bg-gray-100 dark:bg-gray-800', text: 'text-gray-700 dark:text-gray-300' },
  applications: { bg: 'bg-lime-100 dark:bg-lime-900/30', text: 'text-lime-700 dark:text-lime-300' },
  other: { bg: 'bg-gray-100 dark:bg-gray-800', text: 'text-gray-600 dark:text-gray-400' },
  unknown: { bg: 'bg-gray-100 dark:bg-gray-800', text: 'text-gray-600 dark:text-gray-400' },
};

export const RESEARCH_AREA_LABELS: Record<string, string> = {
  nlp: 'NLP',
  cv: 'CV',
  rl: 'RL',
  multimodal: '多模态',
  generative: '生成式',
  agent: 'Agent',
  reasoning: '推理',
  efficiency: '效率优化',
  security: '安全对齐',
  robotics: '机器人',
  systems: '系统',
  theory: '理论',
  applications: '应用',
  other: '其他',
  unknown: '其他',
};

// ---------------------------------------------------------------------------
// 专题标注数据形状（匹配 Stage 2 管道输出的 snake_case 字段）
// ---------------------------------------------------------------------------

interface PaperTagsData {
  paper_title: string;
  authors: string[];
  affiliations: string[];
  venue?: string;
  code_url?: string;
  dataset_url?: string;
  research_area: string;
  method_type: string;
  aiDetail?: AiDetail | null;
}

// ---------------------------------------------------------------------------
// Props
// ---------------------------------------------------------------------------

interface PaperCardProps {
  /** Stage 2 specialized_tags.paper */
  tags: PaperTagsData;
  /** Stage 3 论文分析结果（可能未运行） */
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  analysis?: Record<string, any>;
}

// ---------------------------------------------------------------------------
// 子组件
// ---------------------------------------------------------------------------

/**
 * 研究领域标签 Pill。
 * 根据领域 key 映射颜色和中文标签。
 */
function ResearchAreaPill({ area }: { area: string }) {
  const colors = RESEARCH_AREA_COLORS[area] || RESEARCH_AREA_COLORS.unknown;
  const label = RESEARCH_AREA_LABELS[area] || area;
  return (
    <span
      className={`inline-flex items-center rounded-full px-2.5 py-0.5 text-xs font-medium ${colors.bg} ${colors.text}`}
    >
      {label}
    </span>
  );
}

/**
 * 创新类型 Badge。
 * 根据 noveltyType 映射颜色和中文标签。
 */
function NoveltyTypeBadge({ noveltyType }: { noveltyType: string }) {
  const colors: Record<string, string> = {
    architectural: 'bg-purple-100 text-purple-700 dark:bg-purple-900/30 dark:text-purple-300',
    algorithmic: 'bg-blue-100 text-blue-700 dark:bg-blue-900/30 dark:text-blue-300',
    training_method: 'bg-green-100 text-green-700 dark:bg-green-900/30 dark:text-green-300',
    data_centric: 'bg-orange-100 text-orange-700 dark:bg-orange-900/30 dark:text-orange-300',
    theoretical: 'bg-cyan-100 text-cyan-700 dark:bg-cyan-900/30 dark:text-cyan-300',
    benchmark: 'bg-amber-100 text-amber-700 dark:bg-amber-900/30 dark:text-amber-300',
  };
  const labels: Record<string, string> = {
    architectural: '架构创新',
    algorithmic: '算法创新',
    training_method: '训练方法',
    data_centric: '数据驱动',
    theoretical: '理论创新',
    benchmark: '基准评测',
  };
  const color = colors[noveltyType] || 'bg-gray-100 text-gray-600 dark:bg-gray-800 dark:text-gray-400';
  const label = labels[noveltyType] || noveltyType.replace(/_/g, ' ');
  return (
    <span className={`inline-flex items-center rounded-full px-2 py-0.5 text-xs font-medium ${color}`}>
      {label}
    </span>
  );
}

/**
 * 研究意义 Badge。
 * fundamental / practical / incremental / niche
 */
function SignificanceBadge({ significance }: { significance: string }) {
  const colors: Record<string, string> = {
    fundamental: 'bg-purple-100 text-purple-700 dark:bg-purple-900/30 dark:text-purple-300',
    practical: 'bg-green-100 text-green-700 dark:bg-green-900/30 dark:text-green-300',
    incremental: 'bg-yellow-100 text-yellow-700 dark:bg-yellow-900/30 dark:text-yellow-300',
    niche: 'bg-gray-100 text-gray-600 dark:bg-gray-800 dark:text-gray-400',
  };
  const labels: Record<string, string> = {
    fundamental: '基础突破',
    practical: '实用价值',
    incremental: '增量改进',
    niche: '小众领域',
  };
  const color = colors[significance] || 'bg-gray-100 text-gray-600 dark:bg-gray-800 dark:text-gray-400';
  const label = labels[significance] || significance;
  return (
    <span className={`inline-flex items-center rounded-full px-2 py-0.5 text-xs font-medium ${color}`}>
      {label}
    </span>
  );
}

/**
 * 算力需求 Badge。
 * commodity / datacenter / supercomputer / prohibitive
 */
function ComputeBadge({ compute }: { compute: string }) {
  const colors: Record<string, string> = {
    commodity: 'bg-green-100 text-green-700 dark:bg-green-900/30 dark:text-green-300',
    datacenter: 'bg-yellow-100 text-yellow-700 dark:bg-yellow-900/30 dark:text-yellow-300',
    supercomputer: 'bg-orange-100 text-orange-700 dark:bg-orange-900/30 dark:text-orange-300',
    prohibitive: 'bg-red-100 text-red-700 dark:bg-red-900/30 dark:text-red-300',
  };
  const labels: Record<string, string> = {
    commodity: '消费级算力',
    datacenter: '数据中心',
    supercomputer: '超算',
    prohibitive: '极高门槛',
  };
  const color = colors[compute] || 'bg-gray-100 text-gray-600 dark:bg-gray-800 dark:text-gray-400';
  const label = labels[compute] || compute;
  return (
    <span className={`inline-flex items-center rounded-full px-2 py-0.5 text-xs font-medium ${color}`}>
      {label}
    </span>
  );
}

/**
 * 过度宣称评估 Badge。
 * honest / mild_overclaim / significant_overclaim
 */
function OverclaimingBadge({ assessment }: { assessment: string }) {
  const colors: Record<string, string> = {
    honest: 'bg-green-100 text-green-700 dark:bg-green-900/30 dark:text-green-300',
    mild_overclaim: 'bg-yellow-100 text-yellow-700 dark:bg-yellow-900/30 dark:text-yellow-300',
    significant_overclaim: 'bg-red-100 text-red-700 dark:bg-red-900/30 dark:text-red-300',
  };
  const labels: Record<string, string> = {
    honest: '诚实',
    mild_overclaim: '轻度夸大',
    significant_overclaim: '明显夸大',
  };
  const color = colors[assessment] || 'bg-gray-100 text-gray-600 dark:bg-gray-800 dark:text-gray-400';
  const label = labels[assessment] || assessment;
  return (
    <span className={`inline-flex items-center rounded-full px-2 py-0.5 text-xs font-medium ${color}`}>
      {label}
    </span>
  );
}

function AiCategoryPills({ aiDetail }: { aiDetail: AiDetail }) {
  return (
    <div className="flex flex-wrap gap-1 mt-1">
      {aiDetail.primaryCategories?.map((cat) => (
        <span
          key={cat}
          className="inline-flex items-center rounded-full bg-purple-100 dark:bg-purple-900/20 px-2 py-0.5 text-xs font-medium text-purple-700 dark:text-purple-300"
        >
          {cat.replace(/_/g, ' ')}
        </span>
      ))}
      {aiDetail.agentSubcategory?.map((sub) => (
        <span
          key={sub}
          className="inline-flex items-center rounded-full bg-pink-100 dark:bg-pink-900/20 px-2 py-0.5 text-xs font-medium text-pink-700 dark:text-pink-300 border border-pink-200 dark:border-pink-800"
        >
          agent: {sub.replace(/_/g, ' ')}
        </span>
      ))}
    </div>
  );
}

// ---------------------------------------------------------------------------
// 主组件
// ---------------------------------------------------------------------------

/**
 * 学术论文分析卡片。
 *
 * 在 Source Detail 页面中，展示单篇论文的深度分析，
 * 包括论文元信息、研究问题、方法创新、实验严谨度、局限性、
 * 工业落地潜力和相关工作对比。
 */
export function PaperCard({ tags, analysis }: PaperCardProps) {
  return (
    <div className="rounded-lg border border-gray-200 dark:border-gray-700 overflow-hidden">
      {/* 卡片标题栏 */}
      <div className="px-4 py-3 bg-purple-50/50 dark:bg-purple-950/20 border-b border-gray-200 dark:border-gray-700">
        <div className="flex items-center gap-2">
          <svg className="w-5 h-5 text-purple-600 dark:text-purple-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <path strokeLinecap="round" strokeLinejoin="round" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
          </svg>
          <span className="text-sm font-semibold text-gray-800 dark:text-gray-200">
            论文分析
          </span>
          {/* 论文标签 */}
          {tags.research_area && (
            <ResearchAreaPill area={tags.research_area} />
          )}
          {analysis?.methodology?.novelty_type && (
            <NoveltyTypeBadge noveltyType={analysis.methodology.novelty_type} />
          )}
          {analysis?.research_problem?.significance && (
            <SignificanceBadge significance={analysis.research_problem.significance} />
          )}
        </div>
      </div>

      {/* 卡片正文 */}
      <div className="p-4 space-y-3">
        {/* 论文元信息 */}
        <div>
          <div className="flex items-center gap-2 flex-wrap">
            <span className="text-base font-semibold text-gray-900 dark:text-gray-100">
              {tags.paper_title}
            </span>
          </div>

          {/* 作者与机构 */}
          {tags.authors && tags.authors.length > 0 && (
            <p className="text-xs text-gray-500 dark:text-gray-400 mt-1">
              {tags.authors.slice(0, 6).join(', ')}
              {tags.authors.length > 6 && ` 等 ${tags.authors.length} 位`}
            </p>
          )}

          {/* 发表信息 */}
          <div className="flex items-center gap-3 mt-1 text-xs text-gray-400 dark:text-gray-500">
            {tags.venue && <span>{tags.venue}</span>}
            {tags.method_type && (
              <span className="font-mono text-purple-600 dark:text-purple-400">
                {tags.method_type}
              </span>
            )}
          </div>

          {/* 代码/数据集链接 */}
          <div className="flex items-center gap-3 mt-1">
            {tags.code_url && (
              <a
                href={tags.code_url}
                target="_blank"
                rel="noopener noreferrer"
                className="inline-flex items-center gap-1 text-xs text-purple-600 dark:text-purple-400 hover:underline"
              >
                <svg className="w-3.5 h-3.5" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z" />
                </svg>
                代码
              </a>
            )}
            {tags.dataset_url && (
              <a
                href={tags.dataset_url}
                target="_blank"
                rel="noopener noreferrer"
                className="inline-flex items-center gap-1 text-xs text-purple-600 dark:text-purple-400 hover:underline"
              >
                <svg className="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                  <path strokeLinecap="round" strokeLinejoin="round" d="M4 7v10c0 2 1 3 3 3h10c2 0 3-1 3-3V7M4 7c0-2 1-3 3-3h10c2 0 3 1 3 3M4 7h16M9 11h6" />
                </svg>
                数据集
              </a>
            )}
          </div>

          {/* AI 子标签 */}
          {tags.aiDetail && <AiCategoryPills aiDetail={tags.aiDetail} />}
        </div>

        {/* 研究问题与动机（Stage 3 分析） */}
        {(analysis?.research_problem || analysis?.researchProblem) && (
          <div className="rounded-md bg-purple-50/50 dark:bg-purple-950/10 p-3 border border-purple-100 dark:border-purple-900/30">
            <div className="flex items-center gap-2 mb-1">
              <span className="text-xs font-medium text-purple-600 dark:text-purple-400">
                核心问题
              </span>
            </div>
            <p className="text-sm text-gray-700 dark:text-gray-300">
              {(analysis.research_problem || analysis.researchProblem)?.core_question ||
               (analysis.research_problem || analysis.researchProblem)?.coreQuestion}
            </p>
            {(analysis.research_problem || analysis.researchProblem)?.gap_addressed && (
              <p className="text-xs text-gray-500 dark:text-gray-400 mt-1">
                填补空白: {(analysis.research_problem || analysis.researchProblem)?.gap_addressed ||
                           (analysis.research_problem || analysis.researchProblem)?.gapAddressed}
              </p>
            )}
          </div>
        )}

        {/* 方法创新（Stage 3 分析） */}
        {analysis?.methodology && (
          <div className="rounded-md bg-indigo-50/50 dark:bg-indigo-950/10 p-3 border border-indigo-100 dark:border-indigo-900/30">
            <div className="flex items-center gap-2 mb-1">
              <span className="text-xs font-medium text-indigo-600 dark:text-indigo-400">
                方法创新
              </span>
              {analysis.methodology.technical_depth && (
                <span className="text-xs text-gray-400">
                  · 深度: {analysis.methodology.technical_depth.replace(/_/g, ' ')}
                </span>
              )}
            </div>
            <p className="text-sm text-gray-700 dark:text-gray-300">
              {analysis.methodology.approach_summary || analysis.methodology.approachSummary}
            </p>
            {/* 关键创新点列表 */}
            {(analysis.methodology.key_innovations || analysis.methodology.keyInnovations)?.length > 0 && (
              <ul className="mt-2 space-y-0.5">
                {(analysis.methodology.key_innovations || analysis.methodology.keyInnovations)?.map(
                  (item: string, i: number) => (
                    <li key={i} className="flex items-start gap-1.5 text-xs text-gray-600 dark:text-gray-400">
                      <span className="text-purple-400 mt-0.5">+</span>
                      <span>{item}</span>
                    </li>
                  ),
                )}
              </ul>
            )}
          </div>
        )}

        {/* 实验严谨度 + 局限性（双列布局） */}
        {(analysis?.experimental_rigor || analysis?.experimentalRigor ||
          analysis?.limitations_and_honesty || analysis?.limitationsAndHonesty) && (
          <div className="grid grid-cols-2 gap-3">
            {/* 实验严谨度 */}
            {(analysis?.experimental_rigor || analysis?.experimentalRigor) && (
              <div className="rounded-md bg-gray-50 dark:bg-gray-800/30 p-3">
                <div className="text-xs font-medium text-gray-500 dark:text-gray-400 mb-1">
                  实验严谨度
                </div>
                <div className="text-xs text-gray-600 dark:text-gray-400 space-y-1">
                  {((analysis.experimental_rigor || analysis.experimentalRigor)?.benchmark_coverage ||
                    (analysis.experimental_rigor || analysis.experimentalRigor)?.benchmarkCoverage) && (
                    <div>基准: {(analysis.experimental_rigor || analysis.experimentalRigor)?.benchmark_coverage ||
                                 (analysis.experimental_rigor || analysis.experimentalRigor)?.benchmarkCoverage}</div>
                  )}
                  {((analysis.experimental_rigor || analysis.experimentalRigor)?.baseline_comparison ||
                    (analysis.experimental_rigor || analysis.experimentalRigor)?.baselineComparison) && (
                    <div>基线: {(analysis.experimental_rigor || analysis.experimentalRigor)?.baseline_comparison ||
                                 (analysis.experimental_rigor || analysis.experimentalRigor)?.baselineComparison}</div>
                  )}
                  {((analysis.experimental_rigor || analysis.experimentalRigor)?.ablation_quality ||
                    (analysis.experimental_rigor || analysis.experimentalRigor)?.ablationQuality) && (
                    <div>消融: {(analysis.experimental_rigor || analysis.experimentalRigor)?.ablation_quality ||
                                 (analysis.experimental_rigor || analysis.experimentalRigor)?.ablationQuality}</div>
                  )}
                  {((analysis.experimental_rigor || analysis.experimentalRigor)?.reproducibility_level ||
                    (analysis.experimental_rigor || analysis.experimentalRigor)?.reproducibilityLevel) && (
                    <div>可复现: {(analysis.experimental_rigor || analysis.experimentalRigor)?.reproducibility_level ||
                                   (analysis.experimental_rigor || analysis.experimentalRigor)?.reproducibilityLevel}</div>
                  )}
                </div>
              </div>
            )}

            {/* 局限性与诚实度 */}
            {(analysis?.limitations_and_honesty || analysis?.limitationsAndHonesty) && (
              <div className="rounded-md bg-gray-50 dark:bg-gray-800/30 p-3">
                <div className="flex items-center gap-2 mb-1">
                  <span className="text-xs font-medium text-gray-500 dark:text-gray-400">
                    局限性与诚实度
                  </span>
                  {((analysis.limitations_and_honesty || analysis.limitationsAndHonesty)?.overclaiming_assessment ||
                    (analysis.limitations_and_honesty || analysis.limitationsAndHonesty)?.overclaimingAssessment) && (
                    <OverclaimingBadge
                      assessment={
                        (analysis.limitations_and_honesty || analysis.limitationsAndHonesty)?.overclaiming_assessment ||
                        (analysis.limitations_and_honesty || analysis.limitationsAndHonesty)?.overclaimingAssessment
                      }
                    />
                  )}
                </div>
                <div className="text-xs text-gray-600 dark:text-gray-400 space-y-1">
                  {((analysis.limitations_and_honesty || analysis.limitationsAndHonesty)?.stated_limitations ||
                    (analysis.limitations_and_honesty || analysis.limitationsAndHonesty)?.statedLimitations)?.length > 0 && (
                    <div>
                      <span className="text-gray-400">自述局限: </span>
                      {((analysis.limitations_and_honesty || analysis.limitationsAndHonesty)?.stated_limitations ||
                        (analysis.limitations_and_honesty || analysis.limitationsAndHonesty)?.statedLimitations)
                        ?.slice(0, 3).join('; ')}
                    </div>
                  )}
                  {((analysis.limitations_and_honesty || analysis.limitationsAndHonesty)?.reviewer_concerns ||
                    (analysis.limitations_and_honesty || analysis.limitationsAndHonesty)?.reviewerConcerns)?.length > 0 && (
                    <div>
                      <span className="text-gray-400">审稿疑虑: </span>
                      {((analysis.limitations_and_honesty || analysis.limitationsAndHonesty)?.reviewer_concerns ||
                        (analysis.limitations_and_honesty || analysis.limitationsAndHonesty)?.reviewerConcerns)
                        ?.slice(0, 2).join('; ')}
                    </div>
                  )}
                </div>
              </div>
            )}
          </div>
        )}

        {/* 工业落地潜力 */}
        {(analysis?.industrial_relevance || analysis?.industrialRelevance) && (
          <div className="rounded-md bg-green-50/50 dark:bg-green-950/10 p-3 border border-green-100 dark:border-green-900/30">
            <div className="flex items-center gap-2 mb-1">
              <span className="text-xs font-medium text-green-600 dark:text-green-400">
                工业落地潜力
              </span>
              {((analysis.industrial_relevance || analysis.industrialRelevance)?.compute_requirements ||
                (analysis.industrial_relevance || analysis.industrialRelevance)?.computeRequirements) && (
                <ComputeBadge
                  compute={
                    (analysis.industrial_relevance || analysis.industrialRelevance)?.compute_requirements ||
                    (analysis.industrial_relevance || analysis.industrialRelevance)?.computeRequirements
                  }
                />
              )}
              {((analysis.industrial_relevance || analysis.industrialRelevance)?.integration_readiness ||
                (analysis.industrial_relevance || analysis.industrialRelevance)?.integrationReadiness) && (
                <span className="text-xs text-gray-400">
                  · 集成就绪: {(((analysis.industrial_relevance || analysis.industrialRelevance)?.integration_readiness ||
                                   (analysis.industrial_relevance || analysis.industrialRelevance)?.integrationReadiness) ?? '')
                                   .replace(/_/g, ' ')}
                </span>
              )}
            </div>
            {/* 可应用领域 */}
            {((analysis.industrial_relevance || analysis.industrialRelevance)?.applicable_domains ||
              (analysis.industrial_relevance || analysis.industrialRelevance)?.applicableDomains)?.length > 0 && (
              <div className="flex flex-wrap gap-1 mb-1">
                {((analysis.industrial_relevance || analysis.industrialRelevance)?.applicable_domains ||
                  (analysis.industrial_relevance || analysis.industrialRelevance)?.applicableDomains)
                  ?.slice(0, 5).map((domain: string) => (
                    <span
                      key={domain}
                      className="inline-flex items-center rounded-full bg-green-100 dark:bg-green-900/20 px-2 py-0.5 text-xs text-green-700 dark:text-green-300"
                    >
                      {domain}
                    </span>
                  ))}
              </div>
            )}
            {/* 成本效益分析 */}
            {((analysis.industrial_relevance || analysis.industrialRelevance)?.cost_efficiency_analysis ||
              (analysis.industrial_relevance || analysis.industrialRelevance)?.costEfficiencyAnalysis) && (
              <p className="text-xs text-gray-500 dark:text-gray-400">
                {(analysis.industrial_relevance || analysis.industrialRelevance)?.cost_efficiency_analysis ||
                 (analysis.industrial_relevance || analysis.industrialRelevance)?.costEfficiencyAnalysis}
              </p>
            )}
          </div>
        )}

        {/* 与相关工作的关系 */}
        {(analysis?.related_work_context || analysis?.relatedWorkContext) && (
          <div className="rounded-md bg-gray-50 dark:bg-gray-800/30 p-3">
            <div className="flex items-center gap-2 mb-1">
              <span className="text-xs font-medium text-gray-500 dark:text-gray-400">
                相关工作
              </span>
              {((analysis.related_work_context || analysis.relatedWorkContext)?.opens_new_direction != null ||
                (analysis.related_work_context || analysis.relatedWorkContext)?.opensNewDirection != null) && (
                <span
                  className={`inline-flex items-center rounded-full px-2 py-0.5 text-xs font-medium ${
                    (analysis.related_work_context || analysis.relatedWorkContext)?.opens_new_direction ||
                    (analysis.related_work_context || analysis.relatedWorkContext)?.opensNewDirection
                      ? 'bg-purple-100 text-purple-700 dark:bg-purple-900/30 dark:text-purple-300'
                      : 'bg-gray-100 text-gray-500 dark:bg-gray-800 dark:text-gray-400'
                  }`}
                >
                  {(analysis.related_work_context || analysis.relatedWorkContext)?.opens_new_direction ||
                   (analysis.related_work_context || analysis.relatedWorkContext)?.opensNewDirection
                    ? '新方向'
                    : '跟进工作'}
                </span>
              )}
            </div>
            {/* 最接近的先前工作 */}
            {((analysis.related_work_context || analysis.relatedWorkContext)?.closest_prior_works ||
              (analysis.related_work_context || analysis.relatedWorkContext)?.closestPriorWorks)?.length > 0 && (
              <div className="mb-1">
                <span className="text-xs text-gray-400">先前工作: </span>
                <span className="text-xs text-gray-600 dark:text-gray-400">
                  {((analysis.related_work_context || analysis.relatedWorkContext)?.closest_prior_works ||
                    (analysis.related_work_context || analysis.relatedWorkContext)?.closestPriorWorks)
                    ?.slice(0, 3).join(', ')}
                </span>
              </div>
            )}
            {/* 实质进步 */}
            {((analysis.related_work_context || analysis.relatedWorkContext)?.advancement_over_prior ||
              (analysis.related_work_context || analysis.relatedWorkContext)?.advancementOverPrior) && (
              <p className="text-xs text-gray-600 dark:text-gray-400">
                进步: {(analysis.related_work_context || analysis.relatedWorkContext)?.advancement_over_prior ||
                       (analysis.related_work_context || analysis.relatedWorkContext)?.advancementOverPrior}
              </p>
            )}
          </div>
        )}
      </div>
    </div>
  );
}
