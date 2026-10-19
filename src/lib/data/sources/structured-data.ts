// ============================================================================
// sources/structured-data.ts — 结构化文章数据加载（DB 主数据源 + 快照回退）
//
// 从 PostgreSQL articles 表读取文章数据，payload 采用两级轻量查询避免整列
// 搬运（issue #152）。只有 DB 抛错时才通过 withDbFallback 读取
// data/snapshot/articles/{source}.json；DB 返回空数组/null 不回退。
//
// 快照仅含近 7 天热窗口，老文章 enrichment 缺失属于预期降级。
// 消费者：sources/index.ts 的 getSourceDetailEnriched / getSourceArticleDetail。
// ============================================================================

import { and, eq, gte, inArray, lte, sql } from "drizzle-orm";

import type { ProcessingStatus, StructuredArticle } from "@/lib/data/status";
import { structuredArticleSchema } from "@/lib/data/status";
import { withDbFallback } from "@/lib/data/snapshot/fallback";
import {
  loadStructuredById as loadStructuredByIdFromSnapshot,
  loadStructuredByUrls as loadStructuredByUrlsFromSnapshot,
  loadStructuredSummaries as loadStructuredSummariesFromSnapshot,
} from "@/lib/data/snapshot/structured";
import { getDb } from "@/lib/db/client";
import { articles } from "@/lib/db/schema";
import { normalizeUrl } from "./manifests";
import type { DateRange } from "./types";

// ---------------------------------------------------------------------------
// 轻量摘要 — 不搬运 payload 的列表关联/排序/状态判定数据
// ---------------------------------------------------------------------------

/**
 * 文章轻量摘要：关联、状态判定与 impact 排序所需的最小字段集。
 *
 * 布尔标志与排序分均在 SQL 侧从 payload JSON 路径提取（只回传
 * 几个字节），语义与 determineProcessingStatus / 排序回退规则对齐。
 */
export interface StructuredArticleSummary {
  /** articles 表主键（SHA-256(url) 前 16 位），详情页按 id 精确补 payload 用 */
  id: string;
  /** 原文 URL（frontmatter 的 source 字段），与 manifest 文章关联用；可为空 */
  url: string | null;
  /** payload.impact_score 存在（Stage 3 分析完成信号之一） */
  hasImpactScore: boolean;
  /** payload.sentiment 非空 */
  hasSentiment: boolean;
  /** payload.tldr 非空（Stage 2 提取完成信号之一） */
  hasTldr: boolean;
  /** payload.objective_summary 非空 */
  hasObjectiveSummary: boolean;
  /** payload.impact_score.score；无法解析为数值时为 null */
  impactScore: number | null;
  /** payload.compound_value.score；无法解析为数值时为 null */
  compoundScore: number | null;
}

/**
 * 由轻量摘要判定处理阶段，与 determineProcessingStatus 的判定口径一致：
 * impact_score && sentiment → analyzed；tldr || objective_summary → extracted；
 * 否则 scout。摘要标志本身即从这些 payload 字段提取，故两者等价。
 */
export function summarizeStatus(
  summary: StructuredArticleSummary,
): ProcessingStatus {
  if (summary.hasImpactScore && summary.hasSentiment) {
    return "analyzed";
  }
  if (summary.hasTldr || summary.hasObjectiveSummary) {
    return "extracted";
  }
  return "scout";
}

/** 按 source_dir + 可选 created 范围组装查询条件（两级查询共用） */
function buildConditions(sourceName: string, dateRange?: DateRange) {
  const conditions = [eq(articles.sourceDir, sourceName)];
  if (dateRange?.from) conditions.push(gte(articles.created, dateRange.from));
  if (dateRange?.to) conditions.push(lte(articles.created, dateRange.to));
  return conditions;
}

/** 将 payload 中提取的 score 文本解析为数值；非数值一律视为 null（参与 ?? 回退） */
function parseScoreText(text: string | null): number | null {
  if (text === null) return null;
  const n = Number(text);
  return Number.isFinite(n) ? n : null;
}

