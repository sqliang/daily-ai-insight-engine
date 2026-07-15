// ============================================================================
// ArticleCardSpecialized.tsx — 专题分析容器
//
// 按文章来源类型派发对应的专题分析卡片。
// 在 ArticleCard 展开态中，渲染于黄金三角分析下方。
// TODO: 专题分析能力暂时停用，待重新设计后恢复。
// ============================================================================

// ---------------------------------------------------------------------------
// Props
// ---------------------------------------------------------------------------

interface ArticleCardSpecializedProps {
  source: string;
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  enriched: Record<string, any> | null;
}

// ---------------------------------------------------------------------------
// 主组件
// ---------------------------------------------------------------------------

/**
 * 专题分析容器组件。
 *
 * 按文章来源类型（github-trending / producthunt / arxiv-cs-ai）派发对应的
 * 专题分析卡片，渲染于黄金三角分析下方。
 */
export function ArticleCardSpecialized({ source, enriched }: ArticleCardSpecializedProps) {
  void source;
  void enriched;
  // TODO: 专题分析能力暂时停用，待重新设计后恢复。
  return null;
}
