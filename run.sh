#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
VENV_PYTHON="$SCRIPT_DIR/.venv/bin/python"

if [ ! -f "$VENV_PYTHON" ]; then
    echo "错误: 未找到虚拟环境，请先运行: uv pip install -r pipeline/requirements.txt" >&2
    exit 1
fi

exec "$VENV_PYTHON" "$SCRIPT_DIR/pipeline/run.py" "$@"
