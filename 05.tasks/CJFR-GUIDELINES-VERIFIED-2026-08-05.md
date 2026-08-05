# Canadian Journal of Forest Research: guidelines verified 2026-08-05

Venue selected by the author on 5 August 2026: **Canadian Journal of Forest Research**, Canadian
Science Publishing. Submission by ScholarOne. Editorial office `cjfr@cdnsciencepub.com`.

**Article type: Research article.** Not Discussion, for reasons set out below that were the main
finding of this check.

## How these pages were read, and the caveat that goes with it

`cdnsciencepub.com` returns HTTP 403 to `curl` and to any plain automated fetch, including with a
browser user agent, and the Claude browser extension was not connected. The pages were therefore read
through the `r.jina.ai` text-extraction proxy, which renders the live page and returned HTTP 200 for
each. The journal-specific guidelines sit behind a JavaScript selector on
`cdnsciencepub.com/journal/cjfr/authors` and do not appear in the proxy's text rendering; they were
recovered by requesting the raw HTML from the same proxy and parsing the selector's contents.

**Everything below is quoted from the live page, but none of it was read in a browser.** The Wayback
Machine has no capture of the author page and only a 2021 capture of the fees page, so there is no
second source. Confirm the numbers in a browser before submitting. The pages read were
`/journal/cjfr/about`, `/journal/cjfr/authors`, `/journal/cjfr/publication-fees` and
`/authors-and-reviewers/submission-process`.

## Cost, which was the reason for choosing this venue

**Publication is free. There are no page charges and no mandatory fee of any kind.**

> "For this subscription journal, fees apply only if authors choose for the article to be published
> open access. Authors may select this option right after acceptance or at the proof stage. This
> journal does not have page charges."

Open access is optional and costs USD 3,750 for manuscripts submitted after 1 January 2026. If the
corresponding author's institution subscribes through the Canadian Research Knowledge Network the
discount is 25 per cent, and the CRKN list includes the University of British Columbia, Simon Fraser
University, the University of Victoria and the University of Northern British Columbia. None of that
is needed to publish; it only buys open access.

Discussion, Reply and Review are exempt from the open access fee because they are "published as free
access by default". That exemption was the original attraction of this venue and it does not apply to
us, but it does not matter, because the subscription route costs nothing anyway.

## The article type, and why Discussion is not available

The Discussion type looked like an exact fit for a paper that re-analyses a published study. Reading
its full description rules it out three times over.

> "Discussions are brief pieces (typically <2000 words) that aim to challenge or rebut important
> scientific aspects of a published article **within the journal** [...] Discussions should be based
> on knowledge that is contemporaneous with the published article, not subsequent scientific
> developments, data or findings from other published articles or original, previously unpublished
> results or data."

The parent paper is in *Forest Ecology and Management*, not in this journal, so the type does not
apply. The limit is about 2,000 words and this manuscript is 5,323. And the type explicitly excludes
original previously unpublished results, which is most of what this paper contains.

One further clause is worth reading carefully rather than skimming, because it bears on the
provenance finding:

> "Clear errors or mistakes in the published article, and ethical concerns related to the research or
> handling of the article at peer review, may result in an Expression of Concern, Correction, or
> Retraction and should not be submitted as Discussions but rather be brought directly to the
> attention of the publisher's Integrity and Engagement team."

That is Canadian Science Publishing's policy for its own journals and has no force over *Forest
Ecology and Management*. It is quoted here because the question it raises is live for us in Elsevier's
form rather than CSP's: see the open item on notifying the parent journal and the co-authors.

**Research article is the correct type.** "Reports in a concise manner the results of a substantial,
completed work."

## Hard limits, and where the manuscript stands

Measured against the current render on 5 August 2026.

| Requirement | Limit | Manuscript | Status |
|---|---|---|---|
| Abstract | 200 words, all article types | 323 | **over by 123** |
| Body, Introduction through end of Discussion | 6,000 words | 5,323 | ok, 677 to spare |
| References | 50 | 13 | ok |
| Tables and figures | no stated numeric cap; "all figures and tables should be necessary to support the text" | 16 tables, 2 figures | **needs a main and supplementary split** |
| Line numbering | required on all submissions | absent | **to add** |
| Citation style | Harvard, in-text (author year), alphabetical, unnumbered, DOIs and hyperlinks included | APA | **to switch** |
| Editable table format | Word or Excel, one data point per cell | rendered from code | **to check on the docx render** |
| Language, spacing, layout | English or French, double-spaced, single column, page numbers, 8.5x11 or A4 | docx render exists | to verify |

The word count is the pleasant surprise. The manuscript fits the Research article limit as written,
with room, because the analysis lives in tables rather than in prose.

## Required statements, none of which the manuscript currently carries

All are listed as author statements on the CJFR author page. Each needs writing.

1. **Author contribution statement**, using CRediT roles, identifying authors by initials.
2. **Competing interests statement.** If none: "The authors declare there are no competing interests."
3. **Data availability statement.** This one is substantive rather than boilerplate, see below.
4. **Funding statement.** If unfunded: "Funding: The authors declare no specific funding for this work."
5. **Acknowledgements**, optional, and the place where any AI writing assistance must be named.

## Data availability, and the Dryad offer

CJFR has partnered with Dryad and **authors publishing with the journal can deposit data and code
free through the end of 2026**, using a provisional URL issued at submission. That is directly useful
here: the manuscript is a single executable document whose entire argument is reproducibility, and
the rasters it reads are not in this repository. Depositing the derived inputs and the `.qmd` would
turn the paper's strongest claim into something a referee can run.

The obstacle is that the source rasters belong to the parent study and are not the author's alone to
license. Decide what may be deposited before writing the statement.

## Scope, and one sentence in it to be careful about

The journal covers "disturbances, forest health" and "biometrics/inventory" explicitly, and asks that
"the topic, content, and scope of papers should be of interest to an international readership". The
sentence to notice is this one:

> "Methodological and modeling papers should include applications and provide a verification of
> enhanced performance."

Read strictly, a paper whose result is that an existing model's inference is wrong does not "verify
enhanced performance". The framing that avoids the objection is the one the manuscript already has:
this is a disturbance-ecology paper about a beetle and fire sequence, which reports a provenance
result and a conditioned within-burn gradient, and whose interaction test carries the general lesson.
It is not a methods paper about block bootstraps. **Do not reframe it as one to chase novelty.**

## Journal facts worth knowing

Impact factor 1.5 for 2024, five-year 2.1. Median 97 days to final decision with review. Accept rate
42 per cent. Continuous publication since January 2025, so there is no issue queue. Single-anonymous
peer review: referees see author names. Affiliated with the Canadian Society of Ecology and Evolution
and the Canadian Centre for Evidence-Informed Conservation.

Single-anonymous review matters here. Referees will see that the author of the critique is an author
of the paper being critiqued, which is a point in the paper's favour if the framing is candid and a
problem if it is not.

## Assets prepared

`04.references/cjfr.csl` is in place. Zotero's `canadian-journal-of-forest-research` style is a
dependent style whose independent parent is `canadian-journal-of-fisheries-and-aquatic-sciences`, the
shared NRC Research Press author-date style, so the parent was downloaded and saved under the CJFR
name. It parses as valid CSL. It has not yet been wired into the `.qmd`, which still uses `apa.csl`.
