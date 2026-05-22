"""
一次性脚本：将 data/01_raw, 02_extracted, 03_analyzed 下的序号 .md 文件重命名为 {id}.md

路径配置从 config.yaml 的 pipeline.data_dirs 读取。
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from pipeline.core.config_loader import resolve_data_dir
from pipeline.utils.frontmatter import read_frontmatter


def rename_dir(base: Path) -> int:
    """重命名 base 目录下所有 .md 文件为 {id}.md，返回修改数量。"""
    count = 0
    for md_path in sorted(base.rglob("*.md")):
        stem = md_path.stem
        fm, _ = read_frontmatter(md_path)
        article_id = fm.get("id", "")
        if not article_id:
            print(f"  [跳过] {md_path.relative_to(base.parent)} — 无 id 字段")
            continue
        if stem == article_id:
            continue  # already correct
        new_path = md_path.with_stem(article_id)
        if new_path.exists():
            print(f"  [冲突] {md_path.relative_to(base.parent)} → {new_path.name} — 目标已存在，跳过")
            continue
        md_path.rename(new_path)
        print(f"  {md_path.name} → {new_path.name}")
        count += 1
    return count


def main():
    for dir_key in ["raw", "extracted", "analyzed"]:
        base = resolve_data_dir(dir_key)
        if not base.exists():
            print(f"\n{dir_key}/ 不存在，跳过")
            continue
        print(f"\n=== {dir_key}/ ===")
        n = rename_dir(base)
        print(f"共重命名 {n} 个文件")

    print("\n完成。")


if __name__ == "__main__":
    main()
