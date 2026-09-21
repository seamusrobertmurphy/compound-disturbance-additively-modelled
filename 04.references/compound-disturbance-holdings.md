# Compound disturbance holdings

On 20 September 2026 the central store at `Github/library-science` was scanned for every study bearing on compound disturbance, as the first reading for the follow-up paper to Murphy et al. (2026). The store held 815 catalogued records and 836 PDF files on that date, of which 45 had reading notes. The scan compiled 31 studies, 9 of them central to the subject, and found that seven works the manuscript's bibliography already cites were not held in the store at all.

This note is a scan of what the store holds. It is not the frozen protocol review in `library-science/protocols/literature-review.md`, which searches Semantic Scholar as well and takes its terms only from the manuscript's title and keywords. The sections below give the search, the vocabulary the field uses, the studies grouped by the question each one answers, the works not held, and the state of the store's records.

## Search method

Two passes were run. The first matched the catalogue title, the stored abstract and the first three pages of all 814 staged records against fourteen phrases for the concept, among them compound disturbance, linked disturbance, disturbance interaction, multiple disturbance, short-interval disturbance and reburn, and separately flagged any record naming fire together with a second cause in its title or abstract. It returned 31 records, 8 on the concept phrases. The second pass extracted the full text of all 836 PDFs with `pdftotext` and counted five phrase families. It returned 43 files with at least one match and none that failed to open. The manifest lists 26 PDFs as thin or scanned and 2 as unreadable, so a study held only as a scanned image could have been missed.

Every quotation below was checked on the day against the text of its PDF by a normalised string match, with one invented sentence as a negative control, which failed as it should. Page numbers are PDF pages.

## Field vocabulary

The field separates two relationships between successive disturbances, and the separation maps onto the manuscript's two objectives. Talucci (2019, thesis, p. 16) defined them. "Short-interval disturbances may create linked effects where the first event influences the frequency or severity of the second event (Simard et al. 2011). Short-interval disturbances can also create compound effects in which the first event alters the ecological outcome of the second event, sensu Paine et al. (1998)." Sieg et al. (2017, p. 3) added a sign to the linked effect, calling it antagonistic where the combined severity was less than that of the two events occurring independently and synergistic where it was greater. Krawchuk et al. (2020, p. 1) used neither term and wrote of overlap. "Forest disturbances often overlap, generating complex positive and negative relationships, or even feedbacks, that influence the structure and function of refugia."

## Linked effects

These studies asked whether a prior outbreak changed the severity of the fire that followed, which is the manuscript's objective 1.

| Key | Study | Design | Finding |
| --- | --- | --- | --- |
| `talucci2019dead` | Talucci and Krawchuk (2019), *Ecosphere*, mountain pine beetle, central interior British Columbia | 63 field plots across three fires of 2012 to 2014 in grey-phase lodgepole pine | "We found no evidence of a relationship between outbreak severity and fire severity for six of seven first-order fire effects, with the exception of deep charring" (p. 1) |
| not verified | Talucci (2019), doctoral thesis, 192 pages, held twice under two filenames | Field plots and a Landsat chapter modelling the probability of high burn severity | "intermediate levels of outbreak generate a fuel arrangement that supports the greatest probability of high severity fire on these landscapes" (p. 2) |
| `liang2016forest` | Liang et al. (2016), Southern Rocky Mountains, mountain pine beetle | Landsat time series, sequence contrast of beetle then fire against fire then beetle | "The severity of fire was unrelated to pre-fire outbreak severity, and no evidence of MPB mortality increasing fire occurrence was found" (p. 9) |
| `sieg2017fires` | Sieg et al. (2017), *Fire Ecology*, ponderosa pine, northern Arizona | Physics-based fire simulation (HIGRAD/FIRETEC) on fuel beds from 60 field plots, full factorial in outbreak phase, mortality and wind | Red-phase fires were more severe and synergistic. For grey-phase fires after moderate mortality, beetle-caused mortality "may buffer rather than exacerbate fire severity" (p. 3) |

The set agreed that the linked effect was small or absent in the grey phase, and Talucci and Krawchuk (2019, p. 1) attributed fire severity to "the interaction of fuels, weather, and topography during fire events". The manuscript's objective 1 result, a log-odds of 0.043 with an interval spanning zero, agreed with all four.

