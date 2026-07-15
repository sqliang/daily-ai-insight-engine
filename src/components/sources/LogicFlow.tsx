// ============================================================================
// LogicFlow.tsx — 逻辑链步骤展示
//
// 以编号步骤列表完整呈现因果推理过程。
// 由文章详情页消费，保留全部步骤以便读者核对分析依据。
// 被 ArticleCardExtraction 的逻辑链区块消费。
// ============================================================================

type LogicFlowProps = {
  steps: string[];
};

/**
 * 逻辑链步骤展示组件，以编号步骤列表呈现因果推理过程。
 *
 * 用于 ArticleCardExtraction 的逻辑链区块。
 *
 * 详情页承担完整阅读职责，因此不折叠任何步骤，也不需要客户端状态。
 */
export function LogicFlow({ steps }: LogicFlowProps) {
  if (steps.length === 0) return null;

  return (
    <ol className="space-y-3">
      {steps.map((step, i) => {
        const isLastTwo = i >= steps.length - 2;
        return (
          <li
            key={i}
            className="flex items-start gap-3 rounded-lg border border-line/45 bg-panel/70 p-3"
          >
            <span
              className="mt-0.5 flex h-6 w-6 shrink-0 items-center justify-center rounded-full text-[11px] font-bold"
              style={{
                backgroundColor: isLastTwo ? "var(--accent-glow)" : "var(--surface)",
                color: isLastTwo ? "var(--accent)" : "var(--muted)",
                border: isLastTwo ? "none" : "1.5px solid var(--line)",
              }}
            >
              {i + 1}
            </span>
            <span className={`text-[15px] leading-7 ${isLastTwo ? "font-medium text-foreground/90" : "text-foreground/75"}`}>
              {step}
            </span>
          </li>
        );
      })}
    </ol>
  );
}
