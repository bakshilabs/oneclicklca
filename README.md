# One Click LCA application: Senior Product Marketing Manager

A static site of research, decision models and plans for the One Click LCA Senior Product Marketing Manager interview. Built 23 October 2026.

## Site
The published site is the `docs/` folder. Open `docs/index.html`. It is a password page; only a salted hash of the password is stored here. The site has two groups.

The pages are shown on screen in the interview and then shared with the One Click LCA interviewer. Writing rules are in `build/STYLE.md`.

Meeting pages, in the order of a one-hour interview (about 25 minutes of material):
- `agenda.html`: the first page a reader sees: what the hour covers, the case in four parts and how to use the site
- `fit.html`: each requirement against career evidence (minutes 5 to 9)
- `buyer-2028.html`: three findings about the first-time buyer created by EU disclosure in 2028 (minutes 9 to 17)
- `proposal.html`: the tier one launch proposal for first-time EU buyers, with segment filter, message, milestones, value model, targets and risks (minutes 17 to 27)
- `first-90-days.html`: listen, decide, ship (minutes 27 to 30)
- `questions.html`: the questions I will ask One Click LCA, in priority order

Research appendix, indexed by `overview.html` and shown with an appendix bar on each page: A1 `role.html`, A2 `portfolio.html`, A3 `demand.html`, A4 `buyers.html`, A5 `segments.html`, A6 `alternatives.html`, A7 `positioning.html`, A8 `launch.html`, A9 `enablement.html`, A10 `metrics.html`, A11 `ai.html`, A12 `cv.html`.

## Build
Page bodies live in `build/pages/`. Run `python3 build/build.py` to rebuild `docs/`: it copies `assets/`, wraps each page with the shared head, navigation (meeting links, plus the appendix bar on appendix pages) and footer and writes `docs/index.html` from `build/gate.html`. Do not edit files in `docs/` by hand. Put the password in `build/.password` (ignored by git) to change it; otherwise the stored hash in `build/gate.hash` is reused. Styles: `assets/site.css`, `nav.css`, `a11y.css` (from the Populous site) and `assets/pages.css` (this site's components and green accent).

## Research
`research/` holds the four sourced research files behind the pages: `company.md`, `competitors.md`, `regulation.md`, `team-and-voice.md`. Claims are flagged verified, secondary or unverified.

## Other files
- `job-description.txt`: the listing
- `PLAN.md`: the first plan for the interview materials
- `session-notes.md`: decisions and open points

Keep this repository private. The research names no individual employees beyond the CEO.

## Publishing
Publish the `docs/` folder only, for example with GitHub Pages set to deploy from the `main` branch and the `/docs` folder. Everything outside `docs/` (research files, notes, plan, job description, screenshots) stays out of the published site. The password check runs in the browser, so it hides the pages from casual visitors but does not protect them: anyone with a page URL can fetch its HTML. Pages carry `noindex`.
