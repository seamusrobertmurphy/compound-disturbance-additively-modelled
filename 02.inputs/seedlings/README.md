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

1. **Three seedling counts are in circulation and none of them agrees.** The UTM file holds 3,912
   points, the two reprojected files hold 3,866, and the published abstract reports 3,886 mapped
   seedlings. Establish which screening produced the published figure before quoting any of them,
   and state the choice in the Methods. Do not assume the difference is reprojection: the two file
   families carry entirely different attribute schemas, so they are different products rather than
   different projections of one product.

2. **The two families are not interchangeable.** The UTM file carries the modelling covariates
   already joined (`elevation`, `slope`, `rix`, kernel and host fields); the reprojected pair
   carries plot membership flags instead. Whichever is used, re-derive the covariates in the
   document rather than trusting a join made in 2021.

3. **The point pattern lies wholly inside the burn**, so every cell entering the point process model
   sits within the masked footprint described in `../README.md`. This is why the mask does not
   compromise question B.
