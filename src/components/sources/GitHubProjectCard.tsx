// ============================================================================
// GitHubProjectCard.tsx — GitHub 开源项目分析卡片
//
// 在 Source Detail 页面中，展示单篇文章的 GitHub 项目深度分析。
// 作为 ArticleCardSpecialized 的子卡片渲染。
// ============================================================================

import type { AiDetail } from '@/lib/data/status';

// ---------------------------------------------------------------------------
// 领域颜色映射 (14 domains + other)
// ---------------------------------------------------------------------------

export const DOMAIN_COLORS: Record<string, { bg: string; text: string }> = {
  ai_ml: { bg: 'bg-purple-100 dark:bg-purple-900/30', text: 'text-purple-700 dark:text-purple-300' },
  web_frontend: { bg: 'bg-blue-100 dark:bg-blue-900/30', text: 'text-blue-700 dark:text-blue-300' },
  web_backend: { bg: 'bg-green-100 dark:bg-green-900/30', text: 'text-green-700 dark:text-green-300' },
  devops_infra: { bg: 'bg-orange-100 dark:bg-orange-900/30', text: 'text-orange-700 dark:text-orange-300' },
  database_storage: { bg: 'bg-cyan-100 dark:bg-cyan-900/30', text: 'text-cyan-700 dark:text-cyan-300' },
  programming_languages: { bg: 'bg-red-100 dark:bg-red-900/30', text: 'text-red-700 dark:text-red-300' },
  developer_tools: { bg: 'bg-indigo-100 dark:bg-indigo-900/30', text: 'text-indigo-700 dark:text-indigo-300' },
  security: { bg: 'bg-rose-100 dark:bg-rose-900/30', text: 'text-rose-700 dark:text-rose-300' },
  mobile: { bg: 'bg-emerald-100 dark:bg-emerald-900/30', text: 'text-emerald-700 dark:text-emerald-300' },
  blockchain: { bg: 'bg-amber-100 dark:bg-amber-900/30', text: 'text-amber-700 dark:text-amber-300' },
  data_engineering: { bg: 'bg-teal-100 dark:bg-teal-900/30', text: 'text-teal-700 dark:text-teal-300' },
  game_development: { bg: 'bg-pink-100 dark:bg-pink-900/30', text: 'text-pink-700 dark:text-pink-300' },
  documentation: { bg: 'bg-gray-100 dark:bg-gray-800', text: 'text-gray-700 dark:text-gray-300' },
  iot_embedded: { bg: 'bg-lime-100 dark:bg-lime-900/30', text: 'text-lime-700 dark:text-lime-300' },
  other: { bg: 'bg-gray-100 dark:bg-gray-800', text: 'text-gray-600 dark:text-gray-400' },
};

export const DOMAIN_LABELS: Record<string, string> = {
  ai_ml: 'AI/ML',
  web_frontend: 'Web 前端',
  web_backend: 'Web 后端',
  devops_infra: 'DevOps/基础设施',
  database_storage: '数据库/存储',
  programming_languages: '编程语言',
  developer_tools: '开发者工具',
  security: '安全',
  mobile: '移动端',
  blockchain: '区块链',
  data_engineering: '数据工程',
  game_development: '游戏开发',
  documentation: '文档/知识库',
  iot_embedded: 'IoT/嵌入式',
  other: '其他',
};

export const DOMAIN_LIST = [
  'ai_ml', 'web_frontend', 'web_backend', 'devops_infra', 'database_storage',
  'programming_languages', 'developer_tools', 'security', 'mobile', 'blockchain',
  'data_engineering', 'game_development', 'documentation', 'iot_embedded', 'other',
];

// ---------------------------------------------------------------------------
// 专题标注数据形状（匹配 Stage 2 管道输出的 snake_case 字段）
// Piper 使用 Python，输出字段为 snake_case；前端按实际数据形状访问。
// ---------------------------------------------------------------------------

interface GitHubTagsData {
  project_name: string;
  project_url: string;
  primary_language: string;
  license_type: string;
  domain: string;
  cross_tags?: string[];
  aiDetail?: AiDetail | null;
}

// ---------------------------------------------------------------------------
// Props
// ---------------------------------------------------------------------------

interface GitHubProjectCardProps {
  /** Stage 2 specialized_tags.github */
  tags: GitHubTagsData;
  /** Stage 3 分析结果（可能未运行） */
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  analysis?: Record<string, any>;
}

// ---------------------------------------------------------------------------
// 子组件
// ---------------------------------------------------------------------------

