"""
tests/test_publish.py — Stage 5 publish 字段映射纯函数测试

只测 map_* / parse_* / clean_* / strip_* 等纯函数（不连真实数据库），
覆盖：author wiki-link 剥壳、impact_score 三种形态、created 日期截断、
manifest 文件名解析兜底、frontmatter 剥离、URL 规范化去重。
"""

from datetime import date, timezone
from pathlib import Path
from unittest.mock import MagicMock

from pipeline.publish.publishers import (
    clean_author,
    map_article,
    map_manifest,
    map_report,
    normalize_url,
    parse_impact_score,
    parse_iso_date,
    parse_iso_datetime,
    parse_manifest_filename,
    strip_frontmatter,
)


# ---------------------------------------------------------------------------
# author 清洗
# ---------------------------------------------------------------------------

class TestCleanAuthor:
    def test_wiki_link_list(self):
        """列表形态的 wiki-link：取第一个元素并剥掉 [[ ]] 包裹。"""
        assert clean_author(["[[Sandeep Gaddamwar]]"]) == "Sandeep Gaddamwar"

    def test_wiki_link_string(self):
        """字符串形态的 wiki-link 同样剥壳。"""
        assert clean_author("[[Jane Doe]]") == "Jane Doe"

    def test_plain_string(self):
        assert clean_author("OpenAI") == "OpenAI"

    def test_empty_list(self):
        assert clean_author([]) is None

    def test_none(self):
        assert clean_author(None) is None

    def test_non_string_coerced(self):
        """数字等非字符串类型强转 str。"""
        assert clean_author(42) == "42"


# ---------------------------------------------------------------------------
# impact_score 三种形态
# ---------------------------------------------------------------------------

class TestParseImpactScore:
    def test_dict_form(self):
        """Stage 3 标准产出：{"score": x, "reason": ...} 取 score 键。"""
        assert parse_impact_score({"score": 2.5, "reason": "…"}) == 2.5

    def test_numeric_form(self):
        assert parse_impact_score(7) == 7.0
        assert parse_impact_score(3.5) == 3.5

    def test_numeric_string(self):
        assert parse_impact_score("4.5") == 4.5

    def test_none_and_unparseable(self):
        assert parse_impact_score(None) is None
        assert parse_impact_score({}) is None
        assert parse_impact_score({"reason": "无 score"}) is None
        assert parse_impact_score("高") is None
        # bool 是 int 子类但语义上不是分数
        assert parse_impact_score(True) is None


# ---------------------------------------------------------------------------
# created 日期截断
# ---------------------------------------------------------------------------

class TestParseIsoDate:
    def test_plain_date(self):
        assert parse_iso_date("2026-08-28") == date(2026, 8, 28)

    def test_iso_timestamp_truncated(self):
        """完整 ISO 时间戳截断为日期。"""
        assert parse_iso_date("2026-08-28T10:30:00+00:00") == date(2026, 8, 28)

    def test_z_suffix(self):
        assert parse_iso_date("2026-08-28T10:30:00Z") == date(2026, 8, 28)

    def test_invalid(self):
        assert parse_iso_date("not-a-date") is None
        assert parse_iso_date(None) is None
        assert parse_iso_date("") is None

    def test_non_string_coerced(self):
        # 无连字符的基本 ISO 格式可被 Python 3.11+ 解析，强转后有效
        assert parse_iso_date(20260828) == date(2026, 8, 28)
        # 完全无法解析的数字 → None
        assert parse_iso_date(42) is None


# ---------------------------------------------------------------------------
# manifest 文件名解析兜底
# ---------------------------------------------------------------------------

class TestManifestFilename:
    def test_simple_source(self):
        assert parse_manifest_filename("36kr_2026-05-08") == ("36kr", "2026-05-08")

    def test_hyphenated_source(self):
        """source 本身含连字符时从右侧切分，保证日期部分完整。"""
        assert parse_manifest_filename("arxiv-cs-ai_2026-08-28") == ("arxiv-cs-ai", "2026-08-28")

    def test_invalid(self):
        assert parse_manifest_filename("no-date-here") is None

    def test_map_manifest_prefers_json_fields(self):
        """JSON 内 source/date 优先于文件名。"""
        row = map_manifest("wrong-name", {
            "source": "36kr", "date": "2026-05-08",
            "generated_at": "2026-05-08T01:52:51+00:00", "articles": [],
        })
        assert row["source"] == "36kr"
        assert row["date"] == "2026-05-08"
        assert row["generated_at"].tzinfo is not None

    def test_map_manifest_filename_fallback(self):
        """JSON 缺 source/date 时用文件名兜底。"""
        row = map_manifest("bensbites_2026-06-01", {"articles": []})
        assert row["source"] == "bensbites"
        assert row["date"] == "2026-06-01"
        assert row["generated_at"] is None

    def test_map_manifest_unresolvable(self):
        assert map_manifest("garbage", {}) is None


# ---------------------------------------------------------------------------
# 日报映射与 frontmatter 剥离
# ---------------------------------------------------------------------------

class TestStripFrontmatter:
    def test_strip(self):
        text = "---\ntitle: 日报\ndate: 2026-08-29\n---\n\n# 正文\n内容"
        assert strip_frontmatter(text) == "# 正文\n内容"

    def test_no_frontmatter(self):
        assert strip_frontmatter("# 正文") == "# 正文"

    def test_unclosed_frontmatter_passthrough(self):
        """只有起始 --- 没有闭合 --- 时原样返回。"""
        text = "---\ntitle: 未闭合\n# 正文"
        assert strip_frontmatter(text) == text


