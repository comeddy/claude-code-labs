"""Capstone 5, Playbook Foundry 생성기. HoL-Style-01 규격."""
import pathlib
import sys

BASE = pathlib.Path(__file__).resolve().parent
SKILL = pathlib.Path('/home/ec2-user/2nd-claude-cdoe-workshop/.claude/skills/HoL-Style-01/assets')
sys.path.insert(0, str(SKILL))
from helpers import esc, code, sol, heredoc  # noqa: E402

A = BASE / 'assets'
asset = lambda name: (A / name).read_text()

TITLE = 'Capstone 5, Playbook Foundry - Claude Code Deep Dive Workshop'
head = SKILL.joinpath('lab_head.html').read_text().replace(
    '<title>Capstone Hands-on Lab - Claude Code Deep Dive Workshop</title>',
    f'<title>{TITLE}</title>')
if TITLE not in head:
    raise SystemExit('title swap failed')

tail = SKILL.joinpath('lab_tail.html').read_text()
tail = tail.replace('{{LAB_TITLE}}', 'Claude Code Deep Dive Workshop, Capstone 5')
tail = tail.replace('{{BASELINE}}', 'Claude Code 2.1.x + MkDocs Material 9.x + Python 3.9+, 원작 pai-playbook, 2026.08')
tail = tail.replace('{{TASK_GROUPS}}', '{ m0:["m0"], m1:["m1"], m2:["m2a","m2b"], m3:["m3a","m3b"], m4:["m4"], m5:["m5"] }')
tail = tail.replace('{{TASK_COUNT}}', '6')

body = []
w = body.append

# ---------------------------------------------------------------- hero
w('''<body>

<header class="hero">
  <span class="eyebrow">CAPSTONE 5 / PLAYBOOK FOUNDRY / 135 MIN</span>
  <h1>내 기술분야 플레이북, 파운드리</h1>
  <div class="subtitle">신호 필터 → 페이지 생성 → 신선도 게이트 → 출고, 스스로 안 낡는 지식 자산</div>
  <p class="lede">
    내가 가장 자주 질문받는 기술분야를 하나 골라, <strong>검증 우선(THE FILTER) 큐레이션 방법론</strong>으로
    나만의 플레이북 사이트를 만듭니다. Claude Code가 마스터 프롬프트 하나로 페이지를 규격대로 찍어내고,
    신선도 메타데이터와 출고 게이트가 문서가 낡는 것을 감시합니다. 실존 프로젝트
    <a href="https://comeddy.github.io/pai-playbook/" style="color:#c9a2ff">pai-playbook</a>(Physical AI Playbook,
    4개 언어 운영)의 골격을 135분 스코프로 압축했습니다. API 키가 필요 없고, 로컬에서 완결됩니다.
  </p>
  <div class="hero-meta">
    <span>소요 시간 <strong>135분</strong></span>
    <span>미션 <strong>5개 + 피날레</strong></span>
    <span>산출물 <strong>출고 게이트를 통과한 내 도메인 플레이북</strong></span>
    <span>Update <strong>2026.08</strong></span>
  </div>
</header>

<nav class="timeline" aria-label="미션 타임라인">
  <div class="timeline-inner">
    <span class="timeline-label">진행 <strong id="progress-count">0/6</strong></span>
    <div class="segments" id="segments">
      <button class="seg" data-task="m0" style="flex:10" title="M0 사전 준비, 10분"><span class="fill"></span><span class="seg-txt">M0 준비</span></button>
      <button class="seg" data-task="m1" style="flex:25" title="M1 도메인과 마스터 프롬프트, 25분"><span class="fill"></span><span class="seg-txt">M1 마스터 프롬프트</span></button>
      <button class="seg" data-task="m2" style="flex:35" title="M2 뼈대와 다섯 페이지, 35분"><span class="fill"></span><span class="seg-txt">M2 페이지</span></button>
      <button class="seg" data-task="m3" style="flex:30" title="M3 신선도 게이트, 30분"><span class="fill"></span><span class="seg-txt">M3 신선도</span></button>
      <button class="seg" data-task="m4" style="flex:20" title="M4 출고 게이트, 20분"><span class="fill"></span><span class="seg-txt">M4 출고 게이트</span></button>
      <button class="seg" data-task="m5" style="flex:15" title="M5 피날레, THE FILTER 실사격, 15분"><span class="fill"></span><span class="seg-txt">M5 피날레</span></button>
    </div>
    <span class="timeline-label">135 min</span>
  </div>
</nav>

<div class="layout">

<aside class="sidenav" aria-label="미션 목차">
  <div class="nav-title">MISSIONS / 135분</div>
  <a href="#brief" data-nav="brief"><span class="dot"></span>브리핑<span class="nav-time"></span></a>
  <a href="#m0" data-nav="m0"><span class="dot"></span>M0 사전 준비<span class="nav-time">10분</span></a>
  <a href="#m1" data-nav="m1"><span class="dot"></span>M1 마스터 프롬프트<span class="nav-time">25분</span></a>
  <a href="#m2" data-nav="m2"><span class="dot"></span>M2 뼈대와 페이지<span class="nav-time">35분</span></a>
  <a href="#m3" data-nav="m3"><span class="dot"></span>M3 신선도 게이트<span class="nav-time">30분</span></a>
  <a href="#m4" data-nav="m4"><span class="dot"></span>M4 출고 게이트<span class="nav-time">20분</span></a>
  <a href="#m5" data-nav="m5"><span class="dot"></span>M5 피날레<span class="nav-time">15분</span></a>
  <a href="#opt-pages" data-nav="opt-pages"><span class="dot"></span>OPT 웹 공개<span class="nav-time">+15분</span></a>
  <a href="#appx" data-nav="appx"><span class="dot"></span>부록<span class="nav-time"></span></a>
  <a href="#wrapup" data-nav="wrapup"><span class="dot"></span>마무리<span class="nav-time"></span></a>
</aside>

<main>
''')

