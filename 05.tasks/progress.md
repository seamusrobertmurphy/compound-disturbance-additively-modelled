# Progress log: compound beetle and fire disturbance at Darkwoods

**Started:** 2026-08-02
**Status:** Phases 0 to 4 complete. The manuscript is a complete draft: provenance, conditioned
gradient, interaction refit, discussion and conclusions. Venue is the outstanding decision.
**Last updated:** 2026-08-05
**Current task request:** `TASK-REQUEST-2026-08-02.md`
**Parent paper:** Murphy et al. 2026, *Forest Ecology and Management* 618:123985, published
**Sibling paper and template:** `beetle-topography-and-wind-study`

## Timeline

### Phase 0, the provenance check (2 August 2026)

**Partly superseded the same day by the Phase 0 revision below.** The conclusion stands; the
attribution of the clip and two of the numbers do not. Kept because it records what was checked and
in what order.

Worked §7 Phase 0 of the task request, which asked one question: is the beetle red-stage raster
confined to the burn, and if so does that manufacture the association reported in §4 of the scoping
document. The answer is yes to both.

**What was done.** Established the footprint of every disturbance surface against the terrain grid.
Decoded the classified severity raster against its own binary class masks. Cross-tabulated red
attack against the fire perimeter at native alignment. Retrieved the provincial Aerial Overview
Survey from the sibling repository and compared it against the local classified surface class by
class. All of it lives in live chunks in the manuscript; none of it is quoted from a script.

**The finding.** All 493 red-attack cells fall inside the fire perimeter and none falls outside it,
on a raster that extends 763 m beyond the perimeter and covers 2.98 km² of unburned ground. The
furthest any attacked cell reaches beyond the perimeter is zero metres. The independent survey
records 40.8 per cent of that same outside ground as attacked, and 52.0 per cent of the unclassified
ground inside the perimeter, which is the highest attack rate of any class in the table. Inside the
classified burn the two records agree in the ordinary way, the local surface running at 0.26 to 0.51
of the survey rate.

The red-attack classification was run only where burn severity had been classified. The zeroes
outside that footprint are unobserved, not unattacked.

**What it costs.** Question A as posed, comparing burned against unburned ground, cannot be asked of
these surfaces. The scoping document's headline contingency, beetle attack rising from 0.2 per cent
in unburned forest to 19.9 per cent at moderate severity, measures the mask.

**What it leaves.** The three severity classes all sit inside the classified footprint and are
equally exposed to the mask, so it cannot generate differences among them. Within the burn, red
attack runs 6.3 per cent at low severity, 20.6 at moderate and 12.1 at high. The independent survey
traces the same non-monotone shape at 24.3, 40.5 and 33.0 per cent, peaking at moderate as the local
surface does. Two records sharing no measurement pathway agree on the shape. Question A survives as
a within-burn question about the severity gradient.

**The immediate caveat, and the Phase 1 priority.** Moderate severity also occupies the highest mean
elevation of the three burned classes at 1,448 m, and the sibling study finds beetle attack peaking
near 1,430 m for reasons unrelated to fire. The agreement between the two records may be agreement
about elevation. Conditioning on host abundance and elevation is the first task of Phase 1, not a
robustness check appended to it.

### Phase 0 revision, against the corrected rasters (2 August 2026)

The author pointed at `5.Submissions/`, which carries the latest corrections to these rasters. The
substantive one is `Archive/Greystage_Raster_Fix_2026-06-02/`, a verification re-run with its own
memo, three corrected rasters and the scripts that built them. Working it changed the Phase 0
finding in three ways, one of which corrected an error of mine.

**The clip is the fire perimeter, applied at source, not the classified severity footprint.** The
first pass concluded that the red-attack classification had been run only where burn severity was
classified. That was the wrong attribution. The corrected grey raster is built from the same annual
files by an entirely separate route, in Python with `rasterio`, and it stops at the fire perimeter
too: 1,540 of its 1,541 cells fall inside it. Checking the annual files directly settles it. All
nine carry an identical 3,423 nodata cells, of which 3,419 lie outside the perimeter, out of 3,429
cells outside. Only 10 cells beyond the perimeter are observed in any year. The time series was
clipped to the burn before any classification that used it was ever run.

**There are two clips, one inside the other, and the narrower one is an accident.** The red-stage
surface reads exactly zero across the 1,367 cells that lie inside the perimeter but in no severity
class, where the corrected grey union reads 33.1 per cent. The memo explains why: `mpb_red_na.tif`,
the layer the published analysis intended to use, **is missing from the parent repository**, and
`Beetle.Outbreak.RedStage.tif` was substituted for it. Finding the missing layer is the cheapest
available improvement to the red surface.

