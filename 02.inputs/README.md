# Data provenance

Central register for every dataset the manuscript reads. Each subfolder carries its own
`README.md` with the detail; this file holds the summary and must not contradict them.

**Nothing in this repository stores the rasters themselves.** They live in the parent study's
working directory and are read at render time from `DARKWOODS_DATA`, which defaults to
`/Users/seamus/repos/publications-pending/Darkwoods-Disturbance-Paper/3.SpatialData`. Set the
environment variable to relocate them. The provincial survey is read from `DARKWOODS_AOS`, which
defaults into the companion refugia repository rather than duplicating a 950 MB geodatabase.

## Sources

| Dataset | Folder | Origin | Licence | Retrieved | Used for |
|---|---|---|---|---|---|
| Beetle red and grey stage, annual series | `beetle-stages/` | Landsat NDMI classification, parent study | Author's own, unpublished derivative | 2021, built for @murphy2026 | Question A response, question B covariate |
| Burn severity, classified | `fire-severity/` | Landsat dNBR classification, parent study | Author's own, unpublished derivative | 2021, built for @murphy2026 | Both questions |
| Beetle by fire intersections | `beetle-fire/` | Parent study, never used in any manuscript | Author's own | 2021 | Question B interaction term |
| Fire perimeter | `fire-severity/` | Parent study | Author's own | 2021 | The provenance check |
| Aerial Overview Survey | `aerial-survey/` | BC Ministry of Forests | Open Government Licence BC | 2026-07-30 | Independent check on the classified beetle layer |
| Seedling point pattern | `seedlings/` | Field mapping, three 4 ha plots | Author's own | 2021 | Question B response |
| Terrain and wind | `terrain/` | Parent study, from NRCan HRDEM and Global Wind Atlas | Mixed, see folder | 2021 | Question B covariates |

## The trap that governs everything

The classified beetle red-stage surface is **masked to the classified burn-severity footprint**. It
reports zero attack in every cell outside that footprint, including roughly three square kilometres
of adjoining unburned forest that the independent survey records as heavily attacked. This is
established in `01.manuscript/` §3 and is not a matter of opinion: all 493 attacked cells fall
inside the fire perimeter and none falls outside it.

The consequence is a rule, not a caveat. **Any comparison that crosses the boundary of the
classified burn measures the mask.** Comparisons made entirely inside it are unaffected, because
every severity class sits within the mask and is equally exposed to it.

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
