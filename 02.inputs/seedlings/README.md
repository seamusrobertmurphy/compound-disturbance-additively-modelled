# Seedling point pattern

The response for question B. Field-mapped conifer seedlings across three 4 ha plots inside the 2015
burn, collected for the parent study [@murphy2026]. Not stored here; read at render time from
`DARKWOODS_DATA/seedlings`.

| File | Points | CRS | Fields |
|---|---:|---|---|
| `Seedlings.shp` | 3,912 | EPSG:32611 | `FID_1`, `seedlings_`, `seedlings1`, `point_lp_h`, `kernel_lp_`, `elevation`, `slope`, `rix` |
| `Seedlings_EPSG3857.shp` | 3,866 | EPSG:3857 | `data_point`, `x`, `y`, `geodetic_d`, `plot123`, `plot1`, `plot2`, `plot3` |
| `Seedlings_EPSG4326.shp` | 3,866 | EPSG:4326 | as above |

## How the manuscript will use it

As the point pattern in the inhomogeneous Cox process refit that tests the beetle by fire product
term. Nothing here is in the document yet; this is Phase 2.

## Traps

1. **Three seedling counts are in circulation and two of them are now explained.** The parent
   study's own Table S2 reconciliation, at
   `5.Submissions/2026-06-19/TableS2_reconciliation.csv`, analyses **3,912** points pooled, and its
   per-plot rows sum to exactly that (1,037 + 1,268 + 1,607). Its per-species rows sum to **3,866**,
   which is the count in the two reprojected files, so 3,866 is the species-assigned subset rather
   than a different survey. The published abstract's **3,886** matches neither and is unexplained.
   Use 3,912 as the analysis frame and 3,866 where species is required, state which in the Methods,
   and query the abstract figure with the author before repeating it.

   Do not assume the file families differ only by projection: they carry entirely different
   attribute schemas.

2. **The two families are not interchangeable.** The UTM file carries the modelling covariates
   already joined (`elevation`, `slope`, `rix`, kernel and host fields); the reprojected pair
   carries plot membership flags instead. Whichever is used, re-derive the covariates in the
   document rather than trusting a join made in 2021.

3. **The point pattern lies wholly inside the burn**, so every cell entering the point process model
   sits within the clipped footprint described in `../README.md` and is equally affected by it. This
   is why the clip does not compromise question B.