**An error of mine, made and caught.** The first cross-check table was keyed on the severity code,
so its "outside perimeter" row was severity code 0, which contains 67 cells that actually lie inside
the perimeter. That put the observed-outside sample at 73 cells and a grey attack rate of 30.1 per
cent, and the draft used it as internal corroboration of the survey. Keyed correctly on the
perimeter, the observed-outside sample is **10 cells**, of which 1 is attacked. There is no internal
corroboration. The manuscript now says so and rests the argument on the survey alone, which is
sufficient. The general lesson is trap 6 in `INDEX.md`: key a class table on the perimeter first,
then on severity within it.

**What improved.** The corrected grey union is three times denser than the red surface and observed
throughout the perimeter, so the within-burn gradient now has three records rather than two, and all
three peak at moderate severity. The manuscript asserts that agreement with a `stopifnot` that fails
the render if they ever stop agreeing.

**A seedling question resolved.** `5.Submissions/2026-06-19/TableS2_reconciliation.csv` analyses
3,912 points pooled, its per-plot rows summing to exactly that and its per-species rows to 3,866. So
3,866 is the species-assigned subset rather than a rival survey. The published abstract's 3,886
matches neither and remains unexplained; query it with the author.

### Phase 1, the gradient conditioned on host and elevation (2 August 2026)

Frame: 5,413 cells inside the fire perimeter that the annual rasters observe, of which 1,518 carry
grey-stage attack. Response is the corrected grey union, being the denser of the two local surfaces
and the only one observed throughout the perimeter. Host is lodgepole cover from the provincial
inventory, summed across the three species slots and reduced to presence. Inference is a spatial
block bootstrap, 400 replicates, swept across 300, 400, 500 and 750 m blocks. No naive p-value is
reported anywhere.

**The moderate-severity peak survives conditioning.** Crude log-odds against low severity 0.705,
falling to 0.416 with host and elevation in the model, so roughly 41 per cent of the crude
association is host and terrain and the rest is not. It clears the block interval at all four block
sizes, weakest at 750 m where the lower bound is 0.020 on 14 blocks. A quadratic elevation term
moves it to 0.403 and changes nothing.

**The fall at high severity is not supported.** High against low spans zero in every specification,
crude and conditioned. So the non-monotone shape that three records trace is supported at its peak
and not at its fall, on 553 high-severity cells. The manuscript says so in bold and the framing must
not overreach it.

**Host cannot be separated from elevation at this extent, and that is a finding about the study
area.** Lodgepole cover and elevation correlate at 0.52 across the burn. Entered together, elevation
clears every interval at 0.424 per 100 m and host clears none at 0.186, despite a crude contrast of
35.3 per cent attacked where lodgepole is present against 15.3 where it is absent. The sibling study
separates the two because 1,776 m of relief contains pine-poor ground at every height; 8 km² does
not. **Do not read the null host coefficient as evidence that host does not matter.**

**The elevation optimum is invisible inside the burn.** The fitted quadratic peaks at 503 m, far
below the 872 to 1,747 m the clip spans, so within the burn the relationship is monotone increasing.
The sibling's landscape-scale hump at about 1,430 m is not contradicted, it is out of view. An
analyst working only inside this perimeter would report attack rising with elevation without limit.

**The extent constrains the inference itself, not merely the ecology.** Residual dependence falls
from 0.394 within 100 m to 0.057 by 500 m, so a 500 m block contains most of it. The burn spans
about 4.0 by 2.0 km, which affords 27 blocks at 500 m and 14 at 750 m. The sibling uses roughly 1 km
blocks over a landscape affording hundreds; here 1 km affords eight, which is not a bootstrap. This
is the paper's own subject matter arriving in its own inference and the manuscript makes the point
rather than hiding it.

**A bug worth recording.** `model.matrix` silently drops rows whose factor level is `NA`. A handful
of cells inside the perimeter carry the outside-perimeter severity code and fall outside the four
severity levels, so the design matrix came out shorter than the response and every bootstrap index
was off by that many. The frame now drops them explicitly and a `stopifnot` asserts the lengths
match. It is trap 12 in `INDEX.md`.

**A drafting error caught by the render.** The first draft of the block sweep asserted that the
moderate coefficient fails at 750 m, carried over from an earlier specification using continuous
lodgepole cover and raw elevation. Under the reported specification it clears at all four sizes. The
passage now derives its claim from the sweep object rather than asserting one, so a refit cannot
leave the prose stranded.