# ---------------------------------------------------------------- brief
w('''<section class="task" id="brief">
  <div class="task-head"><span class="task-num">MISSION BRIEFING</span><h2>지식을 제품처럼 출고하는 법</h2><span class="time-badge">숙지</span></div>
  <p class="task-goal">
    다른 캡스톤과 같은 기조입니다: <strong>빈 폴더에서 Claude Code와 함께</strong> 설계하고 미션 단위로 빌드합니다.
    다른 점이 하나 있습니다. 이번 산출물은 서비스가 아니라 <strong>지식 자산</strong>이고,
    적은 코드로 콘텐츠의 품질과 신선도를 구조적으로 강제하는 것이 미션입니다.
  </p>
''')
w(code('파이프라인, 이 캡스톤이 만드는 것', '''후보 항목 (뉴스, 논문, 릴리스 노트, 데모)
        │
        ▼
  THE FILTER (4기준 중 2개 이상) ──미달──▶ docs/radar.md (한 줄 대기열)
        │ 통과
        ▼
  필러 페이지 5장 (성숙도 라벨 + 다음 액션 + front matter 메타데이터)
        │
        ▼
  출고 게이트 ship.sh
    [1/3] check_freshness.py   [2/3] 성숙도 라벨 lint   [3/3] mkdocs build --strict
        │ 전부 통과
        ▼
  site/ (정적 사이트, 어디에나 배포 가능)''', kind='output'))
w('''  <p class="body">지키는 규칙은 세 줄입니다.</p>
  <table class="tbl">
    <tr><th>규칙</th><th>의미</th></tr>
    <tr><td>검증 없이 본문 없음</td><td>THE FILTER 미달 후보는 radar 대기열에 한 줄로만 남는다</td></tr>
    <tr><td>모든 항목은 다음 액션으로 끝난다</td><td>개념 설명으로 끝나는 항목은 미완성이다</td></tr>
    <tr><td>낡음은 게이트가 감시한다</td><td>모든 페이지에 owner, updated, volatility를 붙이고 기한을 스크립트로 판정한다</td></tr>
  </table>

  <div class="step-title"><span class="step-no">L</span>학습 목표, Level 200</div>
  <p class="body">이 캡스톤을 마치면 다음 네 가지를 <strong>설명할 수 있고, 다시 만들 수 있습니다</strong>.</p>
  <table class="tbl">
    <tr><th>목표</th><th>검증되는 순간</th></tr>
    <tr><td>정보 더미를 신호로 거르는 포함 기준(THE FILTER)을 설계하는 법</td><td>M1에서 4개 기준을 내 도메인의 언어로 확정할 때</td></tr>
    <tr><td>마스터 프롬프트 하나로 페이지를 규격대로 찍어내는 법</td><td>M2에서 다섯 페이지가 같은 골격(L0/Top3/L1 표)으로 나올 때</td></tr>
    <tr><td>메타데이터로 문서의 낡음을 감시하는 법</td><td>M3에서 과거 날짜 페이지가 REVIEW NEEDED로 잡힐 때</td></tr>
    <tr><td>품질 규율을 스크립트 게이트로 강제하는 법</td><td>M4에서 불량 페이지가 출고를 막는 것을 관측할 때</td></tr>
  </table>
  <div class="callout tip">
    <span class="co-title">원작이 있습니다</span>
    이 캡스톤의 골격은 실제 운영 중인 <a href="https://comeddy.github.io/pai-playbook/" style="color:#c9a2ff">Physical AI Playbook</a>에서
    왔습니다. 원작은 여기에 4개 언어 번역 드리프트 감지(ko_hash), 주간 자동 레이더 스캔, CI 배지 주입까지 얹어
    운영합니다. 오늘 만드는 것은 그 심장부인 <strong>필터, 규격, 게이트</strong>입니다.
  </div>
</section>
''')

