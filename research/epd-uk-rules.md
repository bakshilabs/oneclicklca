# How UK (England) whole life carbon rules treat products without a product-specific EPD

Research date: 11 November 2026. Scope: England, with UK-wide standards where relevant. Audience: campaign aimed at UK construction product manufacturers.

Status labels used below: **MANDATORY** (legally binding or binding on those who choose or are required to use it), **VOLUNTARY**, **PROPOSED** (draft or consultation), **UNVERIFIED** (could not be confirmed from a primary source in this session).

Quotations are copied from the source text. Long dashes in original sources have been rendered as hyphens.

---

## 1. Summary table

| # | Rule or standard | Status (Nov 2026) | Who it binds | Product without an EPD: what happens | Fixed uplift on generic data? |
|---|---|---|---|---|---|
| 1 | RICS PS *Whole life carbon assessment for the built environment*, 2nd ed. (Sept 2023, v3 Aug 2024) | MANDATORY for RICS members from 1 July 2024; used by reference in GLA, UKNZCBS, BREEAM, local plans | RICS members doing WLCAs; anyone using a scheme that cites it | Data hierarchy: product EPD, then collective/sector EPD, then generic national database (BECD as first point of reference). Generic data scores lower in a carbon data confidence matrix | **No per-product uplift.** An asset-level "carbon data uncertainty factor" of 0% to 7% is added to modules A to D (excl. B6 to B8), driven by the confidence score of the ten most impactful products. Plus a 15% / 6% / 0% contingency by stage (applies regardless of data type) |
| 2 | London Plan 2021 Policy SI 2 Part F + GLA WLC LPG (March 2022) | MANDATORY for referable applications in London (planning) | Applicants for referable schemes | Ordered list of acceptable data sources, EPDs first; "sector level data" if manufacturer has not provided data; generic (ICE) as fallback for MEP not covered by TM65 | No |
| 2b | Draft London Plan 2026, Policy GHR3 | PROPOSED (published 16 July 2026; consultation closed 15 Oct 2026; adoption expected early 2028) | Referable applications | Adds upfront carbon targets (500 / 700 / 700 kgCO2e/m2) on top of WLC reporting | No uplift found |
| 3 | UK Net Zero Carbon Buildings Standard (UKNZCBS) Version 1, Rev 1 | VOLUNTARY (v1 published 10 March 2026; verification launched July 2026) | Projects claiming "net zero carbon aligned" | Mandatory 11-box data selection flowchart (Figure 8). Generic data point used only where no national manufacturer/group EPD. Must apply the RICS WLCA uncertainty factor. Extra reporting-only assessment using IStructE default values for concrete, steel and aluminium | No per-product uplift; RICS uncertainty factor applies |
| 4 | BREEAM UK New Construction V7 / V7.1 (and 2018 "v6") Mat 01 / Mat 02 | VOLUNTARY (client choice; often a planning or funder condition) | Projects seeking BREEAM | Mat 01: whole-building LCA (generic data allowed). Mat 02: EPD points (product-specific EPD 1.5 points; 20 points = 1 credit) | No uplift; EPDs rewarded by a separate credit |
| 5 | Part Z / national embodied carbon regulation | NOT IN LAW. Industry proposal. Government (March and Oct 2026) declines to mandate WLCA "at this time" | Nobody | n/a | n/a |
| 5b | Future Homes and Buildings Standards (S.I. 2026/335, laid 24 March 2026, in force 24 March 2027) | MANDATORY (operational energy only) | All new homes and buildings in England | Embodied carbon out of scope | n/a |
| 6 | Local plans (B&NES SCR8, Reading CC2, Westminster Policy 43, Greater Cambridge draft) | MANDATORY where adopted (planning); some PROPOSED | Major schemes above thresholds | B&NES post-completion condition requires "List of product-specific EPDs for the installed products and materials". ICE allowed only "until RIBA Stage 2" | No |
| 6b | Public sector (NHS Net Zero Building Standard; DfE; NISTA handbook; PAS 2080) | MANDATORY as client requirements (NHS, DfE); guidance (NISTA, PAS 2080) | Public projects | NHS: default carbon assumptions to be used absent better data; "uplift factors are used where necessary"; warns against "best-case assumptions" | NHS mentions uplift factors but sets no fixed figure |
| 7 | Generic data sources (ICE, One Click LCA generic / GCD UK, Green Guide) | n/a | n/a | ICE no longer licensed for commercial use after 30 Sept 2026; One Click LCA's UK GCD averages UK EPDs ("typical product"); Green Guide withdrawn from current BREEAM | One Click LCA global generic data described by One Click LCA as "conservative"; no UK fixed uplift |
| 8 | Construction Products Reform (Green Paper Feb 2025; White Paper Feb 2026) | PROPOSED regime; EPDs to stay VOLUNTARY for products outside designated standards | Manufacturers | Government "concluded that government action to introduce a mandatory approach ... is not needed at this time" | n/a |
| Nordic comparison | Sweden (Boverket climate declaration), Finland (CO2data) | MANDATORY national regulation | All new buildings in scope | Generic data must come from the national database, which is deliberately inflated | **Yes: about 25% (Sweden), 20% (Finland)** |

---

## 2. RICS Professional Standard, 2nd edition

**Source:** RICS, *Whole life carbon assessment for the built environment*, Global, 2nd edition, September 2023, Version 3 issued August 2024, "Effective from 1 July 2024". PDF: https://www.rics.org/content/dam/ricsglobal/documents/standards/Whole_life_carbon_assessment_PS_Sept23.pdf (text extracted and read in full for the sections cited). Status: **MANDATORY** for RICS members ("in full effect from 1 July 2024, RICS members need to follow the 2nd edition standard's requirements", RICS standard page https://www.rics.org/profession-standards/rics-standards-and-guidance/sector-standards/building-surveying-standards/whole-life-carbon-assessment-2nd-edition). No 3rd edition or 2026 revision found; the April 2026 RICS-led CLEAR coalition "is not designed to produce a new standard" (https://www.rics.org/news-insights/current-topics-campaigns/sustainability/clear, via search summary; UNVERIFIED wording).

