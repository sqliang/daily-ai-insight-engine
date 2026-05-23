// ============================================================================
// StatusBadge.tsx — 处理状态徽章
//
// 以彩色圆点 + 中英双语标签展示管道处理进度，颜色由 STATUS_CONFIG 根据状态动态派生。
// 被 ArticleCard 消费，用于展示每个数据源的处理状态。
// ============================================================================

import { type ProcessingStatus, STATUS_CONFIG } from "@/lib/data/status";

type StatusBadgeProps = {
  status: ProcessingStatus;
};

/**
 * 处理状态徽章，以彩色圆点 + 中英双语展示管道处理进度。
 *
 * 颜色由 STATUS_CONFIG 根据状态动态派生（ready → blue, processing → amber 等）。
 * 用于 SourceCard 和其他需要展示处理状态的场景。
 */
export function StatusBadge({ status }: StatusBadgeProps) {
  const cfg = STATUS_CONFIG[status];
  return (
    <span
      className="inline-flex items-center gap-1.5 rounded-full border px-3.5 py-1.5 text-[12px] font-semibold backdrop-blur"
      style={{
        borderColor: `${cfg.color} / 0.2`,
        backgroundColor: `${cfg.color} / 0.06`,
        color: cfg.color,
      }}
      title={cfg.description}
    >
      {cfg.english}
      <span className="font-normal opacity-50">·</span>
      <span className="font-medium">{cfg.label}</span>
    </span>
  );
}
