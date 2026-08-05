# compound-disturbance-additively-modelled

**Compound disturbance, additively modelled.** Testing whether beetle mortality and fire severity
interact, in the landscape and in the model, Darkwoods Conservation Area, British Columbia.

Third paper in a family. The parent is published as Murphy et al. 2026, *Forest Ecology and
Management* 618:123985. Its abstract describes the additive effects of increasing beetle to fire
disturbance interactions; its model enters beetle and fire as additive main effects with no product
term. This paper tests the interaction the parent asserted, and asks whether the two agents are
associated on the ground at all.

**Status:** complete draft. Provenance check, conditioned within-burn gradient, interaction refit,
discussion and conclusions. Renders end to end in about three and a half minutes.
**Venue: Canadian Journal of Forest Research, Research article.** Guidelines verified 5 August 2026
in `05.tasks/CJFR-GUIDELINES-VERIFIED-2026-08-05.md`. Publication is free; the abstract and the table
count are the two limits the draft breaks.
**Sibling and template:** `../beetle-topography-and-wind-study` in `claude-science-library`.

## Entry point

`01.manuscript/compound-disturbance-additively-modelled.qmd` is the single source of truth. **If it
is not in the manuscript, it is not part of the study.** Every number in the prose is an inline `r`
expression and every chunk carries an explicit `#| echo: true`. No `echo: false`, no
`include: false`, no `eval: false`. Nothing runs outside the render.

```bash
quarto render 01.manuscript/compound-disturbance-additively-modelled.qmd --to html
```

A render takes about a minute. It needs `DARKWOODS_DATA`, `DARKWOODS_GREYFIX` and `DARKWOODS_AOS`,
which default to the parent study's working directory, its 2 June 2026 correction archive, and the
sibling repository respectively. **Check `/Volumes/PortableSSD` is mounted first.**

`README.md` is generated from the render by `03.outputs/build-readme.py`. Rerun it after every
render; never edit it by hand.

**Headings are limited to three words and are written in formal scientific vocabulary.** This is an
author rule, applied on 5 August 2026, and it governs chapter, section and subsection headings alike.
The manuscript previously used descriptive sentence headings such as "Do the two agents interact in
the model?"; these are now "Regeneration interaction" and the like. **Do not restore the longer
forms.** The `{#sec-...}` anchors were left untouched when the headings were rewritten, so every
cross-reference still resolves, and `number-sections` means a reference renders as a section number
rather than the heading text. A future rewrite of a heading is therefore safe for cross-references
but must respect the three-word limit.

## The finding so far

**The annual beetle classifications are clipped to the fire perimeter, in the source files.** All
nine carry an identical 3,423 nodata cells, and only 10 of the 3,429 cells lying outside the
perimeter are observed in any year. Every beetle surface in the study descends from those files and
inherits the boundary, so no beetle layer on disk can see attack outside the burn. The independent
provincial Aerial Overview Survey, which was never clipped, records 40.4 per cent of that outside
ground as attacked, a rate higher than two of the three burned classes.

**There are two clips, one inside the other.** `Beetle.Outbreak.RedStage.tif`, the layer the parent
study modelled, is confined more tightly still to the classified severity footprint. It reads
exactly zero across the 1,367 cells inside the perimeter that no severity class claims, where the
corrected grey union records 33.1 per cent. The narrower clip is an accident: the intended layer,
`mpb_red_na.tif`, is missing from the repository and the red-stage surface was substituted for it.

Three consequences.

1. **Any comparison crossing the fire perimeter measures the clip.** The scoping document's headline
   contingency, attack rising from 0.2 per cent in unburned forest to 19.9 per cent at moderate
   severity, is an artefact. Question A cannot be asked in that form, and the local data is too
   nearly absent out there to be rescued: 10 cells cannot corroborate or contradict anything.
2. **The within-burn gradient survives**, because every severity class is observed at essentially
   100 per cent and is equally exposed. Three records agree on its shape and all peak at moderate:
   the corrected grey union at 20.8, 34.6 and 27.7 per cent across low, moderate and high, the
   published red surface at 6.3, 20.7 and 12.1, and the independent survey at 24.5, 40.6 and 33.1.
   The two local surfaces share a measurement pathway with each other but not with the survey.
