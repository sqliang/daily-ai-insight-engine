// ============================================================================
// src/lib/data/specialized.ts — 专题分析数据加载
//
// 从 all_articles.json 中加载、过滤、聚合专题分析相关的文章数据。
// 供 GitHub/Product/Paper 专题看板页面消费。
// ============================================================================

import { readFile } from "node:fs/promises";
import { join } from "node:path";

// ---------------------------------------------------------------------------
// 类型定义
// ---------------------------------------------------------------------------

export interface GithubProjectEntry {
  articleId: string;
  title: string;
  url: string;
  projectName: string;
  projectUrl: string;
  primaryLanguage: string;
  licenseType: string;
  domain: string;
  crossTags: string[];
  aiDetail?: {
    primaryCategories: string[];
    agentSubcategory?: string[] | null;
    techTags: string[];
  } | null;
  // Stage 3 分析结果（可能尚未运行）
  techAssessment?: {
    techStackQuality: string;
    architectureHighlights: string;
    maturityScore?: number;
  };
  communityHealth?: {
    contributorActivity: string;
    starsTrend: string;
  };
  adoptionGuidance?: {
    recommendedFor: string[];
    cautionFor: string[];
    timeToProduction: string;
  };
}

// ---------------------------------------------------------------------------
// 数据加载
// ---------------------------------------------------------------------------

/**
 * 加载指定日期的 GitHub 专题文章。
 *
 * 从 all_articles.json 中筛选 source_dir == "github-trending" 的文章，
 * 提取 specialized_tags.github（Stage 2 标注）和 Stage 3 分析字段。
 *
 * 参数：
 *    date: 目标日期，格式 YYYY-MM-DD（当前未强制过滤，预留接口）
 *
 * 返回：
 *    GithubProjectEntry 数组，无数据时返回空数组
 */
export async function loadGithubArticles(
  _date: string,
): Promise<GithubProjectEntry[]> {
  const allArticlesPath = join(
    process.cwd(),
    "data/04_structured/all_articles.json",
  );

  try {
    const raw = await readFile(allArticlesPath, "utf8");
    const data = JSON.parse(raw);
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    const articles = (data.articles || []) as any[];

    return articles
      .filter((a) => a.source_dir === "github-trending")
      .map((a) => {
        const gh = a.specialized_tags?.github || {};

        return {
          articleId: a.id || "",
          title: a.title || "",
          url: a.url || "",
          projectName: gh.project_name || gh.projectName || "",
          projectUrl: gh.project_url || gh.projectUrl || "",
          primaryLanguage: gh.primary_language || gh.primaryLanguage || "",
          licenseType: gh.license_type || gh.licenseType || "",
          domain: gh.domain || "other",
          crossTags: gh.cross_tags || gh.crossTags || [],
          aiDetail: gh.ai_detail || gh.aiDetail || null,
          techAssessment: {
            techStackQuality: a.tech_assessment?.tech_stack_quality || "",
            architectureHighlights:
              a.tech_assessment?.architecture_highlights || "",
          },
          communityHealth: {
            contributorActivity: a.community_health?.contributor_activity || "",
            starsTrend: a.community_health?.stars_trend || "",
          },
          adoptionGuidance: {
            recommendedFor: a.adoption_guidance?.recommended_for || [],
            cautionFor: a.adoption_guidance?.caution_for || [],
            timeToProduction: a.adoption_guidance?.time_to_production || "",
          },
        };
      });
  } catch {
    return [];
  }
}

// ---------------------------------------------------------------------------
// 论文类型定义
// ---------------------------------------------------------------------------

export interface PaperEntry {
  articleId: string;
  title: string;
  url: string;
  // Stage 2 论文标注字段 (specialized_tags.paper)
  paperTitle: string;
  authors: string[];
  affiliations: string[];
  venue: string;
  codeUrl: string;
  datasetUrl: string;
  researchArea: string;
  methodType: string;
  // Stage 3 论文深度分析字段
  paperMetadata?: {
    title: string;
    authors: string[];
    affiliations: string[];
    venue: string;
    paperUrl: string;
    codeUrl: string;
    datasetUrl: string;
  };
  researchProblem?: {
    coreQuestion: string;
    motivation: string;
    significance: string;
    gapAddressed: string;
  };
  methodology?: {
    approachSummary: string;
    noveltyType: string;
    keyInnovations: string[];
    inspirationSources: string[];
    technicalDepth: string;
  };
  experimentalRigor?: {
    benchmarkCoverage: string;
    baselineComparison: string;
    ablationQuality: string;
    reproducibilityLevel: string;
    claimedImprovement: string;
  };
  limitationsAndHonesty?: {
    statedLimitations: string[];
    reviewerConcerns: string[];
    overclaimingAssessment: string;
    generalizationConcern: string;
  };
  industrialRelevance?: {
    applicableDomains: string[];
    computeRequirements: string;
    integrationReadiness: string;
    costEfficiencyAnalysis: string;
  };
  relatedWorkContext?: {
    closestPriorWorks: string[];
    advancementOverPrior: string;
    opensNewDirection: boolean;
    potentialFollowUps: string[];
  };
  // 标准 Stage 2/3 字段（回退展示）
  tldr: string;
  objectiveSummary: string;
}

// ---------------------------------------------------------------------------
// 论文数据加载
// ---------------------------------------------------------------------------

