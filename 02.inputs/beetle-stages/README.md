# Beetle stage surfaces

Classifications of mountain pine beetle mortality built for the parent study [@murphy2026], plus the
corrected grey-stage package of 2 June 2026 [@murphy2026greyfix]. Nothing is stored here. The
annual and derived rasters are read at render time from `DARKWOODS_DATA/beetle_stages`, and the
corrected grey package from `DARKWOODS_GREYFIX`, which defaults to
`Archive/Greystage_Raster_Fix_2026-06-02/` in the parent study's working directory.

| File | What it is | State |
|---|---|---|
| `Beetle.Outbreak.{2005..2011}.tif` | Annual classifications, 135 by 66 at 29.558 m | **The source of everything.** Clipped to the fire perimeter, see trap 1 |
| `Beetle.Outbreak.{2013,2014}.tif` | Annual, unrelated code set | Contribute nothing, see trap 4 |
| `mpb_grey_corrected.tif` | Union of code 44 across 2005 to 2011 | **1,541 cells. Use this one** |
| `mpb_grey_with_redstage.tif` | Above, unioned with the red-stage surface | 1,579 cells, backward-compatible variant |
| `mpb_grey_attackcount_v2.tif` | Attack years per cell, 0 to 5 | Corrected replacement for the stale count |
| `Beetle.Outbreak.RedStage.tif` | Binary red attack | 493 cells. A **substitute** for a missing layer, see trap 2 |
| `Beetle.Outbreak.GreyStage.tif` | Binary grey attack | 270 cells, **deprecated** |
| `mpb_grey_attackcount.tif`, `mpb_grey_na.tif` | Legacy count and mask | **Stale**, 932 cells, built with the wrong value test |
| `MPB.classified.spatstat.tif` | Continuous NDMI surface, 52 by 47 | -0.175 to 0.009. The only surviving continuous spectral surface, and it covers only 2.13 km² |
| `MPB_BC_AerialSurveys.shp` | Local clip of the provincial survey | Geometry only, no `.dbf`, no `.prj`. Use `../aerial-survey/` instead |

## How the manuscript uses them

The corrected grey union is the primary beetle surface. The published red-stage surface is carried
alongside it because it is what the parent study modelled, not because it is better. Both are read
only where the annual rasters actually observe, which the manuscript computes rather than assumes.

## Traps

1. **The annual rasters are clipped to the fire perimeter, at source.** All nine carry an identical
   3,423 nodata cells, of which 3,419 lie outside the perimeter, out of 3,429 cells outside it.
   Only 10 cells beyond the perimeter are observed in any year. Every beetle surface in the study
   descends from these files and inherits the boundary, so **no beetle layer on disk can see attack
   outside the burn**. The independent survey records 40 per cent of that outside ground as
   attacked. Treat absence beyond the perimeter as unobserved, never as unattacked. This is the
   study's first result and it is derived in the manuscript, not asserted here.

2. **There are two clips, one inside the other, and `Beetle.Outbreak.RedStage.tif` carries the
   narrower.** It records attack only within the classified severity footprint and reads exactly
   zero across the 1,367 cells that lie inside the perimeter but in no severity class, where the
   corrected grey union records 33.1 per cent. The reason is documented: the layer the published
   analysis intended, `mpb_red_na.tif`, **is missing from the repository**, and this one was
   substituted for it. Look for the missing layer before using the red surface again.

3. **Use `mpb_grey_corrected.tif`, never `GreyStage.tif` (270) or `mpb_grey_attackcount.tif` (932).**
   The legacy rebuild tested `annual == 1`, but the annual rasters carry a classification legend
   rather than a binary mask, and `1` is a sparse trace class. The legend follows the provincial
   survey's severity coding scheme; the layers themselves are Landsat classifications, not survey
   products. The active red-attack code is `44`. The correct union is 1,541 cells, which reproduces independently. Corrected regeneration
   values that go with it are grey 33.6 per cent with 1,315 seedlings, red 24.7 per cent with 965.
   The Cox grey-stage coefficient in the published Table 12 was computed on a sample seven to eight
   times smaller than it should have been; the corrected refit gives beta near zero, p = 0.99.

4. **The annual series is two products, not one.** Files for 2005 to 2011 share a classification
   legend of codes 1, 36, 44, 61, 77, 80, 94 and 105. Files for 2013 and 2014 carry codes 2 to 7 and no code 44 at
   all, and there is no 2012 file. So the code-44 union is identical whether the window is 2005 to
   2011 or 2005 to 2014, which looks like agreement between two windows and is nothing of the kind.

5. **2008 and 2010 hold no code 44.** For 2008 the file holds only codes 80 and 105. Code 105 covers
   most of the scene at weak enrichment and is a host-stand mask in that year's encoding, not active
   attack. Absence of red attack in those years is a property of the product, not of the outbreak.

6. **The grid is 29.558 m, not 30 m**, and does not align with the severity rasters. See
   `../README.md` trap 4.