**`mpb_red_na.tif` is gone, not mislaid.** Searched the whole parent tree on 2 August 2026; it does
not exist. The narrower of the two clips cannot be lifted without rebuilding the layer.

## Corrections to the task request

Numbers in `TASK-REQUEST-2026-08-02.md` §4 were flagged there as ad hoc and requiring reproduction
before use. Reproduced, three are wrong.

1. **The severity class labels in §4 are wrong for two of four rows.** Decoded against the binary
   class masks, code `1` is high, `32` is low and `34` is moderate. The §4 table's row labels happen
   to land correctly on high and moderate by coincidence of the counts, but the mapping was never
   established and a table built on the numeric order of the codes would invert the top two classes.
   The manuscript now derives the mapping in code and asserts it.

2. **The eight apparently unburned attacked cells do not exist.** They are an artefact of pairing
   the 29.558 m beetle grid with the 30 m severity grid without resampling. At native alignment,
   with an explicit `method = "near"` resample, the count is zero. This matters: eight stray cells
   read as a very low but non-zero rate, which is an ecological quantity, whereas zero is a
   structural one.

3. **§4's "unburned" row pools two distinct classes.** Code 0, outside the perimeter, and code 16,
   inside the perimeter but unclassified, behave differently in the independent survey (40.8 against
   52.0 per cent) and should not be summed.

The §4 counts for red attack in the three burned classes reproduce closely: 67 at high against 67,
136 at low against 132, 290 at moderate against 286. The residual differences are the same
resampling issue.

## Corrections to the trap register

**Trap 7 confirmed, and the correction already existed.** The 1,541-cell union of code 44 across
2005 to 2011 was derived here independently and then found to match `mpb_grey_corrected.tif` exactly.
The parent study had already diagnosed and fixed this on 2 June 2026: the legacy rebuild tested
`annual == 1`, but the annual rasters encode aerial-survey severity codes and `1` is a sparse trace
class, so it captured almost nothing. `Beetle.Outbreak.GreyStage.tif` holds 270 cells and
`mpb_grey_attackcount.tif` holds 932; neither is the layer to use.

**A trap the task request did not record.** The annual beetle series is two incompatible products.
Files for 2005 to 2011 share a code set of 1, 36, 44, 61, 77, 80, 94 and 105; files for 2013 and
2014 carry codes 2 to 7 and nothing else, and contribute no code 44 at all. There is no 2012 file.
The union above is therefore unchanged whether the window is 2005 to 2011 or 2005 to 2014, which
looks like agreement between two windows and is not.

**A second trap the task request did not record.** Three seedling counts are in circulation:
3,912 in `Seedlings.shp`, 3,866 in the two reprojected files, and 3,886 in the published abstract.
The two file families carry different attribute schemas, so they are different products rather than
reprojections of one product. Resolve before Phase 2.

## Deviations from the task request

**Repository location.** §10 specifies
`claude-science-library/publications-academic/beetle-fire-compound-disturbance/`. The repository had
already been created at `/Volumes/PortableSSD/Github/compound-disturbance-additively-modelled` with
its own GitHub remote named for the working title, so the work was done there. Registering it as a
submodule of `claude-science-library` is outstanding.

**`INDEX.md` is tracked here.** It is gitignored in the sibling. §10 rule 5 asked for a deliberate
decision; this is it. The provenance finding is the thing a reader most needs up front.

### Quality pass over the manuscript (2 August 2026)

Ran `/simplify`, four review agents over the `.qmd`, then applied the findings. Every rendered
table is byte-identical before and after, which is the test that matters: this was a readability
and robustness pass, not a change to any result.

Applied. One `vals()` helper replaced twenty-eight `values(x)[, 1]` extractions. `GREY_HIT` and
`RED_HIT` name the attack predicates that had been spelled out fifteen times between them. One
`show()` helper replaced eleven copies of the `kable(keep(...)) |> kable_styling()` incantation.
The class vocabulary, previously eight literal vectors in three incompatible orderings, is now
`SEV_LEVELS`, `ROW_ORDER`, `OUTSIDE` and `UNCLASSED`, defined once. `sev_label()` replaced two
copies of the `CODE_OF` inverse. The severity decode no longer patches its own class labels
positionally after building them, which had left the assertion checking its own input. The three
model formulas moved above the frame so the length guard uses `F_ADJ` rather than inlining it, and
the guard now covers `F_QUAD` too. `HOST` lost a verbatim duplicate `summarise` body, `tbl-nested`
nine hand-written means, and the elevation table two hand-rolled interval lookups.

