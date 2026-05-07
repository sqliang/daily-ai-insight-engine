import type { Metadata } from "next";
import Link from "next/link";
import { getSourceStatuses } from "@/lib/data/sources";
import { PageShell } from "@/components/layout/PageShell";
import { SourcesGrid } from "@/components/sources/SourcesGrid";

export const dynamic = "force-dynamic";

export const metadata: Metadata = {
  title: "Data Sources - Daily AI Insight Engine",
};

export default async function SourcesPage() {
  const sources = await getSourceStatuses();

  return (
    <PageShell>
      {/* Page header */}
      <header className="mb-8">
        <div className="flex items-center gap-2 mb-2">
          <Link
            href="/"
            className="text-[11px] font-medium uppercase tracking-wider text-muted/50 hover:text-accent transition-colors"
          >
            ← Dashboard
          </Link>
        </div>
        <h1 className="text-2xl font-bold text-foreground">Data Sources</h1>
        <p className="mt-1.5 text-sm text-muted">
          {sources.length} enabled sources from pipeline config &mdash; manifest
          data from the latest pipeline run.
        </p>
      </header>

      <SourcesGrid sources={sources} />
    </PageShell>
  );
}
