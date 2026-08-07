# TASK-REQUEST-2026-08-06

Follow-up manuscript to Murphy et al. (2026). Consolidated next steps from two
review passes. Work the sections in order: the blockers gate submission, the
statistics can move reported numbers, the additions harden the argument, and the
compliance items are production fixes. A record of work already completed and the
open decisions for the authors follow at the end.

Target journal: Forest Ecology and Management (Elsevier), matching the parent
paper. The manuscript was drafted against CJFR conventions and must be retargeted
to Elsevier: citation style, reference document, and the AI declaration all change.
Those changes are folded into the tasks below.

Framing to preserve throughout: this is a methodologically driven follow-up, not a
correction of the parent study. The parent paper opened a line of discussion among
spatial modelers and ecologists about the limits of remote sensing in disturbance
ecology and how far inherited raster layers can carry a compound-disturbance analysis.
This paper runs the spatial-inference tests those discussions called for and reports
the additional findings that came out of them. The author is on both papers. Present
every point as an extension of that conversation and a contribution the shared dataset
made possible, never as a fault located in the parent. The parent's additive model was
the defensible modeling choice, and this paper confirms it: the data cannot support a
product term either way. Where the paper reports clustering-aware intervals, frame them
as a general methodological result measured on this dataset, not as a revision of the
parent's numbers. Nothing here revises the parent's ecology.

## First — restore the fuller drafts

Earlier drafts carried more of the outputs and results than the current version, which
was compressed in later passes. Restore those drafts from git history and recover the
fuller results and outputs, then carry the work below forward on the restored version
rather than the trimmed one. Reconcile rather than overwrite: bring back the substantive
tables, figures, and reported numbers that were cut, but keep the corrections already
made (see "Already done") intact. Note the tension with the word limit in task 14:
restoring outputs adds length while FEM caps it, so when trimming to fit, cut prose and
not findings.
Acceptance: the fuller outputs and results from the earlier drafts are back in the
working .qmd; the later fixes (citations, assertions, corrected numbers) are preserved;
no regression introduced by the restore.

## Priority 0 — Blockers (must clear before submission)

1. Remove the parent misquote and quote the parent directly.
   The manuscript says twice, in the Introduction and again in the Discussion,
   that the parent's abstract "describes the additive effects of increasing beetle
   to fire disturbance interactions." The word "additive" appears nowhere in Murphy
   et al. 2026. Replace the paraphrase with the parent's real words, which are the
   stronger premise. The abstract says "Inhomogeneous Cox process models showed that
   areas of overlapping beetle mortality and high burn severity had significantly
   reduced lodgepole pine regeneration." The conclusions say the results suggest
   "the ecological consequences of beetle-fire interactions weaken as surface fuels
   decay over time." Both are joint-condition claims read off additive main effects.
   Support the point with the model terms as fitted: SS_dist, Aspect, RIX, Wind,
   MPB_G, MPB_R, Fire_H, Fire_L, with no product term and no overlap indicator in
   the pooled fit or any of the seven per-species fits. Note the unused intersection
   layer beetle_fire_interactive/mpbred_firehigh.tif, built and entered into no model.
   Acceptance: no occurrence of "additive" attributed to the parent as a quotation;
   the premise rests on verbatim parent text plus the fitted term list.

2. Rewrite the AI acknowledgement to be true.
   Current text: "No generative artificial intelligence was used to produce the
   scientific content, the analysis or the results of this manuscript." The
   repository contradicts it: 05.tasks/progress.md records running /simplify and
   four review agents over the .qmd, logs a quantity the agent measured as agreeing
   to 1.7e-16, and the project ran through Claude Code sessions from
   TASK-REQUEST-2026-08-02.md. Elsevier requires a Declaration of Generative AI in
   Scientific Writing, given as a dedicated statement placed before the reference list.
   Replace the denial with a truthful declaration in that form: every scientific
   judgement was the authors', and generative AI was used as an analysis and drafting
   tool.
   Acceptance: a Declaration of Generative AI section sits before References and
   discloses AI use; no sentence anywhere denies it.

