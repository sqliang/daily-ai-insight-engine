#!/bin/bash
# ============================================================================
# pipeline/scheduled/daily_fetch.sh — 每日定时抓取脚本
#
# 由 launchd 每天 17:30 自动调用，执行 Stage 1a (scout) + Stage 1b (ingest)，
# 解析输出统计数据，写入 last_run.json 状态文件，并通过 macOS 通知中心推送摘要。
#
# 退出码约定：
#   0 — 全部成功
#   1 — 部分失败（scout 或 ingest 有个别源/文章出错，但整体流程完成）
#   2 — 完全失败（scout 或 ingest 脚本级崩溃，未产生任何有效输出）
# ============================================================================

set -uo pipefail  # 不使用 -e，手动捕获子进程退出码

# ---------------------------------------------------------------------------
# 路径定位 — 脚本位于 pipeline/scheduled/，项目根在 ../../
# ---------------------------------------------------------------------------
PROJECT_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
STATUS_FILE="$PROJECT_ROOT/data/scheduled/last_run.json"
LOG_DIR="$PROJECT_ROOT/logs/$(date +%Y-%m-%d)"

mkdir -p "$LOG_DIR" "$(dirname "$STATUS_FILE")"

TIMESTAMP=$(date -Iseconds)
TODAY=$(date +%Y-%m-%d)
NOTIFY_TITLE="Daily AI Insight"

# 临时文件：存放解析出的统计数据，供 Python 汇总脚本读取
TMP_DIR=$(mktemp -d)
SCOUT_FAILED_FILE="$TMP_DIR/scout_failed_sources.txt"
SCOUT_ERRORS_FILE="$TMP_DIR/scout_errors.txt"
INGEST_ERRORS_FILE="$TMP_DIR/ingest_errors.txt"
touch "$SCOUT_FAILED_FILE" "$SCOUT_ERRORS_FILE" "$INGEST_ERRORS_FILE"

# 清理临时目录
_cleanup() { rm -rf "$TMP_DIR"; }
trap _cleanup EXIT

# ---------------------------------------------------------------------------
# 工具函数
# ---------------------------------------------------------------------------

_notify() {
    local title="$1"
    local message="$2"
    osascript -e "display notification \"$message\" with title \"$title\"" 2>/dev/null || true
}

# 从 pipeline 输出的文本行中提取数字（如 "总计: 23 个源, 156 篇文章" → 23）
_extract_number() {
    local text="$1"
    local pattern="$2"
    echo "$text" | grep -oE "$pattern" | grep -oE '[0-9]+' | head -1
}

# ---------------------------------------------------------------------------
# Stage 1a: Scout
# ---------------------------------------------------------------------------

echo "========== $(date '+%Y-%m-%d %H:%M:%S') Scout 开始 =========="

SCOUT_LOG="$LOG_DIR/scout_scheduled.log"
SCOUT_EXIT=0

cd "$PROJECT_ROOT"
uv run python pipeline/run.py scout 2>&1 | tee "$SCOUT_LOG" || SCOUT_EXIT=${PIPESTATUS[0]}
SCOUT_OUTPUT=$(cat "$SCOUT_LOG")

echo "========== $(date '+%Y-%m-%d %H:%M:%S') Scout 结束 (exit=$SCOUT_EXIT) =========="
echo ""

# --- 解析 scout 统计 ---
SCOUT_SOURCES=0
SCOUT_ARTICLES=0

# "总计: 23 个源, 156 篇文章"
SCOUT_SUMMARY=$(echo "$SCOUT_OUTPUT" | grep "总计:" | tail -1)
if [ -n "$SCOUT_SUMMARY" ]; then
    SCOUT_SOURCES=$(_extract_number "$SCOUT_SUMMARY" '[0-9]+ 个源')
    SCOUT_ARTICLES=$(_extract_number "$SCOUT_SUMMARY" '[0-9]+ 篇文章')
fi
SCOUT_SOURCES=${SCOUT_SOURCES:-0}
SCOUT_ARTICLES=${SCOUT_ARTICLES:-0}

# 提取失败源名（"❌ 抓取失败: {name}: {error}" → name）
echo "$SCOUT_OUTPUT" | grep "❌ 抓取失败" | sed -n 's/.*❌ 抓取失败: \([^:]\+\):.*/\1/p' > "$SCOUT_FAILED_FILE"

# 提取错误行（限制 5 行）
echo "$SCOUT_OUTPUT" | grep -E "❌|ERROR" | head -5 > "$SCOUT_ERRORS_FILE"

# ---------------------------------------------------------------------------
# Stage 1b: Ingest
# ---------------------------------------------------------------------------

echo "========== $(date '+%Y-%m-%d %H:%M:%S') Ingest 开始 =========="

INGEST_LOG="$LOG_DIR/ingest_scheduled.log"
INGEST_EXIT=0