# ---------------------------------------------------------------- m0
w('''<section class="task" id="m0">
  <div class="task-head"><span class="task-num">MISSION 00</span><h2>사전 준비, 도구와 원작 견학</h2><span class="time-badge">10분</span></div>
  <p class="task-goal">이 캡스톤은 <strong>API 키가 필요 없습니다</strong>. Python 가상환경과 MkDocs만 준비하면 끝입니다.</p>

  <div class="step-title"><span class="step-no">1</span>작업 디렉토리와 가상환경</div>
''')
w(code('Terminal, 전체 복사', '''mkdir -p ~/capstone/capstone-5 && cd ~/capstone/capstone-5
python3 -m venv .venv && source .venv/bin/activate
pip -q install mkdocs-material pytest
mkdocs --version'''))
w(code('출력 예시', 'mkdocs, version 1.6.1 from .../capstone-5/.venv/... (Python 3.9)', kind='output'))
w('''  <div class="callout warn">
    <span class="co-title">이후 모든 터미널은 이 가상환경에서</span>
    새 터미널을 열었다면 먼저 <code class="inline">cd ~/capstone/capstone-5 &amp;&amp; source .venv/bin/activate</code>.
    <code class="inline">mkdocs: command not found</code>가 보이면 십중팔구 활성화를 빼먹은 것입니다.
  </div>

  <div class="step-title"><span class="step-no">2</span>원작 견학, 5분</div>
  <p class="body"><a href="https://comeddy.github.io/pai-playbook/" style="color:#c9a2ff">comeddy.github.io/pai-playbook</a>을
  열고 세 가지만 관찰하세요. 오늘 전부 직접 만들 것들입니다.</p>
  <table class="tbl">
    <tr><th>관찰 포인트</th><th>어디서</th></tr>
    <tr><td>항목마다 붙은 성숙도 라벨 🟢🟡🔵⚪</td><td>아무 필러 페이지의 표</td></tr>
    <tr><td>본문에 못 들어온 후보들의 대기열</td><td>Radar 페이지</td></tr>
    <tr><td>페이지마다 다른 리뷰 주기(volatility)</td><td>페이지 하단 메타데이터</td></tr>
  </table>
  <div class="checkpoint">
    <div class="cp-title">CHECKPOINT</div>
    <label class="cp-item"><input type="checkbox" data-cp="m0"><span>mkdocs --version이 버전을 출력했고, 가상환경이 활성화되어 있습니다</span></label>
  </div>
</section>
''')

# ---------------------------------------------------------------- m1
w('''<section class="task" id="m1">
  <div class="task-head"><span class="task-num">MISSION 01</span><h2>도메인 선정과 마스터 프롬프트</h2><span class="time-badge">25분</span></div>
  <p class="task-goal">플레이북의 헌법을 만듭니다: 도메인, 독자, 필러 5개, 그리고 <strong>THE FILTER 4기준</strong>.</p>
  <p class="body" style="color:#A6ABBE">이 미션의 바탕 학습: <a href="ClaudeCode_Ch1_HandsOnLab.html" style="color:#c9a2ff">Ch1</a>의 세션 운용과
  <a href="ClaudeCode_Capstone_Setup.html" style="color:#c9a2ff">Capstone Setup</a>의 superpowers 워크플로.</p>

  <div class="step-title"><span class="step-no">1</span>도메인 고르기, 3분 안에</div>
  <p class="body">세 가지가 겹치는 분야가 정답입니다: ① 내가 실제로 질문받는 분야
  ② 후보 항목이 20개 이상 바로 떠오르는 분야 ③ 6개월이면 낡는 정보가 섞여 있는 분야.
  마땅치 않으면 아래에서 하나를 가져가세요.</p>
  <table class="tbl">
    <tr><th>도메인 예시</th><th>필러가 될 만한 축</th><th>독자 예시</th></tr>
    <tr><td>GenAI 애플리케이션 보안</td><td>프롬프트 인젝션 방어, 데이터 유출 통제, 평가와 레드팀, 가드레일 운영, 규제 대응</td><td>보안 검토를 받는 개발팀</td></tr>
    <tr><td>Kubernetes 운영(EKS)</td><td>업그레이드 전략, 오토스케일링, 비용 최적화, 관측성, 장애 대응</td><td>플랫폼 엔지니어</td></tr>
    <tr><td>데이터 엔지니어링</td><td>수집 파이프라인, 테이블 포맷, 오케스트레이션, 품질 게이트, 거버넌스</td><td>분석 조직의 DE</td></tr>
    <tr><td>프론트엔드 성능</td><td>Core Web Vitals, 번들링, 렌더링 전략, 이미지와 폰트, 계측</td><td>웹 서비스 프론트엔드 팀</td></tr>
  </table>

  <div class="step-title"><span class="step-no">2</span>마스터 프롬프트 골격 배치</div>
  <p class="body">원작에서 가져온 골격입니다. <code class="inline">《...》</code> 부분만 내 도메인으로 채우면 됩니다.</p>
''')
w(code('Terminal (~/capstone/capstone-5), 전체 복사',
       heredoc('PROMPT.md', 'PSKEOF', asset('PROMPT.md'))))
