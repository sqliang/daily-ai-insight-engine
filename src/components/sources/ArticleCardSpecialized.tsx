// ============================================================================
// ArticleCardSpecialized.tsx — 文章卡片内嵌专题分析容器（当前为占位实现）
//
// 设计意图：
//   按文章来源类型（github-trending / producthunt / arxiv-cs-ai）在文章卡片展开态中
//   渲染对应的迷你专题分析，作为黄金三角分析的补充。
//
// 当前状态：
//   专题洞察已在 /specialized/* 独立页面和 /dashboard/{date} 顶部入口完整实现。
//   文章卡片内嵌的迷你专题视图尚未实现，因此本组件返回 null，避免在卡片展开态中
//   展示与专题页重复但信息密度不足的内容。后续如需在卡片中展示项目/产品/论文快照，
//   可在此组件中复用 src/components/reports/SpecializedEntries 的渲染逻辑。
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
  // 文章卡片内嵌专题视图尚未实现；完整的专题洞察请查看 /specialized/* 页面。
  return null;
}
