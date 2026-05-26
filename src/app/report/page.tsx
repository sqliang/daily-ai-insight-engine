// ============================================================================
// report/page.tsx — 重定向到日报卡片列表
//
// /report 原为最新日报 Markdown 全文页，重构后改为重定向到 /dashboard。
// 指定日期的 Markdown 全文请访问 /report/[date]。
// ============================================================================

import { redirect } from "next/navigation";

export default function ReportPage() {
  redirect("/dashboard");
}
