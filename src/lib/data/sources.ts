import { readFile, readdir } from "node:fs/promises";
import { join } from "node:path";
import { parse as parseYaml } from "yaml";
import { z } from "zod";
import type { TierMeta } from "@/lib/data/tiers";
import {
  type ProcessingStatus,
  type StructuredArticle,
  structuredArticleSchema,
  determineProcessingStatus,
} from "@/lib/data/status";

// ============================================================================
// Zod schemas for manifest JSON validation
// ============================================================================

const manifestArticleSchema = z.object({
  url: z.string(),
  title: z.string(),
  published: z.string().optional().default(""),
  summary: z.string(),
  author: z.string().optional().default(""),
  id: z.string().optional(),
});

const manifestSchema = z.object({
  source: z.string(),
  source_type: z.enum([
    "academic_paper",
    "tech_blog",
    "news_media",
    "community_discussion",
    "newsletter_rss",
  ]),
  tier: z.enum(["A", "B", "C"]),
  generated_at: z.string(),
  date: z.string(),
  articles: z.array(manifestArticleSchema),
});

// ============================================================================
// Type definitions
// ============================================================================

interface SourceConfig {
  name: string;
  type: string;
  tier: "A" | "B" | "C";
  enabled: boolean;
  display_name?: string;
  description: string;
  display_description?: string;
  url: string;
  language: string;
  fetch_strategy: string;
  filter: { keywords: string[]; max_age_hours: number };
  truncation: { mode: string; limit?: number };
  target_dir?: string;
}

export interface SourceStatus {
  name: string;
  type: string;
  tier: "A" | "B" | "C";
  enabled: boolean;
  display_name: string;
  description: string;
  display_description: string;
  url: string;
  language: string;
  fetch_strategy: string;
  keywords: string[];
  max_age_hours: number;
  truncation: { mode: string; limit?: number };
  target_dir?: string;
  manifestFound: boolean;
  articleCount: number;
  articles: Array<{
    url: string;
    title: string;
    published: string;
    summary: string;
    author: string;
    id?: string;
  }>;
  manifestDate: string | null;
  manifestGeneratedAt: string | null;
}

export interface EnrichedArticle {
  url: string;
  title: string;
  published: string;
  summary: string;
  author: string;
  id?: string;
  enriched: StructuredArticle | null;
  status: ProcessingStatus;
}

export interface DateRange {
  from?: string;
  to?: string;
}

export interface EnrichedSourceDetail {
  name: string;
  type: string;
  tier: "A" | "B" | "C";
  enabled: boolean;
  display_name: string;
  description: string;
  display_description: string;
  url: string;
  language: string;
  fetch_strategy: string;
  keywords: string[];
  max_age_hours: number;
  truncation: { mode: string; limit?: number };
  target_dir?: string;
  manifestFound: boolean;
  articleCount: number;
  articles: EnrichedArticle[];
  manifestDate: string | null;
  manifestGeneratedAt: string | null;
  stageCounts: Record<ProcessingStatus, number>;
  availableDates: string[];
  dateRange: DateRange | null;
}

// ============================================================================
// Data fetching
// ============================================================================

const MANIFEST_DIR = join(process.cwd(), "data/00_manifest");
const CONFIG_PATH = join(process.cwd(), "pipeline/config.yaml");
const TIERS_PATH = join(process.cwd(), "pipeline/tiers.yaml");

async function getSourceConfigs(): Promise<SourceConfig[]> {
  const raw = await readFile(CONFIG_PATH, "utf8");
  const config = parseYaml(raw);
  const sources: unknown[] = config?.sources ?? [];
  return sources
    .filter(
      (s): s is SourceConfig =>
        typeof s === "object" &&
        s !== null &&
        "enabled" in s &&
        (s as SourceConfig).enabled === true,
    )
    .map((s) => s as SourceConfig);
}

async function loadManifests(): Promise<Map<string, z.infer<typeof manifestSchema>>> {
  const manifests = new Map<string, z.infer<typeof manifestSchema>>();
  let entries: string[];
  try {
    entries = await readdir(MANIFEST_DIR);
  } catch {
    return manifests;
  }

  for (const filename of entries) {
    if (!filename.endsWith(".json")) continue;
    const sourceName = filename.replace(/_\d{4}-\d{2}-\d{2}\.json$/, "");
    try {
      const raw = await readFile(join(MANIFEST_DIR, filename), "utf8");
      const data = manifestSchema.parse(JSON.parse(raw));
      // Keep only the newest manifest per source
      const existing = manifests.get(sourceName);
      if (!existing || data.generated_at > existing.generated_at) {
        manifests.set(sourceName, data);
      }
    } catch {
      // Skip malformed manifest files silently
    }
  }
  return manifests;
}

