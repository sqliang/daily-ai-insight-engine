type ArticleCardBasicProps = {
  title: string;
  url: string;
  published: string;
  author: string;
  summary: string;
  id?: string;
};

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
      {/* Title */}
      <a
        href={url}
        target="_blank"
        rel="noopener noreferrer"
        className="block"
      >
        <h3
          className="text-[18px] font-bold leading-tight text-foreground
                     group-hover:text-accent transition-colors duration-200"
        >
          {title || "无标题"}
        </h3>
      </a>

      {/* URL */}
      <a
        href={url}
        target="_blank"
        rel="noopener noreferrer"
        className="mt-2 block w-full break-all font-mono text-[13px] text-muted/50
                   hover:text-accent transition-colors duration-200 leading-relaxed"
      >
        {url}
      </a>

      {/* Meta pills */}
      <div className="mt-3.5 flex flex-wrap items-center gap-2">
        {published && (
          <span className="inline-flex items-center gap-1 rounded-full border border-line/60 bg-surface px-3 py-1 text-[12px] font-medium text-muted">
            <svg
              width="12"
              height="12"
              viewBox="0 0 16 16"
              fill="none"
              stroke="currentColor"
              strokeWidth="1.5"
              className="text-muted/40 shrink-0"
            >
              <rect x="2" y="3" width="12" height="11" rx="2" />
              <path d="M2 7h12M5 2v3m6-3v3" strokeLinecap="round" />
            </svg>
            {published}
          </span>
        )}
        {author && (
          <span className="inline-flex items-center gap-1 rounded-full border border-line/60 bg-surface px-3 py-1 text-[12px] font-medium text-muted">
            <svg
              width="12"
              height="12"
              viewBox="0 0 16 16"
              fill="none"
              stroke="currentColor"
              strokeWidth="1.5"
              className="text-muted/40 shrink-0"
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
          <span className="inline-flex items-center gap-1 rounded-full border border-line/40 bg-surface/50 px-3 py-1 text-[11px] font-mono text-muted/30">
            #{id.slice(0, 12)}
          </span>
        )}
      </div>

      {/* Summary */}
      {summary ? (
        <p className="mt-4 text-[14px] leading-[1.8] text-foreground/72 line-clamp-3">
          {summary}
        </p>
      ) : (
        <p className="mt-4 text-[14px] leading-relaxed text-muted/25 italic">
          （无摘要）
        </p>
      )}
    </div>
  );
}
