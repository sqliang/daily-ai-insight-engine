"use client";

// ============================================================================
// LogicFlow.tsx — 逻辑链步骤展示
//
// 以编号步骤列表呈现因果推理过程，支持折叠/展开切换。
// 折叠态仅显示第一步 + 剩余步数，展开态显示完整编号链。
// 被 ArticleCardExtraction 的逻辑链区块消费。
// ============================================================================

import { useState } from "react";

type LogicFlowProps = {
  steps: string[];
};

/**
 * 逻辑链步骤展示组件，以编号步骤列表呈现因果推理过程。
 *
 * 用于 ArticleCardExtraction 的逻辑链区块。支持折叠/展开切换：
 * 折叠态仅显示第一步 + 剩余步骤数，展开态显示完整编号链。
 */
export function LogicFlow({ steps }: LogicFlowProps) {
  const [collapsed, setCollapsed] = useState(false);

  if (steps.length === 0) return null;

  if (collapsed) {
    return (
      <button
        type="button"
        onClick={() => setCollapsed(false)}
        className="w-full text-left group/btn"
      >
        <div className="flex items-center gap-3 py-2 px-3 rounded-lg transition-colors hover:bg-line/30">
          <svg
            width="14"
            height="14"
            viewBox="0 0 16 16"
            fill="none"
            stroke="currentColor"
            strokeWidth="2"
            strokeLinecap="round"
            className="text-muted/30 shrink-0"
          >
            <polyline points="4 10 8 6 12 10" />
          </svg>
          <span className="text-[13px] text-foreground/60 line-clamp-1 flex-1 leading-relaxed">
            {steps[0]}
          </span>
          <span className="text-[12px] text-accent/60 shrink-0 font-medium group-hover/btn:text-accent">
            +{steps.length - 1} 步
          </span>
        </div>
      </button>
    );
  }

  return (
    <div>
      <button
        type="button"
        onClick={() => setCollapsed(true)}
        className="flex items-center gap-2 mb-3 text-[12px] font-semibold text-muted/35 hover:text-accent transition-colors uppercase tracking-wider"
      >
        <svg
          width="12"
          height="12"
          viewBox="0 0 16 16"
          fill="none"
          stroke="currentColor"
          strokeWidth="2"
          strokeLinecap="round"
        >
          <polyline points="4 6 8 10 12 6" />
        </svg>
        收起
      </button>
      <ol className="relative">
        <div
          className="absolute left-[11px] top-3 bottom-3 w-[2px] rounded-full"
          style={{
            background:
              "linear-gradient(to bottom, var(--accent) / 0.25, var(--line) 90%, transparent)",
          }}
        />
        {steps.map((step, i) => {
          const isLast = i === steps.length - 1;
          const isLastTwo = i >= steps.length - 2;
          return (
            <li
              key={i}
              className={`flex items-start gap-3.5 ${isLast ? "" : "mb-3"}`}
            >
              <span
                className="relative z-10 flex h-[24px] w-[24px] shrink-0 items-center justify-center rounded-full text-[11px] font-bold mt-0.5"
                style={{
                  backgroundColor: isLastTwo ? "var(--accent-glow)" : "var(--surface)",
                  color: isLastTwo ? "var(--accent)" : "var(--muted) / 0.6",
                  border: isLastTwo ? "none" : "1.5px solid var(--line)",
                }}
              >
                {i + 1}
              </span>
              <span className={`text-[14px] leading-[1.75] pt-0.5 ${isLastTwo ? "text-foreground/80 font-medium" : "text-foreground/65"}`}>
                {step}
              </span>
            </li>
          );
        })}
      </ol>
    </div>
  );
}
