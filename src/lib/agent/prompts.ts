import type { RawArticle, StructuredInsight } from "@/lib/agent/schema";

// ============================================================================
// prompts.ts — LLM 提示词模板
//
// 本文件维护两套 System Prompt 和对应的 User Prompt 构造器：
//   1. Extractor  — Map 阶段：从单篇文章中抽取结构化特征
//   2. Synthesizer — Reduce 阶段：从结构化特征中生成分析报告
//
// 设计原则：
//   - 每个 Prompt 只处理一条文章或一组已校验的结构化数据，
//     禁止将原始语料整体丢给 LLM（避免幻觉放大和 token 浪费）。
//   - 所有 Prompt 均要求"仅返回合法 JSON"，配合 schema.ts 的 Zod 校验，
//     形成类型安全的双保险（LLM 输出 → JSON.parse → Zod.parse）。
// ============================================================================

export const extractorSystemPrompt = `
You are a senior AI industry analyst. Extract one news item into strict JSON.
Do not summarize loosely. Capture entities, event type, sentiment, impact, urgency,
key facts, risks, opportunities, and confidence. Prefer evidence-backed judgment.
`.trim();

export const synthesizerSystemPrompt = `
You are generating a daily AI industry insight report from pre-structured article facts.
Use only the provided structured insights. Rank events by impact and evidence density.
Produce concise Chinese analysis with clear business and technology reasoning.
`.trim();

export function buildExtractorPrompt(article: RawArticle): string {
  return `
Return only valid JSON matching StructuredInsight.

Article:
id: ${article.id}
title: ${article.title}
source: ${article.source}
publishedAt: ${article.publishedAt}
url: ${article.url}
summary: ${article.summary}
content: ${article.content}
`.trim();
}

export function buildSynthesizerPrompt(insights: StructuredInsight[]): string {
  return `
Return only valid JSON matching DailyReport.

Structured insights:
${JSON.stringify(insights, null, 2)}
`.trim();
}
