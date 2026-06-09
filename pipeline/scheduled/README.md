# 定时抓取任务（Scheduled Fetch）

## 功能概述

每天 **17:30** 自动执行 `scout` → `ingest` 两个管道阶段，将当日 AI 资讯抓取到本地。完成后通过 **macOS 通知中心** 推送摘要，用户收到通知后可手动执行后续分析阶段（extract → analyze → synthesize）。

**为什么只自动化前两步？** scout 和 ingest 是纯数据抓取（不消耗 LLM token），适合无人值守；extract / analyze / synthesize 需要 AI 调用，保留手动控制以便用户审查结果。

## 工作流程

```
┌─────────────────────────────────────────────────────────┐
│                  macOS launchd                          │
│             每天 17:30 自动触发                          │
└─────────────────┬───────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────────────┐
│            daily_fetch.sh (Shell 包装脚本)               │
│                                                         │
│  1. uv run python pipeline/run.py scout                 │
│     ├─ 遍历 23 个数据源，抓取 RSS/API/Scrape/Browser     │
│     ├─ 生成 data/00_manifest/{source}_{date}.json       │
│     └─ 输出: "总计: N 个源, M 篇文章"                    │
│                                                         │
│  2. uv run python pipeline/run.py ingest                │
│     ├─ 读取 manifest，逐篇下载正文 → Markdown            │
│     ├─ 写入 data/01_raw/{source}/{id}.md                │
│     └─ 输出: "完成: 总计 N 篇 (success/partial/failed)"  │
│                                                         │
│  3. 解析输出 → 提取统计数据                              │
│  4. 写入 data/scheduled/last_run.json (结构化状态)       │
│  5. 发送 macOS 通知 (成功/失败摘要)                      │
└─────────────────────────────────────────────────────────┘
```

## 文件说明

| 文件 | 位置 | 职责 |
|------|------|------|
| `daily_fetch.sh` | `pipeline/scheduled/` | 主执行脚本，被 launchd 调用 |
| `setup.sh` | `pipeline/scheduled/` | 一键安装：替换路径 → 复制 plist → 加载到 launchd |
| `teardown.sh` | `pipeline/scheduled/` | 一键卸载：从 launchd 移除 → 删除 plist |
| `com.daily-ai-insight.fetch.plist` | `pipeline/scheduled/` (模板) → `~/Library/LaunchAgents/` (安装后) | launchd 任务配置 |
| `last_run.json` | `data/scheduled/` | 最近一次运行的完整状态（机器可读） |
| `schedule-status` | `pipeline/run.py` 子命令 | CLI 查询最近运行状态 |

## 安装

### 前置条件

- **macOS** 系统（定时调度依赖 launchd）
- 项目已正确初始化：`.env` 文件就绪，`uv` 已安装，依赖已安装（`uv pip install -r pipeline/requirements.txt`）
- 已手动执行过一次 `scout` + `ingest`，确认管道可正常运行

### 安装步骤

```bash
# 1. 赋予脚本执行权限
chmod +x pipeline/scheduled/*.sh

# 2. 运行安装脚本
./pipeline/scheduled/setup.sh
```

**`setup.sh` 具体做了什么：**

1. 检测项目根目录和用户 Home 路径
2. 将 `com.daily-ai-insight.fetch.plist` 模板中的 `{{PROJECT_ROOT}}` 和 `{{HOME}}` 占位符替换为实际路径
3. 将替换后的 plist 复制到 `~/Library/LaunchAgents/com.daily-ai-insight.fetch.plist`
4. 执行 `launchctl load` 将任务加载到系统调度器
5. 输出验证提示

### 验证安装成功

```bash
# 方法 1：确认任务已在 launchd 中注册
launchctl list | grep com.daily-ai-insight

# 方法 2：手动触发一次（不等 17:30），验证端到端链路
launchctl start com.daily-ai-insight.fetch

# 方法 3：查看最近运行状态
uv run python pipeline/run.py schedule-status
```

## 卸载

### 完全卸载

```bash
./pipeline/scheduled/teardown.sh
```

**`teardown.sh` 具体做了什么：**

1. 执行 `launchctl unload` 从系统调度器移除任务
2. 删除 `~/Library/LaunchAgents/com.daily-ai-insight.fetch.plist` 文件
3. 确认任务已从 `launchctl list` 中消失

### 仅暂停（保留配置，以后可恢复）

```bash
# 暂停定时触发
launchctl unload ~/Library/LaunchAgents/com.daily-ai-insight.fetch.plist

# 恢复定时触发
launchctl load ~/Library/LaunchAgents/com.daily-ai-insight.fetch.plist
```

### 卸载后残留文件

卸载脚本**不会**删除以下文件，如需彻底清理可手动操作：