3. Fix `error: true` and re-render so assertions actually gate.
   Under `error: true`, a failed stopifnot prints a red error block, execution
   continues, and Quarto exits successfully. The manuscript claims the opposite in
   four places ("the assertion above fails the render if they ever stop agreeing").
   The progress log recorded this on 5 August; the YAML was never changed. No
   assertion is currently failing, so nothing published is wrong, but the advertised
   reproducibility guarantee does not exist. Set `error: false` and re-render.
   Acceptance: `error: false` in YAML; clean render with all assertions passing;
   deliberately breaking one assertion fails the render (verify once, then revert).

## Priority 1 — Statistics that could move the reported numbers

4. Raise B_BOOT from 400 to at least 2,000 and re-read the sweep.
   Three conclusions sit within about one Monte Carlo standard error of flipping:
   the moderate-against-low lower bound at 750 m at 0.020, Fire_L at 100 m at 0.001,
   MPB_R at 100 m at -0.027. The MC standard error on a percentile endpoint at
   B = 400 is roughly 0.023 in log-odds. Re-verify "clears at all four block sizes"
   and "two main effects survive" after the increase.

5. Repair the degenerate 100 m point-process bootstrap.
   This run supplies the headline widening factor. The four product cells rest on
   54 to 70 quadrature points each, so a resample omitting the blocks holding them
   leaves the term unidentified, glm.fit returns NA, pfit passes it through because
   it checks only convergence, and na.rm = TRUE discards the draw silently. Surviving
   heavy-tailed draws set the percentiles, and the 7.59 upper end of "2.4 to 7.6"
   comes from exactly that term at that block size. Restore the Usable count computed
   in pp_boot and dropped by the transmute, and surface it so degenerate resamples
   are visible rather than silently averaged.
   Acceptance: Usable count reported per block size; the widening factor recomputed
   on identified resamples only.

6. Fix the collinearity argument.
   It reports cor(FR$pl, FR$elev), the correlation of continuous lodgepole percentage
   with elevation, but the model fits binary host, so r = 0.52 is not the regressor's
   correlation and implies a VIF of about 1.37, not disqualifying at n = 5,413.
   Replace with the real reason host spans zero: an effective sample size of 27 blocks.

7. Resolve the Moran's I claim in sec-blocks.
   "Moran's I on the response is high" is asserted and computed nowhere. Either
   compute it and report the value, or drop the sentence.

## Priority 2 — Cheap additions that harden the argument

8. Add a standard-error column to tbl-ppreproduce.
   The paper asserts the published SEs are naive Poisson but never shows it. The
   parent's refit is sm.GLM(y, X, family=Poisson(), freq_weights=w).fit() reporting
   res.bse, with no cluster-robust or Cox variance component. The coefficients already
   reproduce exactly; adding the SE column turns the central premise from an inference
   about method into a reproduction.

9. State the Cox-versus-Poisson point directly.
   The parent's Methods say "an inhomogeneous, locally weighted Cox process model was
   fitted," its table is named Table12_LGCP_coefficients, yet the implementation
   reports Poisson standard errors. This is the cleanest statement of the finding,
   with the nuance you want: estimating a Cox trend by the Poisson composite
   likelihood is legitimate; only the variance is not.

10. Add a second variance check and state the asymmetry.
    The inference rests on one method with 14 to 36 blocks, below the percentile
    method's reliable floor in the cluster-bootstrap literature. Add a check referees
    already trust, kppm with vcov in spatstat or a cluster-robust sandwich, to
    corroborate the block bootstrap. State the asymmetry in your favour: too-narrow
    intervals make the null product-term result more robust and the positive
    moderate-severity result less so.

11. Correct the description of the parent's spatial diagnostics.
    The manuscript says the parent reported "inhomogeneous K and L functions with
    999-simulation envelopes that show the seedling pattern clustered at every distance
    examined." The parent used Ripley's K only, against a null of non-constant
    intensity, with goodness-of-fit over 0 to 15 m; its Fig. 5 caption reads "patterns
    of dispersion and clustering below and above the null model in each plot." Its
    abstract does claim significant clustering for all species. The argument survives
    either way, since any departure from independence breaks the Poisson SEs and the
    correlogram is the direct evidence, but the sentence must be accurate.

