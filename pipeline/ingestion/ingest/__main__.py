"""
python -m pipeline.ingestion.ingest CLI 入口

用法：
    python -m pipeline.ingestion.ingest                  # 处理今日所有清单
    python -m pipeline.ingestion.ingest --force          # 强制重新抓取
    python -m pipeline.ingestion.ingest --manifest xxx   # 处理指定清单
"""

import sys
from pathlib import Path

# 确保项目根目录在 sys.path 中，支持从任意目录运行
# 路径链: __main__.py → ingest/ → ingestion/ → pipeline/ → 项目根
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent.parent))

from pipeline.ingestion.ingest.cli import main

if __name__ == "__main__":
    sys.exit(main())