3. **Question B is untouched.** The seedling point pattern lies wholly inside the burn, so every cell
   entering the point process model sits inside the clip and is equally affected by it.

### Phase 1: the gradient conditioned

The caveat that governed Phase 1 was that moderate severity also sits highest of the three burned
classes at 1,449 m, and the sibling study finds attack peaking near 1,430 m for reasons unrelated to
fire. Conditioning on lodgepole cover and elevation over 5,413 observed cells settles it three ways.

4. **The moderate-severity peak survives, attenuated by about two fifths.** The crude log-odds
   against low severity falls from 0.705 to 0.416, and still clears the spatial block bootstrap
   interval at all four block sizes tried, 300 to 750 m. It is weakest at 750 m, lower bound 0.020
   on 14 blocks, which is the honest edge of what this extent supports.
5. **The fall at high severity is not supported.** High against low spans zero in every
   specification. The non-monotone shape is a claim the data supports at its peak and not at its
   fall. **Do not report a demonstrated decline at high severity.**
6. **Host cannot be separated from elevation here.** The two correlate at 0.52 across the burn.
   Entered together, elevation clears every interval and host clears none, despite a crude contrast
   of 35.3 against 15.3 per cent. This does not contradict the sibling's host finding; it means the
   question is unaskable at this extent. Relatedly, the fitted elevation optimum inside the burn
   lands at 503 m, far outside the 872 to 1,747 m the clip spans, so within the burn the
   relationship is monotone and the landscape-scale hump is invisible rather than absent.

### Phase 2: the interaction, and the paper's main result

7. **The beetle by fire interaction is decisive under the published likelihood and absent under
   inference that respects the clustering.** The parent study's point process trend is fitted by the
   Berman-Turner device, which is weighted Poisson regression, and a Poisson likelihood counts every
   seedling as independent evidence about the covariates. Adding the four product terms gives a
   likelihood ratio statistic of 99.2 on 4 degrees of freedom and three of four product terms with
   intervals excluding zero. Under a spatial block bootstrap **not one of sixteen product-term
   intervals clears zero**, at any block size from 25 to 100 m. The estimates are identical either
   way. Only the intervals move, widening by a factor of 2.4 to 7.6. That factor is the result.
8. **The justification comes from the parent study's own figures.** It spends two figures and
   999-simulation envelopes establishing that the seedling pattern is clustered at every distance
   examined, then reports coefficients whose standard errors assume it is not. The residual
   correlogram agrees from inside the model: 0.806 within 25 m, 0.332 between 50 and 75 m, crossing
   zero near 100 m.
9. **Only two main effects survive** at every block size, red-stage attack and low burn severity, and
   neither is a product term. This is not evidence that the agents do not interact. It is evidence
   that 12.69 ha of clustered seedlings cannot resolve a difference of differences.

## Layout

| Path | What is there |
|---|---|
| `01.manuscript/` | The `.qmd` and its renders. Edit the `.qmd`, never a render |
| `02.inputs/` | No data, only provenance. `README.md` is the central register; every subfolder carries its own |
| `03.outputs/` | `PNG/` figures at 300 dpi, `TBL/` tables as CSV, `MD/` notes, and `build-readme.py` |
| `04.references/` | `references-compound.bib`, its manifest, CSL, Word style. The parent paper PDF is gitignored, see `grandfather-study/README.md` |
| `05.tasks/` | **Start at `TASK-REQUEST-2026-08-02.md`, then `progress.md`** |

## Data

No raster is stored in this repository. All are read at render time.

- **Disturbance surfaces**, beetle and fire, from the parent study's working directory via
  `DARKWOODS_DATA`. Built in 2021 from Landsat classifications.
- **Corrected grey-stage package** of 2 June 2026 via `DARKWOODS_GREYFIX`. The primary beetle
  surface, 1,541 cells, and the memo that derives it.
- **Aerial Overview Survey**, the independent check, shared with the sibling repository via
  `DARKWOODS_AOS` rather than duplicating 950 MB. Open Government Licence BC, retrieved 30 July 2026.
- **Seedling point pattern and terrain**, from the parent study, unchanged.

## Traps

1. **The perimeter clip governs everything.** Any comparison crossing the fire perimeter measures
   the clip. Comparisons made entirely inside it are fine.
