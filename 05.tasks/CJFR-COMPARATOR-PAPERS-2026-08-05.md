# Comparator papers in the Canadian Journal of Forest Research

**Date:** 5 August 2026
**Purpose:** benchmark this manuscript against what CJFR actually publishes on beetle and fire
disturbance, burn severity and post-disturbance regeneration, to inform the final revisions.
**Related:** `CJFR-GUIDELINES-VERIFIED-2026-08-05.md` for the venue's own rules.

## How this set was assembled, and what could not be read

Candidates came from the CrossRef REST API filtered to the journal's ISSN, searched on eight topic
strings and screened by relevance. Fifteen papers were retained. Metadata below is from the
publisher's own deposited CrossRef record, which is a stronger source than a PDF header for
pagination and reference counts.

**Six of the sixteen could be read in full; the rest are abstract only.** CJFR is a subscription
journal, `cdnsciencepub.com` returns HTTP 403 to automated fetches, and the article landing pages
expose the abstract and nothing else. Open copies were located through Unpaywall and Semantic
Scholar.

| Read in full | Version | Pages |
|---|---|---:|
| Estabrook et al. 2025 | published, typeset | 20 |
| Page et al. 2012 | published, typeset | 17 |
| Donato et al. 2009 | published, typeset | 16 |
| Meyer et al. 2016 | published, typeset | 11 |
| Stevens-Rumann et al. 2016 | author manuscript | 42 double-spaced |
| Dhar et al. 2016 | author manuscript | 51 double-spaced |

The four typeset versions are the useful ones for layout, because an author manuscript shows the
submitted structure rather than the published one.

For the remaining ten only the abstract and the CrossRef metadata were available. **Statements about
their internal structure are inferences from page counts and abstracts, not observations.** Anything
resting on their full text should be checked against a library copy.

## Float profile, and the clearest design finding

Counted from the four typeset papers.

| Paper | Pages | Figures | Tables | Total floats |
|---|---:|---:|---:|---:|
| Estabrook 2025 | 20 | 9 | 4 | 13 |
| Page 2012 | 17 | 7 | 6 | 13 |
| Donato 2009 | 16 | 6 | 6 | 12 |
| Meyer 2016 | 11 | 5 | 2 | 7 |
| **This manuscript** | **-** | **2** | **16** | **18** |

**The float profile is backwards.** These papers run roughly five to nine figures against two to six
tables, and this manuscript runs two figures against sixteen tables. The total, eighteen, is also
above every comparator. This is a more specific instruction than "split some tables into
supplementary": several of the tables should become figures, because that is how this journal
presents quantitative results.

The natural conversions are the ones where the table is really a set of estimates with intervals.
`tbl-ppblocks` and `tbl-blocks`, the two block-bootstrap sweeps, are coefficient plots waiting to
happen: term on the vertical axis, estimate and interval on the horizontal, panelled by block size,
with a line at zero. The whole argument of the paper is visible in one such figure and is currently
spread over thirty-two table rows. `tbl-ppcorr` and `tbl-correlogram` are correlograms and should be
drawn as one. `tbl-withinburn`, three records agreeing on a severity gradient, is a three-series
point plot. That is four figures gained and five tables lost, which lands the manuscript at six
figures and eleven tables, inside the comparator range on both counts.

## The comparator set

| Year | First author | Pages | Refs | Authors | Topic |
|---|---|---:|---:|---:|---|
| 2005 | Bonnet | 11 | 29 | 3 | Spatial pattern of post-fire ponderosa pine regeneration |
| 2006 | Kulakowski | 9 | 31 | 2 | Fire history and susceptibility to spruce beetle outbreak |
| 2008 | Nigh | 11 | 41 | 3 | Advance regeneration in beetle-killed lodgepole stands, BC |
| 2009 | Donato | 16 | 46 | 6 | Conifer regeneration in a mixed-severity wildfire |
| 2012 | Page | 17 | 53 | 3 | Beetle attack alters lodgepole foliage flammability |
| 2014 | Bansal | 10 | 44 | 4 | Interactive effects of burn severity and canopy on seedlings |
| 2015 | Alfaro | 10 | 19 | 3 | Forest legacies after two beetle outbreaks, BC |
| 2015 | Campbell | 11 | 48 | 2 | Advance regeneration after the beetle outbreak, BC |
| 2016 | Meyer | 10 | 32 | 4 | Beetle mortality, structure and regeneration, whitebark pine |
| 2016 | Dhar | 13 | 130 | 3 | Beetle outbreak and ecosystem services, western Canada |
| 2016 | Stevens-Rumann | 11 | 46 | 4 | Prior wildfire influence on subsequent burn severity |
| 2017 | Magnussen | 10 | 74 | ? | Estimating residual spatial autocorrelation from inventory data |
| 2023 | Wikle | 14 | 115 | 2 | Stand spatial structure under adaptation treatments |
| 2023 | Affleck | 15 | 30 | 2 | Model-assisted estimation of post-fire regeneration |
| 2025 | Estabrook | 20 | 76 | 5 | Burn severity from pre-fire structure and weather |
| 2025 | Stevens-Rumann | 22 | 96 | 4 | Burn severity, treatments and day of burning, Colorado |

