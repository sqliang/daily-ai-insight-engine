type ArticleCardProps = {
  article: {
    url: string;
    title: string;
    published: string;
    summary: string;
    author: string;
    id?: string;
  };
};

export function ArticleCard({ article }: ArticleCardProps) {
  return (
    <article
      className="group rounded-xl border border-line bg-panel/80 backdrop-blur-sm p-5
                 transition-all duration-300 ease-out overflow-hidden
                 hover:shadow-lg hover:-translate-y-0.5 hover:border-accent/25"
    >
      {/* Title — larger, prominent */}
      <a
        href={article.url}
        target="_blank"
        rel="noopener noreferrer"
        className="block"
      >
        <h3 className="text-[16px] font-semibold leading-snug text-foreground
                       group-hover:text-accent transition-colors duration-200">
          {article.title || "无标题"}
        </h3>
      </a>

      {/* URL — right after title, prominent mono */}
      <a
        href={article.url}
        target="_blank"
        rel="noopener noreferrer"
        className="mt-1.5 block w-full break-all font-mono text-[12px] text-muted/55
                   hover:text-accent transition-colors duration-200 leading-relaxed"
      >
        {article.url}
      </a>

      {/* Meta tags — date & author as pills */}
      <div className="mt-3 flex flex-wrap items-center gap-2">
        {article.published && (
          <span className="inline-flex items-center gap-1 rounded-full border border-line/60 bg-surface px-2.5 py-0.5 text-[11px] font-medium text-muted">
            <svg
              width="11"
              height="11"
              viewBox="0 0 16 16"
              fill="none"
              stroke="currentColor"
              strokeWidth="1.5"
              className="text-muted/40 shrink-0"
            >
              <rect x="2" y="3" width="12" height="11" rx="2" />
              <path d="M2 7h12M5 2v3m6-3v3" strokeLinecap="round" />
            </svg>
            {article.published}
          </span>
        )}
        {article.author && (
          <span className="inline-flex items-center gap-1 rounded-full border border-line/60 bg-surface px-2.5 py-0.5 text-[11px] font-medium text-muted">
            <svg
              width="11"
              height="11"
              viewBox="0 0 16 16"
              fill="none"
              stroke="currentColor"
              strokeWidth="1.5"
              className="text-muted/40 shrink-0"
            >
              <circle cx="6" cy="5" r="2.5" />
              <path d="M2 14c0-3 2-5 5-5h2c3 0 5 2 5 5" strokeLinecap="round" strokeLinejoin="round" />
            </svg>
            {article.author}
          </span>
        )}
        {article.id && (
          <span className="inline-flex items-center gap-1 rounded-full border border-line/40 bg-surface/50 px-2.5 py-0.5 text-[10px] font-mono text-muted/35">
            #{article.id}
          </span>
        )}
      </div>

      {/* Summary — readable */}
      {article.summary ? (
        <p className="mt-3 text-[13px] leading-7 text-foreground/72">
          {article.summary}
        </p>
      ) : (
        <p className="mt-3 text-[13px] leading-relaxed text-muted/30 italic">
          （无摘要）
        </p>
      )}
    </article>
  );
}
