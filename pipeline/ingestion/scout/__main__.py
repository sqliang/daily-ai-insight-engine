"""
uv run python -m pipeline.ingestion.scout CLI 入口

用法：
    uv run python -m pipeline.ingestion.scout          # 增量抓取（跳过已有清单）
    uv run python -m pipeline.ingestion.scout --force  # 强制重新抓取所有源
"""

import sys
from pathlib import Path

# 确保项目根目录在 sys.path 中，支持从任意目录运行
# 路径链: __main__.py → scout/ → ingestion/ → pipeline/ → 项目根
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent.parent))

from pipeline.ingestion.scout.cli import main

if __name__ == "__main__":
    sys.exit(main())
