// ============================================================================
// sources/manifests.ts — Manifest 文件加载、合并和 URL 规范化
//
// 负责读取 data/00_manifest/ 目录下的 JSON 文件，解析并校验 manifest
// schema，按 source 分组去重（保留最新的 manifest），以及跨 manifest
// 的文章合并。
// ============================================================================

import { readFile, readdir } from "node:fs/promises";
import { join } from "node:path";
import { z } from "zod";
import { manifestSchema } from "./types";

// ---------------------------------------------------------------------------
// 路径常量
// ---------------------------------------------------------------------------

const MANIFEST_DIR = join(process.cwd(), "data/00_manifest");

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

/**
 * 加载所有 source 的最新 manifest。
 *
 * 扫描 data/00_manifest/ 目录，对每个 source 只保留 generated_at 最新
 * 的那份 manifest。
 *
 * 返回：
 *     Map<source名称, manifest数据>，目录不存在或为空时返回空 Map
 */
export async function loadManifests(): Promise<
  Map<string, z.infer<typeof manifestSchema>>
> {
  const manifests = new Map<string, z.infer<typeof manifestSchema>>();
  let entries: string[];
  try {
    entries = await readdir(MANIFEST_DIR);
  } catch {
    return manifests;
  }

  for (const filename of entries) {
    if (!filename.endsWith(".json")) continue;
    const sourceName = filename.replace(/_\d{4}-\d{2}-\d{2}\.json$/, "");
    try {
      const raw = await readFile(join(MANIFEST_DIR, filename), "utf8");
      const data = manifestSchema.parse(JSON.parse(raw));
      // Keep only the newest manifest per source
      const existing = manifests.get(sourceName);
      if (!existing || data.generated_at > existing.generated_at) {
        manifests.set(sourceName, data);
      }
    } catch {
      // Skip malformed manifest files silently
    }
  }
  return manifests;
}

/**
 * 加载指定 source 的所有历史 manifest（按 generated_at 降序排列）。
 *
 * 参数：
 *     sourceName: source 名称，对应 manifest 文件名前缀
 *
 * 返回：
 *     manifest 数组，按 generated_at 降序排列
 */
export async function loadManifestsForSource(
  sourceName: string,
): Promise<z.infer<typeof manifestSchema>[]> {
  const manifests: z.infer<typeof manifestSchema>[] = [];
  let entries: string[];
  try {
    entries = await readdir(MANIFEST_DIR);
  } catch {
    return manifests;
  }

  const prefix = `${sourceName}_`;
  for (const filename of entries) {
    if (!filename.startsWith(prefix) || !filename.endsWith(".json")) continue;
    try {
      const raw = await readFile(join(MANIFEST_DIR, filename), "utf8");
      const data = manifestSchema.parse(JSON.parse(raw));
      manifests.push(data);
    } catch {
      // Skip malformed manifest files silently
    }
  }

  manifests.sort((a, b) => b.generated_at.localeCompare(a.generated_at));
  return manifests;
}

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
