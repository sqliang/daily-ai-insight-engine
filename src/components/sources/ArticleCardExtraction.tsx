import {
  EVENT_TYPE_LABELS,
  EPISTEMIC_STATUS_LABELS,
} from "@/lib/data/status";
import { SOURCE_TYPE_LABELS } from "@/lib/data/tiers";
import { EntityChips } from "./EntityChips";
import { LogicFlow } from "./LogicFlow";

type ArticleCardExtractionProps = {
  tldr?: string;
  objectiveSummary?: string;
  eventType?: string;
  sourceType?: string;
  entities?: {
    companies: string[];
    technologies: string[];
    key_people: string[];
  };
  keyLogicFlow?: string[];
  epistemicStatus?: string;
};

/**
 * 信息提取阶段内容展示。
 *
 * 采用统一的「语义左边框卡片」视觉系统：
 * 每个 block 使用 3px 左侧色条 + 语义色浅底 + 图标/标题区，
 * 自上而下视觉权重递减，颜色从 teal → neutral → amber → plum 过渡。
 */
export function ArticleCardExtraction({
  tldr,
  objectiveSummary,
  eventType,
  sourceType,
  entities,
  keyLogicFlow,
  epistemicStatus,
}: ArticleCardExtractionProps) {
  const hasExtraction = tldr || objectiveSummary || eventType || entities;
  if (!hasExtraction) return null;

  return (
    <div className="space-y-5">
      {/* ---- TL;DR：扫描锚点，最强视觉权重 ---- */}
      {tldr && (
        <div
          className="pl-4 py-3 rounded-r-lg"
          style={{
            borderLeft: "3px solid var(--accent)",
            backgroundColor: "color-mix(in oklch, var(--accent) 4%, transparent)",
          }}
        >
          <div className="text-[11px] font-bold text-accent/60 uppercase tracking-widest mb-1.5">
            TL;DR
          </div>
          <p className="text-[16px] font-semibold leading-[1.6] text-foreground/85">
            {tldr}
          </p>
        </div>
      )}

      {/* ---- 元信息标签行：轻量分隔带，不加容器卡片 ---- */}
      {(eventType || sourceType || epistemicStatus) && (
        <div className="flex flex-wrap items-center gap-2.5">
          {eventType && eventType in EVENT_TYPE_LABELS && (
            <span
              className="inline-flex items-center gap-2 rounded-full px-3.5 py-1.5 text-[13px] font-semibold"
              style={{
                backgroundColor: `${EVENT_TYPE_LABELS[eventType].color} / 0.08`,
                color: EVENT_TYPE_LABELS[eventType].color,
              }}
            >
              <span
                className="h-2 w-2 rounded-full"
                style={{ backgroundColor: EVENT_TYPE_LABELS[eventType].color }}
              />
              {EVENT_TYPE_LABELS[eventType].label}
            </span>
          )}
          {sourceType && sourceType in SOURCE_TYPE_LABELS && (
            <span className="inline-flex items-center gap-1.5 rounded-full border border-line/60 px-3 py-1 text-[12px] font-medium text-foreground/55">
              {SOURCE_TYPE_LABELS[sourceType]}
            </span>
          )}
          {epistemicStatus && epistemicStatus in EPISTEMIC_STATUS_LABELS && (
            <span className="inline-flex items-center gap-1.5 rounded-full border border-line/40 px-3.5 py-1.5 text-[13px] font-medium text-muted/50">
              <svg
                width="13"
                height="13"
                viewBox="0 0 16 16"
                fill="none"
                stroke="currentColor"
                strokeWidth="1.5"
                className="text-muted/30 shrink-0"
              >
                <circle cx="8" cy="8" r="6" />
                <path d="M8 5v3l2 2" strokeLinecap="round" />
              </svg>
              {EPISTEMIC_STATUS_LABELS[epistemicStatus]}
            </span>
          )}
        </div>
      )}

      {/* ---- 客观摘要：中立事实，常规阅读 ---- */}
      {objectiveSummary && (
        <div
          className="pl-4 py-3 rounded-r-lg"
          style={{
            borderLeft: "3px solid var(--line)",
            backgroundColor: "var(--surface)",
          }}
        >
          <div className="text-[11px] font-semibold text-muted/45 uppercase tracking-widest mb-2">
            客观摘要
          </div>
          <p className="text-[14px] leading-[1.85] text-foreground/72">
            {objectiveSummary}
          </p>
        </div>
      )}

      {/* ---- 逻辑链：因果推理，暖色 ---- */}
      {keyLogicFlow && keyLogicFlow.length > 0 && (
        <div
          className="pl-4 py-3 rounded-r-lg"
          style={{
            borderLeft: "3px solid var(--warm)",
            backgroundColor: "color-mix(in oklch, var(--warm) 4%, transparent)",
          }}
        >
          <div className="text-[11px] font-semibold text-warm/60 uppercase tracking-widest mb-3">
            逻辑链
          </div>
          <LogicFlow steps={keyLogicFlow} />
        </div>
      )}

      {/* ---- 实体识别：抽象提取，视觉最轻 ---- */}
      {entities && (
        <div
          className="pl-4 py-3 rounded-r-lg"
          style={{
            borderLeft: "3px solid var(--cool)",
            backgroundColor: "color-mix(in oklch, var(--cool) 3%, transparent)",
          }}
        >
          <div className="text-[11px] font-semibold text-cool/60 uppercase tracking-widest mb-3">
            实体识别
          </div>
          <EntityChips
            companies={entities.companies ?? []}
            technologies={entities.technologies ?? []}
            key_people={entities.key_people ?? []}
          />
        </div>
      )}
    </div>
  );
}
