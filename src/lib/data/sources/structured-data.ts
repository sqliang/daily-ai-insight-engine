// ============================================================================
// sources/structured-data.ts — 结构化文章数据加载
//
// 从 PostgreSQL articles 表（pipeline Stage 5 publish 写入）读取文章的
// 全量扁平 frontmatter（payload JSONB），替代旧的 04_structured 热/冷
// 文件合并逻辑——热/冷分片在 DB 中退化为 created 范围查询，URL 去重
// 由 publish 侧的主键幂等保证。
//
// 消费者：getSourceDetailEnriched() 通过本模块获取 enrichment 数据。
// ============================================================================

import { and, eq, gte, lte } from "drizzle-orm";

import type { StructuredArticle } from "@/lib/data/status";
import { structuredArticleSchema } from "@/lib/data/status";
import { getDb } from "@/lib/db/client";
import { articles } from "@/lib/db/schema";
import type { DateRange } from "./types";

/**
 * 加载指定 source 的结构化文章数据。
 *
 * 按 source_dir 过滤 articles 表；指定 dateRange 时附加 created
 * 范围条件（对齐旧实现中 archive 分片按日期筛选的语义）。
 *
 * 参数：
 *     sourceName: source 名称（对应 source_dir 列）
 *     dateRange:   可选的日期范围筛选 { from?, to? }，格式 YYYY-MM-DD
 *
 * 返回：
 *     结构化的文章数组（payload 整包经 Zod 校验）
 */
export async function loadStructuredData(
  sourceName: string,
  dateRange?: DateRange,
): Promise<StructuredArticle[]> {
  const db = getDb();

  const conditions = [eq(articles.sourceDir, sourceName)];
  if (dateRange?.from) conditions.push(gte(articles.created, dateRange.from));
  if (dateRange?.to) conditions.push(lte(articles.created, dateRange.to));

  const rows = await db
    .select({ payload: articles.payload })
    .from(articles)
    .where(and(...conditions));

  try {
    return structuredArticleSchema.array().parse(rows.map((r) => r.payload));
  } catch {
    // 存在不符合 schema 的行时整体降级为空（与旧实现的整文件容错对齐）；
    // publish 侧写入的 payload 与旧 04_structured JSON 同源，正常不会触发
    return [];
  }
}
