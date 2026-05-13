"use client";

import { useState } from "react";

type LogicFlowProps = {
  steps: string[];
};

export function LogicFlow({ steps }: LogicFlowProps) {
  const [expanded, setExpanded] = useState(false);

  if (steps.length === 0) return null;

  if (!expanded) {
    return (
      <button
        type="button"
        onClick={() => setExpanded(true)}
        className="group w-full text-left"
      >
        <div className="flex items-center gap-2">
          <span className="text-[12px] font-semibold text-muted/35 uppercase tracking-wider">
            逻辑链
          </span>
          <span className="text-[13px] text-foreground/65 line-clamp-1 flex-1 leading-relaxed">
            {steps[0]}
          </span>
          <span className="text-[12px] text-accent shrink-0 font-medium group-hover:underline">
            展开全部 ({steps.length})
          </span>
        </div>
      </button>
    );
  }

  return (
    <div>
      <button
        type="button"
        onClick={() => setExpanded(false)}
        className="mb-3 text-[12px] font-semibold text-muted/35 uppercase tracking-wider hover:text-accent transition-colors"
      >
        收起逻辑链
      </button>
      <ol className="relative space-y-2">
        <div
          className="absolute left-[8px] top-2 bottom-2 w-[1.5px]"
          style={{
            background:
              "linear-gradient(to bottom, var(--line), var(--line) 80%, transparent)",
          }}
        />
        {steps.map((step, i) => (
          <li key={i} className="flex items-start gap-3 pl-0.5">
            <span
              className="relative z-10 flex h-[18px] w-[18px] shrink-0 items-center justify-center rounded-full text-[10px] font-bold"
              style={{
                backgroundColor: "var(--accent-glow)",
                color: "var(--accent)",
              }}
            >
              {i + 1}
            </span>
            <span className="text-[13px] leading-[1.75] text-foreground/75">
              {step}
            </span>
          </li>
        ))}
      </ol>
    </div>
  );
}
