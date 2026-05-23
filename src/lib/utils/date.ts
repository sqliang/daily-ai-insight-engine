// ============================================================================
// date.ts — 共享日期格式化工具
//
// 统一 formatGeneratedAt 函数，全局使用 UTC 时区，避免 SSR 下本地时区漂移。
// ============================================================================

/**
 * 将 ISO 日期字符串格式化为 `YYYY-MM-DD HH:MM UTC`。
 *
 * 使用 UTC 时间确保服务器端渲染与客户端渲染输出一致。
 */
export function formatGeneratedAt(iso: string): string {
  const d = new Date(iso);
  const pad = (n: number) => String(n).padStart(2, "0");
  return `${d.getUTCFullYear()}-${pad(d.getUTCMonth() + 1)}-${pad(d.getUTCDate())} ${pad(d.getUTCHours())}:${pad(d.getUTCMinutes())} UTC`;
}
