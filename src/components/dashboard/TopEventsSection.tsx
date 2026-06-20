"use client";

import { eventTypeLabels } from "@/lib/report/labels";
import type { DailyReport } from "@/lib/agent/schema";
import { SourceCitations } from "@/components/reports/SourceCitations";

type TopEventsSectionProps = {
  topEvents: DailyReport["topEvents"];
};

// ---------------------------------------------------------------------------
// EvidenceText — 每行 evidence 末尾的引用标记渲染
// 精准模式："...text [1][3]"  → [1] [3] 可点击编号，各跳转到参考列表对应行
// 降级模式："...text [7来源]" → [7来源] 可点击徽章，跳转到参考列表容器
// ---------------------------------------------------------------------------

function EvidenceText({
  text,
  eventIndex,
}: {
  text: string;
  eventIndex: number;
}) {
  // 先试精准编号 [1][3]...
  const numRegex = /\[(\d+)\]/g;
  const numMatches: Array<{ index: number; num: string; len: number }> = [];
  let m: RegExpExecArray | null;
  while ((m = numRegex.exec(text)) !== null) {
    numMatches.push({ index: m.index, num: m[1], len: m[0].length });
  }

  // 再试降级计数 [N来源]
  const countMatch = /\[(\d+)来源\]/.exec(text);

  if (numMatches.length > 0) {
    // 精准模式：每个 [n] 渲染为可点击 pill
    const parts: React.ReactNode[] = [];
    let last = 0;
    for (const nm of numMatches) {
      if (nm.index > last) {
        parts.push(<span key={`t-${last}`}>{text.slice(last, nm.index)}</span>);
      }
      parts.push(
        <CitationPill
          key={`c-${nm.index}`}
          label={nm.num}
          targetId={`src-${eventIndex}-${nm.num}`}
        />,
      );
      last = nm.index + nm.len;
    }
    if (last < text.length) {
      parts.push(<span key={`t-${last}`}>{text.slice(last)}</span>);
    }
    return <>{parts}</>;
  }

  if (countMatch) {
    // 降级模式：[N来源] 渲染为可点击徽章
    const before = text.slice(0, countMatch.index);
    const after = text.slice(countMatch.index + countMatch[0].length);
    return (
      <>
        {before}
        <CitationPill
          label={`${countMatch[1]} 来源`}
          targetId={`src-${eventIndex}-list`}
        />
        {after}
      </>
    );
  }

  return <>{text}</>;
}

/** 单个可点击引用 pill — 点击滚动到参考列表 */
function CitationPill({ label, targetId }: { label: string; targetId: string }) {
  const handleClick = (e: React.MouseEvent) => {
    e.preventDefault();
    document.getElementById(targetId)?.scrollIntoView({ behavior: "smooth", block: "nearest" });
  };

  return (
    <a
      onClick={handleClick}
      href={`#${targetId}`}
      className="inline-flex cursor-pointer items-center rounded bg-accent/10 px-1 text-[11px] font-semibold tabular-nums text-accent no-underline transition-colors hover:bg-accent/20"
    >
      {label}
    </a>
  );
}

const rankCircleBg = [
  "bg-accent",
  "bg-warm",
  "bg-cool",
  "bg-positive",
  "bg-accent-dark",
];

export function TopEventsSection({ topEvents }: TopEventsSectionProps) {
  return (
    <section className="rounded-xl border border-line bg-panel p-5 shadow-sm">
      <h2 className="text-lg font-semibold">今日 Top 事件</h2>
      <div className="mt-5 divide-y divide-line">
        {topEvents.map((event, index) => (
          <article
            key={event.title}
            className="py-5 first:pt-0 last:pb-0 transition-shadow hover:shadow-sm hover:bg-surface/50 rounded-lg px-1 -mx-1"
          >
            <div className="flex flex-col gap-3 md:flex-row md:items-start md:justify-between">
              <div className="flex items-start gap-3">
                <span
                  className={`flex h-7 w-7 shrink-0 items-center justify-center rounded-full ${rankCircleBg[index] ?? "bg-accent"} text-xs font-bold text-white`}
                >
                  {index + 1}
                </span>
                <div>
                  <span className="rounded-full bg-accent-light px-2 py-0.5 text-[11px] font-medium text-accent">
                    {eventTypeLabels[event.eventType]}
                  </span>
                  <h3 className="mt-1.5 text-lg font-semibold leading-7">{event.title}</h3>
                </div>
              </div>
              <span className="shrink-0 rounded-lg border border-accent/20 bg-accent-light/40 px-2.5 py-1 text-xs font-semibold text-accent">
                Impact {event.impactScore}/10
              </span>
            </div>

            <div className="mt-1 flex items-center gap-2">
              <div className="h-1 flex-1 rounded-full bg-line">
                <div
                  className="h-1 rounded-full bg-gradient-to-r from-cool to-accent"
                  style={{ width: `${(event.impactScore / 10) * 100}%` }}
                />
              </div>
            </div>

            <p className="mt-3 text-sm leading-7 text-muted">{event.whyItMatters}</p>
            <ul className="mt-3 space-y-1.5 text-sm leading-6 text-muted">
              {event.evidence.map((item) => (
                <li key={item} className="flex items-start gap-2">
                  <span className="mt-2 h-1 w-1 shrink-0 rounded-full bg-accent" />
                  <EvidenceText text={item} eventIndex={index} />
                </li>
              ))}
            </ul>
            <SourceCitations
              sources={event.evidenceSources ?? []}
              eventIndex={index}
            />
          </article>
        ))}
      </div>
    </section>
  );
}
