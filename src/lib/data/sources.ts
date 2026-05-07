import { readFile, readdir } from "node:fs/promises";
import { join } from "node:path";
import { parse as parseYaml } from "yaml";
import { z } from "zod";

// ============================================================================
// Zod schemas for manifest JSON validation
// ============================================================================

const manifestArticleSchema = z.object({
  url: z.string(),
  title: z.string(),
  published: z.string(),
  summary: z.string(),
  author: z.string(),
});

const manifestSchema = z.object({
  source: z.string(),
  source_type: z.enum([
    "academic_paper",
    "tech_blog",
    "news_media",
    "community_discussion",
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
  description: string;
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
  description: string;
  url: string;
  language: string;
  fetch_strategy: string;
  filter: { keywords: string[]; max_age_hours: number };
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
  }>;
  manifestDate: string | null;
  manifestGeneratedAt: string | null;
}

// ============================================================================
// Data fetching
// ============================================================================

const MANIFEST_DIR = join(process.cwd(), "data/00_manifest");
const CONFIG_PATH = join(process.cwd(), "pipeline/config.yaml");

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

export async function getSourceStatuses(): Promise<SourceStatus[]> {
  const [configs, manifests] = await Promise.all([
    getSourceConfigs(),
    loadManifests(),
  ]);

  const results: SourceStatus[] = configs.map((cfg) => {
    const manifest = manifests.get(cfg.name);
    return {
      ...cfg,
      manifestFound: manifest !== undefined,
      articleCount: manifest?.articles.length ?? 0,
      articles: manifest?.articles ?? [],
      manifestDate: manifest?.date ?? null,
      manifestGeneratedAt: manifest?.generated_at ?? null,
    };
  });

  // Sort by tier (A→B→C), then alphabetically by name
  const tierOrder = { A: 0, B: 1, C: 2 };
  results.sort((a, b) => {
    const d = tierOrder[a.tier] - tierOrder[b.tier];
    return d !== 0 ? d : a.name.localeCompare(b.name);
  });

  return results;
}
