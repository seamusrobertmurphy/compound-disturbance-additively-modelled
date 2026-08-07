# TASK-REQUEST-2026-08-07

Next steps for the follow-up manuscript to Murphy et al. (2026), written after the
Forest Ecology and Management retarget of 6 August. The manuscript is complete and
renders clean with every assertion gating. What remains divides into three kinds:
decisions only the authors can make, analysis that would strengthen the paper against
the referee questions it invites, and production work for the submission portal.

Work the sections in order. The decisions gate submission and some of them gate the
analysis. Nothing in the analysis section is required for the paper to be correct;
each item answers a question a referee is likely to ask.

Target journal: Forest Ecology and Management (Elsevier), Regular paper. Single
anonymized review. Framing unchanged from the previous request and repeated here
because it governs several items below: this is a methodologically driven follow-up,
not a correction of the parent study. The parent's additive model was the defensible
modelling choice and this paper confirms it. Present every point as an extension of
the discussion the parent opened, never as a fault located in it.

## Priority 0: Decisions that gate submission

1. **Verify the live Forest Ecology and Management guide for authors in a browser.**
   ScienceDirect blocked every automated route tried on 6 August: the guide page
   returned 403 or a robot-check redirect via direct fetch, four public proxies, two
   search-engine user agents, and Wayback Save Page Now. There are no Wayback captures
   of the current page. Everything journal-specific now in the manuscript rests on a
   capture dated 1 February 2022, four years old. Open
   `https://www.sciencedirect.com/journal/forest-ecology-and-management/publish/guide-for-authors`
   and confirm four things: whether any word or length limit now exists for regular
   papers, whether a keyword count has been added, the exact heading the journal uses
   for the generative AI declaration, and that the article-type list still has no
   methods category. The 2022 text states no length limit of any kind, a 400-word
   abstract, and no short-communication category. **Do not submit on the strength of
   the archived text alone.**
   Acceptance: the four items confirmed against the live page, and any divergence from
   the archived text carried into the manuscript.

2. **Resolve the parent paper's co-authors.** Murphy et al. 2026 is Murphy, Leslie,
   Wilson and Banks. This manuscript is single-author, it re-analyses their data, and
   under single anonymized review the referees will see that the author is one of the
   authors of the study being extended. That helps if the co-authors have been brought
   in and hurts badly if they have not. This has been the top open item since 2 August
   and is still unresolved. Decide whether they are notified, whether any belong on
   this paper, and whether the editor should be told at submission. A co-author
   invitation was being drafted separately; finish it.
   Acceptance: every co-author has been contacted and their position recorded here.

3. **Settle what may be deposited, then write the data availability statement.** The
   statement currently promises deposit on acceptance with the identifier to follow.
   The obstacle is unchanged: the source rasters belong to the parent study and are not
   this author's alone to license. The executable `.qmd` and the derived inputs are a
   different matter and are the part that carries the paper's argument. A paper whose
   subject is reproducible inference should deposit what it can.
   Acceptance: the statement names what is deposited, where, and under what licence,
   with the rights question settled rather than deferred.

4. **Nominate four reviewers.** FEM requires four qualified reviewers with working email
   addresses at submission. Given item 2, none should be a co-author of the parent
   study. Candidates suggest themselves from the bibliography: the authors of the
   contested beetle-to-fire literature already cited, and anyone working on spatial
   inference for point processes in forest ecology.
   Acceptance: four names, affiliations and current email addresses.

5. **Decide whether to raise the parent study's internal inconsistencies, and if so
   where.** Reading the PDF against its own tables on 6 August turned up several
   divergences that are not currently mentioned anywhere in this manuscript, and were
   deliberately left out because the framing forbids anything that reads as an attack.
   They are recorded here so the decision is made knowingly rather than by omission.
   Table 9 gives Fire-high a coefficient of -0.6430 while Table 12 gives Fire-H as
   +0.207 pooled, and the Results prose describes intensity decreasing in high-severity
   areas. Several coefficients quoted in the Results and Discussion do not match Table
   12. The Wind coefficients are described as adverse in prose and are positive in the
   table for three of the four species named. One Fig. 6 panel is titled
   `mcarlo_999sim_pinus_albi` while the caption and every table say *Pinus monticola*.
   The abstract reports 3886 seedlings and the Methods and Fig. 4 caption report 3912.
   And the combined-disturbance claim is stated four times with a different mechanism
   each time, against a model that carries no term corresponding to it.
   **The recommendation is to raise none of them in this paper.** They are irrelevant
   to this paper's argument, which needs only that the published fit is additive and
   its standard errors are Poisson, and both are now demonstrated by reproduction. A
   list of errata reads as an attack on co-authors and would undermine the framing that
   makes this paper publishable. The right route is a note to the co-authors under item
   2 and, if warranted, a corrigendum to the parent, which is their decision and not
   this manuscript's business.
   Acceptance: an explicit decision recorded here, with reasons, either way.

