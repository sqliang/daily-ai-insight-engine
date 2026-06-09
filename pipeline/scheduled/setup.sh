#!/bin/bash
# ============================================================================
# pipeline/scheduled/setup.sh — 一键安装定时任务
#
# 执行步骤：
#   1. 检测项目根目录和用户 Home
#   2. 将 plist 模板中的占位符替换为实际路径
#   3. 复制到 ~/Library/LaunchAgents/
#   4. launchctl load 加载任务
#   5. 输出验证提示
#
# 使用方式：
#   chmod +x pipeline/scheduled/setup.sh
#   ./pipeline/scheduled/setup.sh
# ============================================================================

set -euo pipefail

# ---------------------------------------------------------------------------
# 路径定位
# ---------------------------------------------------------------------------
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
PLIST_TEMPLATE="$SCRIPT_DIR/com.daily-ai-insight.fetch.plist"
PLIST_NAME="com.daily-ai-insight.fetch.plist"
PLIST_DEST="$HOME/Library/LaunchAgents/$PLIST_NAME"

echo "============================================"
echo "  Daily AI Insight — 定时任务安装"
echo "============================================"
echo ""

# ---------------------------------------------------------------------------
# 1. 前置检查
# ---------------------------------------------------------------------------

if [ ! -f "$PLIST_TEMPLATE" ]; then
    echo "❌ 错误: 找不到 plist 模板文件: $PLIST_TEMPLATE"
    exit 1
fi

if [ ! -f "$SCRIPT_DIR/daily_fetch.sh" ]; then
    echo "❌ 错误: 找不到 daily_fetch.sh: $SCRIPT_DIR/daily_fetch.sh"
    exit 1
fi

# 确保 daily_fetch.sh 有执行权限
chmod +x "$SCRIPT_DIR/daily_fetch.sh"

# ---------------------------------------------------------------------------
# 2. 替换占位符 → 写入目标 plist
# ---------------------------------------------------------------------------

echo "  项目根目录: $PROJECT_ROOT"
echo "  用户 Home:   $HOME"
echo "  目标位置:    $PLIST_DEST"
echo ""

mkdir -p "$HOME/Library/LaunchAgents"

# 用 sed 替换占位符，写入目标位置
sed -e "s|{{PROJECT_ROOT}}|$PROJECT_ROOT|g" \
    -e "s|{{HOME}}|$HOME|g" \
    "$PLIST_TEMPLATE" > "$PLIST_DEST"

echo "  ✅ plist 已生成: $PLIST_DEST"

# ---------------------------------------------------------------------------
# 3. 加载到 launchd
# ---------------------------------------------------------------------------

# 先尝试卸载已存在的同名任务（避免重复加载报错）
launchctl unload "$PLIST_DEST" 2>/dev/null || true

launchctl load "$PLIST_DEST"
echo "  ✅ 已加载到 launchd"

# ---------------------------------------------------------------------------
# 4. 验证
# ---------------------------------------------------------------------------

echo ""
echo "--------------------------------------------"
echo "  验证安装"
echo "--------------------------------------------"

if launchctl list | grep -q "com.daily-ai-insight.fetch"; then
    echo "  ✅ 任务已在 launchd 中注册"
else
    echo "  ⚠️  警告: 未在 launchctl list 中找到任务，可能加载失败"
fi

echo ""
echo "--------------------------------------------"
echo "  安装完成！"
echo "--------------------------------------------"
echo ""
echo "  调度规则: 每天 17:30 自动执行 scout + ingest"
echo ""
echo "  手动触发测试（立即执行一次，不等 17:30）："
echo "    launchctl start com.daily-ai-insight.fetch"
echo ""
echo "  查看任务状态："
echo "    launchctl list | grep com.daily-ai-insight"
echo ""
echo "  查看最近运行结果："
echo "    uv run python pipeline/run.py schedule-status"
echo ""
echo "  卸载定时任务："
echo "    ./pipeline/scheduled/teardown.sh"
echo ""
