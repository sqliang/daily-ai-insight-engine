// ============================================================================
// sources/structured-data.ts — 结构化文章数据加载（热/冷 archive 分流）
//
// 实现 CLAUDE.md 中描述的 "04_structured hot/cold split" 逻辑：
//   1. 先加载热数据 ({source}.json)
//   2. 如果指定了 dateRange，按需加载 archive 分片并合并
//
// 消费者：getSourceDetailEnriched() 通过本模块获取 enrichment 数据。
// ============================================================================

import { readFile, readdir } from "node:fs/promises";
import { join } from "node:path";
import type { StructuredArticle } from "@/lib/data/status";
import { structuredArticleSchema } from "@/lib/data/status";
import type { DateRange } from "./types";
import { normalizeUrl } from "./manifests";

/**
 * 加载指定 source 的结构化文章数据。
 *
 * 先读取热数据文件 {source}.json，如果指定了 dateRange 参数，
 * 则额外从 archive/{source}/ 目录按日期分片加载冷数据并合并。
 * URL 去重：热数据优先，冷数据中相同 URL 跳过。
 *
 * 参数：
 *     sourceName: source 名称
 *     dateRange:   可选的日期范围筛选 { from?, to? }，格式 YYYY-MM-DD
 *
 * 返回：
 *     结构化的文章数组，按热数据 + 冷数据顺序排列
 */
export async function loadStructuredData(
  sourceName: string,
  dateRange?: DateRange,
): Promise<StructuredArticle[]> {
  const structuredDir = join(process.cwd(), "data/04_structured");
  const results: StructuredArticle[] = [];

  // 1. 加载热数据 ({source}.json)
  const hotPath = join(structuredDir, `${sourceName}.json`);
  try {
    const raw = await readFile(hotPath, "utf8");
    const parsed: unknown = JSON.parse(raw);
    if (Array.isArray(parsed)) {
      const validated = structuredArticleSchema.array().parse(parsed);
      results.push(...validated);
    }
  } catch {
    // 热数据文件不存在或解析失败，继续尝试 archive
  }

  // 2. 如果指定了 dateRange，加载对应的 archive 分片
  if (dateRange?.from || dateRange?.to) {
    const archiveDir = join(structuredDir, "archive", sourceName);
    let shardFiles: string[];
    try {
      shardFiles = await readdir(archiveDir);
    } catch {
      // archive 目录不存在（老版本兼容），直接返回热数据
      return results;
    }

    const seenUrls = new Set(results.map((r) => normalizeUrl(r.source)));

    for (const filename of shardFiles) {
      if (!filename.endsWith(".json")) continue;
      // 文件名格式: {source}_{YYYY-MM-DD}.json
      const datePart = filename.replace(/\.json$/, "").split("_").pop();
      if (!datePart || datePart.length !== 10) continue;

      // 按 dateRange 筛选分片
      if (dateRange.from && datePart < dateRange.from) continue;
      if (dateRange.to && datePart > dateRange.to) continue;

      try {
        const raw = await readFile(join(archiveDir, filename), "utf8");
        const parsed: unknown = JSON.parse(raw);
        if (!Array.isArray(parsed)) continue;
        const validated = structuredArticleSchema.array().parse(parsed);
        for (const article of validated) {
          const url = normalizeUrl(article.source);
          if (!seenUrls.has(url)) {
            seenUrls.add(url);
            results.push(article);
          }
        }
      } catch {
        // 分片文件损坏，跳过
      }
    }
  }

  return results;
}
