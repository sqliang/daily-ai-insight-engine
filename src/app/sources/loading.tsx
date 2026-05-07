export default function Loading() {
  return (
    <main className="mx-auto max-w-7xl px-4 py-6 sm:px-6 md:px-8 md:py-8">
      <div className="animate-pulse space-y-8">
        {/* Header skeleton */}
        <div>
          <div className="h-3 w-20 rounded bg-line" />
          <div className="mt-3 h-8 w-48 rounded bg-line" />
          <div className="mt-2 h-4 w-96 rounded bg-line" />
        </div>

        {/* Tier sections */}
        {["A", "B", "C"].map((tier) => (
          <div key={tier}>
            <div className="flex items-center gap-3 mb-4">
              <div className="h-2 w-2 rounded-full bg-line" />
              <div className="h-4 w-40 rounded bg-line" />
            </div>
            <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
              {[1, 2, 3].map((i) => (
                <div
                  key={i}
                  className="rounded-xl border border-line bg-panel p-5"
                >
                  <div className="h-5 w-32 rounded bg-line" />
                  <div className="mt-2 h-4 w-20 rounded bg-line" />
                  <div className="mt-3 h-4 w-full rounded bg-line" />
                  <div className="mt-2 h-4 w-3/4 rounded bg-line" />
                  <div className="mt-5 border-t border-line pt-4 space-y-2">
                    <div className="h-4 w-full rounded bg-line" />
                    <div className="h-4 w-5/6 rounded bg-line" />
                    <div className="h-4 w-2/3 rounded bg-line" />
                  </div>
                </div>
              ))}
            </div>
          </div>
        ))}
      </div>
    </main>
  );
}