async function loadManifestsForSource(
  sourceName: string,
): Promise<z.infer<typeof manifestSchema>[]> {
  const manifests: z.infer<typeof manifestSchema>[] = [];
  let entries: string[];
  try {
    entries = await readdir(MANIFEST_DIR);
  } catch {
    return manifests;
  }

  const prefix = `${sourceName}_`;
  for (const filename of entries) {
    if (!filename.startsWith(prefix) || !filename.endsWith(".json")) continue;
    try {
      const raw = await readFile(join(MANIFEST_DIR, filename), "utf8");
      const data = manifestSchema.parse(JSON.parse(raw));
      manifests.push(data);
    } catch {
      // Skip malformed manifest files silently
    }
  }

  manifests.sort(
    (a, b) => b.generated_at.localeCompare(a.generated_at),
  );
  return manifests;
}

function mergeArticlesFromManifests(
  manifests: z.infer<typeof manifestSchema>[],
): Array<{
  url: string;
  title: string;
  published: string;
  summary: string;
  author: string;
  id?: string;
}> {
  const seen = new Set<string>();
  const merged: Array<{
    url: string;
    title: string;
    published: string;
    summary: string;
    author: string;
    id?: string;
  }> = [];

  for (const manifest of manifests) {
    for (const article of manifest.articles) {
      const key = normalizeUrl(article.url);
      if (seen.has(key)) continue;
      seen.add(key);
      merged.push({
        url: article.url,
        title: article.title,
        published: article.published ?? "",
        summary: article.summary ?? "",
        author: article.author ?? "",
        id: article.id,
      });
    }
  }

  return merged;
}

function configToStatus(
  cfg: SourceConfig,
  manifest: z.infer<typeof manifestSchema> | undefined,
): SourceStatus {
  return {
    name: cfg.name,
    type: cfg.type,
    tier: cfg.tier,
    enabled: cfg.enabled,
    display_name: cfg.display_name ?? cfg.name,
    description: cfg.description,
    display_description: cfg.display_description ?? cfg.description,
    url: cfg.url,
    language: cfg.language,
    fetch_strategy: cfg.fetch_strategy,
    keywords: cfg.filter?.keywords ?? [],
    max_age_hours: cfg.filter?.max_age_hours ?? 0,
    truncation: cfg.truncation,
    target_dir: cfg.target_dir,
    manifestFound: manifest !== undefined,
    articleCount: manifest?.articles.length ?? 0,
    articles: manifest?.articles ?? [],
    manifestDate: manifest?.date ?? null,
    manifestGeneratedAt: manifest?.generated_at ?? null,
  };
}

export async function getSourceStatuses(): Promise<SourceStatus[]> {
  const [configs, manifests] = await Promise.all([
    getSourceConfigs(),
    loadManifests(),
  ]);

  const results: SourceStatus[] = configs.map((cfg) => {
    const manifest = manifests.get(cfg.name);
    return configToStatus(cfg, manifest);
  });

  // Sort by tier (A→B→C), then alphabetically by name
  const tierOrder = { A: 0, B: 1, C: 2 };
  results.sort((a, b) => {
    const d = tierOrder[a.tier] - tierOrder[b.tier];
    return d !== 0 ? d : a.name.localeCompare(b.name);
  });

  return results;
}

export async function getSourceDetail(
  name: string,
): Promise<SourceStatus | null> {
  const [configs, manifests] = await Promise.all([
    getSourceConfigs(),
    loadManifests(),
  ]);

  const config = configs.find((c) => c.name === name);
  if (!config) return null;

  return configToStatus(config, manifests.get(name));
}

