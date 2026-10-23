#!/usr/bin/env python3
"""Wrap each page body in build/pages/*.html with the shared head, navigation and footer.

Each page body file starts with a metadata comment:
<!--meta title="..." desc="..."-->
followed by the HTML that goes inside <main>. Run: python3 build/build.py
"""
import hashlib, html, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGES_DIR = ROOT / "build" / "pages"
DATE = "23 October 2026"
SALT = "oneclicklca-pmm-2026:"
PASSWORD_FILE = ROOT / "build" / ".password"  # not committed; see README

# nav order: (file, nav label)
PAGES = [
    ("overview.html", "Overview"),
    ("role.html", "The Role"),
    ("fit.html", "Fit"),
    ("portfolio.html", "Portfolio"),
    ("demand.html", "Demand Drivers"),
    ("buyers.html", "Buyers"),
    ("segments.html", "Segment Model"),
    ("alternatives.html", "Alternatives"),
    ("positioning.html", "Positioning"),
    ("launch.html", "Launch Playbook"),
    ("enablement.html", "Enablement"),
    ("metrics.html", "Win Rate"),
    ("first-90-days.html", "90 Days"),
    ("ai.html", "AI Workflow"),
    ("cv.html", "CV"),
]

GUARD = ('<script>try{if(sessionStorage.getItem("pw")!=="ok"){document.documentElement.style.visibility="hidden";'
         'location.replace("index.html?next="+encodeURIComponent(location.pathname.split("/").pop()))}}'
         'catch(e){location.replace("index.html")}</script>')

HEAD = """<!doctype html>
<html lang="en-GB">
<head>
{guard}
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex">
<link rel="stylesheet" href="assets/site.css">
<link rel="stylesheet" href="assets/nav.css">
<link rel="stylesheet" href="assets/a11y.css">
<link rel="stylesheet" href="assets/pages.css">
<link rel="stylesheet" href="assets/viz.css">
<script src="assets/viz.js"></script>
<script>try{{var s=localStorage.getItem("theme");if(s==="light"||s==="dark")document.documentElement.setAttribute("data-theme",s)}}catch(e){{}}</script>
<meta name="color-scheme" content="light dark">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 32 32%27%3E%3Crect width=%2732%27 height=%2732%27 rx=%277%27 fill=%27%23007a5e%27/%3E%3C/svg%3E">
</head>
<body>
"""

NAV_JS = ("<script>(function(){var r=document.documentElement,t=document.querySelector('.sitenav .theme');"
          "function cur(){return r.getAttribute('data-theme')||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light')}"
          "function show(){var d=cur()==='dark';t.textContent=d?'Light':'Dark';t.setAttribute('aria-label','Switch to '+(d?'light':'dark')+' mode')}"
          "if(t){t.addEventListener('click',function(){var n=cur()==='dark'?'light':'dark';r.setAttribute('data-theme',n);try{localStorage.setItem('theme',n)}catch(e){}show()});show()}"
          "var b=document.querySelector('.sitenav .menu'),l=document.getElementById('sitelinks');if(!b)return;"
          "b.addEventListener('click',function(){var o=l.classList.toggle('open');b.setAttribute('aria-expanded',o?'true':'false');b.textContent=o?'Close':'Menu';});"
          "l.addEventListener('click',function(e){if(e.target.tagName==='A'){l.classList.remove('open');b.textContent='Menu';b.setAttribute('aria-expanded','false');}});})();</script>")


def nav(current):
    links = "".join(
        f'<a href="{f}"{" aria-current=\"page\"" if f == current else ""}>{html.escape(label)}</a>' for f, label in PAGES)
    return ('<header class="sitenav"><div class="in"><a class="brand" href="overview.html">Arpan Bakshi<span>One Click LCA product marketing</span></a>'
            '<button class="theme" type="button" aria-label="Switch to dark mode">Dark</button>'
            '<button class="menu" type="button" aria-expanded="false" aria-controls="sitelinks">Menu</button>'
            f'<nav class="links" id="sitelinks" aria-label="Site pages">{links}</nav></div></header>' + NAV_JS)


def pager(i):
    parts = []
    if i > 0:
        f, label = PAGES[i - 1]
        parts.append(f'<a class="prev" href="{f}"><small>Previous</small><b>{html.escape(label)}</b></a>')
    if i < len(PAGES) - 1:
        f, label = PAGES[i + 1]
        parts.append(f'<a class="next" href="{f}"><small>Next</small><b>{html.escape(label)}</b></a>')
    return f'<nav class="pager" aria-label="Page navigation">{"".join(parts)}</nav>'


FOOT = ('<footer class="site-foot"><span>Prepared {date} by Arpan Bakshi for the Senior Product Marketing Manager role at One Click LCA. '
        'Independent work from public sources; not produced or endorsed by One Click LCA.</span></footer>')


def build_page(i, fname):
    src = (PAGES_DIR / fname).read_text()
    m = re.match(r'\s*<!--meta title="([^"]*)" desc="([^"]*)"-->\s*', src)
    if not m:
        raise SystemExit(f"{fname}: missing meta comment")
    body = src[m.end():].replace('<div class="tw">', '<div class="tw" tabindex="0" role="region" aria-label="Scrollable table">')
    out = (HEAD.format(guard=GUARD, title=html.escape(m.group(1)), desc=html.escape(m.group(2)))
           + '<a class="skip" href="#main">Skip to content</a>\n' + nav(fname)
           + f'\n<main class="wrap page" id="main" tabindex="-1">\n{body}\n</main>\n'
           + pager(i) + FOOT.format(date=DATE) + "\n</body>\n</html>\n")
    (ROOT / fname).write_text(out)


def build_gate():
    if PASSWORD_FILE.exists():
        pw = PASSWORD_FILE.read_text().strip()
        digest = hashlib.sha256((SALT + pw).encode()).hexdigest()
    else:
        digest = (ROOT / "build" / "gate.hash").read_text().strip()
    (ROOT / "build" / "gate.hash").write_text(digest + "\n")
    ok = ",".join(f'"{f}"' for f, _ in PAGES)
    tpl = (ROOT / "build" / "gate.html").read_text()
    (ROOT / "index.html").write_text(tpl.replace("%HASH%", digest).replace("%SALT%", SALT).replace("%OK%", ok))


if __name__ == "__main__":
    for i, (f, _) in enumerate(PAGES):
        if (PAGES_DIR / f).exists():
            build_page(i, f)
            print("wrote", f)
        else:
            print("missing", f)
    build_gate()
    print("wrote index.html")
