// ============================================================================
// DistributionSection.tsx — 分布图表区组件
//
// 职责：渲染事件类型分布和情感分布两个柱状图，以双栏布局展示。
//
// 数据处理：
//   - eventTypeDistribution：原始 label（英文枚举）→ 中文标签（eventTypeLabels）
//   - sentimentDistribution：原始 label（英文枚举）→ 中文标签（sentimentLabels）
//   - Bars 组件负责归一化渲染，以最大值为 100% 计算各柱宽度
//
// 布局设计：
//   - 两列 grid 布局（grid gap-5），上下排列于主内容区
//   - sentimentBars 使用 tone="amber"（暖色）区分于默认的 signal 色
//
// 复用说明：
//   - 此组件组合了 Bars 组件，实现分布数据的免打扰渲染
//   - 如需调整柱条样式，仅需修改 Bars 组件或传入不同 tone 参数
// ============================================================================

import { Bars } from "@/components/dashboard/Bars";
import { eventTypeLabels, sentimentLabels } from "@/lib/report/labels";
import type { DailyReport } from "@/lib/agent/schema";

type DistributionSectionProps = {
  visualizationData: DailyReport["visualizationData"];
};

export function DistributionSection({ visualizationData }: DistributionSectionProps) {
  const eventBars = visualizationData.eventTypeDistribution.map((item) => ({
    label: eventTypeLabels[item.label],
    value: item.count,
  }));

  const sentimentBars = visualizationData.sentimentDistribution.map((item) => ({
    label: sentimentLabels[item.label],
    value: item.count,
  }));

  return (
    <div className="grid gap-5">
      <Bars title="事件类型分布" data={eventBars} />
      <Bars title="情绪分布" data={sentimentBars} tone="amber" />
    </div>
  );
}
