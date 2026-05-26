// ============================================================================
// MarkdownRenderer.tsx — 日报 Markdown 全文渲染
//
// 针对管道产出日报的结构化排版：章节标题、Top 事件卡片、元数据列表、
// 表格与引用块均使用品牌 Token 强化层次，提升长文阅读体验。
// 仅被 report/[date]/page.tsx 消费。
// ============================================================================

"use client";

import type { ReactElement, ReactNode } from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import type { Components } from "react-markdown";

// ---------------------------------------------------------------------------
// 工具函数
// ---------------------------------------------------------------------------

/**
 * 从 React 子节点递归提取纯文本，用于解析标题中的 `#1` 事件编号。
 */
function getNodeText(node: ReactNode): string {
  if (typeof node === "string") return node;
  if (typeof node === "number") return String(node);
  if (Array.isArray(node)) return node.map(getNodeText).join("");
  if (node && typeof node === "object" && "props" in node) {
    const element = node as ReactElement<{ children?: ReactNode }>;
    return getNodeText(element.props.children);
  }
  return "";
}

/**
 * 去掉文首一级标题，避免与 ReportHeader 标题重复。
 */
function stripLeadingH1(markdown: string): string {
  return markdown.replace(/^\s*#\s+[^\n]+\n+/, "");
}

/** Top 事件标题：`### #1 标题` */
const TOP_EVENT_HEADING = /^#(\d+)\s+(.+)$/;

// ---------------------------------------------------------------------------
// Markdown 组件映射
// ---------------------------------------------------------------------------

function createMarkdownComponents(): Components {
  return {
    h1: ({ children, ...props }) => (
      <h1
        className="mb-8 border-b border-line pb-4 text-2xl font-bold tracking-tight text-foreground md:text-3xl"
        {...props}
      >
        {children}
      </h1>
    ),

    h2: ({ children, ...props }) => (
      <div className="mt-12 scroll-mt-24 first:mt-0">
        <div className="mb-5 flex items-center gap-3">
          <span
            className="h-9 w-1 shrink-0 rounded-full bg-gradient-to-b from-accent to-accent-dark"
            aria-hidden
          />
          <h2
            className="text-xl font-bold tracking-tight text-foreground md:text-2xl"
            {...props}
          >
            {children}
          </h2>
        </div>
      </div>
    ),

    h3: ({ children, ...props }) => {
      const text = getNodeText(children).trim();
      const topEvent = text.match(TOP_EVENT_HEADING);

      if (topEvent) {
        const [, rank, title] = topEvent;
        return (
          <div
            className="event-rank-header mt-8 flex gap-4 overflow-hidden rounded-t-xl border border-line border-b-0 bg-gradient-to-r from-accent-light/50 via-panel to-panel px-5 py-4 shadow-sm md:px-6"
            {...props}
          >
            <span
              className="flex h-11 w-11 shrink-0 items-center justify-center rounded-xl bg-accent text-lg font-bold tabular-nums text-white shadow-glow"
              aria-label={`事件排名 ${rank}`}
            >
              {rank}
            </span>
            <h3 className="min-w-0 flex-1 pt-1 text-lg font-bold leading-snug text-foreground md:text-xl">
              {title}
            </h3>
          </div>
        );
      }

      return (
        <h3
          className="mb-3 mt-8 flex items-center gap-2 text-base font-semibold text-foreground md:text-lg"
          {...props}
        >
          <span className="h-1.5 w-1.5 shrink-0 rounded-full bg-cool" aria-hidden />
          {children}
        </h3>
      );
    },

    p: ({ children, ...props }) => (
      <p className="my-4 text-[15px] leading-8 text-muted md:text-base" {...props}>
        {children}
      </p>
    ),

    ul: ({ children, ...props }) => (
      <ul
        className="my-4 space-y-2.5 rounded-xl border border-line/70 bg-background/60 px-4 py-3.5 md:px-5 [&>li]:list-none [&>li]:pl-0"
        {...props}
      >
        {children}
      </ul>
    ),

    ol: ({ children, ...props }) => (
      <ol
        className="my-4 list-decimal space-y-2 rounded-xl border border-line/70 bg-background/60 px-5 py-3.5 pl-8 md:px-6"
        {...props}
      >
        {children}
      </ol>
    ),

    li: ({ children, ...props }) => (
      <li
        className="text-[15px] leading-7 text-muted [&>strong:first-child]:mr-1 [&>strong:first-child]:font-semibold [&>strong:first-child]:text-foreground"
        {...props}
      >
        <span className="flex gap-2">
          <span className="mt-2.5 h-1.5 w-1.5 shrink-0 rounded-full bg-accent/70" aria-hidden />
          <span className="min-w-0 flex-1">{children}</span>
        </span>
      </li>
    ),

    table: ({ children, ...props }) => (
      <div className="my-6 overflow-hidden rounded-xl border border-line shadow-sm">
        <div className="overflow-x-auto">
          <table className="min-w-full border-collapse text-sm" {...props}>
            {children}
          </table>
        </div>
      </div>
    ),

    thead: ({ children, ...props }) => (
      <thead className="bg-gradient-to-r from-accent-light/60 to-surface" {...props}>
        {children}
      </thead>
    ),

    th: ({ children, ...props }) => (
      <th
        className="border-b border-line px-4 py-3 text-left text-xs font-semibold uppercase tracking-wider text-foreground"
        {...props}
      >
        {children}
      </th>
    ),

    td: ({ children, ...props }) => (
      <td
        className="border-b border-line/80 px-4 py-3 text-sm leading-6 text-muted last:border-0"
        {...props}
      >
        {children}
      </td>
    ),

    tr: ({ children, ...props }) => (
      <tr className="even:bg-surface/80 transition-colors hover:bg-accent-light/20" {...props}>
        {children}
      </tr>
    ),

    blockquote: ({ children, ...props }) => (
      <blockquote
        className="my-6 rounded-r-xl border-l-4 border-warm bg-warm-light/40 px-5 py-4 text-[15px] leading-7 text-foreground shadow-sm"
        {...props}
      >
        {children}
      </blockquote>
    ),

    strong: ({ children, ...props }) => (
      <strong className="font-semibold text-foreground" {...props}>
        {children}
      </strong>
    ),

    em: ({ children, ...props }) => (
      <em className="italic text-foreground/85" {...props}>
        {children}
      </em>
    ),

    hr: () => (
      <div className="my-10 flex items-center gap-3" role="separator">
        <span className="h-px flex-1 bg-gradient-to-r from-transparent via-line to-transparent" />
        <span className="text-[10px] font-semibold uppercase tracking-widest text-muted/60">
          · · ·
        </span>
        <span className="h-px flex-1 bg-gradient-to-r from-transparent via-line to-transparent" />
      </div>
    ),

    a: ({ children, href, ...props }) => (
      <a
        href={href}
        className="font-medium text-accent underline decoration-accent/30 underline-offset-4 transition-colors hover:text-accent-dark hover:decoration-accent"
        target={href?.startsWith("http") ? "_blank" : undefined}
        rel={href?.startsWith("http") ? "noopener noreferrer" : undefined}
        {...props}
      >
        {children}
      </a>
    ),

    code: ({ children, className, ...props }) => {
      const isBlock = className?.includes("language-");
      if (isBlock) {
        return (
          <code
            className={`block overflow-x-auto rounded-lg bg-foreground/5 px-4 py-3 font-mono text-sm text-foreground ${className ?? ""}`}
            {...props}
          >
            {children}
          </code>
        );
      }
      return (
        <code
          className="rounded-md bg-accent-light/50 px-1.5 py-0.5 font-mono text-[0.9em] text-accent-dark"
          {...props}
        >
          {children}
        </code>
      );
    },

    pre: ({ children, ...props }) => (
      <pre
        className="my-6 overflow-hidden rounded-xl border border-line bg-foreground/[0.03] p-0"
        {...props}
      >
        {children}
      </pre>
    ),
  };
}

// ---------------------------------------------------------------------------
// 导出组件
// ---------------------------------------------------------------------------

type MarkdownRendererProps = {
  content: string;
  /**
   * 正文栏最大宽度 Tailwind class。
   * 默认 max-w-6xl：与 PageShell 协调，表格与长文更舒展。
   */
  maxWidthClass?: string;
  /** 去掉与 ReportHeader 重复的首行 # 标题 */
  stripDuplicateTitle?: boolean;
};

/**
 * 将 Markdown 字符串渲染为带品牌排版的长文阅读视图。
 */
export function MarkdownRenderer({
  content,
  maxWidthClass = "max-w-6xl",
  stripDuplicateTitle = true,
}: MarkdownRendererProps) {
  const markdown = stripDuplicateTitle ? stripLeadingH1(content) : content;
  const components = createMarkdownComponents();

  return (
    <article
      className={[
        "report-article mx-auto w-full overflow-hidden rounded-2xl border border-line bg-panel shadow-md ring-1 ring-line/50",
        maxWidthClass,
        /* Top 事件：标题栏 + 紧随其后的列表/段落视觉上合并为一张卡片 */
        "[&_.event-rank-header+ul]:mt-0 [&_.event-rank-header+ul]:rounded-none [&_.event-rank-header+ul]:border-t-0 [&_.event-rank-header+ul]:border-x [&_.event-rank-header+ul]:border-b-0 [&_.event-rank-header+ul]:bg-surface/90",
        "[&_.event-rank-header+ul+p]:my-0 [&_.event-rank-header+ul+p]:border-x [&_.event-rank-header+ul+p]:border-line/70 [&_.event-rank-header+ul+p]:bg-surface/90 [&_.event-rank-header+ul+p]:px-5 [&_.event-rank-header+ul+p]:py-2 [&_.event-rank-header+ul+p]:text-xs [&_.event-rank-header+ul+p]:font-semibold [&_.event-rank-header+ul+p]:uppercase [&_.event-rank-header+ul+p]:tracking-wider [&_.event-rank-header+ul+p]:text-accent-dark",
        "[&_.event-rank-header+ul+p+ul]:mt-0 [&_.event-rank-header+ul+p+ul]:rounded-b-xl [&_.event-rank-header+ul+p+ul]:border [&_.event-rank-header+ul+p+ul]:border-t-0 [&_.event-rank-header+ul+p+ul]:bg-surface/90 [&_.event-rank-header+ul+p+ul]:mb-8",
        "[&_.event-rank-header+ul:not(:has(+p))]:mb-8 [&_.event-rank-header+ul:not(:has(+p))]:rounded-b-xl [&_.event-rank-header+ul:not(:has(+p))]:border-b",
      ].join(" ")}
    >
      {/* 顶部品牌色条 */}
      <div
        className="h-1 bg-gradient-to-r from-accent via-accent-light to-cool"
        aria-hidden
      />

      <div className="px-5 py-8 md:px-10 md:py-10 lg:px-12">
        <ReactMarkdown remarkPlugins={[remarkGfm]} components={components}>
          {markdown}
        </ReactMarkdown>
      </div>
    </article>
  );
}