w('''  <div class="step-title"><span class="step-no">3</span>Claude와 함께 《》 채우기</div>
''')
w(code('Terminal (~/capstone/capstone-5)', 'claude'))
w(code('Claude 세션 입력, 전체 복사', '''/superpowers:brainstorming PROMPT.md를 읽어라. 나와 함께 《...》 placeholder를 전부 채워
"내 기술분야 플레이북"의 마스터 프롬프트를 완성하자.
1) 먼저 내게 도메인과 독자를 물어라. 내 답을 그대로 쓰지 말고 더 좁고 구체적으로 다듬어 제안하라
2) 필러 5개: 상호배타적이고 도메인 전체를 덮게. 각 필러에 한 줄 정의를 붙여 내 확인을 받아라
3) THE FILTER 4기준(ⓐ검증 ⓑ매핑 ⓒ수요 ⓓ성숙)을 내 도메인의 언어로 다시 써라.
   예: "production 검증"이 이 도메인에서 정확히 무엇을 뜻하는지
4) 성숙도 라벨 4종과 페이지 규격(섹션 6)은 그대로 유지하라
5) 확정되면 PROMPT.md를 덮어써 저장하라. 《》가 하나도 남지 않아야 완료다
결정이 필요하면 이 범위 안에서 최소한으로만 물어봐.''', kind='prompt'))
w(code('Terminal, 완료 검사', "grep -c '《' PROMPT.md   # 0이어야 완료"))
w('''  <div class="callout tip">
    <span class="co-title">여기서 시간을 쓰는 게 남는 장사</span>
    THE FILTER가 느슨하면 M5에서 모든 후보가 통과해 버려 필터가 무의미해집니다.
    "데모 영상만으로는 불충분" 같은 <strong>탈락 조건</strong>이 기준마다 한 줄씩 있는지 확인하세요.
  </div>
  <div class="checkpoint">
    <div class="cp-title">DEFINITION OF DONE</div>
    <label class="cp-item"><input type="checkbox" data-cp="m1"><span>PROMPT.md에 《》가 0개이고, 필러 5개와 FILTER 4기준이 내 도메인의 언어로 적혀 있습니다</span></label>
  </div>
</section>
''')

# ---------------------------------------------------------------- m2
w('''<section class="task" id="m2">
  <div class="task-head"><span class="task-num">MISSION 02</span><h2>뼈대와 다섯 페이지</h2><span class="time-badge">35분</span></div>
  <p class="task-goal">사이트 뼈대를 깔고, 마스터 프롬프트로 필러 페이지 5장을 <strong>같은 규격으로</strong> 찍어냅니다.</p>

  <div class="step-title"><span class="step-no">1</span>뼈대 배치, 파일 두 장</div>
  <p class="body">파일명은 규격입니다: 필러 페이지는 <code class="inline">p1.md</code>부터
  <code class="inline">p5.md</code>, 대기열은 <code class="inline">radar.md</code>.
  M3와 M4의 게이트 스크립트가 이 이름을 봅니다.</p>
''')
w(code('Terminal 1/2, 전체 복사',
       'mkdir -p docs scripts tests\n' + heredoc('mkdocs.yml', 'MKDEOF', asset('mkdocs.yml'))))
w(code('Terminal 2/2, 전체 복사',
       heredoc('docs/index.md', 'IDXEOF', asset('index.md'))))