| 文件/目录 | 说明 | 清理命令 |
|-----------|------|----------|
| `data/scheduled/last_run.json` | 历史运行状态记录 | `rm data/scheduled/last_run.json` |
| `logs/launchd-stdout.log` | launchd 标准输出日志 | `rm logs/launchd-*.log` |
| `logs/launchd-stderr.log` | launchd 标准错误日志 | `rm logs/launchd-*.log` |
| `pipeline/scheduled/` | 脚本和配置目录 | 可保留以便日后重新安装 |

## 日常使用

- 每天 17:30 自动执行，完成后弹出 macOS 通知
- 随时运行 `uv run python pipeline/run.py schedule-status` 查看最近运行结果
- 收到**成功通知**后，手动执行后续阶段：

```bash
uv run python pipeline/run.py extract    # Stage 2: 事实提取 → 自动 aggregate
uv run python pipeline/run.py analyze    # Stage 3: 深度分析 → 自动 aggregate
uv run python pipeline/run.py synthesize # Stage 4b: 日报合成
```

## 配置与定制

### 修改执行时间

编辑项目中的 plist 模板文件 `pipeline/scheduled/com.daily-ai-insight.fetch.plist`，修改 `StartCalendarInterval` 中的 `Hour` / `Minute`，然后重新安装：

```bash
# 先卸载旧配置
launchctl unload ~/Library/LaunchAgents/com.daily-ai-insight.fetch.plist

# 重新安装（setup.sh 会重新替换路径并加载）
./pipeline/scheduled/setup.sh
```

也可以直接编辑已安装的 plist：
```bash
vim ~/Library/LaunchAgents/com.daily-ai-insight.fetch.plist
# 修改后重新加载
launchctl unload ~/Library/LaunchAgents/com.daily-ai-insight.fetch.plist
launchctl load ~/Library/LaunchAgents/com.daily-ai-insight.fetch.plist
```

### 关闭通知

通知通过 `osascript` 调用 macOS 原生通知中心，无需额外依赖。
如需关闭通知，编辑 `pipeline/scheduled/daily_fetch.sh`，注释掉 `_notify` 调用行（搜索 `_notify` 即可找到三处调用）。

## 维护与排查

### 查看运行日志

```bash
# 管道各阶段的详细日志（按日期分目录）
tail -100 logs/$(date +%Y-%m-%d)/scout_scheduled.log
tail -100 logs/$(date +%Y-%m-%d)/ingest_scheduled.log

# launchd 自身的标准输出和错误输出
tail -50 logs/launchd-stdout.log
tail -50 logs/launchd-stderr.log
```

### 检查定时任务状态

```bash
# 确认任务是否在 launchd 中注册
launchctl list | grep com.daily-ai-insight

# 查看任务配置详情
launchctl print gui/$(id -u)/com.daily-ai-insight.fetch
```

### 手动触发（不等 17:30）

```bash
# 方式 1：通过 launchd 触发
launchctl start com.daily-ai-insight.fetch

# 方式 2：直接运行脚本
./pipeline/scheduled/daily_fetch.sh
```

### 常见问题

| 问题 | 排查方向 |
|------|----------|
| 到了 17:30 没有执行 | 电脑是否休眠？`launchctl list` 确认任务存在？检查 `logs/launchd-stderr.log` |
| 通知没有弹出 | **系统设置 → 通知**，确认终端（Terminal/iTerm）的通知权限已开启 |
| scout 报错连接超时 | 网络代理是否正常？检查 `logs/{日期}/scout_scheduled.log` |
| ingest 大量文章抓取失败 | 反爬是否升级？检查 `logs/{日期}/ingest_scheduled.log` 中 `[反爬]` 和 `[异常]` 标记 |
| `uv: command not found` | launchd 的 PATH 中可能没有 `uv`，检查 plist 中 `EnvironmentVariables.PATH` 是否包含 `uv` 所在目录（通常 `/opt/homebrew/bin` 或 `~/.local/bin`） |
| 任务已安装但 `schedule-status` 显示"尚未运行" | 任务尚未触发过执行，请手动触发测试 |

### 状态文件结构

`data/scheduled/last_run.json` 格式：

```json
{
  "timestamp": "2026-06-08T17:30:05+08:00",
  "date": "2026-06-08",
  "status": "success",
  "scout": {
    "sources_scanned": 23,
    "articles_found": 156,
    "failed_sources": [],
    "errors": []
  },
  "ingest": {
    "total": 150,
    "success": 145,
    "partial": 4,
    "failed": 1,
    "skipped": 6,
    "errors": []
  },
  "log_files": {
    "scout": "/path/to/logs/2026-06-08/scout_scheduled.log",
    "ingest": "/path/to/logs/2026-06-08/ingest_scheduled.log"
  }
}
```

- `status`: `"success"` 全部成功 / `"partial"` 部分失败 / `"failed"` 完全崩溃
- `scout.failed_sources`: 抓取失败的源名称列表
- `ingest.errors`: ingest 阶段错误信息（最多 5 条）
