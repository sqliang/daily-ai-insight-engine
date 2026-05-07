// ============================================================================
// Bars.tsx — 水平柱状图组件
//
// MVP 阶段刻意使用纯 CSS 柱状图而非重量级图表库（如 ECharts/Recharts）。
// 理由：
//   1. 零依赖 —— 不增加 bundle 体积
//   2. 透明可控 —— 样式完全由 Tailwind class 控制，审查者可直接理解渲染逻辑
//   3. 满足需求 —— 事件类型分布、情感分布、影响力排名等场景中，
//      水平条已足够清晰传达分布和排序信息
//
// tone 参数控制柱状条颜色：
//   - signal (默认): 主题色，用于事件类型和实体
//   - amber:          暖色，用于情感分布
//   - berry:          冷色，用于影响力排名
// ============================================================================

type BarDatum = {
  label: string;
  value: number;
};

type BarsProps = {
  title: string;
  data: BarDatum[];
  tone?: "signal" | "amber" | "berry";
};

const toneClass = {
  signal: "bg-signal",
  amber: "bg-amber",
  berry: "bg-berry",
};

export function Bars({ title, data, tone = "signal" }: BarsProps) {
  // 以最大值为基准归一化宽度，确保最长的条占满容器，
  // 同时保证最小宽度为 8% 以避免零值条目不可见
  const max = Math.max(...data.map((item) => item.value), 1);

  return (
    <section className="rounded-md border border-line bg-panel p-5 shadow-soft">
      <h2 className="text-base font-semibold">{title}</h2>
      <div className="mt-5 space-y-4">
        {data.map((item) => (
          <div key={item.label} className="grid grid-cols-[minmax(90px,160px)_1fr_36px] items-center gap-3">
            <span className="truncate text-sm text-muted" title={item.label}>
              {item.label}
            </span>
            <div className="h-2.5 rounded-full bg-slate-200">
              <div
                className={`h-2.5 rounded-full ${toneClass[tone]}`}
                style={{ width: `${Math.max(8, (item.value / max) * 100)}%` }}
              />
            </div>
            <span className="text-right text-sm font-medium">{item.value}</span>
          </div>
        ))}
      </div>
    </section>
  );
}
