// ============================================================================
// DataUnavailable.tsx — 数据库暂时不可用的降级提示
//
// 当 Neon 流量配额耗尽或维护导致 DB 连接失败时，各页面在数据加载层
// catch 后渲染本组件（HTTP 200 + 友好提示），替代 500 或流式渲染中途
// 抛错造成的"200 空壳"（issue #152 运行时优雅降级）。
//
// 与"暂无数据"空状态语义不同：数据并未丢失，只是连接暂时中断。
// 文案必须明确表达"暂时不可用/会自动恢复"，避免用户误以为数据丢失。
//
// ISR 权衡说明：降级页面会被 ISR 缓存至多 1 小时（revalidate=3600），
// DB 恢复后最迟 1 小时自动回切真实内容 —— 这是可接受的权衡。
// ============================================================================

/**
 * 数据库暂时不可用的全页提示（由调用方包在 PageShell 内）。
 *
 * 使用场景：页面数据加载抛出连接类错误时渲染；正常返回 null/空数组
 * 不属于本组件的语义，仍走 notFound 404 或既有的"暂无数据"空状态。
 */
export function DataUnavailable() {
  return (
    <div className="flex flex-col items-center justify-center py-32 text-center">
      <svg
        width="48"
        height="48"
        viewBox="0 0 24 24"
        fill="none"
        stroke="var(--muted)"
        strokeWidth="1.2"
        strokeLinecap="round"
        strokeLinejoin="round"
        className="mb-5"
        aria-hidden="true"
      >
        {/* 数据库 + 断连符号 */}
        <ellipse cx="12" cy="5" rx="9" ry="3" />
        <path d="M3 5v14a9 3 0 0 0 9 3" />
        <path d="M21 5v5" />
        <path d="M3 12a9 3 0 0 0 9 3" />
        <line x1="16" y1="16" x2="22" y2="22" />
        <line x1="22" y1="16" x2="16" y2="22" />
      </svg>
      <h2 className="text-lg font-bold text-foreground">数据暂时不可用</h2>
      <p className="mt-2 max-w-md text-sm leading-relaxed text-muted">
        数据库连接暂时中断（流量额度或维护中），恢复后页面会在 1
        小时内自动更新，请稍后刷新。
      </p>
    </div>
  );
}
