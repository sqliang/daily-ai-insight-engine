import { z } from "zod";

// ============================================================================
// schema.ts — 数据契约定义层
//
// 本文件是整个工程的"单一事实来源"(single source of truth)。所有 Zod schema
// 被看板页面和报告页面消费，提供 TypeScript 类型推导保障类型安全。
// DailyReport 是 Python 流水线的最终产物，看板页面通过 Zod parse 校验后渲染。
// ============================================================================

export const languageSchema = z.enum(["zh", "en", "mixed"]);

export const eventTypeSchema = z.enum([
  "infrastructure_update",   // 基建更新：新模型发布、芯片算力更新、训练框架升级
  "framework_tools",         // 框架与工具：新的 Agent 框架、开发者工具开源、API 标准
  "capital_movement",        // 资本动向：巨额融资、并购、财报、IPO
  "application_landing",     // 应用落地：具体的 ToB/ToC AI 产品发布与迭代
  "policy_and_safety",       // 政策与安全：监管、版权诉讼、安全事故、伦理争议
  "unknown",                 // 未知分类：LLM 无法确定事件类型时的兜底值
]);

export const sentimentSchema = z.enum(["positive", "neutral", "negative", "mixed"]);

export const evidenceSourceSchema = z.object({
  sourceDir: z.string(),    // 信源目录名，如 "theverge"
  title: z.string(),        // 文章标题
  url: z.string(),          // 原文 URL
});

export const topEventSchema = z.object({
  title: z.string(),
  articleIds: z.array(z.string()).min(1),
  eventType: eventTypeSchema,
  impactScore: z.number().min(1).max(10),
  whyItMatters: z.string(),                        // 为什么重要：面向决策者的简短判断
  evidence: z.array(z.string()).min(2).max(6),      // 支撑证据（2-6 条原文关键事实）
  evidenceArticleIds: z.array(z.array(z.string())).optional(), // 每条 evidence 对应的 articleId 列表
  evidenceSources: z.array(evidenceSourceSchema).optional(),  // 来源链接，pipeline 后处理解析
});

export const deepDiveSchema = z.object({
  title: z.string(),
  background: z.string(),   // 背景：事件来龙去脉
  impact: z.string(),       // 影响：对行业的短期/中期影响
  watchNext: z.string(),    // 后续关注：近期应跟踪的信号
});

export const trendInsightSchema = z.object({
  dimension: z.enum(["technology", "application", "policy", "capital"]),
  judgment: z.string(),
  supportingSignals: z.array(z.string()).min(1).max(5),
});

export const signalSchema = z.object({
  signal: z.string(),                              // 信号描述
  severity: z.enum(["low", "medium", "high"]),     // 严重程度
  rationale: z.string(),                           // 判断依据
});

// visualizationData 是预先计算好的可视化数据，使 Next.js 页面保持纯展示逻辑。
// 页面无需再做聚合计算，只需读取已生成的分布数据和排名即可渲染图表。
export const visualizationDataSchema = z.object({
  eventTypeDistribution: z.array(
    z.object({
      label: eventTypeSchema,
      count: z.number().int().nonnegative(),
    }),
  ),
  sentimentDistribution: z.array(
    z.object({
      label: sentimentSchema,
      count: z.number().int().nonnegative(),
    }),
  ),
  impactRanking: z.array(
    z.object({
      articleId: z.string(),
      title: z.string(),
      score: z.number().min(1).max(10),
    }),
  ),
  entityFrequency: z.array(
    z.object({
      entity: z.string(),
      count: z.number().int().nonnegative(),
      type: z.enum(["company", "technology", "person", "product", "region"]),
    }),
  ),
});

export const dailyReportSchema = z.object({
  // DailyReport 是 Reduce 阶段的最终输出，也是整个流水线的唯一对外产物。
  // 它包含人类可读的分析文本 + 预计算的可视化数据，
  // 使 Next.js 看板页面可以完全无状态、纯展示地渲染。
  date: z.string(),
  generatedAt: z.string(),
  reportTitle: z.string(),
  executiveSummary: z.string(),                     // 执行摘要：30 秒了解今日要点
  dataSourceSummary: z.object({
    totalArticles: z.number().int().nonnegative(),
    sources: z.array(z.string()),
    languages: z.array(languageSchema),
    selectionRationale: z.string(),                 // 信源选择说明
  }),
  topEvents: z.array(topEventSchema).min(3).max(5),
  deepDives: z.array(deepDiveSchema).min(1).max(4),
  trendInsights: z.array(trendInsightSchema).min(3).max(4),
  riskSignals: z.array(signalSchema),
  opportunitySignals: z.array(signalSchema),
  visualizationData: visualizationDataSchema,
});

export type DailyReport = z.infer<typeof dailyReportSchema>;
export type EvidenceSource = z.infer<typeof evidenceSourceSchema>;
export type EventType = z.infer<typeof eventTypeSchema>;
export type Sentiment = z.infer<typeof sentimentSchema>;
