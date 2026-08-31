// ============================================================================
// schema.ts — 站点数据库表结构（Drizzle 定义）
//
// 三张表承载站点全部数据面：
//   daily_reports — 日报（Stage 4b 产物，JSONB 整存 + Markdown 全文）
//   manifests     — 抓取 URL 清单（Stage 1a 产物，按 source+date 整存）
//   articles      — 文章结构化字段（Stage 1b–3 的 frontmatter 汇总，
//                   标量列用于筛选/排序，payload JSONB 保留全量扁平字段）
//
// 写入方：pipeline Stage 5 publish（psycopg upsert）；前端只读。
// drizzle-kit 依据本文件生成迁移 SQL（见 drizzle.config.ts）。
// ============================================================================

import {
  date,
  index,
  jsonb,
  numeric,
  pgTable,
  text,
  timestamp,
  primaryKey,
} from "drizzle-orm/pg-core";

// ---------------------------------------------------------------------------
// daily_reports — 日报（date 主键，report 整存对齐 Zod dailyReportSchema）
// ---------------------------------------------------------------------------

export const dailyReports = pgTable("daily_reports", {
  /** 日报日期，YYYY-MM-DD */
  date: text("date").primaryKey(),
  /** DailyReport 完整 JSON（camelCase，与 src/lib/agent/schema.ts 对齐） */
  report: jsonb("report").notNull(),
  /** Markdown 全文（/report/[date] 直读；为空时前端降级为 JSON→Markdown） */
  reportMd: text("report_md"),
  generatedAt: timestamp("generated_at", { withTimezone: true }),
});

// ---------------------------------------------------------------------------
// manifests — URL 清单（source+date 复合主键，payload 整存含 articles 数组）
// ---------------------------------------------------------------------------

export const manifests = pgTable(
  "manifests",
  {
    /** 数据源名（目录名），如 arxiv-cs-ai */
    source: text("source").notNull(),
    /** manifest 日期，YYYY-MM-DD */
    date: text("date").notNull(),
    generatedAt: timestamp("generated_at", { withTimezone: true }),
    /** manifest 完整 JSON：{source, source_type, tier, generated_at, date, articles[]} */
    payload: jsonb("payload").notNull(),
  },
  (t) => [primaryKey({ columns: [t.source, t.date] })],
);

// ---------------------------------------------------------------------------
// articles — 文章结构化字段（id 主键；payload 为全量扁平 frontmatter）
// ---------------------------------------------------------------------------

export const articles = pgTable(
  "articles",
  {
    /** SHA-256(url) 前 16 位 hex，pipeline 侧生成 */
    id: text("id").primaryKey(),
    /** 数据源目录名（04_structured 的 {source}） */
    sourceDir: text("source_dir").notNull(),
    /** 入库日期（时间筛选基准，frontmatter 的 created） */
    created: date("created").notNull(),
    published: text("published"),
    /** 原文 URL（frontmatter 的 source 字段） */
    url: text("url"),
    title: text("title"),
    author: text("author"),
    description: text("description"),
    tldr: text("tldr"),
    objectiveSummary: text("objective_summary"),
    eventType: text("event_type"),
    sentiment: text("sentiment"),
    /** 影响力评分（从 impact_score.score 拆出，排序/索引用） */
    impactScore: numeric("impact_score"),
    /**
     * 全量扁平 frontmatter（entities / object_mentions / object_insights /
     * risk_matrix 等嵌套结构都在内），对齐 structuredArticleSchema 的
     * passthrough 语义，前端读取后整包 Zod 校验。
     */
    payload: jsonb("payload").notNull(),
    updatedAt: timestamp("updated_at", { withTimezone: true }),
  },
  (t) => [
    index("articles_source_created_idx").on(t.sourceDir, t.created),
    index("articles_created_idx").on(t.created),
    index("articles_impact_score_idx").on(t.impactScore),
  ],
);
