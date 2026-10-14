// ============================================================================
// dashboard/loading.tsx — 卡片列表页骨架屏
//
// 匹配横向全宽卡片 + Hero Banner 的布局节奏。
// ============================================================================

export default function Loading() {
  return (
    <main className="mx-auto max-w-7xl px-5 py-8 md:px-8">
      <div className="animate-pulse">
        {/* Hero Banner 骨架 */}
        <div className="rounded-2xl bg-foreground/5 p-6 md:p-10">
          <div className="flex items-center gap-2.5">
            <div className="h-2.5 w-2.5 rounded-full bg-line" />
            <div className="h-3 w-40 rounded bg-line" />
          </div>
          <div className="mt-4 h-8 w-72 rounded bg-line md:h-9" />
          <div className="mt-2.5 space-y-2">
            <div className="h-5 w-full max-w-xl rounded bg-line" />
            <div className="h-5 w-full max-w-lg rounded bg-line" />
            <div className="h-5 w-full max-w-md rounded bg-line" />
          </div>
          <div className="mt-5 h-3 w-80 rounded bg-line md:mt-6" />
          <div className="mt-4 rounded-xl border border-line/20 bg-white/[0.02] p-4 md:p-5">
            <div className="h-3 w-24 rounded bg-line" />
            <div className="mt-3 grid gap-3 sm:grid-cols-3">
              <div className="h-10 w-full rounded bg-line" />
              <div className="h-10 w-full rounded bg-line" />
              <div className="h-10 w-full rounded bg-line" />
            </div>
          </div>
        </div>

        {/* 横向卡片骨架 */}
        <div className="mt-8 flex flex-col gap-4">
          {[1, 2].map((i) => (
            <div
              key={i}
              className="flex flex-col gap-4 rounded-xl border border-accent/12 bg-panel/80 p-6 sm:flex-row sm:gap-6"
            >
              {/* 左侧日期区块 */}
              <div className="flex shrink-0 flex-row items-center gap-3 sm:w-28 sm:flex-col sm:items-center sm:justify-center sm:border-r sm:border-line/30 sm:pr-4">
                <div className="h-8 w-16 rounded bg-line sm:h-9 sm:w-20" />
                <div className="flex flex-col items-start gap-1 sm:items-center">
                  <div className="h-3 w-8 rounded bg-line" />
                  <div className="h-3 w-10 rounded bg-line" />
                </div>
              </div>
              {/* 中间内容 */}
              <div className="flex min-w-0 flex-1 flex-col justify-center">
                <div className="h-5 w-3/4 rounded bg-line" />
                <div className="mt-2 h-4 w-full rounded bg-line" />
                <div className="mt-2 h-4 w-5/6 rounded bg-line" />
                <div className="mt-2 h-4 w-2/3 rounded bg-line" />
                <div className="mt-3 flex items-center gap-2">
                  <div className="h-5 w-20 rounded-full bg-line" />
                  <div className="h-4 w-24 rounded bg-line" />
                  <div className="h-4 w-16 rounded bg-line" />
                </div>
              </div>
              {/* 右侧箭头 */}
              <div className="flex shrink-0 items-center self-end sm:self-center">
                <div className="h-4 w-4 rounded bg-line" />
              </div>
            </div>
          ))}
        </div>
      </div>
    </main>
  );
}
