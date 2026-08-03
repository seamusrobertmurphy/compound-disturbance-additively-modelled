# Burn severity and fire perimeter

Landsat dNBR classifications of the 2015 Mt Midgeley wildfire, built in 2021 for the parent study
[@murphy2026]. Not stored here; read at render time from `DARKWOODS_DATA/fire_severity` and
`DARKWOODS_DATA/fire_perimiter`. The upstream folder name is misspelled and the path in the
manuscript matches the misspelling deliberately.

| File | What it is |
|---|---|
| `Fire.Severity.NDBR.tif` | Classified severity, 134 by 66 at 30 m, integer codes |
| `Fire.Severiry.NDBR.tif` | Misspelled duplicate; ignore |
| `NDBR1.tif` | Classified, same five values. Not a continuous dNBR |
| `Fire.{High,Med,Low}.NDBR.tif` | Binary mask per severity class |
| `Fire.Perimiter.shp` | Fire perimeter, EPSG:4326, 4.80 km² |

## Traps

1. **The severity codes are not in severity order.** Decoded against the three binary class masks,
   `1` is **high**, `32` is **low** and `34` is **moderate**. A table built on the numeric order of
   the codes reports the two most severe classes the wrong way round. The manuscript derives this
   mapping in code and asserts it with `stopifnot` rather than hard-coding it.

   | Code | Class | Cells |
   |---:|---|---:|
   | 0 | outside perimeter | 3,514 |
   | 16 | inside perimeter, unclassified | 1,268 |
   | 32 | low | 2,144 |
   | 34 | moderate | 1,383 |
   | 1 | high | 535 |

2. **Code 16 is not a severity class.** It is 1,268 cells lying inside the perimeter that no class
   mask claims. It sits outside the classified footprint, so the masked beetle layer reports zero
   attack there while the independent survey reports 52.0 per cent, the highest rate of any class.
   Treat it as unobserved, not as unburned.

3. **There is no continuous dNBR anywhere on disk**, and no Landsat bands, NDMI or tasselled-cap
   rasters to recompute one from. This is why cross-agent spectral separability is out of scope; see
   `05.tasks/TASK-REQUEST-2026-08-02.md` §2.

4. **The perimeter ships as EPSG:4326** while every raster is EPSG:32611. Project it before use.
