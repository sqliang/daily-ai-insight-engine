"""
python -m pipeline.ingestion.backfill_ids CLI 入口

用法：
    python -m pipeline.ingestion.backfill_ids              # 处理 data/01_raw/ 下所有文件
    python -m pipeline.ingestion.backfill_ids --dry-run    # 仅列出文件
    python -m pipeline.ingestion.backfill_ids -i path/to/file.md
"""

import sys
from pathlib import Path

# 确保项目根目录在 sys.path 中，支持从任意目录运行
# 路径链: __main__.py → backfill_ids/ → ingestion/ → pipeline/ → 项目根
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent.parent))

from pipeline.ingestion.backfill_ids.cli import main

if __name__ == "__main__":
    sys.exit(main())
