# Beetle stage surfaces

Landsat NDMI classifications of mountain pine beetle mortality, built in 2021 for the parent study
[@murphy2026]. Not stored here; read at render time from `DARKWOODS_DATA/beetle_stages`.

| File | What it is | State |
|---|---|---|
| `Beetle.Outbreak.RedStage.tif` | Binary red attack, 135 by 66 at 29.558 m | 493 attacked cells, **masked to the burn** |
| `Beetle.Outbreak.GreyStage.tif` | Binary grey attack, same grid | 270 cells, **not the layer to use**, see trap 2 |
| `Beetle.Outbreak.{2005..2011,2013,2014}.tif` | Annual classifications | Two incompatible products, see trap 3 |
| `MPB.classified.spatstat.tif` | Continuous NDMI surface, 52 by 47 at 29.492 m | -0.175 to 0.009, the only surviving continuous spectral surface |
| `mpb_grey_attackcount.tif` | Years-attacked count | **Stale**, 932 cells, built from the superseded grey layer |
| `MPB_BC_AerialSurveys.shp` | Local clip of the provincial survey | Geometry only, no `.dbf`, no `.prj`. Use `aerial-survey/` instead |

## How the manuscript uses it

`Beetle.Outbreak.RedStage.tif` is the question A response, read only within the classified burn
footprint for the reason in trap 1. The continuous surface and the grey union are question B
covariates and are not yet in the document.

## Traps

1. **The red-stage surface is masked to the classified burn footprint.** All 493 attacked cells lie
   inside the fire perimeter, none outside, on a raster that extends 763 m beyond it. The
   independent Aerial Overview Survey records 40.8 per cent of that outside ground as attacked. Read
   the zero as unobserved, never as unattacked. This is the study's first result and it is derived
   in the manuscript, not asserted here.

2. **Use the 1,541-cell grey union, never `GreyStage.tif` (270) or `mpb_grey_attackcount.tif`
   (932).** The correct layer is the union of code `44` across the annual rasters for 2005 to 2011,
   which is what the parent study's abstract describes and what reproduces at 1,541 cells. The 2013
   and 2014 files contribute nothing to it because they carry no code 44 at all. Corrected
   regeneration values that go with the 1,541-cell layer are grey 33.6 per cent with 1,315
   seedlings, red 24.7 per cent with 965 seedlings.

3. **The annual series is two products, not one.** Files for 2005 to 2011 share a code set of
   1, 36, 44, 61, 77, 80, 94 and 105 with -128 as background in all but 2005. Files for 2013 and
   2014 carry codes 2 to 7 and nothing else. There is no 2012 file. Do not stack the series without
   deciding what each code means in each product.

4. **2008 and 2010 hold no code 44.** For 2008 the file holds only codes 80 and 105, so it carries
   no attack classification at all. Absence of red attack in those years is a property of the
   product, not of the outbreak.

5. **The grid is 29.558 m, not 30 m**, and does not align with the severity rasters. See
   `../README.md` trap 4.