Median 11 published pages (range 9 to 22) and **46 references** (range 19 to 130). The four papers
from 2020 onward run 14, 15, 20 and 22 pages with 115, 30, 76 and 96 references, so the journal's
recent output is longer and more heavily referenced than its older output.

The split is by paper type rather than by date. Conventional field studies run 9 to 11 pages;
method-heavy or landscape-scale papers run 15 to 22. **This manuscript is the second kind**, so the
target to aim at is roughly 18 to 22 pages and 70 to 95 references, not the set median.

## Where this manuscript sits

| Measure | This manuscript | Comparator median | Verdict |
|---|---:|---:|---|
| Body words, Introduction to Conclusions | 5,600 | not measurable from metadata | within the 6,000 limit |
| References in the bibliography | 13 | 46 | **far below every paper in the set** |
| Works actually cited in the prose | 9 | 46 | **the real number, and it is the problem** |
| Tables | 16 | not measurable | high |
| Figures | 2 | not measurable | low |

**The citation count is the most exposed feature of this manuscript.** Nine cited works against a
comparator median of 46, and against a journal limit of 50 that leaves ample room. The least
referenced paper in the whole set carries 19. Four entries sit in `references-compound.bib` uncited:
`rodman2021`, `meddens2012`, `wulder2006red` and `safranyik2006`.

The specific hole is in the Introduction, which asserts that "the literature on the question is
contested rather than empty" and then cites nobody for the contest. A referee will stop there.

## Candidates to cite, all in this journal

Citing the venue's own literature is not flattery, it is how a paper demonstrates it belongs there.
Every one of these is directly relevant and none is currently cited.

1. **Stevens-Rumann et al. 2016**, `10.1139/cjfr-2016-0185`. The closest structural analogue in the
   journal: whether a prior disturbance influences the severity of a subsequent fire, across four
   large fires including one in British Columbia. Cite in the Introduction for the question's
   pedigree and in the Discussion for how the analogous result was framed.
2. **Kulakowski and Veblen 2006**, `10.1139/x06-182`. Compound disturbance with the arrow reversed,
   fire history conditioning susceptibility to a spruce beetle outbreak. Useful precisely because it
   runs the other way and so frames the directionality argument.
3. **Page et al. 2012**, `10.1139/x2012-094`. Quantifies the fuel and flammability change that the
   beetle-to-fire mechanism assumes. The Introduction currently asserts the mechanism through two
   non-CJFR citations; this is the measurement behind it.
4. **Bansal et al. 2014**, `10.1139/cjfr-2014-0112`. "Interactive effects" of burn severity and
   canopy on seedlings, tested in a full factorial. The nearest thing in the journal to this paper's
   Question B, and a useful contrast: a designed factorial can resolve an interaction where an
   observational 12.69 ha cannot.
5. **Magnussen et al. 2017**, `10.1139/cjfr-2017-0247`. **The most valuable of the set for the
   Discussion.** It reports that variance estimators "may seriously underestimate uncertainty, and
   confidence intervals may be too narrow" when a model omits residual spatial autocorrelation. That
   is this paper's central finding, in this journal, eight years earlier, in a different corner of
   forest science. It converts our result from an isolated complaint into an instance of a known
   problem the journal has already published on.
6. **Bonnet et al. 2005**, `10.1139/x04-157`. Spatial pattern of post-fire conifer regeneration,
   102 citations. Establishes that CJFR publishes point-pattern regeneration work, which is the
   precedent Question B needs.
7. **Campbell and Antos 2015** `10.1139/cjfr-2015-0104`, **Nigh et al. 2008** `10.1139/x08-117`, and
   **Alfaro et al. 2015** `10.1139/cjfr-2015-0042`. Beetle-affected regeneration in British Columbia.
   The study area section currently cites only the parent paper for its own landscape.
8. **Donato et al. 2009**, `10.1139/x09-016`. Conifer regeneration in a large mixed-severity fire,
   135 citations, and the standard reference for seed-source distance controlling regeneration. The
   parent model's strongest predictor is seed-source distance and it is currently uncited.
9. **Dhar et al. 2016**, `10.1139/cjfr-2016-0137`. Beetle outbreak consequences across western
   Canada. Useful for the opening paragraph's claim about the scale of overlap.

