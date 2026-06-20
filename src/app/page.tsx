import type { Metadata } from "next";
import { PageShell } from "@/components/layout/PageShell";
import { SourcesGrid } from "@/components/sources/SourcesGrid";
import { SourcesHero } from "@/components/sources/SourcesHero";
import { getSourcesViewData } from "@/lib/data/sources";

// Next.js App Router 的一个**路由段配置（Route Segment Config）**声明，
// 作用是告诉 Next.js： 这个页面始终以动态模式渲染，不要进行静态生成（SSG） 
// 确保每次用户访问都能拿到最新的数据,每次请求都重新渲染
export const dynamic = "force-dynamic";

// 页面元数据
export const metadata: Metadata = {
  title: "数据源 - Daily AI Insight Engine",
};

export default async function HomePage() {
  
  // 调用 getSourcesViewData() 来获取数据源信息。
  // 这些数据可能随时变化（比如数据库中新增了 source），所以需要 每次请求都从数据源拉取最新数据 ，而不是在构建时生成一份静态页面。
  const { tiersMeta, sources, totalSources } = await getSourcesViewData();

  const tierSourceCounts: Record<string, number> = {};
  for (const s of sources) {
    tierSourceCounts[s.tier] = (tierSourceCounts[s.tier] ?? 0) + 1;
  }

  return (
    <PageShell>
      <SourcesHero
        tiersMeta={tiersMeta}
        totalSources={totalSources}
        tierSourceCounts={tierSourceCounts}
      />
      <SourcesGrid sources={sources} tiersMeta={tiersMeta} />
    </PageShell>
  );
}