w('''  <div class="step-title"><span class="step-no">2</span>페이지 단위 생성, 원작의 리듬</div>
  <p class="body">원작 마스터 프롬프트의 사용법 그대로입니다: <strong>한 번에 전체를 생성하지 않고,
  페이지 단위로 생성하고 검토합니다</strong>. LLM 콘텐츠 파이프라인의 기본 리듬입니다.</p>
''')
w(code('Claude 세션 입력, 전체 복사', '''PROMPT.md를 읽고 그 규격을 시스템 지침으로 삼아라. 필러 페이지를 생성한다.
1) docs/p1.md부터 docs/p5.md까지 다섯 장, mkdocs.yml nav 순서대로 한 장씩:
   내가 "다음"이라고 하면 다음 페이지로 넘어간다. 각 장의 규격(PROMPT.md 섹션 6):
   - 첫머리 front matter: owner는 내 이름, updated는 오늘(YYYY-MM-DD),
     volatility는 페이지 성격에 맞게 1m/3m/6m 중 택일하고 이유를 한 줄 말하라
   - L0 TL;DR(2문장 이내) → 자주 받는 질문 Top 3 → L1 표(항목/성숙도/다음 액션, 4~6행)
   - 성숙도는 반드시 🟢 GA / 🟡 Preview / 🔵 Research-only / ⚪ Hype 중 하나
   - L2 심화는 details 태그 접기로 1~2개만
2) docs/radar.md: front matter(volatility 1m) + 표 헤더(후보/판정/근거)만, 행은 M5에서 채운다
3) 다섯 장이 끝나면 mkdocs.yml nav의 "필러 n" 라벨과 index.md의 필러 표를 실제 이름으로 갱신하라
사실 확신이 없는 항목은 지어내지 말고 성숙도를 ⚪로 적고 "검증 필요"를 다음 액션에 남겨라.''', kind='prompt'))
w('''  <div class="callout warn">
    <span class="co-title">환각을 규격으로 눌러 두기</span>
    마지막 줄이 이 미션의 안전벨트입니다. 플레이북은 참조 자산이라 <strong>틀린 확신이 빈칸보다 나쁩니다</strong>.
    생성된 표를 훑으며 낯선 항목이 있으면 성숙도가 ⚪인지, 다음 액션에 검증 경로가 있는지 확인하세요.
  </div>

  <div class="step-title"><span class="step-no">3</span>strict 빌드와 첫 화면</div>
''')
w(code('Terminal, 전체 복사', 'mkdocs build --strict && mkdocs serve'))
w(code('출력 예시', '''INFO    -  Documentation built in 0.42 seconds
INFO    -  [15:30:00] Serving on http://127.0.0.1:8000/''', kind='output'))
w('''  <p class="body">브라우저에서 <code class="inline">http://127.0.0.1:8000</code>을 엽니다.
  좌측 내비게이션에 필러 5개와 Radar 대기열이 보이면 성공입니다. 확인 후 <code class="inline">Ctrl+C</code>로 serve를 멈추세요.</p>
  <div class="callout tip">
    <span class="co-title">--strict가 하는 일</span>
    nav에 있는데 파일이 없거나, 깨진 내부 링크가 있으면 <strong>빌드 자체가 실패</strong>합니다.
    원작은 이 옵션 하나로 "죽은 링크가 라이브 사이트에 나가는 사고"를 구조적으로 없앴습니다.
  </div>
  <div class="checkpoint">
    <div class="cp-title">DEFINITION OF DONE</div>
    <label class="cp-item"><input type="checkbox" data-cp="m2a"><span>mkdocs build --strict가 에러 없이 통과했습니다</span></label>
    <label class="cp-item"><input type="checkbox" data-cp="m2b"><span>브라우저에서 필러 5개와 Radar 대기열, 성숙도 라벨이 보입니다</span></label>
  </div>
</section>
''')

# ---------------------------------------------------------------- m3
w('''<section class="task" id="m3">
  <div class="task-head"><span class="task-num">MISSION 03</span><h2>신선도 게이트, 테스트 먼저</h2><span class="time-badge">30분</span></div>
  <p class="task-goal">모든 페이지의 <code class="inline">updated + volatility</code>로 리뷰 기한을 판정하는
  스크립트를 <strong>TDD로</strong> 만듭니다. 스펙은 테스트가 말합니다.</p>
  <p class="body" style="color:#A6ABBE">이 미션의 바탕 학습: <a href="ClaudeCode_Ch2_HandsOnLab.html" style="color:#c9a2ff">Ch2</a>의
  superpowers:test-driven-development.</p>

  <div class="step-title"><span class="step-no">1</span>스펙 배치, RED 확인</div>
  <p class="body">테스트 파일이 곧 요구사항 문서입니다. 아직 구현이 없으니 <strong>실패해야 정상</strong>입니다.</p>
''')
w(code('Terminal, 전체 복사',
       heredoc('tests/test_freshness.py', 'TSTEOF', asset('test_freshness.py'),
               post='.venv/bin/python -m pytest tests/ -q')))
