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
    <div
      className="border-t pt-5 mt-3"
      style={{ borderColor: "var(--line) / 0.4" }}
    >
      {/* TL;DR with accent left line */}
      {tldr && (
        <div
          className="pl-3 mb-3"
          style={{ borderLeft: "2px solid var(--accent) / 0.3" }}
        >
          <p className="text-[15px] font-semibold leading-snug text-foreground/85">
            {tldr}
          </p>
        </div>
      )}

      {/* Badges row */}
      <div className="flex flex-wrap items-center gap-2 mb-3">
        {eventType && eventType in EVENT_TYPE_LABELS && (
          <span
            className="inline-flex items-center gap-1.5 rounded-full px-3 py-1 text-[12px] font-medium"
            style={{
              backgroundColor: `${EVENT_TYPE_LABELS[eventType].color} / 0.08`,
              color: EVENT_TYPE_LABELS[eventType].color,
            }}
          >
            <span
              className="h-1.5 w-1.5 rounded-full"
              style={{ backgroundColor: EVENT_TYPE_LABELS[eventType].color }}
            />
            {EVENT_TYPE_LABELS[eventType].label}
          </span>
        )}
        {epistemicStatus && epistemicStatus in EPISTEMIC_STATUS_LABELS && (
          <span className="inline-flex items-center rounded-full border border-line/40 px-3 py-1 text-[12px] font-medium text-muted/45">
            {EPISTEMIC_STATUS_LABELS[epistemicStatus]}
          </span>
        )}
      </div>

      {/* Objective summary */}
      {objectiveSummary && (
        <p className="text-[13px] leading-[1.8] text-foreground/60 mb-4 line-clamp-3">
          {objectiveSummary}
        </p>
      )}

      {/* Entity chips */}
      {entities && (
        <div className="mb-4">
          <EntityChips
            companies={entities.companies ?? []}
            technologies={entities.technologies ?? []}
            key_people={entities.key_people ?? []}
          />
        </div>
      )}

      {/* Key logic flow */}
      {keyLogicFlow && keyLogicFlow.length > 0 && (
        <LogicFlow steps={keyLogicFlow} />
      )}
    </div>
  );
}
