---
name: HoL-Style-01
description: Claude Code Deep Dive Workshop의 Hands-on Lab HTML 디자인 시스템. 다크 네이비 + 오렌지, macOS 터미널 코드 블록, 진행률 타임라인, DoD 체크포인트, 셀프 페이스 구성의 실습 문서를 만든다. "핸즈온 랩 만들어줘", "HoL 스타일", "실습 랩 HTML", "워크샵 랩", "캡스톤 랩", "Hands-on Lab 문서", "랩 가이드 페이지" 같은 요청, 또는 기존 랩(Ch1~Ch6, Capstone A~D)과 같은 스타일의 새 실습 문서나 포털/레퍼런스 페이지를 요청받으면 이 스킬을 사용한다. 기술 세미나 슬라이드(PPT)가 아니라 웹에서 따라 하는 실습 HTML이 대상이다.
---

# HoL-Style-01, Hands-on Lab 디자인 시스템

단일 HTML 파일로 완결되는 자습형 실습 문서를 만든다. 수강자가 혼자 열어 체크포인트를 찍으며
완주할 수 있어야 하며, 문서에 담긴 모든 코드는 출고 전에 실제로 검증되어야 한다.

## 0. 두 가지 변형

| | 챕터형 (Chapter Lab) | 캡스톤형 (Capstone Mission) |
|---|---|---|
| 시간 | 40~80분 | 135분 목표 / 150분 상한 |
| 단위 | 준비(T0) + 3~5 Task | MISSION 00~05 (M0 준비, M5 피날레) |
| 판정 | CHECKPOINT | DEFINITION OF DONE |
| id | t0, t1, ... | m0 ~ m5 |
| 고유 요소 | 없음 | MISSION BRIEFING(part-divider), 부록(컷라인+트러블슈팅), OPTION 섹션 |
| 피날레 | 마지막 Task | 셀프 검증 이벤트 (혼자 판정 가능해야 함) |

## 1. 디자인 토큰

색: 배경 #12181F, 카드 #1B242E, 코드 #0C1117, 라인 #2A3542, 본문 #E8ECF1,
뮤트 #8B96A5, 오렌지(주 강조) #FF9900, 크림슨(eyebrow) #B6002E, 그린 #3FB950,
퍼플 #7a3ff2, 라벤더 #c9a2ff, warn 라벨 핑크 #FF5C85, 인라인 코드 글자 #FFC466.