## Compound effects

These studies asked whether a prior outbreak changed what the fire left behind, which is the manuscript's objective 2.

| Key | Study | Response | Finding |
| --- | --- | --- | --- |
| `talucci2019drivers` | Talucci et al. (2019), *Forest Ecology and Management*, 83 plots, three fires, central interior British Columbia | Lodgepole pine seedling density, generalised linear models with ten candidate drivers | Recruitment followed fire severity and cone abundance. The thesis chapter states that "substantial underlying tree mortality from the MPB outbreaks did not play a role" (thesis p. 81) |
| `stevensrumann2015bark` | Stevens-Rumann et al. (2015), *Ecosphere*, dry mixed conifer, Idaho and western Montana | Seedling density and age, surface fuels, stand structure, in fire only, beetle only, and beetle then fire within 3 to 8 years | "there was no evidence that a beetle and wildfire interaction affected seedling densities" (p. 1) |
| `carlson2017` | Carlson et al. (2017), *PLOS ONE*, spruce beetle, West Fork Complex fire of 2013, Colorado | Landsat NDVI two years after fire, "sequential autoregressive (SAR) models" in the authors' words | "more severe spruce beetle outbreaks corresponding to reduced post-fire vegetation cover" (p. 1), stronger in red-stage than grey-stage locations |
| `liang2016forest` | Liang et al. (2016) | Area ratio of seedling reestablishment, no uncertainty reported | "Pre-fire beetle outbreaks and subsequent fire produced positive compound effects on seedling reestablishment in this ecoregion" (p. 1) |
| `talucci2020added` | Talucci et al. (2020), *Fire Ecology*, Oregon, three beetle-killed and three fire-killed snags | Pyrogenic carbon by the benzene polycarboxylic acid method | Beetle-killed snags held over five times the marker per kilogram of carbon, "pointing to an important compound effect from the interaction of beetle outbreak and wildfire" (p. 1) |
| `murphy2026` | Murphy et al. (2026), the parent study | Inhomogeneous point process model of seedlings, additive in beetle and fire | The model the follow-up refits |

Set against each other, the field studies of seedling density found no compound effect (Talucci, Stevens-Rumann), and the two positive results came from a spectral index of cover (Carlson) and an area ratio without uncertainty (Liang). The manuscript's null product term sat with the field studies. Carlson et al. (2017) is the comparison a referee is most likely to raise, because it used the same sensor and an autoregressive model of spatial dependence and found an effect.

## Fire before beetle

Two studies ran the sequence the other way. McHugh et al. (2003, p. 1) found that "several Dendroctonus and Ips species colonize fire-damaged ponderosa pines in northern Arizona and colonization is promoted by heavy crown damage from fire", and recorded mountain pine beetle on no trees at two of three fires. Lerch et al. (2016, `lerch2016mountain`) followed 1,173 lodgepole and 599 ponderosa pines for three years after fire in northeastern Utah, where beetle attack concentrated on fire-injured lodgepole pine at first and then moved to uninjured trees. Both bear on the manuscript's statement about the direction of cause.

## Frameworks and reviews

| Key | Work | Use |
| --- | --- | --- |
| `krawchuk2020disturbance` | Krawchuk et al. (2020), disturbance refugia within mosaics of fire, drought and insect outbreak | The refugia framework, and the feedback by which beetle-killed seed trees could slow recovery after fire |
| `gough2024disturbance` | Gough et al. (2024), *Ecology and Evolution*, a viewpoint with no data, source note held | Press and pulse disturbance, thresholds, and that disturbance does not always reduce function |
| `stevensrumann2019tree` | Stevens-Rumann and Morgan (2019), *Fire Ecology*, review of tree regeneration after fire in the western United States | Drivers of seedling density, seed source distance first among them |
| `harvey2018disturbance` | Harvey et al. (2018), wildfire and western spruce budworm in interior British Columbia, source note held | Fire and budworm histories set against climate at eight sites, a different question from whether one disturbance changes the other |
| not verified | Swift et al. (2012), successional responses to disturbance in British Columbia | Regional successional pathways after single and combined disturbances |
| `cartwright2018` | Cartwright (2018), topoedaphic refugia from drought and insects in lodgepole pine, source note held | Terrain as the source of refugia |

