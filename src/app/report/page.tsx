import { readFile } from "node:fs/promises";
import { join } from "node:path";
import type { Metadata } from "next";

import { PageShell } from "@/components/layout/PageShell";
import { MarkdownRenderer } from "@/components/report/MarkdownRenderer";
import { generateMarkdown } from "@/lib/report/generate-markdown";
import { dailyReportSchema } from "@/lib/agent/schema";

export const dynamic = "force-dynamic";

export const metadata: Metadata = {
  title: "Full Report - Daily AI Insight Engine",
  description: "AI 舆情分析日报完整报告",
};

async function getReportMarkdown(): Promise<string> {
  try {
    const mdPath = join(process.cwd(), "data/05_reports/daily-report.md");
    const raw = await readFile(mdPath, "utf8");
    // Strip YAML frontmatter (--- ... ---)
    return raw.replace(/^---[\s\S]*?---\n*/, "").trimStart();
  } catch {
    const jsonPath = join(process.cwd(), "data/05_reports/daily-report.json");
    const content = await readFile(jsonPath, "utf8");
    const report = dailyReportSchema.parse(JSON.parse(content));
    return generateMarkdown(report).replace(/^---[\s\S]*?---\n*/, "").trimStart();
  }
}

export default async function ReportPage() {
  const markdown = await getReportMarkdown();

  return (
    <PageShell>
      <MarkdownRenderer content={markdown} />
    </PageShell>
  );
}
