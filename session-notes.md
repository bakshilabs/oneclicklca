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
- Named employees and LinkedIn links were removed from `research/` on 24 October 2026 at the user's request. Only the CEO is named. Earlier versions remain in git history.
- Optional polish noted by the last review: CV role cards repeat the title and both Foster cards open the same entry; the Positioning test-plan tabs are still shallow.

## Meeting and appendix split (25 October 2026)
- Re-read the site as the candidate in a one-hour panel. Six pages carry the meeting: Agenda, Fit, The 2028 Buyer, Launch Proposal, First 90 Days and Questions. The other twelve became a numbered Research Appendix (A1 to A12) with its own bar under the navigation; `overview.html` is now the appendix index. The password page now opens on the Agenda.
- New pages: `agenda.html`, `buyer-2028.html`, `proposal.html`, `questions.html`. All nineteen pages checked at 1280 and 390 px in light and dark with no script errors and no sideways scroll.
- To fill or confirm: the underperforming launch answer on Questions needs Arpan's own example; the proposal targets (minus 10 points no-decision share, plus 5 points win rate, 60% first-project adoption) and the segment angles are judgement; the Germany angle mentions KfW and QNG work, which assumes those projects run in One Click LCA.

## Publishing preparation (25 October 2026)
- No new information was added. Removed the question about an underperforming launch from Questions, because it needed Arpan's own example. Reworded the Germany angle on Launch Proposal so it no longer assumes KfW and QNG work runs in One Click LCA.
- References to `research/*.md` on the pages now say the research files are available on request, since those files are not published.
- The build now writes the site to `docs/` (pages, `index.html`, `assets/`, `.nojekyll`); the built HTML files were removed from the repository root.

## Visual pass (25 October 2026, continued)
- Replaced the stock palette: Apple system greys became warm stone neutrals, and the reference chart series became an earth palette (slate, terracotta, sage, ochre, clay, moss, muted heather, berry). The dark-mode accent is a softer green.
- Removed every coloured edge stripe (border-left, border-top and ::before bars) across meeting and appendix pages.
- Refined Agenda, The 2028 Buyer, Launch Proposal and Questions to appendix standard. Each scored about 8 after review, up from 5 to 6.
- All 19 pages pass axe-core in light and dark, with no console errors and no sideways scroll at 1280 and 390 px.

## Rewrite for the reader (25 October 2026, continued)
- The site is shown during the interview and then shared with the One Click LCA interviewer, so every page now addresses that reader. Rules are in `build/STYLE.md`: plain words, topic headings, no slogans or punch lines, no contrast constructions, judgement and placeholder figures labelled, example messaging marked as drafts to test.
- Agenda became a plain cover and agenda. Questions now lists only my questions for One Click LCA. The prepared answers moved to `private/prepared-answers.md`, which git ignores so it is never pushed or published.
- Removed stage directions ("minutes 9 to 17"), third-person panel notes and the Role timeline events taken from personal LinkedIn profiles.
- Claims about One Click LCA's own deals, CRM and website are now conditional outside readings.
- All 19 pages pass axe-core in light and dark, with no console errors and no sideways scroll at 1280 and 390 px.

## Approach without figures (25 October 2026, continued)
- The interview is about Arpan's approach, so the meeting pages hold no figures or data charts. They are Agenda, Background (fit.html), Market (market.html), Launch Approach (launch-approach.html), First Months (first-months.html) and Questions. The only numerals left are step markers.
- Market and Launch Approach each set out the steps Arpan follows, with the EU disclosure requirement for new buildings as an example in words. The draft message is now "One model, reported to the EU method and to your national scheme", labelled as a draft to test.
- The appendix keeps its data and models for anyone who asks. The footer carries no dates.
- All 19 pages pass axe-core in light and dark, with no console errors and no sideways scroll at 1280 and 390 px.

## A13 EPD Generator Campaign (11 November 2026)
- Added `epd-campaign.html` as appendix A13 from the take-home brief: messaging framework, landing page wireframe with full copy, a rationale of under 300 words, and a seven-step record of the work.
- Four research subagents ran in parallel and wrote `research/epd-proof.md`, `research/epd-defaults.md`, `research/epd-competitors.md` and `research/epd-buyers.md`.
- Chosen angle: a product with no EPD is counted at a conservative generic value (Norway and Sweden about +25%, Finland +20%, Netherlands +30%). No EPD creation vendor uses it.
- Chosen buyer: the commercial director at a mid-sized Nordic manufacturer. Risk to test: no public source shows sales owning the EPD budget.
- To confirm: Swedish government decision on Boverket report 2026:27; whether the Pre-Verified EPD Generator is offered in the Nordics; One Click LCA data for the placeholder proof and the gap check.
- Same day: moved the campaign from the Nordics to the UK at the user's request. Two more subagents wrote `research/epd-uk-rules.md` and `research/epd-uk-market.md`. No UK rule adds a fixed uplift to generic data, so the UK argument is "counted as average, your advantage is invisible", paired with BREEAM Mat 02 EPD points and contractor requests (Laing O'Rourke). Step 7 on the page records the switch.
- To confirm for the UK: BREEAM V7 EPD point values against BRE's licensed manual; adoption of the draft London Plan Policy GHR3; whether METSEC can be shown as a UK proof logo; a named UK project won after publishing EPDs.
