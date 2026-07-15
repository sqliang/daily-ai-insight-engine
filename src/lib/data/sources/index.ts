// ============================================================================
// sources/index.ts — Public API barrel for source data access
//
// 本文件是 sources/ 目录的对外入口，承担两个职责：
//   1. 实现所有面向消费者的 public API 函数（组合内部模块）
//   2. 通过 barrel re-export 保持向后兼容 —— 所有原有 consumer 的
//      `import { X } from "@/lib/data/sources"` 无需修改即可继续工作
//
// 内部模块依赖关系：
//   types.ts ← config.ts ← index.ts
//   types.ts ← manifests.ts ← structured-data.ts ← index.ts
// ============================================================================

import { z } from "zod";
import type { ProcessingStatus } from "@/lib/data/status";
import { determineProcessingStatus } from "@/lib/data/status";
import type { StructuredArticle } from "@/lib/data/status";

// -- 内部模块导入 --
import type {
  SourceConfig,
  SourceStatus,
  EnrichedArticle,
  DateRange,
  EnrichedSourceDetail,
  SourceArticleDetail,
  SourcesViewData,
} from "./types";
import { manifestSchema } from "./types";
import { getSourceConfigs, getTiersMeta } from "./config";
import {
  loadManifests,
  loadManifestsForSource,
  mergeArticlesFromManifests,
  normalizeUrl,
} from "./manifests";
import { loadStructuredData } from "./structured-data";
import { decodeUrlSlug, normalizeArticleUrl } from "./article-route";

// ============================================================================
// Barrel re-exports — 类型
// ============================================================================

export type {
  SourceStatus,
  EnrichedArticle,
  DateRange,
  EnrichedSourceDetail,
  SourceArticleDetail,
  SourcesViewData,
};

// ============================================================================
// Barrel re-exports — 函数
// ============================================================================

export { getTiersMeta };

function buildSourceListHref(sourceName: string, dateRange?: DateRange, sort?: string): string {
  const params = new URLSearchParams();
  if (dateRange?.from) params.set("from", dateRange.from);
  if (dateRange?.to) params.set("to", dateRange.to);
  if (!dateRange?.from && !dateRange?.to) params.set("preset", "latest");
  if (sort === "impact") params.set("sort", "impact");
  const qs = params.toString();
  return qs ? `/sources/${sourceName}?${qs}` : `/sources/${sourceName}`;
}

function getImpactScore(article: EnrichedArticle): number {
  return (
    article.enriched?.impact_score?.score ??
    article.enriched?.compound_value?.score ??
    0
  );
}

// ============================================================================
// 纯转换函数：SourceConfig → SourceStatus
// ============================================================================

/**
 * 将 SourceConfig 和可选的 manifest 数据合并转换为 SourceStatus。
 *
 * 这是 config 层和 manifest 层之间的桥接函数，仅被本模块的 public API
 * 函数调用，不作为独立 API 暴露给外部消费者。
 */
function configToStatus(
  cfg: SourceConfig,
  manifest: z.infer<typeof manifestSchema> | undefined,
): SourceStatus {
  return {
    name: cfg.name,
    type: cfg.type,
    tier: cfg.tier,
    enabled: cfg.enabled,
    priority: cfg.priority,
    display_name: cfg.display_name ?? cfg.name,
    description: cfg.description,
    display_description: cfg.display_description ?? cfg.description,
    url: cfg.url,
    language: cfg.language,
    fetch_strategy: cfg.fetch_strategy,
    keywords: cfg.filter?.keywords ?? [],
    max_age_hours: cfg.filter?.max_age_hours ?? 0,
    truncation: cfg.truncation,
    target_dir: cfg.target_dir,
    manifestFound: manifest !== undefined,
    articleCount: manifest?.articles.length ?? 0,
    articles: manifest?.articles ?? [],
    manifestDate: manifest?.date ?? null,
    manifestGeneratedAt: manifest?.generated_at ?? null,
  };
}

// ============================================================================
// Public API: Source 状态查询
// ============================================================================

/**
 * 获取所有已启用 source 的状态列表。
 *
 * 返回结果按 tier（A→B→C）→ priority（升序）→ name（字母序）排列。
 * 供首页 SourcesGrid 使用。
 */
