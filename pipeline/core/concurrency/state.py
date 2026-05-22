"""
pipeline/core/concurrency/state.py — 线程安全去重状态

IngestState 封装 ingest 阶段的文章去重逻辑：
  - 内存中用 threading.Lock 保护 seen_hashes 集合
  - 所有 worker 完成后调用 flush_to_disk() 一次性持久化
  - 自动检测并迁移旧格式 MD5 哈希（12位 → SHA-256 16位）

设计理由：
    将状态管理从 orchestrator 中抽出，既让 orchestrator 更薄，
    也使得其他需要类似去重逻辑的阶段可以复用。
"""

import threading
from datetime import datetime, timezone
from typing import Set

from pipeline.core.file_utils import read_json, resolve_state_file, write_json


class IngestState:
    """
    线程安全的内存去重状态。

    Worker 线程通过 is_seen() / mark_seen() 检查并标记已处理文章，
    两者均在 threading.Lock 保护下操作内部 set。
    所有 worker 完成后由主线程调用 flush_to_disk() 持久化。
    """

    def __init__(self, force: bool = False):
        self._lock = threading.Lock()
        self._state_path = resolve_state_file()
        self._force = force
        self._dirty = False
        self._new_count = 0

        raw = self._load_raw_state()
        if force:
            self._seen_ids: Set[str] = set()
        else:
            self._seen_ids: Set[str] = set(raw.get("seen_hashes", []))

        self._last_ingest = raw.get("last_ingest", "")

    # --- 公共 API（线程安全） ---

    def is_seen(self, article_id: str) -> bool:
        """检查文章 ID 是否已入库。force 模式下始终返回 False。"""
        if self._force:
            return False
        with self._lock:
            return article_id in self._seen_ids

    def mark_seen(self, article_id: str) -> None:
        """标记文章 ID 为已入库。线程安全。"""
        with self._lock:
            if article_id not in self._seen_ids:
                self._seen_ids.add(article_id)
                self._new_count += 1
                self._dirty = True

    def flush_to_disk(self) -> None:
        """
        将去重状态持久化到磁盘。

        非线程安全 — 仅在所有 worker 完成后由主线程调用一次。
        """
        if not self._dirty:
            return
        state = {
            "seen_hashes": sorted(self._seen_ids),
            "last_ingest": datetime.now(timezone.utc).isoformat(),
        }
        write_json(self._state_path, state)

    # --- 只读属性 ---

    @property
    def seen_count(self) -> int:
        """累计去重总数（含历史）。"""
        with self._lock:
            return len(self._seen_ids)

    @property
    def new_count(self) -> int:
        """本次会话新增的已处理数。"""
        return self._new_count

    # --- 内部 ---

    def _load_raw_state(self) -> dict:
        """加载原始状态文件，自动检测并迁移旧格式。"""
        path = self._state_path
        if not path.exists():
            return {"seen_hashes": [], "last_ingest": ""}

        state = read_json(path) or {"seen_hashes": [], "last_ingest": ""}
        hashes = state.get("seen_hashes", [])

        # 检测旧格式 MD5 哈希（12 位）→ 重置
        if hashes and len(str(hashes[0])) == 12:
            print("  [迁移] 检测到旧格式 MD5 去重数据（12位），已自动切换为 SHA-256 ID（16位）")
            state["seen_hashes"] = []

        return state
