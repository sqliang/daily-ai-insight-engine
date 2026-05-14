import {
  EVENT_TYPE_LABELS,
  EPISTEMIC_STATUS_LABELS,
} from "@/lib/data/status";
import { EntityChips } from "./EntityChips";
import { LogicFlow } from "./LogicFlow";

type ArticleCardExtractionProps = {
  tldr?: string;
  objectiveSummary?: string;
  eventType?: string;
  entities?: {
    companies: string[];
    technologies: string[];
    key_people: string[];
  };
  keyLogicFlow?: string[];
  epistemicStatus?: string;
};

export function ArticleCardExtraction({
  tldr,
  objectiveSummary,
  eventType,
  entities,
  keyLogicFlow,
  epistemicStatus,
}: ArticleCardExtractionProps) {
  const hasExtraction = tldr || objectiveSummary || eventType || entities;
  if (!hasExtraction) return null;

  return (
    <div className="space-y-5">
      {tldr && (
        <div
          className="pl-4 py-2 rounded-r-lg"
          style={{
            borderLeft: "3px solid var(--accent) / 0.5",
            backgroundColor: "var(--accent) / 0.02",
          }}
        >
          <div className="text-[11px] font-bold text-accent/50 uppercase tracking-widest mb-1">
            TL;DR
          </div>
          <p className="text-[16px] font-semibold leading-[1.6] text-foreground/85">
            {tldr}
          </p>
        </div>
      )}

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

      {objectiveSummary && (
        <div className="p-4 rounded-xl" style={{ backgroundColor: "var(--surface)" }}>
          <div className="text-[12px] font-bold text-muted/40 uppercase tracking-widest mb-2">
            客观摘要
          </div>
          <p className="text-[14px] leading-[1.85] text-foreground/65">
            {objectiveSummary}
          </p>
        </div>
      )}

      {entities && (
        <div className="p-4 rounded-xl" style={{ backgroundColor: "var(--surface)" }}>
          <div className="text-[12px] font-bold text-muted/40 uppercase tracking-widest mb-3">
            实体识别
          </div>
          <EntityChips
            companies={entities.companies ?? []}
            technologies={entities.technologies ?? []}
            key_people={entities.key_people ?? []}
          />
        </div>
      )}

      {keyLogicFlow && keyLogicFlow.length > 0 && (
        <div className="p-4 rounded-xl" style={{ backgroundColor: "var(--surface)" }}>
          <div className="text-[12px] font-bold text-muted/40 uppercase tracking-widest mb-3">
            逻辑链
          </div>
          <LogicFlow steps={keyLogicFlow} />
        </div>
      )}
    </div>
  );
}
