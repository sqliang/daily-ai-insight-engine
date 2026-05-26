// ============================================================================
// SiteFooter.tsx — 全站页脚声明与作者信息
//
// 在根 layout 底部展示免责说明与开源链接，所有页面统一可见。
// ============================================================================

const GITHUB_PROFILE = "https://github.com/sqliang";
const GITHUB_REPO = "https://github.com/sqliang/daily-ai-insight-engine";

/**
 * 全站页脚：AI 生成内容免责、个人项目说明与源码链接。
 */
export function SiteFooter() {
  return (
    <footer className="mt-auto border-t border-line/60 bg-surface/50">
      <div className="mx-auto max-w-7xl px-4 py-8 sm:px-6 md:px-8 md:py-10">
        <div className="flex flex-col gap-6 md:flex-row md:items-start md:justify-between">
          {/* 免责与产品说明 */}
          <div className="max-w-2xl space-y-2">
            <p className="text-[13px] font-semibold tracking-tight text-foreground">
              免责声明
            </p>
            <p className="text-[13px] leading-relaxed text-muted">
              本站内容由 AI 自动聚合、分析与生成，仅供信息参考与学习交流，不构成投资、法律、医疗或其他重大决策建议。请结合原始信源独立判断，作者不对因使用本站内容而产生的任何后果承担责任。
            </p>
          </div>

          {/* 作者与源码 */}
          <div className="shrink-0 space-y-2 md:text-right">
            <p className="text-[13px] font-semibold tracking-tight text-foreground">
              关于本项目
            </p>
            <p className="text-[13px] leading-relaxed text-muted">
              个人开源实验项目，由{" "}
              <a
                href={GITHUB_PROFILE}
                target="_blank"
                rel="noopener noreferrer"
                className="font-medium text-accent underline decoration-accent/30 underline-offset-2 hover:text-accent-dark"
              >
                @sqliang
              </a>{" "}
              构建与维护。
            </p>
            <a
              href={GITHUB_REPO}
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center gap-1.5 text-[13px] font-medium text-accent transition-colors hover:text-accent-dark md:ml-auto md:flex md:justify-end"
            >
              <svg
                width="14"
                height="14"
                viewBox="0 0 24 24"
                fill="currentColor"
                aria-hidden
              >
                <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-3.795-.735-.405-1.03-1.005-1.305-1.005-1.305-.825-.555.015-.555.015-.555.9.105 1.365 1.2 1.365 1.2.81 1.395 2.085.99 2.595.765.09-.6.315-.99.57-1.215-2.4-.27-4.92-1.2-4.92-5.355 0-1.185.42-2.145 1.125-2.895-.12-.27-.48-1.365.105-2.85 0 0 .915-.3 3.015 1.14.87-.24 1.805-.36 2.73-.36.93 0 1.86.12 2.73.36 2.1-1.44 3.015-1.14 3.015-1.14.585 1.485.225 2.58.105 2.85.705.75 1.125 1.71 1.125 2.895 0 4.17-2.52 5.085-4.935 5.355.39.33.735.96.735 1.955 0 1.41-.015 2.55-.015 2.895 0 .315.225.69.84.57A8.203 8.203 0 0 0 24 12c0-6.63-5.37-12-12-12z" />
              </svg>
              在 GitHub 查看源码
            </a>
          </div>
        </div>

        <p className="mt-6 border-t border-line/50 pt-5 text-center text-[11px] text-muted/80">
          © {new Date().getFullYear()} Daily AI Insight Engine · Built with AI-assisted pipelines
        </p>
      </div>
    </footer>
  );
}
