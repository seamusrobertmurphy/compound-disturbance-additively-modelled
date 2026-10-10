# Materials and methods

<!-- Redraft of 20 September 2026 for approval. Prose only. Every code chunk stays where it is, and
each is marked below by its label. Every inline R expression is copied unchanged from the draft of
3 September 2026. Sentences marked NEW are additions, everything else is the existing text, kept or
tightened. The subsection order follows the parent study and Talucci et al. (2019) in the same
journal, which run study area, data, then statistical analysis. -->

## Study area {#sec-area}

The study was set in the Darkwoods Conservation Area, in the southern Selkirk Mountains of southeastern British Columbia, where the Mt Midgeley wildfire of August 2015 burned 479.77 ha in a mixed-severity mosaic [@murphy2026]. A mountain pine beetle outbreak had affected the property through the decade to 2014, with intervals from attack to fire of one to eleven years and a median of seven [@murphy2026]. NEW The attack surface the models used closed in `r max(ANN_YEARS)`, so the attacked stands burned `r 2015L - max(ANN_YEARS)` to `r 2015L - min(ANN_YEARS)` years after attack, within the grey stage as @hart2015 defined it, "any pixel recording infestation within 3 to 15 y before burning", and as @harvey2014 sampled it. The outbreak preceded the fire, and for mountain pine beetle the reverse sequence is weak, because @mchugh2003 found the species "not attracted to fire-damaged trees" where other bark beetles colonised them, and @liang2016 found post-fire beetle severity "lowest in areas with higher burn severity, due to the limited availability of live host trees", so the linked effect tested here ran from beetle to fire.

## Attack chronology {#sec-dating}

Prior disturbance had been dated by several means in the studies reviewed, in that @kulakowski2006 dated a nineteenth-century outbreak from growth releases in surviving trees, @meyer2016 reconstructed pre-attack structure by returning recently dead trees to the live tally, and @estabrook2025 showed how a forest inventory's remeasurement interval degraded its record of pre-fire condition. Here attack was dated from the annual Landsat classifications, `r length(ANN_ALL)` files in all, with the attack year of a cell taken as the first file that recorded it (@tbl-annual).

[chunk tbl-annual]

@wulder2006red found red-attack foliage detectable for roughly one to three years after the attack that produced it, so a first detection dated the change in crown colour within a window and not to a year. The series also held fewer usable years than files, in that there was no file for `r paste(YR_GAP, collapse = " or ")`, the files for `r paste(YR_EMPTY[YR_EMPTY > max(ANN_YEARS)], collapse = " and ")` used a different classification legend and recorded the red-attack code in no cell, and two files inside the window, for `r paste(YR_EMPTY[YR_EMPTY <= max(ANN_YEARS)], collapse = " and ")`, were likewise empty of it, so the grey-stage union rested on `r length(YR_LIVE)` annual observations across a `r max(ANN_YEARS) - min(ANN_YEARS) + 1`-year window that closed in `r max(ANN_YEARS)`. Two attack surfaces were used, the grey-stage union, which recorded whether a cell was attacked at any time from `r min(ANN_YEARS)` to `r max(ANN_YEARS)`, and the attack-year count, which recorded in how many of those annual files the cell carried the red-attack code, from zero to `r length(YR_LIVE)` and served as the graded measure of outbreak severity that @talucci2019thesis modelled as a continuous spectral change. NEW Field studies measured outbreak severity as the basal area or the proportion of trees the beetle killed [@harvey2014; @talucci2019dead], a quantity no surface here recorded, so the count measured how long a cell stayed in red attack and not how much of its stand died.

## Classified surfaces {#sec-local}

[chunk tbl-footprints]

The fire perimeter enclosed `r round(PERIM_KM2, 2)` km^2^, the beetle red-stage raster spanned a rectangle of `r RECT_KM2` km^2^ around it, and the terrain grid covered `r round(GRID_KM2, 0)` km^2^ of the same landscape (@tbl-footprints).

## Severity codes {#sec-decode}