## Priority 1: Analysis that answers the obvious referee questions

6. **Put a number on how much data the interaction test would need.** The Limitations
   section says that a larger or better distributed sample could return a different
   answer and that this study offers no estimate of how much larger. That is the first
   thing a referee will ask of a null result, and it is answerable. Compute a minimum
   detectable effect for the product terms at the observed dependence: fix the block
   structure and the residual correlation the correlogram measures, and simulate the
   power to detect a product coefficient of a given size as a function of plot area or
   number of plots. The answer converts the paper's central negative into a design
   recommendation, which is the form in which it will actually be used by anyone
   planning the next study.
   Acceptance: a stated minimum detectable effect at the observed extent, and the extent
   at which a coefficient of the size fitted here would be resolvable, both computed at
   render time.

7. **Test the product term per species, not only pooled.** The parent study fits one
   pooled model and seven per-species models. This paper refits the pooled one. The
   pooled null is the weaker claim, because an interaction present in lodgepole alone
   could be diluted by six species that show nothing, and lodgepole is 74 per cent of
   the stems and the species the parent's own combined-disturbance claim is about.
   Refit with product terms for lodgepole specifically and report it beside the pooled
   result. Expect the intervals to widen further on a smaller sample, which strengthens
   rather than weakens the conclusion, but it must be shown rather than assumed.
   Acceptance: a lodgepole-only refit reported with the same block bootstrap and
   sandwich treatment as the pooled fit.

8. **Fit the four-level severity specification as a robustness check.** The published
   model carries indicators for high and low severity only, so moderate severity is
   pooled with unclassified ground into a reference category that is 82 per cent
   moderate, the class carrying the most beetle attack. The manuscript
   reproduces this deliberately and says plainly that no fire coefficient means quite
   what its label says. That is honest but it leaves a referee free to ask whether the
   null product-term result is an artefact of the reference category. Fit severity as a
   four-level factor with a clean reference, add the product terms to that, and report
   whether the verdict changes. The prediction is that it does not and the intervals
   widen again.
   Acceptance: the alternative specification reported, with the verdict stated either
   way, and the published specification retained as the primary one.

9. **Add the spatstat `kppm` variance as a third estimate, if it is cheap.** The
   inference now rests on a block bootstrap and a cluster-robust sandwich, which agree
   at 1.8 to 5.5 against the naive Poisson but share the assumption that blocks are
   independent. Fitting the same trend as a cluster process in `spatstat` and taking
   its variance would break that shared assumption, because the dependence is then
   modelled rather than blocked around. This was suggested in the previous request and
   the sandwich was implemented instead, on the ground that it was cheaper and more
   directly comparable. Revisit only if it can be done without rebuilding the point
   pattern from scratch; the argument does not need it.
   Acceptance: either a third variance estimate reported, or a recorded decision that
   the cost is not worth it.

10. **Resolve the 68-cell divergence between the `tbl-crosscheck` and `tbl-host`
    frames.** Carried unchanged since 2 August. The two frames differ by 68 cells in the
    unclassified class with no explanation in the Methods. A `stopifnot` stops the
    divergence widening silently, which is containment rather than a fix. Either unify
    the frames or state the cause in the Methods. A referee who notices two cell counts
    for the same ground will not accept an assertion in place of an explanation.
    Acceptance: the frames unified, or the difference stated and its cause named.

11. **Close the 3,886 seedling question or say it is closed.** `Seedlings.shp` holds
    3,912 points and the seven-species filter leaves 3,866, which accounts for both
    counts in circulation. The parent's abstract and Results say 3886 while its own
    Methods and Fig. 4 caption say 3912, so the discrepancy is internal to the parent
    and not a disagreement with it. The manuscript currently reports that no filter
    reproduces 3,886. Confirm with the co-authors under item 2 and then either name the
    cause or state that it is unexplained and move on. Do not leave it as an open query
    in a submitted paper.
    Acceptance: the sentence in `sec-ppframe` either names the cause or states plainly
    that the count is unreconciled, with no implication of error.

## Priority 2: Production and portal requirements

12. **Convert `Highlights.md` to an editable file with "Highlights" in the name.** FEM
    requires highlights in a separate editable file uploaded to the submission system,
    not embedded in the manuscript. The five bullets are drafted and all sit within the
    85-character limit. Produce `Highlights.docx`.
    Acceptance: an editable Highlights file, three to five bullets, each within 85
    characters including spaces, verified by counting rather than by eye.