The most valuable fix. The block sweep formatted its numeric bounds into a display string and then
regex-parsed them back out forty lines later to decide which block sizes clear zero. That regex
excludes `+` and `e`, so a change to the interval format would have silently turned every bound into
`NA` and put wrong numbers into the prose with `warning: false` suppressing the complaint. Bounds
now stay numeric and formatting is a leaf.

Three efficiency fixes, about 15 s off a two-minute render. The 500 m entry in the block sweep was
recomputing `M_ADJ` bit for bit, so it now reuses it. The correlogram built four dense 3,000 by
3,000 matrices to read two triangles; it uses `dist()` and one lower triangle instead, which the
agent measured as agreeing to 1.7e-16, invisible under the reported rounding. And `fig-mask` was
rendering the four panels twice, once to PNG and once to knitr's device; it now embeds the file it
just wrote.

Two prose corrections. The clip paragraph claimed "all nine annual files" while `ANN` held only the
seven in the outbreak window, so the claim was true but not derived in the document, which breaks
the house rule. There is now an `ANN_ALL` list, the counts are computed, a `stopifnot` asserts they
really are identical, and the sentence reports `r length(ANN_ALL)`. Two captions carried hard-coded
numbers the chunks compute, which would have gone stale on a re-render; they now name no figures.

**Skipped, and worth an author decision.** `tbl-crosscheck` and `tbl-host` are built from two
different frames: the first over every cell in a class, the second over the modelling frame, which
additionally drops cells with missing elevation or inventory cover. They agree exactly on all three
burned classes, so nothing reported twice disagrees. But the unclassified class is **1,367 cells in
`tbl-nested` and `tbl-crosscheck` and 1,299 in `tbl-host`**, a 68-cell difference with no
explanation in the text, and a referee comparing the two tables would ask. Unifying the frames would
change printed numbers, so it was out of scope for a quality pass. A `stopifnot` now asserts the two
paths still agree where they overlap, so the divergence cannot widen silently. Decide before
submission whether to unify the frames or to state the difference in the Methods.

Also skipped. Refitting the model by formula for the correlogram residuals duplicates a fit
`block_boot` already does, but it costs 0.029 s and reads more clearly than threading fitted values
out of `glm.fit`. The AOS geodatabase read costs 39 s, a third of the render, and the extent filter
does not stop the driver scanning the 950 MB store; the only fix is caching a clipped extract as an
input file, which moves a step outside the document and against the house rule. Flagged as a
decision, not taken.

### Phase 2, the interaction refit (5 August 2026)

The outstanding analysis, and the one the paper is named for. It is now in the manuscript as
`sec-interaction`, live like everything else.

**The baseline is the grey-corrected refit, not the one in `spatstat_refit_2026-06-01/`.** This was
nearly got wrong. That folder's `Table12_LGCP_coefficients.csv` reports the grey-stage main effect at
+0.609, p = 5e-11, and it is built from `mpb_grey_na.tif`. Reading
`rebuild_mpb_grey_na.py` shows that raster is built with the test `annual == 1`, which is exactly the
wrong value test of trap 3: it is why the file holds 932 cells, the same count as the discredited
`mpb_grey_attackcount.tif`, because the same script writes both. The parent study caught this before
publication and re-ran the model against `mpb_grey_corrected.tif`, giving
`Table12_LGCP_coefficients_CORRECTED.csv` in the 2 June archive. That is the canonical published fit
and the one this work reproduces. Anyone starting from the obvious folder would have refit against a
superseded model and reported the difference as a finding.

**The published fit reproduces exactly.** All nine coefficients agree to four decimal places, and a
`stopifnot` in `tbl-ppreproduce` fails the render if that ever stops holding. The reproduction is the
licence for everything after it: a product term added to a model that did not reproduce would test
nothing. The specification is the Berman-Turner device, 3,866 data points against 1,282 quadrature
points at 10 m over 12.69 ha, fitted as weighted Poisson regression.

**The interaction is decisive under the published likelihood and absent under honest inference.**
Adding the four beetle by fire product terms gives a likelihood ratio statistic of 99.2 on 4 degrees
of freedom, and three of the four product terms carry naive intervals excluding zero. Under a spatial
block bootstrap none of them clears at any of the four block sizes tried, 25 to 100 m. Sixteen
product-term intervals, zero clearing. The estimates do not move at all; the intervals widen by a
factor of 2.4 to 7.6. That factor is the whole result.

