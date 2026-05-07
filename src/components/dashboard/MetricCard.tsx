// ============================================================================
// MetricCard.tsx — KPI 指标卡片组件
//
// 日报首屏顶部的三个指标卡片：样本量、信源数、语言覆盖。
// 每个卡片展示核心数值 + 辅助说明文字，让审阅者无需滚动即可
// 了解当日语料规模、信源覆盖面和报告时效性。
// ============================================================================

type MetricCardProps = {
  label: string;
  value: string | number;
  helper: string;
};

export function MetricCard({ label, value, helper }: MetricCardProps) {
  return (
    <section className="rounded-md border border-line bg-panel p-4 shadow-soft">
      <p className="text-sm text-muted">{label}</p>
      <p className="mt-2 text-3xl font-semibold tracking-normal">{value}</p>
      <p className="mt-2 text-sm leading-6 text-muted">{helper}</p>
    </section>
  );
}