13. **Check the rendered docx against FEM's structural requirements.** Double spacing,
    continuous line numbering and single column are confirmed in the 6 August render.
    Three things are not: that figures and tables sit next to the relevant text rather
    than collected at the end, that each caption sits directly below its display item,
    and that sections are numbered 1, 1.1, 1.1.1 with the abstract outside the
    numbering. Open the docx and confirm all three.
    Acceptance: the three items confirmed, or the reference document adjusted until
    they are.

14. **Consider a graphical abstract.** Optional at FEM but encouraged, and this paper
    has an unusually good candidate: the same four product terms under the naive
    Poisson interval and under the block bootstrap, which is `fig-interaction` already.
    A cut-down version at 531 by 1328 pixels minimum would carry the whole argument.
    Acceptance: either a graphical abstract file, or a recorded decision to skip it.

15. **Decide what to do with the vendored Elsevier extension.** `_extensions/quarto-journals/elsevier`
    was recorded on 5 August as dead weight because CJFR had no Quarto template. The
    retarget makes it live again in principle, but it is a LaTeX `elsarticle` route and
    the submission is a Word file under Your Paper Your Way, so it is still not needed.
    Its bundled `elsevier-harvard.csl` is an older revision than the one now in
    `04.references/` and should not be used in preference to it. Remove the extension or
    record why it is being kept.
    Acceptance: removed, or a one-line note in `INDEX.md` saying why it stays.

16. **Commit the working tree.** Twenty-three changed or new files from the 6 August
    session are uncommitted, including the manuscript, the new reference files, the
    rebuilt README, and two new traps in `INDEX.md`. Commit before any further work so
    that the next change has a clean baseline to diff against.
    Acceptance: a clean `git status`, with the commit naming Seamus only.

## Already done (do not repeat)

The 6 August session cleared the whole of `TASK-REQUEST-2026-08-06_1.md`. In summary,
and with the numbers that changed:

The bootstrap runs at 2,000 replicates. The interval widening factor moved from 2.4 to
7.6 down to **2.3 to 5.9**, because the old upper end came from a term that six of
thirty-two term-by-block combinations could not identify in every draw. The usable-draw
count is restored to `tbl-ppblocks` and the widening factor is computed on fully
identified combinations only. No conclusion changed: every product term still spans
zero at every block size, and the moderate-severity peak still clears at all four,
weakest at 750 m with a lower bound of 0.019.

`error: false` is set. Under the previous `error: true` a failed assertion did not fail
the render, and in a chunk that also sets `output: false` it produced no signal at all,
which is how the abstract's 2.4 and 7.6 survived a refit that moved them. This is trap
18 in `INDEX.md` and is the reason the abstract's hard-coded quantities can now be
trusted.

The published standard errors are demonstrated, not inferred, to be naive Poisson
standard errors: `tbl-ppreproduce` sets the parent's own `Std.Error` column beside the
standard error implied by a weighted Poisson fit to the same design matrix, and they
agree to `0e+00` on all nine terms. A cluster-robust sandwich, validated against
`sandwich::vcovCL`, corroborates the bootstrap and leaves 0 of 8 product intervals
excluding zero. The asymmetry is stated: unmodelled dependence leaves intervals too
narrow, which is conservative for the negative result and adverse for the positive one.

The word "additive" appears nowhere in the parent; the paraphrase is replaced by two
verbatim quotations and the fitted term list, with the unused `beetle_fire_interactive/`
rasters noted. The parent reports Ripley's inhomogeneous K only, against a null of
non-constant intensity, and the "K and L functions" claim is corrected. The collinearity
argument now reports the binary host indicator the model actually fits, whose VIF of
1.38 disqualifies nothing, and names the 27-block effective sample size as the binding
constraint instead. Moran's I is computed rather than asserted, at 0.66. The AI
acknowledgement is replaced by an Elsevier-form declaration before the references.

Five tables converted to figures in `b0315a1` are restored beside their figures, giving
18 tables and 6 figures. Nothing else had been lost: the manuscript grew monotonically
across its history and the commit that appeared to cut 454 lines was a re-wrap.

FEM compliance: `elsevier-harvard.csl` verified to resolve all 22 references,
`style-elsevier-submission.docx` built with `BodyText` at true double spacing, and
`Highlights.md` drafted. There is no FEM word limit in the archived guide, so nothing
was trimmed and the body stands at 7,017 words.

## Notes for whoever picks this up

A full render is roughly 25 minutes at 2,000 replicates, and the point-process bootstrap
is nearly all of it. Budget for that before starting anything that needs a render to
verify, and prefer to batch changes into one render rather than iterating. If iteration
becomes painful, Quarto's `freeze` would help, but it must not be enabled for the render
that produces the submission file, because the paper's claim is that every number is
computed from the source data at render time.

Read `INDEX.md` before touching the analysis. Traps 18 and 19 were added on 6 August and
both concern silent failure in exactly the machinery this paper is about.