export async function getSourceStatuses(): Promise<SourceStatus[]> {
  const [configs, manifests] = await Promise.all([
    getSourceConfigs(),
    loadManifests(),
  ]);

  const results: SourceStatus[] = configs.map((cfg) => {
    const manifest = manifests.get(cfg.name);
    return configToStatus(cfg, manifest);
  });

  // Sort by tier (A→B→C) → priority (ascending, unset defaults to 999) → name (alphabetical)
  const tierOrder = { A: 0, B: 1, C: 2 };
  const DEFAULT_PRIORITY = 999;
  results.sort((a, b) => {
    const d = tierOrder[a.tier] - tierOrder[b.tier];
    if (d !== 0) return d;
    const pa = a.priority ?? DEFAULT_PRIORITY;
    const pb = b.priority ?? DEFAULT_PRIORITY;
    if (pa !== pb) return pa - pb;
    return a.name.localeCompare(b.name);
  });

  return results;
}

/**
 * 获取单个 source 的状态。
 *
 * 参数：
 *     name: source 名称（对应 config.yaml 中的 name 字段）
 *
 * 返回：
 *     对应的 SourceStatus，如果 source 不存在则返回 null
 */
export async function getSourceDetail(
  name: string,
): Promise<SourceStatus | null> {
  const [configs, manifests] = await Promise.all([
    getSourceConfigs(),
    loadManifests(),
  ]);

  const config = configs.find((c) => c.name === name);
  if (!config) return null;

  return configToStatus(config, manifests.get(name));
}

// ============================================================================
// Public API: 带 enrichment 的 Source 详情
// ============================================================================

/**
 * 获取 source 详情，包含结构化 enrichment 数据。
 *
 * 这是 source 详情页（/sources/[name]）的主要数据获取函数。
 * 执行以下步骤：
 *   1. 读取 config.yaml 获取 source 配置
 *   2. 加载最新 manifest（或 dateRange 内的所有 manifest）
 *   3. 通过 loadStructuredData 加载 enrichment（含 archive 分片）
 *   4. 将 manifest articles 与 enrichment 数据合并
 *   5. 计算处理阶段分布和可用日期列表
 *
 * 参数：
 *     name:      source 名称
 *     dateRange: 可选的日期范围筛选
 *
 * 返回：
 *     带 enrichment 的完整 source 详情，不存在时返回 null
 */