Burn severity here meant the three classes of the parent study's classified differenced Normalised Burn Ratio raster, low, moderate and high, in the sense @lentile2006 gave the term, the degree of ecosystem change the fire caused as measured after it, distinct from fire intensity and from immediate fire severity. @lentile2006 cautioned that class thresholds transfer poorly between environments and that at 30 m the moderate class is the most mixed, and the classes were kept as the parent study defined them. NEW The field studies this one is compared with measured fire severity on the ground, as char height, bole scorch and tree mortality in plots [@harvey2014; @talucci2019dead], and @carlson2017 removed the difference by analysing high-severity cells alone, so a satellite class stood here for what those studies measured directly. The raster used integer codes that were not in severity order, so the order was established from the three binary class masks and not assumed (@tbl-decode).

[chunk tbl-decode]

Code 1 was high severity, code 34 moderate and code 32 low. Code 16 was the class that no severity mask claimed, `r format(DECODE$Cells[DECODE$Class == "Inside perimeter, unclassified"], big.mark = ",")` cells lying inside the fire perimeter but assigned to none of high, moderate or low, which corresponded to what @talucci2019thesis called "MPB-affected fire refugia (Meddens et al. 2018), locations that experience insect outbreak but did not burn within a given fire event" where they were attacked.

## Seedling plots {#sec-plots}

NEW The regeneration data were the parent study's, for which in summer 2020, five growing seasons after the fire, every conifer seedling in three four-hectare plots of 200 m by 200 m inside the fire perimeter was mapped as a point and identified to species [@murphy2026], and the counts that entered the refit are given with the model (@sec-ppframe). The plots were "purposively distributed across gradients of fire severity and beetle-outbreak history, and each was positioned within 200 m of residual forest" [@murphy2026]. A stem map differed in kind from the plot counts of the field studies, since @harvey2014 counted seedlings in 70 plots of 0.07 ha, @talucci2019drivers in 83 plots and @stevensrumann2015 in 180 plots of 0.04 ha, each plot giving one density, whereas three mapped plots gave thousands of locations and three samples of the landscape. Under that design the product terms were identified by variation in attack and severity within and among three purposively placed plots, and no result from them was extended to the burn as a whole.

## Aerial survey {#sec-aos}

The provincial Aerial Overview Survey was the operational record of forest health in British Columbia, in which observers sketch-mapped damage each year from fixed-wing aircraft and labelled each polygon by year, cause, severity class and host species [@bcaos2026]. It was coarse and observer-based, and its errors were positional and perceptual and not spectral, so they were uncorrelated with the errors of the Landsat classification.

[chunk aos]

Over the terrain grid the survey held `r format(AOS_ALL, big.mark = ",")` damage polygons of all causes and years, of which `r AOS_N` were mountain pine beetle within the `r min(OUTBREAK)` to `r max(OUTBREAK)` outbreak window.

## Spatial coverage {#sec-maps}

Everything the study analysed lay inside one small burn, and @fig-location shows what that meant at three nested scales. The regional panel shows the international border because the provincial survey stopped there, and so did any comparison drawn from it.

[chunk fig-location]

The terrain grid covered `r round(GRID_KM2, 0)` km^2^, every disturbance raster shared a footprint of `r RECT_KM2` km^2^, and the fire perimeter inside it enclosed `r round(PERIM_KM2, 2)` km^2^.

<!-- CUT, proposed. The sentence giving the three representative fractions and the panel width of
`r sprintf("%.2f", PANEL_IN)` inches, and the sentence naming the projections, both already in the
figure caption. A reader of the Methods does not need how the scale was measured. -->

## Data limits {#sec-limits}

Beetle mortality is under-detected in Landsat time series even where it is mapped, because @rodman2021 found that a standard change-detection algorithm "more accurately detected wildfire than spruce beetle-induced tree mortality, and both mortality agents were more easily detected when they occurred at high severity", and predicted about forty per cent less affected area than alternative methods, so an absence of attack in a Landsat product was weak evidence of absence and every local surface was checked against the survey. The check found that the annual rasters of `r min(ANN_YEARS)` to `r max(ANN_YEARS)` held data on only a fraction of the cells outside the fire perimeter and no data on the rest, and every beetle surface in the study descended from those files and inherited that boundary (@tbl-perimeter).

[chunk tbl-perimeter]

