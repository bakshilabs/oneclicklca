# One Click LCA application: Senior Product Marketing Manager

A static site of research, decision models and plans for the One Click LCA Senior Product Marketing Manager interview. Built 23 October 2026.

## Site
Open `index.html`. It is a password page; only a salted hash of the password is stored here. Pages in nav order:

- `overview.html`: headline findings and links
- `role.html`: the eight duties decoded, context, working relationships, operating rhythm, success at 6 and 12 months, questions for the panel
- `fit.html`: each requirement against career evidence
- `portfolio.html`: products by buyer, job and trigger; packaging; four first-quarter fixes
- `demand.html`: regulatory forcing dates 2025 to 2031 and the three waves of buyers
- `buyers.html`: buying committees, criteria heat map, customer quotes, interview programme
- `segments.html`: interactive sub-segment scoring model with launch-type presets
- `alternatives.html`: competitor map and table, cost of doing nothing, six risks
- `positioning.html`: positioning statement, six message houses, One Click LCA and SimaPro rule, test plan
- `launch.html`: interactive launch tiering tool, worked EU 2028 launch, 2027 calendar
- `enablement.html`: business case calculator, discovery questions, objections, battlecard
- `metrics.html`: interactive win rate model, CRM fields, metric tree, attribution
- `first-90-days.html`, `ai.html`, `cv.html`

## Build
Page bodies live in `build/pages/`. Run `python3 build/build.py` to wrap them with the shared head, navigation and footer and to write `index.html` from `build/gate.html`. Put the password in `build/.password` (ignored by git) to change it; otherwise the stored hash in `build/gate.hash` is reused. Styles: `assets/site.css`, `nav.css`, `a11y.css` (from the Populous site) and `assets/pages.css` (this site's components and green accent).

## Research
`research/` holds the four sourced research files behind the pages: `company.md`, `competitors.md`, `regulation.md`, `team-and-voice.md`. Claims are flagged verified, secondary or unverified.

## Other files
- `job-description.txt`: the listing
- `PLAN.md`: the first plan for the interview materials
- `session-notes.md`: decisions and open points

Keep this repository private. The research names no individual employees beyond the CEO.
