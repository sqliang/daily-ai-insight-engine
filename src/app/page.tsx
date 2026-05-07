// ============================================================================
// page.tsx — 日报看板首页（服务端组件）
//
// 本文件是 Next.js App Router 的唯一页面路由（/）。
// 作为服务端组件，它在每次请求时（或构建时）从文件系统读取预生成的日报 JSON，
// 经 Zod 校验后直接渲染为 HTML。
//
// 架构决策：页面是纯展示层
//   - 不做任何数据聚合计算（visualizationData 已由流水线预计算）
//   - 不做 AI 调用（AI 抽取在 scripts/run-pipeline.ts 中离线完成）
//   - 页面本身无状态、无客户端交互，可被 CDN 缓存
//
// 数据流：data/reports/daily-report.json → Zod.parse → 组件 props → HTML
//
// 组件拆分说明：
//   - ReportHeader：页头区（标题 + 元信息 + 执行摘要）
//   - KPISection：KPI 指标卡片区（样本量、信源数、语言覆盖）
//   - TopEventsSection：Top 5 事件列表
//   - DistributionSection：事件类型分布 + 情感分布（双栏）
//   - RankingsSection：影响力排名 + 高频实体（双栏）
//   - DeepDivesSection：关键事件深度总结
//   - TrendInsightsSection：趋势判断（四维）
//   - SignalList：风险 & 机会信号区（已存在组件）
//   - ReportFooter：页脚信源说明
// ============================================================================

import { readFile } from "node:fs/promises";
import { join } from "node:path";

import { DeepDivesSection } from "@/components/dashboard/DeepDivesSection";
import { DistributionSection } from "@/components/dashboard/DistributionSection";
import { KPISection } from "@/components/dashboard/KPISection";
import { RankingsSection } from "@/components/dashboard/RankingsSection";
import { ReportFooter } from "@/components/dashboard/ReportFooter";
import { ReportHeader } from "@/components/dashboard/ReportHeader";
import { SignalList } from "@/components/dashboard/SignalList";
import { TopEventsSection } from "@/components/dashboard/TopEventsSection";
import { TrendInsightsSection } from "@/components/dashboard/TrendInsightsSection";
import { dailyReportSchema } from "@/lib/agent/schema";

// ============================================================================
// getReport — 数据获取函数
//
// 从文件系统读取预生成的日报 JSON 文件，经 Zod 校验后返回类型安全的 report 对象。
// 每次页面渲染时调用，确保展示数据与流水线产物一致。
// ============================================================================
async function getReport() {
  const filePath = join(process.cwd(), "data/reports/daily-report.json");
  const content = await readFile(filePath, "utf8");
  return dailyReportSchema.parse(JSON.parse(content));
}

// ============================================================================
// Home — 页面默认导出组件
//
// 职责：组装所有区块组件为完整页面。
// 处理可视化数据的 label 映射（英文枚举 → 中文标签），
// 将映射后的数据传递给对应的展示组件。
// ============================================================================
export default async function Home() {
  const report = await getReport();

  return (
    <main className="mx-auto max-w-7xl px-5 py-6 md:px-8 md:py-8">
      {/* ====== 页头区：标题 + 元信息 + 执行摘要 ====== */}
      <ReportHeader
        report={{
          reportTitle: report.reportTitle,
          date: report.date,
          generatedAt: report.generatedAt,
          executiveSummary: report.executiveSummary,
        }}
      />

      {/* ====== KPI 指标卡片区：样本量、信源数、语言覆盖 ====== */}
      <KPISection dataSourceSummary={report.dataSourceSummary} />

      {/* ====== 主内容区：Top 事件 + 分布图（双栏布局） ====== */}
      <section className="mt-6 grid gap-5 lg:grid-cols-[1.2fr_0.8fr]">
        <TopEventsSection topEvents={report.topEvents} />
        <DistributionSection visualizationData={report.visualizationData} />
      </section>

      {/* ====== 影响力排名 + 高频实体（双栏布局） ====== */}
      <RankingsSection visualizationData={report.visualizationData} />

      {/* ====== 深度分析区：关键事件的背景、影响、后续关注 ====== */}
      <DeepDivesSection deepDives={report.deepDives} />

      {/* ====== 趋势判断区：技术/应用/政策/资本四维判断 ====== */}
      <TrendInsightsSection trendInsights={report.trendInsights} />

      {/* ====== 风险 & 机会信号区 ====== */}
      <section className="mt-6 grid gap-5 lg:grid-cols-2">
        <SignalList title="风险提示" items={report.riskSignals} />
        <SignalList title="机会提示" items={report.opportunitySignals} />
      </section>

      {/* ====== 页脚：信源选择说明 ====== */}
      <ReportFooter selectionRationale={report.dataSourceSummary.selectionRationale} />
    </main>
  );
}