/** 从 articles 表加载轻量摘要（SQL 侧提取状态标志与排序分） */
async function loadStructuredSummariesFromDb(
  sourceName: string,
  dateRange?: DateRange,
): Promise<StructuredArticleSummary[]> {
  const db = getDb();

  const rows = await db
    .select({
      id: articles.id,
      url: articles.url,
      // -> 对缺失键与 JSON null 均返回 SQL NULL，与 JS 中 null/undefined  falsy 语义一致
      hasImpactScore: sql<boolean>`(${articles.payload} -> 'impact_score') IS NOT NULL`,
      hasSentiment: sql<boolean>`NULLIF(${articles.payload} ->> 'sentiment', '') IS NOT NULL`,
      hasTldr: sql<boolean>`NULLIF(${articles.payload} ->> 'tldr', '') IS NOT NULL`,
      hasObjectiveSummary: sql<boolean>`NULLIF(${articles.payload} ->> 'objective_summary', '') IS NOT NULL`,
      impactScoreText: sql<string | null>`${articles.payload} -> 'impact_score' ->> 'score'`,
      compoundScoreText: sql<string | null>`${articles.payload} -> 'compound_value' ->> 'score'`,
    })
    .from(articles)
    .where(and(...buildConditions(sourceName, dateRange)));

  return rows.map((r) => ({
    id: r.id,
    url: r.url,
    hasImpactScore: r.hasImpactScore,
    hasSentiment: r.hasSentiment,
    hasTldr: r.hasTldr,
    hasObjectiveSummary: r.hasObjectiveSummary,
    impactScore: parseScoreText(r.impactScoreText),
    compoundScore: parseScoreText(r.compoundScoreText),
  }));
}

/**
 * 加载指定 source 的文章轻量摘要（不搬运 payload）。
 * DB 抛错时回退到快照，在 JS 侧按同一口径计算状态标志与排序分。
 */
export const loadStructuredSummaries = withDbFallback(
  loadStructuredSummariesFromDb,
  loadStructuredSummariesFromSnapshot,
);

/** 对单行 payload 做 Zod 校验；失败返回 null（跳过该行，不拖垮整批） */
function parsePayload(payload: unknown): StructuredArticle | null {
  try {
    return structuredArticleSchema.parse(payload);
  } catch {
    // 单行数据损坏/格式不兼容时跳过；publish 侧写入的 payload 与
    // structuredArticleSchema 同源，正常不会触发
    return null;
  }
}

/** 从 articles 表按 URL 集合取回完整 payload（仅当前页切片） */
async function loadStructuredByUrlsFromDb(
  sourceName: string,
  urls: string[],
): Promise<Map<string, StructuredArticle>> {
  const result = new Map<string, StructuredArticle>();
  if (urls.length === 0) return result;

  // URL 变体：raw / 去尾斜杠 / 单尾斜杠，覆盖 manifest 与 articles 表
  // 之间可能的格式漂移（normalizeUrl 的归一化规则）
  const candidates = new Set<string>();
  for (const u of urls) {
    candidates.add(u);
    const normalized = normalizeUrl(u);
    candidates.add(normalized);
    candidates.add(`${normalized}/`);
  }

  const db = getDb();
  const rows = await db
    .select({ url: articles.url, payload: articles.payload })
    .from(articles)
    .where(
      and(
        eq(articles.sourceDir, sourceName),
        inArray(articles.url, [...candidates]),
      ),
    );

  for (const row of rows) {
    const parsed = parsePayload(row.payload);
    if (!parsed) continue;
    const key = row.url ? normalizeUrl(row.url) : normalizeUrl(parsed.source);
    if (!result.has(key)) {
      result.set(key, parsed);
    }
  }
  return result;
}

/**
 * 按 URL 集合取回完整 payload（仅当前页切片，通常 ≤ PAGE_SIZE_ARTICLES 行）。
 * DB 抛错时回退到快照热窗口数据，返回 Map 的键仍为 normalizeUrl(url)。
 */
export const loadStructuredByUrls = withDbFallback(
  loadStructuredByUrlsFromDb,
  loadStructuredByUrlsFromSnapshot,
);

/** 从 articles 表按主键 id 精确取回单篇完整 payload */
async function loadStructuredByIdFromDb(
  sourceName: string,
  id: string,
): Promise<StructuredArticle | null> {
  const db = getDb();
  const rows = await db
    .select({ payload: articles.payload })
    .from(articles)
    .where(and(eq(articles.sourceDir, sourceName), eq(articles.id, id)))
    .limit(1);

  if (rows.length === 0) return null;
  return parsePayload(rows[0].payload);
}

/**
 * 按 articles 主键 id 精确取回单篇文章的完整 payload。
 * DB 抛错时回退到快照；快照热窗口未覆盖的老文章返回 null，不报错。
 */
export const loadStructuredById = withDbFallback(
  loadStructuredByIdFromDb,
  loadStructuredByIdFromSnapshot,
);