2. **Two clips, not one.** The red-stage surface is confined to the classified severity footprint
   and reads zero where the corrected grey union reads 33.1 per cent. Prefer the corrected grey
   union, and look for the missing `mpb_red_na.tif` before using the red surface again.
3. **Use `mpb_grey_corrected.tif`, 1,541 cells**, the union of aerial-survey code 44 over 2005 to
   2011. Not `GreyStage.tif` (270), not `mpb_grey_attackcount.tif` (932, built with the wrong value
   test). The correction is documented in the parent study's memo of 2 June 2026.
4. **The severity codes are not in severity order.** `1` is high, `32` is low, `34` is moderate. A
   table built on numeric order inverts the top two classes. The manuscript derives the mapping in
   code and asserts it with `stopifnot`. Do not hard-code it.
5. **Code 16 is not a severity class.** It is cells inside the perimeter that no class mask claims.
   They are fully observed and roughly a third grey-attacked, so treat them as burned-unclassified,
   not as unobserved and not as unburned.
6. **Key any class table on the perimeter first, then on severity.** Keying on the severity code
   alone puts 67 in-perimeter cells that the severity raster codes 0 into the outside row and
   inflates what little the local data says out there by a factor of seven. This error was made and
   caught during Phase 0.
7. **The disturbance grids are not co-registered.** Beetle 29.558 m on 135 by 66, severity 30 m on
   134 by 66, intersections 29.558 m on 136 by 67. Resample to a named target explicitly. The eight
   stray unburned attacked cells reported during scoping are this, and vanish at native alignment.
8. **The annual beetle series is two incompatible products.** 2005 to 2011 use one code set, 2013
   and 2014 use another and carry no code 44 at all. There is no 2012 file. So the 2005 to 2011 and
   2005 to 2014 unions are identical, which looks like corroboration and is not.
9. **Three seedling counts are in circulation.** 3,912 is the analysis frame, 3,866 the
   species-assigned subset, and the published 3,886 matches neither and is unexplained.
10. **Extent is the live methodological risk.** Everything but the terrain grid sits inside an 8 km²
    clip, which is precisely the extent the sibling study shows can reverse a coefficient's sign.
11. **Never report a naive p-value here, and do not default to 1 km blocks.** The manuscript's own
    residual correlogram puts dependence at 0.394 within 100 m, decaying to 0.057 by 500 m, so a
    500 m block holds most of it. The burn affords 27 blocks at 500 m, 14 at 750 m and only 8 at the
    1 km the sibling study uses, so the sweep across block sizes is reported rather than a single
    interval. The task request's figure of 0.728 for Moran's I on the red-attack union was not
    reproduced here and should not be quoted until it is.
12. **`model.matrix` silently drops rows with an `NA` factor level.** A few cells inside the
    perimeter carry the outside-perimeter severity code and fall outside the four severity levels.
    Left in, the design matrix is shorter than the response and every bootstrap index is off by that
    many. The frame chunk drops them and a `stopifnot` asserts the lengths match. Do not remove it.
13. **`dplyr::intersect` masks `terra::intersect`.** Namespace it.
14. **Do not re-present the published index comparison.** The five fire and four beetle indices,
    their separability, ANOVA and SVM diagnostics are in the parent paper's main text and
    supplement, and in three public repositories. Cite them, never re-table them.
15. **The canonical published point process fit is the corrected one, and it is not in the obvious
    folder.** `4.RData/spatstat_refit_2026-06-01/Table12_LGCP_coefficients.csv` is superseded. It is
    built from `mpb_grey_na.tif`, which `rebuild_mpb_grey_na.py` writes with the test `annual == 1`,
    the same wrong value test as trap 3 and by the same script that writes the discredited
    `mpb_grey_attackcount.tif`. That is why both hold 932 cells. Use
    `Archive/Greystage_Raster_Fix_2026-06-02/tables/Table12_LGCP_coefficients_CORRECTED.csv`, built
    from `mpb_grey_corrected.tif`. The two differ where it matters: the grey main effect is +0.609 at
    p = 5e-11 in the superseded fit and -0.0007 at p = 0.99 in the canonical one. Refitting against
    the wrong baseline would produce a large difference and invite reporting it as a finding.