cd "$PROJECT_ROOT"
uv run python pipeline/run.py ingest 2>&1 | tee "$INGEST_LOG" || INGEST_EXIT=${PIPESTATUS[0]}
INGEST_OUTPUT=$(cat "$INGEST_LOG")

echo "========== $(date '+%Y-%m-%d %H:%M:%S') Ingest 结束 (exit=$INGEST_EXIT) =========="
echo ""

# --- 解析 ingest 统计 ---
INGEST_TOTAL=0
INGEST_SUCCESS=0
INGEST_PARTIAL=0
INGEST_FAILED=0
INGEST_SKIPPED=0

# "=== 完成: 总计 150 篇 (success: 145, partial: 4, failed: 1), 跳过 6 篇（历史去重） ==="
INGEST_SUMMARY=$(echo "$INGEST_OUTPUT" | grep "=== 完成:" | tail -1)
if [ -n "$INGEST_SUMMARY" ]; then
    INGEST_TOTAL=$(_extract_number "$INGEST_SUMMARY" '总计 [0-9]+ 篇')
    INGEST_SUCCESS=$(_extract_number "$INGEST_SUMMARY" 'success: [0-9]+')
    INGEST_PARTIAL=$(_extract_number "$INGEST_SUMMARY" 'partial: [0-9]+')
    INGEST_FAILED=$(_extract_number "$INGEST_SUMMARY" 'failed: [0-9]+')
    INGEST_SKIPPED=$(_extract_number "$INGEST_SUMMARY" '跳过 [0-9]+ 篇')
fi
INGEST_TOTAL=${INGEST_TOTAL:-0}
INGEST_SUCCESS=${INGEST_SUCCESS:-0}
INGEST_PARTIAL=${INGEST_PARTIAL:-0}
INGEST_FAILED=${INGEST_FAILED:-0}
INGEST_SKIPPED=${INGEST_SKIPPED:-0}

# 错误行（限制 5 行）
echo "$INGEST_OUTPUT" | grep -E "\[异常\]|ERROR" | head -5 > "$INGEST_ERRORS_FILE"

# ---------------------------------------------------------------------------
# Stage 1c: Repair — 自动修复抓取失败的文章
# ---------------------------------------------------------------------------

REPAIR_TOTAL=0
REPAIR_REPAIRED=0
REPAIR_STILL_FAILED=0

if [ "$INGEST_FAILED" -gt 0 ] || [ "$INGEST_PARTIAL" -gt 0 ]; then
    echo "========== $(date '+%Y-%m-%d %H:%M:%S') Repair 开始 =========="

    REPAIR_LOG="$LOG_DIR/repair_scheduled.log"
    cd "$PROJECT_ROOT"
    uv run python pipeline/run.py repair 2>&1 | tee "$REPAIR_LOG"
    REPAIR_OUTPUT=$(cat "$REPAIR_LOG")

    # 解析 repair 统计
    REPAIR_TOTAL=$(echo "$REPAIR_OUTPUT" | grep "发现:" | grep -o '[0-9]*' | head -1)
    REPAIR_REPAIRED=$(echo "$REPAIR_OUTPUT" | grep "修复:" | grep -o '[0-9]*' | head -1)
    REPAIR_STILL_FAILED=$(echo "$REPAIR_OUTPUT" | grep "仍失败:" | grep -o '[0-9]*' | head -1)
    REPAIR_TOTAL=${REPAIR_TOTAL:-0}
    REPAIR_REPAIRED=${REPAIR_REPAIRED:-0}
    REPAIR_STILL_FAILED=${REPAIR_STILL_FAILED:-0}

    echo "========== $(date '+%Y-%m-%d %H:%M:%S') Repair 结束 =========="
    echo ""
else
    echo "无需修复：无 failed 或 partial 文章，跳过 Repair"
    echo ""
fi

# ---------------------------------------------------------------------------
# 判断整体状态
# ---------------------------------------------------------------------------

FAILED_SOURCE_COUNT=$(wc -l < "$SCOUT_FAILED_FILE" | tr -d ' ')
FAILED_SOURCE_COUNT=${FAILED_SOURCE_COUNT:-0}

if [ "$SCOUT_EXIT" -eq 0 ] && [ "$INGEST_EXIT" -eq 0 ] \
   && [ "$FAILED_SOURCE_COUNT" -eq 0 ] && [ "$INGEST_FAILED" -eq 0 ]; then
    OVERALL_STATUS="success"
    OVERALL_EMOJI="✅"
elif [ "$SCOUT_EXIT" -ne 0 ] || [ "$INGEST_EXIT" -ne 0 ]; then
    OVERALL_STATUS="failed"
    OVERALL_EMOJI="❌"
else
    OVERALL_STATUS="partial"
    OVERALL_EMOJI="⚠️"
fi

# ---------------------------------------------------------------------------
# 写入 last_run.json（委托 Python 处理 JSON 转义和格式化）
# ---------------------------------------------------------------------------

