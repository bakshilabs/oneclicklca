#!/usr/bin/env python3
"""Wrap each page body in build/pages/*.html with the shared head, navigation and footer.

Each page body file starts with a metadata comment:
<!--meta title="..." desc="..."-->
followed by the HTML that goes inside <main>. Run: python3 build/build.py
"""
import hashlib, html, pathlib, re, shutil

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGES_DIR = ROOT / "build" / "pages"
DATE = "23 October 2026"
SALT = "oneclicklca-pmm-2026:"
PASSWORD_FILE = ROOT / "build" / ".password"  # not committed; see README
OUT = ROOT / "docs"  # the published site: pages, index.html and assets only

# nav order: (file, nav label, group). Meeting pages carry the one-hour conversation;
# appendix pages hold the research behind it and get a code (A1, A2, ...).
PAGES = [
    ("agenda.html", "Agenda", "meeting"),
    ("fit.html", "Fit", "meeting"),
    ("buyer-2028.html", "The 2028 Buyer", "meeting"),
    ("proposal.html", "Launch Proposal", "meeting"),
    ("first-90-days.html", "First 90 Days", "meeting"),
    ("questions.html", "Questions", "meeting"),
    ("overview.html", "Research Appendix", "index"),
    ("role.html", "The Role", "appendix"),
    ("portfolio.html", "Portfolio", "appendix"),
    ("demand.html", "Demand Drivers", "appendix"),
    ("buyers.html", "Buyers", "appendix"),
    ("segments.html", "Segment Model", "appendix"),
    ("alternatives.html", "Alternatives", "appendix"),
    ("positioning.html", "Positioning", "appendix"),
    ("launch.html", "Launch Playbook", "appendix"),
    ("enablement.html", "Enablement", "appendix"),
    ("metrics.html", "Win Rate", "appendix"),
    ("ai.html", "AI Workflow", "appendix"),
    ("cv.html", "CV", "appendix"),
]
APPX = [f for f, _, g in PAGES if g == "appendix"]
CODE = {f: f"A{i + 1}" for i, f in enumerate(APPX)}
LABEL = {f: label for f, label, _ in PAGES}
GROUP = {f: g for f, _, g in PAGES}

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
        f'<a href="{f}"{" aria-current=\"page\"" if f == current else ""}>{html.escape(label)}</a>'
        for f, label, g in PAGES if g == "meeting")
    in_appx = GROUP[current] != "meeting"
    links += (f'<a class="appx" href="overview.html"{" aria-current=\"page\"" if in_appx else ""}>Appendix</a>')
    bar = ""
    if in_appx:
        items = "".join(
            f'<a href="{f}"{" aria-current=\"page\"" if f == current else ""}><b>{CODE[f]}</b>{html.escape(LABEL[f])}</a>'
            for f in APPX)
        bar = (f'<nav class="appxbar" aria-label="Research appendix"><div class="in">'
               f'<a class="home" href="overview.html"{" aria-current=\"page\"" if current == "overview.html" else ""}>Research Appendix</a>'
               f'{items}</div></nav>')
    return ('<header class="sitenav"><div class="in"><a class="brand" href="agenda.html">Arpan Bakshi<span>One Click LCA product marketing</span></a>'
            '<button class="theme" type="button" aria-label="Switch to dark mode">Dark</button>'
            '<button class="menu" type="button" aria-expanded="false" aria-controls="sitelinks">Menu</button>'
            f'<nav class="links" id="sitelinks" aria-label="Meeting pages">{links}</nav></div>{bar}</header>' + NAV_JS)


def pager(i):
    parts = []
    if i > 0:
        f, label, _ = PAGES[i - 1]
        parts.append(f'<a class="prev" href="{f}"><small>Previous</small><b>{html.escape(label)}</b></a>')
    if i < len(PAGES) - 1:
        f, label, _ = PAGES[i + 1]
        parts.append(f'<a class="next" href="{f}"><small>Next</small><b>{html.escape(label)}</b></a>')
    return f'<nav class="pager" aria-label="Page navigation">{"".join(parts)}</nav>'


FOOT = ('<footer class="site-foot"><span>Prepared {date} by Arpan Bakshi for the Senior Product Marketing Manager role at One Click LCA. '
        'Independent work from public sources; not produced or endorsed by One Click LCA.</span></footer>')


def build_page(i, fname):
    src = (PAGES_DIR / fname).read_text()
    m = re.match(r'\s*<!--meta title="([^"]*)" desc="([^"]*)"-->\s*', src)
    if not m:
        raise SystemExit(f"{fname}: missing meta comment")
    body = src[m.end():]
    if fname in CODE:
        body = body.replace('<span class="eyebrow">', f'<span class="eyebrow"><b class="acode">Appendix {CODE[fname]}</b>', 1).replace('<div class="tw">', '<div class="tw" tabindex="0" role="region" aria-label="Scrollable table">')
    out = (HEAD.format(guard=GUARD, title=html.escape(m.group(1)), desc=html.escape(m.group(2)))
           + '<a class="skip" href="#main">Skip to content</a>\n' + nav(fname)
           + f'\n<main class="wrap page" id="main" tabindex="-1">\n{body}\n</main>\n'
           + pager(i) + FOOT.format(date=DATE) + "\n</body>\n</html>\n")
    (OUT / fname).write_text(out)


def build_gate():
    if PASSWORD_FILE.exists():
        pw = PASSWORD_FILE.read_text().strip()
        digest = hashlib.sha256((SALT + pw).encode()).hexdigest()
    else:
        digest = (ROOT / "build" / "gate.hash").read_text().strip()
    (ROOT / "build" / "gate.hash").write_text(digest + "\n")
    ok = ",".join(f'"{f}"' for f, _, _ in PAGES)
    tpl = (ROOT / "build" / "gate.html").read_text()
    (OUT / "index.html").write_text(tpl.replace("%HASH%", digest).replace("%SALT%", SALT).replace("%OK%", ok))


if __name__ == "__main__":
    if OUT.exists():
        shutil.rmtree(OUT)
    shutil.copytree(ROOT / "assets", OUT / "assets")
    (OUT / ".nojekyll").write_text("")
    for i, (f, _, _) in enumerate(PAGES):
        if (PAGES_DIR / f).exists():
            build_page(i, f)
            print("wrote", f)
        else:
            print("missing", f)
    build_gate()
    print("wrote index.html")
