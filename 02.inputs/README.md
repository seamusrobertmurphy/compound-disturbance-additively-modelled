# Data provenance

Central register for every dataset the manuscript reads. Each subfolder carries its own
`README.md` with the detail; this file holds the summary and must not contradict them.

**Nothing in this repository stores the rasters themselves.** They live in the parent study's
working directory and are read at render time from `DARKWOODS_DATA`, which defaults to
`/Users/seamus/repos/publications-pending/Darkwoods-Disturbance-Paper/3.SpatialData`. Set the
environment variable to relocate them. The provincial survey is read from `DARKWOODS_AOS`, which
defaults into the companion refugia repository rather than duplicating a 950 MB geodatabase, and the
corrected grey-stage package from `DARKWOODS_GREYFIX`, which defaults to
`Archive/Greystage_Raster_Fix_2026-06-02/` in the parent study's working directory.

## Sources

| Dataset | Folder | Origin | Licence | Retrieved | Used for |
|---|---|---|---|---|---|
| Beetle annual series and derived stages | `beetle-stages/` | Landsat classification, parent study | Author's own, unpublished derivative | 2021, built for @murphy2026 | Question A response, question B covariate |
| Corrected grey-stage package | `beetle-stages/` | Verification re-run of 2 June 2026 | Author's own | 2026-06-02, @murphy2026greyfix | The primary beetle surface |
| Burn severity, classified | `fire-severity/` | Landsat dNBR classification, parent study | Author's own, unpublished derivative | 2021, built for @murphy2026 | Both questions |
| Beetle by fire intersections | `beetle-fire/` | Parent study, never used in any manuscript | Author's own | 2021 | Question B interaction term |
| Fire perimeter | `fire-severity/` | Parent study | Author's own | 2021 | The provenance check |
| Aerial Overview Survey | `aerial-survey/` | BC Ministry of Forests | Open Government Licence BC | 2026-07-30 | Independent check on the classified beetle layer |
| Seedling point pattern | `seedlings/` | Field mapping, three 4 ha plots | Author's own | 2021 | Question B response |
| Terrain and wind | `terrain/` | Parent study, from NRCan HRDEM and Global Wind Atlas | Mixed, see folder | 2021 | Question B covariates |

## The trap that governs everything

The annual beetle classifications are **clipped to the fire perimeter, in the source files**. All
nine carry an identical nodata count and observe only 10 of the 3,429 cells lying outside the
perimeter. Every beetle surface in the study descends from them, so none of them can see attack
outside the burn, while the independent survey records 40 per cent of that ground as attacked.
`Beetle.Outbreak.RedStage.tif` carries a second, narrower clip to the classified severity footprint,
because it was substituted for a layer missing from the repository. This is established in
`01.manuscript/` §3, not asserted here.

The consequence is a rule, not a caveat. **Any comparison that crosses the fire perimeter measures
the clip.** Comparisons made entirely inside it are unaffected, because every severity class is
observed at essentially 100 per cent and is equally exposed.

## Cross-cutting traps

1. **`dplyr::intersect` masks `terra::intersect`.** Namespace it. This broke a render in the
   companion project.
2. **Read the survey geodatabase with an `extent` filter**, built in EPSG:3005 and projected
   afterwards, never the reverse. The whole provincial layer is memory-hostile on an 8 GB machine.
3. **Three coordinate systems are in play**: the analysis grids are EPSG:32611, the survey is
   EPSG:3005, and the fire perimeter and BEC zones ship as EPSG:4326.
4. **The disturbance grids are not co-registered.** Beetle is 29.558 m on a 135 by 66 grid, severity
   is 30.000 m on 134 by 66, and the intersection rasters are 29.558 m on 136 by 67. Resample to a
   named target with `method = "near"` and say which one; do not let an implicit alignment decide.
   The eight apparently unburned attacked cells reported during scoping are an artefact of pairing
   two of these grids without resampling. At native alignment the count is zero.
