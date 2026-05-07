// ============================================================================
// ReportFooter.tsx — 报告页脚组件
//
// 职责：渲染日报底部的信源选择说明文字。
//
// 内容来源：
//   - selectionRationale 来自 dataSourceSummary，在 Reduce 阶段生成
//   - 说明当日选取信源的考量，如"聚焦 AI 行业媒体，兼顾政策信源"
//
// 设计决策：
//   - 独立组件，便于页脚样式/内容的单独维护
//   - 使用 border-t 与上方内容区视觉分隔
//   - 字号较小（text-sm），颜色为 muted，不抢夺主内容注意力
// ============================================================================

type ReportFooterProps = {
  selectionRationale: string;
};

export function ReportFooter({ selectionRationale }: ReportFooterProps) {
  return (
    <footer className="mt-8 border-t border-line pt-5 text-sm leading-7 text-muted">
      {selectionRationale}
    </footer>
  );
}
