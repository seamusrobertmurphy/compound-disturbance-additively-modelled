# Compound disturbance synthesis

On 20 September 2026 the sixteen studies of linked and compound disturbance held in `Github/library-science` were read in full and set against the findings of this manuscript as it stood in the draft of 3 September 2026. The reading rests on the source notes in `library-science/sources/`, in which 273 quotations were checked by script against the page text of each PDF, and on the topic page `library-science/topics/disturbance/linked-and-compound-disturbance.md`, which carries the full account with page numbers. Citation keys below are the library's.

The note first restates the two findings, then sets each against the studies that tested the same question, then takes the vocabulary, the methods and the gaps in turn, and closes with what the manuscript does not yet cite.

## This study's findings

1. Prior grey-stage attack did not change the probability of high-severity burning in the Mt Midgeley fire of 2015 (log-odds 0.043, block bootstrap interval spanning zero at every block size), and the count of attack years showed no hump-shaped effect.
2. Beetle by fire product terms in the parent study's point process model of seedlings were decisive under the Poisson likelihood (likelihood ratio test, p < 0.001) and absent once the clustering of seedlings was respected, with identical coefficients, intervals 2.3 to 5.9 times wider, none of sixteen product-term intervals excluding zero, and a cluster-robust sandwich estimator in agreement.

## Linked effect compared

Six studies asked whether a bark beetle outbreak changed the fire that followed, and none found a general amplification in the grey stage, which is the stage Darkwoods was in when it burned, four years after the grey-stage record closed in 2011.

| Study | Evidence | Finding |
| --- | --- | --- |
| `harvey2014recent` | 105 plots, six fires of 2011, lodgepole pine, US Northern Rockies | Unrelated under moderate burning conditions. In grey-stage stands under extreme conditions, four of eight severity measures rose with outbreak severity (p. 15121) |
| `talucci2019dead` | 63 plots, three fires of 2012 to 2014, central British Columbia, about a decade after the outbreak | No effect on six of seven fire effects, deep charring the exception |
| `liang2016forest` | Landsat, Southern Rockies, 1999 to 2011 | Severity unrelated to prior outbreak severity (p. 43) |
| `hart2015area` | 546 large fires across the western United States | Area burned unaffected by infestation (p. 4377) |
| `simard2011mountain` | Fire simulated on 35 stands, Greater Yellowstone | A dampening. The wind needed for active crown fire rose from 39 km/h undisturbed to 71 km/h in the grey stage (p. 15) |
| `sieg2017fires` | 21 physics-based simulations, ponderosa pine | Grey stage mostly antagonistic, neutral at high wind (p. 14) |

The manuscript's null agrees with all six. The comparison that qualifies it is Harvey et al. (2014), where the beetle signal appeared only under extreme burning conditions, because a single fire at Darkwoods gives no contrast in weather and the log-odds of 0.043 is an average over whatever conditions each cell burned under. Simard et al. (2011, p. 21) found the opposite dependence, an effect only under "certain intermediate weather conditions", and Jenkins et al. (2012, p. 29) judged that study's crown fire model inappropriately applied to beetle-killed canopies, so the simulation evidence is contested in a way the field evidence is not. The hump-shaped relation the manuscript tests for comes from the Talucci (2019) thesis, whose published form, Talucci et al. (2022) in *Environmental Research Letters*, the library does not yet hold.

## Compound effect compared

Seven studies asked whether the pair changed what came after, and they split by what was measured.

