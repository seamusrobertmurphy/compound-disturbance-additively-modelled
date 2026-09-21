<!-- Redraft of the Results, 20 September 2026, for approval. Prose only. Every code chunk stays where
it is and is marked by its label. Every inline R expression is copied by script from the draft of
3 September 2026 and none was retyped. EDIT marks a reworded sentence, MOVED marks literature that goes
to the Discussion, CUT marks a deletion. The guide papers keep other studies out of their Results, and
Harvey et al. (2014) and Talucci et al. (2019) report each question as estimate, test, then breakdown,
which is the order kept here. Unmarked text is unchanged. -->

# Results

## Burn severity {#sec-severity}

### Analysis frame {#sec-frame}

[chunk frame]

The frame was every observed cell inside the fire perimeter, `r format(N_FR, big.mark = ",")` cells, of which `r format(N_HIGH, big.mark = ",")` burned at high severity and `r format(N_HIT, big.mark = ",")` had prior grey-stage attack, with lodgepole pine present on `r round(100 * mean(FR$host))` per cent of them. High severity occurred on `r sprintf("%.1f", P_HIGH_ATT)` per cent of attacked cells and `r sprintf("%.1f", P_HIGH_UN)` per cent of unattacked cells.

### Covariate collinearity {#sec-collinear}

[chunk tbl-host]

Host and elevation moved together (@tbl-host), in that lodgepole percentage correlated with elevation at r = `r sprintf("%.2f", R_PL_EL)` across the frame and the binary host indicator the model fitted at r = `r sprintf("%.2f", R_HOST_EL)`, a variance inflation factor of about `r sprintf("%.2f", VIF_HOST)`, too low to exclude either term. EDIT The limit on the model was the number of independent observations and not the correlation between its predictors, because spatial dependence meant the `r format(N_FR, big.mark = ",")` cells were far from independent, and the block bootstrap of @sec-blocks resampled the `r K_500` blocks that a `r BLOCK_M` m grid gave.

### Severity coefficients {#sec-conditioned}

[chunk tbl-conditioned]

Prior attack did not change the probability of high-severity burning in any of the three logistic regressions. The crude log-odds of high severity for attacked against unattacked cells were `r sprintf("%.3f", SEV_CRUDE)` (95 per cent block bootstrap interval `r ci_of(M_CRUDE, "y")`) and `r sprintf("%.3f", SEV_ADJ)` (`r ci_of(M_ADJ, "y")`) with host presence and elevation in the model, both spanning zero (@tbl-conditioned). The hump-shaped form did not recur. With the attack-year count in place of the binary attack, the linear term was `r sprintf("%.3f", gv(M_QUAD, "cnt"))` (`r ci_of(M_QUAD, "cnt")`) and the squared term `r sprintf("%.3f", gv(M_QUAD, "I(cnt^2)"))` (`r ci_of(M_QUAD, "I(cnt^2)")`), both spanning zero. Lodgepole presence had the largest coefficient in the frame, at `r sprintf("%.3f", gv(M_ADJ, "host"))` (`r ci_of(M_ADJ, "host")`), so cells with lodgepole were less likely to burn at high severity, with an interval that `r if (clears(M_ADJ$Lower[M_ADJ$Term == "host"], M_ADJ$Upper[M_ADJ$Term == "host"])) "excluded zero" else "spanned zero"`, and elevation was `r sprintf("%.3f", gv(M_ADJ, "ec"))` (`r ci_of(M_ADJ, "ec")`) in log-odds per 100 m.

### Block bootstrap {#sec-blocks}

[chunk moran]

Moran's I on the response was `r sprintf("%.2f", MORAN)` at queen adjacency, EDIT so standard errors that assumed independent cells did not apply, and a block bootstrap needed blocks large enough to contain the dependence and numerous enough to resample.

[chunk fig-blocks]

[chunk tbl-blocks]

[chunk tbl-correlogram]

[chunk sweep-summary]

