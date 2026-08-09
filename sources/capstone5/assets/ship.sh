#!/usr/bin/env bash
# 출고 게이트: 셋 중 하나라도 실패하면 site/를 만들지 않는다.
set -euo pipefail

echo "[1/3] 신선도 메타데이터"
python3 scripts/check_freshness.py

echo "[2/3] 성숙도 라벨 lint"
missing=0
for f in docs/p*.md; do
  if ! grep -q "🟢\|🟡\|🔵\|⚪" "$f"; then
    echo "  성숙도 라벨 없음: $f"
    missing=1
  fi
done
test "$missing" -eq 0

echo "[3/3] mkdocs build --strict"
mkdocs build --strict

echo "GATE PASS, site/ 준비 완료"
