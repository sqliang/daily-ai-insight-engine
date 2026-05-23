// ============================================================================
// ArticleCardBasic.tsx — 文章基础信息卡片
//
// 展示文章标题（外链）、域名、发布日期、作者、ID 摘要和正文摘要。
// 被 ArticleCard 消费，最终渲染在 SourceDetailPage（src/app/sources/[name]/page.tsx）。
// ============================================================================

type ArticleCardBasicProps = {
  title: string;
  url: string;
  published: string;
  author: string;
  summary: string;
  id?: string;
};

function getDomain(url: string): string {
  try {
    return new URL(url).hostname.replace(/^www\./, "");
  } catch {
    return url;
  }
}

/**
 * 文章基础信息卡片，在 SourceDetailPage 的 ArticleList 中渲染每篇文章。
 *
 * 展示文章标题（外链）、域名、发布日期、作者、文章 ID 摘要以及正文前几行。
 * 无摘要时显示"（无摘要）"占位提示。
 */
export function ArticleCardBasic({
  title,
  url,
  published,
  author,
  summary,
  id,
}: ArticleCardBasicProps) {
  return (
    <div>
      <a
        href={url}
        target="_blank"
        rel="noopener noreferrer"
        className="block group/title"
      >
        <h2
          className="text-[20px] font-bold leading-[1.4] text-foreground
                     group-hover/title:text-accent transition-colors duration-200"
        >
          {title || "无标题"}
        </h2>
      </a>

      <div className="mt-2.5 flex items-center gap-2">
        <a
          href={url}
          target="_blank"
          rel="noopener noreferrer"
          className="inline-flex items-center gap-1.5 font-mono text-[13px] text-muted/50
                     hover:text-accent transition-colors duration-200 truncate max-w-[400px]"
        >
          <svg
            width="13"
            height="13"
            viewBox="0 0 16 16"
            fill="none"
            stroke="currentColor"
            strokeWidth="1.5"
            className="shrink-0 text-muted/30"
          >
            <path d="M6 3H3a1 1 0 00-1 1v9a1 1 0 001 1h9a1 1 0 001-1V9" strokeLinecap="round" />
            <path d="M8 8l6-6M14 2h-4M14 2v4" strokeLinecap="round" strokeLinejoin="round" />
          </svg>
          {getDomain(url)}
        </a>
      </div>

      <div className="mt-4 flex flex-wrap items-center gap-2.5">
        {published && (
          <span className="inline-flex items-center gap-1.5 rounded-full border border-line/50 bg-surface px-3.5 py-1.5 text-[13px] font-medium text-muted/70">
            <svg
              width="13"
              height="13"
              viewBox="0 0 16 16"
              fill="none"
              stroke="currentColor"
              strokeWidth="1.5"
              className="text-muted/35 shrink-0"
            >
              <rect x="2" y="3" width="12" height="11" rx="2" />
              <path d="M2 7h12M5 2v3m6-3v3" strokeLinecap="round" />
            </svg>
            {published}
          </span>
        )}
        {author && (
          <span className="inline-flex items-center gap-1.5 rounded-full border border-line/50 bg-surface px-3.5 py-1.5 text-[13px] font-medium text-muted/70">
            <svg
              width="13"
              height="13"
              viewBox="0 0 16 16"
              fill="none"
              stroke="currentColor"
              strokeWidth="1.5"
              className="text-muted/35 shrink-0"
            >
              <circle cx="6" cy="5" r="2.5" />
              <path
                d="M2 14c0-3 2-5 5-5h2c3 0 5 2 5 5"
                strokeLinecap="round"
                strokeLinejoin="round"
              />
            </svg>
            {Array.isArray(author) ? author.join(", ") : author}
          </span>
        )}
        {id && (
          <span className="inline-flex items-center gap-1 rounded-full border border-line/30 bg-surface/50 px-3 py-1.5 text-[12px] font-mono text-muted/30">
            #{id.slice(0, 12)}
          </span>
        )}
      </div>

      {summary ? (
        <p className="mt-5 text-[15px] leading-[1.85] text-foreground/70 line-clamp-4">
          {summary}
        </p>
      ) : (
        <p className="mt-5 text-[15px] leading-relaxed text-muted/25 italic">
          （无摘要）
        </p>
      )}
    </div>
  );
}