w(code('출력 예시 (RED, 아직 구현이 없다)', '''ERROR tests/test_freshness.py - FileNotFoundError: [Errno 2] No such file or directory:
'.../capstone-5/scripts/check_freshness.py'.''', kind='output'))
w('''  <div class="step-title"><span class="step-no">2</span>Claude에게 구현을 맡기기, GREEN까지</div>
''')
w(code('Claude 세션 입력, 전체 복사', '''/superpowers:test-driven-development tests/test_freshness.py를 읽어라. 이 테스트 6개를 전부
통과하는 scripts/check_freshness.py를 구현하라.
1) 표준 라이브러리만 사용. 함수는 테스트가 부르는 그대로: parse_meta(text), classify(meta, today),
   scan(docs_dir, today)
2) volatility 기한: 1m=30일, 3m=90일, 6m=180일. updated에서 기한을 넘기면 "review"
3) scan은 페이지별 판정 표를 출력하고 exit code를 돌려준다:
   메타데이터 누락이 하나라도 있으면 2, 아니면 0 (review는 경고일 뿐 통과다)
4) __main__에서는 docs/를 스캔해 sys.exit로 끝낸다
5) 구현 후 .venv/bin/python -m pytest tests/ -q 로 6 passed를 보여라''', kind='prompt'))
w(code('출력 예시 (GREEN)', '''......                                                                   [100%]
6 passed in 0.01s''', kind='output'))
w('''  <div class="callout tip">
    <span class="co-title">왜 "review는 통과"인가</span>
    낡음(review)은 <strong>사람이 검토할 일</strong>이지 출고를 막을 일이 아닙니다. 반면 메타데이터 누락은
    감시 자체가 불가능한 상태라 차단합니다. 원작도 같은 정책입니다: 낡음은 배지로 경고하고, 메타데이터가 없으면 CI가 막습니다.
  </div>

  <div class="step-title"><span class="step-no">3</span>낡음 실험, 시간을 감아 보기</div>
''')
w(code('Terminal, 전체 복사', '''sed -i 's/^updated: .*/updated: 2026-01-05/' docs/p1.md
python3 scripts/check_freshness.py
sed -i "s/^updated: .*/updated: $(date +%F)/" docs/p1.md
python3 scripts/check_freshness.py'''))
w(code('출력 예시 (첫 실행은 REVIEW, 둘째는 전부 OK)', '''  index.md  OK
  p1.md     REVIEW NEEDED
  p2.md     OK''', kind='output'))
w(sol('막힐 때 열어보기, 완성본 scripts/check_freshness.py',
      [code('scripts/check_freshness.py', asset('check_freshness.py'))]))
w('''  <div class="checkpoint">
    <div class="cp-title">DEFINITION OF DONE</div>
    <label class="cp-item"><input type="checkbox" data-cp="m3a"><span>pytest 6개가 전부 통과했습니다(GREEN)</span></label>
    <label class="cp-item"><input type="checkbox" data-cp="m3b"><span>과거 날짜로 바꾼 페이지가 REVIEW NEEDED로 잡히고, 되돌리니 OK가 됐습니다</span></label>
  </div>
</section>
''')

# ---------------------------------------------------------------- m4
w('''<section class="task" id="m4">
  <div class="task-head"><span class="task-num">MISSION 04</span><h2>출고 게이트, 규율의 자동화</h2><span class="time-badge">20분</span></div>
  <p class="task-goal">신선도, 라벨 lint, strict 빌드를 한 줄로 묶습니다. <strong>셋 중 하나라도 실패하면 출고가 없습니다</strong>.</p>

  <div class="step-title"><span class="step-no">1</span>게이트 배치</div>
''')
w(code('Terminal, 전체 복사',
       heredoc('ship.sh', 'SHPEOF', asset('ship.sh'), post='chmod +x ship.sh')))
w('''  <div class="step-title"><span class="step-no">2</span>통과 확인</div>
''')
w(code('Terminal', './ship.sh'))
w(code('출력 예시', '''[1/3] 신선도 메타데이터
  index.md  OK
  p1.md     OK
  ...
[2/3] 성숙도 라벨 lint
[3/3] mkdocs build --strict
INFO    -  Documentation built in 0.41 seconds
GATE PASS, site/ 준비 완료''', kind='output'))
w('''  <div class="step-title"><span class="step-no">3</span>실패 주입, 게이트가 정말 막는지</div>
  <p class="body">라벨도 메타데이터도 없는 불량 페이지를 심고 게이트에 태워 봅니다.
  파일명이 <code class="inline">p9.md</code>인 이유: 라벨 lint가 <code class="inline">docs/p*.md</code>를 보기 때문입니다.</p>
''')
w(code('Terminal, 전체 복사', '''echo "# 라벨도 메타데이터도 없는 페이지" > docs/p9.md
./ship.sh; echo "exit=$?"
rm docs/p9.md
./ship.sh; echo "exit=$?"'''))
w(code('출력 예시 (차단 후 복구)', '''[1/3] 신선도 메타데이터
  p9.md     MISSING META
exit=2
...
GATE PASS, site/ 준비 완료
exit=0''', kind='output'))
w('''  <div class="callout tip">
    <span class="co-title">set -euo pipefail 한 줄의 힘</span>
    ship.sh의 둘째 줄이 게이트의 본체입니다. 어느 단계든 0이 아닌 exit code를 내면
    그 자리에서 멈추고, GATE PASS는 영원히 출력되지 않습니다. 규율을 기억력이 아니라 스크립트에 맡기는 방법입니다.
  </div>
  <div class="checkpoint">
    <div class="cp-title">DEFINITION OF DONE</div>
    <label class="cp-item"><input type="checkbox" data-cp="m4"><span>불량 페이지가 exit=2로 차단되는 것과, 제거 후 GATE PASS를 둘 다 관측했습니다</span></label>
  </div>
</section>
''')

