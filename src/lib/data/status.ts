import { z } from "zod";

// ============================================================================
// Processing status
// ============================================================================

export const PROCESSING_STATUS = ["scout", "extracted", "analyzed"] as const;
export type ProcessingStatus = (typeof PROCESSING_STATUS)[number];

export const STATUS_CONFIG: Record<
  ProcessingStatus,
  { label: string; english: string; color: string; description: string }
> = {
  scout: {
    label: "清单",
    english: "Scout",
    color: "var(--muted)",
    description: "仅基本信息",
  },
  extracted: {
    label: "提取",
    english: "Extracted",
    color: "var(--warm)",
    description: "LLM 信息提取完成",
  },
  analyzed: {
    label: "分析",
    english: "Analyzed",
    color: "var(--accent)",
    description: "深度分析完成",
  },
};

// ============================================================================
// Label maps for display
// ============================================================================

export const EVENT_TYPE_LABELS: Record<
  string,
  { label: string; color: string }
> = {
  infrastructure_update: { label: "基建更新", color: "var(--cool)" },
  framework_tools: { label: "框架工具", color: "var(--accent)" },
  capital_movement: { label: "资本动向", color: "var(--warm)" },
  application_landing: { label: "应用落地", color: "var(--positive)" },
  policy_and_safety: { label: "政策安全", color: "var(--negative)" },
};

export const SENTIMENT_LABELS: Record<
  string,
  { label: string; color: string; icon: string }
> = {
  positive: { label: "积极", color: "var(--positive)", icon: "▲" },
  negative: { label: "消极", color: "var(--negative)", icon: "▼" },
  neutral: { label: "中性", color: "var(--muted)", icon: "─" },
  mixed: { label: "混合", color: "var(--warning)", icon: "⇅" },
};

export const EPISTEMIC_STATUS_LABELS: Record<string, string> = {
  verified_fact: "已核实",
  pr_statement: "公关声明",
  theoretical_claim: "理论主张",
  rumor_leak: "传闻/泄露",
};

export const HYPE_LEVEL_LABELS: Record<
  string,
  { label: string; color: string }
> = {
  low: { label: "低 hype", color: "var(--positive)" },
  medium: { label: "中 hype", color: "var(--warm)" },
  high: { label: "高 hype", color: "var(--negative)" },
};

export const ACTIONABLE_INSIGHT_LABELS: Record<
  string,
  { label: string; color: string }
> = {
  strategic_invest: { label: "策略投资", color: "var(--accent)" },
  monitor: { label: "持续监测", color: "var(--muted)" },
  deep_dive: { label: "深度研判", color: "var(--warm)" },
  speculative_watch: { label: "前瞻关注", color: "var(--cool)" },
  ignore: { label: "可忽略", color: "var(--muted)" },
};

// ============================================================================
// Zod schema for structured article data (from 04_structured/{source}.json)
// ============================================================================

export const structuredArticleSchema = z
  .object({
    id: z.string(),
    source_dir: z.string(),
    title: z.string(),
    source: z.string(),
    author: z.array(z.string()).default([]),
    published: z.string().optional(),
    created: z.string().optional(),
    description: z.string().optional(),
    tags: z.array(z.string()).default([]),
    source_type: z.string().optional(),
    // Stage 2 extraction fields
    tldr: z.string().optional(),
    objective_summary: z.string().optional(),
    event_type: z.string().optional(),
    epistemic_status: z.string().optional(),
    entities: z
      .object({
        companies: z.array(z.string()).default([]),
        technologies: z.array(z.string()).default([]),
        key_people: z.array(z.string()).default([]),
      })
      .optional(),
    key_logic_flow: z.array(z.string()).default([]),
    // Stage 3 analysis fields
    impact_score: z
      .object({
        score: z.number(),
        reason: z.string(),
      })
      .optional(),
    sentiment: z.string().optional(),
    hype_assessment: z
      .object({
        level: z.string(),
        reason: z.string(),
      })
      .optional(),
    domain_disruption: z
      .object({
        technical_innovation: z.string(),
        business_model: z.string(),
      })
      .optional(),
    compound_value: z
      .object({
        score: z.number(),
        reason: z.string(),
      })
      .optional(),
    developer_sentiment: z
      .object({
        tone: z.string(),
        primary_focus: z.string(),
      })
      .optional(),
    risk_matrix: z
      .object({
        regulatory: z.string().optional(),
        technological: z.string().optional(),
        competitive: z.string().optional(),
        ethical: z.string().optional(),
        additional: z.array(z.string()).default([]),
      })
      .optional(),
    confidence: z
      .object({
        impact: z.string().optional(),
        compound: z.string().optional(),
        hype: z.string().optional(),
      })
      .optional(),
    actionable_insight: z.string().optional(),
    information_entropy: z.string().optional(),
    engineering_complexity: z.string().optional(),
    moat_impact: z.string().optional(),
    value_capture_layer: z.string().optional(),
    key_beneficiaries: z.array(z.string()).default([]),
    competitive_casualty: z.array(z.string()).default([]),
    market_opportunities: z.array(z.string()).default([]),
  })
  .passthrough();

export type StructuredArticle = z.infer<typeof structuredArticleSchema>;

// ============================================================================
// Status detection
// ============================================================================

export function determineProcessingStatus(
  article: StructuredArticle,
): ProcessingStatus {
  if (article.impact_score && article.sentiment) {
    return "analyzed";
  }
  if (article.tldr || article.objective_summary) {
    return "extracted";
  }
  return "scout";
}