The annual rasters held data on `r round(PCT_OBS_OUT, 1)` per cent of the `r format(CELLS_OUT, big.mark = ",")` cells lying outside the fire perimeter, all `r length(ANN_ALL)` files had an identical no-data count of `r format(ND_COUNTS[1], big.mark = ",")` cells, `r format(ND_OUT[1], big.mark = ",")` of them outside the perimeter, and the boundary the no-data traced was the fire perimeter, so the annual series had been clipped to the perimeter before classification. The corrected grey union placed `r GREY_OUT` of its `r sum(GREY_HIT)` cells outside the perimeter and the published red-stage surface `r RED_OUT` of its `r N_RED`. The two surfaces also stopped in different places inside the perimeter (@tbl-nested).

[chunk tbl-nested]

Inside the perimeter but outside the classified severity footprint, the annual rasters were `r NEST$"Annual data (%)"[2]` per cent observed, the grey union recorded attack on `r NEST$"Grey attack (%)"[2]` per cent of cells and the red-stage surface on `r NEST$"Red attack (%)"[2]` per cent, because the red-stage surface stopped at the classified severity footprint, standing in for a layer, `mpb_red_na.tif`, that is absent from the parent repository [@murphy2026greyfix]. The grey union, the denser surface and the one observed throughout the perimeter, was therefore the attack surface used in the models.

[chunk tbl-crosscheck]

The survey recorded `r sprintf("%.1f", OUTROW$"Survey (%)")` per cent of the ground outside the perimeter as attacked, a rate no lower than any burned class and higher than two of the three, while the annual rasters observed only `r OUTROW$Observed` of the `r format(OUTROW$Cells, big.mark = ",")` cells there (@tbl-crosscheck, shaded row). A contingency table of red attack against severity built over every cell of the published surface would have reported attack on `r sprintf("%.1f", RED_ALL_OUT)` per cent of cells outside the perimeter against `r sprintf("%.1f", RED_ALL_MOD)` per cent at moderate severity and would have measured the coverage of the rasters and not the attack (@fig-mask). For the design this meant that a comparison of attacked stands that burned against attacked stands that did not, the comparison @mcintire2006 made across disturbance boundaries tens of metres wide and @talucci2019drivers made between burned plots and fire refugia, was not available, and the fire perimeter used as a hard clip discarded the boundary zone in which such a comparison is made. Every comparison in this study was therefore made inside the perimeter, where the three severity classes were observed at better than `r floor(min(BURNED$"Observed (%)"))` per cent and the clip could not generate differences among them.

[chunk fig-mask]

[chunk withinburn]

## Expected effects {#sec-expected}

NEW Each term the two models entered was given its expected direction from the studies reviewed above before the models were fitted (@tbl-expected). The expectation for every beetle term was no effect, and the product terms had a stated alternative, the negative effect of grey-stage attack under high severity that @harvey2014 left open and the feedback of @krawchuk2020 predicts.

| Model | Term | Expected direction | Reasoning and source |
| --- | --- | --- | --- |
| Severity | Grey-stage attack | None, or negative | Severity unrelated to outbreak severity outside extreme weather [@harvey2014], no effect on six of seven fire effects [@talucci2019dead], a dampening of crown fire in simulation [@simard2011; @sieg2017] |
| Severity | Attack-year count and its square | Positive then negative | High severity most probable at intermediate outbreak severity [@talucci2019thesis] |
| Severity | Lodgepole pine presence | Not set | Attack occurs only where the host grows, so host cover was entered to separate the two, as @hart2015 computed expected area burned within host forest |
| Severity | Elevation | Not set | Weather and topography were the primary drivers of severity [@harvey2014], and topography entered every comparable model [@carlson2017; @talucci2019thesis] |
| Regeneration | Seed source distance | Negative | Negative in the published fit [@murphy2026], and a review of post-fire regeneration found seedling densities "attributed to distances to a seed source" before any other driver [@stevensrumann2019] |
| Regeneration | Aspect, ruggedness, wind | As published | Positive in the published fit [@murphy2026], entered unchanged so that the refit differed from it only in the product terms |
| Regeneration | High and low severity | Positive | Positive in the published fit [@murphy2026], and recruitment after crown fire "over six times greater compared to fire refugia" in serotinous lodgepole pine [@talucci2019drivers] |
| Regeneration | Red-stage and grey-stage attack | None | Seedling density unrelated to outbreak severity [@harvey2014; @talucci2019drivers; @stevensrumann2015] |
| Regeneration | Attack by severity products | None, the neutral case | An additive outcome is the neutral linkage of @sieg2017, and a compounded effect is "multiplicative, not additive" [@paine1998]. The alternative was a negative product of grey-stage attack with high severity [@harvey2014; @krawchuk2020] |