## Detection limits

Rodman et al. (2021, `rodman2021disturbance`, p. 1) found that LandTrendr detected wildfire more accurately than spruce beetle mortality, and that "prior spruce beetle outbreaks did not influence the detectability of subsequent wildfire". Meigs et al. (2011, `meigs2011landsat`) related Landsat spectral trajectories to field measures of mortality and fuels, and the store held only its abstract, 2,834 characters. Lentile et al. (2006, `lentile2006`, source note held) set out the distinction between fire intensity, fire severity and burn severity. Perrakis and Zell (2008, not verified) piloted remote burn severity assessment, and Meddens et al. (2012, not verified, catalogued under a junk title) mapped bark beetle mortality across British Columbia and the western United States.

## Spatial inference

These are not compound disturbance studies. They are the methods neighbours of the manuscript's transferable result, that clustered seedlings counted as independent observations give intervals that are too narrow. McIntire and Fortin (2006, `jbmcintire2006structure`, p. 6) stated the problem for fire and beetle boundaries in British Columbia. "because of lack of independence of data points, the effective degrees of freedom is less than the number of sample plots, thereby reducing the power of the statistical tests". Malone et al. (2018, `malone2018mixed`, p. 1) reported that "Post-fire regenerating conifers, which ranged in density from 241 to 1036 TPH, were also clustered at distances up to at least 30 m". Ziegler et al. (2017, `ziegler2017tree`, p. 1) "found that all species were spatially aggregated". Mathys et al. (2018, `mathys2018diverging`, p. 1) separated the life stages the two objectives act on. "Small changes in temperature and precipitation impact seedlings more than adult trees, whereas the opposite is the case with bark beetles and wind storms."

## Peripheral holdings

Ray et al. (2019) compared woodboring beetles after fire and after bark beetle outbreak in California. Frank et al. (2026), held under the filename "James et al 2026 Disturbance regimes shifting in Oregon", compared ground beetles after clearcut and after stand-replacing fire. Vore et al. (2020) related climate, fire seasons, mountain pine beetle and runoff in large British Columbia watersheds. Perbet et al. (2024) classified boreal disturbance types from Landsat subsequences. Taylor and Carroll (2003, not verified) was a conference paper on disturbance, forest age and mountain pine beetle outbreak dynamics in British Columbia. None tested a linked or compound effect.

## Not held

`references-compound.bib` cites seven works on this subject that the store did not hold in any form on 20 September 2026, by author search of the manifest and by the full text pass. They are Paine et al. (1998), Simard et al. (2011), Harvey et al. (2014), Hart et al. (2015), Kulakowski and Veblen (2006), Jenkins et al. (2012) and Stevens-Rumann et al. (2016). Paine et al. (1998) and Simard et al. (2011) are the sources of the field's two definitions, and Harvey et al. (2014) is the lodgepole pine regeneration result that both Liang et al. (2016) and Krawchuk et al. (2020) cite. Buma and Wessman (2011) and Johnstone et al. (2010), which Liang et al. (2016) cite for compound effects on regeneration, were not held either.

Later on 20 September 2026 eight of these nine were supplied, verified at CrossRef and given source notes, all but Stevens-Rumann et al. (2016). What the sixteen noted studies found, set against this manuscript's findings, is in `compound-disturbance-synthesis.md`.

## Store records

Of the 9 central studies, only `carlson2017` and `murphy2026` had a source note, and the Carlson note covered its plot protocol, not its compound effect finding. The Talucci thesis was held as two files of 192 pages with different checksums, neither verified nor keyed. The sentence that `05.tasks/LITERATURE-REFRAME-2026-09-03.md` and the manuscript quote from Ziegler et al. (2017, p. 6), "All species had aggregated spatial patterns, with aggregation greatest at smaller scales", is in the paper. A string check on 20 September 2026 failed to find it because the text layer of the held PDF prints each word of that passage twice ("had had aggregated aggregatedspatial spatialpatterns"), so a quotation from that page has to be checked by eye.
