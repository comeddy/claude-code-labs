"""HoL-Style-01 QA 파이프라인. 사용: python3 qa.py <lab.html> [에셋디렉토리]
검사: HTML 밸런스, 페이지 JS 구문, 구두점, 금칙어, heredoc 왕복(에셋 디렉토리 지정 시), 렌더 수납."""
import sys, re, html as h, subprocess, os
from html.parser import HTMLParser

doc = open(sys.argv[1]).read()
assets = sys.argv[2] if len(sys.argv) > 2 else None
fail = []

class V(HTMLParser):
    VOID = {'meta','br','hr','img','input','link','area','base','col','embed','source','track','wbr'}
    def __init__(self): super().__init__(convert_charrefs=False); self.stack=[]; self.err=[]
    def handle_starttag(self, t, a):
        if t not in self.VOID: self.stack.append(t)
    def handle_endtag(self, t):
        if not self.stack or self.stack.pop() != t: self.err.append(t)
v = V(); v.feed(doc)
if v.err or v.stack: fail.append(f"HTML 불균형 {v.err[:3]}{v.stack[:3]}")

js = re.findall(r'<script>(.*?)</script>', doc, re.S)
if js:
    open('/tmp/_qa.js','w').write(js[-1])
    if subprocess.run(['node','--check','/tmp/_qa.js'], capture_output=True).returncode:
        fail.append("페이지 JS 구문 오류")

if doc.count(chr(0x2014)): fail.append("em-dash 발견")
if doc.count(chr(0xB7)) and 'Claude account with subscription' not in doc:
    fail.append("가운데점 발견")
for w in ['진행자','옆자리','전원 동시','APPENDIX B','P2P']:
    if w in doc: fail.append(f"금칙어: {w}")

if assets:
    blocks = [h.unescape(re.sub(r'<[^>]+>','',b)) for b in re.findall(r'<pre><code>(.*?)</code></pre>', doc, re.S)]
    def match(orig):
        o = orig.rstrip()
        for b in blocks:
            if b.rstrip() == o: return True
            m = re.search(r"<< '([A-Z]+EOF)'\n(.*?)\n\1", b, re.S)
            if m and m.group(2).rstrip() == o: return True
        return False
    for root, _, files in os.walk(assets):
        for fn in files:
            if not match(open(os.path.join(root, fn)).read()):
                fail.append(f"에셋 불일치: {fn}")

for width in (1280, 420):
    png = f'/tmp/_qa_{width}.png'
    subprocess.run(['xvfb-run','-a','wkhtmltoimage','--width',str(width),'--quality','45',
                    '--enable-local-file-access', sys.argv[1], png],
                   capture_output=True)
    try:
        from PIL import Image
        if Image.open(png).size[0] != width:
            fail.append(f"{width}px 뷰포트 최소폭 강제(수납 실패)")
    except Exception:
        pass

print("QA " + ("실패:\n- " + "\n- ".join(fail) if fail else "전부 통과"))
sys.exit(1 if fail else 0)