### 2.1 Data hierarchy

Section 4.7: "The BECD has been developed to provide an up-to-date list of generic and specific carbon data for the UK, including environmental product declarations (EPDs). For the UK, the BECD should be used as a first point of reference to identify carbon data for construction materials and products."

"Any EPD should be independently verified according to ISO 14025, with third-party verification preferred. EPDs using EN 15804 and ISO 21930:2017 are preferred."

Table 8 (A1 to A3 data by project phase):
- Early design: "Generic carbon factors."
- Technical design and construction: "Specific carbon factors from EPDs where products/systems are specified or purchased during construction phase." and "If EPDs are not available, use generic carbon factors (appropriate national carbon factors from accepted industry databases)."
- Post-completion: "Specific carbon factors from EPDs for the actual products/systems used." with the same fallback.

Section 4.7.2: "For a construction or post-completion phase assessment, the first choice should be an EPD from the chosen manufacturer that covers the actual product used. If this is not available, the selection of data should be similar to the approach needed earlier in the project ... the most representative type of generic data for a material or product would be a collective EPD from all the members of the appropriate regional industrial sector ... If a collective EPD is not available, generic data from a geographically relevant database would be appropriate. The BECD is intended to be a source of generic data for the UK."

"If no average or collective EPDs or generic data are available, a specific EPD from the region could be used as a proxy for a generic product, but this will affect the data confidence scores ..."

Note for the campaign: RICS treats a sector-average (trade association) EPD as "generic data" in the hierarchy. A manufacturer without its own EPD is therefore usually represented by its trade association's average EPD where one exists, not by a penal value.

### 2.2 Uplift, contingency and conservative factors

RICS does **not** require a conservative or inflated value for an individual product lacking an EPD. It requires an asset-level "WLCA uncertainty factor" made of three parts (section 4.10):

1. Contingency factor (Table 10): early design (RIBA 0 to 2) **15%**; technical design and construction (RIBA 3 to 5) **6%**; post-completion (RIBA 6) **0%**. Applies whatever data is used.
2. Carbon data uncertainty factor (section 4.10.2): "It reflects uncertainty regarding the representativeness of the carbon data in relation to the impact of the actual products that will be used, and the quality of the data. **It should be high when generic data is used in any phase, and should be low when specific data for the actual products is used.** It is calculated using the asset data confidence score, based on the representativeness of ten key datasets."
3. Quantities uncertainty factor (0% to 4%, Table 14).

Key products: "the ten most impactful products or materials in terms of the percentage of the asset's embodied carbon impact (modules A1-A5, B1-B5, C1-C4)."

Table 11 scores each key dataset out of 40 (geography 10, technology 6, product specificity 6, temporal 8, granularity 5, verification 5). Table 12 converts the impact-weighted average score into an uplift:

| Asset carbon confidence score | ≤10 | 10<15 | 15<20 | 20<25 | 25<30 | 30<35 | 35<40 | 40 |
|---|---|---|---|---|---|---|---|---|
| Carbon data uncertainty factor | 7% | 6% | 5% | 4% | 3% | 2% | 1% | 0% |

"the carbon data uncertainty factor must be applied to all modules A-D before reporting upfront, embodied, operational and user carbon". Worked example: "6% + 4% + 1% = 11%", added "to all modules except B6, B7 and B8".

Indicative scores (Appendix B, Table B2, "for UK-produced product" assessed in 2023):
- Product- and manufacturer-specific EPD (2022): 40/40
- Manufacturer-specific EPD for product group: 35
- National average product EPD: 33
- EU average product EPD: 25
- ICE database V3 2019 (main materials): 21 to 23
- ecoinvent/GaBi data for similar EU product: 23
- Proxy EPD from European country: 20
- TM65 generic datapoint: 15
- ICE V3 2019 (other materials based on V2 2011): 13

Implication: if all ten key products used generic data scoring about 20 to 23, the asset would take roughly a 4% to 5% carbon data uplift; with product-specific EPDs for all key products, 0%. The penalty is applied to the whole building total, is capped at 7%, and depends only on the ten most impactful products, so a single minor product without an EPD has little or no measurable effect.

The only RICS text using "conservative" in a data sense concerns scenarios: "If there is a range of scenarios, the most conservative ..." (section on scenarios) and "conservative scenario should be used" (Appendix). Not a rule on generic product data.

### 2.3 Reporting of data sources

"The WLC assessor must explicitly state the data source in the WLCA report, and for generic data the territorial scope and basis (consumption- or production-based) ..."

"During the technical design, construction and post-completion phases, the asset carbon confidence score produced using this method must be reported in the WLCA report, together with the percentage of the asset's overall upfront and embodied carbon for which the key products are responsible." "The contingency factor(s) used must be reported in the WLCA report."

MEP: "For MEP products where no specific EPDs are available, the CIBSE TM65 method should be used".

---

## 3. London Plan Policy SI 2 and GLA WLC guidance

**Source:** GLA, *London Plan Guidance: Whole Life-Cycle Carbon Assessments*, March 2022. PDF: https://www.london.gov.uk/sites/default/files/lpg_-_wlca_guidance.pdf (read in full). Guidance page: https://www.london.gov.uk/what-we-do/planning/implementing-london-plan/london-plan-guidance/whole-life-cycle-carbon-assessments-guidance (returned HTTP 403 in this session).

### 3.1 Who must submit (MANDATORY, planning)

