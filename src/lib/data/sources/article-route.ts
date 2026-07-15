// ============================================================================
// article-route.ts — Source 文章详情页路由工具
//
// 纯字符串工具，不依赖 node:fs，供客户端卡片和服务端数据层共同使用。
// ============================================================================

import type { EnrichedArticle } from "./types";

/**
 * 规范化文章 URL，用于生成和匹配缺 ID 文章的兜底 slug。
 */
export function normalizeArticleUrl(url: string): string {
  return url
    .trim()
    .replace(/\/+$/, "")
    .replace(/^http:\/\//i, "http://")
    .replace(/^https:\/\//i, "https://");
}

function encodeUrlSlug(url: string): string {
  return btoa(normalizeArticleUrl(url))
    .replace(/\+/g, "-")
    .replace(/\//g, "_")
    .replace(/=+$/, "");
}

/**
 * 解码 URL 兜底 slug。非法 slug 返回 null，由调用方进入 404。
 */
export function decodeUrlSlug(slug: string): string | null {
  try {
    const normalized = slug.replace(/-/g, "+").replace(/_/g, "/");
    const padded = normalized.padEnd(
      normalized.length + ((4 - (normalized.length % 4)) % 4),
      "=",
    );
    return atob(padded);
  } catch {
    return null;
  }
}

/**
 * 获取文章详情页使用的稳定 route id。
 */
export function getArticleRouteId(article: Pick<EnrichedArticle, "id" | "url">): string {
  return article.id ?? `url-${encodeUrlSlug(article.url)}`;
}

/**
 * 拼装 source 文章详情页链接，保留当前筛选和排序参数。
 */
export function buildArticleDetailHref(
  sourceName: string,
  article: Pick<EnrichedArticle, "id" | "url">,
  searchParams?: URLSearchParams | string,
): string {
  const suffix =
    typeof searchParams === "string"
      ? searchParams
      : searchParams?.toString() ?? "";
  const base = `/sources/${sourceName}/articles/${getArticleRouteId(article)}`;
  return suffix ? `${base}?${suffix}` : base;
}
