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
import type { ProcessingStatus, StructuredArticle } from "@/lib/data/status";

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
import {
  loadStructuredById,
  loadStructuredByUrls,
  loadStructuredSummaries,
  summarizeStatus,
  type StructuredArticleSummary,
} from "./structured-data";
import { decodeUrlSlug, normalizeArticleUrl } from "./article-route";
import { paginate, PAGE_SIZE_ARTICLES } from "@/lib/utils/pagination";

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

// ---------------------------------------------------------------------------
// impact 排序 — 基于轻量摘要的排序分（不依赖完整 payload）
// ---------------------------------------------------------------------------

/**
 * 按影响力分数降序排序（返回新数组，不改原数组）。
 *
 * 排序分来自 summaries（payload 的 JSON 路径在服务端提取），回退规则
 * impactScore ?? compoundScore ?? 0 与旧的 enriched.impact_score?.score
 * ?? enriched.compound_value?.score ?? 0 完全等价。
 * 共享 helper：getSourceDetailEnriched（服务端排序上移）与
 * getSourceArticleDetail（详情页 prev/next 排序）必须使用同一套
 * 排序逻辑，否则列表页与详情页的文章顺序会不一致。
 */
function sortArticlesByImpact(
  articles: EnrichedArticle[],
  sortScoreByUrl: Map<string, number>,
): EnrichedArticle[] {
  const scoreOf = (a: EnrichedArticle) =>
    sortScoreByUrl.get(normalizeUrl(a.url)) ?? 0;
  return [...articles].sort((a, b) => scoreOf(b) - scoreOf(a));
}

// 详情页兜底定位用的全量时间范围：覆盖所有 manifest 日期，确保任何
// 列表页可达的文章都能被详情页找到。仅用于"按 id/url 定位文章"，
// 不影响 prev/next 导航沿用的筛选上下文（见 getSourceArticleDetail）。
const ARTICLE_LOCATE_FULL_RANGE: DateRange = {
  from: "1970-01-01",
  to: "9999-12-31",
};

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
 * getSourceDetailEnriched 的可选查询参数。
 *
 * page/pageSize 同时缺省时返回完整列表（分页元信息为 null），
 * 供文章详情页等需要全量 prev/next 的场景使用。
 */
export interface SourceDetailQueryOptions {
  /** 目标页码（1-based），越界由 paginate() clamp */
  page?: number;
  /** 每页条数，缺省 PAGE_SIZE_ARTICLES */
  pageSize?: number;
  /**
   * 排序方式："impact" 时按影响力分数降序（服务端排序）。
   * 排序必须在分页切片之前完成，否则跨页顺序会错乱 —— 这正是
   * 排序从客户端上移到数据层的原因。
   */
  sort?: "impact" | null;
}

// ---------------------------------------------------------------------------
// 内部：manifest + 轻量摘要的合并上下文（两个 public API 共用）
//
// 设计理由（issue #152）：articles.payload 平均 ~10KB/行，列表构建只需要
// 状态标志与排序分，因此关联层一律使用 loadStructuredSummaries 的轻量
// 摘要；完整 payload 只在分页切片后按当前页 URL（或详情页目标文章 id）
// 取回。EnrichedArticle.enriched 在本层一律为 null（延迟加载）。
// ---------------------------------------------------------------------------

/**
 * manifest 文章列表与轻量摘要的合并结果。
 *
 * 供 getSourceDetailEnriched（排序→分页→当前页补 payload）与
 * getSourceArticleDetail（定位→单篇补 payload）共用，保证两者看到的
 * 列表顺序与排序分完全一致。
 */
interface ArticleListContext {
  config: SourceConfig;
  /** 合并后的文章列表；enriched 均为 null（延迟加载），status 来自摘要 */
  articles: EnrichedArticle[];
  /** normalizeUrl(url) → impact 排序分（impactScore ?? compoundScore ?? 0） */
  sortScoreByUrl: Map<string, number>;
  manifestDate: string | null;
  manifestGeneratedAt: string | null;
  availableDates: string[];
  stageCounts: Record<ProcessingStatus, number>;
}

/**
 * 构建文章列表上下文：加载 manifest 与轻量摘要，按 normalizeUrl 关联，
 * 计算 status / stageCounts / availableDates。
 *
 * 指定 dateRange 时合并该范围内的全部 manifest（按 manifest.date 筛选），
 * 否则只使用最新 manifest —— 与旧实现口径一致。
 */
