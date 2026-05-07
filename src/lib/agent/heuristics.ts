import {
  type DailyReport,
  type EventType,
  type RawArticle,
  type Sentiment,
  type StructuredInsight,
} from "@/lib/agent/schema";
import { eventTypeLabels } from "@/lib/report/labels";

// ============================================================================
// heuristics.ts — 确定性启发式抽取 & 报告合成
//
// 本文件提供与 AIInsightEngine 中 Claude 路径等效的"确定性 mock 模式"实现。
// 当未设置 AI_ENGINE_USE_CLAUDE=true 时，流水线使用本模块的纯规则方法完成
// Map（单篇抽取）和 Reduce（报告合成），确保：
//   1. 无需 API Key 即可复现完整报告。
//   2. 输出完全确定，便于面试评审和 CI 验证。
//   3. 逻辑透明，可作为 Claude 抽取结果的对比基线。
//
// 核心流程：
//   heuristicExtract()      → Map 阶段：RawArticle → StructuredInsight
//   heuristicSynthesize()   → Reduce 阶段：StructuredInsight[] → DailyReport
// ============================================================================

// 已知 AI 公司名称词典，用于实体识别（中英双语覆盖）
const companyNames = [
  "OpenAI",
  "Google",
  "DeepMind",
  "Anthropic",
  "Microsoft",
  "NVIDIA",
  "Meta",
  "Apple",
  "Amazon",
  "Hugging Face",
  "Mistral",
  "xAI",
  "百度",
  "阿里",
  "腾讯",
  "字节跳动",
  "智谱",
  "月之暗面",
  "MiniMax",
  "阶跃星辰",
];

// 已知 AI 技术术语词典，覆盖主流技术方向
const technologyNames = [
  "LLM",
  "large language model",
  "大模型",
  "agent",
  "Agent",
  "multimodal",
  "多模态",
  "reasoning",
  "推理",
  "RAG",
  "GPU",
  "inference",
  "推理成本",
  "AI coding",
  "代码生成",
  "robotics",
  "具身智能",
  "open source",
  "开源",
  "safety",
  "安全",
];

// 事件类型信号匹配表：按优先级排序的正则对，第一个命中即为事件类型
// 每个事件类型都配有多语言信号词，确保中英文信源都被覆盖
const eventSignals: Array<[EventType, RegExp]> = [
  ["policy_regulation", /policy|regulat|监管|法规|法案|合规|安全治理/i],
  ["funding_market", /funding|raised|valuation|acquisition|IPO|投资|融资|估值|资本/i],
  ["research_breakthrough", /paper|arxiv|research|benchmark|研究|论文|突破|评测/i],
  ["open_source", /open source|github|release|开源|模型权重/i],
  ["safety_risk", /risk|lawsuit|copyright|安全|风险|版权|诉讼|滥用/i],
  ["industry_adoption", /enterprise|customer|adoption|deploy|落地|企业|客户|行业/i],
  ["product_launch", /launch|product|app|assistant|发布|上线|产品|工具/i],
  ["model_release", /model|GPT|Claude|Gemini|Llama|模型/i],
];

// ============================================================================
// Map 阶段：单篇文章 → 结构化洞察
// ============================================================================

export function heuristicExtract(article: RawArticle): StructuredInsight {
  const text = `${article.title} ${article.summary} ${article.content}`;
  const eventType = detectEventType(text);
  const entities = {
    companies: findMatches(text, companyNames),
    technologies: findMatches(text, technologyNames),
    people: findPeople(text),
    products: findProducts(text),
    regions: findRegions(text),
  };
  const sentiment = detectSentiment(text, eventType);
  const topicTags = buildTopicTags(eventType, entities.technologies, article.language);
  const impactScore = scoreImpact(text, entities.companies.length, eventType);
  const urgencyScore = scoreUrgency(text, eventType);

  return {
    articleId: article.id,
    title: article.title,
    source: article.source,
    url: article.url,
    publishedAt: article.publishedAt,
    eventType,
    topicTags,
    entities,
    sentiment,
    impactScore,
    urgencyScore,
    keyFacts: buildKeyFacts(article, eventType, entities.companies),
    analyticalSummary: buildAnalyticalSummary(article, eventType, impactScore),
    risks: buildRisks(eventType, entities.companies),
    opportunities: buildOpportunities(eventType, entities.technologies),
    confidence: 0.72,   // 启发式方法的固定置信度：规则准确但不含语义理解
  };
}