function DomainPill({ domain }: { domain: string }) {
  const colors = DOMAIN_COLORS[domain] || DOMAIN_COLORS.other;
  const label = DOMAIN_LABELS[domain] || domain;
  return (
    <span
      className={`inline-flex items-center rounded-full px-2.5 py-0.5 text-xs font-medium ${colors.bg} ${colors.text}`}
    >
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

function MaturityBadge({ score }: { score?: number }) {
  if (score === undefined || score === null) return null;
  const color =
    score >= 7
      ? 'bg-green-100 text-green-700 dark:bg-green-900/30 dark:text-green-300'
      : score >= 4
        ? 'bg-yellow-100 text-yellow-700 dark:bg-yellow-900/30 dark:text-yellow-300'
        : 'bg-red-100 text-red-700 dark:bg-red-900/30 dark:text-red-300';
  return (
    <span className={`inline-flex items-center rounded-full px-2 py-0.5 text-xs font-mono font-bold ${color}`}>
      {score.toFixed(1)}
    </span>
  );
}

// ---------------------------------------------------------------------------
// 主组件
// ---------------------------------------------------------------------------

/**
 * GitHub 开源项目分析卡片。
 *
 * 在 Source Detail 页面中，展示单篇文章的 GitHub 项目深度分析，
 * 包括领域分类、AI 标签、技术评价、社区健康度和采用建议。
 */
export function GitHubProjectCard({ tags, analysis }: GitHubProjectCardProps) {
  return (
    <div className="rounded-lg border border-gray-200 dark:border-gray-700 overflow-hidden">
      {/* 卡片标题栏 */}
      <div className="px-4 py-3 bg-gray-50 dark:bg-gray-800/50 border-b border-gray-200 dark:border-gray-700">
        <div className="flex items-center gap-2">
          <svg className="w-5 h-5 text-gray-700 dark:text-gray-300" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
          </svg>
          <span className="text-sm font-semibold text-gray-800 dark:text-gray-200">
            项目分析
          </span>
          {analysis?.adoption_guidance?.maturity_score != null && (
            <MaturityBadge score={analysis.adoption_guidance.maturity_score} />
          )}
        </div>
      </div>

      {/* 卡片正文 */}
      <div className="p-4 space-y-3">
        {/* 项目画像 + 分类标签 */}
        <div>
          <div className="flex items-center gap-2 flex-wrap">
            <span className="text-base font-semibold text-gray-900 dark:text-gray-100">
              {tags.project_name}
            </span>
            <DomainPill domain={tags.domain} />
            {tags.primary_language && (
              <span className="text-xs text-gray-500 dark:text-gray-400 font-mono">
                {tags.primary_language}
              </span>
            )}
            {tags.license_type && (
              <span className="text-xs text-gray-400 dark:text-gray-500">
                {tags.license_type}
              </span>
            )}
          </div>

          {/* AI 子标签 */}
          {tags.aiDetail && <AiCategoryPills aiDetail={tags.aiDetail} />}

          {/* 跨领域标签 */}
          {tags.cross_tags && tags.cross_tags.length > 0 && (
            <div className="flex flex-wrap gap-1 mt-1">
              {tags.cross_tags.map((tag) => (
                <span
                  key={tag}
                  className="inline-flex items-center rounded-full bg-gray-100 dark:bg-gray-800 px-2 py-0.5 text-xs text-gray-600 dark:text-gray-400"
                >
                  {tag}
                </span>
              ))}
            </div>
          )}
        </div>

        {/* 技术评价（如果 Stage 3 已运行） */}
        {analysis?.tech_assessment && (
          <div className="rounded-md bg-gray-50 dark:bg-gray-800/30 p-3">
            <div className="flex items-center gap-2 text-xs text-gray-500 dark:text-gray-400 mb-1">
              <span className="font-medium">技术评价</span>
              <span className="text-gray-400">·</span>
              <span>{analysis.tech_assessment.tech_stack_quality}</span>
              {analysis.tech_assessment.code_quality_indicators?.has_tests && (
                <>
                  <span className="text-gray-400">·</span>
                  <span className="text-green-600 dark:text-green-400">有测试</span>
                </>
              )}
              {analysis.tech_assessment.code_quality_indicators?.has_ci_cd && (
                <>
                  <span className="text-gray-400">·</span>
                  <span className="text-green-600 dark:text-green-400">CI/CD</span>
                </>
              )}
            </div>
            {analysis.tech_assessment.architecture_highlights && (
              <p className="text-sm text-gray-700 dark:text-gray-300">
                {analysis.tech_assessment.architecture_highlights}
              </p>
            )}
          </div>
        )}

        {/* 社区健康度 + 采用建议 */}
        {(analysis?.community_health || analysis?.adoption_guidance) && (
          <div className="grid grid-cols-2 gap-3">
            {analysis?.community_health && (
              <div className="rounded-md bg-gray-50 dark:bg-gray-800/30 p-3">
                <div className="text-xs font-medium text-gray-500 dark:text-gray-400 mb-1">
                  社区活跃度
                </div>
                <div className="text-sm text-gray-700 dark:text-gray-300 space-y-1">
                  <div>贡献者: {analysis.community_health.contributor_activity}</div>
                  {analysis.community_health.stars_trend && (
                    <div>趋势: {analysis.community_health.stars_trend}</div>
                  )}
                </div>
              </div>
            )}
            {analysis?.adoption_guidance && (
              <div className="rounded-md bg-gray-50 dark:bg-gray-800/30 p-3">
                <div className="text-xs font-medium text-gray-500 dark:text-gray-400 mb-1">
                  采用建议
                </div>
                <div className="text-sm text-gray-700 dark:text-gray-300">
                  <div>状态: {analysis.adoption_guidance.time_to_production}</div>
                  {analysis.adoption_guidance.recommended_for?.length > 0 && (
                    <div className="text-green-700 dark:text-green-400">
                      ✓ {analysis.adoption_guidance.recommended_for.slice(0, 2).join(', ')}
                    </div>
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