async function buildArticleListContext(
  name: string,
  dateRange?: DateRange,
): Promise<ArticleListContext | null> {
  const [configs, latestManifests] = await Promise.all([
    getSourceConfigs(),
    loadManifests(),
  ]);

  const config = configs.find((c) => c.name === name);
  if (!config) return null;

  const latestManifest = latestManifests.get(name);
  const summaries = await loadStructuredSummaries(name, dateRange);

  // 摘要关联 map 与排序分 map 同键（normalizeUrl），首见优先（与旧实现一致）
  const summaryMap = new Map<string, StructuredArticleSummary>();
  const sortScoreByUrl = new Map<string, number>();
  for (const s of summaries) {
    if (!s.url) continue;
    const key = normalizeUrl(s.url);
    if (!summaryMap.has(key)) {
      summaryMap.set(key, s);
      sortScoreByUrl.set(key, s.impactScore ?? s.compoundScore ?? 0);
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

  const articles: EnrichedArticle[] = manifestArticles.map((a) => {
    const summary = summaryMap.get(normalizeUrl(a.url)) ?? null;
    return {
      url: a.url,
      title: a.title,
      published: a.published ?? "",
      summary: a.summary ?? "",
      author: a.author ?? "",
      id: a.id,
      enriched: null,
      status: summary ? summarizeStatus(summary) : "scout",
    };
  });

  const stageCounts: Record<ProcessingStatus, number> = {
    scout: 0,
    extracted: 0,
    analyzed: 0,
  };
  for (const a of articles) {
    stageCounts[a.status]++;
  }

  return {
    config,
    articles,
    sortScoreByUrl,
    manifestDate,
    manifestGeneratedAt,
    availableDates,
    stageCounts,
  };
}

/**
 * 将列表上下文组装为 EnrichedSourceDetail（两个 public API 共用）。
 *
 * articles 参数为最终对外暴露的列表（当前页切片或全量），
 * articleCount 始终保持切片前总数口径（hero 统计、列表徽标依赖）。
 */
function contextToSourceDetail(
  ctx: ArticleListContext,
  articles: EnrichedArticle[],
  dateRange: DateRange | undefined,
  paginated: ReturnType<typeof paginate<EnrichedArticle>> | null,
): EnrichedSourceDetail {
  const { config } = ctx;
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
    manifestFound: ctx.articles.length > 0,
    articleCount: ctx.articles.length,
    articles,
    manifestDate: ctx.manifestDate,
    manifestGeneratedAt: ctx.manifestGeneratedAt,
    stageCounts: ctx.stageCounts,
    availableDates: ctx.availableDates,
    dateRange: dateRange ?? null,
    pagination: paginated
      ? {
          page: paginated.page,
          pageSize: paginated.pageSize,
          totalItems: paginated.totalItems,
          totalPages: paginated.totalPages,
        }
      : null,
  };
}

/**
 * 获取 source 详情，包含结构化 enrichment 数据。
 *
 * 这是 source 详情页（/sources/[name]）的主要数据获取函数。
 * 执行以下步骤：
 *   1. 读取 config.yaml 获取 source 配置
 *   2. 加载最新 manifest（或 dateRange 内的所有 manifest）
 *   3. 通过 loadStructuredSummaries 加载轻量摘要（不搬运 payload）
 *   4. 将 manifest articles 与摘要关联，得到 status 与排序分
 *   5. 计算处理阶段分布和可用日期列表
 *   6. （可选）按影响力排序并分页切片 —— articleCount 始终保持
 *      切片前的总数口径，articles 为当前页数据
 *   7. 分页模式下仅对当前页文章用 loadStructuredByUrls 补全 enriched
 *      payload；未分页时（详情页定位场景）enriched 保持 null，由调用方
 *      按需单篇补全 —— 避免整源 payload 全量传输（issue #152）
 *
 * 参数：
 *     name:      source 名称
 *     dateRange: 可选的日期范围筛选
 *     options:   可选的分页与排序参数
 *
 * 返回：
 *     带 enrichment 的 source 详情，不存在时返回 null
 */
export async function getSourceDetailEnriched(
  name: string,
  dateRange?: DateRange,
  options?: SourceDetailQueryOptions,
): Promise<EnrichedSourceDetail | null> {
  const ctx = await buildArticleListContext(name, dateRange);
  if (!ctx) return null;

  // 排序 → 分页切片：articleCount 保持切片前总数口径（hero 统计、
  // 列表徽标依赖），articles 仅为当前页数据，避免全量渲染导致卡顿
  const sortedArticles =
    options?.sort === "impact"
      ? sortArticlesByImpact(ctx.articles, ctx.sortScoreByUrl)
      : ctx.articles;

  const paginated =
    options?.page !== undefined || options?.pageSize !== undefined
      ? paginate(
          sortedArticles,
          options.page ?? 1,
          options.pageSize ?? PAGE_SIZE_ARTICLES,
        )
      : null;

  let articles = paginated ? paginated.items : sortedArticles;

  // 仅当前页补全 payload：ArticleCard 渲染需要 tldr/sentiment/评分等
  // enriched 字段；非当前页文章不渲染，不需要 payload（流量优化核心）
  if (paginated && paginated.items.length > 0) {
    const payloadMap = await loadStructuredByUrls(
      name,
      paginated.items.map((a) => a.url),
    );
    articles = paginated.items.map((a) => ({
      ...a,
      enriched: payloadMap.get(normalizeUrl(a.url)) ?? null,
    }));
  }

  return contextToSourceDetail(ctx, articles, dateRange, paginated);
}

/**
 * 获取单篇 source 文章详情。
 *
 * 文章定位优先使用 manifest 中的 article.id；缺 ID 的历史文章使用 url-* slug。
 * previous/next 基于当前日期筛选后的文章列表，并可按影响力排序。
 *
 * 定位基于轻量摘要列表（不触发全量 payload 加载）；定位到目标文章后
 * 只补全该篇的 enriched payload —— 优先按 articles 主键 id 精确查，
 * 未命中时按 url 兜底。prev/next 条目只用于导航卡片（title/url/id），
 * 不需要完整 payload，enriched 保持 null。
 *
 * 定位兜底：dateRange 过滤后的列表找不到时，用全量时间范围再定位一次。
 * 详情页的 dateRange 默认值（近 14 天，见 page.tsx resolveDateRange）会裁掉
 * 老文章，而列表页默认"全部"可达任意历史文章——不兜底的话，从列表点进
 * 任何早于 14 天的文章都会 404（issue #147）。摘要很轻，兜底成本低。
 */
export async function getSourceArticleDetail(
  sourceName: string,
  articleIdOrSlug: string,
  dateRange?: DateRange,
  sort?: "impact" | null,
): Promise<SourceArticleDetail | null> {
  const ctx = await buildArticleListContext(sourceName, dateRange);
  if (!ctx) return null;

  const fallbackUrl = articleIdOrSlug.startsWith("url-")
    ? decodeUrlSlug(articleIdOrSlug.slice(4))
    : null;
  const fallbackKey = fallbackUrl ? normalizeUrl(fallbackUrl) : null;

  const locate = (candidates: EnrichedArticle[]) =>
    candidates.findIndex((article) => {
      if (article.id && article.id === articleIdOrSlug) return true;
      return fallbackKey !== null && normalizeArticleUrl(article.url) === fallbackKey;
    });

  let articles =
    sort === "impact"
      ? sortArticlesByImpact(ctx.articles, ctx.sortScoreByUrl)
      : ctx.articles;
  let index = locate(articles);

  // 筛选窗口内未命中：改用全量范围重新加载并定位。
  // 命中后 prev/next 也基于全量列表（"全部"上下文），保证导航可用
  if (index < 0) {
    const fullCtx = await buildArticleListContext(
      sourceName,
      ARTICLE_LOCATE_FULL_RANGE,
    );
    if (!fullCtx) return null;
    const fullArticles =
      sort === "impact"
        ? sortArticlesByImpact(fullCtx.articles, fullCtx.sortScoreByUrl)
        : fullCtx.articles;
    index = locate(fullArticles);
    if (index < 0) return null;
    articles = fullArticles;
  }

  const target = articles[index];

  // 目标文章补全完整 payload（详情页正文渲染必须）：优先主键 id 精确查，
  // id 缺失或未命中时按 url 兜底（历史 manifest 可能缺 id 字段）
  let enriched: StructuredArticle | null = null;
  if (target.id) {
    enriched = await loadStructuredById(sourceName, target.id);
  }
  if (!enriched) {
    const payloadMap = await loadStructuredByUrls(sourceName, [target.url]);
    enriched = payloadMap.get(normalizeUrl(target.url)) ?? null;
  }
  const article: EnrichedArticle = { ...target, enriched };

  // source 字段沿用首个 dateRange 上下文（与旧实现一致：兜底定位不改变
  // hero 展示的统计口径）；articles 为定位上下文的全量列表
  const source = contextToSourceDetail(ctx, ctx.articles, dateRange, null);

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