export async function getSourceDetailEnriched(
  name: string,
  dateRange?: DateRange,
): Promise<EnrichedSourceDetail | null> {
  const [configs, latestManifests] = await Promise.all([
    getSourceConfigs(),
    loadManifests(),
  ]);

  const config = configs.find((c) => c.name === name);
  if (!config) return null;

  const latestManifest = latestManifests.get(name);
  const structuredData = await loadStructuredData(name, dateRange);

  const structuredMap = new Map<string, StructuredArticle>();
  for (const s of structuredData) {
    const normalized = normalizeUrl(s.source);
    if (!structuredMap.has(normalized)) {
      structuredMap.set(normalized, s);
    }
  }

  // 确定使用哪些文章：指定 dateRange 时合并全部 manifest 并过滤，否则用最新 manifest
  let manifestArticles: Array<{
    url: string;
    title: string;
    published: string;
    summary: string;
    author: string;
    id?: string;
  }>;
  let allManifests: z.infer<typeof manifestSchema>[] = [];
  let manifestDate: string | null;
  let manifestGeneratedAt: string | null;

  if (dateRange?.from || dateRange?.to) {
    allManifests = await loadManifestsForSource(name);
    // 按 manifest.date（抓取日期）筛选，而非 article.published（发布日期）
    if (dateRange.from) {
      allManifests = allManifests.filter(
        (m) => m.date >= dateRange.from!,
      );
    }
    if (dateRange.to) {
      allManifests = allManifests.filter(
        (m) => m.date <= dateRange.to!,
      );
    }
    manifestArticles = mergeArticlesFromManifests(allManifests);
    manifestDate = allManifests[0]?.date ?? null;
    manifestGeneratedAt = allManifests[0]?.generated_at ?? null;
  } else {
    manifestArticles = latestManifest?.articles ?? [];
    manifestDate = latestManifest?.date ?? null;
    manifestGeneratedAt = latestManifest?.generated_at ?? null;
    if (latestManifest) {
      allManifests = [latestManifest];
    }
  }

  // 收集该源所有 manifest 的 date，供日期选择器使用
  const availableDates = allManifests
    .map((m) => m.date)
    .filter((d): d is string => d !== null && d !== undefined);

  const enrichedArticles: EnrichedArticle[] = manifestArticles.map((a) => {
    const normalizedArticleUrl = normalizeUrl(a.url);
    const enriched =
      structuredMap.get(normalizedArticleUrl) ?? null;
    return {
      url: a.url,
      title: a.title,
      published: a.published ?? "",
      summary: a.summary ?? "",
      author: a.author ?? "",
      id: a.id,
      enriched,
      status: enriched
        ? determineProcessingStatus(enriched)
        : "scout",
    };
  });

  const stageCounts: Record<ProcessingStatus, number> = {
    scout: 0,
    extracted: 0,
    analyzed: 0,
  };
  for (const a of enrichedArticles) {
    stageCounts[a.status]++;
  }

  return {
    name: config.name,
    type: config.type,
    tier: config.tier,
    enabled: config.enabled,
    priority: config.priority,
    display_name: config.display_name ?? config.name,
    description: config.description,
    display_description: config.display_description ?? config.description,
    url: config.url,
    language: config.language,
    fetch_strategy: config.fetch_strategy,
    keywords: config.filter?.keywords ?? [],
    max_age_hours: config.filter?.max_age_hours ?? 0,
    truncation: config.truncation,
    target_dir: config.target_dir,
    manifestFound: manifestArticles.length > 0,
    articleCount: enrichedArticles.length,
    articles: enrichedArticles,
    manifestDate,
    manifestGeneratedAt,
    stageCounts,
    availableDates,
    dateRange: dateRange ?? null,
  };
}

/**
 * 获取单篇 source 文章详情。
 *
 * 文章定位优先使用 manifest 中的 article.id；缺 ID 的历史文章使用 url-* slug。
 * previous/next 基于当前日期筛选后的文章列表，并可按影响力排序。
 */
export async function getSourceArticleDetail(
  sourceName: string,
  articleIdOrSlug: string,
  dateRange?: DateRange,
  sort?: "impact" | null,
): Promise<SourceArticleDetail | null> {
  const source = await getSourceDetailEnriched(sourceName, dateRange);
  if (!source) return null;

  const articles =
    sort === "impact"
      ? [...source.articles].sort((a, b) => getImpactScore(b) - getImpactScore(a))
      : source.articles;

  const fallbackUrl = articleIdOrSlug.startsWith("url-")
    ? decodeUrlSlug(articleIdOrSlug.slice(4))
    : null;
  const fallbackKey = fallbackUrl ? normalizeUrl(fallbackUrl) : null;

  const index = articles.findIndex((article) => {
    if (article.id && article.id === articleIdOrSlug) return true;
    return fallbackKey !== null && normalizeArticleUrl(article.url) === fallbackKey;
  });

  if (index < 0) return null;

  const article = articles[index];
  return {
    source,
    article,
    previousArticle: articles[index - 1] ?? null,
    nextArticle: articles[index + 1] ?? null,
    listHref: buildSourceListHref(sourceName, dateRange, sort ?? undefined),
    originalHref: article.url,
  };
}

// ============================================================================
// Public API: Sources 首页视图数据
// ============================================================================

/**
 * 获取 Sources 首页渲染所需的完整数据。
 *
 * 组合 tier 元数据、source 状态列表和最新 manifest 日期，
 * 一次性返回 @/app/page.tsx 需要的所有数据。
 */
export async function getSourcesViewData(): Promise<SourcesViewData> {
  const [sources, tiersMeta] = await Promise.all([
    getSourceStatuses(),
    getTiersMeta(),
  ]);

  const latestDate =
    sources
      .map((s) => s.manifestDate)
      .filter((d): d is string => d !== null)
      .sort()
      .reverse()[0] ?? null;

  return {
    tiersMeta,
    sources,
    totalSources: sources.length,
    latestDate,
  };
}
