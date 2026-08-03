# compound-disturbance-additively-modelled

**Compound disturbance, additively modelled.** Testing whether beetle mortality and fire severity
interact, in the landscape and in the model, Darkwoods Conservation Area, British Columbia.

Third paper in a family. The parent is published as Murphy et al. 2026, *Forest Ecology and
Management* 618:123985. Its abstract describes the additive effects of increasing beetle to fire
disturbance interactions; its model enters beetle and fire as additive main effects with no product
term. This paper tests the interaction the parent asserted, and asks whether the two agents are
associated on the ground at all.

**Status:** Phase 0 complete, renders end to end. Everything after §3 of the manuscript is
outstanding.
**Sibling and template:** `../beetle-topography-and-wind-study` in `claude-science-library`.

## Entry point

`01.manuscript/compound-disturbance-additively-modelled.qmd` is the single source of truth. **If it
is not in the manuscript, it is not part of the study.** Every number in the prose is an inline `r`
expression and every chunk carries an explicit `#| echo: true`. No `echo: false`, no
`include: false`, no `eval: false`. Nothing runs outside the render.

```bash
quarto render 01.manuscript/compound-disturbance-additively-modelled.qmd --to html
```

A render takes about a minute. It needs `DARKWOODS_DATA` and `DARKWOODS_AOS`, which default to the
parent study's working directory and to the sibling repository respectively. **Check
`/Volumes/PortableSSD` is mounted first.**

`README.md` is generated from the render by `03.outputs/build-readme.py`. Rerun it after every
render; never edit it by hand.

## The finding so far

**The classified beetle red-stage surface is masked to the classified burn-severity footprint.**
All 493 attacked cells lie inside the fire perimeter and none lies outside it, on a raster that
extends 763 m beyond the perimeter across 2.98 km² of unburned forest. The independent provincial
Aerial Overview Survey records 40.8 per cent of that outside ground as attacked, and 52.0 per cent
of the unclassified ground inside the perimeter, the highest rate of any class. The zeroes are
unobserved, not unattacked.

Three consequences.

1. **Any burned against unburned comparison measures the mask.** The scoping document's headline
   contingency, attack rising from 0.2 per cent in unburned forest to 19.9 per cent at moderate
   severity, is an artefact. Question A cannot be asked in that form.
2. **The within-burn gradient survives**, because all three severity classes sit inside the mask and
   are equally exposed to it. Red attack runs 6.3 per cent at low severity, 20.6 at moderate and
   12.1 at high, and the independent survey traces the same non-monotone shape at 24.3, 40.5 and
   33.0 per cent. Two records sharing no measurement pathway agree that attack peaks at moderate.
3. **Question B is untouched.** The seedling point pattern lies wholly inside the burn, so every
   cell entering the point process model sits within the mask and is equally affected by it.

**The caveat that governs Phase 1.** Moderate severity also occupies the highest mean elevation of
the three burned classes at 1,448 m, and the sibling study finds beetle attack peaking near 1,430 m
for reasons unrelated to fire. The agreement may be agreement about elevation. Condition on host and
elevation before believing the gradient.

## Layout

| Path | What is there |
|---|---|
| `01.manuscript/` | The `.qmd` and its renders. Edit the `.qmd`, never a render |
| `02.inputs/` | No data, only provenance. `README.md` is the central register; every subfolder carries its own |
| `03.outputs/` | `PNG/` figures at 300 dpi, `TBL/` tables as CSV, `MD/` notes, and `build-readme.py` |
| `04.references/` | `references-compound.bib`, its manifest, CSL, Word style, and the parent paper |
| `05.tasks/` | **Start at `TASK-REQUEST-2026-08-02.md`, then `progress.md`** |

## Data

No raster is stored in this repository. All are read at render time.

- **Disturbance surfaces**, beetle and fire, from the parent study's working directory via
  `DARKWOODS_DATA`. Built in 2021 from Landsat NDMI and dNBR classifications.
- **Aerial Overview Survey**, the independent check, shared with the sibling repository via
  `DARKWOODS_AOS` rather than duplicating 950 MB. Open Government Licence BC, retrieved 30 July 2026.
- **Seedling point pattern and terrain**, from the parent study, unchanged.

## Traps

1. **The red-stage mask governs everything.** Any comparison crossing the classified burn boundary
   measures the mask. Comparisons made entirely inside it are fine.
2. **The severity codes are not in severity order.** `1` is high, `32` is low, `34` is moderate. A
   table built on numeric order inverts the top two classes. The manuscript derives the mapping in
   code and asserts it with `stopifnot`. Do not hard-code it.
3. **Code 16 is not a severity class.** It is 1,268 cells inside the perimeter that no class mask
   claims, and it lies outside the classified footprint. Treat as unobserved, not unburned.
4. **The disturbance grids are not co-registered.** Beetle 29.558 m on 135 by 66, severity 30 m on
   134 by 66, intersections 29.558 m on 136 by 67. Resample to a named target explicitly. The eight
   stray unburned attacked cells reported during scoping are this, and vanish at native alignment.
5. **Use the 1,541-cell grey union**, the union of code 44 over 2005 to 2011. Not `GreyStage.tif`
   (270) and not `mpb_grey_attackcount.tif` (932, stale).
6. **The annual beetle series is two incompatible products.** 2005 to 2011 use one code set, 2013
   and 2014 use another and carry no code 44 at all. There is no 2012 file. So the 2005 to 2011 and
   2005 to 2014 unions are identical, which looks like corroboration and is not.
7. **Three seedling counts are in circulation**: 3,912, 3,866 and the published 3,886. The two file
   families carry different schemas and are different products. Resolve before Phase 2.
8. **Extent is the live methodological risk.** Everything but the terrain grid sits inside an 8 km²
   clip, which is precisely the extent the sibling study shows can reverse a coefficient's sign.
9. **Moran's I on the red-attack union is 0.728.** Use spatial block intervals at roughly 1 km
   blocks. Do not report a naive p-value.
10. **`dplyr::intersect` masks `terra::intersect`.** Namespace it.
11. **Do not re-present the published index comparison.** The five fire and four beetle indices,
    their separability, ANOVA and SVM diagnostics are in the parent paper's main text and
    supplement, and in three public repositories. Cite them, never re-table them.

## Open items

- **Cross-agent spectral separability is blocked, not deferred.** Both fire severity surfaces on
  disk are classified, no continuous dNBR exists, and no Landsat bands or NDMI rasters survive to
  recompute one from. It would mean re-acquiring the archive and re-deriving the published methods.
  See `05.tasks/TASK-REQUEST-2026-08-02.md` §2.
- **Recovering question A in its original form** would mean rebuilding the red-attack classification
  over the unmasked landscape. That is a Landsat reprocessing task, and it runs into the same
  dual-publication problem.
- **Phase 1 and Phase 2 are both live and independent of each other.** See `05.tasks/progress.md`
  "Next steps".
- **Not yet a submodule of `claude-science-library`.** The task request asked for this; the
  repository was created standalone before the request was worked.
- **Venue is the author's decision.** Note only that a Forests feature-paper invitation dated
  24 June 2026 exists and postdates every earlier venue scan. Verify guidelines live, not from
  memory.
