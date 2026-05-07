import {
  dailyReportSchema,
  rawArticleSchema,
  structuredInsightSchema,
  type DailyReport,
  type RawArticle,
  type StructuredInsight,
} from "@/lib/agent/schema";
import { heuristicExtract, heuristicSynthesize } from "@/lib/agent/heuristics";
import { buildExtractorPrompt, buildSynthesizerPrompt } from "@/lib/agent/prompts";

// ============================================================================
// index.ts — AIInsightEngine 主类
//
// 本文件是 AI 引擎的唯一对外入口。它在两种模式之间切换：
//
//   Mode A: 确定性 Mock 模式（默认）
//     当 AI_ENGINE_USE_CLAUDE !== "true" 时启用。
//     使用 heuristics.ts 中的纯规则方法，无需 API Key 即可复现完整报告。
//     适用于面试评审、CI 验证和本地开发。
//
//   Mode B: Claude Agent 模式
//     当 AI_ENGINE_USE_CLAUDE=true 时启用。
//     使用 @anthropic-ai/claude-agent-sdk 调用 Claude 进行 Map/Reduce。
//     Claude Agent SDK 的 query() 函数以 AsyncIterable 形式返回流式结果，
//     本模块将其聚合为完整字符串后解析 JSON。
//
// 双模式架构的关键约束：
//   两种模式必须遵循相同的输入/输出 Schema（schema.ts），
//   确保切换模式时看板页面和验证脚本无需任何修改。
// ============================================================================

type ClaudeQuery = (options: {
  prompt: string;
  options?: {
    systemPrompt?: string;
    maxTurns?: number;
  };
}) => AsyncIterable<{ type?: string; message?: { content?: Array<{ type?: string; text?: string }> } }>;

export class AIInsightEngine {
  private readonly useClaude: boolean;

  constructor(options?: { useClaude?: boolean }) {
    // 默认使用确定性 mock 模式，保障可复现性。
    // 面试官 clone 仓库后无需 API Key 即可生成示例报告，
    // 而真实 Claude 集成只需一个环境变量即可启用。
    this.useClaude = options?.useClaude ?? process.env.AI_ENGINE_USE_CLAUDE === "true";
  }

  // Map 阶段：单篇文章 → 结构化洞察
  // 逐篇独立处理，单篇失败不影响其他文章的抽取
  async extractArticle(article: RawArticle): Promise<StructuredInsight> {
    const parsedArticle = rawArticleSchema.parse(article);
    // 设计原则：每篇文章独立 Map，避免"将所有原始数据一次性丢给 LLM"的模式。
    // 这既是性能考量（token 上限），也是为了降低幻觉和交叉污染。
    if (!this.useClaude) return heuristicExtract(parsedArticle);

    const raw = await this.runClaude(buildExtractorPrompt(parsedArticle));
    return structuredInsightSchema.parse(JSON.parse(raw));
  }

  // Reduce 阶段：结构化洞察集合 → 日报
  // 只接收已校验的 StructuredInsight 集合，不接触原始语料
  async synthesizeReport(insights: StructuredInsight[]): Promise<DailyReport> {
    const parsedInsights = insights.map((item) => structuredInsightSchema.parse(item));
    // Reduce 阶段只接收紧凑的、已验证的结构化特征，而非原始文章全文。
    // 这确保 LLM 的上下文管理可控，且报告质量不受单篇文章噪声影响。
    if (!this.useClaude) return dailyReportSchema.parse(heuristicSynthesize(parsedInsights));

    const raw = await this.runClaude(buildSynthesizerPrompt(parsedInsights));
    return dailyReportSchema.parse(JSON.parse(raw));
  }

  // Claude Agent SDK 调用封装
  // - 动态 import 避免 Agent SDK 被打包到客户端 bundle
  // - 流式结果聚合为完整字符串
  // - JSON fence 剥离：处理 LLM 常见的 ```json ... ``` 包裹
  private async runClaude(prompt: string): Promise<string> {
    // 动态导入确保看板页面在未使用 Claude 时不会引入 Agent SDK，
    // 避免客户端打包错误和包体积膨胀。
    const mod = (await import("@anthropic-ai/claude-agent-sdk")) as { query?: ClaudeQuery };
    if (!mod.query) {
      throw new Error("Claude SDK query function is unavailable.");
    }

    let text = "";
    for await (const message of mod.query({ prompt, options: { maxTurns: 1 } })) {
      const content = message.message?.content ?? [];
      for (const block of content) {
        if (block.type === "text" && block.text) text += block.text;
      }
    }
    return stripJsonFence(text);
  }
}

// 去除 LLM 输出中常见的 Markdown 代码块包裹，
// 确保 JSON.parse 能成功解析
function stripJsonFence(input: string): string {
  return input
    .trim()
    .replace(/^```json\s*/i, "")
    .replace(/^```\s*/i, "")
    .replace(/\s*```$/i, "")
    .trim();
}
