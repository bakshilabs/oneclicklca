# Session notes

## 23 October 2026
- Found the listing on Arc.dev; the One Click LCA careers page and Remotive copies are offline.
- Wrote `PLAN.md`, modelled on the Populous site (`bakshilabs/populous`): a password-protected static site with one page per job description line, plus a 15 to 20 minute walk-through.
- Nothing has been built yet. Open questions are listed at the end of `PLAN.md`.
- Writing rules carried over: plain-noun titles, full sentences, no em-dash asides, no "not X but Y", no closing summary line.

## 23 October 2026, build
- Four research agents wrote `research/*.md`. Findings that changed the plan: the role sits in Product Management; a Lead Product Marketing role exists since Sep 2025; product ships monthly with two live launch events a year; a President, COO and CRO joined Sep 2026 and the CPO left Aug 2026 (LinkedIn snapshots, to confirm); SimaPro is part of the group; Tally was bought by C.Scale in Apr 2026; "Preconstruct" is not a real vendor.
- Built 15 pages with four interactive models (segment scoring, launch tiering, business case, win rate). axe-core clean in light and dark; no horizontal scroll at 390 px.
- Password set to the value given to Arpan in chat; only the hash is committed.

## Open points
- Segment scores, buying criteria weights and calculator defaults are judgement. Replace with interview evidence where possible.
- The "Four things I learnt" panel on `fit.html` is written in Arpan's voice from the brief he gave; he should replace it with his own examples.
- To verify before citing: current CRO and CPO, CPR declaration phasing, Dutch MPG limits after July 2026, whether Sweden's roadmap was delivered, EPD Hub's former relationship with One Click LCA.
- Not yet published to GitHub Pages. Decide whether to publish and from which repo.

## Visual redesign (23 October 2026, continued)
- User feedback: the first build was too text-heavy. Target: at least 8 of 10 for interactivity and visual engagement on every page.
- Added a shared chart layer (`assets/viz.css`, `assets/viz.js`): validated categorical palette, tooltips that pin on click or tap, tabs, reveal motion, count-up numbers, and a section stepper (up, down, n / N, J and K keys; a bottom bar on phones).
- Five rounds of redesign by four page agents, each followed by an independent reviewer. Final independent scores: every page 8 or above (Positioning 8.5, CV 8, Demand, Segments, Launch and Enablement 9).
- Corrections made along the way: the launch window is twelve months (roadmaps 1 Jan 2027, disclosure 1 Jan 2028); 301 unique source links across the research files; the 2030 map shows disclosure required with national limits due, not limits in force everywhere; the CPR penalties date is marked to confirm.
- Open: `research/` is public on GitHub Pages, including named employees in `team-and-voice.md`. The user has not yet decided whether to remove it.
- Optional polish noted by the last review: CV role cards repeat the title and both Foster cards open the same entry; the Positioning test-plan tabs are still shallow.
