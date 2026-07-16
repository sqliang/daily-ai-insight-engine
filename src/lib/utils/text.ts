// ============================================================================
// text.ts — 前端文本展示格式化工具
//
// 提供不改变原始数据的轻量展示兜底。专题洞察等 LLM 生成文本偶发缺少句末
// 标点时，页面通过这里补齐，避免卡片展示出“半句话”的观感。
// ============================================================================

const SENTENCE_ENDING_RE = /[。！？.!?」』”’）)\]]$/;

// ---------------------------------------------------------------------------
// 句末标点兜底
// ---------------------------------------------------------------------------

/**
 * 确保展示文本以句末标点结束。
 *
 * 参数：
 *    value: 待展示的文本
 *
 * 返回：
 *    去除首尾空白并补齐句末标点后的文本。仅用于 UI 展示，不应写回数据源。
 */
export function ensureSentencePunctuation(value: string): string {
  const trimmed = value.trim();
  if (!trimmed) return "";
  return SENTENCE_ENDING_RE.test(trimmed) ? trimmed : `${trimmed}。`;
}

/**
 * 批量确保展示文本以句末标点结束。
 *
 * 参数：
 *    values: 待展示的文本数组
 *
 * 返回：
 *    过滤空文本并补齐句末标点后的数组。
 */
export function ensureSentencePunctuationList(values: string[]): string[] {
  return values
    .map((value) => ensureSentencePunctuation(value))
    .filter(Boolean);
}