| Study | Response | Finding |
| --- | --- | --- |
| `harvey2014recent` | Lodgepole seedling density, one year after fire | Unrelated to outbreak severity (Spearman's rs = -0.16, df = 58, P = 0.23, Table 1, p. 15122) |
| `talucci2019drivers` | Lodgepole seedling counts, 83 plots | Prefire beetle mortality "did not play a role" (p. 6). Fire severity and cone abundance did |
| `stevensrumann2015bark` | Seedling density and fuels, 180 plots, dry mixed conifer | "no evidence that a beetle and wildfire interaction affected seedling densities" (p. 1) |
| `carlson2017` | Landsat NDVI two years after fire, spruce beetle, Colorado | Lower cover with more severe outbreak, coefficient 0.40 red stage and 0.25 grey stage (Table 6, p. 16) |
| `liang2016forest` | Ratio of regrowth area to disturbed area | 64.9 per cent after beetle then fire against 57.9 per cent after fire alone (p. 41), no test or interval |
| `buma2011disturbance` | Conifer seedlings after blowdown then fire, paired plots at 50 sites | Density fell with blowdown severity (Spearman's rho = -0.30, p. 6) |
| `talucci2020added` | Pyrogenic carbon on three beetle-killed and three fire-killed snags | Higher on beetle-killed snags (P = 0.003, p. 6) |

Every study that counted tree seedlings after beetle then fire found no compound effect, in three regions and two forest types, and the manuscript's product terms sit with them. The effects that were found came from a spectral index of cover, which Carlson et al. (2017, p. 17) themselves warned "is not necessarily an indicator of overstory regeneration", from a ratio of mapped areas without uncertainty, or from a different first disturbance that left heavy fuel on the ground. Carlson et al. (2017) remains the study a referee is most likely to raise, since it used Landsat, modelled spatial dependence, and found an effect.

Two of the nulls carry a qualification that bears on Darkwoods. Harvey et al. (2014, p. 15123) allowed that compound effects "may be possible following high-severity fires in stands where most lodgepole pine trees are dead at the time of fire", which is the case the parent study's abstract describes, and the product term of grey-stage attack with high severity is the test of it. Stevens-Rumann et al. (2015, p. 11) found no seedlings on 95 per cent of burned sites and wrote that a further reduction "may not be visible". The manuscript's position, that three four-hectare plots cannot support a product term either way, is the same caution stated for a point pattern.

## Additive is named

The field has a word for the outcome the parent study modelled. Sieg et al. (2017, p. 4) classed a pair of disturbances as linked or neutral, and defined the second as "neutral (also called additive), as mass loss of the combined disturbances is similar to the mass loss of the disturbances occurring independently". Paine et al. (1998, p. 537) defined the alternative as an effect that "is multiplicative, not additive", and Buma and Wessman (2011, p. 2) glossed ecological surprises as "non-additive effects". A beetle by fire product term is therefore the literal test of Paine's claim, and an additive model is the neutral case of Sieg's scheme, a named result and not the absence of one. Stevens-Rumann et al. (2015, p. 1) used "non-additive" in their abstract while reporting no interaction, the one loose use in the set.

## Methods compared

Few of the sixteen fitted a product term between the two disturbances. Talucci et al. (2019) did, in a negative binomial model of plot counts, one model per factor "due to the relatively small sample size" (p. 4), with all terms fixed (p. 5). Harvey et al. (2014) and Talucci and Krawchuk (2019) fitted the first disturbance by weather, not by the second disturbance. Stevens-Rumann et al. (2015) and Liang et al. (2016) contrasted classes. Harvey et al. (2014, p. 15125) tested the compound effect by rank correlation because they "were unable to fit these data to general or generalized linear models". Sieg et al. (2017, pp. 9 to 10) alone computed an explicit additive expectation and indexed the departure from it.

Only two carried spatial dependence into the inference, and both are precedents for this manuscript. Carlson et al. (2017, p. 9) wrote that "spatial dependence in either the response or the explanatory variables can violate assumptions of observation independence and inflate parameter values", found autocorrelation to about 500 m, and fitted a spatial error model. Sieg et al. (2017, p. 9) used "a spatially blocked bootstrapping approach following Lahiri (2003)" with 10,000 samples. Simard et al. (2011, p. 7), Harvey et al. (2014, p. 15124) and Buma and Wessman (2011, p. 3) handled it by spacing plots 350 m, 400 m and 500 m apart, and Buma and Wessman named the problem, "sampling within disturbances necessarily invokes some spatial autocorrelation and pseudoreplication". Johnstone et al. (2010, p. 1285) represented it by latitude and a factor for burn, Talucci and Krawchuk (2019, p. 8) gave plots a random effect in their tree-level models only, and the remaining empirical studies did not mention it.

None of the fifteen other than the parent study modelled mapped individual seedlings, and none fitted a product term between two disturbances to such data, so none met the case this manuscript reports, in which clustered points counted as independent observations made the term significant. That statement covers these studies only. A claim that the literature contains no such case needs the scoping review the protocol prescribes for an absence.

## Not yet cited

The draft of 3 September 2026 cites the Talucci (2019) thesis fourteen times and none of its three published papers, `talucci2019dead`, `talucci2019drivers` and `talucci2020added`, and a referee can open a journal article more easily than a thesis. It does not cite `carlson2017`, `sieg2017fires`, `stevensrumann2015bark`, `buma2011disturbance` or `paine1998compounded`, and it cites no source for the block bootstrap, for which the library now holds Künsch (1989), unverified because the file is a scan, and for which Sieg et al. (2017) cite Lahiri (2003), not held. Stevens-Rumann et al. (2016), which the draft cites, and Talucci et al. (2022) are still to be sourced.