class TestMapReport:
    def _make_report(self, tmp_path: Path, with_md: bool = True):
        json_path = tmp_path / "daily-report-2026-08-29.json"
        json_path.write_text("{}", encoding="utf-8")
        if with_md:
            json_path.with_suffix(".md").write_text(
                "---\ntitle: x\n---\n正文内容", encoding="utf-8"
            )
        return json_path

    def test_basic(self, tmp_path):
        json_path = self._make_report(tmp_path)
        row = map_report(json_path, {"generatedAt": "2026-08-30T00:30:00+08:00"})
        assert row["date"] == "2026-08-29"
        assert row["generated_at"].utcoffset().total_seconds() == 8 * 3600
        assert row["report_md"] == "正文内容"

    def test_generated_at_fallback_to_mtime(self, tmp_path):
        """JSON 无 generatedAt 时用文件 mtime 兜底。"""
        json_path = self._make_report(tmp_path, with_md=False)
        row = map_report(json_path, {})
        assert row["generated_at"] is not None
        assert row["report_md"] is None

    def test_undated_filename_skipped(self, tmp_path):
        """无日期的 daily-report.json 不匹配，返回 None。"""
        assert map_report(tmp_path / "daily-report.json", {}) is None


# ---------------------------------------------------------------------------
# 文章映射
# ---------------------------------------------------------------------------

class TestMapArticle:
    def test_full_mapping(self):
        entry = {
            "id": "abc123",
            "source_dir": "arxiv-cs-ai",
            "created": "2026-08-28",
            "published": "2026-08-27",
            "source": "https://arxiv.org/abs/2608.26151",
            "title": "某论文",
            "author": ["[[Sandeep Gaddamwar]]"],
            "description": "摘要",
            "tldr": "一句话",
            "objective_summary": "客观总结",
            "event_type": "paper",
            "sentiment": "positive",
            "impact_score": {"score": 2.5, "reason": "…"},
        }
        row = map_article(entry)
        assert row["id"] == "abc123"
        assert row["source_dir"] == "arxiv-cs-ai"
        assert row["created"] == date(2026, 8, 28)
        assert row["url"] == "https://arxiv.org/abs/2608.26151"
        assert row["author"] == "Sandeep Gaddamwar"
        assert row["impact_score"] == 2.5
        assert row["payload"] is entry  # payload 整存原始 dict

    def test_created_iso_timestamp_truncated(self):
        entry = {"id": "x", "created": "2026-08-28T10:30:00+00:00"}
        assert map_article(entry)["created"] == date(2026, 8, 28)

    def test_missing_id_skipped(self):
        assert map_article({"created": "2026-08-28"}) is None

    def test_missing_created_skipped(self):
        assert map_article({"id": "x"}) is None

    def test_non_string_published_coerced(self):
        """published 为非字符串类型时强转 str，防止 DB 类型错误。"""
        row = map_article({"id": "x", "created": "2026-08-28", "published": 20260828})
        assert row["published"] == "20260828"


# ---------------------------------------------------------------------------
# URL 规范化
# ---------------------------------------------------------------------------

class TestNormalizeUrl:
    def test_trailing_slash(self):
        assert normalize_url("https://a.com/x/") == "https://a.com/x"

    def test_whitespace_and_case(self):
        assert normalize_url("  HTTPS://a.com/x  ") == "https://a.com/x"


# ---------------------------------------------------------------------------
# DB 写入层（mock 连接，不连真库）
# ---------------------------------------------------------------------------

class TestUpsert:
    def test_upsert_articles_uses_on_conflict(self):
        """验证 upsert SQL 形态与 executemany 调用（mock 连接，不触库）。"""
        from pipeline.publish.publishers import upsert_articles

        conn = MagicMock()
        cur = conn.cursor.return_value.__enter__.return_value
        rows = [{
            "id": "a", "source_dir": "s", "created": date(2026, 8, 28),
            "published": None, "url": "https://x", "title": "t", "author": None,
            "description": None, "tldr": None, "objective_summary": None,
            "event_type": None, "sentiment": None, "impact_score": None,
            "payload": {},
        }]
        assert upsert_articles(conn, rows) == 1
        sql = cur.executemany.call_args[0][0]
        assert "ON CONFLICT (id) DO UPDATE" in sql

    def test_upsert_empty_noop(self):
        from pipeline.publish.publishers import upsert_reports

        conn = MagicMock()
        assert upsert_reports(conn, []) == 0
        conn.cursor.assert_not_called()


# ---------------------------------------------------------------------------
# parse_iso_datetime
# ---------------------------------------------------------------------------

class TestParseIsoDatetime:
    def test_z_suffix(self):
        dt = parse_iso_datetime("2026-05-08T01:52:51.153620Z")
        assert dt.tzinfo is not None

    def test_naive_gets_utc(self):
        """无时区信息按 UTC 处理，避免 timestamptz 写入歧义。"""
        dt = parse_iso_datetime("2026-05-08T01:52:51")
        assert dt.utcoffset() == timezone.utc.utcoffset(None)

    def test_invalid(self):
        assert parse_iso_datetime("bad") is None
        assert parse_iso_datetime(None) is None
