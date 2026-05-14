import type { Metadata } from "next";
import { PageShell } from "@/components/layout/PageShell";
import { SourcesGrid } from "@/components/sources/SourcesGrid";
import { SourcesHero } from "@/components/sources/SourcesHero";
import { getSourcesViewData } from "@/lib/data/sources";

export const dynamic = "force-dynamic";

export const metadata: Metadata = {
  title: "数据源 - Daily AI Insight Engine",
};

export default async function HomePage() {
  const { tiersMeta, sources, totalSources, totalArticles, latestDate } =
    await getSourcesViewData();

  const tierSourceCounts: Record<string, number> = {};
  const tierArticleCounts: Record<string, number> = {};
  for (const s of sources) {
    tierSourceCounts[s.tier] = (tierSourceCounts[s.tier] ?? 0) + 1;
    tierArticleCounts[s.tier] =
      (tierArticleCounts[s.tier] ?? 0) + s.articleCount;
  }

  return (
    <PageShell>
      <SourcesHero
        tiersMeta={tiersMeta}
        totalSources={totalSources}
        totalArticles={totalArticles}
        latestDate={latestDate}
        tierSourceCounts={tierSourceCounts}
        tierArticleCounts={tierArticleCounts}
      />
      <SourcesGrid sources={sources} tiersMeta={tiersMeta} />
    </PageShell>
  );
}
