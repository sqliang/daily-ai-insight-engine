#!/bin/bash
# ============================================================================
# pipeline/scheduled/teardown.sh — 一键卸载定时任务
#
# 执行步骤：
#   1. launchctl unload 从系统调度器移除
#   2. 删除 ~/Library/LaunchAgents/ 下的 plist 文件
#   3. 确认任务已消失
#
# 使用方式：
#   ./pipeline/scheduled/teardown.sh
#
# 注意：卸载不会删除 data/scheduled/last_run.json（历史状态）和
#   pipeline/scheduled/ 目录（方便日后重新安装）。
# ============================================================================

set -euo pipefail

PLIST_NAME="com.daily-ai-insight.fetch.plist"
PLIST_PATH="$HOME/Library/LaunchAgents/$PLIST_NAME"

echo "============================================"
echo "  Daily AI Insight — 卸载定时任务"
echo "============================================"
echo ""

# ---------------------------------------------------------------------------
# 1. 从 launchd 卸载
# ---------------------------------------------------------------------------

if [ -f "$PLIST_PATH" ]; then
    launchctl unload "$PLIST_PATH" 2>/dev/null && \
        echo "  ✅ 已从 launchd 卸载" || \
        echo "  ⚠️  plist 文件存在但卸载失败（可能未被加载）"
else
    echo "  ⚠️  未找到 plist 文件: $PLIST_PATH"
    echo "  定时任务可能已经卸载或从未安装。"
fi

# ---------------------------------------------------------------------------
# 2. 删除 plist 文件
# ---------------------------------------------------------------------------

if [ -f "$PLIST_PATH" ]; then
    rm "$PLIST_PATH"
    echo "  ✅ 已删除: $PLIST_PATH"
fi

# ---------------------------------------------------------------------------
# 3. 验证
# ---------------------------------------------------------------------------

echo ""
if launchctl list 2>/dev/null | grep -q "com.daily-ai-insight.fetch"; then
    echo "  ❌ 警告: 任务仍在 launchctl list 中，请手动检查"
    echo "     launchctl list | grep com.daily-ai-insight"
else
    echo "  ✅ 确认: 任务已从 launchd 中移除"
fi

echo ""
echo "--------------------------------------------"
echo "  卸载完成"
echo "--------------------------------------------"
echo ""
echo "  以下文件未被删除（可手动清理）："
echo "    data/scheduled/last_run.json  — 历史运行状态记录"
echo "    logs/launchd-*.log           — launchd 输出日志"
echo "    pipeline/scheduled/          — 脚本和配置，方便日后重新安装"
echo ""
echo "  重新安装："
echo "    ./pipeline/scheduled/setup.sh"
echo ""
