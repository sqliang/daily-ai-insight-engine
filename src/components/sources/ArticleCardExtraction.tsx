// ============================================================================
// ArticleCardExtraction.tsx — 信息提取结果展示
//
// 以卡片化信息组渲染 TL;DR、事件类型、来源类型、客观摘要、逻辑链和实体识别。
// 被文章详情页消费，既保持内容完整，也贴合站点现有情报看板视觉。
// ============================================================================

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
 * 采用轻量卡片建立信息层级，保留完整文本内容。
 * 信息按“结论、事实、推理、实体”的阅读顺序连续展开。
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
    <div className="space-y-4">
      {tldr && (
        <div className="rounded-xl border border-accent/20 bg-accent/6 p-4">
          <div className="text-[12px] font-semibold text-accent">
            TL;DR
          </div>
          <p className="mt-2 text-[17px] font-semibold leading-8 text-foreground">
            {tldr}
          </p>
        </div>
      )}

      {(eventType || sourceType || epistemicStatus) && (
        <div className="flex flex-wrap items-center gap-2 rounded-xl border border-line/55 bg-background/55 p-3">
          {eventType && eventType in EVENT_TYPE_LABELS && (
            <span
              className="inline-flex items-center gap-2 rounded-full px-3 py-1 text-[13px] font-semibold"
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
            <span className="rounded-full bg-warm/10 px-3 py-1 text-[13px] font-semibold text-foreground/75">
              {SOURCE_TYPE_LABELS[sourceType]}
            </span>
          )}
          {epistemicStatus && epistemicStatus in EPISTEMIC_STATUS_LABELS && (
            <span className="rounded-full bg-cool/10 px-3 py-1 text-[13px] font-semibold text-foreground/75">
              {EPISTEMIC_STATUS_LABELS[epistemicStatus]}
            </span>
          )}
        </div>
      )}

      {objectiveSummary && (
        <div className="rounded-xl border border-line/55 bg-background/55 p-4">
          <div className="text-[12px] font-semibold text-muted/80">
            客观摘要
          </div>
          <p className="mt-2 text-[16px] leading-8 text-foreground/80">
            {objectiveSummary}
          </p>
        </div>
      )}

      {keyLogicFlow && keyLogicFlow.length > 0 && (
        <div className="rounded-xl border border-warm/20 bg-warm/6 p-4">
          <div className="mb-4 text-[12px] font-semibold text-warm">
            逻辑链
          </div>
          <LogicFlow steps={keyLogicFlow} />
        </div>
      )}

      {entities && (
        <div className="rounded-xl border border-cool/20 bg-cool/6 p-4">
          <div className="mb-3 text-[12px] font-semibold text-cool">
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
