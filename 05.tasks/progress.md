# Progress log: compound beetle and fire disturbance at Darkwoods

**Started:** 2026-08-02
**Status:** Phase 0 complete and revised against the corrected rasters of 2 June 2026.
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

0. **Find `mpb_red_na.tif`**, or establish that it is gone. It is the layer the published analysis
   intended for red attack, and its absence is why the red surface carries the narrower of the two
   clips. Cheap, and it improves everything downstream.

1. **Phase 1, conditioned on host.** Bring in the Vegetation Resources Inventory host layer the
   sibling study retrieved, and recompute the within-burn severity gradient conditioned on lodgepole
   presence and on elevation. If the non-monotone shape survives both, it is a result. If it
   flattens, the study is about the elevation confound and that is still a real contribution.
   Report effect sizes with spatial block intervals at roughly 1 km blocks. Moran's I on the
   red-attack union is 0.728, so naive p-values are worthless. Do not report one.

2. **Phase 2, the interaction refit.** Question B is untouched by the mask, because the seedling
   point pattern lies wholly inside the burn. Refit the published additive point process model with
   the beetle by fire product term and compare. Build the missing moderate-severity intersection
   raster first; only high and low exist, and moderate carries the most red attack of the three.

3. **Framing, with the author.** Deferred to Phase 3 as the task request specifies. The Phase 0
   result already gives the paper a spine that does not depend on the interaction test resolving
   either way.

4. **Housekeeping.** Register as a submodule of `claude-science-library`. Verify the venue against
   live guidelines before any template work; note the Forests feature-paper invitation of 24 June
   2026. Decide whether copyrighted PDFs may sit in `04.references/literature/` given the repository
   is public.
