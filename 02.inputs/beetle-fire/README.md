# Beetle by fire intersection rasters

Four rasters built in 2021 for the parent study and **never used in any manuscript or script**.
They are the reason this study exists. Not stored here; read at render time from
`DARKWOODS_DATA/beetle_fire_interactive`. An identical copy sits in `beetle_stages/`.

All four are 136 by 67 at 29.558 m over the roughly 8 km² fire clip.

| File | Values | What it is |
|---|---|---|
| `mpbred_firehigh.tif` | 0: 8,132, 1: 913, 2: 67 | Red attack against high-severity burn |
| `mpbred_firelow.tif` | 0: 6,504, 1: 2,476, 2: 132 | Red attack against low-severity burn |
| `mpbred_firehi1.tif` | 0: 9,045, 1: 67 | The 67 co-occurrence cells, extracted as binary |
| `mpbred_firelo1.tif` | 0: 8,980, 1: 132 | The 132 co-occurrence cells, extracted as binary |

## Coding, verified rather than assumed

`0` is neither agent, `1` is one agent only, `2` is both. Verified by cross-tabulation: all 67
code-2 cells in `mpbred_firehigh.tif` fall in the high-severity mask and are red-attacked, and all
132 in `mpbred_firelow.tif` fall in the low-severity mask and are red-attacked. The `*1.tif` pair is
the code-2 class of its sibling, extracted.

## How the manuscript will use it

These are the empirical content of the beetle by fire product term in question B. Nothing here is
in the document yet; the interaction refit is Phase 2.

## Traps

1. **There is no moderate-severity intersection raster**, although moderate is the class that
   carries the most red attack of the three. Build it rather than treating the pair as the whole
   picture.
2. **These inherit the mask.** Every code-2 cell is red-attacked, and red attack exists only inside
   the classified burn. A cell coded `1` may be burned-without-beetle or beetle-without-burn, and
   outside the classified footprint the second of those cannot occur by construction. Do not read
   the `1` class as a symmetric single-agent category.
3. **The grid is 136 by 67**, one row and one column larger than the beetle rasters and two rows
   larger than the severity rasters. See `../README.md` trap 4.
