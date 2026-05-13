// =============================================================================
// Centralized tier / source-type display labels, colors, and metadata
// Used by all source page components to avoid duplicated inline maps.
// =============================================================================

export interface TierMeta {
  label: string;
  subtitle: string;
  rationale: string;
}

export const TIER_COLORS: Record<string, string> = {
  A: "var(--accent)",
  B: "var(--warm)",
  C: "var(--cool)",
};

export const TIER_LABELS: Record<string, string> = {
  A: "Tier A · 技术与前沿",
  B: "Tier B · 产品与开发者",
  C: "Tier C · 商业与资本",
};

export const TIER_SHORT_LABELS: Record<string, string> = {
  A: "Tier A",
  B: "Tier B",
  C: "Tier C",
};

export const SOURCE_TYPE_LABELS: Record<string, string> = {
  academic_paper: "学术论文",
  tech_blog: "技术博客",
  news_media: "科技媒体",
  community_discussion: "社区讨论",
};

export const LANGUAGE_LABELS: Record<string, string> = {
  zh: "中文",
  en: "EN",
};
