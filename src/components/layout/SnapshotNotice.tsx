// ============================================================================
// SnapshotNotice.tsx — 离线快照数据提示角标
//
// 仅在当前请求确实通过 withDbFallback 使用快照时显示；DB 正常读取、
// 或 DB 与快照均不可用而渲染 DataUnavailable 时均不显示。
// 集中接入 PageShell，首页、日报、信源与专题页无需各自重复实现。
// ============================================================================

import { getSnapshotStatus } from "@/lib/data/snapshot/status";

/**
 * 显示轻量离线数据提示。generated_at 直接来自快照 index.json；
 * 极端情况下索引不可读则显示"未知时间"，不影响正文渲染。
 */
export async function SnapshotNotice() {
  const { used, generatedAt } = await getSnapshotStatus();
  if (!used) return null;

  return (
    <div
      role="status"
      className="mb-5 flex items-start gap-2.5 rounded-xl border border-cool/25 bg-cool/8 px-4 py-3 text-[13px] leading-6 text-foreground/72"
    >
      <span className="mt-2 h-2 w-2 shrink-0 rounded-full bg-cool" aria-hidden="true" />
      <p>
        正在展示离线快照数据（更新于 {generatedAt ?? "未知时间"}），数据库恢复后自动回到实时数据
      </p>
    </div>
  );
}
