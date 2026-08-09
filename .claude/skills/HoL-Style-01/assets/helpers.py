"""HoL-Style-01 본문 생성 헬퍼. python으로 part2(body)를 조립할 때 사용."""
import html

def esc(s):
    return html.escape(s, quote=False)

def code(label, body, kind=""):
    """kind: '' 터미널 / 'prompt' Claude 세션 입력(초록) / 'output' 출력 예시(복사 버튼 없음)"""
    btn = '' if kind == 'output' else '<button class="copy-btn" type="button">복사</button>'
    cls = f' {kind}' if kind else ''
    return (f'  <div class="code-wrap{cls}">\n'
            f'    <div class="code-head"><span class="code-label">{label}</span>{btn}</div>\n'
            f'    <pre><code>{esc(body).rstrip()}</code></pre>\n  </div>\n')

def sol(title, blocks):
    """'막힐 때 열어보기' 접이식 솔루션. blocks는 code() 결과 리스트."""
    return (f'  <details class="solution">\n    <summary>{title}</summary>\n'
            f'    <div class="sol-body">\n{"".join(blocks)}    </div>\n  </details>\n')

def heredoc(path, marker, content, post=""):
    """파일 배치 터미널 블록. marker는 문서 내 유일해야 왕복 검증이 성립."""
    body = f"cat > {path} << '{marker}'\n{content.rstrip()}\n{marker}"
    if post:
        body += "\n" + post
    return body