/**
 * 加载指定日期的论文专题文章。
 *
 * 从 all_articles.json 中筛选 source_dir == "arxiv-cs-ai" 的文章，
 * 提取 specialized_tags.paper（Stage 2 标注）和 Stage 3 论文分析字段。
 *
 * 参数：
 *    _date: 目标日期，格式 YYYY-MM-DD（当前未强制过滤，预留接口）
 *
 * 返回：
 *    PaperEntry 数组，无数据时返回空数组
 */
export async function loadPaperArticles(
  _date: string,
): Promise<PaperEntry[]> {
  const allArticlesPath = join(
    process.cwd(),
    "data/04_structured/all_articles.json",
  );

  try {
    const raw = await readFile(allArticlesPath, "utf8");
    const data = JSON.parse(raw);
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    const articles = (data.articles || []) as any[];

    return articles
      .filter((a) => a.source_dir === "arxiv-cs-ai")
      .map((a) => {
        // eslint-disable-next-line @typescript-eslint/no-explicit-any
        const paperTags: any = a.specialized_tags?.paper || {};

        // 论文分析字段（可能以 snake_case 存储在 frontmatter 中）
        // eslint-disable-next-line @typescript-eslint/no-explicit-any
        const pa: any = a.paper_assessment || {};

        return {
          articleId: a.id || "",
          title: a.title || "",
          url: a.url || "",
          // Stage 2 标注字段
          paperTitle: paperTags.paper_title || paperTags.paperTitle || a.title || "",
          authors: paperTags.authors || [],
          affiliations: paperTags.affiliations || [],
          venue: paperTags.venue || "",
          codeUrl: paperTags.code_url || paperTags.codeUrl || "",
          datasetUrl: paperTags.dataset_url || paperTags.datasetUrl || "",
          researchArea: paperTags.research_area || paperTags.researchArea || "unknown",
          methodType: paperTags.method_type || paperTags.methodType || "",
          // Stage 3 论文分析字段
          paperMetadata: pa.paper_metadata || pa.paperMetadata || undefined,
          researchProblem: pa.research_problem || pa.researchProblem || undefined,
          methodology: pa.methodology || undefined,
          experimentalRigor: pa.experimental_rigor || pa.experimentalRigor || undefined,
          limitationsAndHonesty: pa.limitations_and_honesty || pa.limitationsAndHonesty || undefined,
          industrialRelevance: pa.industrial_relevance || pa.industrialRelevance || undefined,
          relatedWorkContext: pa.related_work_context || pa.relatedWorkContext || undefined,
          // 标准字段
          tldr: a.tldr || "",
          objectiveSummary: a.objective_summary || a.objectiveSummary || "",
        };
      });
  } catch {
    return [];
  }
}

// ---------------------------------------------------------------------------
// 论文聚合统计
// ---------------------------------------------------------------------------

/**
 * 研究领域中英文标签映射。
 * 用于将 research_area 字段值映射为中文显示名称。
 */
export const RESEARCH_AREA_LABELS: Record<string, string> = {
  nlp: "NLP",
  cv: "CV",
  rl: "RL",
  multimodal: "多模态",
  generative: "生成式",
  agent: "Agent",
  reasoning: "推理",
  efficiency: "效率优化",
  security: "安全对齐",
  robotics: "机器人",
  systems: "系统",
  theory: "理论",
  applications: "应用",
  other: "其他",
  unknown: "其他",
};

/**
 * 研究领域完整列表（用于筛选标签展示排序）。
 */
export const RESEARCH_AREA_LIST = [
  "nlp", "cv", "rl", "multimodal", "generative", "agent",
  "reasoning", "efficiency", "security", "robotics", "systems",
  "theory", "applications", "other", "unknown",
];

/**
 * 计算研究领域分布统计。
 *
 * 按 researchArea 字段分组计数，返回 { 领域名: 数量 } 的分布字典。
 */
export function computeResearchAreaDistribution(
  papers: PaperEntry[],
): Record<string, number> {
  const dist: Record<string, number> = {};
  for (const p of papers) {
    const area = p.researchArea || "unknown";
    dist[area] = (dist[area] || 0) + 1;
  }
  return dist;
}

// ---------------------------------------------------------------------------
// 聚合统计
// ---------------------------------------------------------------------------

/**
 * 计算领域分布统计。
 *
 * 按 domain 字段分组计数，返回 { 领域名: 数量 } 的分布字典。
 */
export function computeDomainDistribution(
  projects: GithubProjectEntry[],
): Record<string, number> {
  const dist: Record<string, number> = {};
  for (const p of projects) {
    dist[p.domain] = (dist[p.domain] || 0) + 1;
  }
  return dist;
}

/**
 * 计算 AI 子领域分布统计。
 *
 * 遍历每个项目 aiDetail.primaryCategories，按类别分组计数。
 * 无 aiDetail 或 primaryCategories 为空的项目被跳过。
 */
export function computeAiCategoryDistribution(
  projects: GithubProjectEntry[],
): Record<string, number> {
  const dist: Record<string, number> = {};
  for (const p of projects) {
    if (p.aiDetail?.primaryCategories) {
      for (const cat of p.aiDetail.primaryCategories) {
        dist[cat] = (dist[cat] || 0) + 1;
      }
    }
  }
  return dist;
}
