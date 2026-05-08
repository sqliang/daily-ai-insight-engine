import type { EventType, Sentiment } from "@/lib/agent/schema";

// ============================================================================
// labels.ts — 中文标签映射表
//
// 所有面向用户的展示文本集中维护在此文件中，避免在各组件中散落硬编码字符串。
// 当需要国际化或标签调整时，只需修改此处即可全局生效。
// 被 page.tsx、SignalList.tsx、heuristics.ts 等模块引用。
// ============================================================================

export const eventTypeLabels: Record<EventType, string> = {
  infrastructure_update: "基建更新",
  framework_tools: "框架工具",
  capital_movement: "资本动向",
  application_landing: "应用落地",
  policy_and_safety: "政策与安全",
};

export const sentimentLabels: Record<Sentiment, string> = {
  positive: "正向",
  neutral: "中性",
  negative: "负向",
  mixed: "混合",
};

export const severityLabels = {
  low: "低",
  medium: "中",
  high: "高",
} as const;
