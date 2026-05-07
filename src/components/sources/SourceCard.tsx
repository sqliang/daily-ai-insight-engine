import type { SourceStatus } from "@/lib/data/sources";

const tierColor: Record<string, string> = {
  A: "var(--accent)",
  B: "var(--warm)",
  C: "var(--cool)",
};

const tierLabel: Record<string, string> = {
  A: "Tier A",
  B: "Tier B",
  C: "Tier C",
};

const sourceTypeLabel: Record<string, string> = {
  academic_paper: "学术论文",
  tech_blog: "技术博客",
  news_media: "科技媒体",
  community_discussion: "社区讨论",
};

type SourceCardProps = {
  source: SourceStatus;
};

export function SourceCard({ source }: SourceCardProps) {
  const color = tierColor[source.tier] ?? "var(--line)";

  return (
    <article
      className="rounded-xl border border-line bg-panel shadow-sm transition-shadow hover:shadow-md"
      style={{ borderTopColor: color, borderTopWidth: 2 }}
    >
      {/* Header */}
      <div className="p-5 pb-3">
        <div className="flex items-start justify-between gap-2">
          <h3 className="text-[15px] font-semibold text-foreground leading-snug">
            {source.name}
          </h3>
          <span className="shrink-0 rounded-full bg-accent/10 px-2 py-0.5 text-[10px] font-semibold text-accent">
            {source.articleCount} articles
          </span>
        </div>

        {/* Badge row */}
        <div className="mt-2 flex flex-wrap items-center gap-1.5">
          <span
            className="inline-flex items-center rounded-full px-2 py-0.5 text-[10px] font-medium"
            style={{ backgroundColor: `${color}18`, color }}
          >
            {tierLabel[source.tier] ?? source.tier}
          </span>
          <span className="rounded-full border border-line px-2 py-0.5 text-[10px] font-medium text-muted">
            {sourceTypeLabel[source.type] ?? source.type}
          </span>
          <span className="rounded-full border border-line px-2 py-0.5 text-[10px] font-medium text-muted">
            {source.language === "zh" ? "中文" : "EN"}
          </span>
          {source.fetch_strategy && (
            <span className="rounded-full border border-line px-2 py-0.5 text-[10px] text-muted/70">
              {source.fetch_strategy}
            </span>
          )}
        </div>

        {/* Description */}
        {source.description && (
          <p className="mt-2.5 text-[13px] leading-relaxed text-muted">
            {source.description}
          </p>
        )}

        {/* URL */}
        <a
          href={source.url}
          target="_blank"
          rel="noopener noreferrer"
          className="mt-2 inline-block truncate max-w-full text-[12px] text-muted/60 hover:text-accent transition-colors"
        >
          {source.url}
        </a>
      </div>

      {/* Article list */}
      {source.manifestFound && source.articles.length > 0 ? (
        <div className="border-t border-line max-h-64 overflow-y-auto">
          <ul className="divide-y divide-line">
            {source.articles.map((article, i) => (
              <li key={i} className="px-5 py-2.5">
                <a
                  href={article.url}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="group block"
                >
                  <p className="text-[13px] font-medium leading-snug text-foreground/80 group-hover:text-accent transition-colors line-clamp-2">
                    {article.title}
                  </p>
                  <div className="mt-1 flex items-center gap-2 text-[11px] text-muted/60">
                    <span>{article.published}</span>
                    {article.author && <span>{article.author}</span>}
                  </div>
                  {article.summary && (
                    <p className="mt-1 text-[11px] leading-relaxed text-muted/50 line-clamp-2">
                      {article.summary}
                    </p>
                  )}
                </a>
              </li>
            ))}
          </ul>
        </div>
      ) : (
        <div className="border-t border-line px-5 py-4">
          <p className="text-[12px] text-muted/50 italic">
            {source.manifestFound
              ? "No articles in current pipeline run"
              : "No manifest data — awaiting pipeline run"}
          </p>
        </div>
      )}

      {/* Footer metadata */}
      {source.manifestGeneratedAt && (
        <div className="border-t border-line px-5 py-2">
          <p className="text-[10px] text-muted/50">
            Generated: {new Date(source.manifestGeneratedAt).toLocaleString("zh-CN")}
          </p>
        </div>
      )}
    </article>
  );
}
