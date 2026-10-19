// ============================================================================
// snapshot/structured.ts — 从 data/snapshot/articles 读取结构化文章
//
// articles/{source}.json 是 04_structured 热数据原样数组（仅近 7 天热窗口）。
// 本模块在 JS 侧复现 DB 版的字段提取口径：状态布尔标志、impact/compound
// 排序分、URL 归一化关联与 created 日期过滤。热窗口之外的文章没有
// enrichment 属于预期降级，不视为错误。
// ============================================================================

import type { StructuredArticle } from "@/lib/data/status";
import { structuredArticleSchema } from "@/lib/data/status";
import type { StructuredArticleSummary } from "@/lib/data/sources/structured-data";
import { normalizeUrl } from "@/lib/data/sources/manifests";
import type { DateRange } from "@/lib/data/sources/types";
import {
  assertSnapshotAvailable,
  readSnapshotJson,
} from "./client";

export type SnapshotArticle = Record<string, unknown>;

function isRecord(value: unknown): value is SnapshotArticle {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

/**
 * 读取指定 source 的原始文章数组。供 summaries / payload 查询与论文专题
 * 共用；文件缺失且快照索引可用时返回 []（热窗口缺失属正常）。
 */
export async function readSnapshotArticles(
  sourceName: string,
): Promise<SnapshotArticle[]> {
  const raw = await readSnapshotJson(`articles/${sourceName}.json`);
  if (raw === null) {
    await assertSnapshotAvailable();
    return [];
  }
  if (!Array.isArray(raw)) {
    throw new Error(`快照文章文件格式无效：${sourceName}`);
  }
  return raw.filter(isRecord);
}

/** 对齐 PostgreSQL JSONB ->> 的文本提取：字符串原样，其他 JSON 值取 JSON 文本 */
function jsonText(value: unknown): string | null {
  if (value === null || value === undefined) return null;
  if (typeof value === "string") return value;
  try {
    return JSON.stringify(value) ?? null;
  } catch {
    return null;
  }
}

/** 与 DB 版 parseScoreText 一致：非有限数值一律回退为 null */
function parseScore(value: unknown): number | null {
  const text = jsonText(value);
  if (text === null) return null;
  const score = Number(text);
  return Number.isFinite(score) ? score : null;
}

/** 提取 impact_score / compound_value 对象中的 score；非对象时对齐 SQL 返回 null */
function extractNestedScore(value: unknown): number | null {
  if (!isRecord(value)) return null;
  return parseScore(value.score);
}

/** 从原始 payload 计算轻量摘要，字段口径与 DB 版 SQL 提取一致 */
function toSummary(article: SnapshotArticle): StructuredArticleSummary {
  const sentiment = jsonText(article.sentiment);
  const tldr = jsonText(article.tldr);
  const objectiveSummary = jsonText(article.objective_summary);
  return {
    id: typeof article.id === "string" ? article.id : "",
    url: typeof article.source === "string" ? article.source : null,
    hasImpactScore: article.impact_score !== null && article.impact_score !== undefined,
    hasSentiment: sentiment !== null && sentiment !== "",
    hasTldr: tldr !== null && tldr !== "",
    hasObjectiveSummary: objectiveSummary !== null && objectiveSummary !== "",
    impactScore: extractNestedScore(article.impact_score),
    compoundScore: extractNestedScore(article.compound_value),
  };
}

/** 按 created 字符串过滤日期范围；未传范围时不做过滤 */
function inDateRange(article: SnapshotArticle, dateRange?: DateRange): boolean {
  if (!dateRange?.from && !dateRange?.to) return true;
  if (typeof article.created !== "string") return false;
  if (dateRange.from && article.created < dateRange.from) return false;
  if (dateRange.to && article.created > dateRange.to) return false;
  return true;
}

/**
 * 加载指定 source 的文章轻量摘要（JS 侧计算，不依赖数据库 JSON 路径）。
 */
export async function loadStructuredSummaries(
  sourceName: string,
  dateRange?: DateRange,
): Promise<StructuredArticleSummary[]> {
  const articles = await readSnapshotArticles(sourceName);
  return articles
    .filter((article) => inDateRange(article, dateRange))
    .map(toSummary);
}

/**
 * 按 URL 集合取回完整 payload，返回 Map<normalizeUrl(url), StructuredArticle>。
 * URL 候选变体与 DB 版一致，容忍尾部斜杠等格式漂移。
 */
export async function loadStructuredByUrls(
  sourceName: string,
  urls: string[],
): Promise<Map<string, StructuredArticle>> {
  const result = new Map<string, StructuredArticle>();
  if (urls.length === 0) return result;

  const candidates = new Set<string>();
  for (const url of urls) {
    candidates.add(url);
    const normalized = normalizeUrl(url);
    candidates.add(normalized);
    candidates.add(`${normalized}/`);
  }

  const articles = await readSnapshotArticles(sourceName);
  for (const article of articles) {
    if (typeof article.source !== "string" || !candidates.has(article.source)) {
      continue;
    }
    try {
      const parsed = structuredArticleSchema.parse(article);
      const key = normalizeUrl(
        typeof article.source === "string" ? article.source : parsed.source,
      );
      if (!result.has(key)) result.set(key, parsed);
    } catch {
      // 与 DB 版一致：单行校验失败只跳过该行
    }
  }
  return result;
}

/** 按文章主键 id 取回单篇完整 payload；未命中或校验失败返回 null */
export async function loadStructuredById(
  sourceName: string,
  id: string,
): Promise<StructuredArticle | null> {
  const articles = await readSnapshotArticles(sourceName);
  const article = articles.find((item) => item.id === id);
  if (!article) return null;
  try {
    return structuredArticleSchema.parse(article);
  } catch {
    return null;
  }
}
