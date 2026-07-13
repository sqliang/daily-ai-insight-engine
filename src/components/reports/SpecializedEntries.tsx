// ============================================================================
// SpecializedEntries.tsx — 专题报告子条目组件
//
// 在 ReportCard 内部渲染，展示该日期可用的专题报告类型。
// 每个条目是一个可点击的链接（有数据时）或灰显占位（无数据/即将上线）。
// ============================================================================

import Link from "next/link";
import type { SpecializedAvailability } from "@/lib/data/reports";

// ---------------------------------------------------------------------------
// 领域中文标签映射
// ---------------------------------------------------------------------------

const DOMAIN_LABELS: Record<string, string> = {
  ai_ml: "AI/ML",
  web_frontend: "Web 前端",
  web_backend: "Web 后端",
  devops_infra: "DevOps",
  database_storage: "数据库",
  programming_languages: "编程语言",
  developer_tools: "开发者工具",
  security: "安全",
  mobile: "移动端",
  blockchain: "区块链",
  data_engineering: "数据工程",
  game_development: "游戏开发",
  documentation: "文档",
  iot_embedded: "IoT/嵌入式",
  other: "其他",
};

// ---------------------------------------------------------------------------
// Props
// ---------------------------------------------------------------------------

interface SpecializedEntriesProps {
  specialized: SpecializedAvailability;
  date: string;
}

// ---------------------------------------------------------------------------
// 子条目组件
// ---------------------------------------------------------------------------

interface EntryProps {
  icon: string;
  label: string;
  href: string;
  stat: string;
  detail?: string;
  enabled: boolean;
}

function EntryRow({ icon, label, href, stat, detail, enabled }: EntryProps) {
  const content = (
    <div
      className={`flex items-center gap-3 rounded-lg px-3 py-2 transition-colors ${
        enabled
          ? "hover:bg-white/60 dark:hover:bg-gray-800/60 cursor-pointer"
          : "opacity-40 cursor-default"
      }`}
    >
      {/* 图标 */}
      <span className="text-lg flex-shrink-0">{icon}</span>

      {/* 标签 + 统计 */}
      <div className="flex-1 min-w-0">
        <div className="flex items-center gap-2">
          <span className="text-sm font-medium text-gray-800 dark:text-gray-200">
            {label}
          </span>
          <span
            className={`text-xs font-medium ${
              enabled
                ? "text-gray-500 dark:text-gray-400"
                : "text-gray-400 dark:text-gray-500"
            }`}
          >
            · {stat}
          </span>
        </div>
        {detail && (
          <p className="text-xs text-gray-400 dark:text-gray-500 mt-0.5 truncate">
            {detail}
          </p>
        )}
      </div>

      {/* 箭头 */}
      {enabled && (
        <svg
          className="w-4 h-4 text-gray-300 dark:text-gray-600 flex-shrink-0"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth={2}
            d="M9 5l7 7-7 7"
          />
        </svg>
      )}
    </div>
  );

  if (enabled) {
    return <Link href={href}>{content}</Link>;
  }
  return content;
}

// ---------------------------------------------------------------------------
// 主组件
// ---------------------------------------------------------------------------

/**
 * 专题报告子条目列表。
 *
 * 在日报卡片内展示该日期可用的专题报告入口。
 * 当前 Phase 1 仅 GitHub 可用，Product/Paper 显示为"即将上线"占位。
 */
export function SpecializedEntries({
  specialized,
  date,
}: SpecializedEntriesProps) {
  // 如果所有专题都无数据且未上线，不渲染任何内容
  const hasAnyContent =
    specialized.github || specialized.product || specialized.paper;
  if (!hasAnyContent) {
    // 仅渲染"即将上线"占位（Phase 2/3 预告）
    return (
      <div className="mt-3 pt-3 border-t border-gray-100 dark:border-gray-800">
        <div className="flex items-center gap-2 text-xs text-gray-400 dark:text-gray-500 mb-2">
          <svg className="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" />
          </svg>
          <span className="font-medium">专题报告</span>
        </div>
        <EntryRow
          icon="🐙"
          label="GitHub 项目"
          href=""
          stat="即将上线"
          enabled={false}
        />
        <EntryRow
          icon="📄"
          label="论文速递"
          href=""
          stat="即将上线"
          enabled={false}
        />
        <EntryRow
          icon="📦"
          label="产品扫描"
          href=""
          stat="即将上线"
          enabled={false}
        />
      </div>
    );
  }

  // GitHub 条目
  const githubEntry = (() => {
    if (specialized.github) {
      const { count, domains } = specialized.github;
      const topDomains = Object.entries(domains)
        .sort((a, b) => b[1] - a[1])
        .slice(0, 3)
        .map(([d, c]) => `${DOMAIN_LABELS[d] || d} ×${c}`)
        .join(" · ");
      return (
        <EntryRow
          icon="🐙"
          label="GitHub 项目"
          href={`/specialized/github/${date}`}
          stat={`${count} 个项目`}
          detail={topDomains}
          enabled
        />
      );
    }
    return (
      <EntryRow
        icon="🐙"
        label="GitHub 项目"
        href=""
        stat="暂无数据"
        enabled={false}
      />
    );
  })();

  // Phase 2/3 占位
  const productEntry = specialized.product ? (
    <EntryRow
      icon="📦"
      label="产品扫描"
      href={`/specialized/product/${date}`}
      stat={`${specialized.product.count} 个产品`}
      enabled
    />
  ) : (
    <EntryRow
      icon="📦"
      label="产品扫描"
      href=""
      stat="即将上线"
      enabled={false}
    />
  );

  const paperEntry = specialized.paper ? (
    <EntryRow
      icon="📄"
      label="论文速递"
      href={`/specialized/paper/${date}`}
      stat={`${specialized.paper.count} 篇论文`}
      enabled
    />
  ) : (
    <EntryRow
      icon="📄"
      label="论文速递"
      href=""
      stat="即将上线"
      enabled={false}
    />
  );

  return (
    <div className="mt-3 pt-3 border-t border-gray-100 dark:border-gray-800">
      <div className="flex items-center gap-2 text-xs text-gray-400 dark:text-gray-500 mb-1 px-1">
        <svg
          className="w-3.5 h-3.5"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth={2}
            d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"
          />
        </svg>
        <span className="font-medium">专题报告</span>
      </div>
      <div className="space-y-0.5 py-0.5">
        {githubEntry}
        {paperEntry}
        {productEntry}
      </div>
    </div>
  );
}