python3 << PYEOF
import json, os

def read_lines(path):
    """读取文件中的非空行，去首尾空白。"""
    if not os.path.exists(path):
        return []
    with open(path, 'r', encoding='utf-8') as f:
        return [l.strip() for l in f if l.strip()]

data = {
    "timestamp": "$TIMESTAMP",
    "date": "$TODAY",
    "status": "$OVERALL_STATUS",
    "scout": {
        "sources_scanned": $SCOUT_SOURCES,
        "articles_found": $SCOUT_ARTICLES,
        "failed_sources": read_lines("$SCOUT_FAILED_FILE"),
        "errors": read_lines("$SCOUT_ERRORS_FILE"),
    },
    "ingest": {
        "total": $INGEST_TOTAL,
        "success": $INGEST_SUCCESS,
        "partial": $INGEST_PARTIAL,
        "failed": $INGEST_FAILED,
        "skipped": $INGEST_SKIPPED,
        "errors": read_lines("$INGEST_ERRORS_FILE"),
    },
    "repair": {
        "total": $REPAIR_TOTAL,
        "repaired": $REPAIR_REPAIRED,
        "still_failed": $REPAIR_STILL_FAILED,
    },
    "log_files": {
        "scout": "$SCOUT_LOG",
        "ingest": "$INGEST_LOG",
        "repair": "$REPAIR_LOG",
    },
}

status_path = "$STATUS_FILE"
os.makedirs(os.path.dirname(status_path), exist_ok=True)
with open(status_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print(f"状态文件已写入: {status_path}")
PYEOF

# ---------------------------------------------------------------------------
# 构建通知消息
# ---------------------------------------------------------------------------

if [ "$OVERALL_STATUS" = "success" ]; then
    NOTIFY_MSG="${SCOUT_SOURCES} 个源, ${SCOUT_ARTICLES} 篇文章 | 成功: ${INGEST_SUCCESS}, 部分: ${INGEST_PARTIAL}"
    _notify "$NOTIFY_TITLE $OVERALL_EMOJI 抓取完成" "$NOTIFY_MSG"

elif [ "$OVERALL_STATUS" = "partial" ]; then
    NOTIFY_MSG="${SCOUT_SOURCES} 个源, ${SCOUT_ARTICLES} 篇文章 | 成功: ${INGEST_SUCCESS}, 失败: ${INGEST_FAILED}"
    if [ "$FAILED_SOURCE_COUNT" -gt 0 ]; then
        FAILED_LIST=$(paste -sd, "$SCOUT_FAILED_FILE" 2>/dev/null)
        NOTIFY_MSG="${NOTIFY_MSG} | 失败源: ${FAILED_LIST}"
    fi
    _notify "$NOTIFY_TITLE $OVERALL_EMOJI 部分失败" "$NOTIFY_MSG"

else
    # 完全失败 — 提取第一条错误
    FIRST_ERROR="未知错误"
    if [ -s "$SCOUT_ERRORS_FILE" ]; then
        FIRST_ERROR=$(head -1 "$SCOUT_ERRORS_FILE")
    elif [ -s "$INGEST_ERRORS_FILE" ]; then
        FIRST_ERROR=$(head -1 "$INGEST_ERRORS_FILE")
    elif [ "$SCOUT_EXIT" -ne 0 ]; then
        FIRST_ERROR="scout 退出码: $SCOUT_EXIT"
    elif [ "$INGEST_EXIT" -ne 0 ]; then
        FIRST_ERROR="ingest 退出码: $INGEST_EXIT"
    fi
    FIRST_ERROR=$(echo "$FIRST_ERROR" | cut -c1-120)
    _notify "$NOTIFY_TITLE $OVERALL_EMOJI 抓取失败" "$FIRST_ERROR"
fi

# ---------------------------------------------------------------------------
# 打印摘要到 stdout（供 launchd 日志查阅）
# ---------------------------------------------------------------------------

echo ""
echo "=========================================="
echo "  定时抓取摘要 — $TODAY"
echo "=========================================="
echo "  状态:     $OVERALL_STATUS"
echo "  Scout:    ${SCOUT_SOURCES} 源, ${SCOUT_ARTICLES} 篇"
echo "  Ingest:   总计 ${INGEST_TOTAL} (成功: ${INGEST_SUCCESS}, 部分: ${INGEST_PARTIAL}, 失败: ${INGEST_FAILED}, 跳过: ${INGEST_SKIPPED})"
echo "  日志:     $SCOUT_LOG"
echo "            $INGEST_LOG"
echo "  状态文件: $STATUS_FILE"
echo "=========================================="

if [ "$OVERALL_STATUS" = "success" ]; then
    exit 0
elif [ "$OVERALL_STATUS" = "partial" ]; then
    exit 1
else
    exit 2
fi