// ============================================================================
// Reduce 阶段：结构化洞察集合 → 日报
// ============================================================================

export function heuristicSynthesize(insights: StructuredInsight[]): DailyReport {
  const sorted = [...insights].sort((a, b) => b.impactScore - a.impactScore);
  const top = sorted.slice(0, 5);
  const date = new Date().toISOString().slice(0, 10);
  const sources = [...new Set(insights.map((item) => item.source))].sort();
  const languages = [...new Set(insights.map((item) => inferLanguage(item.title)))];

  return {
    date,
    generatedAt: new Date().toISOString(),
    reportTitle: `${date} AI 舆情分析日报`,
    executiveSummary: `今日样本覆盖 ${insights.length} 条 AI 相关信息，热点集中在${summarizeEventTypes(insights)}。结构化信号显示，大模型产品化、企业落地、监管与开源生态仍在同时推进，行业关注点正从单点模型能力转向成本、可靠性和可控部署。`,
    dataSourceSummary: {
      totalArticles: insights.length,
      sources,
      languages,
      selectionRationale:
        "样本混合科技媒体、官方渠道、研究社区、开发者社区与中文科技媒体，兼顾商业动向、技术发布、社区反馈和本土产业语境。",
    },
    topEvents: top.slice(0, 5).map((item) => ({
      title: item.title,
      articleIds: [item.articleId],
      eventType: item.eventType,
      impactScore: item.impactScore,
      whyItMatters: `${eventTypeLabels[item.eventType]}信号强，影响分 ${item.impactScore}/10。该事件可能改变短期产品路线、开发者采用或监管关注优先级。`,
      evidence: item.keyFacts.slice(0, 3),
    })),
    deepDives: top.slice(0, 3).map((item) => ({
      title: item.title,
      background: item.analyticalSummary,
      impact: `从结构化字段看，该事件同时触发 ${item.topicTags.join("、")} 等标签，影响力和紧迫度分别为 ${item.impactScore}/10、${item.urgencyScore}/10。`,
      watchNext: `后续重点观察 ${[...item.entities.companies, ...item.entities.technologies].slice(0, 3).join("、") || "相关生态"} 的产品迭代、成本变化和外部反馈。`,
    })),
    trendInsights: [
      {
        dimension: "technology",
        judgment: "模型竞争继续从参数规模转向推理能力、多模态体验和工程可用性。",
        supportingSignals: pickSignals(insights, ["model_release", "research_breakthrough", "open_source"]),
      },
      {
        dimension: "application",
        judgment: "企业采用更关注稳定部署、工作流集成和可衡量 ROI，单纯演示型产品吸引力下降。",
        supportingSignals: pickSignals(insights, ["industry_adoption", "product_launch"]),
      },
      {
        dimension: "policy",
        judgment: "监管和安全议题逐渐成为发布节奏的一部分，版权、数据来源和模型风险需要前置处理。",
        supportingSignals: pickSignals(insights, ["policy_regulation", "safety_risk"]),
      },
      {
        dimension: "capital",
        judgment: "资本仍追逐基础设施和高频应用入口，但估值叙事会更依赖真实使用量与毛利改善。",
        supportingSignals: pickSignals(insights, ["funding_market", "industry_adoption"]),
      },
    ],
    riskSignals: buildReportSignals(insights, "risk"),
    opportunitySignals: buildReportSignals(insights, "opportunity"),
    visualizationData: buildVisualizationData(insights),
  };
}

// ============================================================================
// 内部辅助函数
// ============================================================================

// 事件类型检测：遍历 eventSignals 匹配表，返回第一个命中的类型；
// 若无匹配则默认归为 industry_adoption（兜底策略）
function detectEventType(text: string): EventType {
  return eventSignals.find(([, pattern]) => pattern.test(text))?.[0] ?? "industry_adoption";
}

