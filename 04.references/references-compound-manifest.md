# Bibliography manifest

Provenance for every entry in `references-compound.bib`: where it came from, what could not be
extracted, and any disagreement between a filename and the text it names. Twenty-three entries at
5 August 2026, of which fifteen are cited in the manuscript.

## Verified against the source document

| Key | How verified | Notes |
|---|---|---|
| `murphy2026` | Text extracted from the publisher PDF, held locally and gitignored; see `grandfather-study/README.md` | Title, author order, affiliations, volume, article number and DOI all read from page 1. Note the published author order is Murphy, Leslie, Wilson, Banks, which differs from the pre-publication manuscript's Murphy, Leslie, Banks, Wilson |

## Verified against the CrossRef record

Added 5 August 2026 for the point process methods of `sec-interaction`. Neither PDF was read; the
metadata is the publisher's own deposited record, queried by DOI, which is a stronger source than a
PDF header for volume and pagination.

| Key | How verified | Notes |
|---|---|---|
| `berman1992` | CrossRef API, DOI `10.2307/2347614` | The Berman-Turner device itself, which is how the parent study's point process trend is fitted. CrossRef gives the container title as the abbreviated *Applied Statistics*; expanded here to the journal's current full name |
| `baddeley2000` | CrossRef API, DOI `10.1111/1467-842X.00128` | Queried by DOI rather than by title. A title search returns the 1998 conference abstract of the same name in *Advances in Applied Probability* first, which is a different item and the wrong one to cite |

Five comparator papers added 5 August 2026 from the survey in
`05.tasks/CJFR-COMPARATOR-PAPERS-2026-08-05.md`. All are in the target journal. Author lists, volume,
issue and pagination are the publisher's deposited record, queried by DOI. Four of the five were also
read in full from open repository copies, so the metadata is corroborated by the documents.

| Key | How verified | Notes |
|---|---|---|
| `donato2009` | CrossRef API, DOI `10.1139/X09-016`; full text read | Cited for its explicit exclusion of interaction terms on sample-size grounds, which is the precedent the Discussion rests on |
| `bansal2014` | CrossRef API, DOI `10.1139/cjfr-2014-0112` | Abstract only. Cited only for the register point that a designed factorial earns interaction language, which the abstract establishes |
| `estabrook2025` | CrossRef API, DOI `10.1139/cjfr-2024-0305`; full text read | CrossRef reports no issue number; the journal moved to continuous publication in January 2025 and the article-level range 1 to 20 is the real pagination |
| `kulakowski2006` | CrossRef API, DOI `10.1139/x06-182` | Abstract only. Cited for its dendroecological dating of the outbreak, which the abstract describes in enough detail to support the claim made |
| `meyer2016` | CrossRef API, DOI `10.1139/cjfr-2015-0464`; full text read | Cited for reconstructing pre-attack structure by returning recently dead trees to the live tally |

## Carried across from the sibling bibliography

The following were verified during the companion study and are copied verbatim rather than
re-entered. See that project's `references-beetle-manifest.md` for their original provenance.

| Key | Used here for |
|---|---|
| `krawchuk2020` | Compound disturbance and the refugia framing |
| `talucci2019dead` | Beetle outbreak influence on subsequent fire severity |
| `meigs2011` | Landsat characterisation of beetle impact on fuels |
| `rodman2021` | Detection sensitivity to mortality agent and severity |
| `meddens2012` | Regional patterns of bark beetle mortality |
| `wulder2006red` | Red-attack detection probability |
| `safranyik2006` | Beetle biology reference |

## Entered from the source portal

| Key | Source | Notes |
|---|---|---|
| `bcaos2026` | BC Data Catalogue | Dataset citation, not a publication. Publisher, licence and retrieval date read from the portal record on 30 July 2026 during the companion study |

## Incomplete, by intention

| Key | What is missing | Why |
|---|---|---|
| `murphy2026refugia` | Everything except title and year | The companion refugia manuscript is in preparation and has no venue, volume or DOI. Update when it is submitted. Cited here only for its elevation-optimum result, which the Phase 0 caveat depends on |

## Outstanding

**The contested literature is now in the file**, see the section below: `simard2011`, `harvey2014`
and `hart2015` were added on 5 August 2026 from their CrossRef records. None of the three PDFs was
read, so they are cited only for the finding each is known for and each claim made about them is at
the level of the abstract. If any is to carry more weight than that, read it first.

Four entries remain uncited in the manuscript: `rodman2021`, `meddens2012`, `safranyik2006` and
`murphy2026refugia` is cited but the other three are not. Either use them or remove them before
submission; an uncited entry in a reference list is a referee's free catch.

`04.references/literature/` is empty. The repository is public, so whether other publishers' PDFs
may sit there is the author's decision to make explicitly rather than by default. The parent paper's
own PDF is gitignored for this reason; see `grandfather-study/README.md`.

## Added 5 August 2026 for the Introduction and Discussion

Verified against the CrossRef record by DOI. The three PNAS and Ecological Monographs entries are the
contested beetle-to-fire literature the task request flagged as missing from the first draft; the two
CJFR entries come from the comparator survey.

| Key | How verified | Notes |
|---|---|---|
| `simard2011` | CrossRef, DOI `10.1890/10-1176.1` | The negative result on crown-fire probability, and the anchor of the contested literature |
| `harvey2014` | CrossRef, DOI `10.1073/pnas.1411346111` | Beetle effects on severity contingent on outbreak stage rather than uniform |
| `hart2015` | CrossRef, DOI `10.1073/pnas.1424037112` | Area burned unaffected by outbreaks; the strongest negative in the set |
| `stevensrumann2016` | CrossRef, DOI `10.1139/cjfr-2016-0185`; full text read | The closest analogue in the target journal, prior disturbance conditioning subsequent severity |
| `magnussen2017` | CrossRef, DOI `10.1139/cjfr-2017-0247` | **CrossRef deposits the third author's given name as "Fransisco", which is a deposit typo; the bibliography uses "Francisco".** Flagged here rather than silently corrected |
