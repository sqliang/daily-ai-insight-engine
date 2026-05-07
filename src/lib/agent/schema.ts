import { z } from "zod";

// ============================================================================
// schema.ts — 数据契约定义层
//
// 本文件是整个工程的"单一事实来源"(single source of truth)。所有 Zod schema
// 同时被以下模块消费：
//   - 离线流水线 (scripts/run-pipeline.ts) → 校验 Map/Reduce 各阶段产物
//   - AI 抽取层 (src/lib/agent/index.ts)      → 校验 LLM 输出 & 启发式结果
//   - 验证脚本 (scripts/validate-report.ts)   → 回归校验数据完整性
//   - 看板页面 (src/app/page.tsx)             → TypeScript 类型推导保障类型安全
//
// 数据流：RawArticle → [Map] → StructuredInsight → [Reduce] → DailyReport
// 每一步的输出都由对应的 schema 做 .parse() 校验，确保数据契约不被破坏。
// ============================================================================

export const languageSchema = z.enum(["zh", "en", "mixed"]);

export const eventTypeSchema = z.enum([
  "model_release",         // 模型发布：如 GPT-5、Claude 4 等基座模型发布
  "product_launch",        // 产品发布：面向终端用户的应用/功能上线
  "research_breakthrough", // 研究突破：论文、基准测试、学术进展
  "policy_regulation",     // 政策监管：法规、合规、安全治理
  "funding_market",        // 资本市场：融资、估值、IPO、收购
  "open_source",           // 开源生态：模型权重、工具链、社区贡献
  "safety_risk",           // 安全风险：版权、滥用、偏见、事故
  "industry_adoption",     // 行业落地：企业客户、部署案例、垂直场景
]);

export const sentimentSchema = z.enum(["positive", "neutral", "negative", "mixed"]);

export const rawArticleSchema = z.object({
  // RawArticle 是流水线的入口数据结构。每条记录须包含来源 URL 和信源名称，
  // 确保最终报告中的每一条洞察都可追溯到原始语料。
  id: z.string(),
  title: z.string().min(4),
  url: z.string().url(),
  source: z.string().min(2),
  language: languageSchema,
  publishedAt: z.string(),
  summary: z.string().min(20),
  content: z.string().min(80),
});

export const entitySchema = z.object({
  // 实体抽取是结构化的核心：从非结构化文本中识别公司、技术、人物、产品、地区，
  // 为后续的频次统计、影响力评分和趋势判断提供结构化特征。
  companies: z.array(z.string()).default([]),
  technologies: z.array(z.string()).default([]),
  people: z.array(z.string()).default([]),
  products: z.array(z.string()).default([]),
  regions: z.array(z.string()).default([]),
});

export const structuredInsightSchema = z.object({
  // StructuredInsight 是 Map 阶段的输出：一条原始文章 → 一组紧凑的结构化特征。
  // 这些特征可被排序、分组、可视化和审计，是 Reduce 聚合的唯一输入。
  articleId: z.string(),
  title: z.string(),
  source: z.string(),
  url: z.string().url(),
  publishedAt: z.string(),
  eventType: eventTypeSchema,
  topicTags: z.array(z.string()).min(1).max(8),
  entities: entitySchema,
  sentiment: sentimentSchema,
  impactScore: z.number().int().min(1).max(10),   // 影响力 1-10，用于排序和筛选 Top 事件
  urgencyScore: z.number().int().min(1).max(10),   // 紧迫度 1-10，辅助判断是否需要即时响应
  keyFacts: z.array(z.string()).min(2).max(5),      // 关键事实摘要（2-5 条）
  analyticalSummary: z.string().min(40),             // 分析摘要（≥40 字符）
  risks: z.array(z.string()).max(4),                 // 风险提示（最多 4 条）
  opportunities: z.array(z.string()).max(4),         // 机会提示（最多 4 条）
  confidence: z.number().min(0).max(1),              // 抽取置信度 0-1
});

export const topEventSchema = z.object({
  title: z.string(),
  articleIds: z.array(z.string()).min(1),
  eventType: eventTypeSchema,
  impactScore: z.number().int().min(1).max(10),
  whyItMatters: z.string(),                        // 为什么重要：面向决策者的简短判断
  evidence: z.array(z.string()).min(1).max(4),      // 支撑证据（1-4 条原文关键事实）
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
      score: z.number().int().min(1).max(10),
    }),
  ),
  entityFrequency: z.array(
    z.object({
      entity: z.string(),
      count: z.number().int().positive(),
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

export const rawArticleListSchema = z.array(rawArticleSchema).min(10).max(20);
export const structuredInsightListSchema = z.array(structuredInsightSchema);

export type RawArticle = z.infer<typeof rawArticleSchema>;
export type StructuredInsight = z.infer<typeof structuredInsightSchema>;
export type DailyReport = z.infer<typeof dailyReportSchema>;
export type EventType = z.infer<typeof eventTypeSchema>;
export type Sentiment = z.infer<typeof sentimentSchema>;
