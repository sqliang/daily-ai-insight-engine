// ============================================================================
// sources/manifests.ts — Manifest 加载、合并和 URL 规范化（DB + 快照回退）
//
// 正常从 PostgreSQL manifests 表读取；只有 DB 抛错时才回退到
// data/snapshot/manifests/{source}.json。DB 返回空 Map / 空数组不回退。
// URL 规范化与跨 manifest 合并仍是与存储层无关的纯函数。
// React cache() 保留请求内去重（issue #152）。
// ============================================================================

import { cache } from "react";
import { eq, sql } from "drizzle-orm";
import { z } from "zod";

import { withDbFallback } from "@/lib/data/snapshot/fallback";
import {
  loadManifests as loadManifestsFromSnapshot,
  loadManifestsForSource as loadManifestsForSourceFromSnapshot,
} from "@/lib/data/snapshot/manifests";
import { getDb } from "@/lib/db/client";
import { manifests as manifestsTable } from "@/lib/db/schema";
import { manifestSchema } from "./types";

// ---------------------------------------------------------------------------
// URL 规范化
// ---------------------------------------------------------------------------

/**
 * 规范化 URL 用于去重比较。
 *
 * 去除尾部斜杠，统一 http/https 协议前缀的大小写。
 */
export function normalizeUrl(url: string): string {
  return url
    .trim()
    .replace(/\/+$/, "")
    .replace(/^http:\/\//i, "http://")
    .replace(/^https:\/\//i, "https://");
}

// ---------------------------------------------------------------------------
// Manifest 文件加载
// ---------------------------------------------------------------------------

/** 从 manifests 表加载所有 source 的最新 manifest */
async function loadManifestsFromDb(): Promise<
  Map<string, z.infer<typeof manifestSchema>>
> {
  const db = getDb();
  const rows = await db
    .selectDistinctOn([manifestsTable.source], {
      source: manifestsTable.source,
      payload: manifestsTable.payload,
    })
    .from(manifestsTable)
    // generated_at 可能为空（历史数据缺字段），NULLS LAST 保证有效值优先
    .orderBy(
      manifestsTable.source,
      sql`${manifestsTable.generatedAt} DESC NULLS LAST`,
    );

  const result = new Map<string, z.infer<typeof manifestSchema>>();
  for (const row of rows) {
    try {
      result.set(row.source, manifestSchema.parse(row.payload));
    } catch {
      // 跳过校验失败的行（数据损坏或格式不兼容）
    }
  }
  return result;
}

/**
 * 加载所有 source 的最新 manifest（Map<source, manifest>）。
 * React cache() 保留请求内去重；DB 抛错时回退到快照各源首条记录。
 */
export const loadManifests = cache(
  withDbFallback(loadManifestsFromDb, loadManifestsFromSnapshot),
);

/** 从 manifests 表加载指定 source 的全部历史 manifest */
async function loadManifestsForSourceFromDb(
  sourceName: string,
): Promise<z.infer<typeof manifestSchema>[]> {
  const db = getDb();
  const rows = await db
    .select({ payload: manifestsTable.payload })
    .from(manifestsTable)
    .where(eq(manifestsTable.source, sourceName))
    .orderBy(sql`${manifestsTable.generatedAt} DESC NULLS LAST`);

  const result: z.infer<typeof manifestSchema>[] = [];
  for (const row of rows) {
    try {
      result.push(manifestSchema.parse(row.payload));
    } catch {
      // 跳过校验失败的行
    }
  }
  return result;
}

/**
 * 加载指定 source 的所有历史 manifest（按 generated_at / date 降序）。
 * React cache() 保留请求内去重；DB 抛错时回退到快照完整数组。
 */
export const loadManifestsForSource = cache(
  withDbFallback(
    loadManifestsForSourceFromDb,
    loadManifestsForSourceFromSnapshot,
  ),
);

// ---------------------------------------------------------------------------
// 多 manifest 文章合并
// ---------------------------------------------------------------------------

/**
 * 将多个 manifest 中的文章合并去重。
 *
 * 使用 normalizeUrl 进行 URL 去重，先出现的文章优先保留。
 * 用于 dateRange 模式下聚合多个日期的 manifest 数据。
 */
export function mergeArticlesFromManifests(
  manifests: z.infer<typeof manifestSchema>[],
): Array<{
  url: string;
  title: string;
  published: string;
  summary: string;
  author: string;
  id?: string;
}> {
  const seen = new Set<string>();
  const merged: Array<{
    url: string;
    title: string;
    published: string;
    summary: string;
    author: string;
    id?: string;
  }> = [];

  for (const manifest of manifests) {
    for (const article of manifest.articles) {
      const key = normalizeUrl(article.url);
      if (seen.has(key)) continue;
      seen.add(key);
      merged.push({
        url: article.url,
        title: article.title,
        published: article.published ?? "",
        summary: article.summary ?? "",
        author: article.author ?? "",
        id: article.id,
      });
    }
  }

  return merged;
}