Adding these takes the count from 9 to about 20. With the contested beetle-to-fire literature the
task request already flags as missing, Harvey, Hart and Simard, the manuscript would land near 25,
which is defensible even if still below the median.

## Analytical conventions in this journal

Read from the full texts, chiefly Estabrook et al. 2025, which is the journal's most recent
burn-severity paper and therefore the best guide to what a referee will expect.

**The response.** Burn severity is a remotely sensed index, and RdNBR dominates: Estabrook uses a
plot-mean RdNBR, binarised to high against not-high. Both 2025 papers work from "remotely sensed
burn severity" rather than field CBI, and validate against CBI where they can. This matters for us:
our classified five-code severity surface is coarser than what the journal now publishes, and
@sec-decode's finding that the codes are not in severity order should be presented as a data-quality
result rather than glossed.

**The model.** Logistic regression on a binary severity outcome, with model selection by corrected
Akaike information criterion and multi-model averaging following Anderson and Burnham. Predictor
subsets are structured in advance to control collinearity, and there is an explicit observations-per-
parameter rule, at least fifteen, cited to Harrell. Goodness of fit is reported as cross-validated
area under the ROC curve from five folds, using named R packages. Estabrook reports AUC of 0.72 to
0.73 as the headline and uses p-values only in one box-plot figure.

**Spatial dependence.** This is the important one. Estabrook measures "spatial autocorrelation ... by
calculating global Moran's I on the map of residuals" and tests sensitivity to grain. Stevens-Rumann
et al. 2016 go further and fit by sequential autoregression precisely because burn-severity pixels
are not independent. So the journal's convention is to **diagnose** residual autocorrelation as a
matter of course, and sometimes to model it.

**What this means for our positioning.** The block bootstrap is not exotic here and should not be
introduced apologetically. It is the next step along a path the journal is already on: Estabrook
diagnoses residual autocorrelation and reports it, and we propagate it into the intervals. The
sentence to write is that diagnosing dependence and then reporting independence-based intervals
leaves the diagnosis doing no work. Magnussen et al. 2017, in this journal, already showed that
omitting residual spatial autocorrelation makes confidence intervals too narrow; our contribution is
to show what that costs a published compound-disturbance claim.

Our Phase 1 analysis is a binomial GLM, the same family Estabrook uses, which helps. Our Phase 2
analysis is a weighted Poisson fit of a point-process trend, which is less common in this journal,
so @sec-ppframe should explain the Berman-Turner device briefly rather than assume it.

**Effect sizes over p-values.** Both recent papers lead with discrimination or effect estimates
rather than significance. Our decision to report no naive p-value anywhere is aligned with where the
journal is going, not against it, and the Discussion can say so.

## The anatomy of the closest analogue

Stevens-Rumann et al. 2016 was read in full. It asks our Question A with fire in place of beetle:
does a prior disturbance change the severity of the fire that follows. Its shape is the best
available template.

| Section | Their words | Their share | This manuscript | Our share |
|---|---:|---:|---:|---:|
| Introduction | 930 | 15% | 442 | 8% |
| Methods | 2,040 | 34% | 622 (Materials) | 11% |
| Results | 900 | 15% | 2,797 (three analysis sections) | 50% |
| Discussion | 1,660 | 28% | 1,424 | 25% |
| Conclusions | 500 | 8% | 315 | 6% |
| **Main text** | **6,030** | | **5,600** | |

Totals are close. The distribution is not, and two differences matter.

**Our Introduction is half the size it should be.** 442 words against 930, and four cited works
against their fifty references. This is the same defect as the citation gap seen from another angle,
and one edit fixes both: take the Introduction to roughly 900 words and to about fifteen citations,
using the CJFR papers listed above. That is the single highest-value revision available.

**Their Methods is twice their Results; ours is the reverse.** That is largely an artefact of the
executable format, which interleaves method and result in the same section rather than separating
them, and it is defensible. But it means a referee looking for a Methods section will not find one.
The three analysis sections should carry enough signposting that the methodological choices are
findable, and @sec-ppframe in particular should read as Methods.

Four further observations that bear on our revisions.

**They report naive p-values, and we do not.** Their coefficient table is a wall of values below
0.0001 computed at sample sizes up to 975,414, and they half acknowledge the problem by noting that
significance was decoupled from model inclusion. Their actual selection rule is a hard difference in
AIC of 50, stated once without justification. There are no confidence intervals anywhere in the
paper. **Our reporting standard is above the one this journal accepted for the closest comparable
paper**, and the Discussion should say so plainly rather than apologetically.

**They never fit an interaction.** Their substitute is a stratified two-variable submodel, which is
why their contradictory result on one of the four fires is left unresolved. A paper that fits the
product term directly has a clean, statable advance, and that sentence belongs in our Introduction.

