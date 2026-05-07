import { severityLabels } from "@/lib/report/labels";
import type { DailyReport } from "@/lib/agent/schema";

// ============================================================================
// SignalList.tsx — 风险 / 机会信号列表组件
//
// 在报告底部以两列布局展示风险提示和机会提示。
// 每个信号条目包含：
//   - 信号标题
//   - 严重程度标签（低/中/高，颜色随级别变化）
//   - 判断依据说明
//
// 严重程度颜色映射：
//   - low:    灰色边框 + 灰色文字（中性，无需紧张）
//   - medium: 琥珀色（值得关注）
//   - high:   莓红色（需要重视）
// ============================================================================

type SignalListProps = {
  title: string;
  items: DailyReport["riskSignals"];
};

const severityTone = {
  low: "border-slate-300 text-slate-600",
  medium: "border-amber text-amber",
  high: "border-berry text-berry",
};

export function SignalList({ title, items }: SignalListProps) {
  return (
    <section className="rounded-md border border-line bg-panel p-5 shadow-soft">
      <h2 className="text-base font-semibold">{title}</h2>
      <div className="mt-4 space-y-4">
        {items.map((item) => (
          <article key={`${item.signal}-${item.rationale}`} className="border-t border-line pt-4 first:border-t-0 first:pt-0">
            <div className="flex items-start justify-between gap-3">
              <h3 className="text-sm font-semibold leading-6">{item.signal}</h3>
              <span className={`shrink-0 rounded-sm border px-2 py-1 text-xs ${severityTone[item.severity]}`}>
                {severityLabels[item.severity]}
              </span>
            </div>
            <p className="mt-2 text-sm leading-6 text-muted">{item.rationale}</p>
          </article>
        ))}
      </div>
    </section>
  );
}
