// ============================================================================
// RankingsSection.tsx — 影响力排名与高频实体组件
//
// 职责：以双栏布局渲染两个 Bars 柱状图：
//   1. 影响力排名（impactRanking）：取 Top 6 事件，按 score 降序
//      - label 使用事件标题（title），而非枚举值
//      - score 范围 1-10，归一化后展示
//   2. 高频实体（entityFrequency）：取 Top 8 实体，按出现频次降序
//      - label 使用实体名称（entity）
//      - count 为出现次数
//
// 数据处理：
//   - impactRanking 截取前 6 条（.slice(0, 6)）
//   - entityFrequency 截取前 8 条（.slice(0, 8)）
//   - 截取逻辑在组件内部完成，保持 page.tsx 数据流简洁
//
// 布局设计：
//   - 双列 grid 布局（lg:grid-cols-2）
//   - impactRanking 使用 tone="berry"（冷色）突出重要性
//   - entityFrequency 使用默认 signal 色
// ============================================================================

import { Bars } from "@/components/dashboard/Bars";
import type { DailyReport } from "@/lib/agent/schema";

type RankingsSectionProps = {
  visualizationData: DailyReport["visualizationData"];
};

export function RankingsSection({ visualizationData }: RankingsSectionProps) {
  const impactBars = visualizationData.impactRanking.slice(0, 6).map((item) => ({
    label: item.title,
    value: item.score,
  }));

  const entityBars = visualizationData.entityFrequency.slice(0, 8).map((item) => ({
    label: item.entity,
    value: item.count,
  }));

  return (
    <section className="mt-6 grid gap-5 lg:grid-cols-2">
      <Bars title="影响力排名" data={impactBars} tone="berry" />
      <Bars title="高频实体" data={entityBars} />
    </section>
  );
}