# ---------------------------------------------------------------- m5
w('''<section class="task" id="m5">
  <div class="task-head"><span class="task-num">MISSION 05</span><h2>피날레, THE FILTER 실사격</h2><span class="time-badge">15분</span></div>
  <p class="task-goal">진짜 후보들을 필터에 태웁니다. <strong>떨어지는 후보가 있어야 필터입니다</strong>.</p>

  <div class="step-title"><span class="step-no">1</span>후보 6건 판정</div>
''')
w(code('Claude 세션 입력, 전체 복사', '''내 도메인에서 최근 1년 사이 화제가 된 후보 항목 6건을 뽑아라. 조건:
절반은 데모나 발표만 화려하고 실전 검증이 부족한 것으로 일부러 섞어라.
1) 후보 6건을 PROMPT.md의 THE FILTER 4기준(ⓐⓑⓒⓓ)으로 판정하는 표를 보여라:
   후보 / ⓐ / ⓑ / ⓒ / ⓓ / 판정(승급 또는 대기). 2개 미만 충족이면 대기다
2) 대기 후보들은 docs/radar.md 표에 근거 한 줄과 함께 추가하라
3) 승급 후보 중 1건을 골라 해당 필러 페이지 L1 표에 추가하라:
   성숙도 라벨과 다음 액션 필수, 그 페이지의 updated를 오늘로 갱신
4) 확신이 없는 판정은 그렇다고 말하고 보수적으로(대기 쪽으로) 판정하라''', kind='prompt'))
w('''  <div class="callout warn">
    <span class="co-title">전원 승급은 실패 신호</span>
    6건이 모두 승급했다면 필터가 느슨한 것입니다. M1로 돌아가 기준에 탈락 조건을 한 줄씩 추가하고
    다시 판정하세요. 원작 운영에서도 후보의 절반 이상은 Radar에 머뭅니다.
  </div>

  <div class="step-title"><span class="step-no">2</span>최종 출고</div>
''')
w(code('Terminal', './ship.sh'))
w('''  <p class="body">GATE PASS가 뜨면 <code class="inline">site/</code>에 완성된 정적 사이트가 있습니다.
  <code class="inline">mkdocs serve</code>로 마지막으로 열어 오늘 승급한 항목을 눈으로 확인하세요.</p>
  <div class="checkpoint">
    <div class="cp-title">DEFINITION OF DONE</div>
    <label class="cp-item"><input type="checkbox" data-cp="m5"><span>radar.md에 대기 후보가 근거와 함께 남았고, 본문에 오늘 승급한 항목 1건이 있으며, ship.sh가 GATE PASS로 끝났습니다</span></label>
  </div>
</section>
''')

# ---------------------------------------------------------------- option
w('''<section class="task" id="opt-pages">
  <div class="task-head"><span class="task-num">OPTION</span><h2>웹 공개, GitHub Pages</h2><span class="time-badge">+15분</span></div>
  <p class="task-goal">출고 게이트를 통과한 사이트를 진짜 URL로 만듭니다. GitHub 계정과 gh CLI 인증이 있는 경우에만 진행하세요.</p>
''')
w(code('Terminal, 전체 복사', '''cd ~/capstone/capstone-5
printf '.venv/\\nsite/\\n' > .gitignore
git init -b main && git add -A && git commit -m "my playbook v1"
gh repo create my-playbook --public --source . --push
mkdocs gh-deploy --force'''))
w('''  <p class="body">끝나면 <code class="inline">https://&lt;내 GitHub 계정&gt;.github.io/my-playbook/</code>에서
  전 세계 어디서나 내 플레이북이 열립니다. 이 랩 문서 자체도 같은 방식으로 배포되어 있습니다.</p>
  <div class="callout tip">
    <span class="co-title">원작의 다음 단계가 궁금하다면</span>
    push마다 게이트를 CI로 돌리고 싶다면 GitHub Actions에 ship.sh를 그대로 올리면 됩니다.
    원작 리포(<a href="https://github.com/comeddy/pai-playbook" style="color:#c9a2ff">comeddy/pai-playbook</a>)의
    workflows 디렉토리가 살아 있는 예제입니다.
  </div>
  <div class="checkpoint">
    <div class="cp-title">OPTION DONE, 진행률 미집계</div>
    <label class="cp-item"><input type="checkbox" data-cp="optp"><span>공개 URL에서 내 플레이북이 열립니다</span></label>
  </div>
</section>
''')