Residual dependence in the conditioned model fell from `r CORR$"Residual correlation"[1]` within 100 m to `r CORR$"Residual correlation"[4]` by 500 m (@tbl-correlogram, @fig-correlogram left), so a 500 m block contained most of it. EDIT Over a burn of about 4.0 by 2.0 km those two requirements conflicted, because the burn gave `r SWEEP$Blocks[SWEEP$"Block side (m)" == BLOCK_M]` blocks at `r BLOCK_M` m and only `r SWEEP$Blocks[which.max(SWEEP$"Block side (m)")]` at `r max(SWEEP$"Block side (m)")` m, where the roughly 1 km blocks of the companion study would have given eight. The attack coefficient spanned zero at all `r nrow(SWEEP)` block sizes tried (@fig-blocks, @tbl-blocks), with the interval at its narrowest, `r SWEEP$Interval[which.min(SWEEP_RAW$Upper - SWEEP_RAW$Lower)]`, on `r SWEEP$Blocks[which.min(SWEEP_RAW$Upper - SWEEP_RAW$Lower)]` blocks of `r SWEEP$"Block side (m)"[which.min(SWEEP_RAW$Upper - SWEEP_RAW$Lower)]` m, EDIT so the result did not depend on the block size chosen.

## Regeneration interaction {#sec-interaction}

The seedling point pattern lay wholly inside the burn and every cell entering the model was equally masked, so the second objective was untouched by the perimeter. The published model was refitted with the beetle by fire product terms and compared against the published additive fit.

### Model specification {#sec-ppframe}

[chunk ppframe]

The seedling shapefile held `r format(N_RAW, big.mark = ",")` points, of which `r N_DROP` had a species code outside the seven-species lookup the parent study used, leaving `r format(N_SEED, big.mark = ",")`, all inside the plot windows. The fit used `r format(N_DATA, big.mark = ",")` data points against `r format(N_DUMMY, big.mark = ",")` quadrature points over `r sprintf("%.2f", WIN_HA)` ha.

### Fit reproduction {#sec-ppreproduce}

[chunk tbl-ppreproduce]

All `r nrow(REPRO)` coefficients of the additive fit agreed with the published values to four decimal places, and so did the standard errors, to within `r sprintf("%.0e", SE_MAXDIFF)` (@tbl-ppreproduce). The right-hand columns set the published standard errors beside those implied by an ordinary weighted Poisson fit to the same design matrix, and they were the same numbers, so the published uncertainty was Poisson uncertainty, and the rest of this section rested on that reproduction. Two further features of the fit mattered for what followed. The grey-stage coefficient was `r sprintf("%.4f", REPRO$Published[REPRO$Term == "MPB_G"])`, zero to three decimal places, so the parent study's corrected refit had found no grey-stage main effect, and the two fire terms were indicators for high and low severity, so they were contrasts against whatever the reference category contained.

### Covariate support {#sec-ppsupport}

[chunk tbl-ppsupport]

The reference category of the published fit was every quadrature point with neither severity indicator, `r format(REF_N, big.mark = ",")` points, of which `r format(REF_MOD, big.mark = ",")` were moderate severity and the remainder unburned or unclassified ground (@tbl-ppsupport), EDIT so each published fire coefficient compared its class with a pooled category that was `r round(100 * REF_MOD / REF_N)` per cent moderate severity, and not with unburned ground. The grey union recorded attack on `r format(GREY_Q, big.mark = ",")` of `r format(nrow(Q), big.mark = ",")` quadrature points [@murphy2026greyfix]. Red attack was confined as @sec-limits describes, appearing on `r format(RED_Q, big.mark = ",")` quadrature points and on none outside the classified severity classes.

### Product terms {#sec-ppproduct}

[chunk tbl-ppproduct]

Under the likelihood the published model was fitted with, the product terms were decisive. The fit with product terms improved on the additive fit by likelihood ratio test [χ^2^(`r LR_DF`) = `r sprintf("%.1f", LR_STAT)`, `r if (LR_P < 0.001) "p < 0.001" else sprintf("p = %.3f", LR_P)`], and `r N_PROD_SIG` of the `r LR_DF` product terms had Poisson intervals excluding zero (@tbl-ppproduct). MOVED to the Discussion, the comparison of this result with @talucci2019drivers and @harvey2014. EDIT Two features of the fit were inconsistent with a compound effect. The product terms did not share a sign, in that grey attack raised regeneration at high severity and lowered it at low severity, and the fitted signs reversed between the two beetle surfaces on the same severity class. Adding them also moved the main effects sharply, taking the high-severity term from `r sprintf("%.3f", B_ADD[["Fire_H"]])` to `r sprintf("%.3f", B_PROD[["Fire_H"]])` CUT, a general claim about product terms that no source supported.

### Spatial inference {#sec-pphonest}

