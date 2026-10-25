# One Click LCA application: Senior Product Marketing Manager

A static site of research, decision models and plans for the One Click LCA Senior Product Marketing Manager interview. Built 23 October 2026.

## Site
The published site is the `docs/` folder. Open `docs/index.html`. It is a password page; only a salted hash of the password is stored here. The site has two groups.

The pages are shown on screen in the interview and then shared with the One Click LCA interviewer. Writing rules are in `build/STYLE.md`.

Meeting pages, in the order of the interview. They show my approach and contain no figures; data and models stay in the appendix.
- `agenda.html`: the first page a reader sees: the order of the conversation and how to use the site
- `fit.html` (Background): where I have worked, the requirements against my experience, the gap, and how I approach business development
- `market.html` (Market): how I find where new demand comes from, with the EU disclosure requirement as a worked example
- `launch-approach.html` (Launch Approach): the steps I follow to take a release to market, with the same worked example
- `first-months.html` (First Months): listen, decide, ship
- `questions.html` (Questions): the questions I will ask One Click LCA

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
