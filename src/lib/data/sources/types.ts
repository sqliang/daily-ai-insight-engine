// ============================================================================
// sources/types.ts — Zod schemas 和 TypeScript 接口定义
//
// 定义 source 数据层的所有数据形状，包括 manifest JSON 校验 schema、
// source 配置/状态类型、以及 enrichment 相关接口。
// 本模块无运行时逻辑，仅提供类型和 schema 定义，被所有其他 sources/
// 子模块引用。
// ============================================================================

import { z } from "zod";
import type { TierMeta } from "@/lib/data/tiers";
import type {
  ProcessingStatus,
  StructuredArticle,
} from "@/lib/data/status";

// ============================================================================
// Zod schemas for manifest JSON validation
// ============================================================================

export const manifestArticleSchema = z.object({
  url: z.string(),
  title: z.string(),
  published: z.string().optional().default(""),
  summary: z.string(),
  author: z.string().optional().default(""),
  id: z.string().optional(),
});

export const manifestSchema = z.object({
  source: z.string(),
  source_type: z.enum([
    "academic_paper",
    "tech_blog",
    "news_media",
    "community_discussion",
    "newsletter_rss",
  ]),
  tier: z.enum(["A", "B", "C"]),
  generated_at: z.string(),
  date: z.string(),
  articles: z.array(manifestArticleSchema),
});

// ============================================================================
// Type definitions
// ============================================================================

export interface SourceConfig {
  name: string;
  type: string;
  tier: "A" | "B" | "C";
  enabled: boolean;
  priority?: number;  // 同 tier 内排序优先级，数字越小越靠前，未配置的排最后
  display_name?: string;
  description: string;
  display_description?: string;
  url: string;
  language: string;
  fetch_strategy: string;
  filter: { keywords: string[]; max_age_hours: number };
  truncation: { mode: string; limit?: number };
  target_dir?: string;
}

export interface SourceStatus {
  name: string;
  type: string;
  tier: "A" | "B" | "C";
  enabled: boolean;
  priority?: number;
  display_name: string;
  description: string;
  display_description: string;
  url: string;
  language: string;
  fetch_strategy: string;
  keywords: string[];
  max_age_hours: number;
  truncation: { mode: string; limit?: number };
  target_dir?: string;
  manifestFound: boolean;
  articleCount: number;
  articles: Array<{
    url: string;
    title: string;
    published: string;
    summary: string;
    author: string;
    id?: string;
  }>;
  manifestDate: string | null;
  manifestGeneratedAt: string | null;
}

export interface EnrichedArticle {
  url: string;
  title: string;
  published: string;
  summary: string;
  author: string;
  id?: string;
  enriched: StructuredArticle | null;
  status: ProcessingStatus;
}

import type { DateRange } from "../types";
import type { PaginationMeta } from "@/lib/utils/pagination";

export type { DateRange };

export interface EnrichedSourceDetail {
  name: string;
  type: string;
  tier: "A" | "B" | "C";
  enabled: boolean;
  priority?: number;
  display_name: string;
  description: string;
  display_description: string;
  url: string;
  language: string;
  fetch_strategy: string;
  keywords: string[];
  max_age_hours: number;
  truncation: { mode: string; limit?: number };
  target_dir?: string;
  manifestFound: boolean;
  /** 范围内文章总数（切片前口径），hero 统计与列表徽标使用 */
  articleCount: number;
  /** 当前页文章切片；未传分页参数时为完整列表 */
  articles: EnrichedArticle[];
  manifestDate: string | null;
  manifestGeneratedAt: string | null;
  stageCounts: Record<ProcessingStatus, number>;
  availableDates: string[];
  dateRange: DateRange | null;
  /** 分页元信息；未传分页参数时为 null（如文章详情页的全量列表场景） */
  pagination: PaginationMeta | null;
}

export interface SourceArticleDetail {
  source: EnrichedSourceDetail;
  article: EnrichedArticle;
  previousArticle: EnrichedArticle | null;
  nextArticle: EnrichedArticle | null;
  listHref: string;
  originalHref: string;
}

export interface SourcesViewData {
  tiersMeta: Record<string, TierMeta>;
  sources: SourceStatus[];
  totalSources: number;
  latestDate: string | null;
}
