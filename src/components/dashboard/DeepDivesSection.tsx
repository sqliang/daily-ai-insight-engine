// ============================================================================
// DeepDivesSection.tsx — 深度分析区组件
//
// 职责：渲染关键事件的深度分析卡片（通常 1-4 篇），每篇包含：
//   - 标题（title）：事件名称
//   - 背景（background）：事件来龙去脉
//   - 影响（impact）：对行业的短期/中期影响
//   - 后续关注（watchNext）：近期应跟踪的信号
//
// 布局设计：
//   - 三列 grid 布局（lg:grid-cols-3），移动端单列堆叠
//   - 每张卡片顶部有分隔线（border-t），与上方标题视觉区隔
//
// 数据特点：
//   - deepDives 是预生成的结构化文本，非原始 AI 抽取结果
//   - 由 AI 在 Reduce 阶段根据 topEvents 和 evidence 综合生成
// ============================================================================

import type { DailyReport } from "@/lib/agent/schema";

type DeepDivesSectionProps = {
  deepDives: DailyReport["deepDives"];
};

export function DeepDivesSection({ deepDives }: DeepDivesSectionProps) {
  return (
    <section className="mt-6 rounded-md border border-line bg-panel p-5 shadow-soft">
      <h2 className="text-lg font-semibold">关键事件深度总结</h2>
      <div className="mt-5 grid gap-5 lg:grid-cols-3">
        {deepDives.map((item) => (
          <article key={item.title} className="border-t border-line pt-4">
            <h3 className="text-base font-semibold leading-7">{item.title}</h3>
            <p className="mt-3 text-sm leading-7 text-muted">{item.background}</p>
            <p className="mt-3 text-sm leading-7 text-muted">{item.impact}</p>
            <p className="mt-3 text-sm leading-7 text-muted">{item.watchNext}</p>
          </article>
        ))}
      </div>
    </section>
  );
}
