import type { RawArticle } from "@/lib/agent/schema";

// ============================================================================
// cleaner.ts — 文本清洗工具
//
// 在 Map 抽取之前对原始文章进行预处理：
//   1. 去除 HTML 标签（爬虫残留）
//   2. 合并多余空白字符
//   3. 截断过长文本以控制 token 消耗
//
// 这个步骤是防御性的：实际数据可能已经干净，但清洗层提供了
// 对脏数据的容忍度，避免单条异常文章导致 Map 阶段失败。
// ============================================================================

const whitespacePattern = /\s+/g;
const htmlTagPattern = /<[^>]*>/g;

// 清洗单段文本：去 HTML → 压缩空白 → trim → 截断
export function cleanText(input: string, maxLength = 4_000): string {
  return input
    .replace(htmlTagPattern, " ")
    .replace(whitespacePattern, " ")
    .trim()
    .slice(0, maxLength);
}

// 清洗整篇文章：对 title、summary、content 分别应用长度限制
// title 限制 220 字符（足够容纳中英文标题）
// summary 限制 900 字符（控制 Map 阶段的 token 消耗）
// content 限制 4000 字符（保留足够上下文同时避免超出 LLM 窗口）
export function cleanArticle(article: RawArticle): RawArticle {
  return {
    ...article,
    title: cleanText(article.title, 220),
    summary: cleanText(article.summary, 900),
    content: cleanText(article.content, 4_000),
  };
}
