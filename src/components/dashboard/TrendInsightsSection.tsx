// ============================================================================
// TrendInsightsSection.tsx — 趋势判断区组件
//
// 职责：渲染技术/应用/政策/资本四维趋势判断，每维包含：
//   - 维度标签（dimension）：uppercase 小号字体突出，如"TECHNOLOGY"
//   - 判断结论（judgment）：该维度的核心趋势判断
//   - 支撑信号（supportingSignals）：1-5 条支撑该判断的证据
//
// 数据映射：
//   - supportingSignals 数组以中文分号（；）拼接为单段文字
//   - 拼接逻辑在组件内部完成，保持模板简洁
//
// 布局设计：
//   - 双列 grid 布局（md:grid-cols-2），每张卡片独立边框
//   - 卡片内 padding 为 p-4，保证内容不贴边
//   - 维度标签使用 uppercase + 主题色 signal，形成视觉锚点
// ============================================================================

import type { DailyReport } from "@/lib/agent/schema";

type TrendInsightsSectionProps = {
  trendInsights: DailyReport["trendInsights"];
};

export function TrendInsightsSection({ trendInsights }: TrendInsightsSectionProps) {
  return (
    <section className="mt-6 rounded-md border border-line bg-panel p-5 shadow-soft">
      <h2 className="text-lg font-semibold">趋势判断</h2>
      <div className="mt-5 grid gap-4 md:grid-cols-2">
        {trendInsights.map((trend) => (
          <article key={trend.dimension} className="rounded-md border border-line p-4">
            <p className="text-sm font-medium uppercase tracking-normal text-signal">{trend.dimension}</p>
            <h3 className="mt-2 text-base font-semibold leading-7">{trend.judgment}</h3>
            <p className="mt-3 text-sm leading-7 text-muted">{trend.supportingSignals.join("；")}</p>
          </article>
        ))}
      </div>
    </section>
  );
}
