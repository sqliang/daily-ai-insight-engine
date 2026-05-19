export default function Loading() {
  return (
    <main className="mx-auto max-w-7xl px-4 py-6 sm:px-6 md:px-8 md:py-8">
      <div className="animate-pulse">
        {/* ===== ReportHeader skeleton ===== */}
        <div className="rounded-2xl bg-foreground/5 p-6 md:p-10">
          {/* Brand label */}
          <div className="flex items-center gap-2.5">
            <div className="h-2.5 w-2.5 rounded-full bg-line" />
            <div className="h-3 w-40 rounded bg-line" />
          </div>
          {/* Title — max-w-4xl match */}
          <div className="mt-4 h-8 w-full max-w-3xl rounded bg-line md:h-10" />
          <div className="mt-3 h-8 w-3/4 rounded bg-line md:hidden" />
          {/* Metadata row */}
          <div className="mt-5 flex flex-wrap items-center gap-3">
            <div className="h-6 w-28 rounded-full bg-line" />
            <div className="h-6 w-44 rounded-full bg-line" />
            <div className="h-6 w-20 rounded-full bg-line" />
          </div>
          {/* Executive summary */}
          <div className="mt-6 rounded-xl border border-line/20 bg-white/[0.04] p-4 md:p-5">
            <div className="h-4 w-full rounded bg-line" />
            <div className="mt-2 h-4 w-full rounded bg-line" />
            <div className="mt-2 h-4 w-3/5 rounded bg-line" />
            <div className="mt-2 hidden h-4 w-2/3 rounded bg-line md:block" />
          </div>
        </div>

        {/* ===== KPISection skeleton ===== */}
        <div className="mt-6 grid gap-4 md:grid-cols-3">
          {[1, 2, 3].map((i) => (
            <div key={i} className="rounded-xl border border-line bg-panel p-5">
              <div className="flex items-center gap-2">
                <div className="h-8 w-8 rounded-lg bg-line" />
                <div className="h-4 w-16 rounded bg-line" />
              </div>
              <div className="mt-3 h-10 w-24 rounded bg-line" />
              <div className="mt-2 h-4 w-48 rounded bg-line" />
            </div>
          ))}
        </div>

        {/* ===== DistributionSection skeleton ===== */}
        <div className="mt-6 grid gap-5 lg:grid-cols-2">
          {[1, 2].map((i) => (
            <div key={i} className="rounded-xl border border-line bg-panel p-5">
              <div className="h-5 w-28 rounded bg-line" />
              <div className="mt-4 mx-auto h-64 w-64 rounded-full bg-line" />
              <div className="mt-4 space-y-1.5 border-t border-line pt-4">
                <div className="h-4 w-full rounded bg-line" />
                <div className="h-4 w-5/6 rounded bg-line" />
              </div>
            </div>
          ))}
        </div>

        {/* ===== TopEventsSection skeleton ===== */}
        <div className="mt-6 rounded-xl border border-line bg-panel p-5">
          <div className="h-6 w-32 rounded bg-line" />
          <div className="mt-5 divide-y divide-line">
            {[1, 2, 3, 4, 5].map((i) => (
              <div key={i} className="py-5 first:pt-0 last:pb-0">
                <div className="flex items-start gap-3">
                  <div className="h-7 w-7 shrink-0 rounded-full bg-line" />
                  <div className="flex-1 min-w-0">
                    <div className="h-5 w-16 rounded-full bg-line" />
                    <div className="mt-1.5 h-6 w-full rounded bg-line" />
                  </div>
                  <div className="h-6 w-24 shrink-0 rounded-lg bg-line" />
                </div>
                <div className="mt-3 h-1 w-full rounded-full bg-line" />
                <div className="mt-3 h-4 w-full rounded bg-line" />
                <div className="mt-2 h-4 w-2/3 rounded bg-line" />
                <div className="mt-3 space-y-1.5">
                  <div className="flex items-start gap-2">
                    <div className="mt-2 h-1 w-1 shrink-0 rounded-full bg-line" />
                    <div className="h-4 w-3/4 rounded bg-line" />
                  </div>
                  <div className="flex items-start gap-2">
                    <div className="mt-2 h-1 w-1 shrink-0 rounded-full bg-line" />
                    <div className="h-4 w-1/2 rounded bg-line" />
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* ===== RankingsSection skeleton ===== */}
        <div className="mt-6 grid gap-5 lg:grid-cols-2">
          {[1, 2].map((i) => (
            <div key={i} className="rounded-xl border border-line bg-panel p-5">
              <div className="h-5 w-28 rounded bg-line" />
              <div className="mt-5 space-y-4">
                {[1, 2, 3, 4, 5].map((j) => (
                  <div key={j} className="flex items-center gap-3">
                    <div className="h-4 flex-1 rounded bg-line" />
                    <div
                      className="h-3 rounded-full bg-line"
                      style={{ width: `${100 - j * 12}%`, maxWidth: "12rem" }}
                    />
                  </div>
                ))}
              </div>
            </div>
          ))}
        </div>

        {/* ===== TrendInsightsSection skeleton ===== */}
        <div className="mt-6 rounded-xl border border-line bg-panel p-5">
          <div className="h-6 w-28 rounded bg-line" />
          <div className="mt-4 mb-2 flex justify-center">
            <div className="h-[280px] w-[280px] rounded-full bg-line" />
          </div>
          <div className="mt-2 grid gap-4 md:grid-cols-2">
            {[1, 2, 3, 4].map((i) => (
              <div key={i} className="rounded-lg border border-l-2 border-l-line bg-surface p-4">
                <div className="flex items-center gap-2">
                  <div className="h-5 w-5 rounded-full bg-line" />
                  <div className="h-3 w-12 rounded bg-line" />
                </div>
                <div className="mt-2 h-5 w-3/4 rounded bg-line" />
                <div className="mt-3 space-y-1.5">
                  <div className="flex items-start gap-2">
                    <div className="mt-2 h-1 w-1 shrink-0 rounded-full bg-line" />
                    <div className="h-4 w-full rounded bg-line" />
                  </div>
                  <div className="flex items-start gap-2">
                    <div className="mt-2 h-1 w-1 shrink-0 rounded-full bg-line" />
                    <div className="h-4 w-5/6 rounded bg-line" />
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* ===== DeepDivesSection skeleton ===== */}
        <div className="mt-6 rounded-xl border border-line bg-panel p-5">
          <div className="h-6 w-40 rounded bg-line" />
          <div className="mt-5 grid gap-5 lg:grid-cols-3">
            {[1, 2, 3].map((i) => (
              <div key={i} className="rounded-lg border border-l-2 border-l-line bg-surface p-4">
                <div className="h-5 w-3/4 rounded bg-line" />
                <div className="mt-4">
                  <div className="h-3 w-8 rounded bg-line" />
                  <div className="mt-1 h-4 w-full rounded bg-line" />
                  <div className="mt-1 h-4 w-2/3 rounded bg-line" />
                </div>
                <div className="mt-4">
                  <div className="h-3 w-8 rounded bg-line" />
                  <div className="mt-1 h-4 w-full rounded bg-line" />
                  <div className="mt-1 h-4 w-3/4 rounded bg-line" />
                </div>
                <div className="mt-4">
                  <div className="h-3 w-12 rounded bg-line" />
                  <div className="mt-1 h-4 w-full rounded bg-line" />
                  <div className="mt-1 h-4 w-1/2 rounded bg-line" />
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* ===== SignalLists skeleton ===== */}
        <div className="mt-6 grid gap-5 lg:grid-cols-2">
          {[1, 2].map((i) => (
            <div key={i} className="rounded-xl border border-line bg-panel p-5">
              <div className="flex items-center gap-2">
                <div className="h-7 w-7 rounded-lg bg-line" />
                <div className="h-5 w-20 rounded bg-line" />
              </div>
              <div className="mt-4 space-y-3">
                {[1, 2, 3].map((j) => (
                  <div key={j} className="rounded-lg border border-line p-4">
                    <div className="flex items-start justify-between gap-3">
                      <div className="h-5 w-3/4 rounded bg-line" />
                      <div className="h-5 w-12 shrink-0 rounded-full bg-line" />
                    </div>
                    <div className="mt-2 h-1 w-full rounded-full bg-line" />
                    <div className="mt-2 h-4 w-full rounded bg-line" />
                    <div className="mt-1 h-4 w-2/3 rounded bg-line" />
                  </div>
                ))}
              </div>
            </div>
          ))}
        </div>

        {/* ===== ReportFooter skeleton ===== */}
        <div className="mt-8 border-t-2 border-line pt-5">
          <div className="h-3 w-16 rounded bg-line" />
          <div className="mt-1 h-4 w-full rounded bg-line" />
          <div className="mt-2 h-4 w-4/5 rounded bg-line" />
        </div>
      </div>
    </main>
  );
}
