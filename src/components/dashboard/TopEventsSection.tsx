// ============================================================================
// TopEventsSection.tsx — Top 事件列表组件
//
// 职责：渲染今日 Top 事件列表（通常为 3-5 条），每条事件包含：
//   - 事件排名（#1、#2...）
//   - 事件类型标签（如"模型发布"、"政策监管"）
//   - 事件标题（核心事件描述）
//   - 影响力评分（Impact Score 1-10）
//   - 为什么重要（whyItMatters）：面向决策者的简短判断
//   - 支撑证据（evidence）：2-4 条原文关键事实
//
// 数据处理：
//   - eventTypeLabels 映射将英文枚举值转为中文展示标签
//   - 组件本身不修改数据，仅做展示层映射
//
// 设计决策：
//   - 每条事件以 article 结构渲染，内部以 divide-y 分隔
//   - first:pt-0 / last:pb-0 避免首尾多余间距
//   - 影响力评分以边框标签形式展示，颜色使用主题色 signal
// ============================================================================

import { eventTypeLabels } from "@/lib/report/labels";
import type { DailyReport } from "@/lib/agent/schema";

type TopEventsSectionProps = {
  topEvents: DailyReport["topEvents"];
};

export function TopEventsSection({ topEvents }: TopEventsSectionProps) {
  return (
    <section className="rounded-md border border-line bg-panel p-5 shadow-soft">
      <h2 className="text-lg font-semibold">今日 Top 事件</h2>
      <div className="mt-5 divide-y divide-line">
        {topEvents.map((event, index) => (
          <article key={event.title} className="py-5 first:pt-0 last:pb-0">
            <div className="flex flex-col gap-3 md:flex-row md:items-start md:justify-between">
              <div>
                <p className="text-sm text-muted">#{index + 1} · {eventTypeLabels[event.eventType]}</p>
                <h3 className="mt-1 text-xl font-semibold leading-8">{event.title}</h3>
              </div>
              <span className="w-fit rounded-sm border border-signal px-2 py-1 text-sm font-medium text-signal">
                Impact {event.impactScore}/10
              </span>
            </div>
            <p className="mt-3 text-sm leading-7 text-muted">{event.whyItMatters}</p>
            <ul className="mt-3 space-y-2 text-sm leading-6 text-muted">
              {event.evidence.map((item) => (
                <li key={item}>· {item}</li>
              ))}
            </ul>
          </article>
        ))}
      </div>
    </section>
  );
}