function normalizeUrl(url: string): string {
  return url
    .trim()
    .replace(/\/+$/, "")
    .replace(/^http:\/\//i, "http://")
    .replace(/^https:\/\//i, "https://");
}

async function loadStructuredData(
  sourceName: string,
): Promise<StructuredArticle[]> {
  const structuredDir = join(process.cwd(), "data/04_structured");
  let entries: string[];
  try {
    entries = await readdir(structuredDir);
  } catch {
    return [];
  }

  const match = entries.find(
    (f) =>
      f.replace(/\.json$/, "").toLowerCase() === sourceName.toLowerCase(),
  );
  if (!match) return [];

  try {
    const raw = await readFile(join(structuredDir, match), "utf8");
    const parsed: unknown = JSON.parse(raw);
    const arr = Array.isArray(parsed) ? parsed : [];
    return structuredArticleSchema.array().parse(arr);
  } catch {
    return [];
  }
}

export async function getSourceDetailEnriched(
  name: string,
  dateRange?: DateRange,
): Promise<EnrichedSourceDetail | null> {
  const [configs, latestManifests] = await Promise.all([
    getSourceConfigs(),
    loadManifests(),
  ]);

  const config = configs.find((c) => c.name === name);
  if (!config) return null;

  const latestManifest = latestManifests.get(name);
  const structuredData = await loadStructuredData(name);

  const structuredMap = new Map<string, StructuredArticle>();
  for (const s of structuredData) {
    const normalized = normalizeUrl(s.source);
    if (!structuredMap.has(normalized)) {
      structuredMap.set(normalized, s);
    }
  }

  // 确定使用哪些文章：指定 dateRange 时合并全部 manifest 并过滤，否则用最新 manifest
  let manifestArticles: Array<{
    url: string; title: string; published: string;
    summary: string; author: string; id?: string;
  }>;
  let allManifests: z.infer<typeof manifestSchema>[] = [];
  let manifestDate: string | null;
  let manifestGeneratedAt: string | null;

  if (dateRange?.from || dateRange?.to) {
    allManifests = await loadManifestsForSource(name);
    // 按 manifest.date（抓取日期）筛选，而非 article.published（发布日期）
    if (dateRange.from) {
      allManifests = allManifests.filter(
        (m) => m.date >= dateRange.from!,
      );
    }
    if (dateRange.to) {
      allManifests = allManifests.filter(
        (m) => m.date <= dateRange.to!,
      );
    }
    manifestArticles = mergeArticlesFromManifests(allManifests);
    manifestDate = allManifests[0]?.date ?? null;
    manifestGeneratedAt = allManifests[0]?.generated_at ?? null;
  } else {
    manifestArticles = latestManifest?.articles ?? [];
    manifestDate = latestManifest?.date ?? null;
    manifestGeneratedAt = latestManifest?.generated_at ?? null;
    if (latestManifest) {
      allManifests = [latestManifest];
    }
  }

  // 收集该源所有 manifest 的 date，供日期选择器使用
  const availableDates = allManifests
    .map((m) => m.date)
    .filter((d): d is string => d !== null && d !== undefined);

  const enrichedArticles: EnrichedArticle[] = manifestArticles.map((a) => {
    const normalizedArticleUrl = normalizeUrl(a.url);
    const enriched =
      structuredMap.get(normalizedArticleUrl) ?? null;
    return {
      url: a.url,
      title: a.title,
      published: a.published ?? "",
      summary: a.summary ?? "",
      author: a.author ?? "",
      id: a.id,
      enriched,
      status: enriched
        ? determineProcessingStatus(enriched)
        : "scout",
    };
  });

  const stageCounts: Record<ProcessingStatus, number> = {
    scout: 0,
    extracted: 0,
    analyzed: 0,
  };
  for (const a of enrichedArticles) {
    stageCounts[a.status]++;
  }

  return {
    name: config.name,
    type: config.type,
    tier: config.tier,
    enabled: config.enabled,
    display_name: config.display_name ?? config.name,
    description: config.description,
    display_description: config.display_description ?? config.description,
    url: config.url,
    language: config.language,
    fetch_strategy: config.fetch_strategy,
    keywords: config.filter?.keywords ?? [],
    max_age_hours: config.filter?.max_age_hours ?? 0,
    truncation: config.truncation,
    target_dir: config.target_dir,
    manifestFound: manifestArticles.length > 0,
    articleCount: enrichedArticles.length,
    articles: enrichedArticles,
    manifestDate,
    manifestGeneratedAt,
    stageCounts,
    availableDates,
    dateRange: dateRange ?? null,
  };
}

export async function getTiersMeta(): Promise<Record<string, TierMeta>> {
  const raw = await readFile(TIERS_PATH, "utf8");
  const tiers = parseYaml(raw);
  return (tiers ?? {}) as Record<string, TierMeta>;
}

export interface SourcesViewData {
  tiersMeta: Record<string, TierMeta>;
  sources: SourceStatus[];
  totalSources: number;
  latestDate: string | null;
}

export async function getSourcesViewData(): Promise<SourcesViewData> {
  const [sources, tiersMeta] = await Promise.all([
    getSourceStatuses(),
    getTiersMeta(),
  ]);

  const latestDate =
    sources
      .map((s) => s.manifestDate)
      .filter((d): d is string => d !== null)
      .sort()
      .reverse()[0] ?? null;

  return {
    tiersMeta,
    sources,
    totalSources: sources.length,
    latestDate,
  };
}
