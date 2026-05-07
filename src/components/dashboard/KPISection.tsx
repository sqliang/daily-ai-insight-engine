// ============================================================================
// KPISection.tsx — KPI 指标卡片区组件
//
// 职责：渲染日报首屏的三个核心 KPI 指标卡片，向审阅者快速传达：
//   1. 样本量（totalArticles）：当日处理的原始文章数量
//   2. 信源数（sources）：覆盖的不同媒体/平台数量
//   3. 语言覆盖（languages）：中英文信源混合情况
//
// 每个卡片包含：
//   - 指标标签（label）
//   - 核心数值（value）：大字高亮显示
//   - 辅助说明（helper）：解释该指标的统计口径或意义
//
// 设计决策：
//   - 响应式三列布局（md:grid-cols-3），移动端单列堆叠
//   - MetricCard 内部已包含样式封装，此组件仅做数据映射和布局
// ============================================================================

import { MetricCard } from "@/components/dashboard/MetricCard";
import type { DailyReport } from "@/lib/agent/schema";

type KPISectionProps = {
  dataSourceSummary: DailyReport["dataSourceSummary"];
};

export function KPISection({ dataSourceSummary }: KPISectionProps) {
  return (
    <section className="mt-6 grid gap-4 md:grid-cols-3">
      <MetricCard
        label="样本量"
        value={dataSourceSummary.totalArticles}
        helper="逐篇 Map 抽取后再 Reduce 聚合"
      />
      <MetricCard
        label="信源数"
        value={dataSourceSummary.sources.length}
        helper={dataSourceSummary.sources.slice(0, 4).join(" / ")}
      />
      <MetricCard
        label="语言覆盖"
        value={dataSourceSummary.languages.join(" + ")}
        helper="混合中英文信源，兼顾全球与本土语境"
      />
    </section>
  );
}
