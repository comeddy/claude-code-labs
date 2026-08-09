"""페이지 신선도 점검. 사용: python3 scripts/check_freshness.py [docs디렉토리]
front matter의 updated + volatility(1m/3m/6m)로 리뷰 기한을 판정한다.
exit 0: 통과(review는 경고만), exit 2: 메타데이터 누락 페이지 존재."""
import datetime
import pathlib
import sys

VOLATILITY_DAYS = {"1m": 30, "3m": 90, "6m": 180}


def parse_meta(text):
    """front matter(--- ... ---)를 dict로. 없으면 None."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    meta = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return meta if meta else None
        if ":" in line:
            key, value = line.split(":", 1)
            meta[key.strip()] = value.strip()
    return None


def classify(meta, today):
    """'ok' / 'review'(기한 경과) / 'missing'(메타데이터 불량)"""
    if not meta or "updated" not in meta or "volatility" not in meta:
        return "missing"
    days = VOLATILITY_DAYS.get(meta["volatility"])
    if days is None:
        return "missing"
    try:
        updated = datetime.date.fromisoformat(meta["updated"])
    except ValueError:
        return "missing"
    return "review" if (today - updated).days > days else "ok"


def scan(docs_dir, today):
    """docs의 모든 .md를 판정해 표를 찍고 exit code를 돌려준다."""
    rows = []
    for page in sorted(pathlib.Path(docs_dir).glob("*.md")):
        rows.append((page.name, classify(parse_meta(page.read_text()), today)))
    width = max(len(name) for name, _ in rows) if rows else 10
    mark = {"ok": "OK", "review": "REVIEW NEEDED", "missing": "MISSING META"}
    for name, verdict in rows:
        print("  %-*s  %s" % (width, name, mark[verdict]))
    if any(v == "missing" for _, v in rows):
        return 2
    return 0


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "docs"
    sys.exit(scan(target, datetime.date.today()))
