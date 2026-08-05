# Bibliography manifest

Provenance for every entry in `references-compound.bib`: where it came from, what could not be
extracted, and any disagreement between a filename and the text it names. Thirteen entries at
5 August 2026.

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

The compound-disturbance literature the introduction will need is not yet in the file. Harvey,
Hart and Simard are named in the task request as the contested literature on beetle influence on
burn severity and none of them is represented. Add them from read PDFs, not from memory, before the
introduction is written beyond its present stub.

`04.references/literature/` is empty. The repository is public, so whether other publishers' PDFs
may sit there is the author's decision to make explicitly rather than by default. The parent paper's
own PDF is gitignored for this reason; see `grandfather-study/README.md`.