## Priority 3 — Forest Ecology and Management compliance and production

12. Switch the citation style from CJFR to Elsevier.
    The qmd currently uses cjfr.csl. Replace it with the Elsevier reference style FEM
    uses (elsevier-harvard.csl, the numbered-name Elsevier "Harvard" style), and
    re-render so every in-text citation and the reference list reformat. Confirm the
    @page2012 / Jenkins et al. 2012 entry and all twenty-one references still resolve
    cleanly under the new style.
    Acceptance: no cjfr.csl reference in the qmd; references render in Elsevier style
    with no unresolved keys.

13. Fix the reference document and body spacing.
    The qmd wires style-formal.docx, not the submission reference doc, and neither
    produces double-spaced body text: both give 1.5 because the BodyText style sets
    w:line="360", overriding the double-spaced docDefaults. Point the qmd at an
    Elsevier/FEM submission reference doc and set BodyText to true double spacing
    (w:line="480", lineRule auto); Elsevier expects double-spaced submissions. Line
    numbering, single column, and page numbers are already fine. Before re-rendering,
    resolve the Word conflict: the tracked docx has been opened and saved in Word, is
    190 KB larger than the committed version, and has a lock file beside it, so a
    render will destroy any Word markup. Reconcile or discard that copy first.

14. Bring the manuscript within the FEM word limit, and confirm article type.
    Forest Ecology and Management now imposes a word limit on research papers. Confirm
    the current figure in the FEM guide for authors [PLACEHOLDER — insert the limit,
    e.g. 8,000 words; verify before relying on it] and note what it excludes (typically
    abstract, references, tables, and figure captions). The body currently runs 5,965
    words from Introduction through Discussion, 6,276 with the Conclusions folded in,
    so once the fuller drafts are restored the manuscript will likely exceed the cap
    and need trimming. Trim prose, not results: protect the restored outputs and cut
    length elsewhere. FEM has no dedicated Methods Paper type, unlike CJFR, so submit
    as a Research Paper (or a Short Communication only if it comes in short). Elsevier
    accepts flexible "your paper your way" formatting at first submission. Current
    inventory is twelve tables, six figures, all main text, no supplementary split,
    and twenty-one references, all cited. Verify all current requirements against the
    FEM guide for authors before submitting.
    Acceptance: manuscript word count is within the confirmed FEM limit on its counted
    sections, with results preserved.

## Already done (do not repeat)

The abstract was rewritten to close on the findings and the answer, runs 196 words
(verified by parsing the YAML), and now carries numbers: 0.416 in log-odds for the
conditioned moderate-severity peak, intervals 2.4 to 7.6 times wider, and not one of
sixteen product-term intervals excluding zero. Because the abstract lives in YAML where
inline R does not run, a stopifnot was added in pp-verdict asserting all five quantities
against the computed values, so a refit that moves any of them cannot leave the abstract
silently contradicting the results. That guard only becomes real once task 3 is done.
A dangling @page2012 citation rendering as "(page2012?)" was fixed with a CrossRef-verified
Jenkins et al. 2012 entry and a corrected key. "Fourteen envelope simulations" was
corrected to 999. The submission variant was regenerated in sync and re-rendered to HTML
only, so the open docx was left untouched. Current render: zero R errors, five assertions
passing against live data.

Note the coupling: the abstract's 2.4 and 7.6 depend on tasks 4 and 5. When B_BOOT rises
and the 100 m run is repaired, those numbers will move; the pp-verdict assertion will
catch it and fail loudly once task 3 is complete.

## Still open — decisions for the authors

The parent paper's co-authors have not been told. This is the item most likely to cause
trouble late and should be resolved before submission (a co-author invitation is being
drafted separately). The 68-cell divergence between the tbl-crosscheck and tbl-host frames
is still unexplained in the Methods and needs either a reconciliation or a stated cause.
