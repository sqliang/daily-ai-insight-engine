export function SourceCardSkeleton() {
  return (
    <div
      className="rounded-xl border border-line bg-panel p-5"
      style={{ borderTopColor: "var(--line)", borderTopWidth: 3 }}
    >
      {/* Title */}
      <div className="h-6 w-3/4 rounded bg-line" />
      {/* Tag row */}
      <div className="mt-3 flex flex-wrap items-center gap-2">
        <div className="h-5 w-16 rounded-full bg-line" />
        <div className="h-5 w-14 rounded-full bg-line" />
        <div className="h-5 w-10 rounded-full bg-line" />
        <div className="ml-auto h-5 w-14 rounded-full bg-line" />
      </div>
      {/* Description lines */}
      <div className="mt-3 space-y-2">
        <div className="h-4 w-full rounded bg-line" />
        <div className="h-4 w-5/6 rounded bg-line" />
        <div className="h-4 w-2/3 rounded bg-line" />
      </div>
      {/* Keyword chips */}
      <div className="mt-2.5 flex flex-wrap gap-1">
        <div className="h-4 w-14 rounded bg-line" />
        <div className="h-4 w-12 rounded bg-line" />
        <div className="h-4 w-16 rounded bg-line" />
        <div className="h-4 w-10 rounded bg-line" />
      </div>
      {/* Footer */}
      <div className="mt-4 flex items-center justify-between border-t border-line/40 pt-3">
        <div className="h-4 w-20 rounded bg-line" />
        <div className="h-4 w-16 rounded bg-line" />
      </div>
    </div>
  );
}