Estimating the trend of a log-Gaussian Cox process by the Berman-Turner device was legitimate, because @baddeley2000 and @waagepetersen2007 showed the Poisson score to be a composite likelihood that returned consistent trend estimates whether or not the process was Poisson. EDIT That result did not extend to the variance the fit reported, because the standard errors were those of the Poisson model the fit was arithmetically equivalent to, which assumed seedlings placed independently given the covariates. The estimates therefore came from the Cox specification and the uncertainty from the Poisson one, and only the second was affected.

MOVED to the Discussion, the quotations from @malone2018 and @ziegler2017 on why post-fire regeneration is clustered, since they report other studies and not a result of this one. EDIT The seedlings were clustered. The parent study tested the observed pattern against 999 Monte Carlo simulations of Ripley's inhomogeneous K under a null of non-constant intensity and reported significant clustering for every species examined [@murphy2026], and the residuals of the refit showed the same dependence.

[chunk fig-correlogram]

[chunk tbl-ppcorr]

Residual dependence inside the plots ran at `r PCORR$"Residual correlation"[1]` within 25 m and was still `r PCORR$"Residual correlation"[3]` between 50 and 75 m, crossing zero at around 100 m (@tbl-ppcorr, @fig-correlogram right). A block that contained it therefore had to be at least 75 to 100 m on a side, and a 200 m plot gave few of those, EDIT the same conflict @sec-blocks met across the burn, at about one tenth of the block side.

[chunk fig-interaction]

[chunk tbl-ppblocks]

[chunk tbl-sandwich]

[chunk pp-verdict]

None of the `r nrow(PROD_ROWS)` product-term intervals excluded zero across the four block sizes (@fig-interaction, @tbl-ppblocks). The estimates did not move, because the estimates were not what the Poisson likelihood got wrong, and the intervals widened by a factor of `r sprintf("%.1f", WIDEN$lo)` to `r sprintf("%.1f", WIDEN$hi)` against the naive Poisson intervals of @tbl-ppproduct, EDIT and that widening alone separated a decisive likelihood ratio test from `r nrow(PROD_ROWS)` product-term intervals that all spanned zero. The cluster-robust sandwich agreed on both counts (@tbl-sandwich), inflating the standard errors by a factor of `r sprintf("%.1f", SAND_RANGE[1])` to `r sprintf("%.1f", SAND_RANGE[2])`, in the same range as the bootstrap widening, and of the `r SAND_N_PROD` product-term intervals it implied across the block sizes the correlogram supported, `r SAND_PROD_CLEAR` excluded zero. The two estimators shared the assumption that blocks were independent of one another and differed in everything else, in that the bootstrap resampled blocks and the sandwich summed scores within them.

The widening factor was computed only over the `r WIDEN$n` of `r nrow(PPB_RAW)` term-by-block combinations that every one of the `r format(B_BOOT, big.mark = ",")` draws could estimate. The four product cells rested on `r min(PROD_CELLS)` to `r max(PROD_CELLS)` quadrature points each, so a resample that missed the blocks holding one of them left that term unidentified, and `r nrow(DEGEN)` combinations were affected, every one involving red attack or high severity, the worst losing `r B_BOOT - min(PPB_RAW$Usable)` draws of `r format(B_BOOT, big.mark = ",")`. The percentile for such a term was taken over whichever resamples happened to contain its cells, which were the resamples that overweighted them, and that inflated the interval for a reason unconnected with spatial dependence; left in, those combinations put the top of the widening range at `r sprintf("%.1f", max((PPB_RAW$Upper - PPB_RAW$Lower) / (2 * 1.96 * SE_PROD[PPB_RAW$Term])))` rather than `r sprintf("%.1f", WIDEN$hi)`. The count of usable draws is reported in @tbl-ppblocks for every cell, and none of it changed the verdict, because the affected intervals were already the widest and every product term spanned zero on the identified combinations alone.

The only terms among those shown whose intervals excluded zero at every block size were `r MAIN_WORDS`, neither of them a product term, so the regeneration data supported main effects for red-stage beetle attack and low burn severity and supported no statement about the two causes acting together. Three plots totalling `r sprintf("%.1f", WIN_HA)` ha gave `r PP_OK_TXT` across the block sizes the residual range permitted, and a product term asked those blocks to resolve a difference of differences across four severity-by-attack combinations. The published likelihood answered the question confidently because it counted `r format(N_DATA, big.mark = ",")` seedlings as `r format(N_DATA, big.mark = ",")` independent pieces of evidence.
