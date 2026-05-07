export default function Loading() {
  return (
    <main className="mx-auto max-w-7xl px-4 py-6 sm:px-6 md:px-8 md:py-8">
      <div className="animate-pulse space-y-6">
        {/* Header skeleton */}
        <div className="rounded-xl border border-line bg-panel p-6 md:p-8">
          <div className="h-3 w-40 rounded bg-line" />
          <div className="mt-3 h-8 w-96 rounded bg-line" />
          <div className="mt-2 h-1 w-16 rounded bg-line" />
          <div className="mt-4 h-16 rounded bg-line" />
        </div>

        {/* KPI cards skeleton */}
        <div className="grid gap-4 md:grid-cols-3">
          {[1, 2, 3].map((i) => (
            <div key={i} className="rounded-xl border border-line bg-panel p-5">
              <div className="h-4 w-20 rounded bg-line" />
              <div className="mt-3 h-10 w-16 rounded bg-line" />
              <div className="mt-2 h-4 w-40 rounded bg-line" />
            </div>
          ))}
        </div>

        {/* Donut charts skeleton */}
        <div className="grid gap-5 lg:grid-cols-2">
          {[1, 2].map((i) => (
            <div key={i} className="rounded-xl border border-line bg-panel p-5">
              <div className="h-5 w-28 rounded bg-line" />
              <div className="mt-4 mx-auto h-64 w-64 rounded-full bg-line" />
            </div>
          ))}
        </div>

        {/* Top events skeleton */}
        <div className="rounded-xl border border-line bg-panel p-5">
          <div className="h-5 w-32 rounded bg-line" />
          {[1, 2, 3, 4, 5].map((i) => (
            <div key={i} className="mt-5 border-t border-line pt-5">
              <div className="h-5 w-80 rounded bg-line" />
              <div className="mt-2 h-4 w-full rounded bg-line" />
              <div className="mt-2 h-4 w-3/4 rounded bg-line" />
            </div>
          ))}
        </div>
      </div>
    </main>
  );
}