// 情感检测：负面关键词优先 → 混合信号 → 事件类型推断 → 默认中性
function detectSentiment(text: string, eventType: EventType): Sentiment {
  if (/lawsuit|risk|concern|ban|breach|安全|风险|诉讼|争议|下架|裁员/i.test(text)) return "negative";
  if (/mixed|debate|scrutiny|监管|争议|但|however/i.test(text)) return "mixed";
  if (["product_launch", "model_release", "funding_market", "research_breakthrough"].includes(eventType)) {
    return "positive";
  }
  return "neutral";
}

// 影响力评分：基数 5 + 实体数量加成 + 重点公司/事件类型加权，上限 10
function scoreImpact(text: string, entityCount: number, eventType: EventType): number {
  let score = 5 + Math.min(2, entityCount);
  if (/OpenAI|Google|Anthropic|Microsoft|NVIDIA|Meta|Apple|监管|policy|funding|融资/i.test(text)) score += 2;
  if (["policy_regulation", "funding_market", "model_release"].includes(eventType)) score += 1;
  return Math.min(10, score);
}

// 紧迫度评分：政策/安全/产品类事件默认偏高，含即时性关键词再加权
function scoreUrgency(text: string, eventType: EventType): number {
  let score = ["policy_regulation", "safety_risk", "product_launch"].includes(eventType) ? 7 : 5;
  if (/today|now|urgent|immediately|今日|最新|刚刚|宣布/i.test(text)) score += 1;
  return Math.min(10, score);
}

// 基于词典的实体匹配：正则全文中搜索，去重后最多返回 8 个
function findMatches(text: string, dictionary: string[]): string[] {
  const normalized = new Set<string>();
  for (const item of dictionary) {
    if (new RegExp(escapeRegExp(item), "i").test(text)) normalized.add(item);
  }
  return [...normalized].slice(0, 8);
}

function findPeople(text: string): string[] {
  return findMatches(text, ["Sam Altman", "Dario Amodei", "Sundar Pichai", "Jensen Huang", "Yann LeCun", "李彦宏", "周鸿祎"]);
}

function findProducts(text: string): string[] {
  return findMatches(text, ["ChatGPT", "Claude", "Gemini", "Copilot", "Llama", "Sora", "Grok", "DeepSeek", "Kimi"]);
}

function findRegions(text: string): string[] {
  return findMatches(text, ["US", "EU", "China", "中国", "Europe", "美国", "欧盟", "Asia"]);
}

// 话题标签 = 事件类型中文名 + 语言标识 + 技术实体（最多 8 个）
function buildTopicTags(eventType: EventType, technologies: string[], language: RawArticle["language"]): string[] {
  const base = [eventTypeLabels[eventType], language === "zh" ? "中文信源" : "英文信源"];
  return [...new Set([...base, ...technologies.slice(0, 4)])].slice(0, 8);
}

function buildKeyFacts(article: RawArticle, eventType: EventType, companies: string[]): string[] {
  return [
    `${article.source} 报道了 ${eventTypeLabels[eventType]} 相关事件。`,
    companies.length > 0 ? `涉及主体包括 ${companies.slice(0, 4).join("、")}。` : "事件与 AI 产业链或开发者生态相关。",
    article.summary,
  ].slice(0, 5);
}

function buildAnalyticalSummary(article: RawArticle, eventType: EventType, impactScore: number): string {
  return `该信息属于${eventTypeLabels[eventType]}类别，核心事实是：${article.summary} 其价值不只在单条新闻本身，而在于它提供了可聚合的产业信号，当前影响力评分为 ${impactScore}/10。`;
}

// 风险生成：根据事件类型返回针对性的风险描述
function buildRisks(eventType: EventType, companies: string[]): string[] {
  if (eventType === "policy_regulation") return ["监管要求可能提高模型发布和数据合规成本。"];
  if (eventType === "safety_risk") return ["负面舆情可能扩大到品牌信任、版权或安全治理层面。"];
  if (eventType === "funding_market") return ["估值预期可能领先商业化兑现，存在资本回调压力。"];
  return companies.length > 0 ? [`${companies[0]} 等主体的快速迭代可能加剧同类产品竞争。`] : [];
}

// 机会生成：根据事件类型返回针对性的机会描述
function buildOpportunities(eventType: EventType, technologies: string[]): string[] {
  if (eventType === "open_source") return ["开源模型和工具链降低开发者试验成本。"];
  if (eventType === "industry_adoption") return ["垂直行业场景进入可复制部署阶段。"];
  if (eventType === "model_release") return ["新模型能力可带动应用层体验升级。"];
  return technologies.length > 0 ? [`${technologies[0]} 相关能力存在产品化机会。`] : [];
}

