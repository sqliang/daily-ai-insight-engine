import type { Metadata } from "next";
import { PageShell } from "@/components/layout/PageShell";
import { SourcesGrid } from "@/components/sources/SourcesGrid";
import { SourcesHero } from "@/components/sources/SourcesHero";
import {
  getSourcesViewData,
  getTiersMeta,
  type SourceStatus,
} from "@/lib/data/sources";
import type { TierMeta } from "@/lib/data/tiers";

// Next.js App Router 路由段配置：1 小时 ISR。
// 数据（manifest / 日报）一天只由 pipeline 发布一两次，无需逐请求渲染；
// 原 force-dynamic 零缓存是 Neon 出站流量耗尽的根因之一（issue #152）
export const revalidate = 3600;

// 页面元数据
export const metadata: Metadata = {
  title: "数据源 - Daily AI Insight Engine",
};

export default async function HomePage() {
  // 数据获取 fail-soft：CI 无 DATABASE_URL、或 Neon 挂起导致 DB 不可达时，
  // 用空数据兜底渲染，保证构建顺利完成（issue #152 后续修复）。
  // 页面为 1h ISR，DB 恢复后下一次再验证即重新生成真实数据。
  let tiersMeta: Record<string, TierMeta>;
  let sources: SourceStatus[] = [];
  let totalSources = 0;
  try {
    const data = await getSourcesViewData();
    tiersMeta = data.tiersMeta;
    sources = data.sources;
    totalSources = data.totalSources;
  } catch {
    // tiersMeta 来自 config.yaml 文件读取（不依赖 DB），DB 故障时仍可正常展示
    tiersMeta = await getTiersMeta();
  }

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
