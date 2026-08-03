# Terrain, wind and ecosystem context

Covariate surfaces inherited unchanged from the parent study [@murphy2026] and shared with the
companion refugia study. Not stored here; read at render time from
`DARKWOODS_DATA/terrain_environment`, `DARKWOODS_DATA/bec_zones` and
`DARKWOODS_DATA/plot_locations`.

## Terrain and wind

All 695 by 639 at 25.113 m, EPSG:32611, spanning 280 km² and 1,776 m of relief. This is the only
grid in the study that extends beyond the fire clip, which is what makes the provenance check in the
manuscript possible at all.

| File | What it is |
|---|---|
| `Elevation.utm.tif` | Elevation. **The analysis grid**: everything else resamples onto it |
| `Slope.utm.tif`, `Slope.discrete.tif` | Slope, continuous and classed |
| `Aspect.utm.tif`, `Aspect.discrete.tif` | Aspect, continuous and classed |
| `TWI.utm.tif` | Topographic wetness index |
| `Rutm.tif` | Ruggedness index |
| `Wind.utm.tif`, `Wind.discrete.tif` | Wind speed, downscaled from the Global Wind Atlas |
| `Precip.discrete.tif`, `classified1.tif` | Classed precipitation and a land classification |

## Ecosystem and plot context

`bec_zones/BEC.ecozones.shp` holds 8 biogeoclimatic polygons in EPSG:4326 across three zones.
`plot_locations/` holds the three 4 ha regeneration plots as shapefiles and rasters.

## Traps

1. **The wind surface is a downscaling of a coarse mesoscale field over this very elevation model**,
   so it is not independent of terrain, and the dependence tightens as the analysis extent shrinks.
   Over an 8 km² clip most of its variation is elevation. The companion refugia study finds that
   this reverses the sign of the wind coefficient at small extents. Any question B model that
   carries both wind and elevation over the fire clip inherits that problem directly.

2. **Extent is the live methodological risk of this study.** Everything except the terrain grid sits
   inside an 8 km² clip, which is precisely the extent the companion study warns about. Handle it in
   the Methods rather than hoping a referee misses it.

3. **The terrain grid is 25.113 m** and every disturbance grid is roughly 29.5 or 30 m. Resample
   explicitly to a named target and say which.

4. **BEC zones ship as EPSG:4326.** Project before use.

5. **Ground plot coordinates for the 28 beetle basal-area plots do not exist** in the companion
   study, which used them to calibrate a severity scale rather than to validate placement. Check
   before assuming the 94 CBI fire plots are any different.