# ---------------------------------------------------------------- appendix
w('''<section class="task" id="appx">
  <div class="task-head"><span class="task-num">부록</span><h2>컷라인과 트러블슈팅</h2><span class="time-badge">참고</span></div>
  <p class="body"><strong>시간이 부족하면 이 순서로 잘라내세요.</strong> 피날레(M5)는 남기는 것이 원칙입니다.</p>
  <table class="tbl">
    <tr><th>상황</th><th>컷라인</th></tr>
    <tr><td>20분 부족</td><td>M3 step 3(낡음 실험)과 M4 step 3(실패 주입)을 건너뛰고 통과 경로만 확인</td></tr>
    <tr><td>40분 부족</td><td>위에 더해, 필러를 3장으로 축소(mkdocs.yml nav에서 p4/p5 제거, index.md 표도 3행으로) 후 M5 후보는 3건만</td></tr>
    <tr><td>60분 부족</td><td>위에 더해, M3 구현을 솔루션 접기에서 복사해 배치하고 pytest 통과만 확인</td></tr>
  </table>
  <p class="body"><strong>막히면 여기부터.</strong></p>
  <table class="tbl">
    <tr><th>증상</th><th>원인</th><th>처방</th></tr>
    <tr><td>mkdocs: command not found</td><td>가상환경 비활성</td><td><code class="inline">cd ~/capstone/capstone-5 &amp;&amp; source .venv/bin/activate</code></td></tr>
    <tr><td>strict 빌드 실패: nav 파일 없음</td><td>페이지 파일명이 규격과 다름</td><td>docs/에 p1.md~p5.md, radar.md가 정확히 있는지 확인</td></tr>
    <tr><td>pytest가 ERROR로 시작</td><td>M3 step 1 직후라면 정상(RED)</td><td>구현 후에도 그렇다면 scripts/check_freshness.py 경로와 철자 확인</td></tr>
    <tr><td>8000 포트가 이미 사용 중</td><td>이전 serve가 살아 있음</td><td><code class="inline">mkdocs serve -a 127.0.0.1:8001</code>로 우회</td></tr>
    <tr><td>PROMPT.md에 《》가 남음</td><td>M1 세션이 일부만 채움</td><td>M1 step 3 프롬프트를 다시 실행, <code class="inline">grep -c '《' PROMPT.md</code>가 0이어야</td></tr>
    <tr><td>게이트 [2/3]에서 라벨 없음</td><td>페이지에 성숙도 이모지가 없음</td><td>해당 페이지 L1 표의 성숙도 열에 🟢🟡🔵⚪ 중 하나를 채움</td></tr>
  </table>
</section>
''')

# ---------------------------------------------------------------- wrapup
w('''<section class="wrapup" id="wrapup">
  <h2>미션 종료</h2>
  <p class="sub">필터가 품질을 만들고, 메타데이터가 신선도를 지키고, 게이트가 규율을 강제합니다. 지식을 제품처럼 출고하는 문법입니다.</p>
  <table class="tbl">
    <tr><th>가져가는 것</th><th>내용</th></tr>
    <tr><td>THE FILTER</td><td>포함 기준을 먼저 못 박으면 콘텐츠 품질이 그때그때의 프롬프트가 아니라 구조에서 나온다</td></tr>
    <tr><td>자기 갱신성</td><td>owner, updated, volatility 세 줄이 문서를 "낡으면 스스로 알리는" 자산으로 바꾼다</td></tr>
    <tr><td>출고 게이트</td><td>기억에 맡긴 규율은 무너진다, 스크립트가 강제하는 규율만 살아남는다</td></tr>
    <tr><td>이식처</td><td>팀 위키, 온보딩 문서, 기술 레이더, 사내 표준 문서. 지식 자산이면 같은 골격이 통한다</td></tr>
  </table>
  <div class="next-box">
    <div>
      <div class="nx-label">NEXT</div>
      <h3>포털로</h3>
      <p>다른 캡스톤(1 Press Start, 2 Market Desk on Web, 3 Frame It, 4 Trend Radar)도 같은 리듬입니다.
      <a href="index.html" style="color:#c9a2ff">워크샵 포털</a>에서 다음 미션을 고르세요.</p>
    </div>
  </div>
</section>

</main>
</div>
''')

out = head + '\n' + ''.join(body) + tail
dest = BASE / 'ClaudeCode_Capstone5_HandsOnLab.html'
dest.write_text(out)
print(f'written: {dest} ({len(out)} bytes)')