: Terms entered in the severity model and the regeneration model, with the direction each was expected to take and the studies the expectation rested on. {#tbl-expected}

## Statistical analysis {#sec-stats}

The first objective followed the form of the Landsat analysis of @talucci2019thesis, who modelled the probability of high burn severity on outbreak severity, weather and terrain. Here the response was whether an observed cell inside the perimeter burned at high severity, and the predictors were prior grey-stage attack, lodgepole presence and centred elevation, in three specifications, attack alone, attack with host and elevation, and the attack-year count with its square in place of the binary attack, the last being the test of the hump-shaped form. NEW @harvey2014 and @talucci2019dead each fitted outbreak severity in a product with burning conditions, because the beetle signal they found depended on fire weather. A single fire gave no contrast in fire weather, so the models here could not separate fuels from weather as theirs did, the attack coefficient was an average over whatever conditions each cell burned under, and that limit is taken up in the Discussion.

NEW The comparison studies met spatial dependence in three ways, in that most spaced their plots, 350 m apart from a semivariogram in @simard2011 and at least 400 m in @harvey2014, @carlson2017 found autocorrelation to about 500 m by variogram and fitted a spatial error model, and @sieg2017 compared simulations by "a spatially blocked bootstrapping approach following Lahiri (2003)". Every cell inside the perimeter was used here, so spacing was not available, and the block bootstrap was adopted because it changes the intervals and leaves the published estimator untouched, which a spatial error model would not. The intervals were spatial block bootstrap percentile intervals, following the block resampling of the companion refugia analysis of this landscape [@murphy2026refugia], with `r format(B_BOOT, big.mark = ",")` replicates over square blocks of `r BLOCK_M` m and a sweep across `r paste(BLOCK_SWEEP, collapse = ", ")` m, the block sizes set from the measured range of the dependence, which @carlson2017 took from a variogram and this study took from a Pearson residual correlogram of the conditioned model and Moran's I on the response at queen adjacency.

The second objective was addressed by reproducing the published point process fit and then extending it. The parent study estimated an inhomogeneous point process trend by the Berman-Turner device, in which the seedlings entered as data points, a regular grid of dummy points held the quadrature weights and the trend was estimated by weighted Poisson regression on the pooled set [@berman1992; @baddeley2000], the same construction @ziegler2017 and @malone2018 used for post-fire regeneration. NEW A point process model was the parent study's answer to a problem the plot studies had met, in that @harvey2014 "were unable to fit these data to general or generalized linear models" and tested the compound effect by rank correlation. That specification was reproduced exactly, including its `r PP_DX` m quadrature spacing, its eight covariates and its sentinel handling, and the reproduction was checked against the published coefficient table and its standard errors. Four beetle by fire product terms were then added, grey and red attack each crossed with high and low severity, the form @talucci2019drivers fitted to plot counts, and the two fits were compared by a likelihood ratio test under the published Poisson likelihood. Because @waagepetersen2007 showed that the Poisson score was a composite likelihood whose trend estimates were consistent for a clustered process but whose variance was not, the same fit was given intervals by a spatial block bootstrap of `r format(B_BOOT, big.mark = ",")` replicates over `r paste(PP_SWEEP, collapse = ", ")` m blocks across the quadrature grid, with the block sizes set by a residual correlogram inside the plots, and by a cluster-robust sandwich estimator [@liang1986] clustered on the same blocks.

All analyses were run in R `r paste(R.version$major, R.version$minor, sep = ".")` with terra `r packageVersion("terra")` and sf `r packageVersion("sf")`. Every number, table and figure in this paper was computed from the source rasters when the document was rendered, each table was written to disk from the same object that rendered it, and every agreement the text reports between two independently computed quantities was asserted in the source document so that a disagreement stopped the render.
