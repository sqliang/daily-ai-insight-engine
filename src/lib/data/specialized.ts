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
