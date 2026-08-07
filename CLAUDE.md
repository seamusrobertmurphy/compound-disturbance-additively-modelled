# Compound disturbance, additively modelled

A single-author follow-up to Murphy et al. (2026), *Forest Ecology and Management*
618:123985. It asks whether mountain pine beetle mortality and wildfire severity
interact in the Darkwoods Conservation Area, and finds that these data cannot say. The
transferable result is not about beetles: it is that a routine analysis produced a
confident interaction from data containing none, because the likelihood counted
clustered seedlings as independent observations.

**Target venue: Forest Ecology and Management, Elsevier, Regular paper.** Retargeted from
the Canadian Journal of Forest Research on 6 August 2026. Anything in the repository
mentioning CJFR predates that and is superseded.

## Read these first

`INDEX.md` carries nineteen numbered traps, each one a mistake made and caught in this
project. Read it before touching the analysis. Traps 18 and 19 are the most important
because they concern silent failure in precisely the machinery the paper is about.

`05.tasks/progress.md` is the chronological record. `05.tasks/TASK-REQUEST-*.md` are the
work orders, worked in date order. The most recent one is the current state of play.

## The two rules that everything else depends on

**Every number in the manuscript is computed at render time from the source data.**
Nothing is quoted from a prior session's notes, no result is retyped, and tables are
written to `03.outputs/TBL` from the same object that renders so the two cannot drift.
If you find yourself about to type a number into the prose, compute it instead and
interpolate it. The only hard-coded numbers in the document are the six in the abstract,
which lives in YAML where inline R does not run, and those are asserted against the
computed values in the `pp-verdict` chunk.

**`error: false` in the YAML is load-bearing. Never set it to `true`.** Under
`error: true` a failed `stopifnot` does not fail the render; Quarto prints a red block
and exits 0. In a chunk that also sets `output: false`, as `pp-verdict` does, even the
red block is suppressed and the failure produces no signal anywhere. This is not
theoretical: it is how the abstract's widening factor stayed at "2.4 to 7.6" through a
refit that moved it to 2.3 to 5.9. Several passages in the manuscript tell the reader
that an assertion "fails the render if they ever stop agreeing", and `error: false` is
the only thing that makes those sentences true.

## Running it

R is the CRAN build at `/usr/local/bin/R`, reading the global user library. There is no
`renv.lock` here and none should be created. Render with:

    quarto render 01.manuscript/compound-disturbance-additively-modelled.qmd --to html

**A full render takes roughly 25 minutes** at `B_BOOT <- 2000L`, and the point-process
block bootstrap is nearly all of it. Batch changes into one render rather than
iterating, and expect to wait. Quarto's `freeze` would speed iteration but must never be
enabled for the render that produces the submission file, because the paper's claim is
that every number comes from the source data at render time.

The analysis reads rasters from outside the repository, overridable by environment
variable and asserted to exist in the `paths` chunk:

| Variable | Default |
| --- | --- |
| `DARKWOODS_DATA` | `~/repos/publications-pending/Darkwoods-Disturbance-Paper/3.SpatialData` |
| `DARKWOODS_GREYFIX` | `.../Darkwoods-Disturbance-Paper/Archive/Greystage_Raster_Fix_2026-06-02` |
| `DARKWOODS_AOS` | the sibling `beetle-topography-and-wind-study` repository |
| `DARKWOODS_VRI` | the sibling `beetle-topography-and-wind-study` repository |

Use the corrected grey-stage raster and the corrected coefficient table from the
`Greystage_Raster_Fix_2026-06-02` archive, never the superseded ones in the obvious
folder. Trap 15 in `INDEX.md` explains why: refitting against the wrong baseline
produces a large difference and invites reporting it as a finding.

## After a render

Rebuild the README from the fresh HTML, never by hand:

    python3 03.outputs/build-readme.py

Regenerate the submission variant, which differs from the working manuscript only in
hiding code:

    sed 's/^  echo: true$/  echo: false/; s/^#| echo: true$/#| echo: false/' \
      01.manuscript/compound-disturbance-additively-modelled.qmd \
      > 01.manuscript/compound-disturbance-submission.qmd

## Manuscript conventions

Section headings are three words, in formal scientific vocabulary. The prose follows the
house style in the global `CLAUDE.md`: plain, compressed, no em-dashes anywhere,
including in code comments and chunk captions.

Code comments in the `.qmd` explain why a thing is done, and in particular record what
went wrong when it was done otherwise. That is deliberate. Several comments exist only
to stop a future session reintroducing a bug, and they should not be trimmed as noise.

Do not re-present the published index comparison. The fire and beetle indices, their
separability and diagnostics are in the parent paper and three public repositories.
Cite them, never re-table them.

## Framing, which is not negotiable

This is a methodologically driven follow-up, not a correction of the parent study. The
parent opened a discussion about the limits of remote sensing in disturbance ecology and
how far inherited raster layers carry a compound-disturbance analysis; this paper runs
the spatial-inference tests that discussion called for. **The parent's additive model was
the defensible modelling choice and this paper confirms it**, because the data cannot
support a product term either way.

The author is on both papers. Present every point as an extension of that conversation
and as a contribution the shared dataset made possible, never as a fault located in the
parent. Where clustering-aware intervals are reported, they are a general methodological
result measured on this dataset, not a revision of the parent's numbers. Nothing here
revises the parent's ecology.

The parent contains several internal inconsistencies beyond the scope of this paper.
They are catalogued in `05.tasks/TASK-REQUEST-2026-08-07_1.md` item 5, and the standing
decision is to raise none of them here. They are irrelevant to this paper's argument,
which needs only that the published fit is additive and its standard errors are Poisson,
and both are demonstrated by reproduction.

## Verification standard

Quote sources verbatim and check them. The parent's abstract and conclusions are quoted
word for word from the PDF, not paraphrased, because an earlier draft attributed the word
"additive" to its abstract and that word appears nowhere in the paper. Journal
requirements are checked against the journal, and where a page could not be reached, the
manuscript records that the requirement is unverified rather than filling in a plausible
number. New bibliography entries are verified against CrossRef before being added.

## Git

Commits, pushes and committed files name Seamus only. Never add a Claude attribution, a
co-author trailer, or a generated-by line.
