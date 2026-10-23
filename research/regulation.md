# Regulatory demand drivers for building and product LCA / EPD software

Prepared for: Senior Product Marketing Manager interview, One Click LCA
Research date: 23 October 2026 (web research; sources listed per item)

## How to read this

- **Status codes:** `IN FORCE` = legally applicable now. `ADOPTED` = law exists, obligations start later. `PROPOSED` = draft, consultation or roadmap only. `VOLUNTARY` = certification or funding lever, not law.
- **Verification flags:**
  - **[V]** = confirmed by an official or primary source, or by several consistent sources.
  - **[S]** = secondary sources only (law firms, consultancies, vendors including One Click LCA's own articles). Probably right, but check the official text.
  - **[UNVERIFIED]** = sources conflict, the information is old, or it comes from my background knowledge without confirmation in this research. Do not quote these without checking.
- **Buyer abbreviations:** ARCH = architect. ENG = structural/MEP engineer or sustainability consultant. CON = contractor. DEV = developer or owner. MFR = product manufacturer. PUB = public client or procurer. FIN = investor or lender.
- No date in this file was invented. Where I could not find a date, the entry says "not found".

---

## 1. EU level

### 1.1 EPBD recast, Directive (EU) 2024/1275, Article 7 (life-cycle GWP)
- **Status:** ADOPTED. The transposition deadline was 29 May 2026 [V]. One blog reports that the Commission sent letters of formal notice to all 27 Member States on 15 July 2026 for late transposition [UNVERIFIED].
- **Key dates:**
  - Commission delegated act on the EU calculation framework (amends Annex III): adopted 16 Dec 2025 as C(2025) 8723. It became Delegated Regulation (EU) 2026/52, reported as published in the OJ on 4 May 2026 and applicable from 24 May 2026 [S; one source says "January 2026", so check the OJ date].
  - National life-cycle GWP roadmaps, including limit-value trajectories: due 1 Jan 2027 [V].
  - Life-cycle GWP calculated and disclosed in the EPC: new buildings over 1,000 m² useful floor area from **1 Jan 2028**, all new buildings from **1 Jan 2030** [V].
  - Limit values: the roadmaps must set targets and limit values for new buildings from 2030 [S, Art 7(5)].
- **Scope:** All new buildings. Methodology: EN 15978-based, kgCO2e/m²/yr over a 50-year reference study period, with results reported per life-cycle stage [V]. Tier 1 (structure) and Tier 2 (shell, core, essential technical systems) are mandatory; Tiers 3 and 4 are illustrative [S]. Default values are allowed where product-specific data is missing [S]. Member States have some flexibility to weight or exclude stages when setting limits [S].
- **Requirement:** Whole-life-carbon (WLC) calculation, disclosed in the EPC. National limit values follow.
- **Forced buyers:** DEV (the obligation holder through the EPC), ARCH, ENG and CON (who run the calculation), MFR (EPD data replaces punitive default values).
- **Sources:** https://build-up.ec.europa.eu/system/files/2025-05/v4xQMgAqu5_26_05_2025_193225.pdf ; https://cif.ie/2026/02/12/epbd-current-state-of-play/ ; https://www.rehva.eu/news/article/eu-publishes-harmonised-framework-for-life-cycle-carbon-assessments-of-new-buildings ; https://transition-pathways.europa.eu/construction/green-transition/eu-delegated-regulation-life-cycle-global-warming-potential-new ; https://energy.ec.europa.eu/news/calculating-global-warming-potential-new-buildings-open-public-feedback-2025-10-06_en ; https://uptocode.ai/blog/epbd-2026-what-designers-need-to-check (infringement claim)

### 1.2 Construction Products Regulation (CPR) recast, Regulation (EU) 2024/3110
- **Status:** IN FORCE. It entered into force on 7/8 Jan 2025 and its main provisions apply from **8 Jan 2026** [V]. Penalty provisions follow from 8 Jan 2027 [S]. The transition from the old CPR 305/2011 runs to about 2039 [S].
- **Environmental declaration (part of the new DoPC):** Each obligation is triggered product family by product family, through revised harmonised standards and delegated acts. It does not apply to everyone on a single date.
  - Secondary sources describe the phasing as GWP first (2026 phase), more core indicators by around 2030, and the full EN 15804 indicator set by around 2032 [S]. A Czech authority gave Nov 2025, Nov 2029 and Nov 2031 [conflict, UNVERIFIED]. Confirm against Art. 22 and Annex I of the regulation.
  - Calculation basis: EN 15804+A2. The Commission is to provide the method and the software tool [S].
- **Digital Product Passport (DPP) for construction products:**
  - The Commission DPP registry (shared with ESPR) is due by 19 Jul 2026 [S].
  - A delegated act on DPP service providers is planned for Q4 2026 [S].
  - The first CPR Working Plan (2026–2029) was published Dec 2025 [S].
  - Product family 15 (cement, limes, hydraulic binders): new standards with a delegated act expected by Q4 2027, after which those products need a DPP [S].
  - Product family 2 (doors, windows, hardware): delegated acts expected 2028–2029 [S].
  - Commentary estimates mandatory DPPs per product family from around 2029 [S/UNVERIFIED].
- **Scope:** All construction products covered by harmonised technical specifications or EADs.
- **Requirement:** EPD-type environmental declaration (GWP first), DPP, and machine-readable data.
- **Forced buyers:** MFR (primary), plus notified bodies and EPD verifiers. Downstream, the free data flow benefits ARCH, ENG and CON.
- **Sources:** https://cobuilder.com/en/digital-product-passport-dpp/digital-product-passports-for-construction-what-the-eus-2026-2029-cpr-working-plan-means-for-stakeholders/ ; https://www.kiwa.com/en/news/construction-products-regulation-cpr-kiwa-and-vincotte-in-the-final-stages-of-becoming-a-notified-body/ ; https://unmz.gov.cz/en/nove-narizeni-o-stavebnich-vyrobcich-2/ ; https://www.certivo.com/frameworks/cpr-compliance ; https://www.construction-products.eu/wp-content/uploads/2025/10/02_Oscar-Nieto-The-new-Construction-Products-Regulation-CPR_071025.pdf

### 1.3 CSRD / ESRS and Omnibus I
- **Status:**
  - Omnibus I (CSRD and CSDDD simplification): political agreement 9 Dec 2025, then European Parliament vote. Reported in force 18 Mar 2026 [S; one source dates approval to 24 Feb 2026, UNVERIFIED].
  - Revised ESRS ("ESRS 2.0"): adopted by the Commission as a delegated act on 3 Jul 2026, then subject to 2+2 months of EP/Council scrutiny. Publication in the OJ was not confirmed as of Oct 2026 [S].
- **Scope after Omnibus:**
  - EU companies with more than 1,000 employees and more than €450m net turnover [V].
  - Non-EU groups with more than €450m EU turnover and an EU subsidiary or branch above €200m [S].
  - This cuts out most mid-size contractors, consultancies and product manufacturers.
- **Key dates:**
  - "Wave 2" companies apply the revised ESRS for FY beginning on or after 1 Jan 2027, with first reports in 2028 [S].
  - Wave 1 companies may opt to use the revised ESRS for FY2026 [S].
  - CSDDD: more than 5,000 employees and €1.5bn turnover, compliance from 26 Jul 2029 [S].
- **Requirement:** ESRS E1 Scope 1, 2 and 3 disclosure. For large contractors, developers and material producers, product and building LCAs feed Scope 3 (cat. 1 and 11) and transition plans. This is an indirect driver: no building-level LCA is mandated.
- **Forced buyers:** Large CON, DEV/REITs and MFR (cement, steel, insulation, glass majors). Their supply chains are no longer in scope directly, but large customers still request data from them.
- **Sources:** https://mofo.com/resources/insights/251222-eu-sustainability-omnibus-i-detailed-omnibus ; https://accountancyeurope.eu/wp-content/uploads/2026/01/260129-Omnibus-explained-CSRD-factsheet.pdf ; https://www.grantthornton.global/en/insights/articles/european-commission-adopts-revised-esrs-and-voluntary-standard/ ; https://sustainablefutures.linklaters.com/post/102n88h/eu-commission-adopts-revised-esrs-and-voluntary-reporting-standard ; https://www.simmons-simmons.com/en/publications/cmjjfgjeh05bkvlz0zmon98e4/omnibus-i-ep-formally-adopts-csrd-csddd-simplification-directive

### 1.4 EU Taxonomy, Climate Delegated Act (2021/2139), activity 7.1 "Construction of new buildings"
- **Status:** IN FORCE.
- **Requirement:** Taxonomy-aligned new buildings over 5,000 m² must calculate life-cycle GWP for each life-cycle stage and disclose it to investors and clients on demand. This is background knowledge of the 2021 text [UNVERIFIED in this research; check consolidated 2021/2139].
- **Pending change:** A 2026 Taxonomy review consultation discusses a revised criterion 7.1(3). From 1 Jan 2028, GWP would be calculated per the EPBD Art 7 Union framework, with a design-stage calculation and as-built disclosure in the EPC [S, proposal stage].
- **Simplification:** A 2025 Taxonomy simplification of the reporting templates exists, but I found no source confirming any change to the 7.1 LCA criterion [UNVERIFIED].
- **Forced buyers:** DEV and FIN (green bonds, green loans, Article 8/9 funds) commission the WLCA from ENG/ARCH.
- **Sources:** https://engage4esg.eurodw.eu/wp-content/uploads/2026/04/ENGAGEforESG_ResponseTaxonomyReview_10April2026.pdf ; https://worldgbc.org/wp-content/uploads/2025/01/WorldGBC-EU-Taxonomy-policy-briefing.pdf

### 1.5 Level(s)
- **Status:** VOLUNTARY EU framework, not law.
- **Role:** Indicator 1.2 (life-cycle GWP) is the reference used in EU GPP criteria, the Taxonomy and national methods. One vendor guide says EPBD reporting follows Level(s) Indicator 1.2. Another source describes the delegated act only as aligned with EN 15978 [conflict, UNVERIFIED].
- **Forced buyers:** PUB and DEV use it as the reporting format. It matters most as the common language behind EPBD and Taxonomy compliance.
- **Sources:** https://oneclicklca.com/en-be/resources/articles/epbd-a-guide-to-the-energy-performance-of-buildings-directive ; https://cif.ie/?p=76436

### 1.6 Green public procurement and industrial policy (EU)
- **Industrial Accelerator Act (IAA), COM(2026) 100, proposed 4 Mar 2026:** PROPOSED.
  - Sets low-carbon requirements for steel, cement/concrete/mortar and aluminium used in buildings, infrastructure and transport, within public procurement and public support schemes. Some items also carry EU-origin requirements.
  - "Low-carbon" is defined through delegated acts under the CPR and ESPR, so CPR GWP declarations become the gatekeeper.
  - Adds a voluntary low-carbon label, first for steel and then cement.
  - A pre-publication draft aligned the steel requirements to 2030 [UNVERIFIED for the final text].
  - Forced buyers: MFR (EPDs and CPR declarations), PUB.
  - Sources: https://www.lw.com/en/insights/european-commission-proposes-industrial-accelerator-act-key-takeaways ; https://commission.europa.eu/news-and-media/news/commission-proposes-new-measures-boost-eu-industry-and-jobs-2026-03-04_en ; https://www.skadden.com/insights/publications/2026/04/european-commission-proposes-industrial-accelerator-act
- **Revision of the Public Procurement Directives:** PROPOSED or pending. A legislative proposal was expected around Q2 2026, and a July 2026 leak suggested green criteria would be hard-wired into tenders. IISD references a September 2026 proposal that keeps GPP largely optional. I could not confirm the publication or its content [UNVERIFIED].
  - Sources: https://carbon-pulse.com/530827/ ; https://arthurcox.foleon.com/horizon-scanner-energy-planning-infrastructure-and-construction/horizon-scanner-energy-planning-infrastructure-and-construction-march-2026/public-procurement ; https://www.iisd.org/publications/digital-story/france-green-public-procurement
- **CPR Art. on GPP:** The CPR lets the Commission set mandatory minimum environmental sustainability requirements for public procurement of construction products via delegated acts. This is background knowledge [UNVERIFIED in this research].

---

## 2. Europe: countries

### Finland: Construction Act 751/2023, climate declaration and limits
- **Status:** IN FORCE. The Act has applied since 1 Jan 2025 [V]. Its low-carbon provisions apply to projects whose permits are applied for from 2026 [V].
- **Key dates:**
  - Climate declaration (ilmastoselvitys, under Decree 1027/2024) plus a building product list: mandatory for permits applied for on or after **1 Jan 2026** [V, Rakennustieto].
  - Carbon footprint **limit values**: Government decree approved 8 Jan 2026, applying to permit applications from **9 Jan 2026** [V, RT/CFCI]. Rakennustieto says 1 Jan 2026 (minor conflict).
  - Limits tighten **at the start of 2029** [V]. The earlier TRIS draft had said 2028.
- **Scope:**
  - Row houses, blocks of flats, offices, health centres, retail, accommodation and care, education and daycare, sports halls and hospitals.
  - Storage, transport, swimming and ice halls over 1,000 m².
  - Excluded: detached houses, holiday homes, agricultural, defence and renovation.
  - The climate declaration is due at final inspection. The building product list is due with the permit application.
- **Requirement:** WLC calculation (national method, including carbon handprint), limit values per use category, and a product list. EPDs improve results versus default data.
- **Forced buyers:** DEV (obligation holder), ARCH/ENG (calculation), CON (as-built data), MFR (Finnish EPDs and CO2data.fi).
- **Sources:** https://rt.fi/en/tiedotteet-ja-uutiset/2026/01/raja-arvot-rakennusten-hiilijalanjaljelle-voimaan-9-1/ ; https://www.rakennustieto.fi/en/rakennuksen-ilmastoselvitys ; https://www.iea.org/policies/31117-construction-act-and-low-carbon-building-requirements-7512023 ; https://technical-regulation-information-system.ec.europa.eu/en/notification/27245

### Netherlands: MPG (Milieuprestatie Gebouwen, Bbl art. 4.159)
- **Status:** IN FORCE. MPG calculation has been mandatory for homes and offices over 100 m² since 2013 and 2018 respectively, with limits for both [background, S].
- **Key dates:**
  - Homes limit tightened from 1.0 to 0.8 €/m²·yr on 1 Jul 2021 [S].
  - **1 Jul 2026:** Revised Bepalingsmethode (BPM 2.0) and NMD dataset **A2 (EN 15804+A2, 19 impact categories)** mandatory, replacing A1 [V, NMD Stichting].
  - Office requirement tightened by 15% [V].
  - **First-time MPG requirement for utility buildings** (schools, retail, healthcare, industrial) [V].
  - Laxer requirements for small homes (apartments under 60 m², detached houses under 80 m²) [S].
  - Weighted requirement for mixed-use buildings [V].
  - Numeric post-July-2026 values: one source says homes 1.6 and offices 1.55 on the A2 basis [S, UNVERIFIED]. A2 shadow costs are not comparable with A1 values.
  - The 2030 ambition to halve the requirement is a policy aim, not law [S].
- **EPBD transposition:** A parliamentary letter introduces a separate new instrument, "wlc-gwp" (a GWP-only WLC indicator), alongside MPG. It would be required with permit applications for buildings over 1,000 m² from 2028 [S]. MKI (environmental cost indicator) remains the single-score basis of MPG and is used in GWW/infrastructure tenders (DuboCalc) [S].
- **Forced buyers:** DEV, ARCH and ENG (permit), PUB (Rijkswaterstaat and ProRail MKI tender criteria), MFR (NMD-registered A2 data; old A1 entries lose value).
- **Sources:** https://milieudatabase.nl/en/latest/news/from-1-july-2026-revised-assessment-method-and-updated-mpg-requirements-take-ef/ ; https://iplo.nl/regelgeving/regels-voor-activiteiten/technische-bouwactiviteit/nieuwbouw/rijksregels/milieuprestatie-regels-vanaf-1-juli-2026/ ; https://solarmagazine.nl/nieuws-zonne-energie/i43931/nieuwe-en-strengere-milieuprestatie-eisen-voor-nieuwbouw-van-kracht ; https://milieudatabase.nl/en/latest/news/parliamentary-letter-on-epbd-introducing-new-instrument-wlc-gwp/ ; https://fhi.nl/en/nieuws/aanscherping-milieuprestatie-voor-gebouwen-op-1-juli

### Denmark: Building Regulations (BR18, now called BR25 by some sources) climate requirements
- **Status:** IN FORCE.
- **Key dates:**
  - LCA mandatory for all new buildings since 1 Jan 2023, with a 12 kgCO2e/m²/yr limit for buildings over 1,000 m² [V].
  - **1 Jul 2025:** National strategy for sustainable construction tightening:
    - Average limit about 7.1 kgCO2e/m²/yr [S].
    - Per type: flats, offices, retail and warehouses **7.5**. Single-family and terraced houses over 150 m² **6.7**. Institutions and other **8.0** [S].
    - Separate **construction process limit (A4–A5) of 1.5 kgCO2e/m²/yr** [S, VCBK guidance from sbst.dk].
    - Scope widened to include more building types, extensions and summerhouses/houses over 150 m² [S, conflicting].
  - **2027 and 2029** step-downs (for example 6.8 then 6.1 for flats and offices) are signposts, not final decisions, according to VCBK [S]. Decisions are still needed.
- **Requirement:** WLC (LCAbyg-based, 50 years), limit values, and a construction-site limit.
- **Forced buyers:** DEV, ARCH and ENG (permit), CON (A4–A5 site emissions, a new contractor obligation), MFR (Danish/Nordic EPDs).
- **Sources:** https://sbst.dk/Media/638731490173267243/VCBK_Guide_Byggeprocessen_fra_1._juli_2025-a[1].pdf ; https://sbst.dk/Media/638731489052141468/VCBK_LCA-publikation_opt-a[1].pdf ; https://www.danskindustri.dk/globalassets/brancher/di-byggeri/baredygtighed-i-byggeri-og-anlag/klimakrav----one-pager.pdf ; https://khr.dk/en/?p=20291 ; https://oneclicklca.com/da/resources/articles/danske-klimakrav-skærpes-markant

### Sweden: Climate declaration act (2021:787)
- **Status:**
  - Climate declaration: IN FORCE since 1 Jan 2022 for most new buildings. It covers A1–A5, with the Boverket climate database as the default data source [V].
  - Limit values: PROPOSED or under investigation.
- **History of limit values:** Boverket's 2023 report proposed limits from 1 Jul 2025 at the earliest, tightening every 5 years, plus an extended declaration from 2027. The government did not proceed [S].
- **Current track:** The Dec 2024 government assignment requires Boverket to deliver:
  - draft legislation implementing the EPBD life-cycle GWP requirement by 1 Jun 2026, and
  - a **roadmap for limit values by 1 Oct 2026** [S, riksdagen/Boverket].
  - The full life-cycle declaration and limits are targeted from 2028 (EPBD), with limits by 2030 at the latest [S].
  - Whether the Oct 2026 report has been published was not confirmed [UNVERIFIED].
- **Forced buyers:** DEV (declaring party), CON (A4–A5 data), MFR (EPDs to beat Boverket generic data with its 25% uplift).
- **Sources:** https://www.boverket.se/en/start/publications/2023/limit-values-for-climate-impact-from-buildings/ ; https://www.boverket.se/sv/om-boverket/boverkets-uppdrag-och-styrning/aktuella-uppdrag/direktiv-for-byggnaders-energiprestanda/hearing-om-gransvarden/ ; https://www.riksdagen.se/sv/dokument-och-lagar/dokument/interpellation/gransvarden-for-byggnaders-klimatpaverkan_hc10359/

### Norway: TEK17
- **Status:**
  - § 17-1 climate gas accounting (materials, A1–A3 plus B4 per NS 3720): IN FORCE since 1 Jul 2022 for residential blocks, offices and commercial buildings [background, S].
  - Limit values: PROPOSED.
- **Proposal:** DiBK consultation note dated 5 Feb 2026, with consultation closing around early May 2026.
  - Would expand § 17-1 to more building categories, life-cycle phases and building parts.
  - New **§ 17-2 limit values** for kindergartens, schools, residential blocks, offices, retail, hotels and nursing homes.
  - Main proposal examples: residential blocks 354, offices 396, schools 294 kgCO2e/m² BTA. The alternative is 10% lower.
  - Entry-into-force date: not found [UNVERIFIED].
- **Public procurement:** Public procurement already weights climate (DFØ reference levels).
- **Forced buyers:** DEV, ARCH, ENG, PUB (Statsbygg and municipalities), MFR (EPD-Norge).
- **Sources:** https://hoering.dibk.no/Hoering/LastNedVedlegg/38076 ; https://www.tekna.no/globalassets/filer/politikkdokumenter/horingsdokumenter/2026/20260504-innspill-til-horing-om-nye-klima--og-energikrav-i-teknisk-forskrift.pdf ; https://www.bnl.no/siteassets/dokumenter/horinger/horingsuttalelse-nye-klima-og-energikrav---oversendt-05.05.26.pdf

### France: RE2020
- **Status:** IN FORCE.
  - Housing since 1 Jan 2022.
  - Offices and education since 1 Jul 2022.
  - Other tertiary uses were phased in later [background, S].
  - Dynamic LCA, INIES/FDES/PEP data, 50 years.
- **Ic construction thresholds (kgCO2e/m²):**

  | Use | 2022 | 2025 | 2028 | 2031 |
  |---|---|---|---|---|
  | Detached house | 640* | 530 | 475 | 415* |
  | Collective housing | 740 | 650 | 580 | 490 |
  | Offices | 980 | 810 | 710 | 600 |
  | Primary/secondary education | 900 | 770 | 680 | 590 |

  *Detached-house 2022 and 2031 values are from background knowledge [UNVERIFIED]. All other values are [S] (FFB, Projet Celsius).
- **Changes in 2026:**
  - **Decree 2026-200 (18 Mar 2026):** relaxes only high-rise buildings (2028 = 95% of 2025). Excludes balcony carbon above a set area and ceiling height above 2.5 m. Adds +25 kgCO2e/m² for district-heating-connected buildings with air conditioning [S].
  - As of Sep 2026, no postponement of the 2028 step [S].
  - The Ic énergie tightening ends in 2028 [S].
- **Product side:** Products must have FDES/PEP environmental declarations, registered in INIES, to be used with specific data. Otherwise penalising default values apply [background, S].
- **Forced buyers:** DEV and promoteurs, ARCH and bureaux d'études (BET), MFR (FDES, a large EPD market).
- **Sources:** https://projetcelsius.com/en/blog/re2020-2028-thresholds/ ; https://www.ffbatiment.fr/actualites-batiment/actualite/nouveaux-seuils-1er-janvier-2025-pour-batiments-soumis-re-2020 ; https://www.qualitel.org/professionnels/reg_fiche_formation_rex-et-solutions-seuils-2025-a-2031_d

### Germany: QNG and KfW "Klimafreundlicher Neubau" (KFN), GEG
- **Status:** No legal building LCA requirement yet. Demand is driven by funding: VOLUNTARY but financially decisive.
- **KFN (KfW 297/298 residential, 299 non-residential):**
  - The current guideline is dated 12 Nov 2025, in force 15 Dec 2025, and runs to 31 Dec 2030 [S].
  - The KFN base tier requires an LCA GWP limit (24 kgCO2e/m²·a in the 2023 annex, which may be outdated) plus Effizienzhaus 40.
  - The higher loan tier (up to €150k per unit versus €100k) requires a **QNG-PLUS/PREMIUM** certificate [S].
  - The EH55 tier was extended to 31 Dec 2026 by the 15 Jun 2026 amendment [S].
- **QNG:** The state sustainability seal requires a whole-building LCA (eLCA/ÖKOBAUDAT methodology) and GWP limits. The 2022 brochure gives 28 (PLUS) and 20 (PREMIUM) kgCO2e/m²·a for residential; current values are on qng.info [S].
- **EPBD transposition:** Germany's EPBD transposition (GEG amendment) introducing life-cycle GWP disclosure: status not found [UNVERIFIED].
- **Public:** The federal Bewertungssystem Nachhaltiges Bauen (BNB) is used for federal buildings [background].
- **Forced buyers:** DEV and housing companies (to access subsidies), energy-efficiency experts and LCA consultants (ENG), MFR (ÖKOBAUDAT/IBU EPDs).
- **Sources:** https://www.umweltpakt.bayern.de/werkzeuge/foerderfibel/programme/353/klimafreundlicher-neubau-wohngebaeude-beg-em/ ; https://www.kfw.de/PDF/Download-Center/F%C3%B6rderprogramme-(Inlandsf%C3%B6rderung)/PDF-Dokumente/6000005054_M_297_298_300_498_TMA.pdf ; https://nexvyra.de/fakten/qng-zertifikat-neubau

### United Kingdom (England)
- **Part Z:** PROPOSED (industry draft since 2021). It would require WLC assessment for projects over 1,000 m², with limits later.
  - Not adopted. The government commissioned research and committed to consult on embodied carbon.
  - As of Oct 2026 I found **no government embodied carbon consultation published** [S/UNVERIFIED].
  - Sources: https://cibse.org/policy-advocacy/industry-initiatives/part-z/ ; https://oneclicklca.com/en-gb/resources/articles/part-z-whole-life-carbon-rules-for-uk-construction ; https://www.designingbuildings.co.uk/wiki/The_Net_Zero_Carbon_Buildings_Standard_and_Part_Z_explained
- **Future Homes and Buildings Standard:** ADOPTED.
  - Published 24 Mar 2026, with the amending regulations in force **24 Mar 2027** [S].
  - **Operational carbon only. Embodied carbon is excluded** [S].
  - This is not a direct LCA driver. Sources: https://questions-statements.parliament.uk/written-statements/detail/2026-03-24/hcws1445 ; https://www.elmhurstenergy.co.uk/blog/2026/03/24/mhclg-release-the-future-homes-standard/ ; https://www.homebuilding.co.uk/news/does-the-future-homes-standard-lack-embodied-carbon-regulations
- **London Plan Policy SI 2(F):** IN FORCE.
  - Every GLA-referable application must submit a WLC assessment (RICS PS-based, GLA template) at pre-app, application and post-construction stages, benchmarked against GLA benchmarks.
  - Non-referable major schemes are encouraged to do one.
  - A new London Plan is in preparation. Adoption status and any changes to the WLC policy were not confirmed [UNVERIFIED].
  - Sources: https://www.london.gov.uk/decisions/add2363-london-plan-whole-life-cycle-carbon-assessments ; https://netzerocompare.com/policies/the-london-plan-2021-whole-life-cycle-carbon-assessments-policy-si-2 ; https://www.planningresource.co.uk/article/1682909/gla-sets-new-sustainability-standards-emerging-london-plan
- **Other UK levers:**
  - Many local plans have WLC policies (for example several London boroughs and Bath & NE Somerset) [background, UNVERIFIED].
  - The UK Net Zero Carbon Buildings Standard is voluntary.
  - The UK CPR replacement (construction products reform) is pending [UNVERIFIED].
- **Forced buyers:** DEV, ARCH and ENG (planning stage, London), MFR (UK EPDs for the GB market).

### Ireland
- **Status:** IN FORCE (procurement) and ADOPTED (EPBD via SEAI method).
- **Key dates:**
  - **1 Sep 2025:** Public bodies must produce or procure a WLCA for new buildings with exchequer funding over €10m (non-residential) or €60m (residential) [S].
  - **1 Jun 2026:** Thresholds drop to €5m and €30m [S].
  - Enterprise.gov.ie guidance for infrastructure: over €60m, extending to over €10m from 1 Jan 2026 [S]. Building versus infrastructure timings differ across sources [UNVERIFIED].
  - Public procurement also requires **EPDs for cement and concrete** and a 30% clinker reduction target [S].
  - **1 Sep 2026:** SEAI national life-cycle GWP method v2.0.0 becomes the approved national reference [S].
  - **1 Jan 2028:** GWP on the BER certificate for new buildings over 1,000 m². **1 Jan 2030:** all new buildings [S].
- **Forced buyers:** PUB (OPW, HSE, education, local authorities), their design teams (ARCH, ENG), CON, MFR (cement and concrete EPDs).
- **Sources:** https://oneclicklca.com/en/resources/articles/irelands-updated-national-methodology-for-calculating-life-cycle-gwp-in-new-buildings ; https://enterprise.gov.ie/en/publications/guidance-public-bodies-reducing-embodied-carbon-in-construction.html ; https://mail.passivehouseplus.co.uk/news/government/most-polluting-cements-ruled-out-in-irish-public-procurement

### Belgium
- **Status:** PROPOSED or in transposition.
- **Tools:** TOTEM is the national (three-region) LCA tool. It uses the MMG method and an EPD-based database, B-EPD [S].
- **Flanders:** A draft decree (TRIS notification) gives OVAM the task of providing the calculation methodology for EPBD Art 7.2/7.5, with GWP limits from 2030. Adoption status was not found [UNVERIFIED].
- **Brussels and Wallonia:** transposition status not found [UNVERIFIED].
- **Forced buyers:** DEV, ARCH, MFR (B-EPD registration).
- **Sources:** https://technical-regulation-information-system.ec.europa.eu/en/notification/28309 ; https://www.dreso.com/be/news-cz/belgiums-real-estate-market-and-the-revised-epbd-entering-the-whole-life-carbon-era

### Switzerland (not EU, not bound by the EPBD)
- **Status:** ADOPTED as a cantonal model code, with uptake canton by canton.
- **MuKEn 2025:** Adopted by EnDK end of Aug 2025 (published 29 Aug 2025) [S]. It introduces **limit values for grey energy / construction GHG emissions for new buildings**. These take effect only when each canton writes them into cantonal energy law. St. Gallen, for example, foresees enforcement **2031 at the earliest** [S].
- **Minergie:** Minergie(-ECO) labels have stricter grey-energy limits, with some tightening from 2026 [S].
- **Federal level:** CO2-Gesetz provisions on grey energy: not verified [UNVERIFIED].
- **Forced buyers:** DEV, ARCH and ENG (in cantons that adopt), PUB (cantonal buildings often already require Minergie or SNBS).
- **Sources:** https://www.vs.ch/documents/d/energie/medienmitteilung_muken ; https://www.minergie.ch/media/minergie_im_kontext_der_muken_2025.pdf ; https://www.ratsinfo.sg.ch/media/documents/published/b1c59377-1656-4d94-85c8-440d8b5b6923.pdf

### Estonia
- **Status:** ADOPTED or IN FORCE [S/UNVERIFIED].
- **Requirement:** The Ministry of Climate prepared a rule requiring a carbon footprint calculation for new buildings over **1,000 m² net enclosed area from 1 Jul 2025**. The ministry page (Jul 2025) still calls it a draft. A developer says the calculation is required at building-permit application from 2025.
- **Method:** The national methodology was developed by TalTech with One Click LCA.
- **Limit values:** Not found.
- **Forced buyers:** DEV, ARCH, ENG.
- **Sources:** https://kliimaministeerium.ee/en/living-environment-circular-economy/construction-and-living-environment/energy-performance ; https://arcovara.com/en/research-buildings-operational-energy-has-greatest-impact-on-new-developments-carbon-footprint/

### Iceland (EEA, so EPBD-relevant)
- **Status:** IN FORCE. LCA is mandatory for most new building permits from **1 Sep 2025**, with a formal transition period [S].
- **Scope and method:** Excludes storage, agricultural buildings, summerhouses and extensions. The HMS method covers A1–A5, B1–B7, C1–C4 and D, in kgCO2e/m²/yr over 50 years, with a 25% safety factor on generic data [S].
- **One Click LCA relevance:** One Click LCA built the official HMS Icelandic tool (partnership announced Oct 2024). These sources are vendor-originated.
- **Forced buyers:** DEV, ARCH, ENG.
- **Sources:** https://oneclicklca.com/en/resources/articles/icelands-2025-mandatory-life-cycle-assessments-for-new-building-permits ; https://help.oneclicklca.com/en/articles/330754-island-lca-tool-for-2025-building-regulations

---

## 3. Outside Europe

### United States: federal Buy Clean
- **Status:** Largely WEAKENED or RESCINDED.
- **IRA funding:** IRA §60503 ($2.15bn for GSA low-embodied-carbon materials) and §60506 (FHWA Low-Carbon Transportation Materials grants) had their unobligated funds rescinded by the One Big Beautiful Bill Act (P.L. 119-21, signed Jul 2025) [S]. The repeal of §60116 (EPA EPD/labelling grants) is confirmed in a section-by-section summary [S].
- **GSA LEC program:** Requirements (EPDs plus GWP limits for concrete, steel, glass and asphalt) still appear on GSA pages, but the effect on new projects is unclear [UNVERIFIED].
- **Forced buyers (residual):** MFR (EPD stock built up: about 17,000 new EPDs since 2023).
- **Sources:** https://www.agri-pulse.com/ext/resources/2025/06/04/2D4AF07A4DE0B74296B89919A379BC7375EDF0F5A5BDF51D67E8919A584069FA.final-epw-reconciliation-title-section-by-section-pdf.pdf ; https://www.cliffordchance.com/content/dam/cliffordchance/briefings/2025/08/one-big-beautiful-bill-act-implications-for-the-environmental-sector.pdf ; https://www.gsa.gov/real-estate/gsa-properties/inflation-reduction-act/lec-program-details/material-requirements-faqs

### United States: California
- **Buy Clean California Act (BCCA):** IN FORCE.
  - Facility-specific EPDs plus maximum GWP limits for structural steel, rebar, flat glass and insulation on state projects. Limits have applied since 2022 and are reviewed every 3 years (the 2025 review lowered the rebar and insulation limits) [S].
  - SB 1207 broadened mineral wool to "insulation" [S].
  - Forced buyers: MFR, CON (submittals), PUB (DGS, Caltrans, UC).
- **CALGreen embodied carbon (Title 24 Part 11, 5.105 reuse / 5.409 LCA / prescriptive EPD path):** IN FORCE.
  - Applied from **1 Jul 2024** to new non-residential buildings over 100,000 ft² and schools over 50,000 ft². From **1 Jan 2026** the threshold drops to 50,000 ft² [S].
  - Compliance paths: building reuse, **WBLCA showing at least 10% GWP reduction** against a baseline, or a prescriptive product-GWP path (EPDs at or below limits) [S].
  - Forced buyers: DEV, ARCH, ENG, MFR.
- **Local:** Marin County and others have concrete codes [background, UNVERIFIED].
- **Sources:** https://www.dgs.ca.gov/PD/Resources/Page-Content/Procurement-Division-Resources-List-Folder/Buy-Clean-California-Act ; https://aiacalifornia.org/news/calgreen-mandatory-measures-for-embodied-carbon-reduction/ ; https://thorntontomasetti.com/calgreen-sustainable-construction ; https://getgreenbadger.com/calgreen-title-24-embodied-carbon-requirements/
- **Other US states:** Buy Clean laws exist in Colorado, Washington, New York, New Jersey, Oregon, Minnesota and Maryland, but were not verified in this research [UNVERIFIED].

### LEED v5 (USGBC, global)
- **Status:** VOLUNTARY. Launched 28 Apr 2025 [S].
- **Requirement:** New **prerequisite "Quantify and Assess Embodied Carbon"**, required for all LEED v5 BD+C projects.
  - Quantify A1–A3 GWP of structure, enclosure and hardscape.
  - Identify the top 3 hotspots and describe mitigation strategies.
  - Sources conflict on whether a WBLCA is required or a bill-of-materials route is enough.
  - The "Reduce Embodied Carbon" credit and the Building Product Selection credit reward EPDs and WBLCA reductions.
- **Forced buyers:** DEV, ARCH, ENG globally (LEED is strong in the US, Middle East, China and India). It also drives MFR EPDs.
- **Sources:** https://oneclicklca.com/en/resources/articles/leed-v5-launches-with-a-focus-on-lca-embodied-carbon ; https://www.dci-engineers.com/news/leed-v5-is-here

### Canada
- **Federal Standard on Embodied Carbon in Construction (Treasury Board):** IN FORCE.
  - In effect since 31 Dec 2022 for major federal construction, with concrete EPDs and a 10% reduction for ready-mix [background].
  - **Updated by Contracting Policy Notice 2025-6 (22 Jul 2025):** adds WBLCA requirements and structural/reinforcing steel requirements [S].
  - A consultant cites a target of at least 30% lower embodied carbon in major materials from 2025 [S/UNVERIFIED].
  - Forced buyers: PUB (PSPC, DND), design teams, MFR.
- **National Building Code:** PROPOSED. CBHCC draft position paper (mid-2025) proposes tiered embodied carbon provisions (A1–A3 first) for the **2030 code cycle** [S].
- **Toronto Green Standard v4:** IN FORCE.
  - City-owned new buildings: upfront embodied carbon (A1–A5, structure and envelope) under 350 kgCO2e/m².
  - Private projects: voluntary Tier 2.
  - TGS v5 may make it mandatory (timing 2025–2026 unclear) [S/UNVERIFIED].
- **Vancouver:** Building by-law embodied carbon reporting/limits not verified [UNVERIFIED].
- **Sources:** https://www.canada.ca/en/treasury-board-secretariat/services/policy-notice/2025-6.html ; https://www.tbs-sct.canada.ca/pol/doc-eng.aspx?id=32742 ; https://magazine.glasscanadamag.com/articles/cbhcc-releases-embodied-carbon-policy-proposal ; https://community.carbonleadershipforum.org/t/toronto-becomes-first-jurisdiction-in-north-america-to-put-embodied-carbon-caps-on-new-city-owned-construction-a1-a5-350-kg-co2e-m2/6744

### Australia
- **NABERS Embodied Carbon:** VOLUNTARY.
  - Launched late 2024. Rules v2.0 and calculator released in 2025. First certified rating Dec 2025 [S].
  - Covers upfront emissions (A1–A5) and excludes fit-out.
- **NCC 2025:** NABERS Embodied Carbon is a **voluntary** route for commercial buildings. Mandatory embodied carbon minimums are still under development [S]. Adoption timing varies by state [UNVERIFIED].
- **Green Star Buildings:** Requires at least a 10% upfront carbon reduction (minimum expectation) and 20% for credit points, rising to 40% later. NABERS EC is accepted [S].
- **NSW:** NSW (BASIX / State Environmental Planning Policy) embodied emissions reporting for large non-residential buildings: not verified in this research [UNVERIFIED].
- **Forced buyers:** DEV and REITs (Green Star is standard for institutional property), ENG, MFR (EPD Australasia).
- **Sources:** https://nabers.gov.au/ratings/our-ratings/nabers-embodied-carbon ; https://nabers.gov.au/news/key-updates-embodied-carbon-ratings-2025 ; https://epd-australasia.com/2024/12/nabers-embodied-carbon-rating-tool-launched/ ; https://www.gbca.au/wp-content/uploads/NSW-Protection-of-Environment-Policy-submission.pdf

### Singapore
- **Green Mark 2021 (2nd edition):** Applies to all projects assessed from 1 Jun 2024 [S].
  - Includes a **Whole Life Carbon** section that requires embodied carbon calculation using the BCA embodied carbon calculator.
  - Green Mark is legally mandatory (minimum level) for new buildings over 5,000 m² GFA and for major retrofits under the Building Control (Environmental Sustainability) Regulations [background, UNVERIFIED].
- Whether embodied carbon calculation is mandatory at the minimum level: [UNVERIFIED].
- **Forced buyers:** DEV, ENG (Green Mark consultants), MFR (SGBC-certified products).
- **Sources:** https://www1.bca.gov.sg/sustainability/greenmark/green-mark-2021/ ; https://www1.bca.gov.sg/buildsg/sustainability/green-building-masterplans

### UAE
- **Status:** No binding embodied carbon requirement found.
  - Dubai Green Building Regulations (mandatory since 2014) and Al Sa'fat (2016) are operational-focused.
  - Estidama Pearl (Abu Dhabi) contains material credits, but no mandatory LCA was found [S].
- **Demand drivers:** LEED v5 (widely used in the UAE) and the UAE Climate Law (Federal Decree-Law 11/2024, emissions reporting) [S]. CIBSE TM65 UAE (MEP embodied carbon) [S].
- **Forced buyers:** DEV (LEED/ESG), MFR exporting to the EU (CPR, CBAM) [UNVERIFIED].
- **Sources:** https://orfme.org/expert-speak/building-sustainable-infrastructure-in-a-rapidly-expanding-gulf-estate-market/ ; https://www.cundall.com/ideas/blog/the-convergence-of-green-certification-and-regulatory-compliance-how-leed-v5-complements-the-uae-climate-law ; https://www.cibse.org/policy-advocacy/news/cibse-unveils-the-revolutionary-tm65-uae-at-light-plus-intelligent-building-middle-east-summit-as-uae-targets-net-zero-by-2050/

---

## 4. Chronological table, 2025–2032

| Date | Jurisdiction | Event | Status | Who must act | Flag |
|---|---|---|---|---|---|
| 1 Jan 2025 | Finland | Construction Act 751/2023 in force | In force | DEV, ARCH | V |
| 7–8 Jan 2025 | EU | CPR 2024/3110 enters into force | In force | MFR | V |
| 28 Apr 2025 | Global | LEED v5 launched; embodied carbon prerequisite | Voluntary | DEV, ARCH, ENG | S |
| 1 Jul 2025 | Denmark | Tighter limits (7.5/6.7/8.0), A4–A5 site limit 1.5, wider scope | In force | DEV, ARCH, ENG, CON | S |
| 1 Jul 2025 | Estonia | Carbon footprint calculation for new buildings over 1,000 m² | In force? | DEV, ARCH | UNVERIFIED |
| Jul 2025 | US | OBBBA rescinds unobligated IRA low-carbon materials funds | In force | (MFR demand drop) | S |
| 22 Jul 2025 | Canada | Federal Embodied Carbon Standard updated (WBLCA, steel) | In force | PUB, design teams | S |
| 29 Aug 2025 | Switzerland | MuKEn 2025 adopted, with grey-energy limits (cantonal uptake later) | Adopted | DEV, ARCH | S |
| 1 Sep 2025 | Iceland | LCA mandatory for most new building permits | In force | DEV, ARCH, ENG | S |
| 1 Sep 2025 | Ireland | WLCA for exchequer-funded buildings over €10m / €60m | In force | PUB, ARCH, ENG | S |
| 9 Dec 2025 | EU | Omnibus I political agreement | Adopted | Large CON, DEV, MFR | V |
| 16 Dec 2025 | EU | EPBD life-cycle GWP delegated act adopted (later DR 2026/52) | Adopted | All | V |
| Dec 2025 | Australia | First certified NABERS Embodied Carbon rating | Voluntary | DEV | S |
| Dec 2025 | EU | CPR Working Plan 2026–2029 published | Adopted | MFR | S |
| 1 Jan 2026 | Finland | Climate declaration + building product list for permits | In force | DEV, ARCH, ENG, MFR | V |
| 9 Jan 2026 | Finland | Carbon footprint limit values (permit applications) | In force | DEV, ARCH, ENG | V |
| 1 Jan 2026 | California | CALGreen embodied carbon threshold falls to 50,000 ft² | In force | DEV, ARCH, ENG, MFR | S |
| 1 Jan 2026 | Ireland | Infrastructure WLCA threshold extends to over €10m | In force | PUB | S/UNVERIFIED |
| 8 Jan 2026 | EU | CPR main provisions apply (DoPC framework, environmental declaration as acts arrive) | In force | MFR | V |
| 5 Feb 2026 | Norway | DiBK consults on TEK17 § 17-2 limit values | Proposed | DEV, ARCH, ENG | S |
| 4 Mar 2026 | EU | Industrial Accelerator Act proposed (low-carbon steel, cement, aluminium in GPP) | Proposed | MFR, PUB | S |
| 18 Mar 2026 | EU | Omnibus I in force (CSRD over 1,000 employees and €450m) | In force | Large CON, DEV, MFR | S |
| 18 Mar 2026 | France | Decree 2026-200: RE2020 high-rise relief | In force | DEV, ARCH | S |
| 24 Mar 2026 | England | Future Homes/Buildings Standard published (operational only) | Adopted | — | S |
| 24 May 2026 | EU | DR 2026/52 (EU life-cycle GWP method) applicable | In force | All | S |
| 29 May 2026 | EU | EPBD transposition deadline | Deadline | Member States | V |
| 1 Jun 2026 | Ireland | Public WLCA thresholds fall to €5m / €30m | In force | PUB | S |
| 1 Jun 2026 | Sweden | Boverket draft legislation on EPBD GWP due | Proposed | — | S |
| 1 Jul 2026 | Netherlands | MPG on EN 15804+A2 (BPM 2.0); offices −15%; utility buildings in scope | In force | DEV, ARCH, ENG, MFR | V |
| 3 Jul 2026 | EU | Revised ESRS delegated act adopted (scrutiny period) | Adopted | Large companies | S |
| 19 Jul 2026 | EU | DPP registry deadline (ESPR/CPR) | Deadline | Commission | S |
| 1 Sep 2026 | Ireland | SEAI national GWP method v2.0.0 becomes the reference | In force | ARCH, ENG | S |
| 1 Oct 2026 | Sweden | Boverket limit-value roadmap due | Proposed | — | S/UNVERIFIED delivery |
| Q4 2026 | EU | CPR delegated act on DPP service providers | Planned | MFR | S |
| 31 Dec 2026 | Germany | KFN EH55 tier expires | In force | DEV | S |
| 1 Jan 2027 | EU | National life-cycle GWP roadmaps (incl. limits) due | Deadline | Member States | V |
| 1 Jan 2027 | EU | Wave-2 CSRD reporting FY starts (report 2028) | Adopted | Large companies | S |
| 8 Jan 2027 | EU | CPR penalty provisions apply | Adopted | MFR | S |
| 24 Mar 2027 | England | Future Homes/Buildings Standard in force | Adopted | — | S |
| 2027 | Denmark | Second tightening step (e.g. 6.8) | Signposted | DEV, ARCH | S (not final) |
| Q4 2027 | EU | Cement (family 15) CPR delegated act, DPP to follow | Planned | MFR (cement) | S |
| 1 Jan 2028 | EU-27 + EEA | **Life-cycle GWP disclosure in EPC for new buildings over 1,000 m²** | Adopted | DEV, ARCH, ENG, CON | V |
| 1 Jan 2028 | Netherlands | wlc-gwp with permit for buildings over 1,000 m² | Proposed | DEV, ARCH | S |
| 1 Jan 2028 | Ireland | GWP on BER for new buildings over 1,000 m² | Adopted | DEV | S |
| 1 Jan 2028 | EU Taxonomy | Proposed 7.1: GWP per EPBD Union framework | Proposed | DEV, FIN | S |
| 1 Jan 2028 | France | RE2020 Ic construction step 2 (−10 to −18%) | In force | DEV, ARCH, MFR | S |
| 2028–2029 | EU | CPR acts for doors/windows (family 2); first mandatory construction DPPs around 2029 | Planned | MFR | S/UNVERIFIED |
| 2028 | Sweden | Expected start of extended (full-LCA) declaration | Proposed | DEV | S |
| 1 Jan 2029 | Finland | Limit values tighten | Adopted | DEV, ARCH | V |
| 2029 | Denmark | Third tightening step (e.g. 6.1) | Signposted | DEV, ARCH | S (not final) |
| 26 Jul 2029 | EU | CSDDD compliance for in-scope companies | Adopted | Very large companies | S |
| 1 Jan 2030 | EU-27 + EEA | **Life-cycle GWP disclosure for all new buildings; national limit values due** | Adopted | DEV, ARCH, ENG, CON, MFR | V |
| ~2030 | EU (CPR) | More environmental indicators in CPR declarations | Adopted (phasing) | MFR | S |
| ~2030 | EU (IAA) | Possible low-carbon steel requirement in public procurement | Proposed | MFR, PUB | UNVERIFIED |
| By 2030 | Sweden | Limit values in force | Proposed | DEV | S |
| 2030 | Canada | NBC embodied carbon provisions (code cycle) | Proposed | DEV, ARCH | S |
| 2030 | Netherlands | Ambition to halve MPG requirement | Policy aim | DEV | S |
| 31 Dec 2030 | Germany | KFN guideline end date | In force | DEV | S |
| 1 Jan 2031 | France | RE2020 final Ic construction step | In force | DEV, ARCH, MFR | S |
| ≥2031 | Switzerland | MuKEn 2025 grey-energy limits in some cantons (St. Gallen at the earliest) | Proposed | DEV, ARCH | S |
| ~2032 | EU (CPR) | Full EN 15804 indicator set in declarations | Adopted (phasing) | MFR | S |

---

## 5. Segment × deadline matrix (nearest forcing events from Oct 2026)

| Segment | Already forced now (2025–2026) | Next hard deadline |
|---|---|---|
| Developers/owners | FI (limits), DK (limits), NL (MPG A2), FR (RE2020), IS, IE (public), London, CALGreen | **1 Jan 2028**: EU EPC GWP over 1,000 m²; FR 2028 step; FI 2029 |
| Architects/engineers/LCA consultants | Same as above; the calculation work falls to them | National tools and methods aligned to DR 2026/52 during 2027 (roadmaps), then 2028 |
| Contractors | DK A4–A5 site limit (since Jul 2025); FI as-built declaration; SE A1–A5 declaration; IE public WLCA | 2028 EPBD as-built disclosure; CSRD Wave 2 FY2027 for large contractors |
| Manufacturers | NL A2 data in NMD (Jul 2026); FR FDES/INIES; CALGreen/BCCA EPDs; IE cement/concrete EPDs; CPR applies (Jan 2026) | CPR family-by-family acts (cement Q4 2027), DPP around 2028–2029, IAA low-carbon public procurement |
| Public clients | IE thresholds (Jun 2026), Canada federal standard, BCCA, Toronto city buildings, NO procurement | EU procurement revision and IAA (proposed) |
| Investors/lenders | EU Taxonomy 7.1 (over 5,000 m²) | Revised 7.1 tied to EPBD method from 2028 (proposed) |

## 6. Main open items to verify before the interview
1. CPR Art. 22 exact phasing years for GWP, core and full indicators (2026/2030/2032 versus 2025/2029/2031).
2. DR 2026/52 OJ publication date (4 May 2026 versus Jan 2026).
3. NL post-1 Jul 2026 numeric MPG limits on the A2 basis.
4. Whether Boverket delivered the 1 Oct 2026 Swedish limit-value roadmap, and its proposed dates.
5. Norway § 17-2 final adoption and entry-into-force date.
6. Status of the UK embodied carbon consultation and the new London Plan.
7. German EPBD transposition (GEG) of life-cycle GWP disclosure.
8. Estonia: final adoption of the 1 Jul 2025 rule.
9. EU public procurement directive revision: published proposal content.