**The compound-disturbance literature is open ground here.** Their framing is self-regulation,
ecological memory and top-down versus bottom-up control. The phrase "compound disturbance" does not
appear, Paine et al. 1998 is not cited, and their term of art is "fire on fire interactions". So the
cross-agent framing this manuscript uses is not competing with an established house style; it is
filling a gap, and can be introduced as such.

**The trap they fell into, which we must not.** The reburned fraction is a small minority of their
modelled pixels, and the paper gives two irreconcilable figures for it, 15 per cent in the abstract
and "roughly 3 per cent" in the discussion. Sample sizes are reported for the whole landscape, so a
reader cannot tell how much data supports the headline contrast. **Report the stratum sizes
explicitly.** @tbl-ppsupport already does this for the point process and is, on this evidence, one of
the manuscript's stronger features rather than a candidate for supplementary.

**Their abstract is 195 words and nine sentences**, containing no coefficient, no interval, no sample
size and no p-value. Its only numbers are the scale of the study system. Results are stated
qualitatively with one directional word and one differentiating phrase. Ours must fall from 323 words
to 200, and this is the model for how.

## Five findings from the wider set that change what we should write

Four further full texts were obtained from US Forest Service repositories, which none of the open
access aggregators index: Page 2012, Donato 2009, Meyer 2016 and Estabrook 2025. Unpaywall, OpenAlex
and Semantic Scholar all report these as closed, so agency repositories are worth checking directly
whenever a paper has a federal co-author.

**1. Nothing in this journal fits a spatial point process, so ours needs more scaffolding than we
have given it.** The closest antecedents are Donato's nearest-neighbour spatial C-statistic and
Campbell and Antos's occupancy of 5 m by 5 m subplots, both of which are quadrat or distance
summaries that a point process subsumes. @sec-ppframe currently explains the Berman-Turner device in
two sentences and assumes the reader knows what a quadrature scheme is. It should not.
**Consider also reporting a conventional density regression alongside the point process**, showing
the two agree, because a referee here will have no prior for the unfamiliar one and every reason to
trust the familiar one.

**2. Donato et al. 2009 declined to fit interaction terms, in this journal, for our exact reason.**
Their sentence is that models with more than five predictors or with interaction terms "were excluded
from analysis because of modest sample size". That is a highly cited CJFR paper reaching our
conclusion by judgement where we reach it by measurement. **It belongs in the Discussion.** It turns
our result from a complaint about one published model into the demonstration of a caution the
journal's own literature already exercises.

**3. Interaction language is granted conditionally here and we should match the register.** Designed
factorials get it outright, which is how Bansal et al. 2014 can speak of interactive effects.
Observational regressions mostly decline it: Estabrook et al. say severity is "contingent on weather"
in the abstract and then fit weather as main effects only. The manuscript should say that the product
term is or is not retained, and what its interval covers, rather than that beetle and fire do or do
not interact. Our Conclusions currently do this well; the Introduction is looser.

**4. Every comparator states how it dated the prior disturbance, and we do not.** Kulakowski and
Veblen reconstruct outbreak timing from growth releases in surviving non-host trees. Meyer et al.
rebuild pre-attack stand structure by adding trees dead seven years or less back into the live tally.
Estabrook et al. discuss at length how the remeasurement lag in the inventory degrades their pre-fire
condition. **We have no equivalent statement.** The outbreak window is 2005 to 2014 and the fire is
2015, the annual classifications are the dating instrument, and @sec-perimeter already establishes
that two of those annual files use an unrelated code set. A short passage in Materials on how
precisely beetle state is dated, and how much drift a one to eleven year interval admits, closes an
obvious referee question.

**5. A negative applied result is publishable here, and recently was.** Estabrook et al. 2025 report
an AUC of 0.72 to 0.73 as an acceptable severity model and are then candid that the mapped
application failed, at 55.9 per cent accuracy with residual Moran's I of about 0.78. That passed
review in this journal this year. It is both a calibration for what counts as adequate performance
and a licence for our own negative results to be stated plainly rather than buried.

One further note on their method, because it bears on our framing: among the six predictors Estabrook
retained is **basal area of standing dead trees**. The beetle-to-fire pathway is already in the
journal's recent burn-severity literature, carried as a stand-structure covariate rather than as a
disturbance history. Our framing should acknowledge that rather than present the link as unexamined.

## The article type question, settled by observation

CJFR runs an active Comment and Discussion-Reply exchange: Duchesne and Ouimet 2011, Klein et al.
2011, Williamson and Nelson 2018, Battles et al. 2019 and Gray et al. 2025 are all replies to
comments or discussions of papers published in the journal. This confirms the machinery is live and
also confirms it is used the way the guidelines describe, for papers published *in CJFR*. It is not
available to us and the Research article route stands.
