// ============================================================================
// SourceCitations.tsx — 参考来源引用列表
//
// 位于每个 TopEvent 底部，编号列表展示证据来源。
// evidence 中的 [1][2][3] 编号标记点击后锚定到此处对应行。
// ============================================================================

import type { EvidenceSource } from "@/lib/agent/schema";

// ---------------------------------------------------------------------------
// Props
// ---------------------------------------------------------------------------

interface SourceCitationsProps {
  sources: EvidenceSource[];
  /** Event 在列表中的索引，用于生成锚点 id */
  eventIndex: number;
}

// ---------------------------------------------------------------------------
// 来源名 → 颜色映射（六色轮换）
// ---------------------------------------------------------------------------

const TAG_COLORS = [
  "bg-blue-50 text-blue-700 ring-blue-200",
  "bg-emerald-50 text-emerald-700 ring-emerald-200",
  "bg-amber-50 text-amber-700 ring-amber-200",
  "bg-violet-50 text-violet-700 ring-violet-200",
  "bg-rose-50 text-rose-700 ring-rose-200",
  "bg-cyan-50 text-cyan-700 ring-cyan-200",
];

// ---------------------------------------------------------------------------
// Component
// ---------------------------------------------------------------------------

export function SourceCitations({ sources, eventIndex }: SourceCitationsProps) {
  if (!sources || sources.length === 0) return null;

  return (
    <div id={`src-${eventIndex}-list`} className="mt-4 rounded-xl border border-line bg-surface/40 p-4">
      <h4 className="mb-2.5 text-xs font-semibold uppercase tracking-wider text-muted">
        参考来源
      </h4>
      <ol className="space-y-1.5">
        {sources.map((source, i) => (
          <li
            key={source.url}
            id={`src-${eventIndex}-${i + 1}`}
            className="flex items-center gap-2 text-xs leading-5"
          >
            {/* 编号 badge */}
            <span className="inline-flex h-4 w-4 shrink-0 items-center justify-center rounded bg-accent/10 text-[10px] font-semibold tabular-nums text-accent">
              {i + 1}
            </span>
            {/* 来源名彩色标签 */}
            <span
              className={`inline-flex shrink-0 items-center rounded px-1.5 py-px text-[10px] font-medium ring-1 ring-inset ${TAG_COLORS[i % TAG_COLORS.length]}`}
            >
              {source.sourceDir}
            </span>
            {/* 标题 + 链接 */}
            <a
              href={source.url}
              target="_blank"
              rel="noopener noreferrer"
              className="min-w-0 truncate text-muted-foreground transition-colors hover:text-foreground hover:underline"
            >
              {source.title}
            </a>
            {/* 外链图标 */}
            <svg
              width="10"
              height="10"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              strokeWidth="2"
              strokeLinecap="round"
              strokeLinejoin="round"
              className="shrink-0 opacity-30"
            >
              <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6" />
              <polyline points="15 3 21 3 21 9" />
              <line x1="10" y1="14" x2="21" y2="3" />
            </svg>
          </li>
        ))}
      </ol>
    </div>
  );
}
