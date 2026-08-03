# Progress log: compound beetle and fire disturbance at Darkwoods

**Started:** 2026-08-02
**Status:** Phases 0 and 1 complete. Phase 2, the interaction refit, is next.
**Last updated:** 2026-08-02
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

## Next steps

1. **Phases 0 and 1 are done.** See the entries above. `mpb_red_na.tif` is confirmed gone from the
   parent tree, so the narrower of the two clips cannot be lifted without rebuilding the layer.

2. **Phase 2, the interaction refit.** The outstanding analysis, and untouched by the clip because
   the seedling point pattern lies wholly inside the burn. Refit the published additive point
   process model with the beetle by fire product term and compare against the published fit. Two
   things to do first. Build the missing moderate-severity intersection raster, since only high and
   low exist and moderate carries the most attack of the three. And settle the seedling frame at
   3,912 or 3,866, stating which in the Methods and querying the published 3,886 with the author.

   Use the corrected grey union, not the published red-stage surface, wherever either would serve.
   Note that the parent study's own corrected refit already puts the grey-stage main effect at
   roughly zero, p = 0.99, so the interaction term is being added to a model whose grey main effect
   is null. That is worth stating plainly rather than discovering late.

3. **Framing, with the author.** Deferred to Phase 3 as the task request specifies. Phases 0 and 1
   already give the paper a spine that does not depend on the interaction test resolving either way:
   a provenance result that invalidates the burned-against-unburned comparison, a narrow within-burn
   result that survives conditioning, and two negative results that are both about extent.

4. **Housekeeping.** Register as a submodule of `claude-science-library`. Verify the venue against
   live guidelines before any template work; note the Forests feature-paper invitation of 24 June
   2026. Decide whether copyrighted PDFs may sit in `04.references/literature/` given the repository
   is public; the parent paper's own PDF is gitignored for that reason.
