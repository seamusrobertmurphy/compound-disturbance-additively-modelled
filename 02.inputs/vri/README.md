# BC Vegetation Resources Inventory: the host layer

Without a host layer, a cell with no beetle attack cannot be told apart from a cell with no pine.
This is the layer that makes the confound in question A addressable at all.

## Source and licence

| | |
|---|---|
| Layer | `WHSE_FOREST_VEGETATION.VEG_COMP_LYR_R1_POLY`, pulled by WFS bounding box |
| Publisher | Province of British Columbia, Ministry of Forests |
| Portal | https://catalogue.data.gov.bc.ca/dataset/vri-2023-forest-vegetation-composite-polygons |
| Licence | Open Government Licence, British Columbia |
| Extent pulled | The Darkwoods study window, 2,743 polygons |
| CRS | EPSG:3005, BC Albers |
| Retrieved | 2026-07-30 |

## Not stored here

Shared with the companion refugia study rather than duplicated. The manuscript reads it from
`DARKWOODS_VRI`, which defaults to that repository's `02.inputs/vri/vri_darkwoods.geojson`.

## How the manuscript uses it

Lodgepole cover is summed across the three species slots, because a polygon may carry pine in any of
`SPECIES_CD_1`, `_2` or `_3`, matching any code beginning `PL`. That gives a percentage per polygon,
rasterised onto the beetle grid and reduced to presence for the model. Inside the fire perimeter the
inventory covers every cell for species composition.

## Traps

1. **Host and elevation cannot be separated at this extent.** Across the fire clip lodgepole cover
   correlates with elevation at 0.52. Entered together, elevation clears the block interval and host
   does not, despite a crude contrast of 35.3 per cent attacked where lodgepole is present against
   15.3 per cent where it is absent. The companion study separates the two because its 1,776 m of
   relief contains pine-poor ground at every height; eight square kilometres does not. **Do not read
   the null host coefficient as evidence that host does not matter.**

2. **Basal area is missing on a large minority of cells**, 1,567 of the 5,481 inside the perimeter.
   Species composition is complete where basal area is not, which is why the manuscript uses cover
   rather than basal area. Any model that switches to basal area silently changes the analysis frame.

3. **Match species codes with a prefix, not equality.** Lodgepole appears as both `PL` and `PLI` in
   `SPECIES_CD_1` alone, and the full code list over this window runs to twenty-one species.

4. **The layer is EPSG:3005** and every analysis grid is EPSG:32611. Project after reading.

5. **The inventory is a photo-interpreted projection, not a measurement**, and its attribution date
   is not the outbreak date. It records what the stand was mapped as, which is the right covariate
   for host availability and the wrong one for stand condition after attack.
