# BC Aerial Overview Survey: pest infestation polygons

**The independent check on the classified beetle layer**, and the reason the provenance result in
the manuscript is a finding rather than a suspicion.

The Aerial Overview Survey is the operational provincial record of forest health. Observers
sketch-map damage annually from fixed-wing aircraft and label each polygon by year, causal agent,
severity class and host species.

## Source and licence

| | |
|---|---|
| Layer | `pest_infestation_poly` (File Geodatabase), 1,172,716 features |
| Publisher | Province of British Columbia, Ministry of Forests |
| Portal | https://catalogue.data.gov.bc.ca/dataset/pest-infestation-polygons |
| Direct download | https://pub.data.gov.bc.ca/datasets/450b67bb-02d5-4526-8bc0-ac7924125a1e/pest_infestation_poly.zip |
| Licence | Open Government Licence, British Columbia |
| Coverage | Province-wide, all agents, survey years 1965 to 2025 |
| Size | 769 MB zipped, 950 MB unzipped |
| Retrieved | 2026-07-30 |

## Not stored here

The geodatabase is shared with the companion refugia study rather than duplicated. The manuscript
reads it from `DARKWOODS_AOS`, which defaults to that repository's `02.inputs/aos/`. Re-download it
from the link above if the companion repository is unavailable, and point the environment variable
at wherever it lands.

## How the manuscript uses it

Filtered by extent to the terrain grid, then to `PEST_SPECIES_CODE == "IBM"` and `CAPTURE_YEAR`
within 2005 to 2014, the outbreak window preceding the fire. That gives 276 polygons of the 608
damage polygons of all agents in the window. Rasterised onto the beetle grid as presence, and
compared class by class against the local classified surface.

Its value here is precisely that its errors are observer errors. Whatever is wrong with a
sketch-mapped polygon is uncorrelated with whatever is wrong with a Landsat classification, so
where the two disagree by two orders of magnitude the disagreement is structural rather than noise.

## Traps

1. **Always pass an `extent` filter when reading.** The whole provincial layer is memory-hostile on
   an 8 GB machine.
2. **The geodatabase is EPSG:3005** (BC Albers) and the analysis grids are EPSG:32611. Build the
   extent filter in 3005 and project the result afterwards, not the other way round.
3. **Polygon presence is not cell-level attack.** An observer draws a boundary around a patch with
   scattered mortality, so rasterised presence overstates the attacked area. This is why the
   manuscript compares the *contrast* between classes across the two records rather than their
   absolute rates.
4. **Do not use `beetle_stages/MPB_BC_AerialSurveys.shp`** as a substitute. It is a local clip
   carrying geometry only, with no `.dbf` and no `.prj`, so it has neither year nor agent nor
   severity and no declared coordinate system.
