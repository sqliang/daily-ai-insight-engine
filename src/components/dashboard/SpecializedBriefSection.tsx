// ============================================================================
// SpecializedBriefSection.tsx — 日报专题洞察入口 Section
//
// 从 dailyReport.specializedBrief 读取可选子块，
// 渲染为总洞察报告下的轻量延伸入口。
// 这里不展开专题摘要和对象列表，避免打断 /dashboard/[date] 的主报告阅读链路。
// GitHub 与 Product 已恢复；Paper 当前保持关闭，未来有数据后可自然加入入口。
// ============================================================================

import Link from 'next/link';

// ---------------------------------------------------------------------------
// 类型定义（匹配 Stage 4b 输出的 specializedBrief 字段形状）
// ---------------------------------------------------------------------------

interface GithubHighlights {
  summary: string;
  topProjects: string[];
  domainDistribution: Record<string, number>;
  aiCategoryDistribution?: Record<string, number> | null;
  articleCount: number;
}

interface PaperHighlights {
  summary: string;
  keyPapers: string[];
  researchAreas: string[];
  articleCount: number;
}

interface ProductHighlights {
  summary: string;
  notableProducts: string[];
  launchContextDistribution?: Record<string, number>;
  articleCount: number;
}

interface SpecializedBrief {
  githubHighlights?: GithubHighlights | null;
  productHighlights?: ProductHighlights | null;
  paperHighlights?: PaperHighlights | null;
}

interface SpecializedBriefSectionProps {
  data: SpecializedBrief | null | undefined;
  date: string;
  /** 渲染场景：banner 用于深色 ReportHeader 内，surface 用于普通页面背景 */
  variant?: "surface" | "banner";
}

interface InsightLink {
  label: string;
  href: string;
  tone: "accent" | "warm" | "cool";
}

// ---------------------------------------------------------------------------
// 主组件
// ---------------------------------------------------------------------------

/**
 * 日报专题洞察入口 Section。
 *
 * 在 DashboardContent 头部之后渲染，作为主报告的轻量延伸导航。
 * 当 specializedBrief 为空或所有子块均为 null 时，不渲染任何内容。
 */
export function SpecializedBriefSection({
  data,
  date,
  variant = "surface",
}: SpecializedBriefSectionProps) {
  if (!data) return null;

  const links: InsightLink[] = [];

  if (data.githubHighlights) {
    links.push({
      label: "项目洞察",
      href: `/specialized/github/${date}`,
      tone: "accent",
    });
  }

  if (data.productHighlights) {
    links.push({
      label: "产品洞察",
      href: `/specialized/product/${date}`,
      tone: "warm",
    });
  }

  if (data.paperHighlights) {
    links.push({
      label: "论文洞察",
      href: `/specialized/paper/${date}`,
      tone: "cool",
    });
  }

  if (links.length === 0) return null;

  const isBanner = variant === "banner";
  const sectionClass = isBanner
    ? "rounded-xl border border-white/10 bg-white/[0.055] px-4 py-3 backdrop-blur md:px-5"
    : "mt-4 rounded-2xl border border-line/70 bg-panel/75 px-4 py-3 shadow-sm backdrop-blur sm:px-5";
  const titleClass = isBanner
    ? "text-sm font-bold text-white"
    : "text-sm font-bold text-foreground";
  const descriptionClass = isBanner
    ? "mt-1 max-w-3xl text-xs leading-5 text-white/68 md:text-[13px] md:leading-6"
    : "mt-1 max-w-3xl text-xs leading-5 text-foreground/66 md:text-[13px] md:leading-6";

  return (
    <section
      className={sectionClass}
      aria-labelledby="specialized-insight-title"
    >
      <div className="flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
        <div className="flex min-w-0 items-start gap-3">
          <span
            className="mt-1 h-8 w-1 shrink-0 rounded-full bg-gradient-to-b from-accent via-warm to-cool"
            aria-hidden="true"
          />
          <div className="min-w-0">
            <h2
              id="specialized-insight-title"
              className={titleClass}
            >
              专题洞察
            </h2>
            <p className={descriptionClass}>
              在总览趋势之外，进一步识别值得持续跟踪的项目与产品线索，从宏观判断下钻到具体对象，捕捉技术演进与产品化机会。
            </p>
          </div>
        </div>

        <nav
          className="flex flex-wrap items-center gap-2 sm:justify-end"
          aria-label="专题洞察入口"
        >
          {links.map((link) => (
            <InsightLinkChip
              key={link.href}
              link={link}
              variant={variant}
            />
          ))}
        </nav>
      </div>
    </section>
  );
}

// ---------------------------------------------------------------------------
// 入口 Chip
// ---------------------------------------------------------------------------

function InsightLinkChip({
  link,
  variant,
}: {
  link: InsightLink;
  variant: "surface" | "banner";
}) {
  const toneClass =
    variant === "banner"
      ? {
          accent:
            "border-accent-light/35 bg-accent-light/10 text-accent-light hover:border-accent-light/60 hover:bg-accent-light/16",
          warm:
            "border-warm/45 bg-warm/12 text-warm-light hover:border-warm/70 hover:bg-warm/18",
          cool:
            "border-cool/45 bg-cool/12 text-cool-light hover:border-cool/70 hover:bg-cool/18",
        }[link.tone]
      : {
          accent:
            "border-accent/25 bg-accent/8 text-accent hover:border-accent/45 hover:bg-accent/12",
          warm:
            "border-warm/25 bg-warm/8 text-warm hover:border-warm/45 hover:bg-warm/12",
          cool:
            "border-cool/25 bg-cool/8 text-cool hover:border-cool/45 hover:bg-cool/12",
        }[link.tone];

  return (
    <Link
      href={link.href}
      className={`inline-flex min-h-8 items-center gap-1.5 rounded-full border px-3 py-1 text-xs font-semibold transition-colors focus:outline-none focus-visible:ring-2 focus-visible:ring-accent ${toneClass}`}
    >
      {link.label}
      <svg
        className="h-3.5 w-3.5 text-current/60"
        viewBox="0 0 16 16"
        fill="none"
        stroke="currentColor"
        strokeWidth="1.8"
        strokeLinecap="round"
        strokeLinejoin="round"
        aria-hidden="true"
      >
        <path d="M3 8h9" />
        <path d="m9 4 4 4-4 4" />
      </svg>
    </Link>
  );
}