**The justification is the parent study's own figures.** The Poisson likelihood assumes seedlings are
placed independently given the covariates, and the parent study spends two figures and 999-simulation
envelopes establishing that they are not. The residual correlogram agrees from inside the model: 0.806
within 25 m, still 0.332 between 50 and 75 m, crossing zero near 100 m. That range is what sets the
block sizes, and a 200 m plot affords 36 blocks at 75 m and 27 at 100 m.

**Two specification findings, reported but not repaired.** The published fit carries indicators for
high and low severity only, so its reference category is 671 quadrature points of which 553 are
moderate severity, the class carrying the most beetle attack. And adding the product terms moves the
high-severity main effect from +0.207 to -0.139, which is not how a real product term behaves. The
specification is reproduced rather than corrected, because the object was to test the published model
rather than to replace it, and the manuscript says so.

**The seedling count is settled.** `Seedlings.shp` holds 3,912 points; 46 carry species code 6, which
is outside the seven-species lookup; 3,866 remain and every one falls inside the plot windows. So the
two counts in circulation differ by a species filter and nothing else. The published abstract's 3,886
matches neither and is reproduced by no filter tried. Trap 9 can be closed on the first two and stands
on the third. **Still worth querying with the author.**

**A bug worth recording.** The first block bootstrap returned no usable draws at any block size and
every interval came back `NA`. The cause is scoping, not statistics: `glm` resolves `weights` in the
formula's environment when it is not a column of `data`, the formula carried the global environment,
and the function-local weight vector was invisible from there. Every fit failed and `try` swallowed
all of it. The fix is to keep the weight as a column of the frame. The general lesson is that a
bootstrap returning all-`NA` is a code failure until proven otherwise, and `try` inside a loop needs a
usable-draw count reported alongside the interval. `tbl-ppblocks` carries one.

### Phases 3 and 4, framing and writing (5 August 2026)

The framing question the task request deferred to Phase 3 answers itself on the Phase 2 result. The
paper is not about a compound-disturbance interaction. It is about the gap between a claim and the
inference offered for it, with the interaction as the worked example, and the title chosen on
2 August survives exactly as intended.

Written: `sec-discussion` with subsections on findings, the general result, extent, limitations and
what would settle the open questions; and `sec-conclusions`. The `sec-status` placeholder is gone. The
abstract is rewritten and is no longer marked provisional. The introduction gains a paragraph
previewing the second result. Two references added for the Berman-Turner device, `berman1992` and
`baddeley2000`, both verified against the CrossRef record by DOI rather than by title, because a title
search for the second returns a different item of the same name.

**Render time roughly doubled**, from about 90 seconds to about 3 minutes 20, all of it the new block
bootstrap. Acceptable, and cheaper than moving the analysis out of the document.

## Next steps

The analysis is complete and the manuscript is a complete draft. What remains is author decisions and
housekeeping, not work that changes a number.

1. **Venue, and it is the binding item.** See `VENUE-NOTE-2026-08-05.md`. Two emails settle it: read
   the Forests feature-paper invitation of 24 June 2026 for its APC terms and its scope language, and
   ask the *Forest Ecology and Management* editor whether a re-analysis of a paper they published in
   2026 is admissible and under what article type. Both publisher sites returned 403 to a direct
   fetch, so nothing in that note was read off the live page and every figure in it needs confirming
   in a browser. Do no template work before this resolves; the Elsevier extension is vendored and
   the document already renders to Word, so formatting is cheap and late.

2. **Query the published 3,886 with the author.** `Seedlings.shp` holds 3,912 points and the
   seven-species filter leaves 3,866. No filter tried reproduces 3,886. The manuscript says so.

3. **Two author decisions carried over.** Whether to unify the `tbl-crosscheck` and `tbl-host`
   frames or to state their 68-cell difference in the Methods; a `stopifnot` currently prevents the
   divergence widening silently. And whether copyrighted PDFs may sit in `04.references/literature/`
   given the repository is public, the parent paper's own PDF being gitignored for that reason.

4. **Housekeeping.** Register as a submodule of `claude-science-library`.

5. **Not needed after all.** The moderate-severity intersection raster, listed here on 2 August as a
   Phase 2 prerequisite, was never required: the interaction is fitted from the severity class masks
   directly, so the intersection rasters play no part in it. And the caution that the interaction was
   being added to a model whose grey main effect is null proved correct and is now derived in the
   document rather than recalled, in `tbl-ppreproduce`.
