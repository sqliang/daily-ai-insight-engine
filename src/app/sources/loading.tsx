import { PageShell } from "@/components/layout/PageShell";
import { SourceCardSkeleton } from "@/components/sources/SourceCardSkeleton";

export default function Loading() {
  return (
    <PageShell>
      <div className="animate-pulse space-y-10">
        {/* Hero skeleton — matches SourcesHero structure */}
        <div className="rounded-2xl bg-foreground/5 p-6 md:p-10">
          <div className="h-3 w-32 rounded bg-line" />
          <div className="mt-4 h-8 w-72 rounded bg-line" />
          <div className="mt-2 h-5 w-[520px] rounded bg-line" />
          <div className="mt-5 flex flex-wrap gap-2">
            <div className="h-7 w-24 rounded-full bg-line" />
            <div className="h-7 w-24 rounded-full bg-line" />
            <div className="h-7 w-32 rounded-full bg-line" />
          </div>
          {/* Vertex cards skeleton */}
          <div className="mt-6 grid gap-4 sm:grid-cols-3">
            {[1, 2, 3].map((i) => (
              <div key={i} className="rounded-xl border border-line/20 bg-white/[0.02] p-4 md:p-5">
                <div className="flex items-center gap-3">
                  <div className="h-9 w-9 rounded-full bg-line" />
                  <div>
                    <div className="h-5 w-24 rounded bg-line" />
                    <div className="mt-1 h-3 w-16 rounded bg-line" />
                  </div>
                </div>
                <div className="mt-3 h-4 w-full rounded bg-line" />
              </div>
            ))}
          </div>
          {/* Filter strategy skeleton */}
          <div className="mt-5 rounded-xl border border-line/20 bg-white/[0.02] p-4 md:p-5">
            <div className="h-3 w-28 rounded bg-line" />
            <div className="mt-3 grid gap-3 sm:grid-cols-3">
              <div className="h-4 w-full rounded bg-line" />
              <div className="h-4 w-full rounded bg-line" />
              <div className="h-4 w-full rounded bg-line" />
            </div>
          </div>
        </div>

        {/* Tier section skeletons — match TierSection + SourceCard structure */}
        {["A", "B", "C"].map((tier) => (
          <div key={tier}>
            {/* Tier header skeleton */}
            <div className="flex items-center gap-4 mb-6">
              <div className="h-8 w-1 rounded-full bg-line" />
              <div className="flex-1 min-w-0">
                <div className="h-7 w-36 rounded bg-line" />
                <div className="mt-1 h-4 w-80 rounded bg-line" />
              </div>
              <div className="h-6 w-28 rounded-full bg-line shrink-0" />
            </div>
            {/* Card grid */}
            <div className="grid gap-5 md:grid-cols-2 lg:grid-cols-3">
              {[1, 2, 3].map((i) => (
                <SourceCardSkeleton key={i} />
              ))}
            </div>
          </div>
        ))}
      </div>
    </PageShell>
  );
}