"All applications for referable development (outline, detailed and/or hybrid applications) are required to submit a Whole Life-Cycle Carbon (WLC) assessment." "WLC assessments for non-referable major development are encouraged." Referable thresholds are set by the Mayor of London Order 2008 (for example 150 or more homes, or buildings over 30 m outside the City) (UNVERIFIED in this session; general knowledge).

### 3.2 Stages

Para 2.2.1: "pre-application (where relevant)"; "planning application submission (i.e. RIBA stage 2/3)"; "Post-construction (i.e. prior to occupation of the development. Generally, it would be expected that the assessment would be received three months post-construction)". Post-construction evidence includes "contractor confirmation of as-built material quantities and specifications".

The guidance is based on RICS PS 1st edition (2017). A search summary of the GLA page states applicants "can additionally provide assessments in accordance with second edition methodology if they wish" (UNVERIFIED: page blocked).

### 3.3 Treatment of product data and EPDs

Para 2.7.1: "The following are acceptable sources of carbon data for materials and products (or the latest available versions) in order of preference:
- verified Type III EPDs in accordance with BS EN 15804 2012+A1:2013 or A2:2019
- verified Type III EPDs in accordance with ISO 21930: 2017
- verified Type III EPDs in accordance with ISO 21930: 2007
- third-party (independently) verified, or peer-reviewed, carbon emissions to ISO 14067 ...
- verified Type III EPDs in accordance with ISO 14025
- peer-reviewed Life-cycle Carbon Assessment studies in accordance with ISO 14044
- independently verified or peer-reviewed carbon emissions to PAS 2050:2011 ..."

Para 2.7.2: "Applicants should use data from the manufacturer of the actual materials and products being used, following the order of preference above. If the manufacturer has not provided data or it is too early in the design process for the manufacturer to be known, then sector level data (e.g. EPDs that use data covering several manufacturers) should be used."

MEP: "Applicants should use the default material carbon data in TM65 if product-specific carbon data is not available. For any materials that are not covered by TM65, applicants should use generic data sources which follow the EN15804 methodology e.g. the ICE Database v3. If data following this methodology is not available then other generic data sources should be used e.g. older versions of the ICE Database v2. The final resort would be to use specific data from other manufacturers for similar products."

Reporting (Box 4): "software tool used, type of EPDs used." Reserved matters: "update any default values used as far as possible." No uplift or penalty on generic data.

### 3.4 Benchmarks (comparison only, not limits)

Appendix 2: "The WLC benchmarks should be used as a guide by all applicants." Aspirational benchmarks "are based on a 40 per cent reduction". Example (offices): A1 to A5 "<950" kgCO2e/m2 GIA, aspirational "<600"; B to C "<450", aspirational "<370". Residential A1 to A5 <850 (aspirational <500) per GLA evidence base summary.

### 3.5 New London Plan (draft 2026)

