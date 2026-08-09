"""신선도 게이트 스펙. scripts/check_freshness.py가 이 테스트를 전부 통과해야 M3 완료.
실행: .venv/bin/python -m pytest tests/ -q"""
import datetime
import importlib.util
import pathlib

_spec = importlib.util.spec_from_file_location(
    "check_freshness",
    pathlib.Path(__file__).resolve().parents[1] / "scripts" / "check_freshness.py")
assert _spec is not None and _spec.loader is not None
cf = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cf)

TODAY = datetime.date(2026, 8, 9)

FRESH = """---
owner: me
updated: 2026-08-01
volatility: 3m
---
# 최근 페이지
"""

STALE = """---
owner: me
updated: 2026-01-05
volatility: 1m
---
# 오래된 페이지
"""

NO_META = """# 메타데이터가 없는 페이지
본문만 있다.
"""


def test_parse_meta_reads_front_matter():
    meta = cf.parse_meta(FRESH)
    assert meta["owner"] == "me"
    assert meta["updated"] == "2026-08-01"
    assert meta["volatility"] == "3m"


def test_parse_meta_returns_none_without_front_matter():
    assert cf.parse_meta(NO_META) is None


def test_classify_fresh_page_is_ok():
    assert cf.classify(cf.parse_meta(FRESH), TODAY) == "ok"


def test_classify_overdue_page_needs_review():
    assert cf.classify(cf.parse_meta(STALE), TODAY) == "review"


def test_classify_missing_meta():
    assert cf.classify(None, TODAY) == "missing"


def test_scan_exit_code(tmp_path):
    docs = tmp_path / "docs"
    docs.mkdir()
    (docs / "a.md").write_text(FRESH)
    (docs / "b.md").write_text(STALE)
    assert cf.scan(docs, TODAY) == 0          # review는 경고일 뿐 통과
    (docs / "c.md").write_text(NO_META)
    assert cf.scan(docs, TODAY) == 2          # 메타데이터 누락은 차단
