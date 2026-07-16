import type { DailyReport, EvidenceSource, TopEvent } from "@/lib/agent/schema";
import { eventTypeLabels, severityLabels } from "@/lib/report/labels";

const dimensionLabels: Record<string, string> = {
  technology: "技术",
  application: "应用",
  policy: "政策",
  capital: "资本",
};

export function generateMarkdown(report: DailyReport): string {
  const lines: string[] = [];

  lines.push("---");
  lines.push(`title: "${report.reportTitle}"`);
  lines.push(`date: ${report.date}`);
  lines.push(`generated: ${report.generatedAt}`);
  lines.push("---");
  lines.push("");
  lines.push(`# ${report.reportTitle}`);
  lines.push("");

  // Executive Summary
  lines.push("## 执行摘要");
  lines.push("");
  lines.push(report.executiveSummary);
  lines.push("");

  // Data Overview
  lines.push("## 数据概览");
  lines.push("");
  lines.push("| 指标 | 数值 |");
  lines.push("|------|------|");
  lines.push(`| 样本总量 | ${report.dataSourceSummary.totalArticles} |`);
  lines.push(
    `| 信源数 | ${report.dataSourceSummary.sources.length} (${report.dataSourceSummary.sources.join(", ")}) |`,
  );
  lines.push(`| 语言覆盖 | ${report.dataSourceSummary.languages.join(", ")} |`);
  lines.push("");

  // Top Events
  lines.push("## 今日 Top 事件");
  lines.push("");
  report.topEvents.forEach((event: TopEvent, i) => {
    lines.push(`### #${i + 1} ${event.title}`);
    lines.push("");
    lines.push(`- **事件类型**: ${eventTypeLabels[event.eventType]}`);
    lines.push(`- **影响力评分**: ${event.impactScore}/10`);
    lines.push(`- **为什么重要**: ${event.whyItMatters}`);
    lines.push("");
    lines.push("**支撑证据**:");
    lines.push("");
    event.evidence.forEach((e) => {
      lines.push(`- ${e}`);
    });
    // 参考来源
    const srcList = event.evidenceSources;
    if (srcList && srcList.length > 0) {
      lines.push("");
      srcList.forEach((s: EvidenceSource, i: number) => {
        lines.push(`*${i + 1}.* [${s.sourceDir}](${s.url}) — ${s.title}`);
      });
    }
    lines.push("");
  });

  // Deep Dives
  lines.push("## 深度分析");
  lines.push("");
  report.deepDives.forEach((dive) => {
    lines.push(`### ${dive.title}`);
    lines.push("");
    lines.push(`**背景**: ${dive.background}`);
    lines.push("");
    lines.push(`**影响**: ${dive.impact}`);
    lines.push("");
    lines.push(`**后续关注**: ${dive.watchNext}`);
    lines.push("");
  });

  // Trend Insights
  lines.push("## 趋势判断");
  lines.push("");
  report.trendInsights.forEach((trend) => {
    const dimLabel = dimensionLabels[trend.dimension] ?? trend.dimension;
    lines.push(`### ${dimLabel}`);
    lines.push("");
    lines.push(`**判断**: ${trend.judgment}`);
    lines.push("");
    lines.push("**支撑信号**:");
    lines.push("");
    trend.supportingSignals.forEach((s) => {
      lines.push(`- ${s}`);
    });
    lines.push("");
  });

  // Risk Signals
  lines.push("## 风险提示");
  lines.push("");
  lines.push("| 严重程度 | 信号 | 判断依据 |");
  lines.push("|----------|------|----------|");
  report.riskSignals.forEach((s) => {
    lines.push(`| ${severityLabels[s.severity]} | ${s.signal} | ${s.rationale} |`);
  });
  lines.push("");

  // Opportunity Signals
  lines.push("## 机会提示");
  lines.push("");
  lines.push("| 重要程度 | 信号 | 判断依据 |");
  lines.push("|----------|------|----------|");
  report.opportunitySignals.forEach((s) => {
    lines.push(`| ${severityLabels[s.severity]} | ${s.signal} | ${s.rationale} |`);
  });
  lines.push("");

  // Data Source
  lines.push("## 信源说明");
  lines.push("");
  lines.push(report.dataSourceSummary.selectionRationale);
  lines.push("");

  return lines.join("\n");
}