- Draft London Plan published 16 July 2026; consultation closed 15 October 2026; "adoption expected in early 2028" (Elmhurst Energy, 14 Sept 2026, https://www.elmhurstenergy.co.uk/blog/2026/09/14/draft-london-plan-2026-signals-major-changes-to-energy-standards-for-new-developments/). Status: **PROPOSED**. The GLA consultation page returned HTTP 403, so dates are from secondary sources (consistent across Turley, Etude, Hawkins\Brown, Max Fordham).
- Policy SI 2 is replaced by GHR1 to GHR4; whole life-cycle carbon becomes **Policy GHR3**. "For referable applications, developers would be required to assess opportunities to retain existing buildings and structures, demonstrate how upfront embodied carbon has been reduced through design and material efficiency, and calculate and report whole life-cycle carbon emissions." (Elmhurst).
- Proposed baseline upfront targets: "500 kgCO2e/m2 for residential buildings under 11 metres"; "700 kgCO2e/m2 for residential buildings 11 metres and above"; "700 kgCO2e/m2 for Use Class E (commercial)" plus aspirational targets (Hawkins\Brown webinar summary, https://www.hawkinsbrown.com/news/towards-a-new-london-plan-exploring-the-evidence/; Turley, 28 July 2026, https://turley.co.uk/latest/comment/decoding-draft-london-plans-greener-ambitions). Draft plan text itself not read (file exceeded fetch size): exact policy wording UNVERIFIED.
- GLA evidence base (*Towards a new London Plan: Evidence base for embodied and whole life carbon policies*, September 2025, https://data.london.gov.uk/download/2yoq5/127/LPNZ%20Evidence-Embodied%20carbon.pdf, read): "Performance level 3 is in line with UK Net Zero ..." and "The UKNZCBS 2025 limit of 565 kgCO2e/m2 (GIA) for flats". On data: "Going forwards data quality will improve, but reported emissions may rise as calculations get more accurate." Equality impact table: "The policy will require building material suppliers and manufacturers to provide robust and up-to-date carbon calculations and certifications for their products. This will incur a cost for businesses, many of which will be SMEs in London".
- No EPD uplift or generic-data penalty found in the draft policy summaries.

---

## 4. UK Net Zero Carbon Buildings Standard (UKNZCBS)

**Source:** *UK Net Zero Carbon Buildings Standard*, Version 1, Rev 1, April 2026, PDF via https://www.nzcbuildings.co.uk/the-standard (file https://www.nzcbuildings.co.uk/_files/ugd/790941_c050829805364847b15590dc1d579b2d.pdf, read).

### 4.1 Status

"Version 1 was published in March 2026, with verification launched in July 2026." "The UK Net Zero Carbon Buildings Standard is a voluntary standard applicable to new build, existing buildings and retrofits." (nzcbuildings.co.uk). Publication date 10 March 2026 (Circular Ecology news, 11 March 2026). Status: **VOLUNTARY**, but upfront carbon limits are pass/fail for anyone claiming conformity.

### 4.2 Embodied carbon limits

Table 3: pass/fail "Upfront carbon limits"; "Life cycle embodied carbon limits (future versions only)"; reporting metrics include "Upfront carbon with generic material specifications". Section 5.1.6.1: "Where 'whole building' limits in Tables EC-1 and EC-2 (see Annex A) for the works type and sector ... those limits shall not be exceeded." Limits vary by Date of Commencement. Example values cited by the GLA evidence base: flats 565 kgCO2e/m2 GIA (2025); office shell and core 475 kgCO2e/m2 GIA (Annex A tables not machine-readable in this session; values UNVERIFIED against Annex A).

### 4.3 Rules on generic data vs EPDs

Section 5.1.4: "The assessment methodology shall be according to the RICS PS ... The assessment shall account for the RICS PS 'WLCA uncertainty factor' (see section 4.10 of the RICS PS), noting that this is added at the end after the total embodied carbon is assessed in each lifecycle module."

"NOTE Most of the requirements in this section follow a hierarchical approach, prioritising the highest quality data (e.g., product-specific EPDs, as-delivered material quantities) but allowing relaxations where this is not available."

Section 5.1.4.3: "The carbon data used for construction products/materials and systems for life cycle module A1-A3 shall be according to the flowchart provided in Figure 8." Figure 8 (read from the rendered page), in order:
- BOX 1: EPD from the actual manufacturer covering the actual site and product, or a group EPD from the country that includes the actual manufacturer: "Use this EPD".
- BOX 2: group EPD in the country not representative of the manufacturer (e.g. not a trade association member) but allowing use by it.
- BOX 3: "Is there a national generic data point from the country where the actual product is manufactured?" then "Use this generic data point".
- BOX 4: sector EPD for wider region (EU etc.).
- BOX 5: generic dataset from another country with similar technology.
- BOX 6: manufacturer Bill of Materials, then CIBSE TM65 (MEP) or CWCT methodology (non-MEP), or ISO 14067 / PAS 2050 PCF.
- BOX 7 to 11: EPDs (or averages of EPDs) from other manufacturers for the same type of product.

Requirement 2: "For the calculation of the carbon data uncertainty factor, if the EPD is for a key product (see section 4.10 of the RICS PS) then the EPD shall be considered as a proxy EPD for this product, as the actual manufacturer is not covered by the EPD". "EPD ... shall be independently verified according to ISO 14025, and use EN 15804 or ISO 21930".

Section 5.1.2.6 (reporting only): "An additional upfront carbon assessment shall be completed ... replacing A1-A3 carbon factors with the recommended default values given in IStructE How to Calculate Embodied Carbon for ... All structural concrete ... All structural steel ... All façade aluminium and structural aluminium". "The results shall not be compared with limits." Purpose: "to identify the extent to which meeting the upfront carbon limits was dependent on the use of lower carbon material specifications."

Key product reporting: "key product/material information shall be reported according to the requirements of the Submission Proforma (see Annex B)."

### 4.4 Is product-specific data required?

No. EPDs are not mandated; the flowchart permits national generic data where no manufacturer or group EPD exists. Through the RICS uncertainty factor, lack of EPDs for key products raises the assessed figure modestly. Whether the uncertainty-inclusive figure is the one compared with limits is implied by 5.1.4 but not stated explicitly in the text read (UNVERIFIED; check verification guidance).

### 4.5 One Click LCA article (requested)

**Source:** One Click LCA, "How Environmental Product Declarations (EPDs) support UKNZCBS conformity: A guide for UK specifiers", https://oneclicklca.com/en-gb/resources/articles/epds-and-uknzcbs-a-guide-for-uk-specifiers-one-click-lca (page dated 13 July 2026 on the page; search index shows 6 July 2026).

Quotes:
- "UKNZCBS verification requires whole life carbon assessment aligned with the RICS Whole Life Carbon Assessment (WLCA) second edition methodology. That methodology establishes a clear data hierarchy. Manufacturer-specific data, in the form of third-party verified Environmental Product Declarations (EPDs), sits at the top. Industry average EPDs come next, and generic database values are the fallback."
- "When a specified product lacks an EPD, the assessor uses generic database values. Those values are typically conservative, derived from older or averaged production data, and tend to overestimate the impact of a specific manufacturer's product."
- "This methodology requires data quality scoring for the highest-impact materials in an assessment. Consistently low data quality scores increase uncertainty in the model and increase the likelihood of a project exceeding the upfront carbon limit, even on a well-designed scheme."
- FAQ: "The UKNZCBS does not mandate EPDs directly, but they can be beneficial. It requires RICS WLCA v2-aligned whole life carbon assessment, which places manufacturer-specific EPDs at the top of its data hierarchy. Without them, conservative generic values apply, making it harder to meet the upfront carbon limit."
- Cites NFRC: "generic default values apply, and these are typically conservative, making it harder for projects to meet the standard."

Accuracy check: the claim that generic values are "typically conservative" is **not** stated in the RICS standard or UKNZCBS text. Its stated source is the NFRC paper (below), which itself gives no evidence. The data-quality-scoring statement is accurate (RICS 4.10.2). The article does not mention any numeric uplift.

**NFRC position paper** (1 April 2026), https://www.nfrc.co.uk/static/20833f00-b451-4423-835b1dec2116e204/NFRC-UKNZCBS-Position-Paper-Final.pdf: "Where product-specific EPDs are unavailable, assessors must use generic default data. Generic values are typically conservative and can produce higher embodied carbon figures, making it harder for projects to meet the standard." (Trade body opinion; no data cited.)

---

## 5. BREEAM UK New Construction (V7 and 2018 "v6")

- V7 launched 30 September 2025 (Emidat blog, 28 Aug 2026, https://www.emidat.com/blog/how-epds-score-in-breeam; UNVERIFIED against BRE). BRE *BREEAM UK New Construction: Commercial Version 7.1 Technical Standard Summary* (https://files.bregroup.com/breeam/V7/3A%20BREEAM%20UK%20New%20Construction%20Commercial%20Version%207%20Technical%20Standard%20Summary.pdf, read) lists materials topics: "Building life cycle assessment with embodied carbon reporting requirements including MEP services." and "Environmental product declarations for critical building components". Minimum standard at the top rating: "All project stage LCA and embodied carbon reporting - 5 credits (Mat 01)". Status: **VOLUNTARY**.
- Mat 01 V7 guidance: GN51 "provides supporting information for the new Mat 01 criteria in BREEAM V7", v1.1 released 28 October 2026 (https://kb.breeam.com/us/knowledgebase/gn51/). Full text not accessible (licensed). V7 consultation (Oct 2023): credits based on performance against upfront or embodied carbon benchmarks; submission to BECD proposed (search summary of https://files.bregroup.com/breeam/BREEAM-Consultation_Document_V7.pdf; UNVERIFIED wording).
- Mat 02 (EPD credit), BRE wording (https://bregroup.com/services/standards/environmental/en-15804-environmental-product-declaration-epd): "Up to 1.5 EPD points are available for each construction product EPD specified" and "one credit is available for assessments that achieve an EPD points score of at least 20." Mat 01 in the same page: "Seven credits are available in this section including two credits for building performance against a benchmark." (scheme version not stated; likely 2018/v6).
- Mat 02 aim (BREEAM UK NC 2018 manual, https://files.bregroup.com/breeam/technicalmanuals/NC2018/content/09_material/mat02.htm): "To encourage availability of robust and comparable data on the impacts of construction products through the provision of EPD."
- Points by EPD type (secondary, consistent across sources): industry EPD 0.5; manufacturer product-category EPD 0.75; product-specific EPD 1.5; "Points are capped at four per category" (Emidat, describing V7). V7 primary text UNVERIFIED.
- BREEAM does not apply any uplift to generic data in Mat 01. EPDs are rewarded directly via Mat 02. Green Guide: "withdrawal of the Green Guide methodology in the current version of BREEAM UK New Construction" (BREEAM KB KBCN1466, https://kb.breeam.com/knowledgebase/green-guide-updated-validity-requirements/).

---

## 6. Part Z, the government embodied carbon position, and the Future Homes Standard

### 6.1 Part Z

Industry-drafted amendment to Schedule 1 of the Building Regulations 2010 (first published July 2021) with draft Approved Document Z: Z1 mandatory WLCA reporting for major projects, Z2 later upfront carbon limit. Status: **NOT LAW, no government commitment, no timetable.** A 2 November 2026 summary: "Government has not adopted it and has set no timetable for embodied carbon regulation." and no consultation on embodied carbon regulation was found "when we checked on 2 November 2026" (https://netzero.co.uk/blogs/part-z-explained-will-embodied-carbon-limits-become-law, secondary). Draft AD Z approach: generic factors pre-construction, then "Update the assessment with final material quantities and environmental product declarations (EPDs)" (same source; Part Z primary text not re-read).

### 6.2 Government response, March 2026 (primary)

House of Commons Environmental Audit Committee, *Environmental sustainability and housing growth: Government Response*, Eighth Special Report of Session 2024-26, HC 1785, published 13 March 2026 (response received 3 March 2026), https://publications.parliament.uk/pa/cm5901/cmselect/cmenvaud/1785/report.html (read):

- Para 72: "The Government is not currently considering adopting the RICS methodology as the UK industry standard for whole-life carbon assessments. However, we acknowledge this recommendation and will keep it under review."
- Para 73: "Mandating carbon assessments would introduce significant challenges for many local authorities and developers, creating disproportionate burdens and delays. ... Therefore, we currently intend to maintain a voluntary approach to the use of carbon accounting, and have instead committed to updating the Planning Practice Guidance ..."
- Para 82: "we do not agree with mandating whole life carbon assessments at this time".
- Para 84 (on the committee's call for an embodied carbon consultation by March 2026): "The commitment to conduct a consultation on the measurement of embodied carbon was made under the previous government. The Government is taking the time to properly review the available evidence and consider policy options. ... We continue to assess the evidence to consider the best way forward for measuring and reducing embodied carbon in new buildings."
- Para 76: MHCLG "commissioned research" (AECOM, *Consideration of embodied carbon in new buildings*, published July 2025).

### 6.3 Latest position (October 2026)

Written answer by the MHCLG Minister of State, 15 October 2026 (to question 31357 tabled 9 October 2026): "We have published the final report, Consideration of embodied carbon in new buildings, to share the insights with industry. The Government is considering its next steps on this matter carefully." (via https://westminsterbrief.co.uk/archive/pq/2026-10-09/31357, secondary mirror of the Parliament written answer; UNVERIFIED against questions-statements.parliament.uk). A Commons debate on embodied carbon took place on 13 July 2026 (Hansard page returned 403; content UNVERIFIED).

**Conclusion:** As of 11 November 2026, the UK government has **not** consulted on embodied carbon regulation, has **not** committed to mandatory WLCA, and has stated it intends to keep a voluntary approach.

### 6.4 Future Homes and Buildings Standards (March 2026)

- The Building Regulations etc. (Amendment) (England) Regulations 2026 (S.I. 2026/335) "were laid on 24 March 2026, and will come into force on 24 March 2027" (MHCLG circular, https://assets.publishing.service.gov.uk/media/69c2aa1ebd142c66ffe44373/FHBS_Circular.pdf). **MANDATORY** (operational energy).
- Government consultation response (March 2026, https://assets.publishing.service.gov.uk/media/69c13592bb0dfe55b83e4b85/Future_Homes_and_Buildings_Standards_Consultation_Response.pdf): "There were several comments beyond the scope of this consultation, such as requests for embodied carbon to be regulated in the Building Regulations." Embodied carbon is outside the standard. Also: "We have decided not to proceed with a Future Homes Standard brand."
- Future Homes Hub (industry, **VOLUNTARY**): aims to "Encourage voluntary measurement and disclosure of upfront and whole life embodied carbon" and to "Engage with manufacturers and the supply chain to ensure that EPDs and relevant default assumptions are increasingly available" (https://www.futurehomes.org.uk/embodied-and-whole-life-carbon). A 2026 update to the Hub's WLC Conventions added site infrastructure (specificationonline.co.uk, 24 July 2026; secondary).

---

## 7. Local plans outside (and inside) London, and public sector requirements

### 7.1 Bath and North East Somerset (B&NES) Policy SCR8 (MANDATORY, adopted January 2023)

- "Policy SCR8 requires developments demonstrate a score of less than 900kgCO2e/m2 can be achieved within the development for the substructure, superstructure and finishes." Applies to "50 dwellings or more; or 5000m2 of commercial floor area". "The embodied carbon assessment must be third party verified" (https://www.bathnes.gov.uk/policy-and-documents-library/embodied-carbon-assessment).
- Sustainable Construction Checklist SPD (https://www.bathnes.gov.uk/sites/default/files/2024-12/Sustainable%20Construction%20Checklist%20SPD%20finalCS.pdf): scope modules A1 to A5; submitted at "Planning application stage (RIBA Stage 3)" and "Post-construction/handover stage".
  - Para 4.63: "Preferable data sources for embodied carbon calculations are: Environmental-product declarations (EPDs) ... The University of Bath ICE database ... Proprietary data and databases".
  - Para 4.69 acceptable sources: "ICE database (until RIBA Stage 2)" followed by verified EPDs (EN 15804, ISO 21930, etc.).
  - Para 4.76: report "Type of EPDs used".
  - Model post-completion condition evidence includes: "**List of product-specific EPDs for the installed products and materials**".
- Draft new Local Plan (2025) proposes more stringent embodied carbon targets (B&NES Cabinet report; PROPOSED; values UNVERIFIED).
- A University of Bath evaluation (Dec 2025, https://doi.org/10.15125/bathro-377855006) found eligible projects met 900 kgCO2e/m2 "by a large margin".

### 7.2 Cornwall Climate Emergency DPD (adopted 21 February 2023)

Policy SEC1 (applies from 15 June 2023) sets operational energy targets (space heating <30 kWh/m2/yr, total energy <40 kWh/m2/yr, on-site renewables) and BREEAM Excellent for major non-residential (https://www.cornwall.gov.uk/climateemergencydpd; Inspector's report). Materials clause asks proposals to minimise materials and consider "the life cycle of development". **No embodied carbon limit or mandatory WLCA found** in Cornwall; it is not a useful EPD example.

### 7.3 Others

- **Reading** Local Plan Partial Update (submission draft May 2025, examination 2026; PROPOSED): "All applications for new-build commercial floorspace of 5000m2 or more must include an embodied carbon assessment. This assessment must demonstrate that a score of less than 800kg/m2 of carbon can be achieved within the development for the substructure, superstructure and finishes." (https://images.reading.gov.uk/2026/02/EX096-Policies-CC2-and-H5-clean-version-as-proposed-to-be-amended-in-Hearing-Statements.pdf).
- **Westminster** City Plan Policy 43 (Retrofit First) guidance (https://westminster.moderngov.co.uk/documents/s70111/PED26-02%20Appendix%20B%20-%20Retrofit%20First%20Guidance%20Addendum%20Adoption%20Version.pdf): "all major schemes, and all non-major schemes involving substantial demolition ... submit a Whole Life Carbon Assessment. The Whole Life Carbon Assessment must be compliant with the RICS Whole Life Carbon Assessment (WLCA) Standard, 2nd Edition." Limits: commercial 650 (aspirational 550) kgCO2e/m2; residential/hotels over 18 m 700 (600); under 18 m 650 (550). Adoption January 2026 per a secondary source (UNVERIFIED).
- **Greater Cambridge** draft Local Plan (Dec 2025, PROPOSED): "All major development must calculate whole life carbon emissions through a nationally recognised whole life carbon assessment tool and demonstrate actions to reduce up-front embodied carbon emissions (modules A1-A5 of the RICS methodology)".
- Written evidence to Parliament reports "26 LPAs ... (with 17 of these LPAs outside of London) are requiring, or about to require, WLCAs" and limits in South Oxfordshire and Vale of White Horse, Enfield, Bristol, Newham, North Somerset, Wealden, Welwyn Hatfield and Westminster (https://committees.parliament.uk/writtenevidence/133084/html/; not individually verified).
- Constraint: B&NES notes "Government has said that local authorities cannot use local policies to set more stringent or ambitious targets than the Future Homes Standard" (operational energy); this does not directly cover embodied carbon.

None of these local policies applies an uplift to generic data.

### 7.4 Public sector procurement

- **NHS Net Zero Building Standard** (NHS England, February 2023, https://www.england.nhs.uk/wp-content/uploads/2023/02/B1697-NHS-Net-Zero-Building-Standards-Feb-2023.pdf). Applies to "all investments in new buildings and upgrades to existing facilities that are subject to HM Treasury business case approval" (Health Estate Journal). **MANDATORY** for those projects: "mandatory whole life-cycle assessments, Upfront Carbon Limits". On data: para 4.4 "uplift factors are used where necessary to make an informed allowance ..." and "where data is lacking, the Design Team ... proactively engage with the supply chain to accelerate industry data availability, e.g. through all suppliers providing EPD information." Para 6.76: baseline default values "should be used by the Project Team in absence of more accurate information". Para 6.77: "avoiding manipulation of assessments using best-case assumptions". Para 6.81: designers should "ensure this risk is mitigated through early engagement with the supply chain and representative data used in carbon calculations." Tier 1 elements are those with "robust EPD data". No fixed uplift percentage.
- **Department for Education**: School Output Specification Technical Annex 2J (November 2022): "the Contractor shall report on Embodied Carbon in Construction using EN15978" and "There is no requirement for projects to achieve a set standard for Embodied carbon, but Embodied carbon reporting forms part of the DfE's EIR and is required at RIBA Stages 4 and 6." NISTA handbook (March 2026) says DfE's new Design Standards "require whole life carbon reporting throughout project design and delivery using a carbon reporting template and supported with product-specific information from industry" (DfE primary text UNVERIFIED).
- **NISTA** *Whole Life Carbon Management Handbook for the Built Environment*, March 2026 (https://assets.publishing.service.gov.uk/media/6a4b7a7e8effd97622f53d4c/NISTA_Whole_Life_Carbon_Management_Handbook_2026.pdf), good practice guidance (**VOLUNTARY**): "For bottom-up assessments and development of as-built benchmarks EN 15804:2012 for Environmental Product Declaration (EPD) should be utilised"; "the value chain must provide the necessary information to those undertaking the WLC assessment. This could include design information, EPDs, bills of materials ..."; "The RICS WLCA Professional Statement is a standard for WLC assessment, recognised in the UK as being compliant with the requirements of PAS2080:2023."
- **PAS 2080:2023** (BSI, second edition March 2023, effective 31 March 2023): requires value chain members to "seek to improve the accuracy of their assessment(s), to neither overestimate nor underestimate actual emissions". Note: PAS 2080 explicitly rejects deliberate overestimation. **VOLUNTARY** unless contractually required (widely required by infrastructure clients; UNVERIFIED which).
- **Crown Commercial Service**: no CCS rule requiring product EPDs was found (UNVERIFIED). PPN 06/21 carbon reduction plans are corporate, not product-level. DESNZ (2026) says voluntary low carbon procurement requirements will be added to the Government Buying Standards for Buildings.

---

## 8. Generic data sources and "conservative" statements

### 8.1 ICE database (Circular Ecology)

- Latest: "ICE Database Educational V5.0 - June 2026". "Non-educational use of the ICE Database or its underlying data is no longer permitted as of 30th September 2026." Commercial successor IC+ launched 22 October 2026; "The factors represent typical materials rather than specific branded products." (https://circularecology.com/embodied-carbon-footprint-database.html; https://circularecology.com/news/icplus-launch-embodied-carbon-database-for-professional-use).
- IStructE (29 Sept 2026): its *How to calculate embodied carbon* defaults are partly based on ICE; "The Institution continues to recommend the use of generic industry-average data during early design stages" (https://www.istructe.org/resources/news/changes-to-ice-database-access/).
- No statement found that ICE values are deliberately conservative. RICS Table B2 scores ICE V3 at 13 to 23 out of 40 (low confidence).

### 8.2 One Click LCA generic data

- Global generic data (help article, 25 March 2026, https://help.oneclicklca.com/en/articles/275910-generic-materials-data-production-at-one-click-lca): "One Click LCA generic materials are modelled to be usable globally, representing average production methods and technology. For this reason, material and energy inputs are global and not specific to your country. This is a conscious choice to make One Click LCA generic materials both available globally and conservative in terms of environmental impacts. In other words, you can expect somewhat higher environmental impacts from a One Click LCA generic material than from an actual EPD applicable to your country."
- UK-specific: *Generic Construction Data (GCD), UK edition* (https://help.oneclicklca.com/en/articles/844227-generic-construction-data-gcd-uk-edition): 836 UK datasets, "One Click LCA's recommended replacement for the ICE datasets, which One Click LCA deactivated on September 30, 2026." Method: "a statistical average of valid, third-party verified EPDs for comparable products in the UK, with outliers excluded. **The result represents a typical product in that category.**"
- Implication: for UK assessments in One Click LCA after 30 September 2026, generic values for main materials are UK averages, not deliberately conservative. The "conservative" statement applies to the global generic library, not to GCD UK.

### 8.3 BRE Green Guide

"withdrawal of the Green Guide methodology in the current version of BREEAM UK New Construction" (BREEAM KB KBCN1466). BRE: "They are generic rankings that illustrate a range of typical materials." (https://bregroup.com/products/green-guide). Not a current route for UK WLC.

### 8.4 Other generic sources

BECD (RICS "first point of reference" for UK); BRE IMPACT database; CIBSE TM65 (MEP); IStructE default values (used in UKNZCBS reporting-only generic specification assessment); UKGBC prototype generic materials database (Oct 2025, "generic rather than project-specific").

### 8.5 Nordic comparison (for contrast)

- Sweden, Boverket climate database (https://www.boverket.se/sv/klimatdeklaration/klimatdatabas/om-klimatdatabas/): "Klimatdata för byggprodukterna i Boverkets databas är konservativt satta, det vill säga cirka 25 procent högre än genomsnittet för att stimulera användning av specifika klimatdata." Translation: climate data for construction products in Boverket's database are set conservatively, that is about 25% higher than the average, to stimulate use of specific climate data. Also: "tanken är att det aldrig ska vara en fördel att använda generiska klimatdata i stället för specifika klimatdata" (the idea is that it should never be an advantage to use generic data instead of specific data). Use of the database is mandatory for generic data in the legally required climate declaration.
- Finland CO2data: 20% conservative top-up (One Click LCA NollCO2 help article, https://help.oneclicklca.com/en/articles/374933-sverige-nollco2: "conservative top-up factors of 25 % for Boverket data and 20 % for CO2data"). Finnish primary source not checked (UNVERIFIED).

---

## 9. UK Construction Products Reform

- Green Paper, MHCLG, 26 February 2025 (consultation to May 2025), https://www.gov.uk/government/consultations/construction-products-reform-green-paper/construction-products-reform-green-paper-2025-html. Para 10.2: "there are currently no specific environmental requirements for products under the Construction Products Regulations (CPR)". Q54 asked whether environmental measures should be "mandatory or voluntary". Summary of responses: "There was also some support for mandatory Environmental Product Declaration/Life Cycle Assessment (EPDs/LCAs)."
- **White Paper**, MHCLG, February 2026 (consultation ran until 20 May 2026), https://assets.publishing.service.gov.uk/media/699c68cad2b9c6ec5b6fbbe8/Construction_Products_Reform_White_Paper.pdf (read):
  - Products under designated standards (**PROPOSED**): "We can confirm that the government intends to maintain consistency with the environmental aspects of the revised the EU-CPR 2024." EU-CPR requires manufacturers to "declare product performance against these essential environmental characteristics", phased "from 2026" with more from 2030 and 2032. Decisions on delegated acts "on a case-by-case basis".
  - Products not covered by designated standards: "We heard mixed views about whether government should introduce a mandatory or voluntary approach to presenting environmental data (e.g. by mandating Environmental Product Declarations)." Para 10.3.4: "**We have therefore concluded that government action to introduce a mandatory approach to environmental reporting and data for products not covered by a designated standard is not needed at this time.**" Para 10.3.6: "The standard itself or the need to produce an EPD for products not covered by a designated standard will remain voluntary." Government "will look for opportunities to raise awareness and encourage the use of EN 15804 +A2."
  - Para 10.3.5: "Construction products manufacturers are already being asked by their buyers for product level embodied emissions data, normally in the form of EPDs prepared in line with EN15804".
- DESNZ, *A policy framework to grow the market for low carbon industrial products: government response* (2026; exact month UNVERIFIED), https://assets.publishing.service.gov.uk/media/6a18151a916cd732dcdaac4a/low-carbon-products-government-response.pdf: Embodied Emissions Reporting Framework guidance "will initially be introduced on a voluntary basis"; "a mandatory EERF should only be explored once further work has been done on the interoperability between the CBAM and EERF"; "The government intends to publish buyer and producer guidance in 2027." Initial scope steel, cement, concrete.
- **Answer:** The UK will not require EPDs for most construction products. For products under designated standards it intends to mirror EU-CPR environmental declarations (timing tied to EU standards; UK implementing legislation not yet made). ASBP (May 2026) is "calling for a mandatory trajectory".

---

## 10. Notes for the campaign

1. **No UK rule assigns a deliberately inflated value to a product without an EPD.** RICS, GLA, UKNZCBS, BREEAM and local plans all fall back to sector-average EPDs or national generic data (BECD, ICE, GCD UK, TM65, IStructE defaults), which are designed to be typical or average.
2. **The verifiable penalty is the RICS carbon data uncertainty factor:** 0% to 7% added to the whole building's modules A to D (excl. B6 to B8), driven by the ten most impactful products. RICS says it "should be high when generic data is used". UKNZCBS makes this factor mandatory for conformity. It is real but small and diluted.
3. **"Average" cuts both ways for manufacturers.** A better-than-average product without an EPD is counted as average, so its advantage is invisible; a worse-than-average product is flattered. The honest UK message is "without an EPD you are counted as average and you add uncertainty", not "you are counted as worse".
4. **Where EPDs are explicitly required or rewarded:** B&NES post-completion condition ("List of product-specific EPDs for the installed products and materials"); BREEAM Mat 02 (1.5 points per product-specific EPD); UKNZCBS flowchart (proxy treatment where the manufacturer is not covered); NHS Tier 1 elements and supply chain EPD engagement; DfE "product-specific information from industry" (per NISTA).
5. **Caution on "conservative" claims:** The One Click LCA UKNZCBS article and the NFRC paper say generic values are "typically conservative", but no UK standard says so, PAS 2080 asks assessors "to neither overestimate nor underestimate", and One Click LCA's own GCD UK edition describes its UK generic data as representing "a typical product". Using the word "conservative" for UK generic data invites challenge. One Click LCA's global generic library is described by One Click LCA as conservative; that is the only defensible "conservative" source and it applies mainly where no UK-specific dataset exists.
6. **Regulatory outlook:** no national WLC mandate before at least 2027 to 2028; London's GHR3 (adoption expected early 2028) and local plans are the main levers; EU-CPR alignment is the main route to mandatory product declarations for exporters and designated-standard products.

---

## 11. Unverified or partially verified items

- GLA guidance page statement on optional RICS 2nd edition (page 403).
- Draft London Plan 2026 GHR3 exact text and numbers (from consistent secondary sources only).
- UKNZCBS Annex A numeric limits (565 / 475 kgCO2e/m2 taken from GLA evidence base).
- Whether UKNZCBS compares the uncertainty-inclusive figure with the limits (implied by 5.1.4).
- BREEAM V7 launch date (30 Sept 2025) and V7 Mat 02 point values (secondary only).
- Westminster Policy 43 adoption date (January 2026, secondary).
- 13 July 2026 Commons debate content and 15 October 2026 written answer (secondary mirror).
- DfE new Design Standards wording (quoted via NISTA).
- CCS product EPD requirements (none found).
- Finland CO2data 20% (via One Click LCA, not Finnish primary source).
- DESNZ low carbon products response publication month.
