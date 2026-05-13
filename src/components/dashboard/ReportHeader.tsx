import Link from "next/link";
import type { DailyReport } from "@/lib/agent/schema";

function formatGeneratedAt(iso: string): string {
  const d = new Date(iso);
  const pad = (n: number) => String(n).padStart(2, "0");
  return `${d.getUTCFullYear()}-${pad(d.getUTCMonth() + 1)}-${pad(d.getUTCDate())} ${pad(d.getUTCHours())}:${pad(d.getUTCMinutes())} UTC`;
}

type ReportHeaderProps = {
  report: Pick<DailyReport, "reportTitle" | "date" | "generatedAt" | "executiveSummary">;
};

export function ReportHeader({ report }: ReportHeaderProps) {
  return (
    <header className="relative overflow-hidden rounded-2xl bg-gradient-to-br from-foreground via-foreground to-accent-dark p-6 shadow-lg md:p-10">
      {/* Decorative geometric shapes */}
      <svg
        className="pointer-events-none absolute inset-0 h-full w-full"
        aria-hidden="true"
        viewBox="0 0 1200 400"
        preserveAspectRatio="none"
      >
        {/* Large blurred circle — top right */}
        <circle
          cx="1050"
          cy="60"
          r="180"
          fill="oklch(0.55 0.13 200 / 0.12)"
        />
        <circle
          cx="1080"
          cy="40"
          r="100"
          fill="oklch(0.55 0.13 200 / 0.10)"
        />
        {/* Medium circle — bottom left */}
        <circle
          cx="80"
          cy="340"
          r="140"
          fill="oklch(0.45 0.16 340 / 0.10)"
        />
        <circle
          cx="50"
          cy="360"
          r="80"
          fill="oklch(0.45 0.16 340 / 0.08)"
        />
        {/* Small dot grid — top left area */}
        {Array.from({ length: 6 }).flatMap((_, row) =>
          Array.from({ length: 6 }).map((_, col) => (
            <circle
              key={`${row}-${col}`}
              cx={40 + col * 24}
              cy={30 + row * 24}
              r="1.2"
              fill="oklch(1 0 0 / 0.18)"
            />
          )),
        )}
        {/* Accent line — bottom decorative */}
        <line
          x1="36"
          y1="370"
          x2="400"
          y2="370"
          stroke="oklch(0.55 0.13 200 / 0.25)"
          strokeWidth="0.5"
          strokeDasharray="4 6"
        />
      </svg>

      <div className="relative">
        {/* Brand label */}
        <div className="flex items-center gap-2.5">
          <span className="relative flex h-2.5 w-2.5">
            <span className="absolute inline-flex h-full w-full animate-ping rounded-full bg-accent opacity-60" />
            <span className="relative inline-flex h-2.5 w-2.5 rounded-full bg-accent" />
          </span>
          <p className="text-[11px] font-medium uppercase tracking-[0.25em] text-accent-light/90">
            Daily AI Insight Engine
          </p>
        </div>

        {/* Title */}
        <h1 className="mt-4 max-w-4xl bg-gradient-to-r from-white via-white to-accent-light bg-clip-text text-3xl font-bold leading-tight tracking-tight text-transparent md:text-4xl lg:text-5xl">
          {report.reportTitle}
        </h1>

        {/* Metadata row */}
        <div className="mt-5 flex flex-wrap items-center justify-between gap-3">
          <div className="flex flex-wrap items-center gap-3">
            <span className="inline-flex items-center gap-1.5 rounded-full border border-white/10 bg-white/5 px-3 py-1 text-xs font-medium text-white/70 backdrop-blur">
              <svg
                width="12"
                height="12"
                viewBox="0 0 16 16"
                fill="none"
                stroke="currentColor"
                strokeWidth="1.5"
                className="text-accent-light"
              >
                <rect x="2" y="3" width="12" height="11" rx="2" />
                <path d="M2 7h12M5 2v3m6-3v3" strokeLinecap="round" />
              </svg>
              {report.date}
            </span>
            <span className="inline-flex items-center gap-1.5 rounded-full border border-white/10 bg-white/5 px-3 py-1 text-xs font-medium text-white/50 backdrop-blur">
              <svg
                width="12"
                height="12"
                viewBox="0 0 16 16"
                fill="none"
                stroke="currentColor"
                strokeWidth="1.5"
              >
                <circle cx="8" cy="8" r="6.5" />
                <path d="M8 4.5V8l3 2" strokeLinecap="round" strokeLinejoin="round" />
              </svg>
              {formatGeneratedAt(report.generatedAt)}
            </span>
          </div>
          <Link
            href="/report"
            className="inline-flex items-center rounded-full bg-accent px-4 py-1.5 text-xs font-semibold text-white shadow-glow transition-all duration-200 hover:bg-accent-dark"
          >
            完整报告
          </Link>
        </div>

        {/* Executive summary — glass panel */}
        <div className="mt-6 rounded-xl border border-white/8 bg-white/[0.04] p-4 backdrop-blur md:p-5">
          <p className="text-sm leading-7 text-white/75 md:text-base md:leading-8">
            {report.executiveSummary}
          </p>
        </div>
      </div>
    </header>
  );
}
