"""
pipeline/publish/db.py — PostgreSQL 连接管理

职责：从环境变量 DATABASE_URL 建立 psycopg 连接，供 publishers.py 使用。
DATABASE_URL 由 pipeline/run.py 入口从 .env 自动加载（python-dotenv）。
表结构由 drizzle 迁移管理，本模块只负责连接，不做任何 DDL。
"""

import os

import psycopg


def get_connection(database_url: str | None = None) -> "psycopg.Connection":
    """
    建立 PostgreSQL 连接。

    参数：
        database_url: 连接串（默认从环境变量 DATABASE_URL 读取，便于测试注入）

    返回：
        psycopg.Connection: 已建立的连接（调用方负责关闭）

    异常：
        RuntimeError: DATABASE_URL 未配置时抛出，附中文配置指引
    """
    url = database_url or os.environ.get("DATABASE_URL")
    if not url:
        # 显式报错而非静默失败：DB 是 publish 阶段的唯一写入目标，
        # 缺配置继续跑只会产生"成功"的假象
        raise RuntimeError(
            "未配置 DATABASE_URL 环境变量，无法连接 PostgreSQL。\n"
            "请在项目根目录 .env 中添加，例如：\n"
            "  DATABASE_URL=postgresql://postgres:postgres@localhost:5433/ai_insight\n"
            "（pipeline/run.py 会自动加载 .env）"
        )
    return psycopg.connect(url)
