# Phase 0 result: the beetle time series is clipped to the fire perimeter

**2 August 2026, revised the same day** against the corrected rasters of 2 June 2026. The superseded
first version is at `../Archive/2026-08-02-phase0-provenance_pre-greyfix.md`. Full derivation is in
`01.manuscript/compound-disturbance-additively-modelled.qmd` §3, in live chunks. Nothing here is
quoted from a script; this note is a pointer and a summary, not a source.

## The test

The task request's §7 Phase 0 asked whether the beetle red-stage raster is confined to the fire
perimeter, and whether that would manufacture the association its §4 reported. Four checks:

1. Every beetle surface cross-tabulated against the fire perimeter at native alignment.
2. Nodata in the nine annual classifications, against the perimeter.
3. The published red-stage surface against the corrected grey-stage union of 2 June 2026, which is
   built from the same annual files by an independent route.
4. Both local surfaces against the provincial Aerial Overview Survey, class by class.

## The result

| | |
|---|---|
| Cells outside the fire perimeter | 3,429 |
| Of those, observed in any annual raster | **10** |
| Nodata cells per annual file, all nine identical | 3,423, of which 3,419 outside the perimeter |
| Corrected grey union, cells outside the perimeter | 1 of 1,541 |
| Published red-stage surface, cells outside the perimeter | 0 of 493 |
| Survey attack rate outside the perimeter | 40.4 per cent |

The clip is in the source data. Whoever prepared the annual time series clipped it to the burn
before the classification that used it was ever run, and every beetle surface in the study inherits
the boundary.

## Two clips, one inside the other

| Region | Cells | Annual data | Grey attack | Red attack |
|---|---:|---:|---:|---:|
| Outside the fire perimeter | 3,429 | 0.3 % | 0 %, on 10 observed cells | 0 % |
| Inside perimeter, unclassified severity | 1,367 | 99.7 % | 33.1 % | **0 %** |
| Inside the classified severity footprint | 4,136 | 99.5 % | 26.3 % | 11.9 % |

The published red-stage surface reads zero on ground that the corrected grey union reads as a third
attacked. That contrast cannot be ecological. The cause is documented in the parent study's memo:
`mpb_red_na.tif`, the layer the published analysis intended, is missing from the repository and
`Beetle.Outbreak.RedStage.tif` was substituted for it.

## What it costs and what it leaves

Any comparison crossing the fire perimeter measures the clip, so question A cannot be asked as
burned against unburned, and the local data is too nearly absent out there to rescue it. Ten cells
corroborate nothing. The argument rests on the survey alone, which is sufficient: an independent
census of the same ground in the same years finds beetle attack in ordinary abundance.

Comparisons inside the perimeter are unaffected, because every severity class is observed at
essentially 100 per cent. There, three records agree and all peak at moderate severity:

| Class | Grey | Red | Survey |
|---|---:|---:|---:|
| Low | 20.8 % | 6.3 % | 24.5 % |
| Moderate | **34.6 %** | **20.7 %** | **40.6 %** |
| High | 27.7 % | 12.1 % | 33.1 % |

Question B is untouched: the seedling point pattern lies wholly inside the burn.

## The caveat that governs Phase 1

Moderate severity occupies the highest mean elevation of the three burned classes at 1,449 m, and
the companion study finds beetle attack peaking near 1,430 m for reasons unrelated to fire. The
agreement between the three records may be agreement about elevation. Condition on host and
elevation before believing the gradient.

## One method note worth carrying forward

Key any class table on the perimeter first and on severity within it. Keyed on the severity code
alone, the outside-perimeter row picks up 67 cells that actually lie inside the perimeter and
inflates the observed-outside sample sevenfold, from 10 cells to 73. That error was made in the
first version of this analysis and caught here.