16. **A map must never claim a scale it is not drawn at, and there are two ways to get this wrong.**
    First, `st_bbox` returns a named vector, so building `c(xmin = b["xmin"] - hw)` from it produces
    the name `xmin.xmin`; a `[` lookup then returns `NA` silently and `coord_sf` falls back to the
    data extent while the subtitle goes on claiming the requested ratio. Both panels were framed
    wrong this way and one carried a false 1:250 000 while drawn at about 1:170 000. Use `[[`, which
    errors instead, and let `box_at()` assert the width it produced.
    Second, and less obvious: the ratio is ground width over **drawn** width, and a panel is not
    drawn at its share of the figure. Axis text, titles and legends take fixed space first and
    `coord_sf` then locks the panel's aspect, which can shrink it again. A nominal `PANEL_IN` is an
    assumption, and it was 1.3 per cent out. `panel_in_of()` computes the drawn width from the
    gtable the way gtable itself resolves the layout, both figures are built twice, once at a guess
    and once at the measurement, and a `stopifnot` requires the second pass to agree with the first
    to within 0.5 per cent. **Do not reintroduce a hard-coded panel width.**
17. **`glm` resolves `weights` in the formula's environment, not in the calling function's.** A
    formula defined at top level carries the global environment, so a weight vector local to a
    bootstrap function is invisible and every fit errors. Wrapped in `try` inside a loop this is
    silent and returns an all-`NA` interval. Keep the weight as a column of the frame and pass it by
    name. `tbl-ppblocks` reports a usable-draw count so an all-`NA` result cannot pass as a wide
    interval. This cost a debugging cycle on 5 August 2026.

## Open items

- **Cross-agent spectral separability is blocked, not deferred.** Both fire severity surfaces on
  disk are classified, no continuous dNBR exists, and no Landsat bands or NDMI rasters survive to
  recompute one from. It would mean re-acquiring the archive and re-deriving the published methods.
  See `05.tasks/TASK-REQUEST-2026-08-02.md` §2.
- **Recovering question A in its original form** would mean rebuilding the classification over the
  unclipped landscape from the Landsat archive. That is a reprocessing task, and it re-treads the
  parent study's published methods.
- **`mpb_red_na.tif` does not exist anywhere in the parent repository.** Searched on 2 August 2026
  across the whole tree and it is absent, so the narrower of the two clips cannot be lifted without
  rebuilding the layer. Closed as gone rather than mislaid.
- **The published 3,886 seedlings is still unexplained.** `Seedlings.shp` holds 3,912 points and the
  seven-species filter leaves 3,866, which accounts for both counts in circulation. No filter tried
  reproduces the abstract's 3,886. Query with the author.
- **The `tbl-crosscheck` and `tbl-host` frames differ by 68 cells** in the unclassified class, with
  no explanation in the text. A `stopifnot` prevents the divergence widening silently. Decide before
  submission whether to unify the frames or state the difference in the Methods.
- **Not yet a submodule of `claude-science-library`.** The task request asked for this; the
  repository was created standalone before the request was worked.
- **Venue is settled and the compliance gap is small.** Canadian Journal of Forest Research, Research
  article, free to publish. The abstract must fall from 323 words to 200, the sixteen tables need a
  main and supplementary split, the citation style must go from APA to Harvard using the
  `04.references/cjfr.csl` already downloaded, and line numbering must be added. The body is 5,323
  words against a 6,000 limit and 13 references against 50, so length is not a problem. The float
  count is now 16 tables and 2 figures. Full detail
  and the compliance table are in `05.tasks/CJFR-GUIDELINES-VERIFIED-2026-08-05.md`; the workplan is
  in `05.tasks/progress.md`.
- **`cdnsciencepub.com` returns 403 to every automated fetch.** The guidelines were read through a
  text-extraction proxy and the journal-specific section had to be parsed out of raw HTML because it
  sits behind a JavaScript selector. There is no Wayback capture of the author page to cross-check
  against. **Confirm the limits in a browser before submitting.**
- **The parent paper's co-authors have not been consulted.** Murphy et al. 2026 is Murphy, Leslie,
  Wilson and Banks; this manuscript is single-author and revises that paper's inference. CJFR uses
  single-anonymous review, so referees will see the overlap. Nothing about notification or authorship
  is recorded anywhere. This is the open item most likely to cause trouble late.
