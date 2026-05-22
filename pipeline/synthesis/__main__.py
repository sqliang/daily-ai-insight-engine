"""
uv run python -m pipeline.synthesis CLI 入口

用法：
    uv run python -m pipeline.synthesis aggregate                 Stage 4a: 聚合 frontmatter
    uv run python -m pipeline.synthesis aggregate --dry-run       Stage 4a: 仅列出文件
    uv run python -m pipeline.synthesis synthesize                Stage 4b: 日报合成
    uv run python -m pipeline.synthesis synthesize --dry-run      Stage 4b: 显示 prompt 预估
"""

import sys
from pathlib import Path

# 确保项目根目录在 sys.path 中，支持从任意目录运行
# 路径链: __main__.py → synthesis/ → pipeline/ → 项目根
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from pipeline.synthesis.cli import main

if __name__ == "__main__":
    sys.exit(main())
