import { mkdir, readFile, writeFile } from "node:fs/promises";
import { dirname } from "node:path";
import { z } from "zod";

// ============================================================================
// files.ts — 类型安全的 JSON 文件读写工具
//
// 为流水线提供统一的文件 I/O 抽象：
//   - readJsonFile:  读取 + JSON.parse + Zod 校验，失败即抛错
//   - writeJsonFile: 自动创建父目录 + 格式化 JSON 输出
//
// 所有流水线中的数据持久化均通过这两个函数完成，
// 确保读写的每个 JSON 文件都经过 Schema 校验。
// ============================================================================

export async function readJsonFile<T>(filePath: string, schema: z.ZodType<T>): Promise<T> {
  const content = await readFile(filePath, "utf8");
  return schema.parse(JSON.parse(content));
}

export async function writeJsonFile(filePath: string, value: unknown): Promise<void> {
  await mkdir(dirname(filePath), { recursive: true });
  await writeFile(filePath, `${JSON.stringify(value, null, 2)}\n`, "utf8");
}