타이포: `body { word-break: keep-all; overflow-wrap: break-word }` 필수(한국어 단어 단위 줄바꿈).
h1은 clamp(26px, 4vw, 38px) + text-wrap: balance. 본문 max-width 캡 없음(전체 폭 사용).
콜아웃/카드의 좌측 강조 바 금지, 강조는 라벨 색으로(tip 제목 오렌지, warn 제목 핑크).
코드 블록 헤더는 macOS 신호등 3버튼(::before, #FF5F57/#FEBC2E/#28C840).

구두점: 가운데점(U+00B7)과 em-dash(U+2014) 금지, 구분은 쉼표나 슬래시, 대시는 하이픈(-).
예외 단 하나: 실제 UI 문구 원문 인용(예: 로그인 화면 라벨)은 허용하되 문서당 1회.

## 2. 문서 해부 (위에서 아래로)

hero(eyebrow 배지, h1, subtitle 오렌지, lede, hero-meta 배지 4개)
→ timeline(세그먼트 flex 값 = 분, 클릭 스크롤, 진행 n/N)
→ layout(좌측 sidenav + main)
→ [캡스톤만] part-divider "MISSION BRIEFING": 아키텍처 pre + 규칙 3줄
→ 섹션들: task-head(번호/제목/시간 배지), task-goal, step-title(번호 칩),
  code-wrap(터미널/prompt/output), callout(tip/warn), 체크포인트
→ [캡스톤만] OPTION 섹션(진행률 미집계, data-cp는 taskGroups 밖 키 사용)
→ [캡스톤만] 부록: 컷라인 표(시간 부족 시 순서대로) + 트러블슈팅 표(증상/원인/처방)
→ wrapup: 지도 표(배운 것과 출처/이식처) + next-box(다음 챕터 예고)
→ footer 2줄: 랩 이름, "기준: ..." (발표자 개인정보 금지)
→ script: 복사 버튼, taskGroups 진행률, IntersectionObserver 내비 하이라이트

## 3. 콘텐츠 규칙

셀프 페이스: 진행자, 옆자리, 전원 동시, 교차 방문 같은 표현 금지. 피날레와 카드류(변화구,
인터뷰, 방문 카드)는 본문 미션 안에 넣어 혼자 수행한다. destroy 안내는
"# 실습을 마쳤다면 비용 정리 (이어서 볼 계획이면 유지):" 주석으로.

코드 블록 3종: 라벨 "Terminal, 전체 복사"(기본), "Claude 세션 입력"(kind=prompt),
"출력 예시"(kind=output, 복사 버튼 없음). 파일 배치는 heredoc으로, 마커는 문서 내
유일한 대문자+EOF(예: MEDICEOF). 같은 마커 재사용 금지, 왕복 검증의 키다.

솔루션: 큰 미션에는 details.solution "막힐 때 열어보기, 완성본"을 두고 원본 파일과
바이트 일치시킨다. 판정 문장(DoD/CHECKPOINT)은 혼자 확인 가능한 관측 가능 사실로 쓴다
(좋음: "함정 질문에 refused true가 돌아온다" / 나쁨: "동작을 이해했다").

모델: Bedrock 기본 `global.anthropic.claude-sonnet-4-6`, 교체 옵션 행으로
`global.anthropic.claude-sonnet-5` 하나만. 임베딩은 `amazon.titan-embed-text-v2:0`.

## 4. 빌드 워크플로 (반드시 이 순서)

1. 확인: 챕터형인지 캡스톤형인지, 총 시간, Task/Mission 수와 각 시간. 모호하면 질문.
2. 에셋 먼저: 문서에 들어갈 모든 코드(.mjs, .sh, .ts, SKILL.md 등)를 별도 디렉토리에
   실제 파일로 작성하고 컨테이너에서 검증한다. 최소 node --check와 bash -n, 순수 로직은
   단위 테스트 실행, 스크립트는 mock 서버 e2e까지. 검증 안 된 코드는 문서에 싣지 않는다.
3. 조립: assets/lab_head.html(그대로, title만 교체) + 본문(python 생성기에서
   assets/helpers.py의 esc/code/sol/heredoc 사용) + assets/lab_tail.html
   ({{LAB_TITLE}}, {{BASELINE}}, {{TASK_GROUPS}}, {{TASK_COUNT}} 치환).
4. 검증: `python3 assets/qa.py 산출물.html 에셋디렉토리` 가 전부 통과해야 한다
   (HTML 밸런스, JS 구문, 구두점, 금칙어, heredoc 왕복, 1280/420 뷰포트 수납).
5. 픽셀 스팟: wkhtmltoimage 1280 렌더에서 다크 비율 75%+, 우측 3px 오버플로 0.03% 미만,
   신호등 3색 픽셀 존재 확인.
6. 출고: /mnt/user-data/outputs에 `ClaudeCode_<이름>_HandsOnLab.html`로 저장하고,
   포털(index.html)이 있으면 행 추가와 링크 실존 검사까지.

## 5. 흔한 함정

- python 생성기에서 스니펫이 작은따옴표로 끝나면 트리플쿼트와 충돌한다, 개행을 넣어라.
- pre 안 내용은 esc()로만 넣는다. 직접 문자열 결합으로 <, & 를 흘리면 파서가 깨진다.
- 인라인 code에 white-space: nowrap을 주지 마라. 긴 토큰 하나가 페이지 최소폭을 강제해
  좁은 화면에서 우측이 잘린다(헤드 템플릿이 이미 wrap 허용으로 잡혀 있다).
- 표가 많으면 420px 검사가 최소폭 강제로 실패한다. 헤드 템플릿의 .tbl 블록 스크롤
  규칙을 지우지 마라.
- 문서를 고치면 에셋도 같이 고쳐 바이트 일치를 유지하라(반대도 동일).

## 6. 번들 자산

- assets/lab_head.html : 검증된 <head>+CSS 전체(타이포 수정 v1~v5, 신호등, 바 제거 반영).
  첫 줄 title만 교체해 그대로 쓴다. CSS를 새로 쓰지 마라.
- assets/lab_tail.html : footer + 표준 JS. 플레이스홀더 4개 치환.
- assets/helpers.py : esc / code / sol / heredoc 빌더.
- assets/qa.py : 출고 게이트. 통과 전에는 출고하지 않는다.
