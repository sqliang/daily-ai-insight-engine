// ============================================================================
// sources/structured-data.ts — 结构化文章数据加载
//
// 从 PostgreSQL articles 表（pipeline Stage 5 publish 写入）读取文章数据。
// payload JSONB 平均 ~10KB/行，整列无 LIMIT 拉取曾是 Neon 出站流量耗尽
// 的根因（issue #152），因此本模块按用途拆成两级查询：
//   loadStructuredSummaries — 轻量摘要（id/url + 状态标志 + 排序分），
//     不搬运 payload，供 manifest 关联、status 判定、stageCounts 与
//     impact 排序使用；排序分从 payload 的 JSON 路径在服务端提取，
//     保持 impact_score.score ?? compound_value.score ?? 0 的回退语义。
//   loadStructuredByUrls / loadStructuredById — 按需取回完整 payload
//     （Zod 校验），仅覆盖当前页切片或详情页目标文章（≤ 每页条数行）。
//
// 旧的 loadStructuredData（全量 payload 无分页）已随唯一消费者
// getSourceDetailEnriched 的改造一并移除。
//
// 消费者：sources/index.ts 的 getSourceDetailEnriched / getSourceArticleDetail。
// ============================================================================

import { and, eq, gte, inArray, lte, sql } from "drizzle-orm";

import type { ProcessingStatus, StructuredArticle } from "@/lib/data/status";
import { structuredArticleSchema } from "@/lib/data/status";
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

/**
 * 加载指定 source 的文章轻量摘要（不搬运 payload）。
 *
 * 按 source_dir 过滤 articles 表；指定 dateRange 时附加 created 范围条件。
 * 布尔标志用 NULLIF(...,'''') IS NOT NULL 判定，与 JS 真值语义对齐
 * （payload 中出现空字符串时按"无"处理）；排序分以文本取出后在 JS 侧
 * 解析，避免数据库对脏数据执行 ::float 转换报错。
 *
 * 参数：
 *     sourceName: source 名称（对应 source_dir 列）
 *     dateRange:   可选的日期范围筛选 { from?, to? }，格式 YYYY-MM-DD
 *
 * 返回：
 *     轻量摘要数组（每行仅数十字节，可安全全量加载）
 */
export async function loadStructuredSummaries(
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

/**
 * 按 URL 集合取回完整 payload（仅当前页切片，通常 ≤ PAGE_SIZE_ARTICLES 行）。
 *
 * SQL 过滤同时传入原始与归一化（含去/加尾部斜杠）的 URL 变体，容忍
 * manifest 与 articles.url 之间的细微格式差异；返回 Map 的键统一为
 * normalizeUrl(url)，与调用方的关联键一致。
 *
 * 参数：
 *     sourceName: source 名称（对应 source_dir 列）
 *     urls:       目标文章的原文 URL 列表
 *
 * 返回：
 *     Map<normalizeUrl(url), 校验后的 StructuredArticle>；校验失败的行被跳过
 */
export async function loadStructuredByUrls(
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
 * 按 articles 主键 id 精确取回单篇文章的完整 payload。
 *
 * 详情页定位到目标文章后优先走本函数（主键等值查询，单行传输）；
 * manifest 中的文章 id 与 articles.id 同源（SHA-256(url) 前 16 位）。
 *
 * 参数：
 *     sourceName: source 名称（对应 source_dir 列，防御性过滤）
 *     id:         articles 表主键
 *
 * 返回：
 *     校验后的 StructuredArticle；未命中或校验失败返回 null
 */
export async function loadStructuredById(
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
