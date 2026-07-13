// ============================================================================
// ArticleCardSpecialized.tsx — 专题分析容器
//
// 按文章来源类型派发对应的专题分析卡片。
// 在 ArticleCard 展开态中，渲染于黄金三角分析下方。
// ============================================================================

import { GitHubProjectCard } from './GitHubProjectCard';

// ---------------------------------------------------------------------------
// Props
// ---------------------------------------------------------------------------

interface ArticleCardSpecializedProps {
  source: string;
  enriched: Record<string, any> | null;
}

// ---------------------------------------------------------------------------
// 主组件
// ---------------------------------------------------------------------------

export function ArticleCardSpecialized({ source, enriched }: ArticleCardSpecializedProps) {
  if (!enriched) return null;

  const specializedTags = enriched.specialized_tags;

  // Phase 1: GitHub — 检查是否有 GitHub 标注
  if (source === 'github-trending' && specializedTags?.github) {
    // 提取 Stage 3 GitHub 分析字段（snake_case，匹配管道输出）
    const analysis = {
      project_profile: enriched.project_profile,
      project_classification: enriched.project_classification,
      tech_assessment: enriched.tech_assessment,
      community_health: enriched.community_health,
      competitive_landscape: enriched.competitive_landscape,
      adoption_guidance: enriched.adoption_guidance,
    };

    return (
      <div className="mt-4">
        <div className="flex items-center gap-2 mb-3">
          <div className="h-px flex-1 bg-gradient-to-r from-transparent via-purple-300 dark:via-purple-700 to-transparent" />
          <span className="text-xs font-medium text-purple-600 dark:text-purple-400 uppercase tracking-wider">
            专题分析
          </span>
          <div className="h-px flex-1 bg-gradient-to-r from-transparent via-purple-300 dark:via-purple-700 to-transparent" />
        </div>
        <GitHubProjectCard tags={specializedTags.github} analysis={analysis} />
      </div>
    );
  }

  // Phase 2: Product — 待实现
  // if (['producthunt', 'whytryai'].includes(source) && specializedTags?.product) { ... }

  // Phase 3: Paper — 待实现
  // if (source === 'arxiv-cs-ai' && specializedTags?.paper) { ... }

  return null;
}