// 统计事件类型分布，返回 Top 3 类型的中文名称
function summarizeEventTypes(insights: StructuredInsight[]): string {
  const counts = new Map<EventType, number>();
  for (const item of insights) counts.set(item.eventType, (counts.get(item.eventType) ?? 0) + 1);
  return [...counts.entries()]
    .sort((a, b) => b[1] - a[1])
    .slice(0, 3)
    .map(([type]) => eventTypeLabels[type])
    .join("、");
}

// 语言推断：标题含中文字符 → zh，否则 en
function inferLanguage(title: string): "zh" | "en" | "mixed" {
  return /[一-龥]/.test(title) ? "zh" : "en";
}

// 从洞察列表中筛选指定类型的事件标题，用于填充趋势判断的支撑信号
function pickSignals(insights: StructuredInsight[], types: EventType[]): string[] {
  return insights
    .filter((item) => types.includes(item.eventType))
    .sort((a, b) => b.impactScore - a.impactScore)
    .slice(0, 3)
    .map((item) => item.title);
}

// 构建风险和机会信号列表：从每条洞察的 risks/opportunities 字段中展开，
// 根据影响力映射严重程度，取前 5 条
function buildReportSignals(insights: StructuredInsight[], kind: "risk" | "opportunity") {
  const values = insights.flatMap((item) =>
    (kind === "risk" ? item.risks : item.opportunities).map((signal) => ({
      signal,
      severity: item.impactScore >= 8 ? ("high" as const) : item.impactScore >= 6 ? ("medium" as const) : ("low" as const),
      rationale: `${item.title}，影响分 ${item.impactScore}/10。`,
    })),
  );
  return values.slice(0, 5);
}

// 预计算所有可视化数据：使前端页面无需再做聚合计算
function buildVisualizationData(insights: StructuredInsight[]): DailyReport["visualizationData"] {
  return {
    eventTypeDistribution: countBy(insights.map((item) => item.eventType)).map(([label, count]) => ({ label, count })),
    sentimentDistribution: countBy(insights.map((item) => item.sentiment)).map(([label, count]) => ({ label, count })),
    impactRanking: [...insights]
      .sort((a, b) => b.impactScore - a.impactScore)
      .slice(0, 8)
      .map((item) => ({ articleId: item.articleId, title: item.title, score: item.impactScore })),
    entityFrequency: buildEntityFrequency(insights),
  };
}

// 通用计数工具：将字符串数组转为 [值, 频次] 的排序列表
function countBy<T extends string>(items: T[]): Array<[T, number]> {
  const counts = new Map<T, number>();
  for (const item of items) counts.set(item, (counts.get(item) ?? 0) + 1);
  return [...counts.entries()].sort((a, b) => b[1] - a[1]);
}

// 实体频次统计：展开所有洞察中的实体 → 按 (类型:名称) 去重计数 → 按计数降序取前 16
function buildEntityFrequency(insights: StructuredInsight[]): DailyReport["visualizationData"]["entityFrequency"] {
  const pairs = insights.flatMap((item) => [
    ...item.entities.companies.map((entity) => ({ entity, type: "company" as const })),
    ...item.entities.technologies.map((entity) => ({ entity, type: "technology" as const })),
    ...item.entities.people.map((entity) => ({ entity, type: "person" as const })),
    ...item.entities.products.map((entity) => ({ entity, type: "product" as const })),
    ...item.entities.regions.map((entity) => ({ entity, type: "region" as const })),
  ]);
  const counts = new Map<string, { entity: string; type: (typeof pairs)[number]["type"]; count: number }>();
  for (const pair of pairs) {
    const key = `${pair.type}:${pair.entity}`;
    counts.set(key, { ...pair, count: (counts.get(key)?.count ?? 0) + 1 });
  }
  return [...counts.values()].sort((a, b) => b.count - a.count).slice(0, 16);
}

// 转义正则特殊字符，防止词典词条中的特殊字符破坏正则匹配
function escapeRegExp(value: string): string {
  return value.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}
